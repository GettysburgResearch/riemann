"""Static source import inventory, including BARE module names such as Mathlib.
Not Lean elaboration or proof checking. Outputs one summary per requested library target.
"""
from pathlib import Path
import re,json,subprocess,sys
B=Path(__file__).resolve().parents[2]
R=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else B/'sources/formal_round2/zeta-23-lean-v1.0'
roots=[R,R/'comparator']+[p for p in (R/'.lake/packages').iterdir() if p.is_dir()]
index={}
for root in roots:
 for path in root.rglob('*.lean'):
  if '.lake' in path.relative_to(root).parts:continue
  mod='.'.join(path.relative_to(root).with_suffix('').parts)
  index.setdefault(mod,path)
def uncomment(text):
 out=[];i=0;depth=0
 while i<len(text):
  if text.startswith('/-',i):depth+=1;i+=2;continue
  if depth:
   if text.startswith('-/',i):depth-=1;i+=2
   else:
    if text[i]=='\n':out.append('\n')
    i+=1
  elif text.startswith('--',i):
   while i<len(text) and text[i]!='\n':i+=1
  else:out.append(text[i]);i+=1
 return ''.join(out)
def imports(path):
 mods=[]
 for line in uncomment(path.read_text()).splitlines():
  mat=re.match(r'^\s*(?:public\s+)?(?:meta\s+)?import\s+(.+)$',line)
  if mat:mods.extend(re.findall(r'\b[A-Za-z_][A-Za-z_0-9]*(?:\.[A-Za-z_][A-Za-z_0-9]*)*\b',mat.group(1)))
 return mods
memo={}
def closure(target):
 seen=set();missing=set();todo=[target];bare=[]
 while todo:
  m=todo.pop()
  if m in seen or m in missing:continue
  if m not in index:missing.add(m);continue
  seen.add(m);path=index[m];deps=memo.setdefault(m,imports(path))
  if 'Mathlib' in deps:bare.append({'module':m,'path':str(path.relative_to(R)) if path.is_relative_to(R) else str(path),'import':'Mathlib'})
  todo.extend(deps)
 return {'target':target,'source_modules':len(seen),'mathlib_modules':sum(m=='Mathlib' or m.startswith('Mathlib.') for m in seen),'zeta23_modules':sum(m=='Zeta23' or m.startswith('Zeta23.') for m in seen),'bare_Mathlib_imports_in_cone':sorted(bare,key=lambda r:r['module']),'contains_full_Mathlib_aggregate':'Mathlib' in seen,'unresolved_or_toolchain_modules':sorted(missing)}
out={'kind':'static_source_import_inventory_NOT_elaboration','commit':subprocess.check_output(['git','-C',str(R),'rev-parse','HEAD'],text=True).strip(),'mathlib_commit':subprocess.check_output(['git','-C',str(R/'.lake/packages/mathlib'),'rev-parse','HEAD'],text=True).strip(),'targets':[closure(t) for t in ['Zeta23.FinalMult','Zeta23.ThmD.Mult','Solution.Multiplicity']],'limitation':'Includes bare module names. Regex/static inventory only; actual Lake jobs may differ. Does not start a build or validate proof terms.'}
(B/'experiments/results/formal_semantic_import_closure.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({**out,'targets':[{k:v for k,v in row.items() if k!='unresolved_or_toolchain_modules'} for row in out['targets']]},indent=2))
