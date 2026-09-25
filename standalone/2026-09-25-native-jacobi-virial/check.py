#!/usr/bin/env python3
"""Exact replay for native Jacobi / logarithmic-virial comparisons.

Standard library only. All acceptance decisions use integers and Fractions.
The analytic Fourier/orthogonality theorems are written/imported in PROOF.md;
finite moment checks do not prove them. No RH bound is certified here.
"""
from __future__ import annotations
import argparse
from collections import defaultdict
from fractions import Fraction as F
from hashlib import sha256
import json
from math import comb, gcd, isqrt, lcm
from pathlib import Path

COUNTS: dict[str, int] = defaultdict(int)

def require(ok: bool, label: str) -> None:
    COUNTS[label] += 1
    if not ok:
        raise ValueError(label)

def eq(a, b, label: str) -> None:
    require(a == b, label)

def digest_ints(values) -> str:
    # Hex encoding avoids Python's decimal-digit ceiling at large exact panels.
    h = sha256()
    for n in values:
        h.update((hex(n)+'\n').encode('ascii'))
    return h.hexdigest()

def trim(p):
    p = list(p)
    while len(p) > 1 and not p[-1]:
        p.pop()
    return p

def add(p, q):
    r = [F(0)]*max(len(p), len(q))
    for i, x in enumerate(p): r[i] += x
    for i, x in enumerate(q): r[i] += x
    return trim(r)

def scale(p, x):
    return trim([x*y for y in p])

def mul(p, q):
    r = [F(0)]*(len(p)+len(q)-1)
    for i, x in enumerate(p):
        for j, y in enumerate(q): r[i+j] += x*y
    return trim(r)

def polynomials(degree):
    out = [[F(1)]]
    for n in range(1, degree+1):
        q = mul(out[-1], [F(2*n*n)-F(1,4), F(-1)])
        if n > 1: q = add(q, scale(out[-2], -n*(n-1)))
        out.append(scale(q, F(1,n*(n+1))))
    return out

def hypergeometric_polynomial(m):
    # 3F2(-m,1/2+it,1/2-it;1,2;1), represented in z=t^2.
    total, term = [F(1)], [F(1)]
    for k in range(1, m+1):
        term = scale(mul(term, [F(2*k-1,2)**2, F(1)]),
                     F(-m+k-1, k*k*(k+1)))
        total = add(total, term)
    return total

def moment_checks(degree=20):
    ps = polynomials(degree+1)
    euler = [1]
    for k in range(1, 2*degree+3):
        euler.append(-sum(comb(2*k,2*j)*euler[j] for j in range(k)))
    rho = [F((2*k+1)*abs(euler[k]), 1 << (2*k)) for k in range(2*degree+2)]
    w = [rho[k+1]+rho[k]/4 for k in range(2*degree+1)]
    for i in range(degree+1):
        eq(ps[i], hypergeometric_polynomial(i), 'hypergeometric_recurrence_match')
        for j in range(degree+1):
            p = mul(ps[i], ps[j])
            eq(sum(v*w[k] for k,v in enumerate(p)), int(i==j), 'exact_weight_orthogonality')
            eq(sum(v*rho[k] for k,v in enumerate(p)), F(1,max(i,j)+1), 'exact_resolvent_green_moments')
    for n in range(1, degree+1):
        left = add(scale(ps[n-1],2*n*n),scale(ps[n],-n*(n+1)))
        if n > 1: left = add(left,scale(ps[n-2],-n*(n-1)))
        eq(left,mul(ps[n-1],[F(1,4),F(1)]),'exact_jacobi_recurrence')
    require(rho[0] != F(1,2), 'reject_wrong_spectral_normalization')
    return {'max_polynomial_degree':degree,
            'pairs':(degree+1)**2,
            'first_polynomials_in_t_squared':[[str(v) for v in p] for p in ps[:3]],
            'rho_moments_first_five':[str(v) for v in rho[:5]]}

def native_kernel(m,n,N):
    return F(1,max(m,n))-F(1,N+1)

def prefix(c):
    out=[0]
    for x in c[1:]: out.append(out[-1]+x)
    return out

def energy(c):
    S=prefix(c)
    return sum((F(S[k]*S[k],k*(k+1)) for k in range(1,len(c))),F(0))

def matrix_checks():
    for N in range(1,49):
        for m in range(1,N+1):
            for n in range(1,N+1):
                value=2*m*m*native_kernel(m,n,N)
                if m>1: value-=m*(m-1)*native_kernel(m-1,n,N)
                if m<N: value-=m*(m+1)*native_kernel(m+1,n,N)
                eq(value,int(m==n),'finite_green_inverse_entries')
                eq(F(1,max(m,n))-native_kernel(m,n,N),F(1,N+1),'rank_one_boundary_entries')
        c=[0]+[((7*n*n+3*n+N)%11)-5 for n in range(1,N+1)]
        Kc=[0]+[sum(native_kernel(n,m,N)*c[m] for m in range(1,N+1)) for n in range(1,N+1)]
        eq(sum(c[n]*Kc[n] for n in range(1,N+1)),energy(c),'native_energy_quadratic')
        # Discrete Poisson solution d_n=n(K_N c)_n, Dirichlet at 0 and N+1.
        d=[F(0)]+[n*Kc[n] for n in range(1,N+1)]+[F(0)]
        for n in range(1,N+1):
            eq(2*d[n]-d[n-1]-d[n+1],F(c[n],n),'discrete_poisson_equation')
        eq(sum((d[n]-d[n-1])**2 for n in range(1,N+2)),energy(c),'dirichlet_energy_identity')
        reciprocal=[F(0)]
        for n in range(1,N+1): reciprocal.append(reciprocal[-1]+F(c[n],n))
        mean=sum(reciprocal)/F(N+1)
        eq(mean,reciprocal[-1]-F(sum(c),N+1),'reciprocal_mean_boundary')
        eq(sum((v-mean)**2 for v in reciprocal),energy(c),'centered_reciprocal_variance')
        # Causal dilation, including its exact nonzero rounding correction.
        for a in range(2,11):
            m=N//a
            v=[0]+[c[n//a] if n%a==0 else 0 for n in range(1,N+1)]
            sm=sum(c[1:m+1])
            correction=sm*sm*(F(1,N+1)-F(1,a*(m+1)))
            eq(energy(v),energy(c[:m+1])/a-correction,'dilation_boundary_scale_identity')
    # With c=e_1, N=4, a=2: a nonzero boundary correction is indispensable.
    c=[0,1,0,0,0]; v=[0,0,1,0,0]
    require(energy(v)!=energy(c[:3])/2,'reject_omitted_rounding_boundary')
    require(energy([0,1])!=F(1),'reject_omitted_rank_one_boundary')

def jacobi_matrix(N):
    return [[F(2*(i+1)**2) if i==j else (F(-(min(i,j)+1)*(min(i,j)+2)) if abs(i-j)==1 else F(0))
             for j in range(N)] for i in range(N)]

def eliminate(matrix,labels,keep):
    matrix=[list(row) for row in matrix]; labels=list(labels)
    for label in list(labels):
        if label in keep: continue
        k=labels.index(label); pivot=matrix[k][k]
        require(pivot>0,'positive_schur_pivots')
        indices=[i for i in range(len(labels)) if i!=k]
        matrix=[[matrix[i][j]-matrix[i][k]*matrix[k][j]/pivot for j in indices] for i in indices]
        labels.pop(k)
    return matrix,labels

def schur_checks():
    for N in range(2,25):
        for a in range(2,min(N,8)+1):
            m=N//a; r=N+1-a*m
            matrix,labels=eliminate(jacobi_matrix(N),range(1,N+1),set(range(a,N+1,a)))
            expected=[[a*x for x in row] for row in jacobi_matrix(m)]
            expected[-1][-1]+=F(a*m*m*(a-r),r)
            eq(matrix,expected,'exact_dilation_schur_renormalization')
            eq(labels,[a*j for j in range(1,m+1)],'retained_arithmetic_indices')
    for N in (12,17,23):
        full=jacobi_matrix(N); labs=list(range(1,N+1)); keep=set(range(6,N+1,6))
        direct,_=eliminate(full,labs,keep)
        for first in (2,3):
            middle,labels=eliminate(full,labs,set(range(first,N+1,first)))
            final,_=eliminate(middle,labels,keep)
            eq(final,direct,'factor_order_schur_coherence')

def arithmetic(N):
    spf=list(range(N+1))
    for p in range(2,isqrt(N)+1):
        if spf[p]==p:
            for k in range(p*p,N+1,p):
                if spf[k]==k: spf[k]=p
    mu=[0,1]+[0]*(N-1)
    liouville=[0,1]+[0]*(N-1)
    for n in range(2,N+1):
        p=spf[n]; m=n//p
        liouville[n]=-liouville[m]
        mu[n]=0 if m%p==0 else -mu[m]
    return spf,mu,liouville

def factors(n,spf):
    out={}
    while n>1:
        p=spf[n]; j=0
        while n%p==0: n//=p; j+=1
        out[p]=j
    return out

def authenticate(mu):
    N=len(mu)-1; sums=[0]*(N+1)
    for d in range(1,N+1):
        if mu[d]:
            for n in range(d,N+1,d): sums[n]+=mu[d]
    if sums[1]!=1 or any(sums[2:]):
        raise ValueError('primitive Mobius authentication failed')

def source_checks(spf,mu,lam):
    N=len(mu)-1
    authenticate(mu)
    COUNTS['dirichlet_inverse_coefficients']+=N
    for n in range(1,N+1):
        eq(lam[n]*mu[n],mu[n]**2,'liouville_source_gauge')
        for p,j in factors(n,spf).items():
            value=j*mu[n]; d=1
            for a in range(1,j+1):
                d*=p; value+=mu[n//d]
            eq(value,0,'logarithmic_convolution_prime_coefficients')
    bad=list(mu); bad[2]+=1
    try: authenticate(bad)
    except ValueError: COUNTS['reject_corrupted_primitive_source']+=1
    else: raise ValueError('corrupted source accepted')
    for K in (12,31,63,127):
        for a in range(2,10):
            for b in range(2,10):
                ga=gcd(a,b); aa=a//ga; bb=b//ga
                image_a={a*n:mu[n] for n in range(1,K+1) if a*n>K}
                image_b={b*n:mu[n] for n in range(1,K+1) if b*n>K}
                dot=sum(x*image_b.get(n,0) for n,x in image_a.items())
                count=sum(mu[k]**2 for k in range(K//lcm(a,b)+1,K//max(aa,bb)+1) if gcd(k,aa*bb)==1)
                eq(dot,mu[aa]*mu[bb]*count,'native_escape_signed_count')
                if mu[a] and mu[b]:
                    require(mu[a]*mu[b]*dot>=0,'squarefree_weighted_escape_nonnegative')
    # Adding a prime need not contract the native energy.
    eq(energy([0,1,-1,0,0,0]),F(1,2),'prime_insertion_control_before')
    eq(energy([0,1,-1,-1,0,0]),F(2,3),'prime_insertion_control_after')
    return {'authenticated_through':N,'source_sha256':digest_ints(mu),
            'prime_insertion_counterexample':{'N':5,'old_primes':[2],'added_prime':3,
                                             'old_energy':'1/2','new_energy':'2/3'}}

def add_log(vector,integer,coefficient,spf):
    for p,e in factors(integer,spf).items(): vector[p]+=e*coefficient

def normalized(vector):
    return {p:c for p,c in vector.items() if c}

def log_interval(n,bits=96,terms=40):
    """Outward dyadic interval for log(n), using atanh on a ratio in [1,2)."""
    def series(r):
        z=(r-1)/(r+1); term=z; total=F(0)
        for j in range(terms):
            total+=2*term/(2*j+1); term*=z*z
        tail=2*term/((2*terms+1)*(1-z*z))
        return total,total+tail
    k=n.bit_length()-1
    l2,u2=series(F(2)); lo,hi=series(F(n,1<<k))
    lo+=k*l2; hi+=k*u2; scale=1<<bits
    return (lo.numerator*scale//lo.denominator,
            -((-hi.numerator*scale)//hi.denominator))

def enclosure(constant,vector,D,logs,bits=96,outbits=40):
    lo=hi=constant*(1<<bits)
    for p,c in vector.items():
        a,b=logs[p]
        lo+=c*(a if c>=0 else b)
        hi+=c*(b if c>=0 else a)
    den=D*(1<<bits); out=1<<outbits
    lo=lo*out//den; hi=-((-hi*out)//den)
    return {'lower_numerator':lo,'upper_numerator':hi,'denominator':out,
            'display':[lo/out,hi/out]}

def ward_panel(N,spf,mu,logs,character=None):
    source=mu[:N+1] if character is None else [mu[n]*character(n) for n in range(N+1)]
    M=prefix(source); D=lcm(*range(1,N+2))
    weights=[0]+[D//(k*(k+1)) for k in range(1,N+1)]
    require(all(D%(k*(k+1))==0 for k in range(1,N+1)),'exact_common_denominator')
    E=sum(M[k]**2*weights[k] for k in range(1,N+1))
    Wprefix=[0]
    for k in range(1,N+1): Wprefix.append(Wprefix[-1]+M[k]*weights[k])
    V=defaultdict(int); Q=defaultdict(int); C=defaultdict(int); prime_only=defaultdict(int)
    for k in range(1,N+1):
        add_log(V,k,M[k]**2*(D//k),spf)
        add_log(V,k+1,-M[k]**2*(D//(k+1)),spf)
        q=M[k]*(Wprefix[N]-Wprefix[k])-M[k]**2*(D//(k+1))
        add_log(Q,k+1,q,spf); add_log(Q,k,-q,spf)
    prime_powers=0
    for p in range(2,N+1):
        if spf[p]!=p: continue
        d=p
        while d<=N:
            acc=sum(M[j]*(Wprefix[min(N,d*(j+1)-1)]-Wprefix[d*j-1]) for j in range(1,N//d+1))
            if N<=127:
                direct=sum(M[k]*M[k//d]*weights[k] for k in range(d,N+1))
                eq(acc,direct,'direct_vs_hyperbola_correlations')
            weight=1 if character is None else character(d)
            C[p]+=weight*acc
            if d==p: prime_only[p]+=weight*acc
            prime_powers+=1; d*=p
    difference={p:Q.get(p,0)-V.get(p,0) for p in set(Q)|set(V)}
    eq(normalized(difference),normalized(C),'ward_identity_all_prime_log_coefficients')
    if character is None:
        require(normalized(C)!=normalized(prime_only),'reject_omitted_prime_power_channels')
    out={'N':N,'mertens':M[N],'prime_power_channels':prime_powers,
         'common_denominator_bits':D.bit_length(),
         'symbolic_coefficients_sha256':digest_ints([D,E]+[x for p in sorted(set(Q)|set(V)|set(C)) for x in (p,V[p],Q[p],C[p])]),
         'E':enclosure(E,{},D,logs), 'V_log_moment':enclosure(E,V,D,logs),
         'Q_positive_resolvent':enclosure(E,Q,D,logs), 'W_complete_covariance':enclosure(0,C,D,logs)}
    require(out['Q_positive_resolvent']['lower_numerator']>=0,'directed_positive_resolvent')
    require(out['Q_positive_resolvent']['upper_numerator']<=2*out['E']['lower_numerator'],'directed_resolvent_upper')
    require(out['V_log_moment']['lower_numerator']>=0,'directed_log_moment_positive')
    return out

def run(limit):
    COUNTS.clear()
    spf,mu,lam=arithmetic(limit+1)
    spectral=moment_checks()
    matrix_checks()
    schur_checks()
    source=source_checks(spf,mu[:limit+1],lam[:limit+1])
    logs={p:log_interval(p) for p in range(2,limit+2) if spf[p]==p}
    panels=[ward_panel(n,spf,mu,logs) for n in sorted(set([31,63,127,255,1023,limit]))]
    characters={'mod3':lambda n:0 if n%3==0 else (1 if n%3==1 else -1),
                'mod4':lambda n:0 if n%2==0 else (1 if n%4==1 else -1)}
    twists={}
    for name,chi in characters.items():
        for a in range(1,64):
            for b in range(1,64): eq(chi(a*b),chi(a)*chi(b),'character_multiplicativity_control')
        twists[name]=ward_panel(255,spf,mu,logs,chi)
    # Fixed rational bounds provide a minimal independent sanity check for log evaluation.
    l2,u2=logs[2]
    require(2*(1<<96)<3*l2 and 4*u2<3*(1<<96),'directed_log2_sanity')
    return {'status':'proposed component comparisons, not a native asymptotic improvement or RH proof',
            'arithmetic':'integers, exact Fractions, explicit outward dyadic log bounds',
            'source':source,'spectral_checks':spectral,'ward_panels':panels,'twisted_panels':twists,
            'predicate_counts':dict(sorted(COUNTS.items())),
            'not_established':['independent mathematical review','proof-assistant verification',
                               'repository-wide CI','new asymptotic bound for native E_N',
                               'identification with full Newton or Weil covariance','RH']}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--limit',type=int,default=4095)
    ap.add_argument('--output',type=Path)
    ap.add_argument('--check',type=Path)
    args=ap.parse_args()
    if not 1023<=args.limit<=16383: ap.error('--limit must be between 1023 and 16383')
    result=run(args.limit)
    if args.check:
        expected=json.loads(args.check.read_text(encoding='utf-8'))
        if result!=expected: raise ValueError('receipt does not match primitive replay')
    text=json.dumps(result,indent=2,sort_keys=True)+'\n'
    if args.output: args.output.write_text(text,encoding='utf-8')
    print(text,end='')

if __name__=='__main__': main()
