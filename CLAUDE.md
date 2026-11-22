# Easy Garage — how this repo works

**The source of truth is `src/`. Never edit `{lang}/index.html` by hand.**

- `src/game.html` — the whole game (HTML/CSS/JS), English layout, with `{{T:kNNNN}}` placeholders for every piece of text that changes per language.
- `src/i18n/{en,ar,it,es,zh,ru,ja,tr}.json` — the text for each placeholder. To find a string, search `en.json` for the English text.
- `src/build.py` — builds the 8 pages.

## Making a change
1. Code change: edit `src/game.html` once (applies to all languages).
   New text: add `{{T:kNEW}}` in `game.html` and add `kNEW` to **all 8** json files.
2. Site: `python3 src/build.py` → commit `src/` and the rebuilt `{lang}/index.html` together on `main`.
3. App: on the `android` branch run `python3 <path-to-main>/src/build.py --app www`, bump `versionCode`/`versionName` in `android/app/build.gradle`, commit, push. CI builds the unsigned AAB into the `android-bundle` release.
4. `python3 src/build.py --check` (CI runs it on every push) fails if built pages drift from `src/`.

## Never commit
The upload keystore (`upload.jks`) or its password. Sign the AAB locally with jarsigner.

`tools/extract_src.py` is the one-time script that rebuilt `src/` from the built pages (Nov 2026); keep it for reference.
