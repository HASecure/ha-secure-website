# Portfolio-Synchronisierung – Website

**Stand:** 23.11.2026 · **Basis:** `main` @ `6c796bf4f397255e92a6d11c67ec5544755916f9`

## Nachgewiesener Website-Stand
- Das Website-Repository enthält Portfolio- und Brand-Assets sowie ein Produkt-Icon-Manifest.
- Der aktuelle GitHub-Baum enthält lokale Brand-Assets und Referenzen für die elf Produktkarten.
- Der vorherige Brand-Audit-PR dokumentiert 11/11 vorhandene Portfolio-Bildreferenzen und 11/11 Beta-Karten-Bildpfade.
- Ein bytegenauer SHA-256-Abgleich der Website-Binärdateien gegen alle gelieferten Original-ZIP-Dateien ist im bisherigen Audit ausdrücklich noch nicht belegt.

## Beta-Registrierung
Die öffentliche Beta-Anmeldung darf erst als geöffnet dargestellt werden, wenn ein veröffentlichter und geprüfter Airtable-Formularlink verfügbar ist. Der letzte HAWallisellen-Website-Abgleich dokumentiert, dass eine veröffentlichte Formularseite bzw. ein geprüfter Formular-Endpunkt noch fehlte. Kein unsicherer Webhook-/Issue-Ersatz.

## Synchronisationsgrenze
Die Website bildet Produktstatus ab, ist aber keine Quelle für Runtime-Funktionalität. Statusangaben müssen mit den jeweiligen Produkt-Repositories und deren CI-/TestVM-Nachweisen übereinstimmen. „Design“, „Scaffold“, „Beta“, „TestVM-validiert“ und „veröffentlicht“ sind getrennte Zustände.

## Offene Punkte
- Brand-Binärdateien Website ↔ kanonische Produkt-Brand-SSOTs bytegenau prüfen.
- Produktstatus und Versionen aus den jeweiligen aktuellen Manifests/Portfolio-Sync-Dokumenten nachführen.
- Anmeldung erst nach verifiziertem Airtable-Formularlink aktivieren.
- Keine Beta-Verfügbarkeit oder Produktfunktion behaupten, die nicht im jeweiligen Produkt-Repo belegt ist.

Dokumentation only. Keine Website-Veröffentlichung, kein Main-Merge und keine Aktivierung der Registrierung.


## Nachtrag – Portfolio-Validierung

Der neue [docs/PORTFOLIO_VALIDATION_CONTRACT.md](PORTFOLIO_VALIDATION_CONTRACT.md) definiert WEB-001 bis WEB-010 für Produkt-ID/Version, belegte Statusangaben, Branding-Prüfsummen, Link Health, Datenschutz und Beta-Registrierung. Die Website bleibt eine Darstellungsschicht und ist keine Quelle für Runtime-Funktionalität. Veröffentlichung und Beta-Anmeldung bleiben separat freigabepflichtig.
