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
