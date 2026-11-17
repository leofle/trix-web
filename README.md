# trix-web

The website for [trix](https://github.com/leofle/trix).

Live at https://trixapp.ai/

## Files

- `index.html`: the whole site, with its CSS and JS inline. This includes the animated mascot and the preloader that shows while the page loads.
- `logo.svg`: Trixy, the trix mascot. It's pixel art, 13×14 pixels.
- `favicon.svg`: the tab icon. It's the same character centered in a square, and the site also uses it in the nav and footer.
- `brand/`: the logo in other sizes and formats, for use outside the site.

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

`index.html` also holds a copy of the latest release, which shows if GitHub can't be reached. It's fine if that copy is a little out of date, but update it now and then.

## Deploy

GitHub Pages serves the root of `main`. Push to `main` and the site updates a minute or two later.
