"""Complete even-theta source moments and three Fourier values, in dyadic balls.

The source is 2*integral_0^infinity sum_n (4*pi^2*n^4*exp(9t/2)
 -6*pi*n^2*exp(5t/2))*exp(-pi*n^2*exp(2t)).
Every omitted theta index, real tail, cell Taylor term, and roundoff is paid.
No stored theta moment, zeta value, or zero table is consulted.
"""
from fractions import Fraction as F
from math import comb, factorial
import time
from ball_core import B, ZERO, ONE, I, Q, PI, exp, rad

DEGREE=128
CELLS=192
H=F(1,128)
THETA_MAX=10
ORDERS=tuple(range(0,17,2))
LEFT=F(1413472514173469,100000000000000)
RIGHT=F(141347251417347,10000000000000)
FOURIER=(LEFT,RIGHT,3*(LEFT+RIGHT)/2)


def exp_source_jet(c,n,b):
    """exp(b*(c+h*x)-pi*n^2*exp(2*(c+h*x))) through degree D."""
    A=PI*exp(2*c)*(n*n)
    f=[ZERO]*(DEGREE+1)
    hh=F(1)
    for j in range(1,DEGREE+1):
        hh*=2*H/j
        f[j]=-A*hh
    f[1]=f[1]+b*H
    out=[exp(B.real(b*c)-A)]
    for k in range(1,DEGREE+1):
        s=ZERO
        for j in range(1,k+1): s=s+(f[j]*out[k-j])*j
        out.append(s/k)
    return out


def primitive(progress=False):
    moments={k:ZERO for k in ORDERS}
    fourier=[ZERO for _ in FOURIER]
    skipped={k:F(0) for k in ORDERS}
    skipped_f=F(0)
    included=0; omitted=0
    start=time.monotonic()
    for cell in range(CELLS):
        c=F(2*cell+1,128)
        coeff=[ZERO]*(DEGREE+1)
        cell_skip=F(0)
        ep2lo=exp(2*(c-H))
        for n in range(1,THETA_MAX+1):
            amin=PI*ep2lo*(n*n)
            if amin.a-amin.e >=512*Q:
                # The summand is positive on the real positive axis and is
                # bounded by its positive first part throughout this cell.
                upper=4*PI*PI*(n**4)*exp(F(9,2)*(c+H)-amin)
                cell_skip+=F(upper.norm(),Q)
                omitted+=1
                continue
            u=exp_source_jet(c,n,F(9,2))
            v=exp_source_jet(c,n,F(5,2))
            p=4*PI*PI*(n**4);q=6*PI*(n*n)
            coeff=[coeff[j]+p*u[j]-q*v[j] for j in range(DEGREE+1)]
            included+=1
        # Actual real integration is [0,3]: c=(2j+1)/128, h=1/128.
        for k in ORDERS:
            poly=[F(comb(k,r))*c**(k-r)*H**r for r in range(k+1)]
            total=ZERO
            for j in range(DEGREE+1):
                w=sum((2*poly[r]/(j+r+1) for r in range(k+1) if (j+r)%2==0),F(0))
                total=total+coeff[j]*w
            moments[k]=moments[k]+2*H*total
            skipped[k]+=4*H*max(F(1),(c+H)**k)*cell_skip
        skipped_f+=4*H*cell_skip
        for ind,z in enumerate(FOURIER):
            ee=[exp(I*(z*c))]
            for k in range(1,DEGREE+1):ee.append(ee[-1]*(I*(z*H))/k)
            total=ZERO
            for k in range(0,DEGREE+1,2):
                cc=ZERO
                for j in range(k+1):cc=cc+coeff[j]*ee[k-j]
                total=total+cc*F(2,k+1)
            fourier[ind]=fourier[ind]+2*H*total
        if progress and (cell+1)%16==0:
            print('source cells',cell+1,'/',CELLS,'elapsed',round(time.monotonic()-start,1),flush=True)
    # e^3>16, pi>3, pi<4 are independently bounded by the arithmetic core.
    # Uniform |phi_partial|<2^46 in the radius-1/16 disks.
    taylor=F(2**46,8**(DEGREE+1))*F(8,7)
    taylor_f=F(2**51,8**(DEGREE+1))*F(8,7)
    # All n>=11 over [0,3]; ratio of successive positive majorants <1/2.
    ntail={k:F(768*3**k*11**4,2**484) for k in ORDERS}
    # All n and all t>=3; u=e^(2t)>256 and t^k<=exp(8t), k<=16.
    future=F(128,2**1024)*sum((F(factorial(6),factorial(6-j))*F(256**(6-j),3**(j+1)) for j in range(7)),F(0))
    errors={}
    for k in ORDERS:
        error=6*3**k*taylor+ntail[k]+future+skipped[k]
        moments[k]=moments[k].grow(rad(error))
        errors[str(k)]={'taylor':str(6*3**k*taylor),'theta_tail':str(ntail[k]),'future':str(future),'skipped':str(skipped[k])}
    for j in range(len(fourier)):
        b=fourier[j].grow(rad(6*taylor_f+ntail[0]+future+skipped_f))
        fourier[j]=B(b.a,0,b.e) # exactly the cosine integral, not its sine part
    return moments,fourier,{'degree':DEGREE,'cells':CELLS,'theta_indices':THETA_MAX,'included_terms':included,'pointwise_bounded_terms':omitted,'errors':errors}


def cumulants(mu):
    out=[ZERO]*len(mu)
    for n in range(1,len(mu)):
        s=ZERO
        for j in range(1,n):s=s+comb(n-1,j-1)*out[j]*mu[n-j]
        out[n]=mu[n]-s
    return out


def standardized(raw):
    mu=[ZERO]*17;mu[0]=ONE;mu[2]=ONE
    normal=raw[0];v=raw[2]/normal
    for r in range(2,9):
        vp=ONE
        for _ in range(r):vp=vp*v
        mu[2*r]=raw[2*r]/normal/vp
    return mu,cumulants(mu),v

if __name__=='__main__':
    import json
    raw,ff,coverage=primitive(progress=True)
    mu,kk,var=standardized(raw)
    print('variance',var)
    for n in ORDERS:print(n,raw[n],mu[n],kk[n])
    print('Fourier',ff)
    def encode(b):return [b.a,b.b,b.e]
    json.dump({'raw':{str(k):encode(v) for k,v in raw.items()},'fourier':[encode(v) for v in ff],'coverage':coverage},open('native_result.json','w'),sort_keys=True,indent=2)
