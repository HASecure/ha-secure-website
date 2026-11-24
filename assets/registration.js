// Beta-Anmeldung bleibt geschlossen, bis ein geprüftes Formular und
// vollständige Datenschutzinformationen vorliegen.
const REGISTRATION_URL = "";

(function () {
  var btn = document.getElementById("register-btn");
  if (!btn) return;
  // Absichtlich keine Aktivierung über clientseitige Konfiguration.
  btn.removeAttribute("href");
  btn.setAttribute("aria-disabled", "true");
})();
