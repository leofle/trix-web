# trix-web

The website for [trix](https://github.com/leofle/trix).

Live at https://leofle.github.io/trix-web/

## Files

- `index.html`: the whole site, with its CSS and JS inline
- `logo.svg`: the mascot
- `favicon.svg`: the tab icon

There is no build step and nothing to install. Fonts load from Google Fonts.

## Run it locally

Open `index.html` in a browser, or serve the folder:

```sh
python3 -m http.server
```

then go to http://localhost:8000.

## Deploy

GitHub Pages serves the root of `main`. Push to `main` and the site updates a minute or two later.
