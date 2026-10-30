"""Fresh kernel replay of the isolated chain131 closure, with input checks.

The checker uses the same Lean kernel: it is not an external verifier or
tracker admission.  Run only after v6 postflight; it preserves prior logs.
RSS and cgroup guards are sampled and cannot guarantee avoiding every OOM.
"""
import hashlib,json,os,re,signal,subprocess,sys,time
from pathlib import Path
if not __debug__: raise RuntimeError('optimized Python disables required assertions')
root=Path('/workspace/scratch/chain131-return-build')
lean=Path('/workspace/scratch/lean-4.34.1-linux/bin')
qproject=Path('/workspace/scratch/qproject')
candidate=Path('/workspace/scratch/chain131-candidate')
packet=Path('/workspace/riemann/research/exploratory/2026-10-29-chain-extension/lean-draft')
log=packet/'fresh-replay.log';input_file=packet/'fresh-replay-inputs.json';result_file=packet/'fresh-replay-result.json'
if any(p.exists() for p in (log,input_file,result_file)):raise RuntimeError('preserve existing fresh replay evidence')
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
  try:os.posix_fadvise(f.fileno(),0,0,os.POSIX_FADV_DONTNEED)
  except (AttributeError,OSError):pass
 return h.hexdigest()
def rel(m,ext='.olean'):return Path(*m.split('.')).with_suffix(ext)
def release_tree(rootpath):
 if not rootpath.exists():return
 for base,dirs,files in os.walk(rootpath,followlinks=False):
  for name in files:
   path=Path(base)/name
   try:
    if path.is_symlink() or not path.is_file():continue
    with path.open('rb') as f:os.posix_fadvise(f.fileno(),0,0,os.POSIX_FADV_DONTNEED)
   except (AttributeError,PermissionError,FileNotFoundError,OSError):pass
def no_other_workers():
 for line in subprocess.check_output(['ps','-eo','pid,args'],text=True).splitlines():
  fields=line.strip().split(None,1)
  if len(fields)==2 and fields[0].isdigit() and int(fields[0])!=os.getpid() and re.search(r'(?:^|/)(?:nanoda_bin|con-ron|lean4export|leanchecker|lean)(?:\s|$)',fields[1]):
   raise RuntimeError('another Lean/kernel process is active: '+line.strip())
def headroom(minimum):
 lim=Path('/sys/fs/cgroup/memory.max');cur=Path('/sys/fs/cgroup/memory.current')
 if lim.exists() and cur.exists() and lim.read_text().strip()!='max':
  if int(lim.read_text())-int(cur.read_text())<minimum:raise RuntimeError('insufficient cgroup memory headroom')
def toolchain_digest():
 h=hashlib.sha256();lib=lean.parent/'lib'
 for p in sorted(x for x in lib.rglob('*') if x.is_file() and ('.olean' in x.name or '.so' in x.name or x.name.endswith('.ir.sig') or x.suffix in ('.a','.ir'))):
  h.update(str(p.relative_to(lib)).encode()+b'\0'+sha(p).encode()+b'\n')
 return h.hexdigest()
def dynamic_libs(binary=lean/'lean'):
 listing=subprocess.check_output(['ldd',str(binary)],text=True)
 paths={str(Path(x).resolve()) for x in re.findall(r'(/[^\s()]+)\s*\(',listing)}
 if not paths:raise RuntimeError('could not fingerprint Lean dynamic libraries')
 return {p:sha(p) for p in sorted(paths)}
manifest_path=root/'run-manifest-v6.json';plan_path=root/'plan-v6.json'
manifest=json.loads(manifest_path.read_text());plan=json.loads(plan_path.read_text())
assert manifest.get('completed') is True and manifest.get('plan_sha256')==sha(plan_path), 'v6 postflight or plan binding missing'
target=plan['target'];assert target=='Candidate.ChainExtension.Main131'
assert sha(lean/'lean')==plan['lean_sha256']
assert sha(qproject/'input-cache.json')==plan['input_cache_sha256']
assert sha(candidate/'gate-build-manifest.json')==plan['gate_manifest_sha256']
assert sha(Path('/workspace/scratch/pr94-prepared/contract.json'))==plan['contract_sha256']
libs=sorted(str(p.resolve()) for p in (qproject/'.lake/packages').glob('*/.lake/build/lib/lean') if p.is_dir())
if not libs:raise RuntimeError('package library roots absent')
expected_packages=json.loads((qproject/'input-cache.json').read_text())['libraries']
passed=[x for x in manifest['runs'] if x['status']=='passed']
assert len(passed)==len(plan['build_order']) and {x['module'] for x in passed}==set(plan['build_order']), 'passed module inventory mismatch'
gate=json.loads((candidate/'gate-build-manifest.json').read_text())
expected_cache=dict(plan['reuse_olean_sha256'])
expected_cache.update({x['module']:x['olean_sha256'] for x in gate['runs'] if x['module'] in plan['gates']})
assert set(expected_cache)==set(plan['reuse']+plan['gates'])
assert json.loads((root/'cache-manifest-v6.json').read_text())==expected_cache
expected_sources=plan['source_sha256'];out=root/'olean-v6';cache=root/'cache'
allowed_cache={rel(m) for m in expected_cache};allowed_out={rel(m) for m in plan['build_order']}
def verify_inputs():
 if sha(manifest_path)!=manifest_sha or sha(plan_path)!=plan_sha:raise RuntimeError('manifest/plan changed')
 if sha(Path(__file__).resolve())!=runner_sha:raise RuntimeError('replay runner changed')
 if dynamic_libs(lean/'leanchecker')!=checker_dynamic:raise RuntimeError('checker dynamic libraries changed')
 if sha(lean/'lean')!=plan['lean_sha256'] or sha(lean/'leanchecker')!=checker_sha:raise RuntimeError('compiler/checker changed')
 if sha(qproject/'input-cache.json')!=plan['input_cache_sha256'] or sha(candidate/'gate-build-manifest.json')!=plan['gate_manifest_sha256']:raise RuntimeError('inventory or gate manifest changed')
 if sha(Path('/workspace/scratch/pr94-prepared/contract.json'))!=plan['contract_sha256']:raise RuntimeError('contract changed')
 for m,h in expected_sources.items():
  if sha(root/'src-v6'/rel(m,'.lean'))!=h:raise RuntimeError('source drift: '+m)
 for m,h in expected_cache.items():
  link=out/rel(m);obj=cache/rel(m)
  if not link.is_symlink() or link.resolve()!=obj.resolve() or not obj.is_file() or sha(obj)!=h:raise RuntimeError('cache link/hash drift: '+m)
 for x in passed:
  m=x['module'];obj=out/rel(m)
  if obj.is_symlink() or not obj.is_file() or sha(obj)!=x['olean_sha256']:raise RuntimeError('built object drift: '+m)
  if sha(root/'src-v6'/rel(m,'.lean'))!=x['source_sha256']:raise RuntimeError('built source drift: '+m)
  for d,h in x['dependency_olean_sha256'].items():
   if sha(out/rel(d))!=h:raise RuntimeError('dependency drift: '+m+' -> '+d)
 for base in (out,cache):
  for obj in base.rglob('*'):
   r=obj.relative_to(base)
   if obj.is_symlink():
    if base!=out or r not in allowed_cache or obj.resolve()!=(cache/r).resolve() or not obj.is_file():raise RuntimeError('unexpected artifact symlink: '+str(obj))
   elif obj.is_file() and obj.name.endswith(('.olean','.olean.private','.olean.server','.ir','.ir.sig','.so','.ilean')):
    if r not in (allowed_out if base==out else allowed_cache):raise RuntimeError('unexpected artifact: '+str(obj))
 roots=[Path(x) for x in libs]
 for lib in roots:
  for obj in lib.rglob('*'):
   if obj.is_file() and obj.name.endswith(('.olean','.olean.private','.olean.server','.ir','.ir.sig','.so')) and str(obj.relative_to(lib)) not in expected_packages:
    raise RuntimeError('unpinned package artifact: '+str(obj))
 for name,h in expected_packages.items():
  found=[lib/name for lib in roots if (lib/name).is_file()]
  if len(found)!=1 or sha(found[0])!=h:raise RuntimeError('package inventory mismatch: '+name)
 if toolchain_digest()!=manifest['toolchain_library_sha256'] or dynamic_libs()!=manifest['dynamic_library_sha256']:raise RuntimeError('toolchain or dynamic libraries changed')
no_other_workers()
for tree in (cache,root/'src-v6',qproject/'.lake/packages',lean.parent/'lib'):release_tree(tree)
headroom(10*1024**3)
manifest_sha=sha(manifest_path);plan_sha=sha(plan_path);checker_sha=sha(lean/'leanchecker');runner_sha=sha(Path(__file__).resolve());checker_dynamic=dynamic_libs(lean/'leanchecker')
print('VERIFY INPUTS BEFORE REPLAY',flush=True);verify_inputs();no_other_workers();headroom(10*1024**3)
env=dict(os.environ,LEAN_PATH=':'.join([str(out),*libs]),PATH=str(lean)+':'+os.environ['PATH'])
cmd=[str(lean/'leanchecker'),'--fresh','--verbose',target]
source=root/'src-v6'/rel(target,'.lean');obj=out/rel(target)
inputs={'command':cmd,'timeout_seconds':4200,'sampled_rss_limit_kib':13*1024**2,'startup_headroom_bytes':10*1024**3,'emergency_cgroup_headroom_bytes':1024**3,'lean_sha256':sha(lean/'lean'),'leanchecker_sha256':checker_sha,'target_source_sha256':sha(source),'target_olean_sha256':sha(obj),'plan_sha256':plan_sha,'build_manifest_sha256':manifest_sha,'runner_sha256':runner_sha,'checker_dynamic_library_sha256':checker_dynamic,'package_inventory_entries':len(expected_packages),'lean_path':env['LEAN_PATH'],'cgroup_events_before':Path('/sys/fs/cgroup/memory.events').read_text()}
input_file.write_text(json.dumps(inputs,indent=2)+'\n')
start=time.monotonic();peak=0;reason=None
with log.open('x') as f:
 p=subprocess.Popen(cmd,cwd=root/'src-v6',env=env,stdout=f,stderr=subprocess.STDOUT,start_new_session=True)
 while p.poll() is None:
  try:
   for line in Path(f'/proc/{p.pid}/status').read_text().splitlines():
    if line.startswith('VmRSS:'):peak=max(peak,int(line.split()[1]));break
  except FileNotFoundError:pass
  if peak>13*1024**2:reason='sampled_rss_limit'
  elif time.monotonic()-start>4200:reason='timeout'
  else:
   try:headroom(1024**3)
   except RuntimeError:reason='cgroup_remaining_below_1gib'
  if reason:
   try:os.killpg(p.pid,signal.SIGTERM)
   except ProcessLookupError:pass
   try:p.wait(timeout=5)
   except subprocess.TimeoutExpired:
    try:os.killpg(p.pid,signal.SIGKILL)
    except ProcessLookupError:pass
    p.wait()
   break
  time.sleep(.5)
 status=p.wait()
postflight_error=None
try:
 print('VERIFY INPUTS AFTER REPLAY',flush=True);verify_inputs()
except Exception as exc:postflight_error=str(exc)
result={'exit_code':status,'termination_reason':reason,'postflight_error':postflight_error,'seconds':round(time.monotonic()-start,3),'sampled_peak_rss_kib':peak,'log_sha256':sha(log),'cgroup_events_after':Path('/sys/fs/cgroup/memory.events').read_text()}
result_file.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2),flush=True)
sys.exit(0 if status==0 and reason is None and postflight_error is None else 1)
