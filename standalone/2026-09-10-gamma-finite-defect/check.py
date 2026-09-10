#!/usr/bin/env python3
"""Exact bounded source/algebra controls. NOT an RH or complex-zero certificate."""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from math import comb, factorial
from pathlib import Path
import sys

RADIAL_DIFFERENCE_FACTOR = 4
FILES = {'PROOF.md','README.md','SOURCE_LOCK.json','VALIDATION.md','check.py',
         'test_check.py','results.json','scout.py','scout.json'}

def require(condition, message):
    if not condition:
        raise ValueError(message)

def pairs(items):
    out = {}
    for k,v in items:
        require(k not in out, 'duplicate JSON key')
        out[k]=v
    return out

def decode(text):
    def bad(value):
        raise ValueError('noninteger JSON number')
    return json.loads(text, object_pairs_hook=pairs, parse_float=bad, parse_constant=bad)

def typed_equal(a,b):
    if type(a) is not type(b):
        return False
    if isinstance(a,dict):
        return a.keys()==b.keys() and all(typed_equal(a[k],b[k]) for k in a)
    if isinstance(a,list):
        return len(a)==len(b) and all(typed_equal(x,y) for x,y in zip(a,b))
    return a==b

def enc(q):
    q=Q(q)
    return [q.numerator,q.denominator]

def homogeneous(xs,k):
    h=[Q(1)]+[Q(0)]*k
    for x in xs:
        for j in range(1,k+1):
            h[j]+=x*h[j-1]
    return h

def rise(m,k):
    return factorial(m+k-1)//factorial(m-1)

def rates(N):
    return [Q(n*n) for n in range(1,N+1) for _ in range(2)]

def partials(N):
    out=[]
    for n in range(1,N+1):
        b=Q(2*factorial(N)**2,factorial(N-n)*factorial(N+n))**2
        c=1-2*n*n*sum((Q(1,k*k-n*n) for k in range(1,N+1) if k!=n),Q(0))
        out.append((Q(n*n),b*n**4,b*n*n*(c-1)))
    return out

def partial_derivative(N,k):
    return sum((B*(-a)**k+(A*k*(-a)**(k-1) if k else 0)
                for a,A,B in partials(N)),Q(0))

def negative_exp(x,K=100):
    """Rational enclosure of exp(-x), 0<=x<=4, including the whole series tail."""
    x=Q(x); require(0<=x<=4,'exponential domain')
    term=Q(1); total=term
    for k in range(1,K+1):
        term*=x/k; total+=term
    next_term=term*x/(K+1)
    ratio=x/(K+2)
    require(ratio<1,'exponential tail ratio')
    upper=total+next_term/(1-ratio)
    return 1/upper,1/total

def density_positive(N,x,K=48):
    """Complete positive simplex series with no cancellation at the origin."""
    x=Q(x); B=N*N; m=2*N
    require(N>=1 and x>0 and B*x<=4,'density domain')
    h=homogeneous([B-a for a in rates(N)],K)
    total=sum((h[k]*x**k/rise(m,k) for k in range(K+1)),Q(0))
    v=(B-1)*x; require(v/(K+2)<1,'simplex tail ratio')
    tail=v**(K+1)/factorial(K+1)/(1-v/(K+2))
    e0,e1=negative_exp(B*x)
    c=Q(factorial(N)**4,factorial(m-1))*x**(m-1)
    return c*e0*total,c*e1*(total+tail)

def density_partial(N,x):
    lo=hi=Q(0)
    for a,A,B in partials(N):
        e0,e1=negative_exp(a*x)
        v=A*x+B
        if v>=0: lo+=v*e0;hi+=v*e1
        else:lo+=v*e1;hi+=v*e0
    return lo,hi

# Gaussian rationals, represented as ordered Fraction pairs.
def C(x=0,y=0):return (Q(x),Q(y))
def ca(a,b):return (a[0]+b[0],a[1]+b[1])
def cn(a):return (-a[0],-a[1])
def cm(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def cj(a):return (a[0],-a[1])
def ci(a):
    d=a[0]**2+a[1]**2; require(d!=0,'zero Gaussian divisor')
    return (a[0]/d,-a[1]/d)
def cp(a,k):
    require(k>=0,'negative power'); out=C(1)
    for _ in range(k):out=cm(out,a)
    return out

def pmul(a,b):
    out=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out

def traces_from_coefficients(a,L):
    require(a[0]==1,'polynomial normalization')
    s=[Q(0)]*(L+1)
    for m in range(1,L+1):
        s[m]=-m*(a[m] if m<len(a) else 0)-sum(
            (a[j]*s[m-j] for j in range(1,min(m,len(a)))),Q(0))
    return s

def inertia(matrix):
    """Exact real symmetric congruence, including 2x2 pivots and zero blocks."""
    a=[list(map(Q,row)) for row in matrix]; pos=neg=zero=0
    require(all(len(r)==len(a) for r in a),'nonsquare matrix')
    require(all(a[i][j]==a[j][i] for i in range(len(a)) for j in range(len(a))), 'non-Hermitian real matrix')
    while a:
        n=len(a)
        pivot=next((i for i in range(n) if a[i][i]),None)
        if pivot is not None:
            order=[pivot]+[i for i in range(n) if i!=pivot]
            a=[[a[i][j] for j in order] for i in order];d=a[0][0]
            pos+=int(d>0);neg+=int(d<0)
            a=[[a[i][j]-a[i][0]*a[0][j]/d for j in range(1,n)] for i in range(1,n)]
        else:
            ij=next(((i,j) for i in range(n) for j in range(i+1,n) if a[i][j]),None)
            if ij is None:zero+=n;break
            i,j=ij;order=[i,j]+[k for k in range(n) if k not in ij]
            a=[[a[i][j] for j in order] for i in order];b=a[0][1]
            pos+=1;neg+=1
            a=[[a[i][j]-(a[i][0]*a[1][j]+a[i][1]*a[0][j])/b
                for j in range(2,n)] for i in range(2,n)]
    return [pos,neg,zero]

def shifted_value(poly,z):
    out=C()
    for a in reversed(poly):out=ca(cm(out,z),C(a))
    return out

def variance_S_value(poly,x):
    A=C(x*x+Q(3,4),-x)
    v=cm(A,shifted_value(poly,C(x,-4)))
    return v[0]  # the other summand is its conjugate

def reconstruct():
    derivative_count=laplace_count=density_count=reverse_count=0
    samples=[]
    for N in range(1,13):
        m=2*N;a0=Q(factorial(N)**4,factorial(m-1));hh=homogeneous(rates(N),8)
        for k in range(m+8):
            expected=Q(0) if k<m-1 else a0*(-1)**(k-m+1)*hh[k-m+1]/rise(m,k-m+1)*factorial(k)
            require(partial_derivative(N,k)==expected,'gamma derivative/simplex mismatch')
            derivative_count+=1
        require(hh[1]/m==Q((N+1)*(2*N+1),6),'endpoint mean rate')
        B=N*N;rev=homogeneous([B-a for a in rates(N)],8)
        for k in range(9):
            shifted=sum(((Q(-B)**(k-j))/factorial(k-j)*rev[j]/rise(m,j) for j in range(k+1)),Q(0))
            require(shifted==(-1)**k*hh[k]/rise(m,k),'positive-series tilt mismatch')
            reverse_count+=1
        for s in [Q(0),Q(1,7),Q(1,2),Q(1),Q(3),Q(11),Q(-1,2)]:
            lhs=sum((A/(s+a)**2+B0/(s+a) for a,A,B0 in partials(N)),Q(0))
            rhs=Q(1)
            for lam in rates(N):rhs*=lam/(lam+s)
            require(lhs==rhs,'full gamma Laplace mismatch');laplace_count+=1
        for x in [Q(1,16*B),Q(1,B),Q(4,B)]:
            lo,hi=density_positive(N,x); p0,p1=density_partial(N,x)
            require(0<lo<=hi,'positive density enclosure')
            require(max(lo,p0)<=min(hi,p1),'separate density expressions disagree')
            require((hi-lo)/lo<Q(1,10**25),'density enclosure too broad')
            density_count+=1
            if N in (1,4,8,12) and x==Q(1,B):
                samples.append({'N':N,'x':enc(x),'lower':enc(lo),'upper':enc(hi)})
    signatures=[];moment_count=matrix_count=pair_count=0
    for nr in range(4):
        for q in range(4):
            if nr+q==0:continue
            poly=[Q(1)];radial=[Q(1)];nodes=[];Delta=Q(0);S=Q(0)
            for j in range(nr):
                lam=Q(1,(j+2)**2);mult=j+1;nodes.append((C(lam),mult));S+=mult*lam
                for _ in range(mult):poly=pmul(poly,[1,-lam]);radial=pmul(radial,[1,-lam])
            for j in range(q):
                aa=Q(j+1);bb=Q(1,j+2);rr=aa*aa+bb*bb;lam=ci(cp(C(aa,bb),2));mult=j+1
                nodes.extend([(lam,mult),(cj(lam),mult)])
                A=[Q(1),-2*lam[0],Q(1)/rr**2];B=[Q(1),-2/rr,Q(1)/rr**2]
                require(A[1]-B[1]==RADIAL_DIFFERENCE_FACTOR*bb**2/rr**2,'radial factor defect')
                require(A[0]==B[0] and A[2]==B[2],'quartet constant/high term')
                for _ in range(mult):poly=pmul(poly,A);radial=pmul(radial,B)
                Delta+=mult*bb**2/rr**2;S+=2*mult/rr;pair_count+=1
            L=2*(nr+2*q+2);ss=traces_from_coefficients(poly,L)
            for k in range(1,L+1):
                v=C()
                for lam,mult in nodes:v=ca(v,cm(C(mult),cp(lam,k)))
                require(v[1]==0 and ss[k]==v[0],'moment/logarithm mismatch');moment_count+=1
            require(S-ss[1]==4*Delta,'defect coefficient factor four')
            require(poly[1]-radial[1]==4*Delta,'radial polynomial second derivative')
            rank=nr+2*q
            for d in range(1,rank+3):
                sig=inertia([[ss[i+j+2] for j in range(d)] for i in range(d)])
                require(sig[1]<=q,'negative index upper bound')
                if d>=rank:require(sig==[nr+q,q,d-rank],'finite full interpolation inertia')
                matrix_count+=1
            signatures.append({'real_locations':nr,'nonreal_quartets':q,
                'nonreal_total_multiplicity':sum(range(1,q+1)),
                'last_dimension':rank+2,'last_inertia':sig,'defect':enc(Delta)})
    flow=[]
    for aa in [Q(1,2),Q(1),Q(2),Q(3),Q(4),Q(5)]:
        p=[aa**4,Q(0),-2*aa**2,Q(0),Q(1)]
        v=variance_S_value(p,aa);expect=-64*(aa**4-Q(29,4)*aa**2-3)
        require(v==expect,'variance operator counterexample')
        flow.append({'a':enc(aa),'S_at_double_root':enc(v)})
    require(variance_S_value([256,0,-32,0,1],Q(4))==-8768,'a4 counterexample')
    # A purely imaginary zero gives a NEGATIVE REAL node and remains Hankel PSD.
    negative_node=[]
    for d in range(1,7):
        sig=inertia([[Q(-1)**(i+j+2) for j in range(d)] for i in range(d)])
        require(sig==[1,0,d-1],'negative-real boundary control')
        negative_node.append(sig)
    require(inertia([[0,1],[1,0]])==[1,1,0],'zero diagonal pivot control')
    require(inertia([[0,0],[0,0]])==[0,0,2],'zero matrix control')
    # Symbolic Jensen integral for one full quartet: integral J/r^3=1/rho_abs^2.
    # S_pair - s1_pair = 4 b^2/r^4 was independently checked above.
    return {
        'status':'EXACT_BOUNDED_COMPONENT_CONTROLS_NOT_AN_RH_OR_ZERO_CERTIFICATE',
        'rh_proved':False,'analytic_theorems_machine_verified':False,
        'actual_complex_zeros_certified':False,'full_nonreal_census':False,
        'actual_Hankel_index_computed':False,'actual_defect_value_computed':False,
        'counts':{'gamma_derivative_identities':derivative_count,'gamma_Laplace_values':laplace_count,
                  'positive_tilt_coefficients':reverse_count,'complete_density_enclosures':density_count,
                  'quartet_factor_controls':pair_count,'power_sum_logarithm_identities':moment_count,
                  'synthetic_Hankel_inertias':matrix_count,'variance_operator_panels':len(flow),
                  'negative_real_node_controls':len(negative_node),'extra_inertia_controls':2},
        'density_primitive_contract':{'arithmetic':'Fraction rational intervals','exponential_terms':101,
                'positive_simplex_terms':49,'whole_remainders_paid':True,'separate_partial_fraction_comparison':True},
        'selected_actual_gamma_density_bounds':samples,'synthetic_inertias':signatures,
        'variance_operator':flow,'negative_real_node_inertias':negative_node,
        'zero_split_model':{'location':4,'quadratic_scaled_coefficients':[8768,0,64],
                           'imaginary_scaled_roots_squared':-137,'source':'synthetic polynomial, not xi'},
        'finite_defect_analytic_status':'PROPOSED_WRITTEN_PROOF_REQUIRES_INDEPENDENT_REVIEW',
        'all_N_defect_decay':'OPEN'
    }

def authenticate(root):
    actual={p.name for p in root.iterdir()}
    require(actual==FILES|{'SHA256SUMS'},'packet inventory mismatch')
    require(all(p.is_file() and not p.is_symlink() for p in root.iterdir()),'nonregular/symlink file')
    names=set()
    for line in (root/'SHA256SUMS').read_text().splitlines():
        digest,name=line.split('  ',1)
        require(name in FILES and name not in names,'duplicate/unsafe manifest name')
        require(sha256((root/name).read_bytes()).hexdigest()==digest,'file hash mismatch: '+name)
        names.add(name)
    require(names==FILES,'manifest coverage mismatch')

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    g=ap.add_mutually_exclusive_group(required=True)
    g.add_argument('--emit',type=Path);g.add_argument('--check',type=Path)
    args=ap.parse_args()
    if args.emit:
        result=reconstruct()
        args.emit.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
        print('PRODUCED_BOUNDED_CONTROLS_NOT_ACCEPTANCE')
    else:
        root=Path(__file__).resolve().parent;authenticate(root)
        supplied=decode(args.check.read_text())
        result=reconstruct()
        require(typed_equal(result,supplied),'semantic or type mismatch after reconstruction')
        print('PASS_EXACT_BOUNDED_COMPONENT_CONTROLS_NOT_ANALYTIC_PROOF')

if __name__=='__main__':
    try:main()
    except (ValueError,OSError,KeyError,TypeError,ZeroDivisionError) as exc:
        print('FAIL: '+str(exc),file=sys.stderr);sys.exit(1)
