#!/usr/bin/env python3
"""One-time: rebuild src/game.html + src/i18n/*.json from the built {lang}/index.html pages.
Every span where any language differs from English becomes a {{T:kNNNN}} placeholder."""
import re, json, difflib, os, sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANGS=['en','ar','it','es','zh','ru','ja','tr']
TOK=re.compile(r'\w+|\s+|[^\w\s]',re.U)
pages={l:open(f'{ROOT}/{l}/index.html',encoding='utf8').read().split('\n') for l in LANGS}
n=len(pages['en']); assert all(len(pages[l])==n for l in LANGS),'line counts differ'
def mapper(ops):
  def m(p,end):
    if end:
      c=[j2 for t,i1,i2,j1,j2 in ops if t!='equal' and i2==p]
      if c: return max(c)
    else:
      c=[j1 for t,i1,i2,j1,j2 in ops if t!='equal' and i1==p]
      if c: return min(c)
    for t,i1,i2,j1,j2 in ops:
      if t=='equal' and i1<=p<=i2: return j1+(p-i1)
    raise ValueError(p)
  return m
tmpl=[];strings={l:{} for l in LANGS};k=0
for i in range(n):
  en=pages['en'][i]
  if all(pages[l][i]==en for l in LANGS): tmpl.append(en);continue
  et=TOK.findall(en);toks={};ops={};iv=[]
  for l in LANGS[1:]:
    lt=TOK.findall(pages[l][i]);toks[l]=lt
    o=difflib.SequenceMatcher(None,et,lt,autojunk=False).get_opcodes();ops[l]=o
    iv+=[(a,b) for t,a,b,_,_ in o if t!='equal']
  iv.sort();mg=[]
  for a,b in iv:
    if mg and a<=mg[-1][1]: mg[-1][1]=max(mg[-1][1],b)
    else: mg.append([a,b])
  out=[];pos=0
  for a,b in mg:
    out.append(''.join(et[pos:a]));k+=1;key=f'k{k:04d}';out.append('{{T:'+key+'}}')
    strings['en'][key]=''.join(et[a:b])
    for l in LANGS[1:]:
      m=mapper(ops[l]);strings[l][key]=''.join(toks[l][m(a,False):m(b,True)])
    pos=b
  out.append(''.join(et[pos:]));tmpl.append(''.join(out))
open(f'{ROOT}/src/game.html','w',encoding='utf8').write('\n'.join(tmpl))
for l in LANGS: json.dump(strings[l],open(f'{ROOT}/src/i18n/{l}.json','w',encoding='utf8'),ensure_ascii=False,indent=1)
print('keys',k)
