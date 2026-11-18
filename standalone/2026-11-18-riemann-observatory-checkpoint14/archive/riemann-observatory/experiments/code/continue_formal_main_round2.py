"""Continue the pinned source build AFTER the existing RankTrace process ends.
No duplicate build is started. CLI: repo ranktrace_pid. Status/logs are incremental.
"""
from pathlib import Path
import os,sys,subprocess,json,time,datetime,hashlib
B=Path(__file__).resolve().parents[2];repo=Path(sys.argv[1]).resolve();prior=int(sys.argv[2]);base=repo.parent
result=B/'experiments/results/formal_multiplicity_build.json';log=base/'multiplicity-build.log'
assert subprocess.check_output(['git','-C',str(repo),'rev-parse','HEAD'],text=True).strip()=='3635e74826a4c1fcece7d1cd2b6fa75e43a00510'
def active(pid):
 try:return Path(f'/proc/{pid}/stat').read_text().split()[2] not in ('Z','X')
 except FileNotFoundError:return False
def save(status,**kw):
 out={'status':status,'date_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'commit':'3635e74826a4c1fcece7d1cd2b6fa75e43a00510','target':'Solution.Multiplicity','scope':'Local pinned source build and type/axiom query only; not external independent proof-kernel replay.',**kw};result.write_text(json.dumps(out,indent=2)+'\n');return out
save('waiting_for_existing_ranktrace_build',prior_build_pid=prior)
while active(prior):time.sleep(2)
p=repo/'.lake/build/lib/lean/Zeta23/LinAlg/RankTrace.olean'
if not p.exists():print(json.dumps(save('not_started_prior_target_failed',prior_build_pid=prior)));sys.exit(1)
# Catch another lake build on this exact checkout rather than racing it.
for proc in Path('/proc').iterdir():
 if not proc.name.isdigit() or int(proc.name)==os.getpid():continue
 try:
  cmd=(proc/'cmdline').read_bytes().replace(b'\0',b' ').decode();cwd=(proc/'cwd').resolve()
  if cwd==repo and 'lake' in cmd and ' build ' in cmd and active(int(proc.name)):
   print(json.dumps(save('not_started_other_build_detected',other_pid=int(proc.name))));sys.exit(1)
 except (FileNotFoundError,PermissionError,ProcessLookupError):pass
env=dict(os.environ);env['ELAN_HOME']=str(base/'elan');env['PATH']=str(base/'elan/bin')+os.pathsep+env.get('PATH','');env['LEAN_NUM_THREADS']='4'
start=time.monotonic()
with log.open('w') as stream:
 process=subprocess.Popen([str(base/'elan/bin/lake'),'--no-cache','build','Solution.Multiplicity'],cwd=repo,env=env,stdout=stream,stderr=subprocess.STDOUT)
 print(json.dumps(save('source_build_running',build_pid=process.pid,lean_threads=4)),flush=True)
 ticks=0
 while process.poll() is None:
  time.sleep(20);ticks+=1;progress=save('source_build_running',build_pid=process.pid,elapsed_seconds=time.monotonic()-start,lean_threads=4)
  if ticks%6==0:print(json.dumps(progress),flush=True)
 code=process.returncode
if code:
 print(json.dumps(save('source_build_failed',build_pid=process.pid,build_exit_code=code,elapsed_seconds=time.monotonic()-start,log_tail=log.read_text()[-5000:])));sys.exit(code)
audit=B/'experiments/code/FormalRound2MultiplicityAxioms.lean';query=subprocess.run([str(base/'elan/bin/lake'),'env','lean',str(audit)],cwd=repo,env=env,capture_output=True,text=True)
olean=repo/'.lake/build/lib/lean/Solution/Multiplicity.olean'
out=save('source_build_and_type_axiom_query_completed' if query.returncode==0 else 'source_build_completed_but_query_failed',build_pid=process.pid,build_exit_code=code,query_exit_code=query.returncode,elapsed_seconds=time.monotonic()-start,target_olean_sha256=hashlib.sha256(olean.read_bytes()).hexdigest() if olean.exists() else None,audit_source_sha256=hashlib.sha256(audit.read_bytes()).hexdigest(),stdout=query.stdout,stderr=query.stderr,build_log_sha256=hashlib.sha256(log.read_bytes()).hexdigest())
print(json.dumps({k:v for k,v in out.items() if k not in ('stdout','stderr')},indent=2),flush=True)
