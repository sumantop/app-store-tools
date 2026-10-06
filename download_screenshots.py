"""Download an App Store app's screenshots and icon at full resolution (stdlib only).

usage: python3 download_screenshots.py APP_ID [COUNTRY]   e.g. 6443918070 us
Uses Apple's public iTunes Lookup API; mzstatic serves the original upload when asked for 9999x9999bb.png.
"""
import json, re, sys, urllib.request
from pathlib import Path

app_id, cc = sys.argv[1], (sys.argv[2] if len(sys.argv) > 2 else "us")
get = lambda u: urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=30).read()
res = json.loads(get(f"https://itunes.apple.com/lookup?id={app_id}&country={cc}&entity=software"))["results"]
if not res:
    sys.exit("app not found in that storefront")
app = res[0]
out = Path(f"screenshots-{app_id}-{cc}")
out.mkdir(exist_ok=True)
full = lambda u: re.sub(r"/[^/]+$", "/9999x9999bb.png", u)
items = [("icon", app["artworkUrl512"])] + [(f"iphone-{i}", u) for i, u in enumerate(app.get("screenshotUrls", []), 1)] \
    + [(f"ipad-{i}", u) for i, u in enumerate(app.get("ipadScreenshotUrls", []), 1)]
for name, url in items:
    (out / f"{name}.png").write_bytes(get(full(url)))
print(f"{app['trackName']}: {len(items)} files in {out}/")
