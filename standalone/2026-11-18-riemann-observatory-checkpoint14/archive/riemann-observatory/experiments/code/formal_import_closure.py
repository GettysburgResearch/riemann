"""Static Lean import-closure estimate, blanking comments/strings.
Not elaboration or a build guarantee. CLI: repo_path [module ...]; default RankTrace.
Handles standalone/dotted names and public/meta import headers.
"""
from pathlib import Path
import re,json,sys
def strip(s):
 a=list(s);i=0;depth=0
 while i<len(s):
  if depth:
   if s.startswith('/-',i):depth+=1;a[i:i+2]='  ';i+=2
   elif s.startswith('-/',i):depth-=1;a[i:i+2]='  ';i+=2
   else:
    if s[i]!='\n':a[i]=' '
    i+=1
  elif s.startswith('/-',i):depth=1;a[i:i+2]='  ';i+=2
  elif s.startswith('--',i):
   j=s.find('\n',i);j=len(s) if j<0 else j;a[i:j]=' '*(j-i);i=j
  elif s[i]=='"':
   a[i]=' ';i+=1
   while i<len(s):
    if s[i]=='\\':
     a[i]=' ';i+=1
     if i<len(s):a[i]=' ';i+=1
    elif s[i]=='"':a[i]=' ';i+=1;break
    else:
     if s[i]!='\n':a[i]=' '
     i+=1
  else:i+=1
 return ''.join(a)

root=Path(sys.argv[1]);targets=sys.argv[2:] or ['Zeta23.LinAlg.RankTrace']
roots=[root,root/'comparator']+[p for p in (root/'.lake/packages').iterdir() if p.is_dir()]
seen={};todo=list(targets);missing=set()
while todo:
 m=todo.pop()
 if m in seen or m in missing:continue
 p=next((r/Path(*m.split('.')).with_suffix('.lean') for r in roots if (r/Path(*m.split('.')).with_suffix('.lean')).exists()),None)
 if p is None:missing.add(m);continue
 imports=[]
 for line in strip(p.read_text()).splitlines():
  match=re.match(r'^(?:(?:public|meta)\s+)*import\s+(.+)',line)
  if match:imports.extend(re.findall(r'[A-Za-z_][A-Za-z_0-9]*(?:\.[A-Za-z_][A-Za-z_0-9]*)*',match.group(1)))
 seen[m]=imports;todo.extend(imports)
built={m for m in seen if any((r/'.lake/build/lib/lean'/Path(*m.split('.')).with_suffix('.olean')).exists() for r in roots)}
print(json.dumps({'kind':'static_module_import_closure_estimate_not_elaboration','targets':targets,'source_modules':len(seen),'contains_aggregate_Mathlib':'Mathlib' in seen,'built_module_oleans':len(built),'remaining_approx':len(set(seen)-built),'by_prefix':{pref:sum(m.startswith(pref+'.') or m==pref for m in seen) for pref in ['Zeta23','Mathlib','Aesop','Batteries','Qq','ProofWidgets','LeanSearchClient','ImportGraph']},'externally_supplied_or_unresolved':sorted(missing),'imports':seen},indent=2))
