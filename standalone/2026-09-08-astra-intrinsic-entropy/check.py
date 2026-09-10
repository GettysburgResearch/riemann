"""Reconstruct one fixed-source certificate and bounded algebraic controls.
This is NOT a checker of RH or of any infinite theorem in PROOF.md.
"""
from __future__ import annotations
import argparse, hashlib, json, sys, types
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parent
FILES=('PROOF.md','README.md','REVIEW_AND_SOURCES.md','VALIDATION.md',
       'SOURCE_LOCK.json','interval_core.py','certificate.py','check.py',
       'test_check.py','verification.json')
CORE_SHA='1aa6bfa49f791ffde5224e21c8c92291a2e06b35130034d1de975b4d7a93fa17'
CORE_GIT='92f484bc6bc7b12bf26313bd7d323c637cd834b9'
PARENT='1f97efdcf9dacd24351ecff0819c524f9bf40ec3'

def must(ok,msg):
    if not ok:raise ValueError(msg)

def no_duplicates(pairs):
    out={}
    for k,v in pairs:
        if k in out:raise ValueError('duplicate JSON key')
        out[k]=v
    return out

def load_json(path):
    def bad(x):raise ValueError('noninteger numerical JSON alias: '+x)
    return json.loads(path.read_text(),object_pairs_hook=no_duplicates,
                      parse_float=bad,parse_constant=bad)

def dump(obj):return json.dumps(obj,sort_keys=True,indent=2,ensure_ascii=False)+'\n'

def git_blob(b):return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()

def source_lock():
    z=load_json(ROOT/'SOURCE_LOCK.json')
    must(z['base_commit']==PARENT and z['repository']=='GettysburgResearch/riemann','source base drift')
    must(z['rh_established'] is False and z['intrinsic_zero_established'] is False,'false proof claim')
    must(z['proof_status']=='proposed_components_only','proof status')
    p=z['parent_rate'];c=z['copied_core']
    must(p['commit']==PARENT and type(p['bytes']) is int and p['bytes']==23351,'parent identity')
    must(p['git_blob']=='47c51b2f91a2d52c9f9ab91c642ed207042992ca' and p['sha256']=='b6519788124a6d0317ffe6116910922652d2390fb4f006bf4aefef2eec97caab','parent bytes pin')
    must(c['sha256']==CORE_SHA and c['git_blob']==CORE_GIT and type(c['bytes']) is int and c['bytes']==9799,'core lock drift')
    data=(ROOT/'interval_core.py').read_bytes()
    must(len(data)==9799 and hashlib.sha256(data).hexdigest()==CORE_SHA and git_blob(data)==CORE_GIT,'core not frozen bytes')
    return data

def authenticate():
    expected=set(FILES)|{'SHA256SUMS'}
    names=set()
    for p in ROOT.iterdir():
        must(not p.is_symlink(),'symlink payload')
        must(p.is_file(),'unexpected directory')
        names.add(p.name)
    must(names==expected,'incomplete/extra inventory')
    lines=(ROOT/'SHA256SUMS').read_text().splitlines();seen=set()
    must(len(lines)==len(FILES),'manifest cardinality')
    for ln in lines:
        h,p=ln.split('  ')
        must(p in FILES and p not in seen,'manifest path/duplicate');seen.add(p)
        must(len(h)==64 and all(c in '0123456789abcdef' for c in h),'manifest digest syntax')
        must(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,'manifest mismatch '+p)
    must(seen==set(FILES),'manifest scope')
    return source_lock()

def injected(name,data,path):
    mod=types.ModuleType(name);mod.__file__=str(path);sys.modules[name]=mod
    exec(compile(data,str(path),'exec'),mod.__dict__)
    return mod

def algebra(core):
    C=core.C;I=core.I;cases={};out={}
    # Exact sharp lower bound and upper-bound witnesses for real Blaschke zeros.
    record=[]
    for j in range(1,40):
        x=F(j,40);d=1-x*x
        low=2-x*x-(x+1-x*x)**2
        high=2-x*x-(x-1+x*x)**2
        must(low==(1-x)**3*(1+x),'sharp cubic algebra')
        must(d**3/4<=low<=high<=4*d,'cubic sandwich')
        record.append([str(x),str(d),str(low),str(high)])
    cases['sharp_cubic_blashcke']=len(record);out['sharp_cubic_endpoints']=[record[0],record[-1]]
    # Single-node kernel reproduction checked against b0,b1 projection formula.
    vals=[]
    for r in [F(1,4),F(1,2),F(3,4)]:
      for direction in [C(1),C(-1),C(0,1),C(F(3,5),F(4,5)),C(F(3,5),F(-4,5))]:
        a=r*direction;b0=C(r);b1=-a.conj()/r*(1-r*r)
        cost=C(2)-(b0-b1).abs2()-b0.abs2()
        direct=(1-r*r)*(C(1)-a).abs2()
        must(not cost.im and cost.re==direct,'single kernel mismatch')
        vals.append(str(cost.re))
    cases['single_node_projection']=len(vals);out['single_node_costs']=vals
    # Complete finite Gram, cofactor, and monotonic optimized errors.
    ds=[];prev=F(1);prevq=F(2)
    for n in range(1,13):
        G=[[C(5 if i==j else -2 if abs(i-j)==1 else 0)for j in range(n)]for i in range(n)]
        inv=core.inverse(G);u=1-inv[0][0].re
        must(u==F(3*4**n,4**(n+1)-1),'finite entropy cofactor')
        must(F(3,4)<u<prev,'projection monotonicity');prev=u
        r=[C(3)]+([C(-1)]+[C(0)]*(n-2) if n>=2 else [])
        uq=F(2)-core.quad(r,inv).re
        must(uq>=F(3,16) and uq<=prevq,'ramp floor or monotonicity');prevq=uq
        ratio=1/(1-u)
        must(ratio==F(4**(n+1)-1,4**n-1),'det ratio')
        ds.append({'n':n,'unit_error':str(u),'ramp_error':str(uq),'det_ratio':str(ratio)})
    cases['finite_toeplitz_entropy']=len(ds);out['synthetic_toeplitz']=ds
    # The actual strip geometry, tested on explicitly synthetic conjugate pairs.
    strip=[]
    for beta in [F(5,8),F(3,4),F(7,8)]:
      for gamma in [1,2,4,8]:
        rho=C(beta,F(gamma));a=(rho-1)/rho;r2=a.abs2()
        must(a.re<=r2<1,'strip map')
        b0=r2;b1=-2*a.re*(1-r2);L=b1/b0
        J=-core.logq(r2);tau=2*J+L
        cost=2-(b0-b1)**2-b0*b0
        phi=2-b0*b0*(1+(1+2*J).square())
        reconstructed=phi+b0*b0*(2*(1+2*J)*tau-tau.square())
        must(J.lo>0 and J.hi<I.of(1).lo and tau.lo>0,'strip positive terms')
        must(reconstructed.contains(cost),'strip decomposition algebra enclosure')
        must(phi.hi<I.of(cost).lo,'strip lower inequality')
        strip.append({'beta':str(beta),'gamma':gamma,'b0':str(b0),'b1':str(b1),'cost':str(cost),'J':J.record(),'tau':tau.record()})
    cases['strip_conjugate_pairs']=len(strip);out['synthetic_strip_pairs']=strip
    # Equal boundary Grams do not identify which factor is being synthesized.
    for n in range(1,9):
        def gram(a0,a1):
            return [[a0*a0+a1*a1 if i==j else a0*a1 if abs(i-j)==1 else F(0)for j in range(n)]for i in range(n)]
        must(gram(F(1),F(-2))==gram(F(2),F(-1)),'Gram phase invariance')
    cases['equal_gram_different_normalization']=8
    return {'case_counts':cases,'total_cases':sum(cases.values()),'data':out}

def reconstruct():
    coredata=source_lock()
    core=injected('ie26_authenticated_core',coredata,ROOT/'interval_core.py')
    cert=injected('ie26_certificate',(ROOT/'certificate.py').read_bytes(),ROOT/'certificate.py')
    return {'schema':'IE26/1','status':'proposed_components_only','rh_established':False,
            'intrinsic_zero_established':False,'source':'literal factorial d; original L2 metric',
            'algebra':algebra(core),'actual_certificate':cert.certify(core)}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true')
    args=parser.parse_args()
    if not args.write:authenticate()
    result=reconstruct()
    if args.write:(ROOT/'verification.json').write_text(dump(result))
    else:must(dump(load_json(ROOT/'verification.json'))==dump(result),'primitive replay mismatch')
    print('PASS_IE26_COMPONENT_REPLAY; rh_established=false; cases='+str(result['algebra']['total_cases'])+'; one_actual_certificate; cells=2047')

if __name__=='__main__':
    try:main()
    except (ValueError,TypeError,KeyError,OSError,ArithmeticError) as exc:
        print('REJECT_IE26: '+str(exc),file=sys.stderr);sys.exit(1)
