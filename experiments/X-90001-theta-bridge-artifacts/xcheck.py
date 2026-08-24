"""Cross-examiner independent check (fresh code, not copied from validators).

1) Independent implementation of the dyadic-difference decomposition
   T^s(z) = Phi_s(z) + Ecal_s(z)  at X = 2e4 and 2e5 (larger than D1 tested),
   with d_s(p)=s_X(p) identity check, kernel constants PER DYADIC BAND
   (log-drift test for the log^3-vs-log^4 adjudication), moat profile,
   and B_X.
2) Reconciliation D0 <-> D1 at X = 1e4: max|Phi^s_D0 - Phi_s_D1| (regrouping
   size), equality of the two reconstructions, edge values at z=X.
"""
import numpy as np, math, time, sys

def sieve(X):
    s = np.ones(X + 1, bool); s[:2] = False
    for i in range(2, int(X**0.5) + 1):
        if s[i]: s[i*i::i] = False
    return np.nonzero(s)[0]

def run(X):
    t0 = time.time()
    Y = X // 2
    logX, logY = math.log(X), math.log(Y)
    L = logX - logY
    dlt = Y**-0.5 - X**-0.5
    sqX, sqY = math.sqrt(X), math.sqrt(Y)
    primes = sieve(X); lp = np.log(primes.astype(float))
    th = np.zeros(X + 2); th[primes] = lp; th = np.cumsum(th)  # th[n]=theta(n)

    # ---- seeds (my own code) ----
    def bX(m):
        m = np.asarray(m, float)
        r = 2*np.sqrt(m)*(logX - np.log(m)) - 4*np.sqrt(m) + 4*m/sqX
        return np.where((m >= 2) & (m <= X), r, 0.0)
    def bY(m):
        m = np.asarray(m, float)
        r = 2*np.sqrt(m)*(logY - np.log(m)) - 4*np.sqrt(m) + 4*m/sqY
        return np.where((m >= 2) & (m <= Y), r, 0.0)
    def cfun(m):
        m = np.asarray(m, float)
        lo = 2*np.sqrt(m)*L - 4*m*dlt
        hi = 2*np.sqrt(m)*(logX - np.log(m)) - 4*np.sqrt(m) + 4*m/sqX
        return np.where(m <= Y, lo, np.where(m <= X, hi, 0.0))
    def om(t):
        t = np.asarray(t, float)
        return np.where(t <= Y, t**-0.5*L, t**-0.5*(logX - np.log(t)))
    # antiderivatives (derived by hand, checked below by quadrature)
    def AB(s):
        s = np.asarray(s, float)
        return (4/3)*s**1.5*(logX - np.log(s)) - (16/9)*s**1.5 + 2*s*s/sqX
    ABY = float(AB(float(Y)))
    ACY = (4/3)*Y**1.5*L - 2.0*Y*Y*dlt
    def AC(u):
        u = np.minimum(np.asarray(u, float), float(X))
        lo = (4/3)*u**1.5*L - 2.0*u*u*dlt
        return np.where(u <= Y, lo, AB(u) - ABY + ACY)
    def AW(t):
        t = np.asarray(t, float)
        return 2*np.sqrt(t)*(logX - np.log(t)) + 4*np.sqrt(t)
    AWY = float(AW(float(Y))); AOMY = 2*sqY*L
    def AOm(t):
        t = np.asarray(t, float)
        return np.where(t <= Y, 2*np.sqrt(t)*L, AW(t) - AWY + AOMY)
    # sanity of antiderivatives by midpoint quadrature on random cells
    rng = np.random.default_rng(1)
    for _ in range(4):
        a = rng.uniform(3, X - 2); b = a + rng.uniform(0.5, 2.0)
        g = np.linspace(a, b, 20001)
        q = np.trapezoid(cfun(g), g)
        assert abs(q - (AC(b) - AC(a))) < 1e-6*max(1, abs(q)), "AC wrong"
        q2 = np.trapezoid(om(g), g)
        assert abs(q2 - (AOm(b) - AOm(a))) < 1e-8*max(1, abs(q2)), "AOm wrong"

    # ---- raw prime data ----
    def vsum(p, Z, f):
        k = np.arange(1, Z//p + 1); a = (k*p).astype(float)
        return float(np.sum(f(a) - f(a + 1)))
    vX = np.array([vsum(int(p), X, bX) for p in primes])
    rX = vX - primes.astype(float)**-0.5*(logX - np.log(primes.astype(float)))
    pY = primes[primes <= Y]
    vYv = np.array([vsum(int(p), Y, bY) for p in pY])
    rY = vYv - pY.astype(float)**-0.5*(logY - np.log(pY.astype(float)))
    sX = rX.copy(); sX[:len(pY)] -= rY
    contrib = np.zeros(X + 2); contrib[primes] = lp*sX
    Ts = np.cumsum(contrib[::-1])[::-1]          # Ts[z] = T^s(z)
    BX = max(0.0, Ts[2:X+1].max()); npos = int((Ts[2:X+1] > 1e-9).sum())

    # ---- kernel d_s at integers + cell integrals J ----
    d = np.zeros(X + 2); J = np.zeros(X + 1)
    for n in range(2, X + 1):
        k = np.arange(1, X//n + 1); a = (k*n).astype(float)
        d[n] = np.sum(cfun(a) - cfun(a + 1)) - float(om(float(n)))
        if n < X:
            J[n] = float(np.sum(((AC(a + 1) - AC(a)) - (AC(a + k + 1) - AC(a + k)))/k)) \
                   - float(AOm(float(n + 1)) - AOm(float(n)))
    dp_err = np.max(np.abs(d[primes] - sX))     # d_s(p) == s_X(p)?

    # ---- Phi_s closed form ----
    Phi = np.zeros(X + 1)
    AOX = float(AOm(float(X)))
    for z in range(2, X + 1):
        k = np.arange(1, X//z + 1); a = (k*z).astype(float)
        Phi[z] = float(np.sum((AC(a + 1) - AC(a))/k)) - (AOX - float(AOm(float(z))))
    # ---- Ecal via exact unit-cell quadrature: P_n = int_n^{n+1} E d' dt ----
    n = np.arange(2, X)
    P = th[n]*(d[n+1] - d[n]) - ((n+1)*d[n+1] - n*d[n]) + J[n]
    IE = np.zeros(X + 2); IE[2:X] = np.cumsum(P[::-1])[::-1]
    z = np.arange(2, X + 1)
    Ecal = -(th[z-1] - z)*d[z] - IE[z]
    err = np.max(np.abs(Ts[2:X+1] - Phi[2:X+1] - Ecal))
    scale = np.max(np.abs(Ts[2:X+1]))

    # ---- diagnostics ----
    l2 = math.log(2*X)
    maxPhi = Phi[2:X+1].max(); argmaxPhi = int(z[Phi[2:X+1].argmax()])
    maxPhi_int = Phi[2:X].max()                   # excluding z=X
    minPhi = Phi[2:X+1].min(); argminPhi = int(z[Phi[2:X+1].argmin()])
    supE = np.abs(Ecal).max()
    print(f"X={X}  [{time.time()-t0:.0f}s]  #primes={len(primes)}")
    print(f"  d_s(p)=s_X(p): max err = {dp_err:.2e}")
    print(f"  EXACTNESS max|T^s-(Phi_s+Ecal_s)| = {err:.2e}  (scale {scale:.3g}, rel {err/scale:.1e})")
    print(f"  B_X = {BX:.6g}   #z with T^s>1e-9: {npos}   T^s(X)={Ts[X]:.2e}  d_s(X)={d[X]:.2e}")
    print(f"  moat: max_z Phi_s = {maxPhi:.6g} (z={argmaxPhi}); max over z<X = {maxPhi_int:.6g}; "
          f"min = {minPhi:.4f} at z={argminPhi} (= {argminPhi/X:.3f}X); min/sqrtX = {minPhi/sqX:.5f}")
    for x in (0.05, 0.2, 0.7):
        zz = int(x*X)
        print(f"    x={x}: Phi_s/sqX = {Phi[zz]/sqX:+.5f}   T^s/sqX = {Ts[zz]/sqX:+.5f}")
    print(f"  sup|Ecal_s| = {supE:.4f}   /log^2(2X) = {supE/l2**2:.4f}")
    tgrid = np.arange(2, X + 1, dtype=float)
    k1 = np.sqrt(tgrid)*np.abs(d[2:X+1]); k2 = (tgrid[:-1]**1.5)*np.abs(np.diff(d[2:X+1]))
    print(f"  kernel: sup sqrt(t)|d_s| = {k1.max():.4f} (t={int(tgrid[k1.argmax()])})   "
          f"sup t^1.5|Dd_s| = {k2.max():.4f} (t={int(tgrid[k2.argmax()])})")
    print("  bands [2^j,2^j+1): sqrt(t)|d|max / t^1.5|Dd|max:")
    out = []
    j = 1
    while 2**j < X:
        lo, hi = 2**j, min(2**(j+1), X)
        m = (tgrid >= lo) & (tgrid < hi)
        if m.sum() > 2:
            m2 = m[:-1]
            out.append(f"2^{j}:{k1[m].max():.3f}/{k2[m2].max():.3f}")
        j += 1
    print("   ", "  ".join(out))
    return dict(Phi=Phi, Ecal=Ecal, Ts=Ts, d=d)

if __name__ == "__main__":
    Xs = [int(a) for a in sys.argv[1:]] or [20000]
    for X in Xs:
        R = run(X)
        if X == 10000:   # reconciliation with D0's validator
            sys.path.insert(0, "/tmp/claude-0/-home-user-riemann/d379fac9-baa2-5637-b561-9823a1c28acc/scratchpad")
            import validator as v0
            SX = v0.build(X); SY = v0.build(X//2)
            zz = np.arange(2, X + 1)
            PhiS0 = SX['Phi'] - np.where(zz <= X//2, SY['Phi'][np.minimum(zz, X//2) - 2], 0.0)
            FS0 = SX['F'] - np.where(zz <= X//2, SY['F'][np.minimum(zz, X//2) - 2], 0.0)
            Phi1 = R['Phi'][2:X+1]; E1 = R['Ecal']
            rec = np.max(np.abs((PhiS0 + FS0) - (Phi1 + E1)))
            reg = PhiS0 - Phi1
            print(f"  RECONCILE: max|(Phi0+F0)-(Phi1+E1)| = {rec:.2e}   "
                  f"max|Phi0^s-Phi1_s| = {np.abs(reg).max():.4f} (regroup size)")
            print(f"    check regroup == E1-F0: {np.max(np.abs(reg - (E1 - FS0))):.2e}")
            print(f"    at z=X: Phi0={PhiS0[-1]:.4f} F0={FS0[-1]:.4f}  |  Phi1={Phi1[-1]:.4f} E1={E1[-1]:.4f}")
            print(f"    at z=2: Phi0={PhiS0[0]:.4f} F0={FS0[0]:.4f}  |  Phi1={Phi1[0]:.4f} E1={E1[0]:.4f}")
