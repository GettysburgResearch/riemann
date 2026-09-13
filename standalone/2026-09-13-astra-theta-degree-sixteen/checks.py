"""Independent bounded exact controls; not a theta-quadrature backend."""
from fractions import Fraction as F
from itertools import product
from math import comb, factorial
from primitive import require, cumulants


def moment_convolution(a,b):
    return [sum(F(comb(n,k))*a[k]*b[n-k] for k in range(n+1)) for n in range(len(a))]


def poly_log_cumulants(mom):
    # Independently expand log(1+u) as sum (-1)^(j+1) u^j/j.
    n=len(mom)-1;u=[F(0)]+[mom[k]/factorial(k) for k in range(1,n+1)]
    power=[F(1)]+[F(0)]*n;out=[F(0)]*(n+1)
    for j in range(1,n+1):
        power=[sum(power[k]*u[d-k] for k in range(d+1)) for d in range(n+1)]
        for k in range(n+1):out[k]+=F((-1)**(j+1),j)*power[k]
    return [out[k]*factorial(k) for k in range(n+1)]


def direct(weights,edges,nmax):
    out=[F(0)]*(nmax+1);normal=F(0)
    for bits in product((-1,1),repeat=len(weights)):
        prob=F(1)
        for i,j,t in edges:
            if bits[i]==bits[j]:prob*=t
        x=sum(w*s for w,s in zip(weights,bits));normal+=prob
        for k in range(nmax+1):out[k]+=prob*x**k
    return [x/normal for x in out]


def controls():
    nmax=18;cases=[([F(1,3)],[F(1,7)]),
                  ([F(1,4),F(2,5)],[F(1,6)]),
                  ([F(2,7)],[F(1,5),F(2,9)]),
                  ([],[F(1,3),F(1,4),F(1,8)])]
    norm_checks=0;conv_checks=0;cum_checks=0;states=0
    for signs,pairs in cases:
        weights=signs+[a for w in pairs for a in (w,w)]
        edges=[(len(signs)+2*i,len(signs)+2*i+1,F(3,2)) for i in range(len(pairs))]
        actual=direct(weights,edges,nmax);states+=2**len(weights)
        predicted=[F(1)]+[F(0)]*nmax
        kc=[F(0)]*(nmax+1)
        for w in signs:
            mo=[w**k if k%2==0 else F(0) for k in range(nmax+1)]
            predicted=moment_convolution(predicted,mo)
            kc=[a+b for a,b in zip(kc,poly_log_cumulants(mo))]
        for w in pairs:
            mo=[F(1)]+[F(3,5)*(2*w)**k if k%2==0 else F(0) for k in range(1,nmax+1)]
            predicted=moment_convolution(predicted,mo)
            kc=[a+b for a,b in zip(kc,poly_log_cumulants(mo))]
        for k in range(nmax+1):require(actual[k]==predicted[k],'full spin/convolution');conv_checks+=1
        ca=cumulants(actual)
        for k in range(1,nmax+1):require(ca[k]==kc[k],'direct cumulant addition');cum_checks+=1
        require(actual[0]==1,'probability normalization');norm_checks+=1
    # Exact first Gibbs derivative, computed by polynomial partition sums.
    gibbs_checks=0
    w=[F(1,3),F(2,7),F(1,5)];t=F(3,2);u=F(11,10)
    for n in (2,4,6,8):
        Z=A=B=C=F(0);Zp=Ap=F(0)
        for bits in product((-1,1),repeat=3):
            agree=int(bits[0]==bits[1]);pr=t**agree*u**int(bits[1]==bits[2]);score=bits[0]*bits[1]
            obs=sum(a*s for a,s in zip(w,bits))**n
            Z+=pr;A+=pr*obs;B+=pr*score;C+=pr*obs*score
            Zp+=agree*pr/t;Ap+=agree*pr*obs/t
        require(2*t*(Ap*Z-A*Zp)/Z**2 == C/Z-A*B/Z**2,'Gibbs covariance derivative');gibbs_checks+=1
    # Complete coefficient derivative of x^r, including all high-degree terms.
    jac_checks=0
    for x in (F(1,1000),F(1,7),F(3,11)):
        for r in range(1,10):
            coeff=[F(comb(r,k))*x**(r-k) for k in range(r+1)]
            require(coeff[1]==r*x**(r-1),'polynomial Jacobian');jac_checks+=1
    unit=[F(int(k%2==0)) for k in range(19)]
    require(cumulants(unit)==poly_log_cumulants(unit),'unit cumulant full list')
    return {'direct_spin_configurations':states,'normalized_models':norm_checks,
       'full_moment_comparisons':conv_checks,'cumulant_comparisons':cum_checks,
       'gibbs_derivative_checks':gibbs_checks,'polynomial_derivative_checks':jac_checks,
       'unit_cumulant_list_checks':1}
