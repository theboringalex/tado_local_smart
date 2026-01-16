{\rtf1\ansi\ansicpg1252\cocoartf2867
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 """Config flow for Tado Local Smart Control."""\
import voluptuous as vol\
from homeassistant import config_entries\
from homeassistant.core import callback\
from homeassistant.helpers import selector\
import homeassistant.helpers.config_validation as cv\
\
from .const import *\
\
class TadoSmartFlow(config_entries.ConfigFlow, domain=DOMAIN):\
    """Handle a config flow for Tado Local Smart."""\
\
    VERSION = 1\
\
    async def async_step_user(self, user_input=None):\
        """Handle the initial step."""\
        errors = \{\}\
\
        if user_input is not None:\
            return self.async_create_entry(title="Tado Smart Control", data=user_input)\
\
        # Schema f\'fcr die GUI\
        data_schema = vol.Schema(\{\
            vol.Required(CONF_PEOPLE): selector.EntitySelector(\
                selector.EntitySelectorConfig(domain="person", multiple=True)\
            ),\
            vol.Required(CONF_CLIMATES): selector.EntitySelector(\
                selector.EntitySelectorConfig(domain="climate", multiple=True)\
            ),\
            vol.Required(CONF_WEATHER): selector.EntitySelector(\
                selector.EntitySelectorConfig(domain="weather")\
            ),\
            vol.Required(CONF_TIME_START, default="06:00:00"): selector.TimeSelector(),\
            vol.Required(CONF_TIME_END, default="22:00:00"): selector.TimeSelector(),\
            \
            vol.Required(CONF_TEMP_COMFORT, default=DEFAULT_TEMP_COMFORT): vol.Coerce(float),\
            vol.Required(CONF_TEMP_ECO, default=DEFAULT_TEMP_ECO): vol.Coerce(float),\
            vol.Required(CONF_TEMP_AWAY, default=DEFAULT_TEMP_AWAY): vol.Coerce(float),\
            \
            vol.Optional(CONF_MOLD_THRESH, default=DEFAULT_MOLD_THRESH): int,\
            vol.Optional(CONF_AI_ENABLE, default=False): bool,\
        \})\
\
        return self.async_show_form(\
            step_id="user", data_schema=data_schema, errors=errors\
        )\
\
    @staticmethod\
    @callback\
    def async_get_options_flow(config_entry):\
        return TadoSmartOptionsFlowHandler(config_entry)\
\
class TadoSmartOptionsFlowHandler(config_entries.OptionsFlow):\
    """Handle options flow."""\
\
    def __init__(self, config_entry):\
        self.config_entry = config_entry\
\
    async def async_step_init(self, user_input=None):\
        """Manage the options."""\
        if user_input is not None:\
            return self.async_create_entry(title="", data=user_input)\
\
        current = self.config_entry.data\
        \
        # Vereinfachtes Schema f\'fcr \'c4nderungen\
        data_schema = vol.Schema(\{\
            vol.Required(CONF_TEMP_COMFORT, default=current.get(CONF_TEMP_COMFORT)): vol.Coerce(float),\
            vol.Required(CONF_TEMP_ECO, default=current.get(CONF_TEMP_ECO)): vol.Coerce(float),\
            vol.Required(CONF_TEMP_AWAY, default=current.get(CONF_TEMP_AWAY)): vol.Coerce(float),\
            vol.Required(CONF_TIME_START, default=current.get(CONF_TIME_START)): selector.TimeSelector(),\
            vol.Required(CONF_TIME_END, default=current.get(CONF_TIME_END)): selector.TimeSelector(),\
            vol.Optional(CONF_AI_ENABLE, default=current.get(CONF_AI_ENABLE)): bool,\
        \})\
\
        return self.async_show_form(step_id="init", data_schema=data_schema)}