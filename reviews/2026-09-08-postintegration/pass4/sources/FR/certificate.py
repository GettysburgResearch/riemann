"""Bounded actual-source certificate. All acceptance uses rational/dyadic arithmetic.
interval_core is injected only after byte authentication by check.py.
"""
from fractions import Fraction as F
from math import comb, factorial, isqrt

COEFFS = tuple(F(x,10000) for x in (4284,-1839,-1199,-742,-371))

def gram_floor(k):
    if type(k) is not int or k < 0: raise ValueError('nonnegative integer rank index')
    m=isqrt(k+4)
    if m*m<k+4:m+=1
    return F(1,(k+1)**2 * 2**(13*m))

def full_certificate(core, X=2048, coeffs=COEFFS):
    if type(X) is not int or X!=2048:raise ValueError('frozen source cutoff 2048')
    if type(coeffs) is not tuple or coeffs!=COEFFS:raise ValueError('frozen rational coefficients')
    I=core.I; S=core.SCALE
    K=len(coeffs)-1;zero=I.of(0)
    def power(x,n):
        out=I.of(1)
        for _ in range(n):out=out*x
        return out
    def sqrt_i(x):
        if x.hi<0:raise ValueError('negative squared norm')
        low=isqrt(max(0,x.lo)*S); high=isqrt(x.hi*S)
        if high*high<x.hi*S:high+=1
        return I(low,high)
    def poly_square(p):
        out=[I.of(0) for _ in range(2*len(p)-1)]
        for i,a in enumerate(p):
            for j,b in enumerate(p):out[i+j]+=a*b
        return out
    def norm_poly(p):
        val=sum((a*factorial(i) for i,a in enumerate(poly_square(p))),zero)
        return I(max(0,val.lo),val.hi)
    def atan(x):
        out=I.of(0)
        for j in range(64):out+=I.of((-1)**j*x**(2*j+1)/F(2*j+1))
        nxt=x**129/F(129)
        return out+I.bounds(0,nxt)
    pi=16*atan(F(1,5))-4*atan(F(1,239))
    lowlog=core.logq(F(2*pi.lo,S));hilog=core.logq(F(2*pi.hi,S))
    c=I(lowlog.lo,hilog.hi)/2
    l2=core.logq(F(2)); root2=core.sqrt2()
    logs=[I.of(0)]+[core.logq(F(i)) for i in range(1,2*X+1)]
    lf=[I.of(0)]
    for i in range(1,2*X+1):lf.append(lf[-1]+logs[i])
    H=[I.of(0) for _ in range(K+1)]
    old=I.of(0); partial=I.of(0); cells=0
    # At each cell t=log(x0)+s, g(t)=g0-n*s.
    for m in range(2,2*X):
        n=m//2;x0=F(m,2);x1=F(m+1,2)
        t0=core.logq(x0);dt=core.logq(x1/x0)
        g0=n*(1-t0)+lf[n]
        ip=[]
        p=[I.of(0)for _ in range(K+2)];p[0]=g0;p[1]=I.of(-n);ip.append(p)
        for k in range(1,K+1):
            p=[I.of(0)for _ in range(K+2)]
            for l in range(k):p[l]=H[k-l]/factorial(l)
            p[k]=g0/factorial(k);p[k+1]=I.of(F(-n,factorial(k+1)));ip.append(p)
        q=[I.of(0)for _ in range(K+2)]
        A0=(m-2*n-1)*t0+(m-1)*l2-lf[m]+2*lf[n]
        q[0]=A0/root2;q[1]=I.of(m-2*n-1)/root2
        for j,a in enumerate(coeffs):
            for k in range(j+1):
                w=a*((-1)**k)*comb(j,k)
                for l in range(K+2):q[l]+=w*ip[k][l]
        # Exact incomplete-gamma recurrence. exp(-dt)=x0/x1 is rational.
        ratio=x0/x1;mom=[I.of(1-ratio)];dp=I.of(1)
        for j in range(1,2*K+3):
            dp*=dt;v=j*mom[-1]-dp*ratio
            mom.append(I(max(0,v.lo),v.hi))
        sq=poly_square(q)
        v=sum((a*b for a,b in zip(sq,mom)),zero)/x0
        if v.hi<0:raise ValueError('negative cell upper integral')
        partial+=I(max(0,v.lo),v.hi)
        old+=core.log_square_integral(I.of(m-2*n-1), (m-1)*l2-lf[m]+2*lf[n],x0,x1)/2
        Hn=[I.of(0)for _ in range(K+1)]
        for k in range(1,K+1):
            Hn[k]=sum((ip[k][l]*power(dt,l) for l in range(k+2)),zero)
        H=Hn;cells+=1
    # Infinite tail: exact smooth polynomial plus a bounded oscillatory primitive.
    t=core.logq(F(X));m0=t/2+c-F(1,2)
    HP=[]
    for k in range(K+1):
        p=[I.of(0)for _ in range(K+2)]
        if k==0:p[0]=m0;p[1]=I.of(F(1,2))
        else:
            for l in range(k):p[l]=H[k-l]/factorial(l)
            p[k]=m0/factorial(k);p[k+1]=I.of(F(1,2*factorial(k+1)))
        HP.append(p)
    tailp=[I.of(0)for _ in range(K+2)]
    tailp[0]=(-t/2+c-F(3,2)*l2)/root2;tailp[1]=-I.of(F(1,2))/root2
    for j,a in enumerate(coeffs):
        for k in range(j+1):
            for l in range(K+2):tailp[l]+=a*((-1)**k)*comb(j,k)*HP[k][l]
    rp=[I.of(0)for _ in range(K+2)]
    rp[0]=I.of(abs(sum(coeffs))*(F(1,2)+F(1,6*X)))+I.of(F(5,12*X))/root2
    for j,a in enumerate(coeffs):
        for k in range(1,j+1):rp[k-1]+=abs(a)*F(comb(j,k),3*X*factorial(k-1))
    mean=norm_poly(tailp)/X;remainder=norm_poly(rp)/X
    tail=(sqrt_i(mean)+sqrt_i(remainder)).square()
    full=I(partial.lo,partial.hi+tail.hi)
    if old.lo<=I.of(F(3,10)).hi:raise ValueError('seed lower failed')
    if full.hi>=I.of(F(1,1200)).lo:raise ValueError('ideal error threshold failed')
    # Native compact L2 input: box width 2^-40, then cut the stable filter at 128.
    smoothing_sq=F(410,2**40) # log(2)<1, l1(coeffs)<1.
    stable_tail=F(156*134**3,2**64) # e>2, ||d||_1<=6.
    if smoothing_sq>=F(1,10**8) or stable_tail>=F(1,10**8):raise ValueError('compact-input error costs')
    if (F(29,1000)+F(1,5000))**2>=F(1,1000):raise ValueError('compact final rational threshold')
    return {'cutoff_x':X,'source_degree':K,'half_cells':cells,
            'coefficients':[str(x)for x in coeffs],
            'seed_error_lower':old.record(),'corrected_error_partial':partial.record(),
            'tail_smooth_norm_squared':mean.record(),'tail_remainder_norm_squared':remainder.record(),
            'complete_tail_upper':tail.record(),'ideal_full_error':full.record(),
            'box_width':'1/1099511627776','compact_input_end':128,
            'box_output_error_squared_upper':str(smoothing_sq),
            'input_truncation_output_norm_upper':str(stable_tail),
            'compact_full_error_upper':'1/1000','seed_to_compact_improvement_factor_lower':300,
            'pi':pi.record(),'half_log_two_pi':c.record()}
