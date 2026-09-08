#!/usr/bin/env python3
"""Bounded exact replay. No zeros, floats, external packages, or broad campaign."""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
import hashlib
import itertools
import json
import math
from pathlib import Path, PurePosixPath
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
PARENT = ROOT.parent / '2026-09-06-astra-terminal-endpoint/PROOF.md'
PARENT_SHA256 = '42c7881030424c05b78894c15a3a3542c0ef7e7a61188757fad156ff58e301a1'
PARENT_BLOB = '138dd98c2f8f32b8979926593443986f98f263c5'
HEAD = 'ea66cd5b152e7960ad51ea51b154734eebc9b96a'
FILES = frozenset({'PROOF.md','README.md','SOURCES.md','SOURCE_LOCK.json',
                  'VALIDATION.md','scripts/replay.py','scripts/test_replay.py',
                  'verification.json'})
CONFIG = {'primitive_mu_cap':1089, 'independent_trial_cap':256,
          'quadratic_Y':[3,5,7,9,11,13,15,17,19,23,25,27,31,33],
          'higher_Y_d':[[3,2],[3,3],[3,4],[3,5],[5,2],[5,3],[5,4],[7,2],[7,3]],
          'lobe_L':[1,2,3,5,8,33], 'grid_j':[1,2,3,4],
          'arithmetic':'EXACT_INTEGER_AND_FRACTION_ONLY'}
FLAGS = ('rh_proved','uniform_full_gain_proved','near_linear_actual_form_proved')

def require(test: bool, message: str) -> None:
    if not test:
        raise ValueError(message)

def strict_load(path: Path):
    def pairs(items):
        result={}
        for k,v in items:
            require(k not in result, 'duplicate JSON key: '+k)
            result[k]=v
        return result
    def no_float(s):
        raise ValueError('non-exact JSON number: '+s)
    return json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=pairs,
                      parse_float=no_float, parse_constant=no_float)

def canonical(data) -> str:
    return json.dumps(data, sort_keys=True, indent=2, ensure_ascii=True)+'\n'

def authenticate_parent() -> None:
    require(PARENT.is_file() and not PARENT.is_symlink(),'missing/unsafe parent proof')
    b=PARENT.read_bytes()
    require(len(b)==16669,'parent byte length')
    require(hashlib.sha256(b).hexdigest()==PARENT_SHA256,'parent SHA256')
    require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==PARENT_BLOB,
            'parent Git blob')
    expected={'repository':'GettysburgResearch/riemann','pr':805,'head':HEAD,
              'parent_proof_path':'standalone/2026-09-06-astra-terminal-endpoint/PROOF.md',
              'parent_proof_sha256':PARENT_SHA256,'parent_proof_git_blob':PARENT_BLOB,
              'parent_proof_bytes':16669,'parent_code_executed':False}
    require(canonical(strict_load(ROOT/'SOURCE_LOCK.json'))==canonical(expected),'source lock drift')

def manifest() -> None:
    actual=set()
    for p in ROOT.rglob('*'):
        require(not p.is_symlink(),'symlink in packet')
        if p.is_file(): actual.add(p.relative_to(ROOT).as_posix())
    require(actual==set(FILES)|{'SHA256SUMS'},'packet inventory mismatch')
    rows={}
    for line in (ROOT/'SHA256SUMS').read_text(encoding='ascii').splitlines():
        digest,sep,rel=line.partition('  ')
        require(bool(sep) and len(digest)==64 and all(c in '0123456789abcdef' for c in digest),
                'invalid manifest digest')
        pp=PurePosixPath(rel)
        require(not pp.is_absolute() and '..' not in pp.parts and pp.as_posix()==rel,
                'unsafe manifest path')
        require(rel in FILES and rel not in rows,'duplicate/unexpected manifest path')
        rows[rel]=digest
    require(set(rows)==set(FILES),'incomplete/empty manifest')
    for rel,digest in rows.items():
        require(hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()==digest,'hash mismatch: '+rel)

def mu_sieve(n: int) -> list[int]:
    require(type(n) is int and n>=1,'invalid sieve cap')
    ans=[1]*(n+1);ans[0]=0
    prime=[True]*(n+1);prime[0]=prime[1]=False
    for p in range(2,n+1):
        if prime[p]:
            for j in range(p,n+1,p): ans[j]*=-1
            for j in range(p*p,n+1,p*p):ans[j]=0
            for j in range(p*p,n+1,p):prime[j]=False
    return ans

def mu_trial(n: int) -> int:
    sign=1;p=2
    while p*p<=n:
        if n%p==0:
            n//=p;sign=-sign
            if n%p==0:return 0
            while n%p==0:n//=p
        p+=1
    return -sign if n>1 else sign

def q(x: F, mu: list[int]) -> F:
    x=F(x)
    require(x.numerator//x.denominator < len(mu),'q primitive cap exceeded')
    return sum((mu[k]*(1-x/k) for k in range(1,int(x)+1,2)),F(0))

def terminal(y: int,mu: list[int]) -> dict[int,F]:
    require(type(y) is int and y>=3 and y%2==1 and y<len(mu),'invalid odd cutoff')
    out={k:F(mu[k]) for k in range(1,y+1,2)}
    moment=sum((v/k for k,v in out.items()),F(0))
    out[y]-=y*moment
    return out

@lru_cache(maxsize=None)
def w(z: F) -> F:
    z=F(z)
    return sum((z/r-1 for r in range(1,int(z)+1,2)),F(0)) if z>=1 else F(0)

def form(y: int, c: dict[int,F]) -> F:
    return sum((va*vb*w(F(y*y,a*b)) for a,va in c.items() for b,vb in c.items()),F(0))

def conv(a: dict[int,F], b: dict[int,F], cap: int) -> dict[int,F]:
    out={}
    for i,ai in a.items():
        if not ai:continue
        for j,bj in b.items():
            if i*j<=cap and bj:out[i*j]=out.get(i*j,F(0))+ai*bj
    return {k:v for k,v in out.items() if v}

def add(a,b,scale=1):
    c=dict(a)
    for k,v in b.items():c[k]=c.get(k,F(0))+scale*v
    return {k:v for k,v in c.items() if v}

def weighted(a:dict[int,F],x:F)->F:
    return sum((v*(1-x/n) for n,v in a.items() if n<=x),F(0))

def get_lobe(l:int,positive:bool):
    y=200*l+1; bases=(110,130) if positive else (150,180)
    c={}
    for r in range(l):
        a=bases[0]*l+2*r+1;b=bases[1]*l+2*r+1
        c[a]=F(a,y);c[b]=-F(b,y)
    return y,c

def replay() -> dict:
    checks=Counter()
    def check(label,condition):
        require(condition,'mathematical check failed: '+label);checks[label]+=1
    mu=mu_sieve(CONFIG['primitive_mu_cap'])
    for n in range(1,257):check('independent_mobius',mu[n]==mu_trial(n))
    for n in range(1,1090,2):
        check('odd_divisor_inverse',sum(mu[d] for d in range(1,n+1,2) if n%d==0)==(n==1))
    moment=F(0)
    for n in range(1,1090,2):
        moment+=F(mu[n],n)
        check('harmonic_bound_fixture',abs(moment)<=2)
    quadratic=[]
    for y in CONFIG['quadratic_Y']:
        c=terminal(y,mu); m=sum((F(mu[k],k) for k in c),F(0));qy=q(F(y),mu)
        b=form(y,c); direct=q(F(y*y),mu)
        check('balance',sum((v/k for k,v in c.items()),F(0))==0)
        check('first_coefficient',c[1]==1)
        check('coefficient_sum',sum(c.values())==qy)
        check('balanced_quadratic',direct==2*qy+b)
        raw={k:F(mu[k]) for k in c}
        row=sum((v*w(F(y,k)) for k,v in raw.items()),F(0))
        check('independent_row_cancellation',row==y-1)
        raw_q=2*(sum(raw.values())-y*y*m)+form(y,raw)
        check('uncorrected_hyperbola',raw_q==direct)
        check('terminal_transfer',form(y,raw)-b==2*y*m*(y-1))
        for n in range(1,y):
            fn=sum((v*(n//k-n//(2*k)) for k,v in c.items()),F(0))
            check('exact_horizon',fn==1)
        quadratic.append({'Y':y,'Q_Y':str(qy),'Q_Y_squared':str(direct),
                          'balanced_form':str(b),'form_over_Y':str(b/y),
                          'terminal_coefficient':str(c[y])})
    check('base_form_value',quadratic[0]['balanced_form']=='-32/35')
    check('nonsquarefree_correction',terminal(9,mu)[9]==F(-102,35))
    higher=[]
    for y,d in CONFIG['higher_Y_d']:
        cap=y**d; lam=terminal(y,mu); U={n:F(1) for n in range(1,cap+1,2)}
        upow={1:F(1)};lpow={1:F(1)};approx={};hierarchy=F(d)*q(F(y),mu)
        for r in range(1,d+1):
            lpow=conv(lpow,lam,cap)
            term=conv(upow,lpow,cap)
            approx=add(approx,term,(-1)**(r-1)*math.comb(d,r))
            if r>=2:
                term_sum=sum((lv*sum((dv*(F(cap,k*n)-1) for n,dv in upow.items()
                                       if n*k<=cap),F(0)) for k,lv in lpow.items()),F(0))
                hierarchy+=(-1)**r*math.comb(d,r)*term_sum
            upow=conv(upow,U,cap)
        for n in range(1,cap,2):check('newton_horizon_coefficients',approx.get(n,F(0))==mu[n])
        moment=sum((F(mu[k],k) for k in lam),F(0));edge=(y*moment)**d
        check('boundary_not_silently_extended',F(mu[cap])-approx.get(cap,F(0))==edge)
        check('smoothed_boundary',weighted(approx,F(cap))==q(F(cap),mu))
        check('tensor_hierarchy',hierarchy==q(F(cap),mu))
        higher.append({'Y':y,'degree':d,'cutoff':cap,'boundary_error':str(edge),
                       'Q_cutoff':str(hierarchy)})
    # Algebraic main-term cancellation; rational log-labels test a universal polynomial identity.
    for y in (3,5,9):
        c=terminal(y,mu)
        for r in (2,3,4):
            for degree in range(r):
                value=F(0)
                for ks in itertools.product(c,repeat=r):
                    weight=math.prod((c[k]/k for k in ks))
                    t=F(7,3)-sum((F(k-1,k+1) for k in ks),F(0))
                    value+=weight*t**degree
                check('formal_polynomial_annihilation',value==0)
    lobes=[]
    for l in CONFIG['lobe_L']:
        pair={}
        for positive in (True,False):
            y,c=get_lobe(l,positive);b=form(y,c)
            expected=F(l*l,3)-F(12721*l**4,y*y) if positive else -F(900*l**4,y*y)
            check('lobe_exact_form',b==expected)
            check('lobe_balance',sum((v/k for k,v in c.items()),F(0))==0)
            check('lobe_coefficient_bound',max(map(abs,c.values()))<1)
            check('lobe_sign',b>F(1837*l*l,120000) if positive else b<0)
            moment=sum((k*abs(v) for k,v in c.items()),F(0))
            bound=F(3,8*y*y)*(20*moment+100)
            check('first_cell_augmentation_cost',bound<8)
            if l>=33:check('augmented_sign_persists',b>8 if positive else b<-8)
            pair['positive' if positive else 'negative']={'Y':y,'value':str(b),
                                 'value_over_Y_squared':str(b/(y*y)),
                                 'augmentation_bound':str(bound)}
        lobes.append({'L':l,**pair})
    for y in range(3,66,2):
        check('discrete_norm_majorant',F(3,8*y*y)*sum(k*k for k in range(1,y+1,2))
              ==F((y+1)*(y+2),16*y))
    check('continuum_HS_square',F(3,8)**2*F(1,9)==F(1,64))
    # Exact Green interpolation at a bounded predetermined set, not a global assertion.
    interpolation=[]
    def interpolate(a,b,x):
        linear=(b-x)/(b-a)*q(F(a),mu)+(x-a)/(b-a)*q(F(b),mu)
        green=sum((F(mu[k],k)*(min(x,F(k))-a)*(b-max(x,F(k)))/(b-a)
                   for k in range(a+2,b,2)),F(0))
        error=q(x,mu)-linear
        check('green_interpolation_identity',error==green)
        check('green_interpolation_majorant',abs(error)<=F((b-a)**2,8*a))
        return error
    grid=[(2*j*j+1)**2 for j in CONFIG['grid_j']]
    for a,b in zip(grid,grid[1:]):
        for f in (F(1,4),F(1,2),F(3,4)):
            x=a+(b-a)*f;error=interpolate(a,b,x)
            interpolation.append({'a':a,'b':b,'x':str(x),'error':str(error)})
    for y in (3,5,7,9,15,31):
        a=y*y;b=(y+2)**2
        check('consecutive_odd_square_majorant',F((b-a)**2,8*a)<4)
        for f in (F(1,4),F(1,2),F(3,4)):interpolate(a,b,a+(b-a)*f)
    for j in range(1,65):
        y=2*j*j+1;a=y*y;b=(2*(j+1)**2+1)**2
        check('coarse_grid_polynomial_bounds',b<=9*a and b-a<=72*j**3
              and F((b-a)**2,8*a)<=81*y)
    data={'schema':'riemann-balanced-hyperbola-v1','scientific_status':'PROPOSED_COMPONENT_PROOFS_REVIEW_REQUIRED',
          'config':CONFIG,'counts':dict(sorted(checks.items())),'total_checks':sum(checks.values()),
          'quadratic_panel':quadratic,'higher_order_panel':higher,'signed_lobes':lobes,
          'interpolation_panel':interpolation,'parent_code_executed':False}
    data.update({k:False for k in FLAGS})
    return data

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--write',type=Path)
    args=parser.parse_args()
    authenticate_parent()
    if args.write:
        data=replay();args.write.write_text(canonical(data),encoding='utf-8')
        print('GENERATED_BOUND_COMPONENT_FIXTURES',data['total_checks']);return
    manifest();stored=strict_load(ROOT/'verification.json')
    for flag in FLAGS:require(stored.get(flag) is False,'invalid theorem-status flag')
    actual=replay()
    require(canonical(stored)==canonical(actual),'primitive reconstruction mismatch')
    print('PASS_BALANCED_HYPERBOLA',actual['total_checks'],'EXACT_CHECKS; RH_AND_GAIN_OPEN')

if __name__=='__main__':
    try: main()
    except (ValueError,OSError,KeyError,TypeError,ZeroDivisionError) as exc:
        print('REJECT:',str(exc),file=sys.stderr);sys.exit(1)
