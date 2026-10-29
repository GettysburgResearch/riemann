#!/usr/bin/env python3
"""Freeze/plan or sequentially build the isolated .87386926 return.

Nothing runs Lean unless --execute is passed. Never writes qproject or PR94.
The build reuses only hash-checked local oleans from a filtered cache; their
historical source provenance still requires independent kernel replay.
"""
import argparse, hashlib, heapq, json, os, re, resource, shutil, signal, subprocess, sys, time
from pathlib import Path

ROOT=Path('/workspace/scratch/chain131-candidate')
BASE=Path('/workspace/scratch/pr94-prepared/submission')
CONTRACT=Path('/workspace/scratch/pr94-prepared/contract.json')
Q=Path('/workspace/scratch/qproject')
LEAN=Path('/workspace/scratch/lean-4.34.1-linux/bin/lean')
WORK=Path('/workspace/scratch/chain131-return-build')
GATES=[f'Candidate.ChainExtension.{s}' for s in ('Low130','Low131','High130','High131','Step_130','Step_131')]
TARGET='Candidate.ChainExtension.Main131'
PIN='e5a82f72d8ff39a3cc1ad044e6acd727e77a3fc4'

def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  while b:=f.read(1024*1024):h.update(b)
 return h.hexdigest()
def rel(m,ext='.lean'):return Path(*m.split('.')).with_suffix(ext)
def write_json(path,obj):
 tmp=path.with_suffix(path.suffix+'.tmp');tmp.write_text(json.dumps(obj,indent=2)+'\n');os.replace(tmp,path)
def fail(s):raise RuntimeError(s)
def stripped(s):
 # Lean comments can nest. Preserve newlines; strings do not occur in imports.
 out=[]; i=0; depth=0; string=False
 while i<len(s):
  if depth:
   if s.startswith('/-',i):depth+=1;i+=2
   elif s.startswith('-/',i):depth-=1;i+=2
   else:
    out.append('\n' if s[i]=='\n' else ' ');i+=1
  elif string:
   if s[i]=='\\' and i+1<len(s):out.extend('  ');i+=2
   elif s[i]=='"':out.append(' ');i+=1;string=False
   else:out.append('\n' if s[i]=='\n' else ' ');i+=1
  elif s.startswith('/-',i):depth=1;i+=2
  elif s.startswith('--',i):
   j=s.find('\n',i);i=len(s) if j<0 else j
  elif s[i]=='"':string=True;out.append(' ');i+=1
  else:out.append(s[i]);i+=1
 if depth or string:fail('unclosed Lean comment/string')
 return ''.join(out)
def imports(p):
 ans=[]
 for line in stripped(p.read_text()).splitlines():
  match=re.match(r'^\s*(?:public\s+)?import\s+(.+?)\s*$',line)
  if match:
   for m in match.group(1).split():
    if not re.fullmatch(r'[A-Za-z_][\w.]*',m):fail(f'unsupported import {m} in {p}')
    if m.startswith(('Candidate.','Submissions.')):ans.append(m)
 return ans

def snapshot_prepare():
 if WORK.exists():fail(f'{WORK} exists; preserve it and move it aside manually before new prepare')
 c=json.loads(CONTRACT.read_text())
 if c['head_sha']!=PIN or c['source_commit']!=PIN:fail('PR94 contract pin mismatch')
 gate=json.loads((ROOT/'gate-build-manifest.json').read_text())
 if sha(LEAN)!=gate['lean_binary_sha256']:fail('Lean binary mismatch')
 if set(x['module'] for x in gate['runs'] if x['exit']==0)!=set(GATES):fail('gate manifest incomplete')
 # Verify every pinned local source against the immutable contract.
 for m in c['build_order']:
  p=Path('src')/rel(m);expected=c['source_files'].get(str(p))
  if not expected or sha(BASE/p)!=expected:fail(f'baseline source/contract mismatch: {m}')
 WORK.mkdir(parents=True);shutil.copytree(BASE/'src',WORK/'src',copy_function=shutil.copyfile)
 staged={}
 for src,prefix,dst in [(ROOT/'return-overlay','Submissions.arvi_density.Return.',WORK/'src/Submissions/arvi_density/Return'),(ROOT/'returnd-overlay','Submissions.arvi_density.ReturnD.',WORK/'src/Submissions/arvi_density/ReturnD'),(ROOT/'src/Candidate/ChainExtension','Candidate.ChainExtension.',WORK/'src/Candidate/ChainExtension')]:
  for p in sorted(src.rglob('*.lean')):
   r=p.relative_to(src);m=prefix+'.'.join(r.with_suffix('').parts);q=dst/r;q.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,q);staged[m]=sha(q)
 # Contract graph for pinned files, actual syntax-derived graph for every staged file.
 deps={m:list(v) for m,v in c['module_dependencies'].items()}
 for m in staged:deps[m]=imports(WORK/'src'/rel(m))
 closure=set();stack=[TARGET]
 while stack:
  m=stack.pop()
  if m in closure:continue
  if m not in deps:fail(f'local import missing from graph: {m}')
  closure.add(m);stack.extend(deps[m])
 # Seed dirty with overlay and every source/olean mismatch; forward-close.
 dirty=set(staged)&closure;mismatch=[]
 for m in closure-dirty:
  source=WORK/'src'/rel(m);qsource=Q/'src'/rel(m);obj=Q/'.lake/build/lib/lean'/rel(m,'.olean')
  if not qsource.is_file() or sha(source)!=sha(qsource) or not obj.is_file():dirty.add(m);mismatch.append(m)
 again=True
 while again:
  again=False
  for m in closure-dirty:
   if set(deps[m])&dirty:dirty.add(m);again=True
 # Gate objects can be reused only if their local dependencies, other than gates,
 # are completely outside the dirty closure and the recorded bytes match.
 for m in GATES:
  if m not in closure:fail(f'gate absent from target closure: {m}')
  if sha(WORK/'src'/rel(m))!=gate['source_sha256'][m]:fail(f'gate source drift: {m}')
  obj=ROOT/'gate-olean'/rel(m,'.olean');record=next(x for x in gate['runs'] if x['module']==m)
  if not obj.is_file() or sha(obj)!=record.get('olean_sha256'):fail(f'gate olean drift: {m}')
  stack=list(deps[m]);seen=set()
  while stack:
   d=stack.pop()
   if d in seen:continue
   seen.add(d)
   if d in dirty and d not in GATES:fail(f'gate depends on changed local module: {m} -> {d}')
   stack.extend(deps[d])
 for m,h in gate['dependency_olean_sha256'].items():
  if sha(Q/'.lake/build/lib/lean'/rel(m,'.olean'))!=h:fail(f'gate dependency drift: {m}')
 build=dirty-set(GATES);reuse=closure-dirty
 # Topological order for ALL local nodes; every dependency must precede importer.
 degree={m:len(deps[m]) for m in closure};rev={m:[] for m in closure}
 for m in closure:
  for d in deps[m]:
   if d not in closure:fail(f'bad closure {m} {d}')
   rev[d].append(m)
 heap=[m for m,x in degree.items() if not x];heapq.heapify(heap);order=[]
 while heap:
  m=heapq.heappop(heap);order.append(m)
  for n in rev[m]:
   degree[n]-=1
   if degree[n]==0:heapq.heappush(heap,n)
 if len(order)!=len(closure):fail('local import cycle')
 plan={'schema':1,'pin':PIN,'target':TARGET,'lean_sha256':sha(LEAN),'contract_sha256':sha(CONTRACT),
       'gate_manifest_sha256':sha(ROOT/'gate-build-manifest.json'),'input_cache_sha256':sha(Q/'input-cache.json'),'driver_sha256':sha(Path(__file__).resolve()),
       'source_sha256':{m:sha(WORK/'src'/rel(m)) for m in sorted(closure)},
       'overlay_sha256':staged,'source_mismatch_or_missing_oleans':sorted(mismatch),
       'dependencies':{m:deps[m] for m in sorted(closure)},'order':order,
       'build_order':[m for m in order if m in build],'reuse':sorted(reuse),
       'reuse_olean_sha256':{m:sha(Q/'.lake/build/lib/lean'/rel(m,'.olean')) for m in sorted(reuse)},'gates':GATES,
       'warning':'Reused baseline oleans and package artifacts retain external provenance; full independent kernel replay remains necessary.'}
 write_json(WORK/'plan.json',plan)
 print(f'PREPARED {WORK}: closure={len(closure)} build={len(build)} reused={len(reuse)} gates={len(GATES)}; no Lean run')
 print('mismatched source/cache modules:',len(mismatch))

def ps_guard():
 text=subprocess.check_output(['ps','-eo','pid,args'],text=True)
 for line in text.splitlines():
  fields=line.strip().split(None,1)
  if len(fields)==2 and fields[0].isdigit() and int(fields[0])!=os.getpid() and re.search(r'(?:^|/)(?:nanoda_bin|leanchecker|lean)(?:\s|$)',fields[1]):
   fail('another Lean/kernel process appears active: '+line.strip())
 lim=Path('/sys/fs/cgroup/memory.max');cur=Path('/sys/fs/cgroup/memory.current')
 if lim.exists() and cur.exists():
  value=lim.read_text().strip()
  if value!='max' and int(value)-int(cur.read_text())<10*1024**3:fail('less than 10 GiB cgroup headroom; defer build')

def build(max_wall):
 overall_start=time.monotonic()
 def check_deadline():
  if time.monotonic()-overall_start>max_wall:fail(f'overall {max_wall}s budget reached; resume with --execute')
 plan=json.loads((WORK/'plan.json').read_text());ps_guard()
 if sha(LEAN)!=plan['lean_sha256'] or sha(CONTRACT)!=plan['contract_sha256'] or sha(Q/'input-cache.json')!=plan['input_cache_sha256'] or sha(Path(__file__).resolve())!=plan['driver_sha256']:fail('toolchain/contract/cache/driver fingerprint drift')
 if sha(ROOT/'gate-build-manifest.json')!=plan['gate_manifest_sha256']:fail('gate manifest drift')
 for m,h in plan['source_sha256'].items():
  if sha(WORK/'src'/rel(m))!=h:fail(f'frozen source drift: {m}')
 # Prevent unchecked placeholders in staged source, including early abort on edits.
 for m in plan['overlay_sha256']:
  s=stripped((WORK/'src'/rel(m)).read_text())
  if re.search(r'\b(?:sorry|admit|axiom|unsafe|native_decide)\b',s):fail(f'proof escape in {m}')
 cache=WORK/'cache';out=WORK/'olean';logs=WORK/'logs';cache.mkdir(exist_ok=True);out.mkdir(exist_ok=True);logs.mkdir(exist_ok=True)
 # Copy, not symlink, only permitted reuse artifacts into a clean filtered tree.
 manifest_path=WORK/'cache-manifest.json';existing=json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
 allowed_cache={rel(m,'.olean') for m in plan['reuse']+plan['gates']}
 allowed_out={rel(m,'.olean') for m in plan['build_order']}
 for root,allowed in ((cache,allowed_cache),(out,allowed_out)):
  for p in root.rglob('*.olean'):
   if p.is_symlink() or p.relative_to(root) not in allowed:fail(f'unexpected cache/output olean: {p}')
 gate=json.loads((ROOT/'gate-build-manifest.json').read_text())
 needed=sum(((ROOT/'gate-olean' if m in GATES else Q/'.lake/build/lib/lean')/rel(m,'.olean')).stat().st_size for m in plan['reuse']+plan['gates'] if not (cache/rel(m,'.olean')).is_file())
 available=shutil.disk_usage(WORK).free
 if available<needed+1024**3:fail(f'insufficient disk for isolated cache: need {needed+1024**3}, have {available}')
 for m in plan['reuse']+plan['gates']:
  check_deadline()
  src=(ROOT/'gate-olean' if m in GATES else Q/'.lake/build/lib/lean')/rel(m,'.olean');dst=cache/rel(m,'.olean')
  if not src.is_file():fail(f'missing reuse olean: {m}')
  current=sha(src)
  if m not in GATES and current!=plan['reuse_olean_sha256'][m]:fail(f'baseline olean changed after prepare: {m}')
  if m in GATES:
   expected=next(x['olean_sha256'] for x in gate['runs'] if x['module']==m)
   if current!=expected:fail(f'gate olean changed: {m}')
  if m in existing and existing[m]!=current:fail(f'reused artifact changed after snapshot: {m}')
  if not dst.is_file():
   dst.parent.mkdir(parents=True,exist_ok=True);tmp=dst.with_suffix('.olean.partial');shutil.copyfile(src,tmp)
   if sha(tmp)!=current:fail(f'olean copy changed: {m}')
   os.replace(tmp,dst)
  if sha(dst)!=current:fail(f'filtered cache object drift: {m}')
  existing[m]=current
 write_json(manifest_path,existing)
 libs=sorted(str(p.resolve()) for p in (Q/'.lake/packages').glob('*/.lake/build/lib/lean') if p.is_dir())
 if not libs:fail('missing package libraries')
 # Verify every package artifact recorded by the pinned external inventory,
 # with unique path resolution. Repeat after building to detect drift.
 def check_packages():
  inventory=json.loads((Q/'input-cache.json').read_text())['libraries']
  roots=[Path(x) for x in libs]
  for root in roots:
   for obj in root.rglob('*'):
    if obj.is_file() and (obj.name.endswith(('.olean','.olean.private','.olean.server','.ir','.ir.sig','.so'))) and str(obj.relative_to(root)) not in inventory:
     fail(f'unpinned executable package artifact: {obj}')
  for name,expected in inventory.items():
   check_deadline()
   found=[root/name for root in roots if (root/name).is_file()]
   if len(found)!=1 or sha(found[0])!=expected:fail(f'package inventory mismatch: {name}')
  return len(inventory)
 print('VERIFY PACKAGE INVENTORY',flush=True)
 package_count=check_packages();ps_guard()
 # Pin the actual toolchain libraries used by this execution and recheck at end.
 def toolchain_digest():
  h=hashlib.sha256();lib=LEAN.parent.parent/'lib'
  for p in sorted(x for x in lib.rglob('*') if x.is_file() and ('.olean' in x.name or '.so' in x.name or x.name.endswith('.ir.sig') or x.suffix in ('.a','.ir'))):
   check_deadline()
   h.update(str(p.relative_to(lib)).encode()+b'\0'+sha(p).encode()+b'\n')
  return h.hexdigest()
 toolchain_lib_hash=toolchain_digest();ps_guard()
 def dynamic_libs():
  listing=subprocess.check_output(['ldd',str(LEAN)],text=True)
  paths={str(Path(x).resolve()) for x in re.findall(r'(/[^\s()]+)\s*\(',listing)}
  if not paths:fail('could not fingerprint Lean dynamic libraries')
  return {p:sha(p) for p in sorted(paths)}
 dynamic_hashes=dynamic_libs()
 env=dict(os.environ,LEAN_PATH=':'.join([str(out),str(cache),*libs]))
 logpath=WORK/'run-manifest.json';run=json.loads(logpath.read_text()) if logpath.exists() else {'scope':'isolated changed closure using filtered baseline/gate cache','runs':[],'plan_sha256':sha(WORK/'plan.json')}
 if run['plan_sha256']!=sha(WORK/'plan.json'):fail('plan drift on resume')
 if 'toolchain_library_sha256' in run and run['toolchain_library_sha256']!=toolchain_lib_hash:fail('toolchain libraries changed across resumed runs')
 if 'dynamic_library_sha256' in run and run['dynamic_library_sha256']!=dynamic_hashes:fail('dynamic libraries changed across resumed runs')
 if run['runs'] and ('toolchain_library_sha256' not in run or 'dynamic_library_sha256' not in run):fail('resumed run lacks toolchain library provenance')
 run['toolchain_library_sha256']=toolchain_lib_hash;run['dynamic_library_sha256']=dynamic_hashes;write_json(logpath,run)
 done={x['module']:x for x in run['runs'] if x['status']=='passed'}
 for m in plan['build_order']:
  if time.monotonic()-overall_start>max_wall:fail(f'overall {max_wall}s budget reached; resume with --execute')
  ps_guard();source=WORK/'src'/rel(m);dest=out/rel(m,'.olean');dep_hash={}
  for d in plan['dependencies'][m]:
   p=out/rel(d,'.olean') if d in plan['build_order'] else cache/rel(d,'.olean')
   if not p.is_file():fail(f'missing ordered dependency {m} -> {d}')
   dep_hash[d]=sha(p)
  if m in done and dest.is_file() and done[m]['source_sha256']==sha(source) and done[m]['dependency_olean_sha256']==dep_hash and done[m]['olean_sha256']==sha(dest):
   print('REUSE BUILT',m,flush=True);continue
  if dest.exists():dest.unlink()
  dest.parent.mkdir(parents=True,exist_ok=True)
  cmd=[str(LEAN),'-j1','-o',str(dest),str(rel(m))]
  timeout=900 if ('.Rows.Admission' in m or '.Rows.Edges131' in m or m.endswith('.EdgeCertificates')) else 360
  log=logs/(m+'.log');start=time.monotonic();peak=0;reason=None
  print('START',m,flush=True)
  with log.open('w') as f:
   def limit_address_space():
    cap=12*1024**3;resource.setrlimit(resource.RLIMIT_AS,(cap,cap))
   p=subprocess.Popen(cmd,cwd=WORK/'src',env=env,stdout=f,stderr=subprocess.STDOUT,start_new_session=True,preexec_fn=limit_address_space)
   while p.poll() is None:
    try:
     status=Path(f'/proc/{p.pid}/status').read_text()
     k=re.search(r'^VmRSS:\s+(\d+)',status,re.M)
     if k:peak=max(peak,int(k.group(1)))
    except (FileNotFoundError,ProcessLookupError):pass
    if time.monotonic()-start>timeout:reason='timeout'
    if time.monotonic()-overall_start>max_wall:reason='overall_timeout'
    if peak>8*1024*1024:reason='sampled_rss_limit'
    if reason:
     try:os.killpg(p.pid,signal.SIGTERM)
     except ProcessLookupError:pass
     try:p.wait(timeout=5)
     except subprocess.TimeoutExpired:
      try:os.killpg(p.pid,signal.SIGKILL)
      except ProcessLookupError:pass
      p.wait()
     break
    time.sleep(.2)
  status='passed' if p.returncode==0 and reason is None and dest.is_file() else 'failed'
  record={'module':m,'status':status,'exit':p.returncode,'reason':reason,'timeout_seconds':timeout,
          'address_space_limit_bytes':12*1024**3,'sampled_rss_limit_kib':8*1024*1024,'peak_sampled_rss_kib':peak,'seconds':round(time.monotonic()-start,3),
          'source_sha256':sha(source),'dependency_olean_sha256':dep_hash,'command':cmd,'log':str(log)}
  if status=='passed':record['olean_sha256']=sha(dest)
  elif dest.exists():dest.unlink()
  run['runs'].append(record);write_json(logpath,run)
  print('DONE',m,status,record['seconds'],'s',flush=True)
  if status!='passed':fail(f'build stopped; inspect {log}')
 check_packages()
 for m,expected in existing.items():
  if sha(cache/rel(m,'.olean'))!=expected:fail(f'filtered cache changed during build: {m}')
 if toolchain_digest()!=toolchain_lib_hash or dynamic_libs()!=dynamic_hashes:fail('toolchain or dynamic library drift during build')
 target_log=(logs/(TARGET+'.log')).read_text()
 match=re.search(r'depends on axioms:\s*\[([^]]*)\]',target_log)
 if not match:fail('target axiom report not found; inspect '+str(logs/(TARGET+'.log')))
 axioms={x.strip() for x in match.group(1).split(',') if x.strip()}
 if axioms-{'propext','Classical.choice','Quot.sound'}:fail(f'unexpected target axioms: {sorted(axioms)}')
 run['target_axioms']=sorted(axioms);run['package_artifacts_verified']=package_count;run['toolchain_library_sha256']=toolchain_lib_hash;run['completed']=True
 write_json(logpath,run)
 print('ELABORATED',TARGET,'with axioms',sorted(axioms),'; independently replay full closure')

if __name__=='__main__':
 p=argparse.ArgumentParser();g=p.add_mutually_exclusive_group(required=True);g.add_argument('--prepare',action='store_true');g.add_argument('--execute',action='store_true');p.add_argument('--max-wall',type=int,default=3600,help='execution time budget in seconds; resume safely');a=p.parse_args()
 try:snapshot_prepare() if a.prepare else build(a.max_wall)
 except Exception as exc:print('ERROR:',exc,file=sys.stderr);sys.exit(1)
