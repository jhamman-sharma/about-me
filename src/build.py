"""Builds one standalone HTML page per entry in PAGES: python src/build.py"""
import pathlib
import re

SRC = pathlib.Path(__file__).parent
OUT = SRC.parent

# (body file, theme, extra page css or None, output file, title or None to use the theme's @title)
PAGES = [
    ("body.html", "noir", None, "portfolio-noir-gold.html", None),
    ("body.html", "ivory", None, "portfolio-ivory-ink.html", None),
    ("body.html", "pinkcity", None, "portfolio-pink-city.html", None),
    ("body-merrillion.html", "pinkcity", "page-merrillion.css", "merrillion-proposal.html", "Merrillion — Execution Roadmap"),
]

base = (SRC / "base.css").read_text(encoding="utf-8")

for body_file, theme, extra, out_name, title in PAGES:
    body = (SRC / body_file).read_text(encoding="utf-8")
    css = (SRC / f"theme-{theme}.css").read_text(encoding="utf-8")
    if extra:
        css += "\n" + (SRC / extra).read_text(encoding="utf-8")
    fonts = re.search(r"@fonts (\S+)", css).group(1)
    title = title or re.search(r"@title (.+?) \*/", css).group(1)
    page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="Jhamman Lal Sharma: hospitality and e-commerce technology consultant. Ordering, booking and multi-shop platforms.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{fonts}" rel="stylesheet">
<style>
{base}
{css}
</style>
</head>
<body>
{body}
</body>
</html>
"""
    (OUT / out_name).write_text(page, encoding="utf-8")
    print("built", out_name)
