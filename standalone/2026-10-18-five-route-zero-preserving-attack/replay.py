"""Authenticate the packet, replay five lanes in parallel, and reject mutations.

Independent processes are verification jobs, not independently authored agents.
Children use -I -S to exclude unrelated environment/site startup hooks.
The accepting code uses the Python standard library and no network or solver.
"""
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT=Path(__file__).resolve().parent
LANES=('fields','probes','strip','newton','determinant')
MUTATIONS=(
    ('fields','ramified_as_split','ramified_convolution'),
    ('fields','erase_power_tail','inverse_complete_powers'),
    ('probes','unnormalized_probe','normalized_bias_removal'),
    ('probes','commensurate_pair','joint_nonreal_visibility'),
    ('strip','strip_normalization','probability_normalization'),
    ('strip','rare_variance_omitted','rare_total_variance'),
    ('newton','drop_above_output_products','all_product_mask_factorization'),
    ('newton','root_budget_omitted','adaptive_complete_core_budget'),
    ('newton','missing_square_scale','full_recurrence_exponents'),
    ('determinant','delete_prime_powers','prime_power_determinant'),
    ('determinant','wrong_mass_parameter','all_mass_regularization'),
    ('determinant','lost_unit','unit_preserving_rearrangement'),
)

def require(ok,message):
    if not ok: raise RuntimeError(message)

def authenticate():
    seen=set()
    for line in (ROOT/'SHA256SUMS').read_text().splitlines():
        digest,name=line.split('  ',1)
        require(name not in seen and '/' not in name and name not in ('.','..'),'invalid manifest name')
        seen.add(name);p=ROOT/name
        require(p.is_file() and not p.is_symlink(),'missing or linked file '+name)
        require(hashlib.sha256(p.read_bytes()).hexdigest()==digest,'changed bytes '+name)
    actual={p.name for p in ROOT.iterdir() if p.is_file() and p.name!='SHA256SUMS'}
    require(seen==actual,'manifest inventory mismatch')
    return len(seen)

def execute(lane,optimized,mutant=''):
    cmd=[sys.executable,'-I','-S','-B']+(['-O'] if optimized else [])
    # -I removes the script directory, so runpy explicitly restores ONLY this packet.
    runner="import sys,runpy;sys.path.insert(0,sys.argv[1]);sys.argv=['verify.py']+sys.argv[2:];runpy.run_path(sys.path[0]+'/verify.py',run_name='__main__')"
    cmd+=['-c',runner,str(ROOT),'--lane',lane]
    if mutant:cmd+=['--mutant',mutant]
    p=subprocess.run(cmd,cwd=ROOT,capture_output=True,timeout=120)
    return p.returncode,p.stdout,p.stderr

def lane_pair(lane):
    a=execute(lane,False);b=execute(lane,True)
    require(a[0]==b[0]==0,'accepting lane failed '+lane+': '+(a[2]+b[2]).decode())
    require(a[1]==b[1],'normal/optimized mismatch '+lane)
    require(not a[2] and not b[2],'unexpected diagnostic '+lane)
    data=json.loads(a[1])
    return {k:data[k] for k in ('lane','predicates','gates')} | {'stdout_sha256':hashlib.sha256(a[1]).hexdigest()}

def mutation_run(spec):
    lane,name,gate=spec
    rc,out,err=execute(lane,True,name)
    expected=('REJECT:'+gate+'\n').encode()
    require(rc==2 and err==expected and not out,'wrong mutation result '+name+': '+err.decode())
    return {'lane':lane,'mutation':name,'returncode':rc,'gate':gate}

def main():
    n=authenticate()
    with ThreadPoolExecutor(max_workers=5) as pool:
        lanes=list(pool.map(lane_pair,LANES))
    with ThreadPoolExecutor(max_workers=3) as pool:
        mutants=list(pool.map(mutation_run,MUTATIONS))
    expected=json.loads((ROOT/'CHECKS.json').read_text())
    require(lanes==expected['lanes'],'archived lane mismatch')
    require(mutants==json.loads((ROOT/'MUTATIONS.json').read_text()),'archived mutations mismatch')
    total=sum(v['predicates'] for v in lanes)
    require(total==expected['total_predicates'],'count mismatch')
    print(json.dumps({'status':'PASS','manifested_payloads':n,'finite_predicates_per_mode':total,
                      'lanes':5,'rejected_mutations':len(mutants),'agents_launched':0,
                      'independent_mathematical_review':False,'rh_established':False},sort_keys=True,indent=2))

if __name__=='__main__':
    main()
