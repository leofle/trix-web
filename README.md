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

## Version and what's new

The version number (in the nav, the hero, the demo's top bar and the install section) and the "What's new" list come from GitHub's releases for `leofle/trix`. The page fetches them when it loads, so a new trix release shows up on the site without any change here.

`index.html` also holds a copy of the latest release, which shows if GitHub can't be reached. It's fine if that copy is a little out of date, but update it now and then.

## Deploy

GitHub Pages serves the root of `main`. Push to `main` and the site updates a minute or two later.
