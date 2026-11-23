#!/usr/bin/env python3
"""Validate HA Secure website brand icon mapping and local references."""
from __future__ import annotations
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
manifest_path = ROOT / "brand-icons-manifest.json"
errors: list[str] = []

def fail(message: str) -> None:
    errors.append(message)
    print(f"FAIL: {message}")

def main() -> int:
    if not manifest_path.is_file():
        fail("brand-icons-manifest.json fehlt")
        return 1
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    products = manifest.get("products", [])
    if manifest.get("audited_source_count") != 10 or len(products) != 10:
        fail("Manifest muss genau zehn Quell-Produktfamilien enthalten")
    ids = [p.get("id") for p in products]
    if len(ids) != len(set(ids)):
        fail("Doppelte Produkt-ID im Manifest")
    for product in products:
        for key in ("id", "portfolio", "website", "repo", "source", "sha256"):
            if not product.get(key):
                fail(f"{product.get('id', '<unknown>')}: Feld {key} fehlt")
        if len(product.get("source", [])) != 3 or len(product.get("sha256", [])) != 3:
            fail(f"{product.get('id')}: genau drei Quelldateien und SHA-256-Werte erwartet")
        if not (ROOT / product.get("website", "")).is_file():
            fail(f"Website-Icon fehlt: {product.get('website')}")
    for html_name in ("index.html", "beta.html"):
        path = ROOT / html_name
        if not path.is_file():
            fail(f"{html_name} fehlt")
            continue
        content = path.read_text(encoding="utf-8")
        refs = re.findall(r'src="(assets/icons/[^"]+)"', content)
        cards = len(re.findall(r'<article class="product-card"', content))
        if cards != 11:
            fail(f"{html_name}: 11 Produktkarten erwartet, gefunden {cards}")
        for ref in refs:
            if not (ROOT / ref).is_file():
                fail(f"{html_name}: referenziertes Icon fehlt: {ref}")
    cert = manifest.get("extra_website_asset", {})
    if cert.get("id") == "ha-certificate-guardian":
        if any(p.get("id") == "ha-certificate-guardian" for p in products):
            fail("Certificate Guardian darf nicht unmarkiert im gelieferten 10er-Satz enthalten sein")
        if not (ROOT / cert.get("website", "")).is_file():
            fail("Zusätzliches Certificate-Guardian-Website-Icon fehlt")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if "brand-icons-manifest.json" not in readme:
        fail("README verweist nicht auf das Brand-Icon-Manifest")
    if errors:
        print(f"\\nBrand-Asset-Prüfung fehlgeschlagen: {len(errors)} Befund(e)")
        return 1
    print("PASS: 10 Quell-Iconfamilien, Manifest-Zuordnung, Website- und Beta-Referenzen sowie README geprüft.")
    print("HINWEIS: Der SHA-256-Vergleich der bereits veröffentlichten Website-Binärdateien mit ZIP-Originalen ist ein separater Upload-Abnahmeschritt.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
