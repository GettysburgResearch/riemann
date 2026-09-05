"""Deriver-2 validator: dyadic-difference decomposition of the WSTS charge (T-27501 objects).

Objects (integer X, Y=floor(X/2)):
  b_X(m)=2 sqrt(m)(log(X/m)-2(1-sqrt(m/X))) on [2,X], 0 outside;  b_X(X)=0, b_X'(X)=0.
  v_p(b)=sum_{k<=X/p}[b(kp)-b(kp+1)];  w_X(p)=p^{-1/2}log(X/p);  r_X=v-w;
  s_X(p)=r_X(p)-1_{p<=Y} r_Y(p);  T_X(z)=sum_{z<=p<=X}(log p) r_X(p);
  T^s(z)=sum_{z<=p<=X}(log p) s_X(p);  B_X=max_z [T^s(z)]_+.

Derived exact decomposition (this session), for any C^0-piecewise-C^1 pair (seed a, ramp v)
with a==0 on [X,inf), a(X)=0, v(X)=0:
  frak d(t) = sum_{k<=X/t}[a(kt)-a(kt+1)] - v(t)      (real t in [2,X]; equals the prime data at integers)
  sum_{z<=p<=X}(log p)[v_p(a)-v(p)] = Phi(z) + Ecal(z),
  Phi(z)  = sum_{k<=X/z}(1/k) int_{kz}^{kz+1} a(s)ds - int_z^X v(t)dt   ( = int_z^X frak d dt ),
  Ecal(z) = -E(z^-) frak d(z) - int_z^X E(t) frak d'(t) dt,   E(t)=theta(t)-t, E(z^-)=theta(z-1)-z.
Single-X system: (a,v)=(b_X,w_X).  Difference system: a=c=b_X-b_Y (C^1 on [2,X]),
  c(s)= 2 sqrt(s) L - 4 s dlt  (s<=Y),  b_X(s)  (Y<s<=X),  L=log(X/Y), dlt=Y^{-1/2}-X^{-1/2};
  v=omega,  omega(t)=t^{-1/2} L (t<=Y),  t^{-1/2}log(X/t) (t>Y).
Then T^s(z) = Phi_s(z) + Ecal_s(z) for ALL z in [2,X].
"""
import numpy as np, math, time, sys

def sieve(X):
    isp = np.ones(X + 1, bool); isp[:2] = False
    for i in range(2, int(X ** 0.5) + 1):
        if isp[i]: isp[i * i::i] = False
    return np.nonzero(isp)[0]

def run(X, heavy=True):
    t0 = time.time()
    Y = X // 2
    logX = math.log(X); logY = math.log(Y)
    L = logX - logY
    dlt = Y ** -0.5 - X ** -0.5
    primes = sieve(X); logp = np.log(primes.astype(float))
    theta = np.zeros(X + 2); theta[primes] = logp; theta = np.cumsum(theta)  # theta[n]=sum_{p<=n} log p

    sqX = math.sqrt(X)

    # ---------- single-X seed/ramp ----------
    def bX(s):
        s = np.asarray(s, float)
        return np.where(s <= X, 2*np.sqrt(s)*(logX-np.log(s)) - 4*np.sqrt(s) + 4*s/sqX, 0.0)
    def AntiB(s):
        s = np.minimum(np.asarray(s, float), float(X))
        return (4/3)*s**1.5*(logX-np.log(s)) - (16/9)*s**1.5 + 2*s*s/sqX
    def IB(a, b): return AntiB(b) - AntiB(a)
    def wXf(t):
        t = np.asarray(t, float); return t**-0.5*(logX-np.log(t))
    def AntiW(t):
        t = np.asarray(t, float); return 2*np.sqrt(t)*(logX-np.log(t)) + 4*np.sqrt(t)
    def IW(a, b): return AntiW(b) - AntiW(a)

    # ---------- difference seed/ramp ----------
    def cC(s):
        s = np.asarray(s, float)
        lo = 2*np.sqrt(s)*L - 4*s*dlt
        hi = 2*np.sqrt(s)*(logX-np.log(s)) - 4*np.sqrt(s) + 4*s/sqX
        return np.where(s <= Y, lo, np.where(s <= X, hi, 0.0))
    _ACY = (4/3)*Y**1.5*L - 2.0*Y*Y*dlt   # AntiC(Y) from low branch
    def AntiC(s):
        s = np.minimum(np.asarray(s, float), float(X))
        lo = (4/3)*s**1.5*L - 2.0*s*s*dlt
        hi = AntiB(s) - AntiB(float(Y)) + _ACY
        return np.where(s <= Y, lo, hi)
    def IC(a, b): return AntiC(b) - AntiC(a)
    def om(t):
        t = np.asarray(t, float)
        return np.where(t <= Y, t**-0.5*L, t**-0.5*(logX-np.log(t)))
    _AOY = 2*math.sqrt(Y)*L
    def AntiOm(t):
        t = np.asarray(t, float)
        return np.where(t <= Y, 2*np.sqrt(t)*L, AntiW(t) - AntiW(float(Y)) + _AOY)
    def IOm(a, b): return AntiOm(b) - AntiOm(a)

    # ---------- raw prime data ----------
    def v_of(prs, Z, bfun):
        out = np.empty(len(prs))
        for i, p in enumerate(prs):
            k = np.arange(1, Z // p + 1); m = (k * p).astype(float)
            out[i] = np.sum(bfun(m) - bfun(m + 1)) if len(k) else 0.0
        return out
    vXp = v_of(primes, X, bX)
    rX = vXp - wXf(primes.astype(float))

    # Y-system (raw only, for s and for the T_Y cross-check)
    logYc = logY; sqY = math.sqrt(Y)
    def bYf(s):
        s = np.asarray(s, float)
        return np.where(s <= Y, 2*np.sqrt(s)*(logYc-np.log(s)) - 4*np.sqrt(s) + 4*s/sqY, 0.0)
    pY = primes[primes <= Y]
    vYp = v_of(pY, Y, bYf)
    rY = vYp - pY.astype(float)**-0.5*(logYc-np.log(pY.astype(float)))

    sX = rX.copy(); sX[:len(pY)] -= rY   # s_X(p)

    def sufsum(vals_at_primes):
        contrib = np.zeros(X + 2); contrib[primes] = logp * vals_at_primes
        return np.cumsum(contrib[::-1])[::-1]     # S[z] = sum_{p>=z} (log p)*val
    TX_raw = sufsum(rX)          # T_X(z) = TX_raw[z], z=2..X
    Ts_raw = sufsum(sX)          # T^s(z)
    contribY = np.zeros(X + 2); contribY[pY] = np.log(pY.astype(float)) * rY
    TY_raw = np.cumsum(contribY[::-1])[::-1]
    # sanity: T^s(z) == T_X(z) - 1_{z<=Y} T_Y(z)
    zz = np.arange(2, X + 1)
    chk = Ts_raw[2:X+1] - (TX_raw[2:X+1] - np.where(zz <= Y, TY_raw[2:X+1], 0.0))
    sanity = np.max(np.abs(chk))

    # ---------- decomposition machinery ----------
    def build_tables(seed_pt, seed_I, ramp_pt, ramp_I):
        d = np.zeros(X + 1); J = np.zeros(X + 1)
        for n in range(2, X + 1):
            k = np.arange(1, X // n + 1); a = (k * n).astype(float)
            d[n] = np.sum(seed_pt(a) - seed_pt(a + 1)) - ramp_pt(float(n))
            if n < X:
                J[n] = np.sum((seed_I(a, a + 1) - seed_I(a + k, a + k + 1)) / k) - ramp_I(float(n), float(n + 1))
        return d, J

    def decompose(seed_I, ramp_I, d, J):
        n = np.arange(2, X)      # n = 2..X-1
        P = theta[n]*(d[n+1]-d[n]) - ((n+1)*d[n+1] - n*d[n]) + J[n]
        IE = np.zeros(X + 1)
        IE[2:X] = np.cumsum(P[::-1])[::-1]      # IE[z] = sum_{n=z}^{X-1} P[n]
        Phi = np.zeros(X + 1); Edec = np.zeros(X + 1)
        for z in range(2, X + 1):
            k = np.arange(1, X // z + 1); a = (k * z).astype(float)
            Phi[z] = np.sum(seed_I(a, a + 1) / k) - ramp_I(float(z), float(X))
            Edec[z] = -(theta[z-1] - z)*d[z] - IE[z]
        return Phi, Edec

    dX, JX = build_tables(bX, IB, wXf, IW)
    PhiX, EX = decompose(IB, IW, dX, JX)
    TX_dec = PhiX + EX
    errX = np.max(np.abs(TX_dec[2:X+1] - TX_raw[2:X+1]))
    scaleX = np.max(np.abs(TX_raw[2:X+1]))

    ds, Js = build_tables(cC, IC, om, IOm)
    Phis, Es = decompose(IC, IOm, ds, Js)
    Ts_dec = Phis + Es
    errS = np.max(np.abs(Ts_dec[2:X+1] - Ts_raw[2:X+1]))
    scaleS = np.max(np.abs(Ts_raw[2:X+1]))

    # ---------- B_X and diagnostics ----------
    zarr = np.arange(2, X + 1)
    BX = max(0.0, np.max(Ts_raw[2:X+1]))
    zstar = int(zarr[np.argmax(Ts_raw[2:X+1])])
    maxPhis = np.max(Phis[2:X+1]); argPhis = int(zarr[np.argmax(Phis[2:X+1])])
    maxAbsEs = np.max(np.abs(Es[2:X+1])); argEs = int(zarr[np.argmax(np.abs(Es[2:X+1]))])
    l2X = math.log(2*X)
    print(f"X={X:6d}  [{time.time()-t0:6.1f}s]")
    print(f"  sanity |T^s-(T_X-T_Y)|            = {sanity:.3e}")
    print(f"  VALIDATE single-X:  max|T_X(z)raw - (Phi+Ecal)| = {errX:.3e}   (scale {scaleX:.3e}, rel {errX/scaleX:.3e})")
    print(f"  VALIDATE difference: max|T^s(z)raw - (Phi_s+Ecal_s)| = {errS:.3e}   (scale {scaleS:.3e}, rel {errS/max(scaleS,1e-300):.3e})")
    print(f"  B_X = {BX:.6f} at z*={zstar}   B_X/log^2(2X)={BX/l2X**2:.4f}  /log^3={BX/l2X**3:.5f}  /log^4={BX/l2X**4:.6f}")
    print(f"  moat: max_z Phi_s(z) = {maxPhis:.6f} at z={argPhis}   (positive part {max(0,maxPhis):.3e})")
    print(f"  sampling: max_z |Ecal_s(z)| = {maxAbsEs:.4f} at z={argEs}   /log^2={maxAbsEs/l2X**2:.4f}  /log^3={maxAbsEs/l2X**3:.5f}")
    kb = np.max(np.abs(ds[2:X+1])*np.sqrt(np.arange(2, X+1)))
    kb2 = np.max(np.abs(np.diff(ds[2:X+1]))*(np.arange(2, X)**1.5))
    print(f"  kernel: max t^(1/2)|d_s(t)| = {kb:.4f}   max t^(3/2)|Delta d_s| = {kb2:.4f}   (absolute-constant check)")
    return dict(X=X, BX=BX, zstar=zstar, errX=errX, errS=errS, maxPhis=maxPhis, maxAbsEs=maxAbsEs)

if __name__ == "__main__":
    Xs = [int(a) for a in sys.argv[1:]] or [500, 2000, 10000]
    for X in Xs:
        run(X)
