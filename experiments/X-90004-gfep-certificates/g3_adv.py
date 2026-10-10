"""G3 trap (a): Ingham-adversarial deep signs vs GFEP feasibility, per exit (trap b).

Model: Sigma_{X,n}(p) = sum_{k sf} sgn(k) c_{p,k},  c_{p,k} = sum_{m>=n, mk<=X} dG_p(m) w(mk),
dG_p = increments of the harmonic G-table of exit p (exact Fractions).
Adversary classes (deep k > K0=40; true mu fixed for k<=40 => all certified constraints hold):
  FREE : eps_k in [-1,1] (any termwise/injection/flow argument monotone in these survives class)
  PATT : additionally the Landau bottom pattern C_N(L)<=0 for all N in [5,Kmax], both cell endpoints
         (RH-hard hypothesis, T-90003 par.3)
Outputs per exit p: true Sigma, known part (k<=K0), FREE min, PATT min (LP), binding checks.
Exact recheck: worst FREE vertex assignment re-evaluated through the INDEPENDENT
first-entrance flow recursion (mpmath dps 40) — two disjoint code paths must agree.
"""
import numpy as np
from fractions import Fraction
from mpmath import mp, mpf, log as mlog, sqrt as msqrt
mp.dps = 40
K0 = 40

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

def Gtab(X,n,p):
    G=[Fraction(0)]*(X+2)
    G[p]=Fraction(p)
    for M in range(2*n,X+1):
        s=Fraction(0)
        for c in children(M):
            if c>=n: s+=G[c]
        G[M]=s/2
    return G

def coeffs(X,n,p,w):
    """c_{p,k} for all k<=X//n (float64 from exact Fractions x mp w)."""
    G=Gtab(X,n,p)
    dG={}
    for m in range(n,X+1):
        d=G[m]-(G[m-1] if m-1>=n else Fraction(0))
        if d: dG[m]=float(d)
    Kmax=X//n
    c=np.zeros(Kmax+1)
    for m,d in dG.items():
        for k in range(1,X//m+1):
            c[k]+= d*float(w[m*k])
    return c

def flow_sigma_exact(X,n,sgn):
    """independent path: first-entrance far flow with sign vector sgn (mpmath)."""
    w=[mpf(0)]*(X+2)
    for q in range(1,X+1): w[q]=mlog(mpf(X)/q)/msqrt(mpf(q))
    U=[mpf(0)]*(X+2)
    for m in range(1,X+1):
        U[m]=sum(sgn[k]*w[m*k] for k in range(1,X//m+1) if sgn[k])
    S=[mpf(0)]*(X+2)
    for m in range(n,X+1): S[m]=m*(U[m]-U[m+1])
    g=[mpf(0)]*(X+2); infl=[mpf(0)]*(X+2)
    for m in range(X,2*n-1,-1):
        g[m]=S[m]+infl[m]
        for cch in children(m):
            if cch>=n: infl[cch]+=g[m]*mpf(cch)/(2*m)
    return {p:S[p]+infl[p] for p in range(n,min(2*n,X+1))}

def run(X,n,do_patt=True):
    mu=mobius_sieve(X)
    w=[mpf(0)]*(X+2)
    for q in range(1,X+1): w[q]=mlog(mpf(X)/q)/msqrt(mpf(q))
    Kmax=X//n
    sf=[k for k in range(1,Kmax+1) if mu[k]!=0]
    deep=[k for k in sf if k>K0]
    W=list(range(n,min(2*n,X+1)))
    print(f"== X={X} n={n} Kmax={Kmax} |deep sf|={len(deep)} window={W[0]}..{W[-1]}")
    C={p:coeffs(X,n,p,w) for p in W}
    # constraints for PATT: C_N(L) = sum_k sgn_k [(1+L/2)-log(k)/2]/sqrt(k) <= 0, N in [5,Kmax], L in {log N, log(N+1)}
    if do_patt:
        rows=[]; rhs=[]
        for N in range(5,Kmax+1):
            for L in (np.log(N), np.log(N+1)):
                a=np.zeros(len(deep)); const=0.0
                for k in range(1,N+1):
                    if mu[k]==0: continue
                    coef=((1+L/2)-np.log(k)/2)/np.sqrt(k)
                    if k<=K0: const+=mu[k]*coef
                    else: a[deep.index(k)]=coef
                rows.append(a); rhs.append(-const)
        A_ub=np.array(rows); b_ub=np.array(rhs)
    from scipy.optimize import linprog
    results={}
    for p in W:
        c=C[p]
        known=sum(mu[k]*c[k] for k in sf if k<=K0)
        true=sum(mu[k]*c[k] for k in sf)
        dvec=np.array([c[k] for k in deep])
        free_min=known-np.abs(dvec).sum()
        patt_min=None
        if do_patt and len(deep)>0:
            res=linprog(dvec, A_ub=A_ub, b_ub=b_ub, bounds=[(-1,1)]*len(deep), method='highs')
            patt_min=known+res.fun if res.status==0 else float('nan')
        results[p]=(true,known,free_min,patt_min,dvec)
    # summary
    worst_true=min(results[p][0] for p in W); wt=[p for p in W if results[p][0]==worst_true][0]
    worst_free=min(results[p][2] for p in W); wf=[p for p in W if results[p][2]==worst_free][0]
    print(f"   true min_p Sigma = {worst_true:+.6f} at p={wt}")
    print(f"   FREE adversarial min_p = {worst_free:+.6f} at p={wf}  (negative => refutation in class)")
    if do_patt:
        worst_patt=min(results[p][3] for p in W); wp=[p for p in W if results[p][3]==worst_patt][0]
        print(f"   PATT adversarial min_p = {worst_patt:+.6f} at p={wp}")
    # per-exit table (compact)
    line1="   p:      "+" ".join(f"{p:7d}" for p in W[:12])
    line2="   true:   "+" ".join(f"{results[p][0]:+7.3f}" for p in W[:12])
    line3="   free:   "+" ".join(f"{results[p][2]:+7.3f}" for p in W[:12])
    print(line1); print(line2); print(line3)
    if do_patt:
        print("   patt:   "+" ".join(f"{results[p][3]:+7.3f}" for p in W[:12]))
    # exact recheck of FREE worst vertex at exit wf via independent flow path
    sgn=list(mu)
    for j,k in enumerate(deep):
        ck=results[wf][4][j]
        sgn[k]=-1 if ck>0 else (1 if ck<0 else mu[k])
    Sig=flow_sigma_exact(X,n,sgn)
    print(f"   exact recheck (flow path, dps40): Sigma_adv({wf}) = {float(Sig[wf]):+.8f} "
          f"(LP said {worst_free:+.8f}); min over W = {float(min(Sig.values())):+.8f}")
    return results

if __name__=="__main__":
    run(2000,40)      # Kmax=50, shallow-deep
    run(2000,20)      # Kmax=100
    run(3000,25)      # Kmax=120
