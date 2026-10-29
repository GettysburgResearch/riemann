"""Resume the retune's failed module 55 only after the separate checker has finished.

Requires explicit --execute. Validates both recorded build plans, the v2 source,
object, overlay and package inventories, then writes independent v3 logs. It does
not attempt to certify the earlier objects with a fresh kernel replay.
"""
from pathlib import Path
import argparse, hashlib, json, os, re, subprocess, time

ROOT=Path('/workspace/scratch/retune_project')
BASE=Path('/workspace/scratch/qproject/.lake/build/lib/lean')
PACKAGES=Path('/workspace/scratch/qproject/.lake/packages')
OUT=ROOT/'isolated-olean-v2'
OLD=ROOT/'lean-results-v2'
RESULTS=ROOT/'lean-results-v3'
LEAN=Path('/workspace/scratch/lean-4.34.1-linux/bin/lean')
OLD_PLAN=ROOT/'import-plan.json'
NEW_PLAN=ROOT/'import-plan-v3.json'
OLD_SHA='3f9c743029e9f192ea72274337214e76440c22b6a9f6132ed64328a9c88879f0'
NEW_SHA='1bdceb8ac0e91356f432cb04df1dbce935e8e1b36a156df0cae8b8cd6f3a9f61'
LEAN_SHA='e8baaa71855a616dc351028f3ad2200051b0671f423a1696a100e809302d5550'

def sha(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as f:
        for chunk in iter(lambda:f.read(1024*1024),b''): h.update(chunk)
    return h.hexdigest()
def read(p): return json.loads(Path(p).read_text())
def require(ok,msg):
    if not ok: raise SystemExit(msg)
def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--execute',action='store_true',required=True)
    ap.parse_args()
    require(not RESULTS.exists(),'v3 results directory already exists; preserve it')
    require(sha(OLD_PLAN)==OLD_SHA and sha(NEW_PLAN)==NEW_SHA,'plan SHA mismatch')
    require(sha(LEAN)==LEAN_SHA,'Lean binary SHA mismatch')
    old,new=read(OLD_PLAN),read(NEW_PLAN)
    order=new['affected_build_order']; affected=set(order); source=Path(new['retune_source_root'])
    require(len(order)==61 and len(affected)==61 and old['affected_build_order']==order,'affected order mismatch')
    require(old['module_dependencies']==new['module_dependencies'],'dependency graph changed')
    changed=[m for m in new['source_sha256'] if new['source_sha256'][m]!=old['source_sha256'].get(m)]
    require(changed==[order[54]],'unexpected source changes since v2: '+str(changed))
    for m,h in new['source_sha256'].items():
        require(sha(source/(m.replace('.','/')+'.lean'))==h,'source hash mismatch: '+m)
    records=read(OLD/'modules.json')
    require(len(records)==55 and records[-1]['module']==order[54] and records[-1]['exit_code']!=0,'v2 failure record mismatch')
    for i,record in enumerate(records):
        name=order[i]
        require(record['module']==name,'v2 module order mismatch')
        log=OLD/(f'{i+1:03}-'+name.replace('.','_')+'.log')
        require(sha(log)==record['log_sha256'],'v2 log mismatch: '+name)
        if i<54:
            require(record['exit_code']==0 and sha(OUT/(name.replace('.','/')+'.olean'))==record['olean_sha256'],'v2 object mismatch: '+name)
    for name in order[54:]:
        require(not (OUT/(name.replace('.','/')+'.olean')).exists(),'unexpected pending object: '+name)
    env0=read(OLD/'environment.json')
    require(env0['plan_sha256']==OLD_SHA and env0['lean_sha256']==LEAN_SHA and env0['lean']==str(LEAN),'v2 environment mismatch')
    q=Path('/workspace/scratch/qproject')
    require(sha(q/'lake-manifest.json')==env0['lake_manifest_sha256'] and sha(q/'lean-toolchain')==env0['lean_toolchain_sha256'],'toolchain/manifest mismatch')
    roots=env0['lean_path'].split(os.pathsep)
    require(roots[:2]==[str(OUT),str(BASE)],'Lean path mismatch')
    overlay=read(OLD/'overlay-inventory.json'); baselines=read(OLD/'baseline-olean-inventory.json')
    require(set(baselines)==set(new['source_sha256'])-affected,'baseline inventory coverage mismatch')
    for name,h in baselines.items():
        rel=name.replace('.','/')+'.olean'; p=BASE/rel
        require(sha(p)==h and rel in overlay,'baseline object changed: '+name)
    for rel,item in overlay.items():
        p=OUT/rel
        require(p.is_symlink() and str(p.resolve())==item['baseline_path'] and sha(p)==item['sha256'],'overlay changed: '+rel)
        require(not any(rel==m.replace('.','/')+'.olean' for m in affected),'affected overlay collision: '+rel)
    package_items=read(OLD/'package-olean-inventory.json')
    actual=set()
    for lib in roots[2:]:
        actual.update(str(p) for p in Path(lib).rglob('*.olean*') if p.is_file())
    require(actual==set(package_items),'package object inventory changed')
    for p,h in package_items.items(): require(sha(p)==h,'package object changed: '+p)
    for name,info in env0['packages'].items():
        p=PACKAGES/name
        rev=subprocess.check_output(['git','-C',str(p),'rev-parse','HEAD'],text=True).strip()
        diff=subprocess.check_output(['git','-C',str(p),'diff','--binary'])
        status=subprocess.check_output(['git','-C',str(p),'status','--porcelain'],text=True)
        require(rev==info['revision'] and hashlib.sha256(diff).hexdigest()==info['tracked_diff_sha256'] and status==info['status'],'package state changed: '+name)
    RESULTS.mkdir()
    (RESULTS/'preflight.json').write_text(json.dumps({'old_plan_sha256':OLD_SHA,'new_plan_sha256':NEW_SHA,'lean_sha256':LEAN_SHA,'v2_modules_json_sha256':sha(OLD/'modules.json'),'v2_failure_log_sha256':records[-1]['log_sha256'],'sources_checked':len(new['source_sha256']),'v2_compiled_checked':54,'overlay_checked':len(overlay),'baseline_checked':len(baselines),'package_olean_files_checked':len(package_items),'lean_path':env0['lean_path']},indent=2)+'\n')
    env=dict(os.environ,LEAN_PATH=env0['lean_path']);done=set(order[:54]); current=[]
    for i,name in enumerate(order[54:],55):
        for dep in new['module_dependencies'][name]:
            require(dep not in affected or dep in done,'dependency missing: '+dep)
        rel=name.replace('.','/');dest=OUT/(rel+'.olean');dest.parent.mkdir(parents=True,exist_ok=True)
        cmd=[str(LEAN),'-j1','-o',str(dest),rel+'.lean']; start=time.monotonic()
        proc=subprocess.run(cmd,cwd=source,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        log=RESULTS/(f'{i:03}-'+name.replace('.','_')+'.log');log.write_text(proc.stdout)
        rec={'module':name,'exit_code':proc.returncode,'seconds':round(time.monotonic()-start,3),'log_sha256':sha(log),'command':cmd}
        if dest.is_file():rec['olean_sha256']=sha(dest)
        current.append(rec);(RESULTS/'modules.json').write_text(json.dumps(current,indent=2)+'\n')
        print(f'{i}/61 {name}: exit {proc.returncode}',flush=True)
        require(proc.returncode==0 and dest.is_file(),'compilation failed: '+name)
        done.add(name)
    query='import Candidate.Main\n#check Candidate.bound\n#print axioms Candidate.bound\n'
    proc=subprocess.run([str(LEAN),'--stdin'],cwd=source,env=env,input=query,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
    (RESULTS/'candidate-axioms.log').write_text(proc.stdout)
    match=re.search(r'depends on axioms:\s*\[([^]]*)\]',proc.stdout,re.S)
    require(proc.returncode==0 and match and {a.strip() for a in match.group(1).split(',') if a.strip()}=={'propext','Classical.choice','Quot.sound'} and '4369347 / 5000000' in proc.stdout and 'DirichletCharacter.LFunction' in proc.stdout,'candidate inspection failed')
    (RESULTS/'SUCCESS').write_text('All 61 affected modules compiled across v2 and v3; candidate inspection succeeded.\n')
if __name__=='__main__':main()
