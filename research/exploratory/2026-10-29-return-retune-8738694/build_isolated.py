"""Build a planned retune import closure, only after the active baseline build completes.

No work is done on import. See README; invocation requires explicit --execute.
This script uses one Lean process at a time and never writes to the active library.
"""
from pathlib import Path
import argparse, hashlib, json, os, re, subprocess, sys, time

LAKE_SHA='5c6d8777513f3fa9eee95a8475ea8d2109e7efaff4b315d8c22d4d2714ec9c79'
TOOLCHAIN_SHA='d5edba4e4b8faad9c1baeadb265716d20d03be4d1a2647dc5e35b0c0325bea7b'
LEAN_SHA='e8baaa71855a616dc351028f3ad2200051b0671f423a1696a100e809302d5550'
PLAN_SHA='3f9c743029e9f192ea72274337214e76440c22b6a9f6132ed64328a9c88879f0'
def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--execute', action='store_true', required=True)
    ap.add_argument('--plan', required=True)
    ap.add_argument('--baseline-log', required=True)
    ap.add_argument('--baseline-lib', required=True)
    ap.add_argument('--package-root', required=True)
    ap.add_argument('--lake-manifest', required=True)
    ap.add_argument('--lean-toolchain', required=True)
    ap.add_argument('--lean', required=True)
    ap.add_argument('--output-lib', required=True)
    ap.add_argument('--results-dir', required=True)
    args=ap.parse_args()
    plan_path=Path(args.plan).resolve()
    if digest(plan_path)!=PLAN_SHA: raise SystemExit('Unexpected build plan SHA-256')
    plan=json.loads(plan_path.read_text())
    if digest(args.lean)!=LEAN_SHA: raise SystemExit('Unexpected Lean compiler SHA-256')
    if digest(args.lake_manifest)!=LAKE_SHA or digest(args.lean_toolchain)!=TOOLCHAIN_SHA: raise SystemExit('Unexpected pinned Lake manifest or toolchain')
    if not Path(args.baseline_log).read_text().rstrip().splitlines()[-1].startswith('all modules compiled successfully'):
        raise SystemExit('Active baseline full build has not completed successfully')
    src=Path(plan['retune_source_root']);active_src=Path(plan['active_source_root']);base=Path(args.baseline_lib).resolve();out=Path(args.output_lib).resolve();results=Path(args.results_dir).resolve()
    if out==base or base in out.parents or out in base.parents: raise SystemExit('Output library must be isolated from baseline')
    if out.exists() and any(out.iterdir()): raise SystemExit('Output library must initially be empty')
    if results.exists() and any(results.iterdir()): raise SystemExit('Results directory must initially be empty')
    affected=plan['affected_build_order'];aset=set(affected); changed=set(plan['changed']); sources=plan['source_sha256']; deps=plan['module_dependencies']
    if len(aset)!=plan['affected_count'] or len(sources)!=plan['reachable_count'] or not changed<=aset: raise SystemExit('Plan inventory inconsistent')
    baseline_oleans={}
    for name,sha in sources.items():
        rel=name.replace('.','/')+'.lean'
        if digest(src/rel)!=sha: raise SystemExit('Retune source hash mismatch: '+name)
        if name not in changed and digest(active_src/rel)!=sha: raise SystemExit('Active source hash mismatch: '+name)
        if name not in aset:
            compiled=base/(name.replace('.','/')+'.olean')
            if not compiled.is_file(): raise SystemExit('Missing baseline olean: '+name)
            baseline_oleans[name]=digest(compiled)
    packages=sorted(str(p.resolve()) for p in Path(args.package_root).glob('*/.lake/build/lib/lean') if p.is_dir())
    if not packages: raise SystemExit('No pinned package libraries found')
    manifest=json.loads(Path(args.lake_manifest).read_text()); package_info={}
    for package in manifest['packages']:
        name=package['name'].strip('«»');path=Path(args.package_root)/name
        actual=subprocess.check_output(['git','-C',str(path),'rev-parse','HEAD'],text=True).strip()
        if actual!=package['rev']: raise SystemExit('Package revision mismatch: '+name)
        diff=subprocess.check_output(['git','-C',str(path),'diff','--binary'])
        status=subprocess.check_output(['git','-C',str(path),'status','--porcelain'],text=True)
        package_info[name]={'revision':actual,'tracked_diff_sha256':hashlib.sha256(diff).hexdigest(),'status':status}
    out.mkdir(parents=True,exist_ok=True);results.mkdir(parents=True,exist_ok=True)
    # Lean resolves a namespace from the first library that contains it. Populate
    # the isolated tree with symlinks for unaffected modules so Submissions and
    # Candidate do not shadow missing baseline modules. Never link an affected
    # destination: those are newly compiled in this tree.
    overlay={}
    for name in baseline_oleans:
        rel=Path(name.replace('.','/'))
        original=base/(str(rel)+'.olean')
        for item in sorted(original.parent.glob(original.name+'*')):
            if not item.is_file(): continue
            target=out/item.relative_to(base);target.parent.mkdir(parents=True,exist_ok=True)
            target.symlink_to(item.resolve())
            overlay[str(target.relative_to(out))]={'baseline_path':str(item.resolve()),'sha256':digest(item)}
    (results/'overlay-inventory.json').write_text(json.dumps(overlay,indent=2)+'\n')
    env=dict(os.environ,LEAN_PATH=os.pathsep.join([str(out),str(base),*packages]));done=set();items=[]
    (results/'environment.json').write_text(json.dumps({'lean':str(Path(args.lean).resolve()),'lean_sha256':LEAN_SHA,'plan_sha256':PLAN_SHA,'lake_manifest_sha256':LAKE_SHA,'lean_toolchain_sha256':TOOLCHAIN_SHA,'lean_path':env['LEAN_PATH'],'baseline_log_sha256':digest(args.baseline_log),'source_root':str(src),'packages':package_info},indent=2)+'\n')
    (results/'baseline-olean-inventory.json').write_text(json.dumps(baseline_oleans,indent=2)+'\n')
    package_oleans={}
    for lib in packages:
        base_path=Path(lib)
        for item in sorted(base_path.rglob('*.olean*')):
            if item.is_file(): package_oleans[str(item)]=digest(item)
    (results/'package-olean-inventory.json').write_text(json.dumps(package_oleans,indent=2)+'\n')
    for n,name in enumerate(affected,1):
        for dep in deps[name]:
            if dep in aset and dep not in done: raise SystemExit('Affected dependency not built first: '+dep)
            if dep not in aset and not (base/(dep.replace('.','/')+'.olean')).is_file(): raise SystemExit('Missing external dependency: '+dep)
        rel=name.replace('.','/');dest=out/(rel+'.olean');dest.parent.mkdir(parents=True,exist_ok=True)
        command=[str(Path(args.lean).resolve()),'-j1','-o',str(dest),rel+'.lean']
        start=time.monotonic();proc=subprocess.run(command,cwd=src,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        log=results/(f'{n:03}-'+name.replace('.','_')+'.log');log.write_text(proc.stdout)
        record={'module':name,'exit_code':proc.returncode,'seconds':round(time.monotonic()-start,3),'log_sha256':digest(log)}
        if dest.is_file():record['olean_sha256']=digest(dest)
        items.append(record);(results/'modules.json').write_text(json.dumps(items,indent=2)+'\n')
        print(f'{n}/{len(affected)} {name}: exit {proc.returncode}',flush=True)
        if proc.returncode or not dest.is_file(): raise SystemExit('Compilation failed: '+name)
        done.add(name)
    query='import Candidate.Main\n#check Candidate.bound\n#print axioms Candidate.bound\n'
    proc=subprocess.run([str(Path(args.lean).resolve()),'--stdin'],cwd=src,env=env,input=query,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
    (results/'candidate-axioms.log').write_text(proc.stdout)
    print('candidate #check/#print axioms exit',proc.returncode,flush=True)
    if proc.returncode:raise SystemExit('Candidate theorem inspection failed')
    match=re.search(r'depends on axioms:\s*\[([^]]*)\]',proc.stdout,re.S)
    if not match or {a.strip() for a in match.group(1).split(',') if a.strip()} != {'propext','Classical.choice','Quot.sound'}:
        raise SystemExit('Unexpected transitive axioms; inspect candidate-axioms.log')
    if '4369347 / 5000000' not in proc.stdout or 'DirichletCharacter.LFunction' not in proc.stdout:
        raise SystemExit('Unexpected Candidate.bound type; inspect candidate-axioms.log')
    (results/'SUCCESS').write_text('All affected modules compiled; candidate inspection exited 0.\n')
if __name__=='__main__':main()
