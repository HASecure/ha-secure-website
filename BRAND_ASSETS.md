# HA Secure – Brand-Icon-Katalog und Abgleich

Stand: 23.11.2026

## Verbindliche Quellen

Die drei von Denise bereitgestellten Originalarchive definieren den unveränderten kanonischen Satz aus **10 Produkt-Icon-Familien**:

- `HA_Secure_Brand_Icons_256x256_PNG_10_Icons.zip`: 256×256 RGBA PNG
- `HA_Secure_Brand_Icons_512x512_PNG_10_Icons.zip`: 512×512 RGBA PNG
- `HA_Secure_App_Icons_Master_HighRes_10_Icons.zip`: 1024×1024 RGB JPG

Das ergänzende Paket `HA_Secure_Brand_Asset_Library_v1.1.0.zip` enthält zusätzlich das eigens erstellte **Certificate-Guardian-Icon** in 256×256 PNG, 512×512 PNG und 1024×1024 Master-JPG. Damit umfasst das Portfolio elf Produkt-Icon-Familien: zehn aus den Originalarchiven plus Certificate Guardian als separat ergänztes elftes Produkt. Die ursprünglichen zehn werden dadurch nicht umbenannt oder ersetzt.

## Kanonische Zuordnung

| Produkt-ID | Repository | Asset |
|---|---|---|
| `ha-synology-file-connector` | `ha-synology-file-connector` | Synology File Connector |
| `ha-multi-nas-file-connector` | `ha-universal-nas-connector` | Universal / Multi-NAS File Connector |
| `ha-repo-config-guard` | `ha-repo-config-guard` | Repo Config Guard |
| `ha-ai-diagnostics` | `ha-ai-diagnostics` | AI Diagnostics |
| `ha-presence-simulator` | `ha-presence-simulator` | Presence Simulator |
| `ha-wireguard-client-app` | `ha-wireguard-client-app` | WireGuard Client App |
| `ha-wireguard-client` | `ha-wireguard-client` | WireGuard Client |
| `ha-secure-guard` | `ha-secure-guard` | HA Secure Guard |
| `ha-inventory-exporter` | `ha-inventory-exporter` | Inventory Exporter |
| `ha-repo-updater` | `ha-repo-updater` | Repo Updater |
| `ha-certificate-guardian` | `ha-certificate-guardian` | Certificate Guardian (separate v1.1.0 supplement) |

**Wichtig:** Repo Updater verwendet ausschließlich `ha-repo-updater`; Repo Config Guard ausschließlich `ha-repo-config-guard`. Synology File Connector verwendet ausschließlich `ha-synology-file-connector`; Universal / Multi-NAS File Connector ausschließlich `ha-multi-nas-file-connector`.

## Größen und Home-Assistant-Einbindung

Für echte Home-Assistant-Integrationen gilt:

- Standard-Icon: `custom_components/<domain>/brand/icon.png`, exakt 256×256 PNG.
- HiDPI-Icon: `custom_components/<domain>/brand/icon@2x.png`, exakt 512×512 PNG.
- Master-JPG 1024×1024 ist die hochauflösende Quelle/Preview und wird nicht als HA-Icon eingesetzt.
- `<domain>` muss zuerst aus dem jeweiligen `manifest.json` übernommen werden. Kein Domain-Name wird aus dem Repository-Namen geraten.
- Quadratische Original-Icons werden bytegetreu kopiert. Keine Neugenerierung, Umfärbung, MDI-Ersatzgrafik oder verlustbehaftete Umwandlung.

Eine eigenständige App (WireGuard Client App) wird als App gebrandet, aber nicht fälschlich als Home-Assistant-Integration deklariert. Design-Repositories ohne vorhandenes Integrationsmanifest erhalten eine dokumentierte Produktzuordnung; ein HA-Zielpfad wird erst nach Festlegung einer echten Domain gesetzt.

## Screenshot-Abgleich – 23.11.2026, 03:14:27

Der vom Projekt bereitgestellte Home-Assistant-Screenshot hebt vier Integrationen hervor:

| Integration | Markierung im Screenshot | Korrekte Produkt-ID |
|---|---|---|
| Certificate Guardian | Rot – falsches/fehlendes Produkt-Branding | `ha-certificate-guardian` |
| HA Secure Repo Updater | Rot – falsches/fehlendes Produkt-Branding | `ha-repo-updater` |
| Synology File Connector | Rot – falsches/fehlendes Produkt-Branding | `ha-synology-file-connector` |
| HA Secure Inventory Exporter | Grün – visuell richtige Produktfamilie | `ha-inventory-exporter` |

Das grüne Inventory-Exporter-Motiv ist als Produktfamilie richtig. Die vorhandene Datei wurde technisch jedoch nicht als Originaldatei in 256×256 bestätigt; die HiDPI-Datei fehlte. Grün bedeutet daher korrekte Motiv-Zuordnung, nicht bereits nachgewiesene Größen-/Byte-Parität.

## Technischer Ist-Stand der drei vorhandenen Integrations-Repositories

Prüfung des jeweiligen `main`-Branches am 23.11.2026:

| Repository / Domain | 256×256 `icon.png` | 512×512 `icon@2x.png` | Ergebnis |
|---|---|---|---|
| Synology File Connector / `synology_file_connector` | vorhanden, aber nicht Originaldatei | fehlt | ersetzen/ergänzen |
| Repo Updater / `ha_repo_updater` | vorhanden, aber nicht Originaldatei | fehlt | ersetzen/ergänzen |
| Inventory Exporter / `ha_inventory_exporter` | vorhanden, aber nicht Originaldatei | fehlt | ersetzen/ergänzen |

Für die übrigen Produkt-Repositories ist derzeit keine HA-Integrationsdomain im Main-Branch nachgewiesen. Dort wird deshalb keine Domain oder Custom-Component-Struktur erfunden.

## Upload-/Freigabestatus

Die Produktzuordnungen, 256-/512-Quellprüfsummen und die pro Repository geltenden Zielpfade sind in den jeweiligen `BRAND_ASSETS.md`-Dateien und – für die drei bereits vorhandenen Integrationen – in `custom_components/<domain>/brand/ASSET_SOURCE.json` dokumentiert.

**Die Original-Binärdateien sind in diesem Dokumentationsstand noch nicht in die einzelnen GitHub-Repositories übertragen.** Das ist der verbleibende technische Schritt, bevor HA die korrekten Originale tatsächlich in der Integrationsliste anzeigen kann. Ein Dokumentations-Commit allein ändert die in HA sichtbaren Symbole nicht.

## Referenzen

- Offizielle Home-Assistant-Branding-Dokumentation: https://contributors.home-assistant.io/core/integrations/brands/
- Zentrales Asset-Manifest: `assets/icons/brand-icons-manifest.json`
