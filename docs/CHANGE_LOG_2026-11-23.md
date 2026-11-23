# Änderungsprotokoll 2026-11-23

Statusabgleich der Website mit dem Stand der 11 Produkt-Repos (jeweils `main`).

## Belege

| Produkt | Code auf main | Version | Beta-Paket (workflow_dispatch, main) |
|---|---|---|---|
| ha-synology-file-connector | ja | 0.1.0-beta.3 | grün, [Run 45234145552](https://github.com/HASecure/ha-synology-file-connector/actions/runs/45234145552) |
| ha-inventory-exporter | ja | 0.1.0-beta.3 | grün, [Run 45234133703](https://github.com/HASecure/ha-inventory-exporter/actions/runs/45234133703) |
| ha-repo-updater | ja | 0.1.0-beta.7 | grün, [Run 45234139611](https://github.com/HASecure/ha-repo-updater/actions/runs/45234139611) |
| ha-certificate-guardian | nein (nur Doku, README: Architektur-/Spezifikationsphase) | – | Lauf 45234159781 fehlgeschlagen |
| übrige 7 Repos | nein (Docs/Scripts/Tests) | – | – |

- Brand-SSOT (`brand-source/`, `BRAND_ASSETS.md`, `brand-assets.yml`) ist in allen 11 Repos auf main; `Brand assets`-Läufe auf main grün (2026-11-23, 18:01–18:17 UTC).
- Domain-Scaffolds (ai_diagnostics, ha_secure_guard, repo_config_guard, presence_simulator, wireguard_client) entstehen in anderen Sessions und sind nicht als fertig dargestellt.
- Nicht verifiziert: Laufzeittests in Home Assistant; Austausch der Website-Icons gegen SSOT-Dateien.

## Änderungen

- `index.html`: Kartenzähler auf „/11“; Versionen Synology 0.1.0-beta.3, Inventory Exporter 0.1.0-beta.3, Repo Updater 0.1.0-beta.7; Certificate Guardian von „Beta-Scaffold“ auf „Architektur / Spezifikation“ (Text ohne unbelegte Funktionsaussagen); WireGuard Client App von „Experimentelle Beta“ auf „Design · in Arbeit“; Repo Config Guard, AI Diagnostics, Presence Simulator, HA Secure Guard auf „in Arbeit“; Stand-Hinweis ergänzt.
- `beta.html`: gleiche Statuskorrekturen; Hinweis, dass ein Beta-Status keinen Testplatz bedeutet. Einladungs- und Datenschutzaussagen unverändert.
- `positioning.html`: Karten für Inventory Exporter und Repo Updater ergänzt (11 Karten), Certificate-Guardian- und WireGuard-Texte korrigiert, Stand 23.11.2026.
- `sitemap.xml`: `lastmod` für geänderte Seiten.
- `BRAND_ASSETS.md`: Brand-SSOT-Referenz und aktueller Einbindungsstatus.
- Neu: `docs/STATUS_UPDATE_PROCESS.md`, dieses Protokoll.

## Hinweis zu Synology

Der frühere Status „Praxistest bestätigt“ wurde durch „Beta · 0.1.0-beta.3“ ersetzt; der Betreiberbericht ist auf der Beta-Seite weiter als „berichtet“ vermerkt, auf main nicht dokumentiert.

## Prüfung

Siehe PR-Beschreibung (lokale Link- und Strukturprüfung).
