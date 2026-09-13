#!/usr/bin/env python3
"""Actual accepting-command regressions; each changed packet is a separate copy.
Symlink inability is reported explicitly, not turned into a passing test.
"""
from __future__ import annotations
import argparse, hashlib, json, shutil, subprocess, sys, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parent


def seal(p):
    (p/'SHA256SUMS').write_text(''.join(hashlib.sha256(f.read_bytes()).hexdigest()+'  '+f.name+'\n'
       for f in sorted(p.iterdir()) if f.is_file() and f.name!='SHA256SUMS'),encoding='utf-8')


def command(p,opt):
    return [sys.executable,'-I','-S','-B']+(['-O'] if opt else [])+[str(p/'certify.py'),'--check',str(p/'result.json')]


def run(p,opt):
    return subprocess.run(command(p,opt),text=True,encoding='utf-8',capture_output=True,timeout=180)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--part',type=int,choices=(1,2),required=True)
    ap.add_argument('--optimized',action='store_true');a=ap.parse_args()
    groups={1:['wrong-scope','wrong-number','duplicate','float-alias','extra-file'],
            2:['theta-source','pair-source','unsealed-proof','symlink']}
    passed=[];skipped=[]
    with tempfile.TemporaryDirectory(prefix='d16-refusal-') as tmp:
        base=Path(tmp);clean=base/'clean';shutil.copytree(ROOT,clean)
        r=run(clean,a.optimized)
        if r.returncode:raise RuntimeError('pristine failed: '+r.stderr)
        for case in groups[a.part]:
            p=base/case;shutil.copytree(ROOT,p);expected='';do_seal=True
            path=p/'result.json'
            if case in ('wrong-scope','wrong-number'):
                d=json.loads(path.read_text())
                if case=='wrong-scope':d['matched_even_orders'].append(18)
                else:d['beta_dyadic_upper']+=1
                path.write_text(json.dumps(d),encoding='utf-8');expected='reconstructed result differs'
            elif case=='duplicate':
                txt=path.read_text();path.write_text('{"rh_proved":false,'+txt[1:],encoding='utf-8');expected='duplicate JSON key'
            elif case=='float-alias':
                txt=path.read_text();old='"spins":280'
                if old not in txt:raise RuntimeError('missing exact float mutation primitive')
                path.write_text(txt.replace(old,'"spins":280.0'),encoding='utf-8');expected='noninteger JSON number forbidden'
            elif case=='extra-file':
                (p/'unexpected.txt').write_text('extra',encoding='utf-8');do_seal=False;expected='complete inventory'
            elif case=='theta-source':
                f=p/'primitive.py';s=f.read_text();old='pref=[4*q*q*x-6*q*y'
                if old not in s:raise RuntimeError('missing theta primitive')
                f.write_text(s.replace(old,'pref=[5*q*q*x-6*q*y'),encoding='utf-8');expected=('whole-box invariance','theta variance range','displacement below')
            elif case=='pair-source':
                f=p/'certify.py';s=f.read_text();old='else F(3,5) for n in range(2*R+1)'
                if old not in s:raise RuntimeError('missing pair primitive')
                f.write_text(s.replace(old,'else F(4,5) for n in range(2*R+1)'),encoding='utf-8');expected=('whole-box invariance','inverse row norm','displacement below')
            elif case=='unsealed-proof':
                with (p/'PROOF.md').open('a',encoding='utf-8') as f:f.write('\nChanged unsealed proof.\n')
                do_seal=False;expected='hash PROOF.md'
            elif case=='symlink':
                f=p/'PROOF.md';target=base/'symlink-target.md';target.write_bytes(f.read_bytes());f.unlink()
                try:f.symlink_to(target)
                except (OSError,NotImplementedError) as ex:
                    skipped.append({'case':case,'reason':str(ex)});continue
                do_seal=False;expected='regular file PROOF.md'
            if do_seal:seal(p)
            r=run(p,a.optimized)
            if r.returncode==0:raise RuntimeError('accepted corruption '+case)
            match=(any(s in r.stderr for s in expected) if isinstance(expected,tuple) else expected in r.stderr)
            if not match:raise RuntimeError('wrong failure for '+case+': '+r.stderr)
            passed.append(case)
    print(json.dumps({'part':a.part,'optimized':a.optimized,'pristine_reconstructions':1,
                      'refusals':passed,'skipped':skipped},sort_keys=True))

if __name__=='__main__':main()
