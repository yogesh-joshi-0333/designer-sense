#!/usr/bin/env python3
"""Render a page at several widths (and optionally dark mode) to PNGs.

usage: shoot.py <file.html | http(s)://url> [--out DIR] [--widths 390,768,1440] [--dark] [--full]

Uses Python Playwright when its browser is available. Falls back to a Chrome/Chromium
command-line screenshot when Playwright cannot launch. The fallback supports light-mode,
viewport screenshots only; unsupported requested options are reported explicitly.
"""
import argparse
import pathlib
import shutil
import subprocess
import sys

p = argparse.ArgumentParser()
p.add_argument("target")
p.add_argument("--out", default="shots")
p.add_argument("--widths", default="390,768,1440")
p.add_argument("--height", type=int, default=900)
p.add_argument("--dark", action="store_true", help="also render prefers-color-scheme: dark")
p.add_argument("--full", action="store_true", help="capture the full page (Playwright only)")
a = p.parse_args()

url = a.target if a.target.startswith(("http://", "https://", "file://")) else pathlib.Path(a.target).resolve().as_uri()
out = pathlib.Path(a.out)
out.mkdir(parents=True, exist_ok=True)
widths = [int(w) for w in a.widths.split(",")]
schemes = ["light", "dark"] if a.dark else ["light"]
made = []

try:
    from playwright.sync_api import sync_playwright
except ImportError as exc:
    sync_playwright = None
    playwright_import_error = exc
else:
    playwright_import_error = None

if sync_playwright is not None:
    # Only browser startup failure triggers the CLI fallback. Navigation and
    # screenshot errors are real test failures and must remain visible.
    with sync_playwright() as pw:
        try:
            browser = pw.chromium.launch()
        except Exception as exc:
            browser = None
            fallback_reason = exc
        if browser is not None:
            try:
                for scheme in schemes:
                    for width in widths:
                        page = browser.new_page(
                            viewport={"width": width, "height": a.height},
                            color_scheme=scheme,
                        )
                        try:
                            page.goto(url, wait_until="load", timeout=30000)
                            page.wait_for_timeout(400)
                            output = out / f"{width}-{scheme}.png"
                            page.screenshot(path=str(output), full_page=a.full)
                            made.append(output)
                        finally:
                            page.close()
            finally:
                browser.close()
        else:
            print(
                f"WARNING: Playwright could not launch its browser ({fallback_reason}); "
                "trying the Chrome/Chromium CLI fallback.",
                file=sys.stderr,
            )
else:
    print(
        f"WARNING: Python Playwright is unavailable ({playwright_import_error}); "
        "trying the Chrome/Chromium CLI fallback.",
        file=sys.stderr,
    )

if not made:
    exe = next(
        (shutil.which(name) for name in ("google-chrome", "chromium", "chromium-browser", "chrome")
         if shutil.which(name)),
        None,
    )
    if not exe:
        sys.exit("No usable Playwright browser or Chrome/Chromium binary found.")
    if a.dark:
        print(
            "WARNING: Chrome CLI fallback cannot emulate prefers-color-scheme: dark; "
            "only light screenshots will be captured.",
            file=sys.stderr,
        )
    if a.full:
        print(
            "WARNING: Chrome CLI fallback cannot guarantee full-page capture; "
            "screenshots will use the requested viewport height only.",
            file=sys.stderr,
        )
    for width in widths:
        output = out / f"{width}-light.png"
        subprocess.run(
            [
                exe, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                f"--window-size={width},{a.height}",
                f"--screenshot={output.resolve()}", url,
            ],
            check=True,
            capture_output=True,
        )
        made.append(output)

for output in made:
    print(output)
