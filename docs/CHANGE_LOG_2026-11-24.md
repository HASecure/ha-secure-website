# Änderungsprotokoll 2026-11-24

Abgleich der Website mit dem Stand der Produkt-Repos (Manifest auf `main`, letzte `main`-Läufe via `gh run list -b main`). Alle Angaben sind Statusangaben, keine Zusagen.

## Belegter Stand

| Repo | Domain | Version | `main`-CI | Website-Status |
|---|---|---|---|---|
| ha-synology-file-connector | synology_file_connector | 0.1.0-beta.3 | Validate, Brand assets, Beta package (dispatch) grün | Beta |
| ha-inventory-exporter | ha_inventory_exporter | 0.1.0-beta.3 | Validate, Brand assets, Beta package grün | Beta |
| ha-repo-updater | ha_repo_updater | 0.1.0-beta.7 | Validate, Brand assets, Beta package grün | Beta |
| ha-certificate-guardian | certificate_guardian | 0.1.0-beta.2 | CI, Hassfest, Beta package grün | Beta (neu, vorher „Architektur“) |
| ha-universal-nas-connector | universal_nas_connector | 0.1.0-beta.0 | CI, HA base checks grün | Beta-Vorstufe (neu) |
| ha-repo-config-guard | repo_config_guard | 0.0.1 | Brand assets grün | Scaffold |
| ha-ai-diagnostics | ai_diagnostics | 0.1.0 | Validate grün | Scaffold |
| ha-presence-simulator | ha_secure_presence_simulator | 0.0.1 | Validate grün | Scaffold (neue Domain) |
| ha-wireguard-client | wireguard_client | 0.0.2 | Brand assets grün | Scaffold |
| ha-secure-guard | ha_secure_guard | 0.0.1 | Scaffold CI grün | Scaffold |
| ha-wireguard-client-app | – (Verzeichnis `wireguard_client/`, kein Manifest) | – | Validation, CI grün | in Arbeit |
| ha-secure-dev-board | ha_secure_dev_board | 0.1.0-alpha.1 | Validate grün (Feature-Branches) | nicht auf der Website (privat) |
| HAWallisellen | – | Release v2026.11.21 | CI & Policy Validation grün | nicht auf der Website (privates Betriebs-Repo) |

Grüne Validate-/Scaffold-Läufe belegen Struktur, nicht Funktion. `domain_verified` wird nicht behauptet; TestVM-/Hardwaretests sind offen.

## Änderungen

- `index.html`, `beta.html`, `positioning.html`: Statusbadges (Certificate Guardian, Universal NAS Connector, fünf Scaffolds), Certificate-Guardian-Texte, Stand-Datum 24.11.2026, Hinweis auf Domain `ha_secure_presence_simulator`.
- `sitemap.xml`: `lastmod` 2026-11-24.

## Befunde

- **Icons:** `assets/icons/ha-inventory-exporter-96.png` (git blob `60f487c…`) und `ha-repo-updater-96.png` (`fb293b0…`) stimmen mit keiner Datei in `brand-source/` der Repos überein (abgeleitete 96-px-Fassungen). Die `*.jpg`-Icons sind ebenfalls nicht byte-identisch geprüft. Austausch gegen SSOT-`icon.png`/`icon@2x.png` steht aus; nur unter Freigabe, da Layout (80 px) neu geprüft werden muss.
- **ha-secure-dev-board:** privates Repo; `brand-source/` enthält auf `main` nur `BRAND_MAPPING.json`, kein Icon. Keine Karte, solange nicht freigegeben und Icon fehlt.
- **HAWallisellen:** privates Betriebs-Repo mit Infrastrukturdetails; bewusst nicht auf der öffentlichen Seite.
- **Beta-Anmeldung:** bleibt „noch nicht geöffnet“; kein Formularlink und keine Kontaktdaten in Git.
- **PR #8** (`docs/PORTFOLIO_SYNC_2026-11-23.md`, `docs/PORTFOLIO_VALIDATION_CONTRACT.md`, Draft, nur Doku, keine Checks): überschneidet sich inhaltlich mit diesem Protokoll, kein Dateikonflikt. Der darin genannte Stand ist ältere Datenlage (23.11.).

## Datenschutz (`privacy.html`) – Lücken gegenüber Airtable-Nutzung

Text nicht geändert (keine Rechtsberatung). Offen für spätere Ergänzung vor Öffnung der Anmeldung:

1. Airtable als Auftragsverarbeiter inkl. Drittlandübermittlung (USA) / Auftragsverarbeitungsvertrag.
2. Zweck und Rechtsgrundlage (Einwilligung) der Bewerbungsdaten.
3. Erhobene Felder (Minimierung) und Speicherdauer/Löschfristen.
4. Betroffenenrechte (Auskunft, Löschung, Widerruf) und wie sie ausgeübt werden.
5. Verantwortlicher und Kontaktweg ohne private Kontaktdaten (Impressum fehlt).
6. Hinweis, dass keine Weitergabe an Dritte erfolgt und Zugriff auf wenige Personen beschränkt ist.
7. Zugangsschutz der Airtable-Basis (nur intern, kein öffentlicher Share-Link).

## Prüfung

Lokal: interne Links/Assets vorhanden, Tag-Balance, Sitemap wohlgeformt (siehe PR-Beschreibung).

## Nachtrag Icons (Nutzerentscheid)

Zehn Web-Icons durch rand-source/icon.png der jeweiligen Repos ersetzt (eindeutige Ableitungszuordnung, Tabelle in BRAND_ASSETS.md); Certificate Guardian bleibt offen (Abweichung 16,8). Dev Board erst nach dessen Brand-PR, HAWallisellen wird nie gelistet. PR #9 wird nicht gemergt.
