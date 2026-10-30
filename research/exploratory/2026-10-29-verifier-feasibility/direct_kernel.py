"""Unprotected, resource-bounded native check of one exported theorem closure.

Run exactly one kernel at a time. Not tracker Comparator, sandbox or admission.
"""
import argparse,hashlib,json,os,resource,shutil,signal,subprocess,sys,time
from pathlib import Path
ap=argparse.ArgumentParser(); ap.add_argument('kernel',choices=['nanoda','con-ron']); args=ap.parse_args()
out=Path('/workspace/scratch/direct-kernel-retune')
export=out/'candidate.export'
judge=Path('/workspace/scratch/lean-4.35.0-rc2-linux/bin')
result=out/(args.kernel+'-result.json'); log=out/(args.kernel+'.log')
assert export.is_file() and not result.exists() and not log.exists(), 'missing export or existing evidence'
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''): h.update(b)
 return h.hexdigest()
expinfo=json.loads((out/'export-result.json').read_text())
assert expinfo['exit_code']==0 and expinfo['output_sha256']==sha(export), 'export hash mismatch'
if args.kernel=='nanoda':
 exe=judge/'nanoda_bin'
 config={'use_stdin':False,'export_file_path':str(export),'permitted_axioms':['propext','Classical.choice','Quot.sound'],'unpermitted_axiom_hard_error':True,'num_threads':1,'nat_extension':True,'string_extension':True}
 (out/'nanoda-config.json').write_text(json.dumps(config,indent=2)+'\n')
 cmd=[str(exe),str(out/'nanoda-config.json')]
else:
 exe=judge/'con-ron'; cmd=[str(exe),'--jobs=1',str(export)]
limit=13*1024**2; timeout=7200
start=time.monotonic(); peak=0; reason=None
before=Path('/sys/fs/cgroup/memory.events').read_text()
with log.open('wb') as f:
 p=subprocess.Popen(cmd,cwd=out,stdout=f,stderr=subprocess.STDOUT,start_new_session=True)
 while p.poll() is None:
  try:
   for line in Path(f'/proc/{p.pid}/status').read_text().splitlines():
    if line.startswith('VmRSS:'): peak=max(peak,int(line.split()[1])); break
  except (FileNotFoundError,ProcessLookupError): pass
  if peak>limit: reason='rss_limit'
  elif shutil.disk_usage(out).free<1024**3: reason='disk_reserve'
  elif time.monotonic()-start>timeout: reason='timeout'
  if reason:
   os.killpg(p.pid,signal.SIGTERM)
   try:p.wait(timeout=5)
   except subprocess.TimeoutExpired:os.killpg(p.pid,signal.SIGKILL);p.wait()
   break
  time.sleep(.5)
 status=p.wait()
metrics={'command':cmd,'kernel_sha256':sha(exe),'export_sha256':expinfo['output_sha256'],'max_sampled_rss_kib':limit,'timeout_seconds':timeout,'exit_code':status,'termination_reason':reason,'wall_seconds':round(time.monotonic()-start,3),'sampled_peak_rss_kib':peak,'log_sha256':sha(log),'cgroup_events_before':before,'cgroup_events_after':Path('/sys/fs/cgroup/memory.events').read_text()}
if args.kernel=='nanoda':metrics['config_sha256']=sha(out/'nanoda-config.json')
result.write_text(json.dumps(metrics,indent=2)+'\n')
print(json.dumps(metrics,indent=2),flush=True)
sys.exit(0 if status==0 and reason is None else 1)
