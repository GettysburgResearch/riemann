"""Static, non-kernel Lean artifact inspection. Does not prove build success or soundness.
Run: python experiments/code/formal_round2_scan.py /path/to/checkout
Outputs JSON to stdout. Nested Lean comments and quoted strings are blanked, preserving lines.
"""
import pathlib,sys,re,json,hashlib,subprocess
root=pathlib.Path(sys.argv[1])
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
def git(*args):return subprocess.check_output(['git','-C',str(root),*args],text=True).strip()
files={};hits={k:[] for k in ['axiom','sorry','admit','native_decide','unsafe','implemented_by','run_meta','initialize','addDecl']}
for p in sorted(root.rglob('*.lean')):
 if '.lake' in p.parts:continue
 s=p.read_text();c=strip(s);rel=str(p.relative_to(root));files[rel]={'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'lines':s.count('\n')+1}
 for token in hits:
  for m in re.finditer(r'(?<![\w\u0080-\uffff])'+token+r'(?![\w\u0080-\uffff])',c):hits[token].append({'file':rel,'line':c.count('\n',0,m.start())+1})
def statements(p):
 s=strip(p.read_text());out={}
 # Trusted challenge and solution top declarations contain no local theorem declarations.
 for m in re.finditer(r'\btheorem\s+([^\s:(]+)([\s\S]*?)\s*:=',s):out[m.group(1)]=re.sub(r'\s+',' ',m.group(2)).strip()
 return out
cmp={}
for topic in ['', '/Multiplicity','/XiPrime']:
 ch=root/'comparator'/('Challenge'+topic+'.lean');sol=root/'comparator'/('Solution'+topic+'.lean')
 if ch.exists() and sol.exists():
  a,b=statements(ch),statements(sol);cmp[topic or 'base']={'challenge_theorem_count':len(a),'all_same_text_after_whitespace':all(b.get(n)==v for n,v in a.items()),'different_or_absent':[n for n,v in a.items() if b.get(n)!=v]}
# Definition equality, limited to explicitly inspected count declarations.
count_defs={}
for name in ['IsNontrivialZero','zeroMult','zerosIn','Ncount','Ndist','N0','N0star','N0simple','Nsimple']:
 def finddef(p):
  s=strip(p.read_text());m=re.search(r'\bdef\s+'+name+r'\b([\s\S]*?)(?=\n\s*(?:def|lemma|theorem|section|end|structure|@\[)|\Z)',s)
  return re.sub(r'\s+',' ',m.group(0)).strip() if m else None
 a=finddef(root/'comparator/ChallengeDeps.lean');b=finddef(root/'Zeta23/Statement.lean');count_defs[name]={'text_equal':a==b,'definition':a}
print(json.dumps({'kind':'static_source_inspection_NOT_kernel_verification','date':'2026-11-17','repo':'https://github.com/anthropics/zeta-23-lean','commit':git('rev-parse','HEAD'),'tag_object':git('rev-parse','v1.0'),'lean_file_count':len(files),'lean_lines':sum(x['lines'] for x in files.values()),'tokens':hits,'challenge_solution_statements':cmp,'count_definitions':count_defs,'files':files},indent=2,ensure_ascii=False))
