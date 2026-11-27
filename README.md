# trix-web

The website for [trix](https://github.com/leofle/trix).

Live at https://trixapp.ai/

## Files

- `index.html`: the whole site, with its CSS and JS inline. This includes the animated mascot and the preloader that shows while the page loads.
- `logo.svg`: Trixy, the trix mascot. It's pixel art, 13×14 pixels.
- `favicon.svg`: the tab icon. It's the same character centered in a square, and the site also uses it in the nav and footer.
- `favicon.ico`: a copy of `brand/favicon/favicon.ico`, for browsers and tools that only look at `/favicon.ico`.
- `brand/`: the logo in other sizes and formats, for use outside the site.
- `brand/social/og-image.png`: the 1200×630 card shown when a link to the site is shared. `og-image.html` next to it is its source; the comment at its top has the command that regenerates the PNG.
- `robots.txt` and `sitemap.xml`: for search engines. `robots.txt` lets every crawler in, AI ones included, and points to the sitemap. Update the sitemap's `lastmod` when the page changes a lot.
- `llms.txt`: a plain summary of trix with links to the docs, for AI tools ([llmstxt.org](https://llmstxt.org)). Keep it in step with the page and the trix README.

## Search and AI answers

The page's `<head>` has the title, description, Open Graph and Twitter card tags, and a JSON-LD block that describes trix as a `SoftwareApplication` and repeats the "Questions" section as an `FAQPage`. When you change a question or answer on the page, change it in the JSON-LD too, so the two match.

There is no build step and nothing to install. Fonts load from Google Fonts.

## Logo files

Everything in `brand/` is Trixy. The pixels stay sharp at every size because each file uses a whole-number scale.

- `brand/svg/`: vector files. Use these when you can. There is the logo, a square version, and one-color black and white versions.
- `brand/png/native/`: the logo at 1x to 64x, from 13×14 up to 832×896.
- `brand/png/square/`: square, with a transparent background, from 16 to 1024 px.
- `brand/png/app-icon/`: square on the site's dark background, at 180, 192, 512 and 1024 px.
- `brand/png/mono/`: the one-color versions at 512 px.
- `brand/webp/`: square, with a transparent background, at 256 and 512 px.
- `brand/favicon/`: `favicon.ico` (16, 32 and 48 px), `favicon.svg`, `apple-touch-icon.png`, and icons at 192 and 512 px.

The colors are body `#82A1F1`, highlight `#B7C9F7`, bulb `#D8B172`, eyes `#14141A`, and the site background `#0d0e15`.

## Run it locally

Open `index.html` in a browser, or serve the folder:

```sh
python3 -m http.server
```

then go to http://localhost:8000.

## Version and what's new

The version number (in the nav, the hero, the demo's top bar and the install section) and the "What's new" list come from GitHub's releases for `leofle/trix`. The page fetches them when it loads, so a new trix release shows up on the site without any change here.

`index.html` also holds a copy of the latest release. It's what crawlers that don't run JavaScript see, most AI crawlers among them, and what shows if GitHub can't be reached. The deploy refreshes that copy (see below), so the live site always has the latest release. The copy committed here can lag behind; to refresh it by hand, run `python3 scripts/refresh-releases.py`.

## Deploy

`.github/workflows/pages.yml` deploys the site to GitHub Pages: on every push to `main`, once an hour, and when run by hand from the Actions tab. Before each deploy it runs `scripts/refresh-releases.py`, which writes the latest trix release into the page, so a new release reaches the site within the hour without a commit here. If GitHub's API fails, the deploy goes ahead with the copy in the repo.

Pages' source (Settings › Pages) must be "GitHub Actions" for this workflow to deploy.
