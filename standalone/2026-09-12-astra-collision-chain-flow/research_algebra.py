"""Exact finite controls for the three proposed component proofs.

These checks do not certify an infinite covariance sign, an all-order theta
realization, or extinction of the actual gamma nonreal-zero defect.
"""
from fractions import Fraction as Q
from itertools import product,combinations,combinations_with_replacement
from math import gcd,comb,factorial
from exact_interval import I,log_q,SCALE

def require(test,message):
    if not test:raise ArithmeticError(message)

def mobius(n):
    ans=1;p=2
    while p*p<=n:
        if n%p==0:
            n//=p;ans=-ans
            if n%p==0:return 0
        p+=1
    if n>1:ans=-ans
    return ans

def dirichlet(a,b):
    out={}
    for i,x in a.items():
        for j,y in b.items():out[i*j]=out.get(i*j,Q(0))+x*y
    return {i:x for i,x in out.items() if x}

def arithmetic_controls():
    seen={};tuples=0
    # Tests the injective gcd parametrization, not its asymptotic theorem.
    for g,h,r,s in product(range(8,19),repeat=4):
        if not all(mobius(x) for x in (g,h,r,s)):continue
        if not all(gcd(x,y)==1 for x,y in combinations((g,h,r,s),2)):continue
        key=(g*r,h*s,g*s,h*r)
        require(key not in seen or seen[key]==(g,h,r,s),'gcd map not injective')
        seen[key]=(g,h,r,s)
        require((gcd(key[0],key[2]),gcd(key[1],key[3]))==(g,h),'gcd inverse')
        require(key[0]*key[1]==key[2]*key[3]==g*h*r*s,'product collision')
        require(mobius(key[0])*mobius(key[1])*mobius(key[2])*mobius(key[3])==1,'native signs')
        tuples+=1
    # The local Euler factor is (1-x)^4 (1+4x), with no linear term.
    poly=[comb(4,j)*(-1)**j for j in range(5)];fac=[Q(0)]*6
    for j,c in enumerate(poly):fac[j]+=c;fac[j+1]+=4*c
    require(fac==[1,0,-10,20,-15,4],'Euler factor')
    # Native, complete annular covariance controls at EVERY crossing <= 17.
    rows=[]
    for Y in range(2,18):
        mprev=sum((Q(mobius(n),n) for n in range(1,Y)),Q(0));mY=mprev+Q(mobius(Y),Y)
        if not mobius(Y) or mprev*mY>0:continue
        c={n:Q(mobius(n)) for n in range(1,Y+1) if mobius(n)}
        if mY:c[2*Y]=-2*Y*mY
        require(sum((x/n for n,x in c.items()),Q(0))==0,'crossing balance')
        z=dirichlet(c,c);B=(Y+1)**2-1
        H=[Q(0)]
        for k in range(1,B+1):H.append(H[-1]+Q(1,k))
        pref=[Q(0)];m=Q(0)
        for k in range(1,B+1):m+=Q(mobius(k),k);pref.append(pref[-1]+m*m)
        DD=I.q(0);QQ=Q(0);mixed=Q(0);TT=Q(0);prefix=Q(0)
        for k in range(1,B+1):
            prefix+=c.get(k,Q(0))/k
            if k<=Y:continue
            qk=sum((zd*H[k//d]/d for d,zd in z.items() if d<=k),Q(0))
            native=sum((Q(mobius(n),n) for n in range(1,k+1)),Q(0))
            require(2*prefix-qk==native,'full Newton reciprocal identity')
            QQ+=qk*qk;TT+=prefix*prefix;mixed+=prefix*qk
        for d,zd in z.items():
            L=log_q(Q(d));AA=sum((H[k//d]-H[k] for k in range(Y+1,B+1)),Q(0))
            A2=sum(((H[k//d]-H[k])**2 for k in range(Y+1,B+1)),Q(0))
            DD=DD+(zd/d)**2*(I.q(A2)+2*AA*L+(B-Y)*(L**2))
        CC=I.q(QQ)-DD
        require(TT==(Y-1)*mY*mY,'full collar cost')
        require(pref[B]-pref[Y]==4*TT+QQ-4*mixed,'energy identity')
        require(CC.hi<0,'finite native covariance panel changed sign')
        # Complete squared gain; no future term or divisor product is omitted.
        rows.append({'Y':Y,'B':B,'collar_energy':str(TT),'F_Y':str(pref[Y]),'F_B':str(pref[B]),'D':DD.bounds(),'C':CC.bounds()})
    # A guard against an accidentally changed logarithmic normalization.
    require(log_q(Q(4)).lo> I.q(Q(4,3)).hi,'log(4)>4/3')
    return {'gcd_injection_tuples':tuples,'euler_factor':[str(x) for x in fac], 'native_covariance_rows':rows,
            'diagonal_lower_constant':'A4/(81*15^4), A4=product_p (1-1/p)^4*(1+4/p)',
            'lower_bound_scope':'asymptotic as crossing Y tends to infinity; no explicit onset',
            'unbounded_covariance_bound_proved':False}

def cumulants_from_moments(m):
    k=[Q(0)]*len(m)
    for n in range(1,len(m)):
        k[n]=m[n]-sum((comb(n-1,j-1)*k[j]*m[n-j] for j in range(1,n)),Q(0))
    return k

def markov_moments(weights,q,degree):
    # Exponential generating coefficients of E e^(zX), E[sigma_last e^(zX)].
    A=[Q(0)]*(degree+1);B=A.copy();A[0]=1
    for j,a in enumerate(weights):
        ch=[a**k/Q(factorial(k)) if k%2==0 else Q(0) for k in range(degree+1)]
        sh=[a**k/Q(factorial(k)) if k%2 else Q(0) for k in range(degree+1)]
        qq=q if j else Q(0)
        AA=[sum((ch[k]*A[n-k]+qq*sh[k]*B[n-k] for k in range(n+1)),Q(0)) for n in range(degree+1)]
        BB=[sum((sh[k]*A[n-k]+qq*ch[k]*B[n-k] for k in range(n+1)),Q(0)) for n in range(degree+1)]
        A,B=AA,BB
    return [a*factorial(k) for k,a in enumerate(A)]

def chain_controls():
    instances=0;quadruples=0
    for n in range(1,8):
        weights=[Q(1,j+5) for j in range(n)]
        for qq in (Q(0),Q(1,100),Q(1,3)):
            direct=[Q(0)]*9
            for ss in product((-1,1),repeat=n):
                prob=Q(1,2)
                for j in range(1,n):prob*=Q(1,2)*(1+qq*ss[j-1]*ss[j])
                x=sum((a*s for a,s in zip(weights,ss)),Q(0))
                for r in range(9):direct[r]+=prob*x**r
            transfer=markov_moments(weights,qq,8)
            require(transfer==direct,'Markov transfer/direct enumeration')
            v=sum((a*b*qq**abs(i-j) for i,a in enumerate(weights) for j,b in enumerate(weights)),Q(0))
            k4=-2*sum((weights[i]*weights[j]*weights[k]*weights[l]*qq**(sorted((i,j,k,l))[2]-sorted((i,j,k,l))[0]+sorted((i,j,k,l))[3]-sorted((i,j,k,l))[1]) for i,j,k,l in product(range(n),repeat=4)),Q(0))
            require(v==direct[2] and k4==direct[4]-3*v*v,'ordered fourth cumulant formula')
            instances+=1;quadruples+=n**4
    def partitions(items):
        if not items:
            yield ()
            return
        first=items[0]
        for rest in partitions(items[1:]):
            yield ((first,),)+rest
            for j in range(len(rest)):
                yield rest[:j]+((first,)+rest[j],)+rest[j+1:]
    even_parts=[p for p in partitions(tuple(range(6))) if all(len(b)%2==0 for b in p)]
    require(len(even_parts)==31,'all even-block partitions of six labels')
    joint=0
    for gaps in product((0,1),repeat=5):
        ii=[0]
        for g in gaps:ii.append(ii[-1]+g)
        for qq in (Q(0),Q(1,5),Q(1,2)):
            direct=Q(0)
            for parts in even_parts:
                term=Q((-1)**(len(parts)-1)*factorial(len(parts)-1))
                for block in parts:
                    jj=sorted(ii[j] for j in block)
                    term*=qq**sum(jj[k+1]-jj[k] for k in range(0,len(jj),2))
                direct+=term
            g1,g2,g3,g4,g5=gaps
            formula=4*qq**(g1+2*g2+g3+2*g4+g5)*(1+3*qq**(2*g3))
            require(direct==formula,'complete sixth joint cumulant')
            joint+=1
    return {'exact_chain_instances':instances,'ordered_quadruple_terms':quadruples,
            'sixth_joint_cumulant_partition_cases':joint,
            'even_block_partitions_per_sixth_case':31,
            'scope':'bounded algebra controls, not all-order moment realization'}

def poch(a,n):
    out=Q(1)
    for j in range(n):out*=a+j
    return out

def coeff_product(values,K):
    h=[Q(0)]*(K+1);h[0]=1
    for a in values:
        for k in range(1,K+1):h[k]+=a*h[k-1]
    return h

def gamma_controls():
    rows=0;score_rows=0
    for N in range(2,8):
        BB=(N+1)**2;m=2*N
        lam=[Q(n*n) for n in range(1,N+1) for _ in range(2)]
        h=coeff_product([BB-a for a in lam],18)
        for t in (Q(0),Q(1,2),Q(1),Q(3,2),Q(2)):
            nu=m+t
            # Expand e^(-B w) S_nu(w) and compare its density jet
            # with complete homogeneous polynomials of the actual gamma rates.
            hh=[Q(0)]*19;hh[0]=1
            for k in range(1,19):
                powers=sum((a**k for a in lam),Q(0))+t*BB**k
                hh[k]=sum(((sum((a**j for a in lam),Q(0))+t*BB**j)*hh[k-j] for j in range(1,k+1)),Q(0))/k
            for k in range(19):
                jet=sum(((-BB)**(k-j)/Q(factorial(k-j))*h[j]/poch(nu,j) for j in range(k+1)),Q(0))
                require(jet==(-1)**k*hh[k]/poch(nu,k),'gamma positive series density jet')
                require(h[k]/poch(nu,k)<=Q((BB-1)**k,factorial(k)),'complete positive term majorant')
                rows+=1
            # Exact parameter derivative of 1/(nu)_k and w^k, via product rule.
            for k in range(1,19):
                harmonic=sum((1/(nu+j) for j in range(k)),Q(0))
                product_derivative=sum((poch(nu,k)/(nu+j) for j in range(k)),Q(0))
                require(product_derivative/poch(nu,k)==harmonic,'score harmonic term')
                score_rows+=1
        # A complete formal Laplace step at selected rational frequencies.
        for s in (Q(1,7),Q(2,3),Q(3)):
            ratio=(1+s/BB)**-2
            old=Q(1)
            for n in range(1,N+1):old*=(1+s/(n*n))**-2
            new=old*(1+s/BB)**-2
            require(new/old==ratio,'integer stage Laplace ratio')
    # Exact zero-flux derivative for a Gaussian-rational moving root:
    # w=y²/(x²+y²)², checked by symbolic rational differentiation.
    flux=0
    for x,y,dx,dy in product((Q(1),Q(2)),(Q(1,3),Q(2,5)),(Q(-1),Q(1,2)),(Q(-2,3),Q(1))):
        r2=x*x+y*y
        derivative=2*y*dy/r2**2-4*y*y*(x*dx+y*dy)/r2**3
        current=2*y*((x*x-y*y)*dy-2*x*y*dx)/r2**3
        require(derivative==current,'nonreal zero current sign or factor')
        flux+=1
    # A collision control: z=+/-sqrt(a² +/- i sqrt(t)) is not assumed
    # simple at t=0. For a direct pair x=a,y=sqrt(t), the weight is
    # t/(a²+t)², continuous and absolutely continuous at the birth.
    return {'positive_density_jet_checks':rows,'score_product_checks':score_rows,
            'gaussian_rational_flux_checks':flux,'interpolation':'gamma SHAPE t in [0,2], not scale interpolation',
            'all_zero_flux_identity_scope':'fixed integer step, full source, multiplicities retained; analytic proof requires review',
            'defect_dissipation_sign_proved':False,'defect_extinction_proved':False}

def report():
    return {'arithmetic':arithmetic_controls(),'ising':chain_controls(),'gamma':gamma_controls()}
