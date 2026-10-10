"""G2 — counting interpretation of GFEP.
Exact identity verification at X=100, 1000 (mpmath 50dps for w; Fractions for E/G).

Identities under test:
 I5a (inversion):      sum_{k<=X/m} U(mk) = w(m)  for all m<=X
 I5b (mass):           sum_{m<=X} U(m) = w(1) = log X ; sum_{m=1}^X m R(m) = log X
 I5c (log-moment):     sum_{m<=X} U(m) log m = sum_{q<=X} Lambda(q) w(q)   [prime ramp]
 I5d (Id-moment):      sum_{m<=X} m U(m) = sum_{q<=X} phi(q) w(q)
 I1  (G-harmonic):     G(M):=M*E_n(M,p) satisfies G(M) = (1/2) sum_children G(c) for M>=2n
                       (children below n contribute 0), G = p*delta on band.
 I2  (Abel form):      Sigma(p) = sum_{m=n}^X U(m) dG(m),  dG(m)=G(m)-G(m-1), G(n-1):=0
                       and Sigma(p) = p R(p) + sum_{m>=2n} U(m) dG(m)
 I3  (doubling defect):G(2m) - G(m) = (1/2)[G(ceil(2m/3)) + G(floor(4m/3))]  for m>=n
 I4  (convexity pair): D_j(m) := w(mj)-w((m+1)j) satisfies D_j(m) > D_{2j}(m) when (2m+2)j<=X
 IF  (2-adic fold):    Sigma(p) = sum_{j odd sf} mu(j) * [ sum_{m>=n,2mj<=X} w(2mj)(dG(2m)-dG(m))
                         + sum_{M>=n odd, Mj<=X} w(Mj) dG(M)
                         + sum_{M even in [n,2n), Mj<=X} w(Mj) dG(M) ]
Measurements:
 M1: signs of dG(m) for m>2n ("is dG a positive measure above the band?")
 M2: signs of dG(2m)-dG(m) (cross-pair kernel)
 M3: G(2m)-2G(m) sign and ratio G(2m)/(2G(m)) (superadditivity / razor's edge)
 M4: R-form pair dominance: s_j(m) = D_j(2m)G(2m) - D_{2j}(m)G(m) sign stats
"""
import sys
from fractions import Fraction
from mpmath import mp, mpf, log, sqrt

mp.dps = 50

def mobius_sieve(n):
    mu = [0]*(n+1); mu[1] = 1
    primes = []; comp = [False]*(n+1)
    for i in range(2, n+1):
        if not comp[i]:
            primes.append(i); mu[i] = -1
        for p in primes:
            if i*p > n: break
            comp[i*p] = True
            if i % p == 0:
                mu[i*p] = 0; break
            mu[i*p] = -mu[i]
    return mu

def lambda_phi(n):
    lam = [mpf(0)]*(n+1); phi = list(range(n+1))
    spf = [0]*(n+1)
    for i in range(2, n+1):
        if spf[i]==0:
            for j in range(i, n+1, i):
                if spf[j]==0: spf[j]=i
    for q in range(2, n+1):
        p = spf[q]; m = q
        a = 0
        while m % p == 0: m//=p; a+=1
        if m == 1: lam[q] = log(p)
    for i in range(2, n+1):
        if spf[i]==i:
            for j in range(i, n+1, i):
                phi[j] -= phi[j]//i
    return lam, phi

def children(m):
    return (m//2, m - m//2, (m+2)//3, m - (m+2)//3)

def run(X, n, plist=None, verbose=True):
    mu = mobius_sieve(X)
    w = [mpf(0)]*(X+2)
    for q in range(1, X+1):
        w[q] = log(mpf(X)/q)/sqrt(mpf(q))
    U = [mpf(0)]*(X+2)
    for m in range(1, X+1):
        s = mpf(0)
        for k in range(1, X//m+1):
            if mu[k]: s += mu[k]*w[m*k]
        U[m] = s
    R = [U[m]-U[m+1] for m in range(0, X+1)]  # R[m], R[0] junk

    # ---- I5a inversion
    err5a = mpf(0)
    for m in range(1, X+1):
        s = mpf(0)
        for k in range(1, X//m+1): s += U[m*k]
        err5a = max(err5a, abs(s - w[m]))
    # ---- I5b masses
    sU = sum(U[1:X+1]); smR = sum(m*R[m] for m in range(1,X+1))
    err5b = max(abs(sU - w[1]), abs(smR - w[1]))
    # ---- I5c, I5d moments
    lam, phi = lambda_phi(X)
    err5c = abs(sum(U[m]*log(m) for m in range(1,X+1)) - sum(lam[q]*w[q] for q in range(1,X+1)))
    err5d = abs(sum(m*U[m] for m in range(1,X+1)) - sum(phi[q]*w[q] for q in range(1,X+1)))

    band = list(range(n, min(2*n, X+1)))
    if plist is None: plist = band
    results = {}
    for p in plist:
        # exact E via Fractions, upward
        E = [Fraction(0)]*(X+1)
        for M in band: E[M] = Fraction(1 if M==p else 0)
        for M in range(2*n, X+1):
            s = Fraction(0)
            for c in children(M):
                if c >= n: s += Fraction(c, 2*M)*E[c]
            E[M] = s
        G = [Fraction(0)]*(X+2)
        for M in range(n, X+1): G[M] = M*E[M]
        # I1 harmonicity
        bad1 = 0
        for M in range(2*n, X+1):
            s = sum(G[c] if c>=n else Fraction(0) for c in children(M))
            if G[M]*2 != s: bad1 += 1
        # I3 doubling defect
        bad3 = 0
        for m in range(n, X//2+1):
            lhs = G[2*m]-G[m]
            rhs = Fraction(1,2)*( (G[(2*m+2)//3] if (2*m+2)//3>=n else Fraction(0))
                                 +(G[2*m-(2*m+2)//3] if 2*m-(2*m+2)//3>=n else Fraction(0)))
            if lhs != rhs: bad3 += 1
        # Sigma direct
        Sig = sum(m*R[m]*mpf(E[m].numerator)/mpf(E[m].denominator) for m in range(n, X+1))
        # I2 Abel
        dG = {}
        for m in range(n, X+1):
            gm1 = G[m-1] if m-1>=n else Fraction(0)
            dG[m] = G[m]-gm1
        SigA = sum(U[m]*mpf(dG[m].numerator)/mpf(dG[m].denominator) for m in range(n, X+1))
        far = sum(U[m]*mpf(dG[m].numerator)/mpf(dG[m].denominator) for m in range(2*n, X+1))
        SigB = p*R[p] + far
        err2 = max(abs(Sig-SigA), abs(Sig-SigB))
        # IF fold
        fold = mpf(0)
        for j in range(1, X+1, 2):
            if mu[j]==0: continue
            t = mpf(0)
            for m in range(n, X//(2*j)+1):
                d = dG[2*m]-dG[m]
                t += w[2*m*j]*mpf(d.numerator)/mpf(d.denominator)
            M0 = n if n%2==1 else n+1
            for M in range(M0, X//j+1, 2):
                t += w[M*j]*mpf(dG[M].numerator)/mpf(dG[M].denominator)
            for M in range(n, min(2*n, X+1)):
                if M%2==0 and M//2 < n and M*j<=X:
                    t += w[M*j]*mpf(dG[M].numerator)/mpf(dG[M].denominator)
            fold += mu[j]*t
        errF = abs(fold - Sig)
        # M1, M2, M3
        neg_dG = [m for m in range(2*n, X+1) if dG[m] < 0]
        neg_cross = [m for m in range(n, X//2+1) if dG[2*m]-dG[m] < 0]
        supadd = [m for m in range(n, X//2+1) if G[m]>0 and G[2*m] < 2*G[m]]
        ratios = [float(Fraction(G[2*m], 2*G[m])) for m in range(n, X//2+1) if G[m]>0]
        # M4 R-form pair dominance
        dom_bad = 0; dom_tot = 0
        for m in range(n, X+1):
            for j in range(1, X//(2*m)+1, 2):
                if mu[j]==0: continue
                if (2*m+2)*j > X: continue
                Dj2m = w[2*m*j]-w[(2*m+1)*j]
                D2jm = w[2*m*j]-w[(2*m+2)*j] if (m+1)*2*j<=X else None
                if D2jm is None: continue
                s = Dj2m*mpf((G[2*m]).numerator)/mpf((G[2*m]).denominator) - D2jm*mpf(G[m].numerator)/mpf(G[m].denominator)
                dom_tot += 1
                if s < 0: dom_bad += 1
        results[p] = dict(Sig=Sig, err2=err2, errF=errF, bad1=bad1, bad3=bad3,
                          neg_dG=len(neg_dG), neg_dG_ex=neg_dG[:8],
                          neg_cross=len(neg_cross), neg_cross_ex=neg_cross[:8],
                          supadd_viol=len(supadd), rat_min=min(ratios) if ratios else None,
                          rat_max=max(ratios) if ratios else None,
                          dom_bad=dom_bad, dom_tot=dom_tot)
    print(f"X={X} n={n}: I5a={float(err5a):.2e} I5b={float(err5b):.2e} I5c={float(err5c):.2e} I5d={float(err5d):.2e}")
    for p, r in results.items():
        print(f"  p={p}: Sigma={float(r['Sig']):+.6e}  I2err={float(r['err2']):.2e} folderr={float(r['errF']):.2e} "
              f"harmviol={r['bad1']} dblviol={r['bad3']}")
        print(f"        dG<0 above 2n: {r['neg_dG']} (ex {r['neg_dG_ex']}); cross dG(2m)<dG(m): {r['neg_cross']} (ex {r['neg_cross_ex']})")
        print(f"        G(2m)<2G(m): {r['supadd_viol']} pairs; G(2m)/2G(m) in [{r['rat_min']:.4f},{r['rat_max']:.4f}]"
              if r['rat_min'] is not None else "        no ratios")
        print(f"        R-form pair dominance fails {r['dom_bad']}/{r['dom_tot']}")
    return results

if __name__ == "__main__":
    run(100, 8)
    run(100, 6, plist=[6,7,11])
