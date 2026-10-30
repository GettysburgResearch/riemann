"""Recheck the retune target in a fresh native Lean kernel environment."""
import hashlib, json, os, resource, subprocess, sys, time
from pathlib import Path
root=Path('/workspace/scratch/retune_project')
lean_bin=Path('/workspace/scratch/lean-4.34.1-linux/bin')
env=dict(os.environ)
env['LEAN_PATH']=json.loads((root/'lean-results-v2/environment.json').read_text())['lean_path']
env['PATH']=str(lean_bin)+os.pathsep+env['PATH']
def sha(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as f:
        for c in iter(lambda:f.read(1024*1024),b''): h.update(c)
    return h.hexdigest()
for p in (lean_bin/'lean',lean_bin/'leanchecker',root/'src/Candidate/Main.lean',root/'isolated-olean-v2/Candidate/Main.olean',root/'import-plan-v3.json'):
    print(f'sha256 {p} {sha(p)}',flush=True)
print('LEAN_PATH='+env['LEAN_PATH'],flush=True)
events=Path('/sys/fs/cgroup/memory.events')
print('cgroup events before:\n'+events.read_text(),flush=True)
cmd=['leanchecker','--fresh','--verbose','Candidate.Main']
print('command:',repr(cmd),'timeout_seconds=10800',flush=True)
start=time.monotonic()
try:
    result=subprocess.run(cmd,cwd=root/'src',env=env,timeout=10800)
    status=result.returncode
except subprocess.TimeoutExpired:
    print('timed out after 10800 seconds',flush=True)
    status=124
usage=resource.getrusage(resource.RUSAGE_CHILDREN)
print(f'wall_seconds={time.monotonic()-start:.3f} user_seconds={usage.ru_utime:.3f} system_seconds={usage.ru_stime:.3f} max_rss_kib={usage.ru_maxrss}',flush=True)
print('cgroup events after:\n'+events.read_text(),flush=True)
print(f'exit={status}',flush=True)
sys.exit(status)
