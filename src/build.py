#!/usr/bin/env python3
"""Build the 8 language pages of Easy Garage from src/game.html + src/i18n/{lang}.json.

  python3 src/build.py                 # site pages  -> ./{lang}/index.html   (main branch, GitHub Pages)
  python3 src/build.py --app DIR       # app pages   -> DIR/{lang}/index.html (android branch: DIR=www)
  python3 src/build.py --check [--app DIR]   # build in memory and compare with the files on disk
"""
import json, os, re, sys
SRC=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.dirname(SRC)
LANGS=['en','ar','it','es','zh','ru','ja','tr']
# The app (Capacitor) build differs from the site build only by these rules.
APP_RULES=[
 ('<meta name="google-adsense-account" content="ca-pub-6936703685284243"><script src="../consent.js"></script>',''),
 ('<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>','<script src="../lib/three.min.js"></script>'),
 ('<script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>','<script src="../lib/OrbitControls.js"></script>'),
 ('<script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/environments/RoomEnvironment.js"></script>','<script src="../lib/RoomEnvironment.js"></script>'),
 ('admob:{android:{banner:"ca-app-pub-3940256099942544/6300978111",interstitial:"ca-app-pub-3940256099942544/1033173712",rewarded:"ca-app-pub-3940256099942544/5224354917"}',
  'admob:{android:{banner:"ca-app-pub-6936703685284243/9239524674",interstitial:"ca-app-pub-6936703685284243/5218333277",rewarded:"ca-app-pub-6936703685284243/6040460356"}'),
 ('LANG_FILE=""','LANG_FILE="index.html"'),
]
def page(lang,app=False):
  t=open(f'{SRC}/game.html',encoding='utf8').read()
  s=json.load(open(f'{SRC}/i18n/{lang}.json',encoding='utf8'))
  out=re.sub(r'\{\{T:(k\d+)\}\}',lambda m:s[m.group(1)],t)
  if app:
    for a,b in APP_RULES:
      if out.count(a)!=1: sys.exit(f'app rule not found exactly once in {lang}: {a[:60]}')
      out=out.replace(a,b)
  return out
def main():
  a=sys.argv[1:];check='--check' in a;app=None
  if '--app' in a: app=a[a.index('--app')+1]
  base=app or ROOT;bad=0
  for l in LANGS:
    s=page(l,bool(app));p=os.path.join(base,l,'index.html')
    if check:
      ok=open(p,encoding='utf8').read()==s;bad+=not ok;print(l,'OK' if ok else 'DIFFERENT')
    else:
      os.makedirs(os.path.dirname(p),exist_ok=True);open(p,'w',encoding='utf8').write(s);print('built',p)
  sys.exit(1 if bad else 0)
if __name__=='__main__':main()
