from mpmath import mp, mpf, log as mlog, sqrt as msqrt
mp.dps=30
from g3_adv import mobius_sieve
def check(X,n,K0=40):
    mu=mobius_sieve(X); Kmax=X//n
    sgn=list(mu)
    for k in range(K0+1,Kmax+1):
        if mu[k]!=0: sgn[k]=-1   # adversarial deep signs (kernel c>0 => -1 direction)
    bad=[]
    for N in range(5,Kmax+1):
        M=sum(sgn[k]/msqrt(mpf(k)) for k in range(1,N+1) if sgn[k])
        A=sum(sgn[k]*mlog(mpf(k))/msqrt(mpf(k)) for k in range(1,N+1) if sgn[k])
        for L in (mlog(mpf(N)), mlog(mpf(N+1))):
            C=(1+L/2)*M-A/2
            if C>0: bad.append((N,float(C)))
    print(f"X={X} n={n}: adversarial assignment violates C_N<=0 at {len(bad)} of {2*(Kmax-4)} endpoints; worst={max((b for _,b in bad),default=0.0):.3e}")
check(2000,20); check(3000,25)
