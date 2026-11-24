// Einzige Konfigurationsstelle der Beta-Registrierung.
// Leer lassen = Anmeldung bleibt geschlossen. Erst nach Freigabe durch Denise
// den privaten Formularlink eintragen (muss mit https://airtable.com/ beginnen).
const REGISTRATION_URL = "";

(function () {
  var btn = document.getElementById("register-btn");
  var box = document.getElementById("consent");
  var note = document.getElementById("register-note");
  if (!btn || !box) return;
  var open = /^https:\/\/airtable\.com\//.test(REGISTRATION_URL);
  function update() {
    var ok = open && box.checked;
    btn.setAttribute("aria-disabled", ok ? "false" : "true");
    if (ok) { btn.setAttribute("href", REGISTRATION_URL); btn.setAttribute("rel", "noopener noreferrer"); }
    else { btn.removeAttribute("href"); }
  }
  btn.addEventListener("click", function (e) {
    if (btn.getAttribute("aria-disabled") === "true") e.preventDefault();
  });
  box.addEventListener("change", update);
  if (!open) {
    box.disabled = true;
    if (note) note.hidden = false;
  }
  update();
})();
