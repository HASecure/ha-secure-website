# HA Secure – Website Portfolio-Validierungsvertrag

**Version:** 1.0-draft · **Stand:** 23.11.2026 · Europe/Zurich

## Zweck

Die Website stellt Portfolio-Status, Produktinformationen, Beta-Hinweise und Branding dar. Sie ist keine Quelle für Runtime-Funktionalität und darf keine Fähigkeiten behaupten, die das jeweilige Produkt-Repository nicht durch Code/CI und gegebenenfalls Test-Lab-Nachweise belegt.

## Pflichtprüfungen

| ID | Prüfung | Soll |
|---|---|---|
| WEB-001 | Produktinventar | alle Produkt-IDs eindeutig und mit Repository verknüpft |
| WEB-002 | Version | angezeigte Version entspricht dem geprüften Manifest bzw. App-Manifest |
| WEB-003 | Statussemantik | Design, Scaffold, Implemented, CI-tested, TestVM-validated und Released bleiben getrennte Zustände |
| WEB-004 | Evidence | jede Runtime-Aussage verweist auf belegten Code-/CI-/Test-Lab-Nachweis |
| WEB-005 | Branding | lokale Bildreferenz, Produkt-ID, Asset-Version und SHA-256-Mapping konsistent |
| WEB-006 | Link Health | interne Links, README-Links und Beta-/Support-Links erreichbar oder eindeutig als Draft markiert |
| WEB-007 | Beta Registration | Anmeldung nur aktiv, wenn ein veröffentlichter, getesteter Formular-Endpunkt existiert |
| WEB-008 | Privacy | keine privaten Betriebsdaten, Tokens, Personen-/Geräteidentifikatoren oder Test-VM-Zugangsdaten |
| WEB-009 | Build | reproduzierbarer Static-Site-Build und Link-/Asset-Prüfungen |
| WEB-010 | No release drift | Website-Status darf nicht weiter sein als das Produkt-Repo bzw. Test-Lab-Gate |

## Abhängigkeiten

- Produktstatus wird aus den jeweiligen Repository-Manifests und Testverträgen abgeleitet.
- Branding-Quellnachweise stammen aus den produktbezogenen Brand-SSOTs und dem Website-Manifest.
- Keine automatische Veröffentlichung durch Statussynchronisierung; Publish bleibt separater Freigabeschritt.
- Beta-Formular bleibt deaktiviert, bis der konkrete Formularlink verifiziert wurde.

## Aktuelle Einschränkung

Die vorherige Prüfung belegte vorhandene Bildreferenzen, aber noch keinen vollständigen bytegenauen Website-Binärabgleich mit den bereitgestellten Original-ZIP-Dateien. Dieser Abgleich bleibt offen. Auch das Vorhandensein von elf Portfolio-Karten beweist keine elf abgeschlossenen Produkte.

**Status:** Dokumentierter Soll-Vertrag. Noch kein Nachweis, dass alle WEB-001 bis WEB-010 automatisiert implementiert sind.
