"""Resume the exact main source build only if no existing build is active.
Usage: python experiments/code/resume_formal_safely.py [pinned_AF_checkout]
Current workspace defaults to the private source cache; downloaded archives need
clones/toolchain installed as documented in experiments/formal_reproducibility.md.
"""
from pathlib import Path
import datetime,json,os,shutil,subprocess,sys
B=Path(__file__).resolve().parents[2]
repo=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else B/'sources/formal_round2/zeta-23-lean-v1.0'
status_file=B/'experiments/results/formal_multiplicity_build.json'
if not (repo/'lakefile.toml').exists():
 raise SystemExit('Pinned source checkout missing; follow experiments/formal_reproducibility.md first.')
def active(pid):
 try:return Path(f'/proc/{pid}/stat').read_text().split()[2] not in ('Z','X')
 except FileNotFoundError:return False
status=json.loads(status_file.read_text()) if status_file.exists() else {}
pid=int(status.get('build_pid',0))
def expected_build(pid):
 try:
  cmd=(Path(f'/proc/{pid}/cmdline')).read_bytes().replace(b'\0',b' ').decode()
  return active(pid) and Path(f'/proc/{pid}/cwd').resolve()==repo and 'lake' in cmd and ' build ' in cmd
 except (FileNotFoundError,PermissionError,ProcessLookupError):return False
if pid and expected_build(pid):
 print(json.dumps({'action':'existing_build_left_running','build_pid':pid,'status_file':str(status_file)}));sys.exit(0)
if status.get('status')=='source_build_and_type_axiom_query_completed' and status.get('query_exit_code')==0:
 print(json.dumps({'action':'already_completed','status_file':str(status_file)}));sys.exit(0)
for proc in Path('/proc').iterdir():
 if not proc.name.isdigit():continue
 try:
  cmd=(proc/'cmdline').read_bytes().replace(b'\0',b' ').decode()
  if (proc/'cwd').resolve()==repo and 'lake' in cmd and ' build ' in cmd and active(int(proc.name)):
   print(json.dumps({'action':'other_existing_build_left_running','build_pid':int(proc.name)}));sys.exit(0)
 except (FileNotFoundError,PermissionError,ProcessLookupError):pass
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ')
if status_file.exists():
 previous=dict(status);previous['resume_observed_utc']=stamp;previous['observed_previous_pid_active']=False
 (B/f'experiments/results/formal_multiplicity_checkpoint_{stamp}.json').write_text(json.dumps(previous,indent=2)+'\n')
log=repo.parent/'multiplicity-build.log'
if log.exists():shutil.copyfile(log,repo.parent/f'multiplicity-build-before-{stamp}.log')
wait_pid=pid if not active(pid) else 0
print(json.dumps({'action':'resuming_pinned_source_build','repo':str(repo),'prior_pid':pid,'wait_pid':wait_pid}),flush=True)
raise SystemExit(subprocess.call([sys.executable,str(B/'experiments/code/continue_formal_main_round2.py'),str(repo),str(wait_pid)]))
