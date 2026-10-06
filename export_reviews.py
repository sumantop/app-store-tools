import csv, json, sys, time, urllib.request

app_id, country = sys.argv[1], (sys.argv[2] if len(sys.argv) > 2 else "us")
rows = []
for page in range(1, 11):
    url = f"https://itunes.apple.com/{country}/rss/customerreviews/page={page}/id={app_id}/sortby=mostrecent/json"
    for attempt in range(3):  # a page can come back empty while later pages are full: retry, never stop early
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        entries = json.load(urllib.request.urlopen(req, timeout=30))["feed"].get("entry", [])
        if isinstance(entries, dict): entries = [entries]
        if entries: break
        time.sleep(3)
    for e in entries:
        rows.append([e["updated"]["label"][:10], e["im:rating"]["label"], e["im:version"]["label"],
                     e["title"]["label"], e["content"]["label"]])
    time.sleep(1)

with open(f"reviews-{app_id}-{country}.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["date", "rating", "version", "title", "review"])
    w.writerows(rows)
print(f"{len(rows)} reviews, {rows[-1][0]} to {rows[0][0]}" if rows else "no reviews in this storefront")
