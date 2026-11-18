"""Static, non-kernel Knausgård artifact inspection. Does not prove build success or soundness.
Run: python experiments/code/formal_839_scan.py /path/to/checkout
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
hits={k:[] for k in ['axiom','sorry','admit','native_decide','unsafe','implemented_by']};files={}
for p in sorted((root/'lean').rglob('*.lean')):
 s=p.read_text();c=strip(s);rel=str(p.relative_to(root));files[rel]=hashlib.sha256(p.read_bytes()).hexdigest()
 for token in hits:
  for m in re.finditer(r'(?<![\w\u0080-\uffff])'+token+r'(?![\w\u0080-\uffff])',c):hits[token].append({'file':rel,'line':c.count('\n',0,m.start())+1})
def stmts(p):
 s=strip(p.read_text());return {m.group(1):re.sub(r'\s+',' ',m.group(2)).strip() for m in re.finditer(r'\btheorem\s+([^\s:(]+)([\s\S]*?)\s*:=',s)}
cmp={}
for topic in ['839','673','Further','889','Ceilings']:
 a,b=stmts(root/f'lean/Challenge{topic}.lean'),stmts(root/f'lean/Solution{topic}.lean');cmp[topic]={'count':len(a),'all_matching':all(b.get(k)==v for k,v in a.items()),'different':[k for k,v in a.items() if b.get(k)!=v]}
check=subprocess.run(['sha256sum','-c','CHECKSUMS.sha256'],cwd=root,capture_output=True,text=True)
print(json.dumps({'kind':'static_source_scan_NOT_kernel_verification','repository':'https://github.com/kristianmk/839','commit':subprocess.check_output(['git','-C',str(root),'rev-parse','HEAD'],text=True).strip(),'tag':'v1','files':files,'tokens':hits,'challenge_solution_types':cmp,'checksums_manifest':{'files':len(check.stdout.splitlines()),'all_ok':check.returncode==0,'meaning':'Self-consistency with repository-supplied manifest, not correctness or independent provenance'},'upstream_required_commit':'fbdc36bbf17d20af3fd0447c6d1a8a02773c9844','upstream_patch_sha256':hashlib.sha256((root/'lean/upstream_relax.patch').read_bytes()).hexdigest()},indent=2,ensure_ascii=False))
