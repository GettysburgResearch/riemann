"""G3 (embedded skeptic) — pre-positioned classification theorem, machine verification.

THM G3-1 (threshold <-> Moebius dictionary). All identities EXACT (finite algebra):
 (a) tau(th) := int_th^1 t^{-1/2} C_{fl(1/t)}(log 1/t) dt = 4 m(K) - F(th,K),
     F(t,N) = sqrt(t)[(4+log(1/t)) M_N - A_N],  K=fl(1/th)  [= 4m(1/th)+B(th), H2 finite form]
     derived here independently by telescoping the exact antiderivative
     int t^{-1/2} C_N dt = F(t,N) + const, knot jump F(1/N,N-1)-F(1/N,N) = -4 mu(N)/N.
 (b) <S, 1_[k,X]> = sum_{m=k}^X m R_X(m)  =  k U_X(k) + sum_{m=k+1}^X U_X(m)      (Abel)
                  = sqrt(X) tau(k/X) - X^{-1/2} int_{k/X}^1 {tX} t^{-3/2} C dt     (sawtooth)
     with k U_X(k) = sqrt(X th) [L M_K - A_K] exact (th=k/X, L=log(1/th)).
 (c) capture split: sum_{m>=n} S(m) = sum_{p in W} Sigma(p) + Leak_n,
     Leak_n = sum_{m in F} g(m) P_m(Z_1 < n)  (G1 Lemma 2, h=1 on V; g = canonical far flow)
 (d) window-trace decomposition: for any certificate h in C_n with trace h|_W,
     <S,h> = hbar * [ <S,1_[n,X]> - Leak_n ] + sum_p (h(p)-hbar) Sigma(p).
 (e) superharmonic correction: for h = 1_[k,X] (threshold),
     <S,h> - sum_p h(p) Sigma(p) = sum_F g(m) (Lh)(m), (Lh)(m)=P_m(Z_1<k) >= 0,
     so threshold-cut one-sidedness <=> tau one-sidedness MOD the sign of g (deep occupancy).
"""
from fractions import Fraction
from mpmath import mp, mpf, log, sqrt
mp.dps = 40

def mobius_sieve(n):
    mu=[0]*(n+1); mu[1]=1; pr=[]; comp=[False]*(n+1)
    for i in range(2,n+1):
        if not comp[i]: pr.append(i); mu[i]=-1
        for p in pr:
            if i*p>n: break
            comp[i*p]=True
            if i%p==0: mu[i*p]=0; break
            mu[i*p]=-mu[i]
    return mu

def children(m): return (m//2, m-m//2, (m+2)//3, m-(m+2)//3)

def setup(X, mu=None, eps=None):
    """U,R with optional adversarial signs eps[k] replacing mu[k]."""
    if mu is None: mu=mobius_sieve(X)
    sgn = list(mu)
    if eps:
        for k,v in eps.items(): sgn[k]=v
    w=[mpf(0)]*(X+2)
    for q in range(1,X+1): w[q]=log(mpf(X)/q)/sqrt(mpf(q))
    U=[mpf(0)]*(X+2)
    for m in range(1,X+1):
        U[m]=sum(sgn[k]*w[m*k] for k in range(1,X//m+1) if sgn[k])
    R=[ (U[m]-U[m+1]) for m in range(X+1) ]  # R[m] valid m>=1
    return sgn,w,U,R

def MA(N, sgn):
    M=mpf(0); A=mpf(0); mm=mpf(0)
    for k in range(1,N+1):
        if sgn[k]:
            M+=sgn[k]/sqrt(mpf(k)); A+=sgn[k]*log(mpf(k))/sqrt(mpf(k)); mm+=mpf(sgn[k])/k
    return M,A,mm

def F_anti(t, N, sgn):
    M,A,_=MA(N,sgn)
    return sqrt(t)*((4+log(1/t))*M - A)

def tau_closed(th, sgn):
    K=int(mpf(1)/th)  # floor(1/th)
    _,_,mm=MA(K,sgn)
    return 4*mm - F_anti(th,K,sgn)

def tau_cellsum(th, sgn):
    """independent: sum over cells of F(b,N)-F(a,N)."""
    K=int(mpf(1)/th); tot=mpf(0)
    for N in range(1,K+1):
        a = max(th, mpf(1)/(N+1)); b = mpf(1)/N if N>1 else mpf(1)
        if b<=a: continue
        tot += F_anti(b,N,sgn)-F_anti(a,N,sgn)
    return tot

def saw_integral(k, X, sgn):
    """int_{k/X}^1 {tX} t^{-3/2} C dt exactly: per m-interval, split at knots.
       int t^{-1/2}C_N = F(t,N); int t^{-3/2}C_N = -t^{-1/2}[(log 1/t)M_N - A_N] =: -Ut(t,N)."""
    def Ut(t,N):
        M,A,_=MA(N,sgn); return ((log(1/t))*M - A)/sqrt(t)
    tot=mpf(0)
    for m in range(k, X):
        a=mpf(m)/X; b=mpf(m+1)/X
        Nlo=int(mpf(X)/(m+1)); Nhi=int(mpf(X)/m) if m>0 else 0
        pts=[a]+[mpf(1)/N for N in range(Nlo+1, Nhi+1) if a<mpf(1)/N<b]+[b]
        pts=sorted(set(pts))
        for i in range(len(pts)-1):
            lo,hi=pts[i],pts[i+1]
            mid=(lo+hi)/2; N=int(mpf(1)/mid)
            # int (tX-m) t^{-3/2} C = X*(F(hi,N)-F(lo,N)) - m*(-Ut(hi,N)+Ut(lo,N))
            tot += X*(F_anti(hi,N,sgn)-F_anti(lo,N,sgn)) + m*(Ut(hi,N)-Ut(lo,N))
    return tot

def flow_all(X,n,sgn,w,U,R):
    """Sigma(p) for all p via far flow g; plus g, capture, leak."""
    W0,W1=n,min(2*n,X+1)
    S=[mpf(0)]*(X+2)
    for m in range(n,X+1): S[m]=m*R[m]
    g=[mpf(0)]*(X+2)
    for m in range(X,2*n-1,-1):
        acc=S[m]
        # parents m' in F with child m: iterate children of each m'? do reverse: children of m' known; use direct approach
        g[m]=acc
    # recompute properly: g(m)=S(m)+sum_{m' in F} g(m')Q(m',m); descend from top
    g=[mpf(0)]*(X+2)
    inflow=[mpf(0)]*(X+2)
    for m in range(X,2*n-1,-1):
        g[m]=S[m]+inflow[m]
        for c in children(m):
            if c>=n: inflow[c]+=g[m]*mpf(c)/(2*m)
    Sig=[mpf(0)]*(W1)
    for p in range(W0,W1):
        Sig[p]=S[p]+inflow[p]
    leak=mpf(0)
    for m in range(2*n,X+1):
        pk=sum(mpf(c)/(2*m) for c in children(m) if c<n)
        leak+=g[m]*pk
    return Sig,g,leak,inflow

def run(X,n):
    sgn,w,U,R=setup(X)
    th=mpf(n)/X
    # (a) tau closed vs cellsum
    t1=tau_closed(th,sgn); t2=tau_cellsum(th,sgn)
    # (b) Abel vs sawtooth
    lhs=sum(m*R[m] for m in range(n,X+1))
    abel=n*U[n]+sum(U[m] for m in range(n+1,X+1))
    saw=saw_integral(n,X,sgn)
    rhs=sqrt(mpf(X))*t1 - saw/sqrt(mpf(X))
    kU=sqrt(mpf(X)*th)*((log(1/th))*MA(int(1/th),sgn)[0]-MA(int(1/th),sgn)[1])
    # careful: kU formula needs K=floor(X/n) for U_X(n): U uses k<=X/m i.e. K'=X//n
    Kp=X//n
    M,A,_=MA(Kp,sgn)
    kU2=n*U[n]; kU3=sqrt(mpf(X)*th)*((log(1/th))*M-A)  # may differ if floor(1/th)!=X//n
    # (c,d,e)
    Sig,g,leak,_=flow_all(X,n,sgn,w,U,R)
    W=range(n,min(2*n,X+1))
    aggr=sum(Sig[p] for p in W)
    capture_id = lhs - (aggr+leak)
    gmin=min(g[m] for m in range(2*n,X+1))
    print(f"X={X} n={n}: |tau_closed-tau_cellsum|={float(abs(t1-t2)):.1e}  "
          f"|Abel-lhs|={float(abs(abel-lhs)):.1e}  |saw_id|={float(abs(lhs-rhs)):.1e}  "
          f"|kU_closed-nU(n)|={float(abs(kU3-kU2)):.1e}")
    print(f"   sqrtX*tau={float(sqrt(mpf(X))*t1):+.6f}  mass_above_n={float(lhs):+.6f}  "
          f"aggr_Sigma={float(aggr):+.6f}  Leak={float(leak):+.6f}  |capture_id|={float(abs(capture_id)):.1e}  "
          f"min g on F={float(gmin):+.3e}")
    return t1,lhs,aggr,leak

if __name__=="__main__":
    for (X,n) in [(300,12),(1000,20),(2000,20),(2000,63),(3000,100)]:
        run(X,n)
