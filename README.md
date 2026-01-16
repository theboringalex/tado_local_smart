{\rtf1\ansi\ansicpg1252\cocoartf2867
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Tado Local Smart Control \uc0\u55356 \u57312 \u55357 \u56613 \
\
Eine **lokale** Home Assistant Integration f\'fcr Tado Thermostate (via HomeKit Controller).  \
Entwickelt von **theboringAlex**.\
\
Diese Integration ersetzt die Tado Cloud Steuerung durch eine rein lokale Logik in Home Assistant. Sie ber\'fccksichtigt Anwesenheit, Zeitpl\'e4ne und Schimmelgefahr.\
\
## Funktionen\
* \uc0\u55357 \u56594  **100% Lokal:** Keine Tado Cloud notwendig (Voraussetzung: Tado via HomeKit in HA eingebunden).\
* \uc0\u55357 \u56421  **Multi-User:** Erkennt Marie, Krissy und Alex (oder beliebige Personen-Entities).\
* \uc0\u55357 \u56658  **Zeitsteuerung:** Einfache Tag/Nacht Konfiguration via UI.\
* \uc0\u55356 \u57156  **Schimmel-Schutz:** Warnt automatisch bei zu hoher Luftfeuchtigkeit.\
* \uc0\u55358 \u56598  **KI-Ready:** Vorbereitet f\'fcr Wetter-Offsets und KI-Optimierung.\
\
## Installation (HACS)\
\
1.  F\'fcge dieses Repository als **Benutzerdefiniertes Repository** in HACS hinzu:\
    `https://github.com/theboringAlex/hacs_tado_local`\
2.  Installiere "Tado Local Smart Control".\
3.  Starte Home Assistant neu.\
4.  Gehe zu **Einstellungen -> Ger\'e4te & Dienste -> Integration hinzuf\'fcgen**.\
5.  Suche nach **Tado Local Smart Control**.\
\
## Konfiguration\
\
In der Einrichtungsmaske w\'e4hlst du:\
1.  Die Bewohner (f\'fcr Anwesenheitserkennung).\
2.  Die zu steuernden Thermostate.\
3.  Deine Wetter-Entity.\
4.  Wunschtemperaturen f\'fcr Komfort, Eco/Nacht und Abwesenheit.\
\
## Lizenz\
MIT}