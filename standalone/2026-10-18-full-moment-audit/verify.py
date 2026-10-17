"""Exact finite diagnostics, not a certificate of the imported analytic theorems."""
import argparse
from collections import defaultdict
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product
import json
from math import gcd

COUNTS = defaultdict(int)
MUTATION = ''

def require(value, group, message):
    COUNTS[group] += 1
    if not value:
        raise ValueError(group + ': ' + message)

@lru_cache(None)
def factors(n):
    if n < 1:
        raise ValueError('Positive integers required.')
    result=[]; p=2
    while p*p<=n:
        e=0
        while n%p==0:
            n//=p; e+=1
        if e: result.append((p,e))
        p+=1
    if n>1: result.append((n,1))
    return tuple(result)

def strip(n, degree):
    core=power=1
    for p,e in factors(n):
        core*=p**(e%degree); power*=p**(e//degree)
    return core,power

def mu(n):
    f=factors(n)
    return 0 if any(e>1 for _,e in f) else (-1)**len(f)

def jacobi(n,d):
    if d==1: return 1
    ans=1
    for p,e in factors(d):
        if p==2 or e!=1: raise ValueError('Odd squarefree denominator required.')
        if n%p==0: return 0
        z=pow(n%p,(p-1)//2,p)
        ans*=1 if z==1 else -1
    return ans

def quadratic_diagnostics():
    rows=[d for d in range(1,32,2) if mu(d)]
    cases=0; product_columns=0
    for C in (2,4,8,16):
        cols=[c for c in range(C,2*C) if c%2 and mu(c)]
        for k in range(1,7 if C<16 else 5):
            coef={1:Q(1)}
            for _ in range(k):
                new=defaultdict(Q)
                for v,b in coef.items():
                    for c in cols: new[v*c]+=b*Q(mu(c),c)
                coef=dict(new)
            if MUTATION=='collapse-product-length':
                coef={v:b for v,b in coef.items() if v<=2*C}
            direct=defaultdict(Q)
            for cs in product(cols,repeat=k):
                v=1; b=Q(1)
                for c in cs: v*=c; b*=Q(mu(c),c)
                direct[v]+=b
            require(coef==dict(direct),'ordered-products','Complete ordered products/caps changed.')
            cases+=1; product_columns+=len(coef)
            for d in rows:
                original=sum(Q(mu(c),c)*jacobi(c,d) for c in cols)**k
                transformed=Q(0)
                for v,b in coef.items():
                    e,r=strip(v,2)
                    mask=1 if MUTATION=='drop-square-mask' else int(gcd(d,r)==1)
                    if MUTATION=='impose-coprimality' and gcd(e,r)>1: mask=0
                    transformed+=b*jacobi(e,d)*mask
                require(original==transformed,'quadratic-square-removal','Wrong mask, shared square, or multiplicity.')
    # Explicit nonunit and shared-prime witnesses, not dependent on cancellations in a sum.
    for d,v in ((3,9),(3,27),(5,125),(7,49)):
        e,r=strip(v,2)
        mask=1 if MUTATION=='drop-square-mask' else int(gcd(d,r)==1)
        require(jacobi(v,d)==jacobi(e,d)*mask,'literal-nonunit','A removed square must keep its zero.')
    return {'complete_rational_dyads':cases,'distinct_product_columns_total':product_columns,
            'rows':'all odd squarefree d<=31','column_weight':'mu(c)/c; bounded by 1/sqrt(c)',
            'scope':'Actual rational quadratic fixtures, not CT theta values.'}

# Exact Z[zeta_6] arithmetic; zeta_6^2=zeta_6-1.
ZERO=(0,0); ONE=(1,0)
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def times(x,y): return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]+x[1]*y[1])
def power(x,k):
    z=ONE
    for _ in range(k): z=times(z,x)
    return z

def norm(x): return x[0]*x[0]+x[0]*x[1]+x[1]*x[1]
ROOTS=[power((0,1),j) for j in range(6)]
LOGS={p:{pow(g,j,p):j%6 for j in range(p-1)} for p,g in ((7,3),(13,2))}
def symbol(u,column):
    ans=ONE
    for p,e in factors(column):
        if p not in LOGS: raise ValueError('Fixture prime not available.')
        if u%p==0: return ZERO
        ans=times(ans,ROOTS[(LOGS[p][u%p]*e)%6])
    return ans

def native_rows():
    for u in list(range(1,257))+[7**6,7**7,13**6,7*13**6]:
        a,b=strip(u,6)
        require(a*b**6==u and all(e<6 for _,e in factors(a)),'sixth-row-factorization','Wrong sixth-free row.')
        for n in (1,7,13,91,7**7,13**6):
            right=symbol(a,n) if gcd(b,n)==1 else ZERO
            require(symbol(u,n)==right,'sixth-row-mask','Original row-copy mask changed.')
    # Four named columns only, not all ideals below91.
    cols=(1,7,13,91)
    for H in (64,128,256):
        originals=[]; regrouped=[]
        for u in range(1,H+1):
            v=ZERO
            for n in cols:
                x=symbol(u,n); v=add(v,(mu(n)*x[0],mu(n)*x[1]))
            originals.append(norm(v))
        for b in range(1,H+1):
            if b**6>H: break
            if MUTATION=='omit-row-sixth-copies' and b>1: continue
            for a in range(1,H//b**6+1):
                if any(e>=6 for _,e in factors(a)): continue
                v=ZERO
                for n in cols:
                    x=symbol(a,n) if gcd(b,n)==1 else ZERO
                    v=add(v,(mu(n)*x[0],mu(n)*x[1]))
                regrouped.append(norm(v))
        for k in range(1,5):
            require(sum(x**k for x in originals)==sum(x**k for x in regrouped),
                    'native-complete-rows','Sixth-power replicas lost from the full moment.')
    return {'integer_row_caps':[64,128,256],'named_columns':[1,7,13,91],
            'orders':[2,4,6,8],'scope':'Complete stated integer rows, fixed two-prime sextic fixtures; not full ideal columns.'}

MONOMIALS=((Q(1),Q(0)),(Q(0),Q(1)),(Q(5,6),Q(1,3)),(Q(1,3),Q(5,6)))
def kappa(r): return max(a+b*r/2 for a,b in MONOMIALS)
def moment(r,s): return max(Q(1),1+r*(1-2*s),kappa(r)+r*(Q(1,2)-s))
def exponents():
    for r in range(1,17):
        for j in range(1,12):
            s=Q(j,12); f=moment(r,s)
            for theta in (Q(0),Q(1,4),Q(1)):
                for v in (Q(0),theta*r/2):
                    for a,b in MONOMIALS:
                        main=a+v*(b+1-2*s)
                        dual_factor=r*(1-2*s)*(1 if MUTATION=='substitute-conductor' else theta)
                        dual=a+dual_factor+v*(b+2*s-1)
                        require(main<=f and dual<=f,'full-strip-conductor','Dyadic AFE exponent exceeds theorem.')
                        if v==theta*r/2:
                            expected=a+theta*r*(b+1-2*s)/2
                            require(dual==expected,'dual-conductor-identity','Negative conductor power changed.')
        anchor={1:Q(1,2),2:Q(7,12),3:Q(25,36)}.get(r,1-Q(1,r))
        if MUTATION=='false-critical-anchor' and r>=4: anchor=Q(1,2)
        require(moment(r,anchor)==1,'diagonal-anchor','Numerator high moments are not diagonal on1/2.')
        if r>=4:
            eta=Q(1,100*r); w=Q(4,r); low=Q(3,4)-Q(r-4,4)*eta
            require(w*low+(1-w)*(1+eta)==1-Q(1,r),'finite-anchors','Wrong real interpolation line.')
            require(w/Q(8)==Q(1,2*r),'finite-anchors','Wrong reciprocal p interpolation.')
        for j in range(6,12):
            s=Q(j,12); d=2*s-1; best=moment(r,s)
            for u in (Q(0),Q(r,4),Q(r,2),Q(3*r,4),Q(r)):
                value=max([Q(1)]+[a+u*(b-d) for a,b in MONOMIALS]+[a+(r-u)*b-u*d for a,b in MONOMIALS])
                require(value>=best,'asymmetric-AFE','An unbalanced positive envelope cannot beat (12).')
    return {'r_checked':list(range(1,17)), 'central_exponents':[str(kappa(r)) for r in range(1,9)],
            'proof_boundary':'The written arguments, not this finite grid, handle every fixed integer order.'}

def theta_geometry():
    for k in range(1,13):
        for n in range(1,17):
            for ell in (Q(0),Q(1,4),Q(1),Q(n),Q(2*n)):
                lhs=(1 if MUTATION=='drop-holder-cost' else n**(k-1))*(n+ell**k)
                require(lhs>=max(Q(n),ell)**k,'Holder-support-price','The additive support factor was omitted.')
        for j in range(1,13):
            M=Q(j,8)
            for i in range(5):
                P=M*i/4; D=M-P; R=2*D+P-1
                require(P/2+D<=M and P/2+k*R<=k*(2*M-1),
                        'powerful-moment-exponents','Wrong powerful-part aggregation.')
        critical=Q(k,2*k-1)
        require(k*(2*critical-1)==critical,'moment-support-threshold','Wrong diagonal support threshold.')
    for i in range(1,12):
        for j in range(1,12):
            alpha=Q(i,12); beta=Q(j,12)
            forms=(Q(5,6)+alpha/6,Q(5,6)-alpha/3+beta/2,Q(4,3)-5*alpha/6-beta/2)
            dual=Q(7,9)*forms[0]+Q(1,9)*forms[1]+Q(1,9)*forms[2]
            require(dual==Q(8,9) and max(forms)>=dual,'optimistic-budget-dual','Wrong all-order model dual.')
    # Exact geometric model of the entire decaying C-tail, not a numerical Phi evaluation.
    for L in (Q(1,16),Q(1,4),Q(1,2)):
        for A in (2,3,4):
            actual=L**A/(1-Q(1,4)**A)
            returned=Q(0) if MUTATION=='drop-subunit-tail' else actual
            require(returned>=L**A>0,'subunit-tail','Subunit length is not an empty reflected sum.')
    for n in range(1,513):
        h=d=rad=1
        for p,e in factors(n):
            if e==1: d*=p
            else: h*=p**e;rad*=p
        require(h*d==n and gcd(h,d)==1 and rad**2<=h,'powerful-factorization','Lost powerful support inequality.')
    return {'fourth_example':{'N_exponent':'2/3','new_exponent':'2/3','second_plus_sup_exponent':'1'},
            'subunit_tail_scope':'Exact geometric majorant model only; no infinite theta computation.'}

def main():
    global MUTATION
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--mutate',default='',choices=['','drop-square-mask','impose-coprimality',
        'collapse-product-length','omit-row-sixth-copies','substitute-conductor',
        'drop-holder-cost','false-critical-anchor','drop-subunit-tail'])
    MUTATION=ap.parse_args().mutate
    result={'status':'PASS: finite exact diagnostics; no analytic certification',
            'quadratic':quadratic_diagnostics(),'native_rows':native_rows(),
            'numerator_exponents':exponents(),'theta_geometry':theta_geometry()}
    result['predicates_by_group']=dict(sorted(COUNTS.items()))
    result['total_finite_predicates']=sum(COUNTS.values())
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__=='__main__':main()
