# HA Secure – Brand-Icon-Abgleich

**Prüfdatum:** 23.11.2026
**Quelle:** drei vom Projekt bereitgestellte ZIP-Archive mit 256-PNG, 512-PNG und Master-JPG.

## Ergebnis der Quelldateien-Prüfung

| Prüfschritt | Ergebnis |
|---|---:|
| ZIP-Archive geöffnet | 3/3 |
| Produktfamilien | 10 |
| Erwartete Einzeldateien | 30 |
| Vorhandene Einzeldateien | 30 |
| PNG 256×256 RGBA | 10/10 |
| PNG 512×512 RGBA | 10/10 |
| JPG 1024×1024 RGB | 10/10 |
| Dateifamilien nach Produkt-ID zugeordnet | 10/10 |
| SHA-256-Prüfsummen berechnet | 30/30 |

Alle drei Archive sind lesbar. Jede Produktfamilie besitzt eine 256-PNG-, 512-PNG- und Master-JPG-Datei. Die Einzeldateien wurden in ein zusammengeführtes, lokal validiertes Paket übernommen; die Originaldateien wurden dabei nicht verändert.

## Kanonische Produktzuordnung

| Quell-ID im ZIP | Portfolio / Repository | Website-Referenz |
|---|---|---|
| ha-synology-file-connector | Synology File Connector | assets/icons/ha-synology-file-connector.jpg |
| ha-multi-nas-file-connector | Universal NAS Connector | assets/icons/ha-universal-nas-connector.jpg |
| ha-repo-config-guard | Repo Config Guard | assets/icons/ha-repo-config-guard.jpg |
| ha-ai-diagnostics | AI Diagnostics | assets/icons/ha-ai-diagnostics.jpg |
| ha-presence-simulator | Presence Simulator | assets/icons/ha-presence-simulator.jpg |
| ha-wireguard-client-app | WireGuard Client App | assets/icons/ha-wireguard-client-app.jpg |
| ha-wireguard-client | WireGuard Client Integration | assets/icons/ha-wireguard-client.jpg |
| ha-secure-guard | HA Secure Guard | assets/icons/ha-secure-guard.jpg |
| ha-inventory-exporter | Inventory Exporter | assets/icons/ha-inventory-exporter-96.png |
| ha-repo-updater | Repo Updater | assets/icons/ha-repo-updater-96.png |

Die Zuordnung ha-multi-nas-file-connector → ha-universal-nas-connector ist eine bewusste Portfolio-Namenszuordnung. Die Quell-ID bleibt im Manifest erhalten und wird nicht umbenannt.

## Zusätzliche Website-Grafik

Die Website enthält zusätzlich assets/icons/ha-certificate-guardian.jpg. Dieses Bild ist nicht Teil der drei gelieferten 10er-ZIP-Archive. Für Certificate Guardian wurde in den gelieferten Dateien keine passende 256-/512-/Master-Familie gefunden. Das zusätzliche Asset wird deshalb getrennt geführt und nicht als Bestandteil des kanonischen 10er-Satzes ausgegeben.

## Website- und README-Abgleich

- index.html und beta.html referenzieren die Produktgrafiken direkt in den Portfolio-Karten.
- Die referenzierten Dateipfade wurden gegen den Repository-Dateibaum abgeglichen.
- Die Produkt-READMEs der zehn zugeordneten Repositories erhalten eine offizielle Brand-Icon-Abbildung.
- Das HAWallisellen-Haupt-README erhält eine Übersicht der zehn Portfolio-Icons.
- Das Certificate-Guardian-README weist sein zusätzliches, nicht im ZIP enthaltenes Website-Asset ausdrücklich aus.
- Die Website-README nennt elf Portfolio-Produkte und verweist auf dieses Manifest.

## Wichtige Grenze der Prüfung

Die Quell-ZIP-Dateien wurden lokal vollständig auf Dateinamen, Format, Abmessungen, Farbraum und SHA-256 geprüft. Die vorhandenen Website-Bilddateien sind im GitHub-Dateibaum vorhanden und die HTML-Referenzen sind nachvollziehbar.

Ein bytegenauer Vergleich zwischen den Originalen aus den ZIPs und den bereits auf GitHub gespeicherten Website-Bilddateien konnte mit der verfügbaren GitHub-Dateiaktion nicht durchgeführt werden, da sie die binären Repository-Bilddaten nicht zur lokalen SHA-256-Auswertung bereitstellt. Daher ist nicht belegt, dass die vorhandenen JPG-/PNG-Website-Dateien exakt aus den gelieferten ZIP-Originalen erzeugt wurden. Das Manifest enthält die Quell-Prüfsummen, nicht behauptete Website-Prüfsummen.

## Nächster technischer Schritt

Für eine endgültige visuelle/bytegenaue Abnahme müssen die gelieferten 256-PNG-/512-PNG-Dateien als kanonische Website-Assets hochgeladen werden. Anschließend:
1. Website-Karten auf die kanonischen PNG-Dateien umstellen,
2. srcset mit 256-/512-PNG definieren,
3. die tatsächlichen GitHub-Binärdateien herunterladen und SHA-256 gegen dieses Manifest prüfen,
4. Website und alle Produkt-READMEs nach Veröffentlichung erneut automatisiert auf defekte Bildlinks und fehlende Produktzuordnungen testen.

Bis dahin lautet der Status: Quelldateien validiert; Website-Referenzen vorhanden; exakte Binärgleichheit und endgültige Veröffentlichung der gelieferten ZIP-Dateien noch nicht bestätigt.