#!/usr/bin/env python3
"""Direct native infinite physical Gram; scout and directed tensor contraction."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha1, sha256
from itertools import product
import json
import math
import os
from pathlib import Path
import subprocess
import sys
import time

os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
os.environ.setdefault('OMP_NUM_THREADS', '1')
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OLD = ROOT / 'research/riemann-structures/native-six-hour'
PRIMES = (2, 3, 5)
BITS = tuple(product((0, 1), repeat=3))
TRITS = tuple(product(range(3), repeat=3))
BASIS = (
    (0,(0,1,0)),(0,(0,0,1)),(1,(0,0,1)),(0,(0,1,1)),(1,(1,0,1)),
    (0,(0,0,2)),(0,(0,2,0)),(0,(0,2,2)),(1,(0,0,2)),(1,(2,0,0)),
    (1,(2,0,2)),(2,(0,2,0)),(2,(2,0,0)),(2,(2,2,0)),(0,(0,1,2)),
    (1,(1,0,2)),(0,(0,2,1)),(2,(1,2,0)),(1,(2,0,1)),(2,(2,1,0)),
)
INDEX = {(tuple(p[k]+int(k==i) for k in range(3)),i):j
         for j,(i,p) in enumerate(BASIS)}
PINS = (
    ('ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc',
     'claims/lemmas/L-102707-continuous-half-divisor-geodesic-and-polarized-hankel-current.md',
     '6810bcece309b0c54ae6c8fc84b314990004549c'),
    ('ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc',
     'claims/lemmas/L-102880-logarithmic-derivative-outer-detector-has-zero-square-lattice-moment.md',
     'd7330d114ebba1a7a16e22fa9ba6aa6b5eb7cdd6'),
    ('69b5322bc872b46d42d4f74e13dcbeb96c1421da',
     'research/riemann-structures/native-six-hour/ALL_HORIZON_THREE_PRIME_SOURCE_MOMENTS.md',
     '2113ce2bef593e19ca647c12c4fbb3c0728572a2'),
)

def require(ok, why):
    if not ok:
        raise ValueError(why)

def authenticate():
    manifest=[]
    for commit,path,blob in PINS:
        raw=subprocess.check_output(['git','show',commit+':'+path],cwd=ROOT)
        actual=sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
        require(actual==blob,'primitive source blob: '+path)
        manifest.append({'commit':commit,'path':path,'blob':blob})
    return manifest

def decoder(a,b):
    total=tuple(x+y for x,y in zip(a,b))
    row=[0]*21
    if total==(0,0,0): return row
    row[0]=1
    active=[i for i in range(3) if total[i]==1]
    sign=[a[i]-b[i] for i in range(3)]
    if 2 in total:
        for i in active: row[1+INDEX[total,i]]+=sign[i]
    elif active:
        anchor=active[-1]
        row[0]+=sign[anchor]
        for i in active[:-1]: row[1+INDEX[total,i]]+=sign[i]-sign[anchor]
    return row

def coefficients(L):
    # Exact sqrt(1+z) recurrence, then the three literal pair products.
    c=[F(1)]
    for n in range(1,L+2): c.append(c[-1]*(F(1,2)-n+1)/n)
    g=[c[0]]+[c[n]-c[n-1] for n in range(1,L+2)]
    a=[F(int(n==0)-int(n==2)) for n in range(L+1)]
    ad=[g[n]-a[n] for n in range(L+1)]
    dd=[F(2*int(n==0)-int(n==1)-int(n==2))-2*g[n]
        for n in range(L+1)]
    return [a,ad,dd],abs(g[L+1])

def gamma_numpy(logshift):
    import numpy as np
    u=np.abs(logshift)
    shift=np.exp(np.minimum(u,math.log(8)))
    result=np.zeros_like(u)
    sq2=math.sqrt(2)
    pieces=((1.,2.,8.,-4.),(2.,4.,-8*(1+sq2),4*sq2),(4.,8.,8*sq2,-2.))
    for l1,h1,a,b in pieces:
        for l2,h2,c,d in pieces:
            lo=np.maximum(l1,shift*l2); hi=np.minimum(h1,shift*h2)
            mask=(lo<hi)&(u<math.log(8))
            ll=np.where(mask,lo,1); hh=np.where(mask,hi,1)
            term=a*c*np.log(hh/ll)+2*(a*d/np.sqrt(shift)+b*c)*(np.sqrt(hh)-np.sqrt(ll))
            term+=b*d/np.sqrt(shift)*(hh-ll)
            result+=np.where(mask,term,0.)
    return result

def local_numpy(p,L):
    import numpy as np
    coeff,_=coefficients(L)
    v=np.array([[float(c)*p**(-n/2) for n,c in enumerate(row)] for row in coeff])
    out=np.zeros((9,2*L+1))
    for i,j in product(range(3),repeat=2): out[3*i+j]=np.correlate(v[i],v[j],'full')
    return out

def reshuffle_numpy(tensor):
    import numpy as np
    H=np.array([[tensor[3*a[0]+b[0],3*a[1]+b[1],3*a[2]+b[2]]
                 for b in TRITS] for a in TRITS])
    pos={a:i for i,a in enumerate(TRITS)}
    K=np.zeros((64,64))
    D=np.array([decoder(a,b) for a,b in product(BITS,repeat=2)]).T
    pairs=tuple(product(BITS,repeat=2))
    for i,(a,b) in enumerate(pairs):
        for j,(c,d) in enumerate(pairs):
            K[i,j]=H[pos[tuple(x+y for x,y in zip(a,d))],pos[tuple(x+y for x,y in zip(b,c))]]
    return D@K@D.T

def scout(L):
    import numpy as np
    from scipy.optimize import root
    require(L in (16,32),'registered scout cutoff')
    local=[local_numpy(p,L) for p in PRIMES]
    ds=np.arange(-L,L+1)
    s12=ds[:,None]*math.log(2)+ds[None,:]*math.log(3)
    tensor=np.zeros((9,9,9))
    for k,d in enumerate(ds):
        slab=gamma_numpy(s12+d*math.log(5))
        pair=local[0]@slab@local[1].T
        tensor+=pair[:,:,None]*local[2][:,k][None,None,:]
    gram=reshuffle_numpy(tensor)
    baseline=np.zeros(21);baseline[0]=1
    for j,(i,p) in enumerate(BASIS): baseline[j+1]=int(i==2 or j==9)
    plane=np.zeros((21,4));plane[:,0]=baseline
    plane[1,1]=1;plane[10,2]=-2;plane[7,3]=2
    small=plane.T@gram@plane
    def moments(z):
        lam,mu=z
        require(mu>0 and lam<0 and lam+mu>0,'nonempty lower-clipped monotone profile')
        u0=-lam/mu;u1=min(1.,(1-lam)/mu)
        A=lam*(u1-u0)+mu*(u1*u1-u0*u0)/2+1-u1
        B=lam*(u1*u1-u0*u0)/2+mu*(u1**3-u0**3)/3+(1-u1*u1)/2
        C=lam*lam*(u1-u0)+lam*mu*(u1*u1-u0*u0)+mu*mu*(u1**3-u0**3)/3+1-u1
        return np.array([1.,A,B,C/2])
    def fun(z):
        try:
            x=moments(z); lin=(small@x)[1:]
            return [lin[2]*z[0]+lin[0],lin[2]*z[1]+lin[1]]
        except ValueError: return [1e5,1e5]
    sol=root(fun,[-.1265,1.16009])
    x=moments(sol.x); M=plane@x; gradient=(gram@M)[1:]
    cone=[]
    for sig,tau in product((0,1),repeat=2):
        c=lambda j:gradient[j-1]
        pp=(c(2)-2*sig*c(13)+tau*c(6),c(4)-2*sig*c(20)+tau*c(15),c(17)-c(18)-2*sig*c(14)+tau*c(8))
        qq=(c(3)-2*sig*c(12)+tau*c(9),c(5)-2*sig*c(18)+tau*c(16),c(19)-c(20)-2*sig*c(14)+tau*c(11))
        for name,(C,B,A) in [('p',pp),('q',qq)]:
            cand=[(C,0.),(A+B+C,1.)]
            if A>0 and -2*A<B<0:cand.append((C-B*B/(4*A),-B/(2*A)))
            cone.append({'name':name+str(sig)+str(tau),'coefficients':[C,B,A], 'minimum':min(cand)})
    eig=np.linalg.eigvalsh((gram[1:,1:]+gram[1:,1:].T)/2)
    return {'status':'floating reconnaissance only; NOT a certificate','L':L,
            'gram21':gram.tolist(),'symmetry_error':float(np.max(abs(gram-gram.T))),
            'eigenvalues20':eig.tolist(),'plane_gram4':small.tolist(),
            'root_success':bool(sol.success),'lambda_mu':sol.x.tolist(),
            'clipping_regime':'both' if sol.x.sum()>1 else 'lower_only',
            'root_residual':list(map(float,fun(sol.x))), 'energy':float(x@small@x),
            'gradient20':gradient.tolist(),'cone':cone}

def arb_import():
    # Optional task-local binary dependency; no system-package modification.
    cache=Path.home()/'.cache/riemann-five-hour-deps'
    if cache.is_dir(): sys.path.insert(0,str(cache))
    from flint import arb, arb_mat, arb_poly, ctx
    return arb,arb_mat,arb_poly,ctx

def endpoints(x):
    require(x.is_finite(),'finite directed ball')
    return [str(x.lower().fmpq()),str(x.upper().fmpq())]

def gamma_arb(n,d,arb):
    if n<d:n,d=d,n
    if n>=8*d:return arb(0)
    shift=arb(n)/d; sr=shift.sqrt(); sq2=arb(2).sqrt()
    pieces=((1,2,arb(8),arb(-4)),(2,4,-8*(1+sq2),4*sq2),(4,8,8*sq2,arb(-2)))
    result=arb(0)
    for l1,h1,a,b in pieces:
        for l2,h2,c,e in pieces:
            # Exact rational branch comparisons; no floating support decisions.
            ln=max(l1*d,l2*n); hn=min(h1*d,h2*n)
            if ln>=hn:continue
            lo=arb(ln)/d;hi=arb(hn)/d
            result+=a*c*(arb(hn)/ln).log()
            result+=2*(a*e/sr+b*c)*(hi.sqrt()-lo.sqrt())
            result+=b*e/sr*(hi-lo)
    return result

def local_arb(p,L,arb,arb_mat,arb_poly):
    coeff,tailcoef=coefficients(L); q=1/arb(p).sqrt()
    values=[[arb(c.numerator)/c.denominator*q**n for n,c in enumerate(row)] for row in coeff]
    corr=[]
    for i,j in product(range(3),repeat=2):
        pol=arb_poly(values[i])*arb_poly(list(reversed(values[j])))
        corr.append([pol[k] for k in range(2*L+1)])
    masses=[sum((abs(x) for x in row),arb(0)) for row in values]
    tail=arb(tailcoef.numerator)/tailcoef.denominator*q**(L+1)/(1-q)
    tails=[arb(0),tail,2*tail]
    fullmasses=[m+t for m,t in zip(masses,tails)]
    return arb_mat(corr),masses,tails,fullmasses

def certify_gram(L,precision):
    require(L in (64,96,128) and precision in (192,256),'registered directed acquisition')
    arb,arb_mat,arb_poly,ctx=arb_import();ctx.prec=precision
    local=[local_arb(p,L,arb,arb_mat,arb_poly) for p in PRIMES]
    N=2*L+1;ds=list(range(-L,L+1))
    powers=[[(p**max(e,0),p**max(-e,0)) for e in ds] for p in PRIMES]
    pairpowers=[[(a*c,b*d) for c,d in powers[1]] for a,b in powers[0]]
    tensor=[arb(0) for _ in range(729)]
    corr0=local[0][0];corr1T=local[1][0].transpose();corr2=local[2][0]
    cache={};inside=0
    for k,(n3,d3) in enumerate(powers[2]):
        slab=arb_mat(N,N)
        for a in range(N):
            for b in range(N):
                n,d=pairpowers[a][b];n*=n3;d*=d3
                if n>=8*d or d>=8*n:continue
                inside+=1
                if n<d:n,d=d,n
                key=(n,d)
                if key not in cache:cache[key]=gamma_arb(n,d,arb)
                slab[a,b]=cache[key]
        pair=corr0*slab*corr1T
        for i,j,h in product(range(9),repeat=3):
            tensor[81*i+9*j+h]+=pair[i,j]*corr2[h,k]
        if k%16==0: print(json.dumps({'directed_slab':k,'total':N,'kernel_values':len(cache)}),flush=True)
    nu0=128*(3+arb(2).sqrt())*arb(2).log()-288
    require(gamma_arb(1,1,arb).overlaps(nu0),'original kernel mass control')
    masses=[];tails=[]
    for a in TRITS:
        M=arb(1);eta=arb(0)
        for p in range(3):M*=local[p][3][a[p]]
        for p in range(3):
            term=local[p][2][a[p]]
            for q in range(3):
                if q!=p:term*=local[q][3][a[q]]
            eta+=term
        masses.append(M);tails.append(eta)
    H=arb_mat(27,27);max_tail=arb(0)
    for i,a in enumerate(TRITS):
        for j,b in enumerate(TRITS):
            idx=81*(3*a[0]+b[0])+9*(3*a[1]+b[1])+3*a[2]+b[2]
            # Both full and prefix masses are bounded by masses[].
            error=nu0*(tails[i]*masses[j]+tails[j]*masses[i])
            H[i,j]=tensor[idx]+arb(0,error.upper())
            if error.upper()>max_tail:max_tail=error.upper()
    pos={a:i for i,a in enumerate(TRITS)};pairs=tuple(product(BITS,repeat=2))
    K=arb_mat(64,64)
    for i,(a,b) in enumerate(pairs):
        for j,(c,d) in enumerate(pairs):
            K[i,j]=H[pos[tuple(x+y for x,y in zip(a,d))],pos[tuple(x+y for x,y in zip(b,c))]]
    D=arb_mat([decoder(a,b) for a,b in pairs]).transpose()
    gram=D*K*D.transpose()
    # Symmetry is an independent mathematical identity; check overlap.
    for i in range(21):
        for j in range(i):
            require(gram[i,j].overlaps(gram[j,i]),'physical Gram symmetry')
    G=arb_mat([[gram[i+1,j+1] for j in range(20)] for i in range(20)])
    # Interval LDL verifies positivity for the source matrix, not scout eigenvalues.
    ell=[[arb(int(i==j)) for j in range(20)] for i in range(20)];piv=[]
    for i in range(20):
        v=G[i,i]-sum((ell[i][k]**2*piv[k] for k in range(i)),arb(0))
        require(v>0,'directed positive LDL pivot '+str(i));piv.append(v)
        for j in range(i+1,20):
            ell[j][i]=(G[j,i]-sum((ell[j][k]*ell[i][k]*piv[k] for k in range(i)),arb(0)))/v
    inverse=G.inv()
    upper=max(sum(abs(G[i,j]).upper() for j in range(20)) for i in range(20))
    invupper=max(sum(abs(inverse[i,j]).upper() for j in range(20)) for i in range(20))
    lower=1/invupper
    require(lower>0,'positive source Euclidean lower frame bound')
    return {'status':'directed infinite physical Gram acquisition; independent replay pending',
            'L':L,'precision_bits':precision,'local_product_truncation':True,
            'source_norm':'Euclidean norm of twenty declared occupation coordinates',
            'gram21_intervals':[[endpoints(gram[i,j]) for j in range(21)] for i in range(21)],
            'ldl_pivot_intervals':list(map(endpoints,piv)),
            'frame_lower_interval':endpoints(lower),'frame_upper_interval':endpoints(upper),
            'max_holomorphic_covariance_tail':endpoints(max_tail),
            'kernel_mass':endpoints(nu0),'frequency_triples_in_support':inside,
            'distinct_kernel_evaluations':len(cache)}

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--scout',type=int,choices=(16,32))
    parser.add_argument('--certify',type=int,choices=(64,96,128))
    parser.add_argument('--check',type=int,choices=(64,96,128))
    parser.add_argument('--precision',type=int,choices=(192,256),default=192)
    args=parser.parse_args()
    require(sum(x is not None for x in (args.scout,args.certify,args.check))==1,
            'choose exactly one registered action')
    cutoff=args.certify or args.check
    start=time.monotonic(); manifest=authenticate()
    failure=None
    try:
        data=scout(args.scout) if args.scout else certify_gram(cutoff,args.precision)
    except ValueError as exc:
        failure=str(exc)
        data={'status':'REFUSED; no certificate accepted','L':args.scout or cutoff,
              'precision_bits':args.precision,'reason':failure}
    data['primitive_sources']=manifest
    data['producer_sha256']=sha256(Path(__file__).read_text(encoding='utf8').encode()).hexdigest()
    path=HERE/(f'physical_infinity_L{args.scout}.scout.json' if args.scout else
               f'physical_infinity_L{cutoff}_p{args.precision}.acquisition.json')
    if args.check:
        existing=json.loads(path.read_text(encoding='utf8'))
        require(json.dumps(existing,sort_keys=True,allow_nan=False)==
                json.dumps(data,sort_keys=True,allow_nan=False),'complete primitive replay differs')
    else:path.write_text(json.dumps(data,indent=2,allow_nan=False)+'\n',encoding='utf8')
    keys=('status','L','reason') if failure else (
        ('status','L','lambda_mu','energy','eigenvalues20','cone') if args.scout else
        ('status','L','frame_lower_interval','frame_upper_interval','max_holomorphic_covariance_tail'))
    print(json.dumps({k:data[k] for k in keys},indent=2))
    print('seconds',time.monotonic()-start,flush=True)
    if failure and not args.check:raise SystemExit(2)

if __name__=='__main__': main()
