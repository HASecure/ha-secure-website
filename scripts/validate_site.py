#!/usr/bin/env python3
"""Static HTML, local-link, icon and SEC-LOG-01 checks for the public site."""
from __future__ import annotations
import ipaddress
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
TOKEN=re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})\b")
KEY=re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")
HOST=re.compile(r"(?i)\b[a-z0-9][a-z0-9.-]*\.(?:local|lan|home|internal)\b")
IP=re.compile(r"(?<![0-9])(?:[0-9]{1,3}\.){3}[0-9]{1,3}(?![0-9])")
class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__(); self.refs=[]
    def handle_starttag(self, tag, attrs):
        data=dict(attrs)
        if tag=="a" and data.get("href"): self.refs.append(("link",data["href"]))
        if tag in {"img","script"} and data.get("src"): self.refs.append(("asset",data["src"]))
        if tag=="link" and data.get("rel")=="icon" and data.get("href"): self.refs.append(("icon",data["href"]))
def main():
    errors=[]
    pages=sorted(ROOT.glob("*.html"))
    if not pages: errors.append("No root HTML pages found.")
    for page in pages:
        content=page.read_text(encoding="utf-8")
        parser=SiteParser(); parser.feed(content)
        for label,ref in parser.refs:
            if ref.startswith(("https://","http://","mailto:","tel:","javascript:","#","data:")): continue
            target=(page.parent/ref.split("#",1)[0].split("?",1)[0]).resolve()
            if not target.exists(): errors.append(f"{page.name}: missing {label} {ref}")
            if label=="icon" and target.suffix.lower() not in {".png",".svg",".ico",".webp"}:
                errors.append(f"{page.name}: unsupported icon format {ref}")
        for pattern,label in ((TOKEN,"token"),(KEY,"private key"),(HOST,"internal hostname")):
            if pattern.search(content): errors.append(f"SEC-LOG-01: {label} in {page.name}")
        for match in IP.finditer(content):
            try: addr=ipaddress.ip_address(match.group())
            except ValueError: continue
            if addr.is_private and not addr.is_loopback and not addr.is_link_local:
                errors.append(f"SEC-LOG-01: private IP in {page.name}"); break
    print("\n".join(errors) if errors else "Website static HTML, local links/assets/icons and SEC-LOG-01: PASS")
    return 1 if errors else 0
if __name__=="__main__": sys.exit(main())
