# Easy Garage — Android (Capacitor) branch

`www/{lang}/index.html` are **built files**. The source lives on the `main` branch in `src/` (see `CLAUDE.md` there).
Rebuild the app pages from it with:

    python3 <main-checkout>/src/build.py --app www

then bump `versionCode`/`versionName` in `android/app/build.gradle`, commit and push. CI publishes the unsigned AAB to the `android-bundle` release; sign it locally with the upload key (never commit the key).
