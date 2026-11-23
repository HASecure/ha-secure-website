# Status-Pflege der Website

Die Website darf nur Stände zeigen, die in den Produkt-Repos auf `main` belegt sind.

## Quelle der Wahrheit je Produkt
- Version: `custom_components/<domain>/manifest.json` auf `main`.
- Beta-Paket: Lauf von `beta-package.yml` (`workflow_dispatch`) auf `main`.
- Brand: `brand-source/` und `BRAND_ASSETS.md` im jeweiligen Repo.
- Funktionsstand und Abnahme: `docs/VALIDATION_STATUS_2026-11-23.md` im jeweiligen Repo.

## Prüfliste bei jeder Änderung am Entwicklungsstand
1. Version und Status in `index.html` und `beta.html` angleichen.
2. Produktzähler (`NN / 11`) und Kartenzahl prüfen.
3. Keine Funktion als verfügbar darstellen, die auf `main` nicht belegt ist.
4. Keine privaten Kontaktdaten oder Secrets veröffentlichen.
5. Draft-PR mit Belegen (Commit-/Run-Links) öffnen.

## Stand 2026-11-23 (Belege)
- Code auf `main`: synology-file-connector 0.1.0-beta.3, inventory-exporter 0.1.0-beta.3, repo-updater 0.1.0-beta.7.
- Beta-Paket per `workflow_dispatch` erfolgreich: Synology 45234145552, Inventory 45234133703, Repo Updater 45234139611.
- Certificate Guardian: README auf `main` nennt Architektur-/Spezifikationsphase, daher herabgestuft.
- WireGuard Client App: kein Code auf `main`, daher „Experimentelles Scaffold“.

## Offen
- `positioning.html` führt nur 9 Karten (Inventory Exporter und Repo Updater fehlen) und zählt „/ 09“.
- `BRAND_ASSETS.md` nennt 10 statt 11 Produkte.
- Website-Icons (jpg/-96.png) sind nicht byte-identisch zur Brand-SSOT.
