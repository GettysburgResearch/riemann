#!/usr/bin/env python3
"""Sequential isolated Lean step-gate elaboration; DO NOT RUN during live replay.

Uses qproject's prebuilt *unchanged* source dependencies; never writes to qproject.
A success tests these six gates only, not the retuned return or its closure.
"""
from pathlib import Path
import os,sys,json,hashlib,time,subprocess,signal
root=Path('/workspace/scratch/chain131-candidate')
src=root/'src';out=root/'gate-olean';logs=root/'gate-logs'
base=Path('/workspace/scratch/qproject');lean=Path('/workspace/scratch/lean-4.34.1-linux/bin/lean')
mods=['Candidate.ChainExtension.Low130','Candidate.ChainExtension.Low131',
 'Candidate.ChainExtension.High130','Candidate.ChainExtension.High131',
 'Candidate.ChainExtension.Step_130','Candidate.ChainExtension.Step_131']
assert all((src/(m.replace('.','/')+'.lean')).is_file() for m in mods)
assert lean.is_file() and (base/'.lake/build/lib/lean').is_dir()
libs=sorted(str(p.resolve()) for p in (base/'.lake/packages').glob('*/.lake/build/lib/lean') if p.is_dir())
assert libs
out.mkdir(parents=True,exist_ok=True);logs.mkdir(parents=True,exist_ok=True)
# Old changed modules are never imported by these six gates.  Their unchanged
# Source.HybridGates and Cert.Reflect dependencies come from qproject.
env=dict(os.environ,LEAN_PATH=':'.join([str(out),str(base/'.lake/build/lib/lean'),*libs]))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
manifest={'scope':'six gate modules only; qproject dependency oleans imported, not fresh audited',
 'lean_binary_sha256':sha(lean),'source_sha256':{},'dependency_olean_sha256':{},'runs':[]}
for m in mods:manifest['source_sha256'][m]=sha(src/(m.replace('.','/')+'.lean'))
for m in ['Submissions.arvi_density.Source.HybridGates','Submissions.arvi_density.Source.HybridGatesMarked','Submissions.arvi_density.Cert.Reflect']:
 p=base/'.lake/build/lib/lean'/(m.replace('.','/')+'.olean');assert p.is_file(),p
 manifest['dependency_olean_sha256'][m]=sha(p)
for m in mods:
 rel=m.replace('.','/');dest=out/(rel+'.olean');dest.parent.mkdir(parents=True,exist_ok=True)
 cmd=[str(lean),'-j1','-o',str(dest),rel+'.lean'];start=time.monotonic()
 limit=300 if '.High' in m else 180
 print('START',m,flush=True)
 with (logs/(m.rsplit('.',1)[-1]+'.log')).open('w') as fd:
  p=subprocess.Popen(cmd,cwd=src,env=env,stdout=fd,stderr=subprocess.STDOUT,start_new_session=True)
  peak=0;timed_out=False;memory_limited=False
  while p.poll() is None:
   try:
    for line in Path(f'/proc/{p.pid}/status').read_text().splitlines():
     if line.startswith('VmRSS:'):peak=max(peak,int(line.split()[1]))
   except (FileNotFoundError,ProcessLookupError):pass
   if time.monotonic()-start>limit or peak>8*1024*1024:
    timed_out=time.monotonic()-start>limit
    memory_limited=peak>8*1024*1024
    try:os.killpg(p.pid,signal.SIGTERM)
    except ProcessLookupError:pass
    try:p.wait(timeout=5)
    except subprocess.TimeoutExpired:
     try:os.killpg(p.pid,signal.SIGKILL)
     except ProcessLookupError:pass
     p.wait()
    break
   time.sleep(.5)
 item={'module':m,'command':cmd,'cwd':str(src),'exit':p.returncode,'timeout_seconds':limit,
  'timed_out':timed_out,'memory_limit_kib':8*1024*1024,'memory_limited':memory_limited,
  'peak_rss_sampled_kib':peak,'seconds':round(time.monotonic()-start,3)}
 if p.returncode==0 and not timed_out and not memory_limited and dest.is_file():item['olean_sha256']=sha(dest)
 manifest['runs'].append(item)
 (root/'gate-build-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
 print('DONE',m,'exit',p.returncode,'timeout',timed_out,'memory_limit',memory_limited,'sampled_peak_kib',peak,'seconds',item['seconds'],flush=True)
 if timed_out:sys.exit(124)
 if memory_limited:sys.exit(137)
 if p.returncode:sys.exit(p.returncode)
print('Gate elaboration completed; the full candidate and dependencies remain unverified.')
