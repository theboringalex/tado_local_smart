{\rtf1\ansi\ansicpg1252\cocoartf2867
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 """Coordinator for Tado Local Smart Control."""\
import logging\
import datetime\
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator\
from homeassistant.core import HomeAssistant\
from homeassistant.const import STATE_HOME, STATE_NOT_HOME\
from homeassistant.components.climate import SERVICE_SET_TEMPERATURE, HVACMode\
\
from .const import *\
\
_LOGGER = logging.getLogger(__name__)\
\
class TadoSmartCoordinator(DataUpdateCoordinator):\
    """Class to manage fetching data and controlling thermostats."""\
\
    def __init__(self, hass: HomeAssistant, config_entry):\
        self.hass = hass\
        self.config = config_entry.data\
        \
        super().__init__(\
            hass,\
            _LOGGER,\
            name="Tado Smart Logic",\
            update_interval=datetime.timedelta(minutes=5),\
        )\
\
    async def _async_update_data(self):\
        """Main logic loop called every 5 minutes."""\
        # 1. Konfiguration laden\
        people = self.config.get(CONF_PEOPLE, [])\
        climates = self.config.get(CONF_CLIMATES, [])\
        weather_ent = self.config.get(CONF_WEATHER)\
        \
        # 2. Anwesenheitspr\'fcfung (OR Verkn\'fcpfung)\
        is_anyone_home = False\
        for person in people:\
            state = self.hass.states.get(person)\
            if state and state.state == STATE_HOME:\
                is_anyone_home = True\
                break\
\
        # 3. Zeitplan Pr\'fcfung\
        now = datetime.datetime.now().time()\
        start_time = datetime.time.fromisoformat(self.config.get(CONF_TIME_START))\
        end_time = datetime.time.fromisoformat(self.config.get(CONF_TIME_END))\
        \
        # Geht \'fcber Mitternacht? (z.B. 16:00 bis 02:00)\
        if start_time < end_time:\
            is_active_time = start_time <= now <= end_time\
        else:\
            is_active_time = start_time <= now or now <= end_time\
\
        # 4. Zieltemperatur bestimmen\
        target_temp = self.config.get(CONF_TEMP_ECO) # Default: Nacht/Eco\
\
        if not is_anyone_home:\
            target_temp = self.config.get(CONF_TEMP_AWAY)\
        elif is_active_time:\
            target_temp = self.config.get(CONF_TEMP_COMFORT)\
\
        # 5. KI / Wetter Offset\
        ai_offset = 0\
        if self.config.get(CONF_AI_ENABLE) and is_anyone_home and is_active_time:\
            ai_offset = await self._get_ai_offset(weather_ent)\
        \
        final_temp = target_temp + ai_offset\
        _LOGGER.debug(f"Ziel: \{final_temp\}\'b0C (Basis: \{target_temp\}, Offset: \{ai_offset\})")\
\
        # 6. Thermostate steuern\
        for entity_id in climates:\
            await self._control_thermostat(entity_id, final_temp)\
\
    async def _get_ai_offset(self, weather_entity):\
        """Simuliert oder ruft KI auf."""\
        try:\
            weather_state = self.hass.states.get(weather_entity)\
            if not weather_state: return 0\
\
            temp_out = weather_state.attributes.get("temperature", 0)\
            \
            # Simple deterministische 'KI' Logik f\'fcr den Anfang\
            if temp_out > 20: return -1.0\
            if temp_out > 15: return -0.5\
            if temp_out < 0: return +0.5\
            \
            return 0\
        except Exception:\
            return 0\
\
    async def _control_thermostat(self, entity_id, target_temp):\
        """Setzt Temperatur und warnt vor Schimmel."""\
        state = self.hass.states.get(entity_id)\
        if not state: return\
\
        # Hole aktuelle Luftfeuchtigkeit (oft Attribut bei Tado, sonst Sensor pr\'fcfen)\
        current_hum = state.attributes.get("current_humidity")\
        \
        # Fallback: Wenn humidity nicht im Thermostat, m\'fcsste man separaten Sensor lesen (hier vereinfacht)\
        if current_hum is None:\
            current_hum = 0 # Ignorieren wenn nicht verf\'fcgbar\
\
        mold_limit = self.config.get(CONF_MOLD_THRESH, 65)\
\
        if float(current_hum) > mold_limit:\
            _LOGGER.warning(f"Schimmelgefahr in \{state.name\}: \{current_hum\}%")\
            # Sendet persistente Notification in HA\
            self.hass.components.persistent_notification.async_create(\
                f"Hohe Feuchtigkeit in \{state.name\} (\{current_hum\}%). Bitte l\'fcften!",\
                title="\uc0\u9888 \u65039  Schimmelwarnung"\
            )\
\
        # Temperatur nur senden, wenn sie abweicht, um Traffic zu sparen\
        current_setpoint = state.attributes.get("temperature")\
        if current_setpoint != target_temp:\
            await self.hass.services.async_call(\
                "climate", SERVICE_SET_TEMPERATURE,\
                \{\
                    "entity_id": entity_id, \
                    "temperature": target_temp, \
                    "hvac_mode": HVACMode.HEAT\
                \}\
            )}