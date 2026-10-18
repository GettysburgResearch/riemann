"""Exact finite verification for five research routes; not a proof of RH.

Run one lane per subprocess. The replay runs lanes concurrently, but those
processes are mathematical checks, NOT separate research agents. Explicit
checks remain active under python -O. No accepting test computes zeta zeros.
"""
import argparse
from collections import Counter
from fractions import Fraction as Q
from itertools import product
import json
from math import comb, gcd, isqrt
import sys
from intervals import I, sqrt_i, log_i, log_scalar, atan_scalar, pi_i, B_positive

COUNTS = Counter()
MUTANT = ''

def check(ok, gate):
    if not ok:
        raise ValueError('REJECT:'+gate)
    COUNTS[gate] += 1

def sieve(n):
    spf = list(range(n+1))
    for p in range(2,isqrt(n)+1):
        if spf[p] == p:
            for k in range(p*p,n+1,p):
                if spf[k] == k:
                    spf[k] = p
    mu = [0]*(n+1); mu[1] = 1
    for k in range(2,n+1):
        p=spf[k]; r=k//p
        mu[k]=0 if r%p==0 else -mu[r]
    return spf,mu

def factor(n,spf):
    out=[]
    while n>1:
        p=spf[n]; e=0
        while n%p==0:
            n//=p; e+=1
        out.append((p,e))
    return out

def divisors(n):
    out=[]
    for d in range(1,isqrt(n)+1):
        if n%d==0:
            out.append(d)
            if d*d!=n: out.append(n//d)
    return sorted(out)

def jacobi(a,n):
    if n<=0 or n%2==0:
        raise ValueError('Jacobi denominator')
    a%=n; sign=1
    while a:
        while a%2==0:
            a//=2
            if n%8 in (3,5): sign=-sign
        a,n=n,a
        if a%4==n%4==3: sign=-sign
        a%=n
    return sign if n==1 else 0

def conv(a,b):
    n=min(len(a),len(b))-1
    out=[0]*(n+1)
    for i in range(1,n+1):
        for j in range(1,n//i+1):
            out[i*j]+=a[i]*b[j]
    return out

def b_coeff(n,d,spf,mu):
    if gcd(n,6)>1 or not mu[n]: return 0
    z=mu[n]
    for p,e in factor(n,spf):
        c=jacobi(-d,p)
        if MUTANT=='ramified_as_split' and c==0: c=1
        z*=1+c
    return z

def fields():
    spf,mu=sieve(65536)
    fixtures=(3,7,11,15,19,23,35,51,67,163,255)
    nmax=256
    mu6=[mu[n] if gcd(n,6)==1 else 0 for n in range(nmax+1)]
    ramified_witnesses=0
    for d in fixtures:
        check(mu[d]!=0 and d%4==3,'fundamental_discriminant')
        mch=[0]+[mu6[n]*jacobi(-d,n) if n%2 else 0 for n in range(1,nmax+1)]
        a=conv(mu6,mch)
        b=[0]+[b_coeff(n,d,spf,mu) for n in range(1,nmax+1)]
        v=[0,1]+[0]*(nmax-1); w=v.copy()
        for n in range(2,nmax+1):
            vv=ww=1
            for p,e in factor(n,spf):
                c=jacobi(-d,p) if p>=5 else 0
                if p<5 or c==0:
                    vp=wp=0
                elif c==1:
                    vp=-(e-1) if e>=2 else 0
                    wp=2**(e-2) if e>=2 else 0
                else:
                    vp=int(e%2==0); wp=-1 if e==2 else 0
                if MUTANT=='erase_power_tail' and e>=3: wp=0
                vv*=vp; ww*=wp
            v[n]=vv; w[n]=ww
        av,bw,vw=conv(a,v),conv(b,w),conv(v,w)
        for n in range(1,nmax+1):
            check(av[n]==b[n],'ramified_convolution')
            check(bw[n]==a[n],'inverse_complete_powers')
            check(vw[n]==int(n==1),'inverse_kernel')
            if n>=5 and spf[n]==n and d%n==0:
                ramified_witnesses+=1
                check(b[n]==-1,'literal_ramification')
            if mu6[n]:
                ds=divisors(n)
                rhs=mu6[n]*sum(jacobi(-d,r) for r in ds)
                check(b[n]==rhs,'product_divisor_average')
    check(ramified_witnesses>0,'ramified_coverage')
    big=[d for d in range(3,65537,4) if mu[d]]
    check(len(big)>=65536//8,'field_population')
    rs=[r for r in range(3,66,2) if mu[r]]
    means={1:len(big)}
    for r in rs:
        z=sum(jacobi(-d,r) for d in big); means[r]=z
        check(z*z<=9*65536*r,'complete_character_mean')
        harmonic=sum((Q(1,j) for j in range(1,r//2+1)),Q(0))
        total=0
        for H in range(2*r):
            total+=jacobi(4*H+3,r)
            check(total*total<=r*harmonic*harmonic,'primitive_PV_progression')
    for xmax in (8,16,32,64):
        err=0
        for n in range(1,xmax+1):
            if gcd(n,6)>1 or not mu[n]: continue
            s=sum(means[r] for r in divisors(n))
            err+=abs(s-len(big))
        check(65536*err*err<=2304*xmax**3*len(big)**2,'weighted_full_family')
        if isqrt(xmax)**2==xmax:
            bound=9216*xmax*xmax*isqrt(xmax)*(1+log_scalar(Q(xmax)).lo)*len(big)**2
            check(65536*err*err<=bound,'refined_weighted_full_family')
    small=[d for d in range(3,1025,4) if mu[d]]
    for n in range(1,65):
        lhs=sum(b_coeff(n,d,spf,mu) for d in small)
        rhs=0 if gcd(n,6)>1 else mu[n]*sum(sum(jacobi(-d,r) for d in small) for r in divisors(n))
        check(lhs==rhs,'independent_full_average')
    for theta in (Q(1,2),Q(2,3),Q(3,4),Q(5,6),Q(7,8)):
        q=Q(5,2)-2*theta
        check(Q(5,4)-q/2==theta,'family_scale_budget')
    return {'discriminants':list(fixtures),'complete_convolution_limit':nmax,
            'large_family_Q':65536,'large_family_size':len(big),
            'character_moduli':rs,'ramified_witnesses':ramified_witnesses,
            'actual_L_values':False,'cancellation_estimate_proved_by_tests':False}

def probes():
    spf,mu=sieve(40)
    for m in range(1,9):
        for degree in range(m):
            for u in (Q(-2),Q(0),Q(3,7)):
                for h in (Q(1),Q(2,3),Q(7,4)):
                    for dilation in (2,3):
                        s=Q(0)
                        for j in range(m+1):
                            norm=Q(1,dilation**j)
                            if MUTANT=='unnormalized_probe': norm=1
                            s+=(-1)**j*comb(m,j)*norm*dilation**j*(u+j*h)**degree
                        check(s==0,'normalized_bias_removal')
    def W(x): return 1/(1+x+x*x)
    for m in range(1,5):
        for scale in (Q(1),Q(3,2),Q(5)):
            for d in (2,3):
                lhs=sum((-1)**j*comb(m,j)*Q(1,d**j)*sum(mu[n]*W(Q(n)/(scale*d**j)) for n in range(1,41)) for j in range(m+1))
                rhs=sum(mu[n]*sum((-1)**j*comb(m,j)*Q(1,d**j)*W(Q(n)/(scale*d**j)) for j in range(m+1)) for n in range(1,41))
                check(lhs==rhs,'complete_rescaled_source')
    for modulus,gap in ((3,1),(4,2)):
        for n in range(100):
            for sigma in range(1,6):
                term=Q(1,(modulus*n+1)**sigma)-Q(1,(modulus*n+1+gap)**sigma)
                check(term>0,'small_field_positive_pairs')
    for n in range(1,257):
        k=isqrt(2*n*n)
        for m in (k,k+1):
            check(abs(2*n*n-m*m)>=1,'integer_separation')
    # Exact algebraic noncoincidence. With h2=2 the t=2pi first notch is hidden.
    h2_square=4 if MUTANT=='commensurate_pair' else 2
    check(h2_square!=isqrt(h2_square)**2,'joint_nonreal_visibility')
    for multiplicity in range(1,13):
        for nonzero_factor in (Q(1,3),Q(-2),Q(7,5)):
            residue=-multiplicity*nonzero_factor
            check(residue!=0,'multiplicity_preservation')
    return {'difference_orders':[1,8],'finite_source_terms':40,
            'integer_separation_n':[1,256],'synthetic_pole_orders':[1,12],
            'physical_CT_projection_estimated':False}

def law_product(a,b):
    out={}
    for x,p in a.items():
        for y,q in b.items(): out[x+y]=out.get(x+y,Q(0))+p*q
    return out

def moment(law,k): return sum((p*x**k for x,p in law.items()),Q(0))

def strip():
    complete={Q(0):Q(1)}; even=[Q(1)]+[Q(0)]*10
    for a,w in ((Q(3,2),Q(1,3)),(Q(5,4),Q(2,5)),(Q(1,2),Q(3,7)),(Q(2),Q(1))):
        den=a if MUTANT=='strip_normalization' else a+1
        law={Q(0):a/den,w:1/(2*den),-w:1/(2*den)}
        check(sum(law.values())==1,'probability_normalization')
        var=w*w/(a+1)
        for k in range(1,11):
            check(moment(law,2*k)==w**(2*k)/(a+1),'three_point_moments')
            check(moment(law,2*k)<=var*w**(2*k-2),'variance_tail_budget')
        new=[Q(0)]*11
        for k in range(11):
            new[k]=sum(comb(2*k,2*j)*even[j]*moment(law,2*(k-j)) for j in range(k+1))
        complete=law_product(complete,law); even=new
        for k in range(21):
            check(moment(complete,k)==(even[k//2] if k%2==0 else 0),'complete_product_moments')
    for r in (Q(2),Q(3),Q(3,2),Q(5,4)):
        a=(r+1/r)/2
        for root in (-r,-1/r):
            check(root*root+2*a*root+1==0,'exact_zero_polynomial')
    counter=[]
    for n in (16,24,32,64,128,256,512):
        a=(Q(2)**n+Q(1,2)**n)/2; v=Q(n*n)/(a+1)
        check(0<v<1,'rare_variance_domain')
        base=1 if MUTANT=='rare_variance_omitted' else 1-v
        check(base+v==1,'rare_total_variance')
        g=(a+(Q(4)**n+Q(1,4)**n)/2)/(a+1)
        check(g>=2**(n-1),'complex_escape')
        counter.append({'n':n,'variance':str(v),'imaginary_value_lower':str(g)})
        for k in range(1,6):
            full=sum(comb(2*k,2*j)*base**j*(Q(1) if k==j else Q(n**(2*(k-j)))/(a+1)) for j in range(k+1))
            check(full>=0,'rare_fixed_moments')
    # The finite Taylor-tail factor uses only r/R<1, not a horizontal-height limit.
    for L in range(1,21):
        for q in (Q(1,4),Q(1,2),Q(3,4)):
            for k in range(L+1,L+8):
                check(q**k<=q**(L+1),'disk_tail_factor')
    return {'complete_product_support':len(complete),'moments_checked_through':20,
            'counterexample_parameters':counter,'actual_theta_fit':False,
            'new_degree_certificate':False}

def newton():
    spf,mu=sieve(625)
    tested_q=0; above=0
    for Y in range(2,25):
        z=[Q(0)]*(Y*Y+1)
        for a in range(1,Y+1):
            for b in range(1,Y+1): z[a*b]+=mu[a]*mu[b]
        T=[Q(0)]*(Y*Y+1)
        for d in range(1,Y+1):
            T[d]=sum((Q(mu[n],n) for n in range(d,Y+1,d)),Q(0))
        C=[]
        for q in range(Y*Y+1):
            if q==0: C.append(Q(0)); continue
            limit=Y if MUTANT=='drop_above_output_products' else Y*Y
            value=sum((z[d]/d for d in range(q,limit+1,q)),Q(0)); C.append(value)
            fac=factor(q,spf)
            if any(e>=3 for p,e in fac):
                check(value==0,'complete_cube_zero'); continue
            r=1; primes=[]
            for p,e in fac:
                if e==2:r*=p
                else:primes.append(p)
            rhs=Q(0)
            for choices in product(range(3),repeat=len(primes)):
                u=v=w=1
                for p,j in zip(primes,choices):
                    if j==0:u*=p
                    elif j==1:v*=p
                    else:w*=p
                rhs+=mu[w]*T[r*u*w]*T[r*v*w]
            check(value==rhs,'all_product_mask_factorization'); tested_q+=1
            if not primes:
                check(value==T[r]*T[r] and value>=0,'square_sector')
            truncated=sum((z[d]/d for d in range(q,min(Y+1,Y*Y)+1,q)),Q(0))
            above+=int(value!=truncated)
        H=lambda n:sum((Q(1,j) for j in range(1,n+1)),Q(0))
        hy,hy2=H(Y),H(Y*Y)
        denom=2304*hy*hy*hy2**6
        for ratio in (Q(1,3),Q(1),Q(3,2),Q(Y),Q(Y*Y+2)):
            G=denom*ratio; S=min(Y*Y,G//denom)
            removed_sq=Q(0) if S==0 else 144*S*hy*hy*H(S)**6
            rhs=G/16
            if MUTANT=='root_budget_omitted': rhs=G/1000
            check(removed_sq<=rhs,'adaptive_complete_core_budget')
    check(above>0,'above_output_coverage')
    rows=[]
    for a,p in ((Q(1,3),Q(3,2)),(Q(1,4),Q(3,2)),(Q(1,3),Q(4,3)),(Q(0),Q(7,4))):
        fixed=a/(2-p); k=Q(3,4)
        for j in range(1,13):
            k=(a+p*k)/(1 if MUTANT=='missing_square_scale' else 2)
            check(k==fixed+(p/2)**j*(Q(3,4)-fixed),'full_recurrence_exponents')
        rows.append({'a':str(a),'p':str(p),'limit_boundary':str((1+fixed)/2)})
    return {'prefix_Y':[2,24],'complete_nonzero_core_cases':tested_q,
            'above_output_witnesses':above,'conditional_targets':rows,
            'rough_core_bound_proved':False,'all_Y_recurrence_proved':False}

def trim(p):
    while len(p)>1 and p[-1]==0:p.pop()
    return p

def padd(a,b):
    c=[0]*max(len(a),len(b))
    for i,v in enumerate(a):c[i]+=v
    for i,v in enumerate(b):c[i]+=v
    return trim(c)

def pmul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b):c[i+j]+=u*v
    return trim(c)

def pdiv(a,b):
    a=a.copy(); c=[0]*max(1,len(a)-len(b)+1)
    while len(a)>=len(b) and a!=[0]:
        k=len(a)-len(b)
        if a[-1]%b[-1]:raise ValueError('nonintegral polynomial division')
        v=a[-1]//b[-1];c[k]=v
        for j,x in enumerate(b):a[k+j]-=v*x
        trim(a)
    if a!=[0]:raise ValueError('nonzero polynomial remainder')
    return trim(c)

def peval(p,t):
    out=Q(0)
    for x in reversed(p):out=out*t+x
    return out

def determinant(a):
    a=[list(map(Q,row)) for row in a]; out=Q(1); n=len(a)
    for i in range(n):
        pivot=next((j for j in range(i,n) if a[j][i]),None)
        if pivot is None:return Q(0)
        if pivot!=i:a[i],a[pivot]=a[pivot],a[i];out=-out
        v=a[i][i];out*=v
        for j in range(i+1,n):
            r=a[j][i]/v
            for k in range(i+1,n):a[j][k]-=r*a[i][k]
    return out

def determinant_lane():
    spf,mu=sieve(512)
    D={1:[0,1]}; C={0:[0],1:[0,1]}
    for n in range(1,32):
        C[n+1]=padd(padd(pmul([2,1],C[n]),[-x for x in C[n-1]]),[0,2])
    for n in range(2,33):
        den=[1]
        for d in divisors(n)[:-1]:den=pmul(den,D[d])
        D[n]=pdiv(C[n],den)
        check(pmul(D[n],den)==C[n],'whole_cycle_factorization')
        fac=factor(n,spf)
        base=fac[0][0] if len(fac)==1 else 1
        expected=base*base
        if MUTANT=='delete_prime_powers' and len(fac)==1 and fac[0][1]>1:expected=1
        check(D[n][0]==expected,'prime_power_determinant')
        check(all(x>0 for x in D[n]),'positive_polynomial_coefficients')
    for n in range(2,10):
        P=[[Q(sum(d*mu[n//d] for d in divisors(gcd(n,i-j))),n) for j in range(n)] for i in range(n)]
        L=[[2*int(i==j)-int(j==(i+1)%n)-int(j==(i-1)%n) for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                check(sum(P[i][k]*P[k][j] for k in range(n))==P[i][j],'rational_primitive_projector')
        for t in (Q(0),Q(1,16),Q(1,4),Q(1)):
            H=[[int(i==j)-P[i][j]+sum(P[i][k]*L[k][j] for k in range(n))+t*P[i][j] for j in range(n)] for i in range(n)]
            check(determinant(H)==peval(D[n],t),'rational_matrix_determinant')
            for j in range(1,n+1):
                check(determinant([row[:j] for row in H[:j]])>0,'positive_definite_minors')
    # Interval backend algebra and independent identities, not external floating truth.
    for a in range(1,21):
        for b in range(1,8):
            x=Q(a,b); rt=sqrt_i(x)
            check(rt.lo*rt.lo<=x<=rt.hi*rt.hi,'directed_sqrt')
            lx=log_scalar(x); prodlog=log_scalar(2*x)-log_scalar(2)
            check(max(lx.lo,prodlog.lo)<=min(lx.hi,prodlog.hi),'directed_log_identity')
    pi=pi_i()
    check(pi.lo>Q(314159,100000) and pi.hi<Q(314160,100000),'machin_pi_enclosure')
    for x in (Q(1,4),Q(1,2),Q(3,4),Q(1),Q(3),Q(7)):
        z=atan_scalar(x)+atan_scalar(1/x)-pi/2
        check(z.lo<=0<=z.hi,'atan_reciprocal')
    reports=[]
    for N in (3,4,6,8,12,16,24,32):
        masses=[Q(1,16),Q(1,4),Q(1)]
        if N in (4,8,16,24,32):
            for theta in (Q(1,2),Q(5,6)):
                power=(1+theta)/2
                c=next(j for j in range(1,N+1) if j**power.denominator>=N**power.numerator)
                t=Q(c*c,N*N)
                check(t<=1 and t**theta.denominator*N**(theta.denominator-theta.numerator)>=1,'mesoscopic_conditioning_scale')
                masses.append(t)
        for t in masses:
            V=I(0); cp=I(0)
            for n in range(2,N+1):
                V+=(N-n)*log_scalar(peval(D[n],t))/2
                fac=factor(n,spf)
                if len(fac)==1:cp+=(N-n)*log_scalar(Q(fac[0][0]))
            b=N*log_i(1+t/2+sqrt_i(t+t*t/4))
            if MUTANT=='wrong_mass_parameter': b=I(N)*sqrt_i(t)
            BB=B_positive(b,128)
            err=V-cp-N*N*BB
            harmonic=sum((Q(1,m) for m in range(1,N+1)),Q(0))
            lower_budget=b.lo*b.lo*(harmonic/72+Q(1,24*N)+Q(1,576))
            check(max(abs(err.lo),abs(err.hi))<=lower_budget,'all_mass_regularization')
            reports.append({'N':N,'t':str(t),'b':b.text(),'error':err.text(),'budget_lower':str(lower_budget)})
    # Exact unit-sensitive rearrangement for polynomial test profiles, all terms.
    for N in range(2,17):
        for degree in (2,3,4):
            b=Q(7,3)
            left=sum((N-n)*sum(mu[n//d]*(b*d/N)**degree for d in divisors(n)) for n in range(2,N+1))
            right=sum(mu[m]*sum((N-m*d)*(b*d/N)**degree for d in range(1,N//m+1)) for m in range(1,N+1))
            if MUTANT!='lost_unit':right-=(N-1)*(b/N)**degree
            check(left==right,'unit_preserving_rearrangement')
    return {'complete_polynomial_limit':32,'rational_matrix_n':[2,9],
            'mass_comparisons':reports,'B_positive_series_cutoff':128,
            'B_tail_included':True,'centered_height_bound_proved':False}

LANES={'fields':fields,'probes':probes,'strip':strip,'newton':newton,'determinant':determinant_lane}

def main():
    global MUTANT
    ap=argparse.ArgumentParser();ap.add_argument('--lane',choices=LANES,required=True)
    ap.add_argument('--mutant',default='')
    args=ap.parse_args();MUTANT=args.mutant
    try:
        scope=LANES[args.lane]()
        print(json.dumps({'lane':args.lane,'predicates':sum(COUNTS.values()),
                         'gates':dict(sorted(COUNTS.items())),'scope':scope,
                         'rh_established':False},sort_keys=True,indent=2))
    except (ValueError,ArithmeticError) as e:
        print(str(e),file=sys.stderr);return 2
    return 0

if __name__=='__main__':
    raise SystemExit(main())
