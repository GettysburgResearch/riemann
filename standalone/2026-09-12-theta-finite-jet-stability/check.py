#!/usr/bin/env python3
"""Exact polynomial controls for a changed-source finite-jet theorem, not RH."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import argparse
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parent
FILES = {'PROOF.md', 'README.md', 'REVIEW.md', 'SOURCES.json', 'VALIDATION.md',
         'check.py', 'result.json', 'SHA256SUMS'}
PARENT = '4558dce9cb981a2e8c0e3e058b21a5b17f6a1cf5'

def need(condition, message):
    if not condition:
        raise ValueError(message)

def add(p, q, scale=F(1)):
    r = list(p) + [F(0)] * max(0, len(q)-len(p))
    for i, x in enumerate(q):
        r[i] += scale*x
    while len(r)>1 and r[-1]==0:
        r.pop()
    return r

def mul(p, q, cap=None):
    n = len(p)+len(q)-1
    if cap is not None:
        n = min(n, cap+1)
    r = [F(0)]*n
    for i, x in enumerate(p):
        for j, y in enumerate(q[:max(0,n-i)]):
            r[i+j] += x*y
    return r

def val(p, x):
    out=F(0)
    for a in reversed(p):
        out=out*x+a
    return out

def diff(p):
    return [F(k)*p[k] for k in range(1,len(p))] or [F(0)]

def step(p):
    out=[F(0)]*(len(p)+1)
    for k, a in enumerate(p):
        out[k] += (2*k+F(1,2))*a
        out[k+1] -= 2*a
    return out

def exact_bounds(p):
    need(p[-1]>0, 'positive leading coefficient')
    ratio=sum(map(abs,p[:-1]),F(0))/p[-1]
    ceiling=(ratio.numerator+ratio.denominator-1)//ratio.denominator
    L=max(3,1+ceiling)
    C=sum((-a*L**k for k,a in enumerate(p) if a<0),F(0))/18
    U=sum((abs(a)*(4*k)**k for k,a in enumerate(p)),F(0))
    need(L>ratio and L>=3, 'all-Q majorization threshold')
    return L,C,U

def digest_fractions(values):
    """Canonical binary hash avoids decimal-string limits on large integers."""
    h=hashlib.sha256()
    for value in values:
        a=F(value)
        for n in (a.numerator,a.denominator):
            raw=abs(n).to_bytes(max(1,(abs(n).bit_length()+7)//8),'big')
            h.update(b'-' if n<0 else b'+')
            h.update(len(raw).to_bytes(8,'big'))
            h.update(raw)
    return h.hexdigest()

def cmul(z,w):
    return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])

def cadd(z,w):
    return (z[0]+w[0],z[1]+w[1])

def cpow(z,n):
    out=(F(1),F(0))
    while n:
        if n&1: out=cmul(out,z)
        z=cmul(z,z);n//=2
    return out

def cinv(z):
    den=z[0]**2+z[1]**2
    need(den>0,'nonzero complex number')
    return (z[0]/den,-z[1]/den)

def cscale(z,x):
    return (z[0]*x,z[1]*x)

def cval(p,z):
    out=(F(0),F(0))
    for a in reversed(p):
        out=cadd(cmul(out,z),(a,F(0)))
    return out

def log_series(p,n):
    need(p[0]==1,'unit formal logarithm')
    d=diff(p); inv=[F(1)]+[F(0)]*n
    for k in range(1,n+1):
        inv[k]=-sum((p[j]*inv[k-j] for j in range(1,min(k,len(p)-1)+1)),F(0))
    deriv=mul(d,inv,n-1)
    return [F(0)]+[(deriv[k-1] if k-1<len(deriv) else F(0))/k for k in range(1,n+1)]

def independent_derivative_controls(P):
    # Independent composition of exp(x/2-Q(exp(2x)-1))*P0(Q exp(2x)).
    n=12;cases=0
    for Q in (F(3),F(4),F(9)):
        E=[F(2**k,factorial(k)) for k in range(n+1)]
        expo=[F(0)]+[-Q*E[k] for k in range(1,n+1)]
        expo[1]+=F(1,2)
        G=[F(1)]+[F(0)]*n
        for k in range(1,n+1):
            G[k]=sum((j*expo[j]*G[k-j] for j in range(1,k+1)),F(0))/k
        qpoly=[Q*a for a in E]
        source=add([4*a for a in mul(qpoly,qpoly,n)],qpoly,F(-6))
        composed=mul(G,source,n)
        for j in range(n+1):
            need(composed[j]*factorial(j)==val(P[j],Q),'independent derivative composition')
            cases+=1
    return cases

def finite_controls():
    cases=0
    for m in (2,4,6):
        A=[F(0)]*(2*m)+[F(-1,4),F(0),F(1)]
        # Fourier symbol is -v^m(v+1/4).
        symbol=[A[2*k]*(-1)**k for k in range(len(A)//2+1)]
        f=[F(0)]*m+[F(1,4),F(1)]
        need(symbol==[-x for x in f],'Fourier multiplier sign')
        need(val(A,F(1,2))==val(A,F(-1,2))==0,'safe endpoints')
        for k in range(2*m):
            need(all(a==0 for a in A[:k+1]),'finite moment annihilation')
        a=F(1,100);b=F(1,5000)
        B=add(add([F(1)],f,-2*a),mul(f,f),b)
        L=log_series(B,2*m+2)
        need(all(x==0 for x in L[:m]),'logarithm finite jet')
        need(-m*L[m]==m*a/2,'first unseen cumulant is positive')
        need(b>a*a,'strict real-axis quadratic')
        for x in (F(-3),F(-1,4),F(0),F(1,2),F(2)):
            need(val(B,x)==(1-a*val(f,x))**2+(b-a*a)*val(f,x)**2>0,'real-axis factorization')
        cases+=1
    # Exact 2x2 block completion, including a negative Schur remainder.
    H=((F(2),F(1)),(F(1),F(3)))
    inv=((F(3,5),F(-1,5)),(F(-1,5),F(2,5)))
    for bvec in ((F(1),F(2)),(F(3),F(-1))):
        hb=[sum((inv[i][j]*bvec[j] for j in range(2)),F(0)) for i in range(2)]
        for c in (F(0),F(10)):
            rem=c-sum((bvec[i]*hb[i] for i in range(2)),F(0))
            for x,t in (((F(1),F(2)),F(3)),((F(-2),F(1)),F(-1))):
                left=sum((x[i]*H[i][j]*x[j] for i in range(2) for j in range(2)),F(0))
                left+=2*t*sum((x[i]*bvec[i] for i in range(2)),F(0))+c*t*t
                y=[x[i]+t*hb[i] for i in range(2)]
                right=sum((y[i]*H[i][j]*y[j] for i in range(2) for j in range(2)),F(0))+rem*t*t
                need(left==right,'Schur identity')
                cases+=1
    return cases

def reconstruct():
    P=[[F(0),F(-6),F(4)]]
    for _ in range(84):P.append(step(P[-1]))
    nderiv=independent_derivative_controls(P)
    g=add(P[42],P[40],F(-1,4))
    h=add(add(P[84],P[82],F(-1,2)),P[80],F(1,16))
    need(len(g)-1==44 and len(h)-1==86,'operator orders')
    Lg,Cg,Ug=exact_bounds(g);Lh,Ch,Uh=exact_bounds(h)
    R=1<<324;m=20;eta=F(1,4)
    Abar=F(1,R**42);Bbar=Abar*Abar
    loss=2*Abar*Cg+Bbar*Ch
    env=2*Abar*Ug+Bbar*Uh
    need(0<loss<F(1,1<<72),'whole-source positivity budget')
    need(0<env<F(1,1<<13231),'whole-source envelope budget')
    z=(F(R),eta);v=cmul(z,z)
    c=cmul(cpow(v,m),cadd(v,(F(1,4),F(0))))
    need(c[0]>0 and c[1]>0,'complex phase quadrant')
    recip=cinv(c);a=recip[0];b=recip[0]**2+recip[1]**2
    need(0<a<=Abar and 0<b<=Bbar and b>a*a,'actual versus ceiling coefficients')
    # Exact B_R(v)=0 at v=(R+i/4)^2.
    factor=cadd(cadd((F(1),F(0)),cscale(c,-2*a)),cscale(cmul(c,c),b))
    need(factor==(0,0),'exact prescribed nonreal root')
    f=[F(0)]*m+[F(1,4),F(1)]
    need(val(f,F(0))==val(f,F(-1,4))==0,'endpoint normalization polynomial')
    # f has only real critical points. Critical values cannot equal c or conjugate(c).
    critical=F(-m,4*(m+1))
    need(val(diff(f),F(0))==val(diff(f),critical)==0,'critical-point formula')
    nfinite=finite_controls()
    return {
        'schema':1,'parent_commit':PARENT,
        'status':'PROPOSED_CHANGED_SOURCE_THEOREM_NOT_RH',
        'parameters':{'m':m,'eta':'1/4','R_power_of_two':324},
        'retained_moment_degree':39,
        'retained_even_moment_degree':38,
        'inserted_distinct_nonreal_quartets':21,
        'bounds':{'positivity_loss_less_than_two_power':-72,
                  'gaussian_weighted_perturbation_less_than_two_power':-13231},
        'derivative_polynomial_degrees':[44,86],
        'exact_polynomial_digest':digest_fractions(g+h),
        'complete_bound_digest':digest_fractions([Lg,Cg,Ug,Lh,Ch,Uh,loss,env]),
        'complex_parameter_digest':digest_fractions([c[0],c[1],a,b]),
        'controls':{'independent_derivative_coefficients':nderiv,
                    'finite_multiplier_and_Schur_panels':nfinite,
                    'full_source_parameter_certificate':1},
        'native_analytic_proof_complete':False,
        'rh_proved':False,'actual_zeta_zeros_computed':0,
        'analytic_theorems_machine_proved':False,
        'prior_theta_integral_replayed':False}

def strict_load(path):
    def pairs(items):
        out={}
        for k,v in items:
            need(k not in out,'duplicate JSON key');out[k]=v
        return out
    def bad(x):raise ValueError('noninteger JSON numeric literal')
    return json.loads(Path(path).read_text(encoding='utf-8'),object_pairs_hook=pairs,
                      parse_float=bad,parse_constant=bad)

def authenticate():
    need({p.name for p in ROOT.iterdir()}==FILES,'packet inventory')
    need(all((ROOT/n).is_file() and not (ROOT/n).is_symlink() for n in FILES),'regular files required')
    entries={}
    for line in (ROOT/'SHA256SUMS').read_text(encoding='utf-8').splitlines():
        h,n=line.split('  ',1)
        need(n in FILES-{'SHA256SUMS'} and n not in entries,'manifest path')
        need(len(h)==64 and all(c in '0123456789abcdef' for c in h),'manifest hash')
        entries[n]=h
    need(set(entries)==FILES-{'SHA256SUMS'},'manifest completeness')
    for n,h in entries.items():
        need(hashlib.sha256((ROOT/n).read_bytes()).hexdigest()==h,'hash mismatch '+n)
    sources=strict_load(ROOT/'SOURCES.json')
    need(sources['parent_commit']==PARENT,'parent source drift')

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    group=ap.add_mutually_exclusive_group(required=True)
    group.add_argument('--emit',action='store_true')
    group.add_argument('--check',type=Path)
    args=ap.parse_args()
    expected=reconstruct()
    if args.check:
        authenticate();received=strict_load(args.check)
        need(json.dumps(received,sort_keys=True,separators=(',',':'))==
             json.dumps(expected,sort_keys=True,separators=(',',':')),'reconstructed result differs')
    print(json.dumps(expected,sort_keys=True,indent=2))

if __name__=='__main__':
    try:main()
    except (ValueError,OSError,KeyError,TypeError) as exc:
        print('REJECT: '+str(exc),file=sys.stderr);sys.exit(1)
