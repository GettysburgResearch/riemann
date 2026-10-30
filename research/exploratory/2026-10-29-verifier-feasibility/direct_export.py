"""Bounded, unprotected export of a single theorem's full dependency closure.

This is exploratory evidence only. It does not reproduce tracker Comparator,
sandbox, challenge freeze or admission. It preserves incomplete output on failure.
"""
import hashlib,json,os,resource,shutil,signal,subprocess,sys,time
from pathlib import Path
root=Path('/workspace/scratch/retune_project')
out=Path('/workspace/scratch/direct-kernel-retune')
exporter=Path('/workspace/scratch/retune-exporter-src/.lake/build/bin/lean4export')
leanbin=Path('/workspace/scratch/lean-4.34.1-linux/bin')
plan=root/'import-plan-v3.json'
obj=root/'isolated-olean-v2/Candidate/Main.olean'
res=root/'lean-results-v2/environment.json'
assert not out.exists(), 'preserve previous experiment output'
out.mkdir()
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''): h.update(b)
 return h.hexdigest()
env=dict(os.environ)
env['LEAN_PATH']=json.loads(res.read_text())['lean_path']
env['PATH']=str(leanbin)+os.pathsep+env['PATH']
env['LEAN_NUM_THREADS']='1'
cmd=[str(exporter),'Candidate.Main','--','Candidate.bound','propext','Classical.choice','Quot.sound']
limit=4*1024**3
rss_limit=13*1024**2
seconds=3600
def child_limits(): resource.setrlimit(resource.RLIMIT_FSIZE,(limit,limit))
inputs={'exporter_sha256':sha(exporter),'lean_sha256':sha(leanbin/'lean'),'plan_sha256':sha(plan),'candidate_olean_sha256':sha(obj),'candidate_source_sha256':sha(root/'src/Candidate/Main.lean'),'lean_path':env['LEAN_PATH'],'command':cmd,'max_output_bytes':limit,'max_sampled_rss_kib':rss_limit,'timeout_seconds':seconds,'disk_min_free_bytes':1024**3,'cwd':str(root/'src'),'cgroup_events_before':Path('/sys/fs/cgroup/memory.events').read_text()}
(out/'inputs.json').write_text(json.dumps(inputs,indent=2)+'\n')
start=time.monotonic(); peak=0; reason=None
with (out/'candidate.export.partial').open('wb') as output, (out/'export.stderr.log').open('wb') as err:
 p=subprocess.Popen(cmd,cwd=root/'src',env=env,stdout=output,stderr=err,start_new_session=True,preexec_fn=child_limits)
 while p.poll() is None:
  try:
   lines=Path(f'/proc/{p.pid}/status').read_text().splitlines()
   for line in lines:
    if line.startswith('VmRSS:'): peak=max(peak,int(line.split()[1])); break
  except (FileNotFoundError,ProcessLookupError): pass
  if peak>rss_limit: reason='rss_limit'
  elif shutil.disk_usage(out).free<1024**3: reason='disk_reserve'
  elif time.monotonic()-start>seconds: reason='timeout'
  if reason:
   os.killpg(p.pid,signal.SIGTERM)
   try:p.wait(timeout=5)
   except subprocess.TimeoutExpired:os.killpg(p.pid,signal.SIGKILL);p.wait()
   break
  time.sleep(0.5)
 status=p.wait()
partial=out/'candidate.export.partial'
metrics={'exit_code':status,'termination_reason':reason,'wall_seconds':round(time.monotonic()-start,3),'sampled_peak_rss_kib':peak,'output_bytes':partial.stat().st_size,'stderr_sha256':sha(out/'export.stderr.log'),'cgroup_events_after':Path('/sys/fs/cgroup/memory.events').read_text()}
if status==0 and reason is None:
 partial.rename(out/'candidate.export')
 metrics['output_sha256']=sha(out/'candidate.export')
(out/'export-result.json').write_text(json.dumps(metrics,indent=2)+'\n')
print(json.dumps(metrics,indent=2),flush=True)
sys.exit(0 if status==0 and reason is None else 1)
