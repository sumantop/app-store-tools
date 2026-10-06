# app-store-tools

Two small, dependency-free Python scripts for app makers:

- **`export_reviews.py`**: export an app's recent App Store reviews to CSV (date, rating, version, title, review), up to 500 per storefront, from Apple's public reviews feed.
  `python3 export_reviews.py 6443918070 us`
- **`download_screenshots.py`**: download an app's App Store screenshots (iPhone and iPad) and icon at full resolution.
  `python3 download_screenshots.py 6443918070 us`

Python 3.9+, standard library only. Use them for research on your own app or competitors; screenshots and reviews belong to their owners.

No-code versions of both (plus an App Store character counter) run in the browser at
[slideeasy.app/app-store-review-exporter](https://slideeasy.app/app-store-review-exporter) and
[slideeasy.app/app-store-screenshot-downloader](https://slideeasy.app/app-store-screenshot-downloader).

Made by [Sumant Tirkey](https://x.com/sumantxd), who builds [Slide-Easy](https://slideeasy.app), a Mac app that turns an App Store page and its reviews into Instagram Reels and carousels for app makers.

MIT licence.
