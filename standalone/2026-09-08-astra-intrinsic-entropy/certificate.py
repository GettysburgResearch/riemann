"""A single fixed, full-tail exponential-target certificate.
The injected integer interval core is authenticated by check.py before execution.
No floating-point value, zero table, quadrature, or special-function oracle enters.
"""
from fractions import Fraction as F
from math import comb, factorial, isqrt

COEFFICIENTS = tuple(F(x, 1000000) for x in
                     (949546,345582,16668,-144367,-201931,-191089,-125322))
CUTOFF = 2048


def certify(core):
    I, S = core.I, core.SCALE
    zero = I.of(0)
    K, X = 6, CUTOFF
    beta = [sum((COEFFICIENTS[j]*((-1)**k)*comb(j,k)
                 for j in range(k,K+1)), F(0)) for k in range(K+1)]
    def poly_square(p):
        out = [I.of(0) for _ in range(2*len(p)-1)]
        for i,a in enumerate(p):
            for j,b in enumerate(p): out[i+j] += a*b
        return out
    def sqnorm(p):
        z = sum((a*factorial(j) for j,a in enumerate(poly_square(p))),zero)
        if z.hi < 0: raise ArithmeticError('negative polynomial norm upper endpoint')
        return I(max(0,z.lo),z.hi)
    def sqroot(z):
        if z.hi < 0: raise ArithmeticError('negative sqrt')
        a=isqrt(max(0,z.lo)*S); b=isqrt(z.hi*S)
        if b*b < z.hi*S: b+=1
        return I(a,b)
    def atan(q):
        s=sum((I.of((-1)**j*q**(2*j+1)/F(2*j+1)) for j in range(64)),zero)
        return s+I.bounds(0,q**129/F(129))
    pi=16*atan(F(1,5))-4*atan(F(1,239))
    c=I(core.logq(F(2*pi.lo,S)).lo, core.logq(F(2*pi.hi,S)).hi)/2
    H=[I.of(0) for _ in range(K+1)]
    logfact=I.of(0); partial=I.of(0); cells=0
    for n in range(1,X):
        tn=core.logq(F(n)); logfact+=tn
        dt=core.logq(F(n+1,n)); g0=n*(1-tn)+logfact
        ip=[[I.of(0) for _ in range(K+2)] for _ in range(K+1)]
        ip[0][0]=g0;ip[0][1]=I.of(-n)
        for k in range(1,K+1):
            for l in range(k):ip[k][l]=H[k-l]/factorial(l)
            ip[k][k]=g0/factorial(k);ip[k][k+1]=I.of(F(-n,factorial(k+1)))
        q=[sum((beta[k]*ip[k][l] for k in range(K+1)),zero) for l in range(K+2)]
        q[0]-=1
        # Exact integral of e^-s times a polynomial over [0,log((n+1)/n)].
        ratio=F(n,n+1);mom=[I.of(1-ratio)];pw=I.of(1)
        for j in range(1,2*K+3):
            pw*=dt;v=j*mom[-1]-ratio*pw
            if v.hi<0:raise ArithmeticError('negative moment upper endpoint')
            mom.append(I(max(0,v.lo),v.hi))
        val=sum((a*b for a,b in zip(poly_square(q),mom)),zero)/n
        if val.hi<0:raise ArithmeticError('negative cell upper endpoint')
        partial+=I(max(0,val.lo),val.hi)
        dp=[I.of(1)]
        for j in range(1,K+2):dp.append(dp[-1]*dt)
        H=[I.of(0)]+[sum((ip[k][l]*dp[l] for l in range(k+2)),zero) for k in range(1,K+1)]
        cells+=1
    # Complete tail at t=log X+s, with g(t)=t/2+c-1/2+r(t).
    tx=core.logq(F(X));g0=tx/2+c-F(1,2)
    ip=[[I.of(0) for _ in range(K+2)] for _ in range(K+1)]
    ip[0][0]=g0;ip[0][1]=I.of(F(1,2))
    for k in range(1,K+1):
        for l in range(k):ip[k][l]=H[k-l]/factorial(l)
        ip[k][k]=g0/factorial(k);ip[k][k+1]=I.of(F(1,2*factorial(k+1)))
    tailp=[sum((beta[k]*ip[k][l] for k in range(K+1)),zero) for l in range(K+2)]
    tailp[0]-=1
    rp=[I.of(0) for _ in range(K+2)]
    rp[0]=I.of(abs(beta[0])*(F(1,2)+F(1,6*X)))
    for k in range(1,K+1):rp[k-1]+=I.of(abs(beta[k])/F(3*X*factorial(k-1)))
    mean=sqnorm(tailp)/X;remainder=sqnorm(rp)/X
    tail=(sqroot(mean)+sqroot(remainder)).square()
    full=I(partial.lo, partial.hi+tail.hi)
    if full.hi >= I.of(F(13,250)).lo:
        raise ArithmeticError('full error fails the stated strict threshold')
    # From delta <= full < 13/250, J <= -log(1-delta)/2.
    jbound=-core.logq(F(237,250))/2
    if jbound.hi >= I.of(F(27,1000)).lo:
        raise ArithmeticError('entropy ceiling arithmetic fails')
    return {'scope':'one fixed exponential target; no prefix/horizon assertion',
            'target':'u(t)=exp(-t/2); squared norm exactly 1',
            'degree':K,'integer_cutoff':X,'integrated_cells':cells,
            'coefficients':[str(x) for x in COEFFICIENTS],
            'partial_error':partial.record(),'smooth_tail_squared':mean.record(),
            'remainder_tail_squared':remainder.record(),'full_tail_upper':tail.record(),
            'complete_error':full.record(),'error_upper':'13/250',
            'entropy_upper':'27/1000','entropy_log_ceiling':jbound.record(),
            'core_bits':core.BITS}
