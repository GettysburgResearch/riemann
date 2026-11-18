"""Summarize actual completed source/query evidence, never a running status.
No build is started. The private pinned checkout is optional for clean-tree checks.
"""
from pathlib import Path
import json,re,subprocess,datetime,hashlib
B=Path(__file__).resolve().parents[2]
p=B/'experiments/results/formal_multiplicity_build.json';r=json.loads(p.read_text())
if r.get('status')!='source_build_and_type_axiom_query_completed' or r.get('query_exit_code')!=0:
 print(json.dumps({'action':'not_summarized_as_success','actual_status':r.get('status'),'build_pid':r.get('build_pid'),'evidence':str(p)}));raise SystemExit(0)
axioms={name:[v.strip() for v in values.split(',') if v.strip()] for name,values in re.findall(r"'([^']+)' depends on axioms: \[([^\]]*)\]",r['stdout'])}
for name in re.findall(r"'([^']+)' does not depend on any axioms",r['stdout']):axioms[name]=[]
expected=['two_thirds_simple_on_critical_line','two_thirds_simple_on_critical_line_cumulative','five_sixths_distinct','five_sixths_distinct_cumulative','montgomery_taylor_simple_on_critical_line_mult','montgomery_taylor_simple_on_critical_line_mult_cumulative','montgomery_taylor_distinct_mult','montgomery_taylor_distinct_mult_cumulative','dirichlet_two_thirds_simple_on_critical_line','dirichlet_five_sixths_distinct','dirichlet_montgomery_taylor_simple_on_critical_line_mult','dirichlet_montgomery_taylor_distinct_mult']
standard={'propext','Classical.choice','Quot.sound'}
out={'kind':'actual_completed_pinned_source_build_and_query_summary','date_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'commit':r['commit'],'build_exit_code':r['build_exit_code'],'query_exit_code':r['query_exit_code'],'theorem_axioms':axioms,'all_expected_theorems_queried':all(x in axioms for x in expected),'only_standard_axioms_reported':all(set(v)<=standard for v in axioms.values()),'evidence_file':'experiments/results/formal_multiplicity_build.json','target_olean_sha256':r.get('target_olean_sha256'),'scope':'Actual local Lean source build and type/axiom query. No external independent-kernel replay or separate K839 build inferred.'}
out.update({
 'target': r['target'],
 'elapsed_seconds_attempt_including_query': r['elapsed_seconds'],
 'successful_query_count': len(axioms),
 'all_expected_theorems_have_exact_standard_axioms': set(axioms) == set(expected)
     and all(set(values) == standard for values in axioms.values()),
 'scope': 'Actual local Lean source build and type/axiom query for eight zeta declarations and four fixed primitive Dirichlet-character declarations with modulus greater than one.',
 'additional_unchecked_scopes': ['restricted Challenge environment comparison',
     'external independent-kernel replay', 'separate K839 Lean build'],
 'query_stderr_empty': not r['stderr'].strip(),
})
repo=B/'sources/formal_round2/zeta-23-lean-v1.0'
source_log=repo.parent/'multiplicity-build.log'
if source_log.is_file():
 raw_log=source_log.read_bytes()
 if hashlib.sha256(raw_log).hexdigest()==r['build_log_sha256']:
  completed=re.search(rb'Build completed successfully \((\d+) jobs\)\.',raw_log)
  if completed:
   out['completed_lake_jobs']=int(completed.group(1))
if (repo/'lean-toolchain').is_file():
 out['pinned_lean_toolchain']=(repo/'lean-toolchain').read_text().strip()
if (repo/'.git').exists():
 out['git_head_now']=subprocess.check_output(['git','-C',str(repo),'rev-parse','HEAD'],text=True).strip()
 out['tracked_source_changes_now']=subprocess.check_output(['git','-C',str(repo),'diff','--name-only'],text=True).splitlines()
(B/'experiments/results/formal_multiplicity_summary.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
