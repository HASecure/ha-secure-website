# HA Secure – Brand-Icon-Katalog und Abgleich

Stand: 23.11.2026

## Verbindliche Quelle

Referenz für die Produkt-Brand-Dateien ist die Brand-SSOT `brand-source/` im Repository `HASecure/ha-inventory-exporter` (Stand main, 23.11.2026); alle elf Produkt-Repos führen `brand-source/`, `BRAND_ASSETS.md` und den Workflow `brand-assets.yml` auf main. Das Website-Icon-Manifest `assets/icons/brand-icons-manifest.json` beschreibt den ursprünglichen 10er-Satz aus den drei von Denise bereitgestellten Archiven (Stand 2026-11-23) und ist nicht identisch mit den auf der Website eingebundenen älteren Dateien.

Die drei Archive definieren denselben kanonischen Satz aus **10 Produkt-Icon-Familien**:

- `HA_Secure_Brand_Icons_256x256_PNG_10_Icons.zip`: RGBA-PNG, 256×256
- `HA_Secure_Brand_Icons_512x512_PNG_10_Icons.zip`: RGBA-PNG, 512×512
- `HA_Secure_App_Icons_Master_HighRes_10_Icons.zip`: RGB-JPG, 1024×1024

Zuordnung über gemeinsame Produkt-ID (Dateiname ohne Suffix):
| Produkt-ID | Portfolio-Bezeichnung |
|---|---|
| ha-synology-file-connector | Synology File Connector |
| ha-multi-nas-file-connector | Universal / Multi-NAS File Connector |
| ha-repo-config-guard | Repo Config Guard |
| ha-ai-diagnostics | AI Diagnostics |
| ha-presence-simulator | Presence Simulator |
| ha-wireguard-client-app | WireGuard Client App |
| ha-wireguard-client | WireGuard Client |
| ha-secure-guard | HA Secure Guard |
| ha-inventory-exporter | Inventory Exporter |
| ha-repo-updater | Repo Updater |

## Abgleich mit Website

Die Website führt elf Produktkarten. Zehn Karten lassen sich auf den kanonischen Satz abbilden; **Certificate Guardian** besitzt in den drei 10er-Archiven kein eigenes Icon. Es darf nicht stillschweigend das SSL-Motiv aus einem zusätzlichen Einzelbild als Teil des kanonischen 10er-Satzes ausgegeben werden. Dieses Motiv ist ein separater Kandidat und braucht eine eigene freigegebene Produktdatei.

Die vorhandene Website nutzt teilweise abweichende ältere Dateinamen bzw. Formate (z. B. JPG, `-96.png`, `universal-nas-connector`). Der Produkt-/Dateinamen-Abgleich ist daher nicht identisch mit der neuen kanonischen Benennung.

## Zusätzliche Einzelbilder

Sieben zusätzlich bereitgestellte JPEGs wurden visuell geprüft. Sechs Motive stimmen thematisch mit Produkten des 10er-Satzes überein (Synology, Multi-NAS, Repo Config Guard, Inventory Exporter, Repo Updater und KI/Shield); das SSL-Motiv ist ein zusätzlicher Certificate-Guardian-Kandidat. Sie ersetzen nicht automatisch die Masterdateien. Die einzelnen JPEGs sind nicht Teil der drei ZIP-Archive.

## Technische Integritätsprüfung

Alle 30 Dateien (10 Produkt-IDs × 3 Auflösungs-/Mastervarianten) wurden aus den Archiven gelesen:
- 10/10 PNG-Dateien 256×256, RGBA
- 10/10 PNG-Dateien 512×512, RGBA
- 10/10 Master-JPGs 1024×1024, RGB
- Dateizuordnung vollständig: jede Produkt-ID besitzt alle drei Varianten
- SHA-256-Prüfsummen sind in `brand-assets/manifest.json` hinterlegt.

## Einbindung – Status

Stand 24.11.2026: Die älteren Web-Icons (`*.jpg`, `*-96.png`) waren zu keiner SSOT-Datei byte-identisch (abgeleitete Verkleinerungen). Ableitungsprüfung: jedes Web-Icon wurde auf Größe skaliert und gegen die `brand-source/icon.png` aller elf Repos verglichen; bei zehn Produkten war der Treffer des eigenen Repos eindeutig (mittlere Abweichung 3,9–7,7 von 255, nächster fremder Treffer ≥ 32). Diese zehn wurden durch die jeweilige `brand-source/icon.png` (256×256 RGBA, Blob aus dem Repo-`main`) ersetzt; die alten Dateien sind entfernt.

| Repo | Web-Icon-Datei | Quelle | SHA-256 (Anfang) |
|---|---|---|---|
| ha-synology-file-connector | `assets/icons/ha-synology-file-connector.png` | `brand-source/icon.png` in HASecure/ha-synology-file-connector | `76e2fe9ca43586e0…` |
| ha-universal-nas-connector | `assets/icons/ha-universal-nas-connector.png` | `brand-source/icon.png` in HASecure/ha-universal-nas-connector | `94b492b961ce0a8e…` |
| ha-repo-config-guard | `assets/icons/ha-repo-config-guard.png` | `brand-source/icon.png` in HASecure/ha-repo-config-guard | `df3d494569800022…` |
| ha-ai-diagnostics | `assets/icons/ha-ai-diagnostics.png` | `brand-source/icon.png` in HASecure/ha-ai-diagnostics | `7b327ea3077d477f…` |
| ha-presence-simulator | `assets/icons/ha-presence-simulator.png` | `brand-source/icon.png` in HASecure/ha-presence-simulator | `9fd54fb49a583faf…` |
| ha-wireguard-client-app | `assets/icons/ha-wireguard-client-app.png` | `brand-source/icon.png` in HASecure/ha-wireguard-client-app | `0864b3f66ca536bf…` |
| ha-wireguard-client | `assets/icons/ha-wireguard-client.png` | `brand-source/icon.png` in HASecure/ha-wireguard-client | `0dde2037f1134bfa…` |
| ha-secure-guard | `assets/icons/ha-secure-guard.png` | `brand-source/icon.png` in HASecure/ha-secure-guard | `63b29af102c128a7…` |
| ha-inventory-exporter | `assets/icons/ha-inventory-exporter.png` | `brand-source/icon.png` in HASecure/ha-inventory-exporter | `ec055581f485c08a…` |
| ha-repo-updater | `assets/icons/ha-repo-updater.png` | `brand-source/icon.png` in HASecure/ha-repo-updater | `8f04f70a34fbf749…` |

Offen (nicht ersetzt):
- **ha-certificate-guardian:** `assets/icons/ha-certificate-guardian.jpg` weicht mit mittlerer Abweichung 16,8 deutlich stärker von `brand-source/icon.png` ab (SSOT-Master dort ist ein PNG); Zuordnung nicht 100 % belegt, daher unverändert.
- **ha-secure-dev-board:** keine Karte und kein Icon, solange dessen Brand-PR (Icon in `brand-source/`) nicht gemergt ist; danach Status „alpha“ ehrlich ausweisen.
- Der Hash-Abgleich gegen die 1024-px-Master wurde nicht durchgeführt (Web-Icons sind Ableitungen); ein Vergleich mit `brand-icons-manifest.json` (10er-Archivsatz) bleibt separat.

## Regeln für künftige Änderungen

1. Produkt-ID bleibt stabil; Anzeigenamen dürfen sich ändern.
2. 256-PNG ist Standard für kleine Brand-Assets, 512-PNG für hochauflösende Darstellung, 1024-JPG nur Master/Preview.
3. Website-Karten, README-Dateien und Manifest referenzieren dieselbe Produkt-ID.
4. Keine MDI-Icons als Ersatz für eigenständige Produkt-Brand-Icons verwenden.
5. Zusätzliche Produkte (z. B. Certificate Guardian) erhalten eigene freigegebene Assets und werden nicht in die bestehende 10er-Sammlung hineingedeutet.
