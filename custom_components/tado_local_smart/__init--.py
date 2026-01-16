{\rtf1\ansi\ansicpg1252\cocoartf2867
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 """The Tado Local Smart Control integration."""\
from __future__ import annotations\
\
import logging\
from homeassistant.config_entries import ConfigEntry\
from homeassistant.core import HomeAssistant\
\
from .const import DOMAIN\
from .coordinator import TadoSmartCoordinator\
\
_LOGGER = logging.getLogger(__name__)\
\
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:\
    """Set up Tado Local Smart from a config entry."""\
    hass.data.setdefault(DOMAIN, \{\})\
\
    coordinator = TadoSmartCoordinator(hass, entry)\
    \
    # Sofortiges erstes Update erzwingen\
    await coordinator.async_config_entry_first_refresh()\
    \
    hass.data[DOMAIN][entry.entry_id] = coordinator\
\
    return True\
\
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:\
    """Unload a config entry."""\
    if entry.entry_id in hass.data[DOMAIN]:\
        hass.data[DOMAIN].pop(entry.entry_id)\
    return True}