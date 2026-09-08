#!/usr/bin/env python3
"""Reconstruct the finite source certificate and independent exact controls.
This is not a machine proof of the infinite analytic theorems.
"""
import argparse, copy, hashlib, json
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import interval_source as src

HERE=Path(__file__).resolve().parent

def require(ok,msg):
    if not ok:raise ValueError(msg)

def canonical(x):return json.dumps(x,sort_keys=True,separators=(',',':'))

def read_strict(path):
    def pairs(items):
        out={}
        for k,v in items:
            if k in out:raise ValueError('duplicate JSON key')
            out[k]=v
        return out
    def bad(s):raise ValueError('nonfinite JSON constant')
    return json.loads(Path(path).read_text(),object_pairs_hook=pairs,parse_constant=bad)

def equal(a,b):
    require(canonical(a)==canonical(b),'reconstructed record differs')

# Gaussian rationals, with no binary floating-point conversion.
def z(a,b=0):return(F(a),F(b))
def za(a,b):return(a[0]+b[0],a[1]+b[1])
def zn(a):return(-a[0],-a[1])
def zm(a,b):return(a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def zi(a):
    d=a[0]**2+a[1]**2;return(a[0]/d,-a[1]/d)
def zp(a,n):
    if n<0:return zp(zi(a),-n)
    out=z(1)
    for _ in range(n):out=zm(out,a)
    return out

def exact_ldl(a):
    n=len(a); l=[[F(0) for _ in range(n)]for _ in range(n)];d=[]
    for i in range(n):
        q=a[i][i]-sum(l[i][j]**2*d[j] for j in range(i))
        require(q>0,'positive Gamma moment pivot');d.append(q);l[i][i]=1
        for k in range(i+1,n):l[k][i]=(a[k][i]-sum(l[k][j]*l[i][j]*d[j]for j in range(i)))/q
    return d

def controls():
    counts={}
    def check(category,ok):
        require(ok,category);counts[category]=counts.get(category,0)+1
    # Outward arithmetic tested against independent Fraction endpoints.
    for a in [F(-7,3),F(-1,7),F(0),F(1,5),F(11,2)]:
        for b in [F(-5,4),F(0),F(2,7),F(13,3)]:
            for got,real in [(src.Ball(a)+b,a+b),(src.Ball(a)*b,a*b)]:
                check('outward_arithmetic',F(got.lo,src.SCALE)<=real<=F(got.hi,src.SCALE))
            if b:
                got=src.Ball(a)/b;real=a/b
                check('outward_arithmetic',F(got.lo,src.SCALE)<=real<=F(got.hi,src.SCALE))
    check('constant_bounds',F(139008*128)*F(289,400)**128<1)
    check('constant_bounds',(1-F(1,2**23))**96>F(1,2))
    check('constant_bounds',48*F(17,4)**3<2**12)
    check('constant_bounds',src.zeta_uniform_error()<F(1,10**120))
    check('constant_bounds',src.gamma_uniform_error()<F(1,10**120))
    for L in range(1,65):
        U=68*(L+1)**2;N=4096*(L+1)**3;C=8+4*2**L*L
        check('all_cutoff_constant_controls',N>=60*U*(L+1))
        check('all_cutoff_constant_controls',C+1<=2**(L+4)*(L+1))
        check('all_cutoff_constant_controls',5*L+28-60*(L+1)==-55*L-32)
    for N in range(1,13):
        for lam in [F(1,2),F(2),F(3),F(7),F(12)]:
            lhs=1/(lam+2)**N-4/(lam+2)**(N+1)
            check('rational_test_laplace',lhs==(lam-2)/(lam+2)**(N+1))
    # Synthetic atom-side independent check of all confluent matrix formulas.
    atoms=[z(1),z(2,1),z(2,-1)];nodes=[1,2,4,8,16]
    jets={p:[sum((zp(za(A,z(p)),-j-1)[0]*(-1)**j for A in atoms),F(0))for j in range(4)]for p in nodes}
    labs=[(p,r)for p in nodes for r in [0,1]]
    for p,r in labs:
        for q,s in labs:
            direct=sum((zm(zp(za(A,z(p)),-r-1),zp(za(A,z(q)),-s-1))[0]*factorial(r)*factorial(s)for A in atoms),F(0))
            if p==q:formula=(-1)**(r+s+1)*factorial(r)*factorial(s)*jets[p][r+s+1]
            else:
                d=q-p;a=jets[p][0]-jets[q][0]
                if(r,s)==(0,0):formula=a/d
                elif(r,s)==(1,0):formula=-jets[p][1]/d-a/d**2
                elif(r,s)==(0,1):formula=jets[q][1]/d+a/d**2
                else:formula=-(jets[p][1]+jets[q][1])/d**2-2*a/d**3
            check('confluent_source_formula',direct==formula)
    # Exact Fourier endpoint and inversion normalization for square b=3/2.
    b=F(3,2);polys={1:[F(1)]}
    for r in range(1,26):
        old=polys[r];nxt=[F(0)]*(len(old)+1)
        for j,a in enumerate(old):nxt[j]+=(2*r-1-j)*a;nxt[j+1]+=a
        polys[r+1]=nxt
    def fourier_coeff(r):
        return[a*b**j/F(2**(r-1)*factorial(r-1))/b**(2*r-1)for j,a in enumerate(polys[r])]
    for N in range(1,11):
        terms=[(2*N,1),(2*N+1,-4),(2*N+2,4)];poly=[F(0)]*(2*N+2)
        for r,c in terms:
            for j,a in enumerate(fourier_coeff(r)):poly[j]+=c*a
        def integral(rate):return sum(a*factorial(j)/rate**(j+1)for j,a in enumerate(poly))
        check('fourier_endpoint',integral(b-F(1,2))+integral(b+F(1,2))==0)
        check('fourier_inversion',integral(b)==F(1,16)/(b*b)**(2*N+2))
    moments=[F(factorial(2*j),8**j*factorial(j))for j in range(13)]
    for n in range(1,7):
        piv=exact_ldl([[moments[i+j]for j in range(n)]for i in range(n)])
        check('negative_continuum_model',all(p>0 for p in piv))
    return counts

def run():
    cert=src.build_certificate()
    equal(cert,read_strict(HERE/'certificate.json'))
    cnt=controls();cnt['actual_source_positive_pivots']=cert['positive_dimension']
    return {'status':'PASS_SC6_COMPONENT_CHECKS','counts':cnt,'total':sum(cnt.values()),
            'certificate_sha256':hashlib.sha256(canonical(cert).encode()).hexdigest(),
            'full_source_payload_sha256':cert['full_payload_sha256'],
            'finite_source_dimension':10,'rh_proved':False,'all_rank_sign_proved':False,
            'infinite_analytic_proofs_machine_verified':False}

def refusals(good):
    cases={}
    for key,new in [('rh_proved',True),('total',True),('finite_source_dimension',10.0),('all_rank_sign_proved',True)]:
        bad=copy.deepcopy(good);bad[key]=new
        try:equal(good,bad)
        except ValueError:cases[key]='REJECTED'
        else:raise ValueError('failed corruption refusal')
    c=src.build_certificate();bad=copy.deepcopy(c)
    bad['pivot_decimal_enclosures'][-1][0]='-1'
    try:equal(c,bad)
    except ValueError:cases['changed_last_pivot']='REJECTED'
    else:raise ValueError('failed pivot refusal')
    return cases

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--check');ap.add_argument('--refusals',action='store_true')
    args=ap.parse_args();out=run()
    if args.check:equal(out,read_strict(args.check))
    if args.refusals:out={'tests':refusals(out),'scope':'record type/sign corruption; full source recomputed'}
    print(json.dumps(out,indent=2,sort_keys=True))
