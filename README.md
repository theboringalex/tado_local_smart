# Tado Local Smart Control 🏠🔥
A local Home Assistant integration for Tado thermostats (via HomeKit Controller). Developed by theboringAlex.

This integration replaces the Tado Cloud control with purely local logic within Home Assistant. It accounts for presence, schedules, and mold risk.

Features
🔒 100% Local: No Tado Cloud necessary (Prerequisite: Tado integrated into HA via HomeKit).

👥 Multi-User: Detects Marie, Krissy, and Alex (or any person entities).

🕒 Time Control: Simple Day/Night configuration via UI.

🍄 Mold Protection: Automatically warns when humidity is too high.

🤖 AI-Ready: Prepared for weather offsets and AI optimization.

Installation (HACS)
Add this repository as a Custom Repository in HACS: https://github.com/theboringAlex/hacs_tado_local

Install "Tado Local Smart Control".

Restart Home Assistant.

Go to Settings -> Devices & Services -> Add Integration.

Search for Tado Local Smart Control.

Configuration
In the setup dialog, select:

The residents (for presence detection).

The thermostats to be controlled.

Your weather entity.

Target temperatures for Comfort, Eco/Night, and Away.

License
MIT



# Tado Local Smart Control 🏠🔥

Eine **lokale** Home Assistant Integration für Tado Thermostate (via HomeKit Controller).  
Entwickelt von **theboringAlex**.

Diese Integration ersetzt die Tado Cloud Steuerung durch eine rein lokale Logik in Home Assistant. Sie berücksichtigt Anwesenheit, Zeitpläne und Schimmelgefahr.

## Funktionen
* 🔒 **100% Lokal:** Keine Tado Cloud notwendig (Voraussetzung: Tado via HomeKit in HA eingebunden).
* 👥 **Multi-User:** Erkennt Marie, Krissy und Alex (oder beliebige Personen-Entities).
* 🕒 **Zeitsteuerung:** Einfache Tag/Nacht Konfiguration via UI.
* 🍄 **Schimmel-Schutz:** Warnt automatisch bei zu hoher Luftfeuchtigkeit.
* 🤖 **KI-Ready:** Vorbereitet für Wetter-Offsets und KI-Optimierung.

## Installation (HACS)

1.  Füge dieses Repository als **Benutzerdefiniertes Repository** in HACS hinzu:
    `https://github.com/theboringAlex/hacs_tado_local`
2.  Installiere "Tado Local Smart Control".
3.  Starte Home Assistant neu.
4.  Gehe zu **Einstellungen -> Geräte & Dienste -> Integration hinzufügen**.
5.  Suche nach **Tado Local Smart Control**.

## Konfiguration

In der Einrichtungsmaske wählst du:
1.  Die Bewohner (für Anwesenheitserkennung).
2.  Die zu steuernden Thermostate.
3.  Deine Wetter-Entity.
4.  Wunschtemperaturen für Komfort, Eco/Nacht und Abwesenheit.

## Lizenz
MIT
