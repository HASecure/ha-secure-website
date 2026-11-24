# HA Secure – Website-Icons und Brand-Abgleich

**Stand:** 24.11.2026

## Portfolio und Icon-Abdeckung

Das öffentliche Portfolio umfasst zwölf eigenständige Produkte. Auf der Website sind zwölf separate Produkt-Icon-Dateien unter `assets/icons/` eingebunden:

1. Synology File Connector
2. Universal NAS Connector
3. Repo Config Guard
4. AI Diagnostics
5. Presence Simulator
6. WireGuard Client App
7. WireGuard Client Integration
8. HA Secure Guard
9. Certificate Guardian
10. Inventory Exporter
11. Repo Updater
12. HA Secure Dev Board

Das HA Secure Dev Board ist Produkt 12. Sein Icon liegt unter `assets/icons/ha-secure-dev-board.png` und stammt aus dem `brand-source/icon.png` des privaten Dev-Board-Repositories. Es ist als Produkt-Icon in der Website eingebunden; aus der privaten Quelle wird kein Downloadlink abgeleitet.

## Kanonische Brand-Quellen

Die ursprünglichen bereitgestellten Brand-Archive enthalten zehn Produkt-Icon-Familien in 256×256 RGBA-PNG, 512×512 RGBA-PNG und 1024×1024 RGB-JPG. Diese 10er-Archivsammlung ist ein historischer Asset-Satz und nicht die aktuelle Anzahl der Portfolio-Produkte.

Certificate Guardian und HA Secure Dev Board kamen als separate Produkt-Icons hinzu. Die frühere Aussage, Certificate Guardian habe kein eigenes Icon oder die Website enthalte nur elf Produktkarten, ist überholt.

## Integrität und Grenzen des Nachweises

- Die Website bindet zwölf eigenständige Produkt-Icon-Dateien ein.
- Für elf Produkte wurde die jeweilige Datei aus der Brand-Quelle des Produkt-Repositories übernommen; das Dev-Board-Icon stammt aus dessen eigener Brand-Quelle.
- Das vorhandene 10er-Manifest beschreibt weiterhin nur die ursprüngliche Archivsammlung. Es ist kein vollständiges Manifest aller zwölf Website-Produkte.
- Ein vollständiger bytegenauer Abgleich sämtlicher Website-Dateien gegen alle 512-px-Varianten und 1024-px-Master ist nicht als abgeschlossen dokumentiert. Diese Prüfung wird hier nicht als erfolgt behauptet.

## Verbindliche Regeln

1. Produkt-IDs bleiben stabil; Anzeigenamen dürfen sich ändern.
2. Jede Portfolio-Karte verwendet das eigene Brand-Icon des jeweiligen Produkts.
3. Website-Karten, Positionierungsseite und Beta-Übersicht verwenden dieselbe Produkt-ID und dieselbe Icon-Datei.
4. Keine MDI- oder generischen System-Icons als Ersatz für eigenständige Produkt-Brand-Icons verwenden.
5. Zusätzliche Produkte werden als eigene Icon-Familien geführt und nicht nachträglich in die ursprüngliche 10er-Archivsammlung hineingedeutet.
