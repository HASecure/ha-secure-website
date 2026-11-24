# Repo-Status und Scope – ha-secure-website

Stand: 2026-11-24 · Bezugs-Commit: `23cde2b` (Branch `hasecure-status-update-2026-11-24`, Draft-PR #9, nicht gemergt)

## Scope

- Öffentliches Repository (GitHub Pages) ausschließlich für Produktinformation, Portfolioübersicht und die geplante Beta-Tester-Registrierung.
- Keine interne Entwicklungs- oder Testumgebung, keine Produktivdaten, keine Kontaktdaten, keine Secrets.
- Statische Seiten ohne Build-Schritt (`.nojekyll`).

## Nicht-Scope

- Test-Runner, Testprofile und Produktcode (liegen in den privaten Produkt-Repos bzw. im Test-Lab).
- Download- oder Repo-Links zu privaten Repositories.
- Verweise auf interne Betriebs- oder Produktionsumgebungen.
- Zusagen zu Funktionen, Terminen oder Testplätzen.

## Runner / CI

- Das Repo enthält aktuell keine Workflows (`.github/workflows` fehlt).
- Falls Website-Workflows nötig werden: ausschließlich GitHub-hosted Runner. Kein Zugriff auf den Self-hosted Runner (DS220+); Ausnahme laut Master-Prompt Abschnitt 5.

## Funktionsstatus

| Funktion | Klassifikation | Evidenz |
|---|---|---|
| Portfolio-Startseite mit 12 Produktkarten | FUNKTIONSFÄHIG_AUF_MAIN (11 Karten, Stand PR #7); 12. Karte (Dev Board) IN_OFFENEM_PR | main bzw. PR #9 |
| beta.html, positioning.html, privacy.html | FUNKTIONSFÄHIG_AUF_MAIN; Statusupdate IN_OFFENEM_PR | PR #9 |
| Icons aus `brand-source/icon.png` der Repos (12/12) | IN_OFFENEM_PR | `BRAND_ASSETS.md`, Skalierungsvergleich (nicht Hash) |
| Beta-Registrierung | NUR_SPEZIFIZIERT (Anmeldung „noch nicht geöffnet“, Formularlink fehlt) | `beta.html`, `privacy.html` |
| Datenschutztext ↔ Airtable-Nutzung | NICHT_VERIFIZIERT (7 Lücken, siehe `CHANGE_LOG_2026-11-24.md`) | – |
| GitHub-Pages-Build/Rendering von PR #9 | NICHT_VERIFIZIERT | lokal nur Link-/Tag-/Sitemap-Prüfung |
| Brand-/VG-/SSOT-Pin-CI für die Website | FEHLT_NOCH | – |

Produktstatus auf der Website ist Statusangabe, kein Funktionsnachweis: grüne Validate-/CI-Läufe sind keine HA-Live-Tests; TestVM-Läufe stehen aus.

## Offene Punkte

1. Airtable-Formularlink und Datenschutz-Ergänzungen (Verantwortlicher, Rechtsgrundlage, Speicherdauer, Betroffenenrechte, Auftragsverarbeitung/Drittland).
2. Pages-Build nach Merge prüfen; Merge nur nach Freigabe durch Denise.
3. Dev Board: Status nach Beta-RC-Ergebnis in der TestVM nachführen.
4. Icon-Abgleich nur per Skalierungsvergleich; Hash-Abgleich gegen die 1024-px-Master offen.
5. Positioning-Seite ohne Dev-Board-Karte (bewusst).

## Unverhandelbare Sperren

- Kein Push auf `main`, kein Auto-Merge, keine Veröffentlichung ohne Freigabe.
- Keine privaten Mails/Secrets/Kontaktdaten; Bewerbungsdaten nie in Git oder öffentlichen Issues.
- Einladung zur Beta erst nach dokumentierter Beta-v1-Stable-Reife und interner Freigabe.
- Git-Identität: Noreply-Adresse des Organisationskontos.

## Referenzierte SSOT-Definitionen

`BRAND_ASSETS.md` (Brand-SSOT `brand-source/` je Repo), `docs/STATUS_UPDATE_PROCESS.md`. Weitere SSOT-Dokumente (Standards im Test-Lab, `.ha-secure-ssot.json`) wurden hier nicht geprüft; Vorschlag für den Master-Prompt: Website-Statusprozess und Runner-Ausnahme explizit referenzieren.
