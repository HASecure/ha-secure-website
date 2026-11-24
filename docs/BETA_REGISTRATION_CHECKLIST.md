# Beta-Anmeldung – Betriebs- und Freigabecheckliste

**Stand:** 24.11.2026

## Aktueller Zustand

- Die öffentliche Beta-Anmeldung ist geschlossen.
- Es existiert derzeit kein veröffentlichtes oder als Entwurf angelegtes Airtable-Formular.
- Die Website überträgt keine Bewerbungsdaten an Airtable.
- Die private Tabelle `Beta-Benachrichtigungen` ist als manuelle interne Warteliste vorgesehen; sie enthält derzeit keine Datensätze.
- Es gibt kein HMAC-Token-Backend und keine automatische E-Mail-Versendung.

## Vorgesehener manueller Ablauf

1. Eine Anmeldung wird erst nach Einrichtung eines echten, zugriffsgeschützten Airtable-Formulars angenommen.
2. Erfasst werden nur E-Mail-Adresse, ausgewählte Produktinteressen und eine ausdrücklich gesetzte Einwilligung.
3. Einträge werden manuell in der privaten Airtable-Basis geprüft und verwaltet.
4. Eine Einladung erfolgt nur, wenn das jeweilige Produkt den Status `Beta v1-Stable – Testfreigabe` erreicht und `Interne Freigabe` aktiviert ist.
5. Einladungen werden manuell über das Projektpostfach versendet; es gibt keinen automatischen Mailversand.
6. Widerruf und Löschung werden manuell bearbeitet und in Airtable dokumentiert.

## Voraussetzungen vor Öffnung

- Formular in Airtable tatsächlich erstellen und mit der Tabelle `Beta-Benachrichtigungen` verbinden.
- Formularfelder auf E-Mail, Produktinteressen und Einwilligung begrenzen.
- Identität und Kontaktdaten der verantwortlichen Stelle sowie Zweck, Rechtsgrundlage, Empfänger, Aufbewahrung und etwaige Drittlandübermittlungen nachvollziehbar dokumentieren.
- Vertrags- und Zugriffsvoraussetzungen des Airtable-Kontos prüfen.
- Datenschutzhinweise auf der Website vervollständigen und prüfen.
- Formularübermittlung mit Testdatensatz prüfen, Testdatensatz anschließend löschen.
- Erst danach Formularlink in der Website hinterlegen und die Aktivierung über einen Draft-PR prüfen lassen.

**Sperrregel:** Solange eine dieser Voraussetzungen offen ist, bleibt die Registrierung geschlossen. Öffentliche GitHub-Issues sind kein Ersatz für eine vertrauliche Beta-Anmeldung.
