# HA Secure – Brand-Icon-Katalog und Abgleich

Stand: 23.11.2026

## Verbindliche Quelle

Die drei von Denise bereitgestellten Archive definieren denselben kanonischen Satz aus **10 Produkt-Icon-Familien**:

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

Die Website- und Repository-Dateinamen-/Produktzuordnung ist dokumentiert. Die Binärdateien sind in diesem Commit **noch nicht** in GitHub hochgeladen und deshalb auch noch nicht als Website-Assets live eingebunden. Siehe mitgeliefertes Paket `HA_Secure_Brand_Assets_Validated_10_Products.zip`. Nach dem Upload müssen Bild-URLs und Prüfsummen gegen das Manifest validiert werden. Erst danach darf die Website-Galerie als vollständig bezeichnet werden.

## Regeln für künftige Änderungen

1. Produkt-ID bleibt stabil; Anzeigenamen dürfen sich ändern.
2. 256-PNG ist Standard für kleine Brand-Assets, 512-PNG für hochauflösende Darstellung, 1024-JPG nur Master/Preview.
3. Website-Karten, README-Dateien und Manifest referenzieren dieselbe Produkt-ID.
4. Keine MDI-Icons als Ersatz für eigenständige Produkt-Brand-Icons verwenden.
5. Zusätzliche Produkte (z. B. Certificate Guardian) erhalten eigene freigegebene Assets und werden nicht in die bestehende 10er-Sammlung hineingedeutet.
