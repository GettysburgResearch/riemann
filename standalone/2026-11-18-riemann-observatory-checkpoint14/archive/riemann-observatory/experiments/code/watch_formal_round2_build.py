"""Watch an already-running scoped build, then print actual theorem types/axioms.
Does not start or duplicate the build. CLI: repo_path build_pid
"""
import pathlib,sys,os,subprocess,time,json,datetime,hashlib
repo=pathlib.Path(sys.argv[1]).resolve();pid=int(sys.argv[2]);archive=pathlib.Path(__file__).resolve().parents[2]
result=archive/'experiments/results/formal_ranktrace_build.json';base=repo.parent
expected='3635e74826a4c1fcece7d1cd2b6fa75e43a00510'
commit=subprocess.check_output(['git','-C',str(repo),'rev-parse','HEAD'],text=True).strip();assert commit==expected
olean=repo/'.lake/build/lib/lean/Zeta23/LinAlg/RankTrace.olean';start=time.monotonic()
def active():
 try:return pathlib.Path(f'/proc/{pid}/stat').read_text().split()[2] not in ['Z','X']
 except FileNotFoundError:return False
last=-100
while not olean.exists():
 if not active():
  out={'status':'build_stopped_before_target_olean','commit':commit,'build_pid':pid,'elapsed_monitor_seconds':time.monotonic()-start,'scope':'No successful target build or axiom query claimed.'};result.write_text(json.dumps(out,indent=2));print(json.dumps(out));sys.exit(1)
 if time.monotonic()-start-last>=30:
  last=time.monotonic()-start;print(json.dumps({'status':'source_build_running','elapsed_monitor_seconds':last}),flush=True)
 time.sleep(2)
env=dict(os.environ);env['ELAN_HOME']=str(base/'elan');env['PATH']=str(base/'elan/bin')+os.pathsep+env.get('PATH','');env['LEAN_NUM_THREADS']='4'
audit=archive/'experiments/code/FormalRound2Axioms.lean';run=subprocess.run([str(base/'elan/bin/lake'),'env','lean',str(audit)],cwd=repo,env=env,capture_output=True,text=True)
out={'status':'scoped_target_olean_and_axiom_query_completed' if run.returncode==0 else 'target_olean_exists_but_axiom_query_failed','date_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'commit':commit,'target':'Zeta23.LinAlg.RankTrace','build_pid':pid,'target_olean_sha256':hashlib.sha256(olean.read_bytes()).hexdigest(),'audit_source_sha256':hashlib.sha256(audit.read_bytes()).hexdigest(),'query_exit_code':run.returncode,'stdout':run.stdout,'stderr':run.stderr,'elapsed_monitor_seconds':time.monotonic()-start,'scope':'Only rank-trace module and printed theorem types/axioms, not whole zeta proportion theorem or external independent kernel replay.'}
result.write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
