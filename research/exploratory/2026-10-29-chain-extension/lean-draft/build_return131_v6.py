#!/usr/bin/env python3
"""V6: sequential isolated .87386926 build with clean-cache release hints.

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

def release_fd(fd):
 try:os.posix_fadvise(fd,0,0,os.POSIX_FADV_DONTNEED)
 except (AttributeError,OSError):pass

def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  while b:=f.read(1024*1024):h.update(b)
  release_fd(f.fileno())
 return h.hexdigest()

def release_tree(root):
 if not root.exists():return
 for base,dirs,files in os.walk(root,followlinks=False):
  for name in files:
   path=Path(base)/name
   try:
    if path.is_symlink() or not path.is_file():continue
    with path.open('rb') as f:release_fd(f.fileno())
   except (PermissionError,FileNotFoundError,OSError):pass

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
 new=WORK/'plan-v6.json';source=WORK/'src-v6';oldsource=WORK/'src'
 if new.exists() or source.exists():fail('v6 plan or staged source exists; preserve it before preparing')
 parent=WORK/'plan-v5.json';v5run=WORK/'run-manifest-v5.json'
 plan=json.loads(parent.read_text());old=json.loads(v5run.read_text())
 if plan['pin']!=PIN or plan['target']!=TARGET or old['plan_sha256']!=sha(parent):fail('v5 parent plan/manifest mismatch')
 module='Submissions.arvi_density.Return.EdgeCertificates';q=rel(module)
 prev=(oldsource/q).read_bytes();fresh=(ROOT/'return-overlay/EdgeCertificates.lean').read_bytes()
 before='(0/1:ℝ)'.encode();after='(0:ℝ)'.encode()
 if prev.count(before)!=25 or prev.replace(before,after)!=fresh:fail('v6 source change is not exactly the 25 expected zero literal fixes')
 if sha(oldsource/q)!=plan['source_sha256'][module]:fail('v5 edge source drift')
 if shutil.disk_usage(WORK).free<2*1024**3:fail('need 2 GiB free to stage v6 source')
 shutil.copytree(oldsource,source,copy_function=shutil.copyfile)
 (source/q).write_bytes(fresh)
 if imports(source/q)!=plan['dependencies'][module]:fail('edge imports changed; regenerate closure rather than patching')
 plan['source_sha256'][module]=sha(source/q);plan['overlay_sha256'][module]=sha(source/q)
 affected={module};changed=True
 while changed:
  oldcount=len(affected)
  affected.update(m for m in plan['build_order'] if set(plan['dependencies'][m]) & affected)
  changed=len(affected)!=oldcount
 passed=[x for x in old['runs'] if x['status']=='passed']
 if len(passed)!=107 or len({x['module'] for x in passed})!=107:fail('unexpected v5 pass inventory')
 if affected & {x['module'] for x in passed}:fail('v5 passed output lies in changed reverse closure')
 if old.get('toolchain_library_sha256') is None or old.get('dynamic_library_sha256') is None:fail('v5 provenance missing')
 plan['v5_plan_sha256']=sha(parent);plan['v5_manifest_sha256']=sha(v5run)
 plan['v5_passed_olean_sha256']={x['module']:x['olean_sha256'] for x in passed}
 plan['v6_changed_module']=module;plan['v6_affected_reverse_closure']=sorted(affected)
 for m,digest in plan['v5_passed_olean_sha256'].items():
  if m not in plan['build_order'] or sha(WORK/'olean-v5'/rel(m,'.olean'))!=digest:fail(f'v5 passed object mismatch: {m}')
 plan['driver_sha256']=sha(Path(__file__).resolve());write_json(new,plan)
 print('PREPARED V6',new,'affected',len(affected),'passed',len(passed),'; no Lean run')

def ps_guard(check_memory=True):
 text=subprocess.check_output(['ps','-eo','pid,args'],text=True)
 for line in text.splitlines():
  fields=line.strip().split(None,1)
  if len(fields)==2 and fields[0].isdigit() and int(fields[0])!=os.getpid() and re.search(r'(?:^|/)(?:nanoda_bin|leanchecker|lean)(?:\s|$)',fields[1]):
   fail('another Lean/kernel process appears active: '+line.strip())
 lim=Path('/sys/fs/cgroup/memory.max');cur=Path('/sys/fs/cgroup/memory.current')
 if check_memory and lim.exists() and cur.exists():
  value=lim.read_text().strip()
  if value!='max' and int(value)-int(cur.read_text())<10*1024**3:fail('less than 10 GiB cgroup headroom; defer build')

def build(max_wall):
 overall_start=time.monotonic()
 def check_deadline():
  if time.monotonic()-overall_start>max_wall:fail(f'overall {max_wall}s budget reached; resume with --execute')
 plan=json.loads((WORK/'plan-v6.json').read_text());ps_guard(False)
 # Non-destructive hints only: clean, read-only cached pages may be evicted.
 # No theorem, source file, or artifact content is modified.
 for p in (WORK/'cache',WORK/'src-v6',Q/'.lake/packages',Q/'.lake/build/lib/lean',LEAN.parent.parent/'lib',Path('/workspace/scratch/direct-kernel-retune')):release_tree(p)
 ps_guard()
 if sha(LEAN)!=plan['lean_sha256'] or sha(CONTRACT)!=plan['contract_sha256'] or sha(Q/'input-cache.json')!=plan['input_cache_sha256'] or sha(Path(__file__).resolve())!=plan['driver_sha256']:fail('toolchain/contract/cache/driver fingerprint drift')
 if sha(ROOT/'gate-build-manifest.json')!=plan['gate_manifest_sha256']:fail('gate manifest drift')
 for m,h in plan['source_sha256'].items():
  if sha(WORK/'src-v6'/rel(m))!=h:fail(f'frozen source drift: {m}')
 # Prevent unchecked placeholders in staged source, including early abort on edits.
 for m in plan['overlay_sha256']:
  s=stripped((WORK/'src-v6'/rel(m)).read_text())
  if re.search(r'\b(?:sorry|admit|axiom|unsafe|native_decide)\b',s):fail(f'proof escape in {m}')
 cache=WORK/'cache';out=WORK/'olean-v6';logs=WORK/'logs-v6';cache.mkdir(exist_ok=True);out.mkdir(exist_ok=True);logs.mkdir(exist_ok=True)
 # Copy, not symlink, only permitted reuse artifacts into a clean filtered tree.
 manifest_path=WORK/'cache-manifest-v6.json';existing=json.loads(manifest_path.read_text()) if manifest_path.exists() else json.loads((WORK/'cache-manifest.json').read_text())
 if sha(WORK/'plan.json')!=plan['parent_plan_sha256'] or sha(WORK/'cache-manifest.json')!=plan['parent_cache_manifest_sha256']:fail('original evidence drift')
 allowed_cache={rel(m,'.olean') for m in plan['reuse']+plan['gates']}
 allowed_out={rel(m,'.olean') for m in plan['build_order']}
 def check_roots(require_links=False):
  # Lean resolves a whole top-level namespace from the first root.  Every
  # reusable module is linked into that one root; affected modules are regular
  # rebuilt files and can never be linked to the baseline cache.
  for root in (cache,out):
   for p in root.rglob('*'):
    q=p.relative_to(root)
    if p.is_symlink():
     if root!=out or q not in allowed_cache or p.resolve()!=(cache/q).resolve() or not p.is_file():
      fail(f'unexpected or incorrect symlink: {p}')
    elif p.is_file() and p.name.endswith(('.olean','.olean.private','.olean.server','.ir','.ir.sig','.so','.ilean')):
     if q not in (allowed_cache if root==cache else allowed_out):fail(f'unexpected cache/output artifact: {p}')
  if require_links:
   for m in plan['reuse']+plan['gates']:
    q=rel(m,'.olean');link=out/q;target=cache/q
    if not link.is_symlink() or link.resolve()!=target.resolve() or not target.is_file():fail(f'missing or changed reusable link: {link}')
    if sha(link)!=existing[m]:fail(f'reusable link target hash mismatch: {link}')
 check_roots()
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
  if not dst.is_file():fail(f'frozen original filtered-cache object missing: {m}')
  if sha(dst)!=current:fail(f'filtered cache object drift: {m}')
  existing[m]=current
 write_json(manifest_path,existing)
 if allowed_cache & allowed_out:fail('reused and rebuilt module paths overlap')
 for q in sorted(allowed_cache):
  link=out/q;target=cache/q
  if link.is_symlink():
   if link.resolve()!=target.resolve() or not link.is_file():fail(f'bad reusable link: {link}')
  elif link.exists():fail(f'reusable link destination occupied: {link}')
  else:
   link.parent.mkdir(parents=True,exist_ok=True);link.symlink_to(target)
 check_roots(True)
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
 env=dict(os.environ,LEAN_PATH=':'.join([str(out),*libs]))
 logpath=WORK/'run-manifest-v6.json'
 if sha(WORK/'plan-v5.json')!=plan['v5_plan_sha256'] or sha(WORK/'run-manifest-v5.json')!=plan['v5_manifest_sha256']:fail('v5 plan or evidence drift')
 if logpath.exists():run=json.loads(logpath.read_text())
 else:
  old=json.loads((WORK/'run-manifest-v5.json').read_text())
  if old.get('toolchain_library_sha256')!=toolchain_lib_hash or old.get('dynamic_library_sha256')!=dynamic_hashes:fail('v5 toolchain or dynamic library mismatch')
  old_passed=[x for x in old['runs'] if x['status']=='passed']
  if {x['module']:x['olean_sha256'] for x in old_passed}!=plan['v5_passed_olean_sha256']:fail('v5 pass inventory drift')
  copy_bytes=sum((WORK/'olean-v5'/rel(x['module'],'.olean')).stat().st_size for x in old_passed)
  if shutil.disk_usage(WORK).free < copy_bytes+1024**3:fail('insufficient disk to copy v5 outputs and retain 1 GiB')
  for rec in old_passed:
   m=rec['module'];src=WORK/'olean-v5'/rel(m,'.olean');dest=out/rel(m,'.olean')
   if sha(src)!=rec['olean_sha256'] or sha(WORK/'src-v6'/rel(m))!=rec['source_sha256']:fail(f'v5 pass/source changed: {m}')
   if dest.is_symlink():fail(f'v5 copy destination is a symlink: {dest}')
   dest.parent.mkdir(parents=True,exist_ok=True);tmp=dest.with_suffix('.olean.tmp')
   shutil.copyfile(src,tmp)
   with tmp.open('rb') as f:os.fsync(f.fileno());release_fd(f.fileno())
   if sha(tmp)!=rec['olean_sha256']:fail(f'v5 copy mismatch: {m}')
   os.replace(tmp,dest)
  run={'scope':'isolated changed closure with hash-verified v5 passed modules', 'runs':old_passed, 'plan_sha256':sha(WORK/'plan-v6.json'), 'v5_manifest_sha256':plan['v5_manifest_sha256'],'toolchain_library_sha256':toolchain_lib_hash,'dynamic_library_sha256':dynamic_hashes}
 if run['plan_sha256']!=sha(WORK/'plan-v6.json'):fail('plan drift on resume')
 if 'toolchain_library_sha256' in run and run['toolchain_library_sha256']!=toolchain_lib_hash:fail('toolchain libraries changed across resumed runs')
 if 'dynamic_library_sha256' in run and run['dynamic_library_sha256']!=dynamic_hashes:fail('dynamic libraries changed across resumed runs')
 if run['runs'] and ('toolchain_library_sha256' not in run or 'dynamic_library_sha256' not in run):fail('resumed run lacks toolchain library provenance')
 run['toolchain_library_sha256']=toolchain_lib_hash;run['dynamic_library_sha256']=dynamic_hashes;write_json(logpath,run)
 done={x['module']:x for x in run['runs'] if x['status']=='passed'}
 for m in plan['build_order']:
  if time.monotonic()-overall_start>max_wall:fail(f'overall {max_wall}s budget reached; resume with --execute')
  ps_guard(False)
  lim=Path('/sys/fs/cgroup/memory.max');cur=Path('/sys/fs/cgroup/memory.current')
  if lim.exists() and lim.read_text().strip()!='max' and int(lim.read_text())-int(cur.read_text())<10*1024**3:
   print('RELEASE CLEAN FILE CACHE',flush=True)
   for pth in (cache,out,Q/'.lake/packages',LEAN.parent.parent/'lib'):release_tree(pth)
  ps_guard()
  if shutil.disk_usage(WORK).free < 1024**3:fail('less than 1 GiB free disk; defer build')
  source=WORK/'src-v6'/rel(m);dest=out/rel(m,'.olean');dep_hash={}
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
    resource.setrlimit(resource.RLIMIT_AS,(resource.RLIM_INFINITY,resource.RLIM_INFINITY))
   p=subprocess.Popen(cmd,cwd=WORK/'src-v6',env=env,stdout=f,stderr=subprocess.STDOUT,start_new_session=True,preexec_fn=limit_address_space)
   while p.poll() is None:
    try:
     status=Path(f'/proc/{p.pid}/status').read_text()
     k=re.search(r'^VmRSS:\s+(\d+)',status,re.M)
     if k:peak=max(peak,int(k.group(1)))
    except (FileNotFoundError,ProcessLookupError):pass
    if time.monotonic()-start>timeout:reason='timeout'
    if time.monotonic()-overall_start>max_wall:reason='overall_timeout'
    if peak>8*1024*1024:reason='sampled_rss_limit'
    if lim.exists() and lim.read_text().strip()!='max' and int(lim.read_text())-int(cur.read_text())<1024**3:reason='cgroup_remaining_below_1gib'
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
          'address_space_limit_bytes':None,'sampled_rss_limit_kib':8*1024*1024,'peak_sampled_rss_kib':peak,'seconds':round(time.monotonic()-start,3),
          'source_sha256':sha(source),'dependency_olean_sha256':dep_hash,'command':cmd,'log':str(log)}
  if status=='passed':
   with dest.open('rb') as f:os.fsync(f.fileno());release_fd(f.fileno())
   record['olean_sha256']=sha(dest)
  elif dest.exists():dest.unlink()
  run['runs'].append(record);write_json(logpath,run)
  print('DONE',m,status,record['seconds'],'s',flush=True)
  if status!='passed':fail(f'build stopped; inspect {log}')
 check_packages()
 check_roots(True)
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
