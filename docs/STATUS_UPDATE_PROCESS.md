# Status-Update-Prozess

Wie und wann der öffentliche Seitenstatus gepflegt wird. Grundsatz: nur belegte Aussagen, keine Versprechen, keine Garantien, keine Termine.

## Wann aktualisieren

- Ein Produkt-Repo erhält auf `main` Code (`custom_components/`, `manifest.json`) oder eine neue Version.
- Ein Beta-Paket-Lauf (`beta-package.yml`, `workflow_dispatch` auf `main`) ändert sein Ergebnis.
- Ein Scaffold wird gemergt oder verworfen.
- Die Brand-SSOT ändert sich.
- Mindestens bei jedem Meilenstein-Merge; spätestens vor jeder Beta-Einladung.

## Quelle der Wahrheit je Produkt

| Angabe | Quelle |
|---|---|
| Code vorhanden | Verzeichnis `custom_components/` im Repo-`main` |
| Version | `version` in `custom_components/<domain>/manifest.json` auf `main` |
| Beta-Paket | Letzter Lauf `beta-package.yml` (`workflow_dispatch`, Branch `main`) |
| CI-Status | Workflows `Validate` und `Brand assets` auf `main` |
| Reifegrad / Phase | README und `docs/` des Repos auf `main` |
| Brand | `brand-source/` in `HASecure/ha-inventory-exporter` (Referenz) |

Statuswerte: `Beta · <Version>` nur bei Code auf `main`; `Design · in Arbeit` / `Architektur · in Arbeit` für Scaffolds, die nicht auf `main` liegen; `Architektur / Spezifikation` bei reinen Dokumentations-Repos; `Design / geplant` ohne laufende Arbeit. Scaffolds in Arbeit nie als fertig darstellen.

## Prüfliste

1. Stand je Repo erheben (`gh run list -R HASecure/<repo> -b main`, Manifest lesen).
2. `index.html`, `beta.html`, `positioning.html` angleichen (Status, Version, Kartenzähler „NN / 11“).
3. `sitemap.xml` (`lastmod`) und „Stand“-Datum aktualisieren.
4. `BRAND_ASSETS.md` und `assets/icons/brand-icons-manifest.json` gegen die Brand-SSOT prüfen.
5. Kernaussagen beibehalten: Einladung erst nach Beta-v1-Stable-Reife und interner Freigabe; Bewerbungsdaten nicht öffentlich.
6. Keine privaten E-Mails, Secrets oder Kontaktdaten.
7. Lokal prüfen: Links/Anker, HTML-Struktur, Pages-Workflow.
8. Änderungsprotokoll `docs/CHANGE_LOG_<datum>.md` mit Belegen anlegen.
9. Branch `chore/status-update-<datum>`, Draft-PR, kein direkter Push auf `main`; Autor `358860637+HASecure@users.noreply.github.com`.
