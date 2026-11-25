#!/usr/bin/env python3
"""Render a page at several widths (and optionally dark mode) to PNGs so you can look at it.

usage: shoot.py <file.html | http(s)://url> [--out DIR] [--widths 390,768,1440] [--dark] [--full]

Tries Python Playwright first, then a headless Chrome/Chromium binary. Prints the PNG paths.
"""
import argparse, os, pathlib, shutil, subprocess, sys

p = argparse.ArgumentParser()
p.add_argument("target")
p.add_argument("--out", default="shots")
p.add_argument("--widths", default="390,768,1440")
p.add_argument("--height", type=int, default=900)
p.add_argument("--dark", action="store_true", help="also render prefers-color-scheme: dark")
p.add_argument("--full", action="store_true", help="full-page screenshot (Playwright only)")
a = p.parse_args()

url = a.target if a.target.startswith(("http://", "https://", "file://")) else pathlib.Path(a.target).resolve().as_uri()
out = pathlib.Path(a.out); out.mkdir(parents=True, exist_ok=True)
widths = [int(w) for w in a.widths.split(",")]
schemes = ["light", "dark"] if a.dark else ["light"]
made = []

try:
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        for s in schemes:
            for w in widths:
                pg = b.new_page(viewport={"width": w, "height": a.height}, color_scheme=s)
                pg.goto(url, wait_until="networkidle")
                pg.wait_for_timeout(400)  # let fonts and entry animations settle
                f = out / f"{w}-{s}.png"
                pg.screenshot(path=str(f), full_page=a.full)
                made.append(f); pg.close()
        b.close()
except Exception as e:  # no Playwright or no browser for it: fall back to a Chrome binary
    exe = next((shutil.which(n) for n in ("google-chrome", "chromium", "chromium-browser", "chrome") if shutil.which(n)), None)
    if not exe:
        sys.exit(f"No Playwright ({e}) and no Chrome binary found. Open the page in a browser instead.")
    for w in widths:  # shortcut: the CLI cannot emulate dark mode or capture full page
        f = out / f"{w}-light.png"
        subprocess.run([exe, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                        f"--window-size={w},{a.height}", f"--screenshot={f.resolve()}", url],
                       check=True, capture_output=True)
        made.append(f)

for f in made:
    print(f)