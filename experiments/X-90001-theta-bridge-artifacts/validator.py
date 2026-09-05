"""Validator for the exact decomposition  T_X(z) = Phi_X(z) + F_X(z).

Definitions (all EXACT, integers):
  b_X(m) = 2 sqrt(m)(log(X/m) - 2(1-sqrt(m/X))) on [2,X], else 0.   b_X(X)=0.
  Db(n) = b(n)-b(n+1);  v_d(b_X) = sum_{k<=X/d} Db(kd)  for ANY integer d>=2.
  g_X(d) = d^{-1/2} log(X/d);  theta(n) = sum_{p<=n} log p;  E(n) = theta(n)-n.
  V_X(z) = sum_{z<=p<=X} log p * v_p;  W_X(z) = sum_{z<=p<=X} log p * g_X(p);
  T_X(z) = V_X(z) - W_X(z).

Identity 1 (von Mangoldt):   sum_{p^a<=X} Lambda(p^a) v_{p^a}(b_X) = A_X
   with A_X = sum_{n=2}^X Db(n) log n     (exact; log n = sum_{d|n} Lambda(d)).
Hence  V_X(2) = A_X - Q_X,  Q_X = sum_{a>=2} sum_{p<=M_a} log p v_{p^a},
   M_a = floor(X^{1/a}).

Identity 2 (discrete Stieltjes/Abel): for any c on [alpha,beta] (2<=alpha<=beta):
  sum_{alpha<=p<=beta} log p c(p) = sum_{d=alpha}^{beta} c(d)
      + c(beta)E(beta) - c(alpha)E(alpha-1) - sum_{d=alpha}^{beta-1}(c(d+1)-c(d))E(d).

Applying Id.2 to Q_X (per a), to SmallV(z)=sum_{p<z} log p v_p (alpha=2, beta=z-1),
and to W_X(z) (alpha=z, beta=X, note g_X(X)=0), and using E(1) = -1:

  T_X(z) = Phi_X(z) + F_X(z),   with  (z>=3; for z=2 drop the SmallV terms)

  Phi_X(z) = A_X - PPS - [ sum_{d=2}^{z-1} v_d + v_2 ] - sum_{d=z}^{X} g(d)
     PPS   = sum_{a>=2} [ sum_{d=2}^{M_a} v_{d^a} + v_{2^a} ]
  F_X(z)  = - sum_{a>=2} [ v_{M_a^a} E(M_a) - sum_{d=2}^{M_a-1} (v_{(d+1)^a}-v_{d^a}) E(d) ]
            - [ v_{z-1} E(z-1) - sum_{d=2}^{z-2} (v_{d+1}-v_d) E(d) ]
            + g(z) E(z-1) + sum_{d=z}^{X-1} (g(d+1)-g(d)) E(d).

Phi is prime-free (only b and elementary sums).  F is a linear functional of E
with explicit kernels.  s-version: Y=floor(X/2), T^s(z)=T_X(z)-1_{z<=Y}T_Y(z),
B_X = max_z [T^s(z)]_+.
"""
import numpy as np


def sieve(n):
    s = np.ones(n + 1, bool); s[:2] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]: s[i * i::i] = False
    return s


def introot(X, a):
    M = int(round(X ** (1.0 / a)))
    while (M + 1) ** a <= X: M += 1
    while M ** a > X: M -= 1
    return M


def build(X):
    """All arrays for one scale X (prime-free parts + prime parts kept separate)."""
    S = {}
    S['X'] = X
    m = np.arange(0, X + 2, dtype=np.float64)
    b = np.zeros(X + 2)
    mm = m[2:X + 1]
    b[2:X + 1] = 2.0 * np.sqrt(mm) * (np.log(X / mm) - 2.0 * (1.0 - np.sqrt(mm / X)))
    Db = b[:-1] - b[1:]                      # Db[n], n=0..X
    S['b'] = b
    # ---- prime-free objects ----
    v = np.zeros(X + 1)                      # v[d] = v_d(b_X), d=2..X
    for d in range(2, X + 1):
        v[d] = Db[d::d].sum()
    S['v'] = v
    dgrid = np.arange(0, X + 1, dtype=np.float64)
    g = np.zeros(X + 1)
    g[2:] = dgrid[2:] ** -0.5 * np.log(X / dgrid[2:])   # g[d], d=2..X (g[X]=0)
    S['g'] = g
    n = np.arange(2, X + 1, dtype=np.float64)
    S['A'] = float(np.dot(Db[2:X + 1], np.log(n)))       # A_X
    PPS = 0.0
    pp_list = []                                          # (a, M_a, arr v_{d^a})
    a = 2
    while 2 ** a <= X:
        Ma = introot(X, a)
        da = np.arange(2, Ma + 1)
        vpa = v[da ** a]
        PPS += vpa.sum() + vpa[0]                         # + v_{2^a} (E(1)=-1 fold)
        pp_list.append((a, Ma, vpa))
        a += 1
    S['PPS'] = PPS; S['pp'] = pp_list
    # prefix / suffix prime-free sums
    pref_v = np.zeros(X + 2)                              # pref_v[z] = sum_{d=2}^{z-1} v_d
    pref_v[3:X + 2] = np.cumsum(v[2:X + 1])
    S['pref_v'] = pref_v
    GW = np.zeros(X + 2)                                  # GW[z] = sum_{d=z}^{X} g(d)
    GW[2:X + 1] = np.cumsum(g[2:X + 1][::-1])[::-1]
    S['GW'] = GW
    # ---- prime objects ----
    isp = sieve(X)
    logs = np.zeros(X + 1)
    pr = np.nonzero(isp)[0]
    logs[pr] = np.log(pr.astype(np.float64))
    theta = np.cumsum(logs)
    E = theta - np.arange(0, X + 1, dtype=np.float64)     # E[n], n=0..X ; E[1]=-1
    S['isp'] = isp; S['P'] = pr; S['E'] = E; S['theta'] = theta
    # raw T for all integer z: suffix over primes of log p (v_p - g(p))
    term = np.zeros(X + 2)
    term[pr] = logs[pr] * (v[pr] - g[pr])
    S['Traw'] = np.concatenate([np.cumsum(term[::-1])[::-1], ])[:X + 2]  # Traw[z], z<=X
    # decomposition E-parts
    dv = v[3:X + 1] - v[2:X]                              # dv[i] = v[d+1]-v[d], d=2..X-1
    dg = g[3:X + 1] - g[2:X]
    dd = np.arange(2, X)
    pref_dvE = np.zeros(X + 2)                            # sum_{d=2}^{z-2} dv(d)E(d)
    pref_dvE[4:X + 2] = np.cumsum(dv * E[dd])
    S['pref_dvE'] = pref_dvE
    suf_dgE = np.zeros(X + 2)                             # sum_{d=z}^{X-1} dg(d)E(d)
    suf_dgE[2:X] = np.cumsum((dg * E[dd])[::-1])[::-1]
    S['suf_dgE'] = suf_dgE
    PP_E = 0.0
    for a, Ma, vpa in pp_list:
        PP_E += vpa[-1] * E[Ma]
        if Ma > 2:
            d = np.arange(2, Ma)
            PP_E -= np.dot(vpa[1:] - vpa[:-1], E[d])
    S['PP_E'] = PP_E
    # assembled Phi(z), F(z) for all z=2..X
    z = np.arange(2, X + 1)
    smallv_const = np.where(z >= 3, pref_v[z] + v[2], 0.0)
    smallv_E = np.where(z >= 3, v[z - 1] * E[z - 1] - pref_dvE[z], 0.0)
    Phi = S['A'] - PPS - smallv_const - GW[z]
    F = -PP_E - smallv_E + g[z] * E[z - 1] + suf_dgE[z]
    S['z'] = z; S['Phi'] = Phi; S['F'] = F; S['Tdec'] = Phi + F
    return S


def rh_Ebound(X, E):
    """Majorant for |E(d)|: exact below 599 (deterministic), RH bound above."""
    d = np.arange(0, X + 1, dtype=np.float64)
    eb = np.where(d >= 599, np.sqrt(np.maximum(d, 2)) * np.log(np.maximum(d, 2)) ** 2 / (8 * np.pi)
                  + 1.001 * np.sqrt(np.maximum(d, 2)),
                  np.abs(E))
    return eb


def certificate(SX, SY):
    """C^s(z): sum over d of |combined kernel| * Ebound(d), for all z."""
    X, Y = SX['X'], SY['X']
    EbX = rh_Ebound(X, SX['E'])
    v_X, g_X = SX['v'], SX['g']; v_Y, g_Y = SY['v'], SY['g']
    dvX = v_X[3:X + 1] - v_X[2:X]; dgX = g_X[3:X + 1] - g_X[2:X]   # d=2..X-1
    dvY = v_Y[3:Y + 1] - v_Y[2:Y]; dgY = g_Y[3:Y + 1] - g_Y[2:Y]   # d=2..Y-1
    dd = np.arange(2, X)
    eb = EbX[dd]
    # SmallV kernels (prefix, d=2..z-2)
    kv = np.abs(dvX.copy())
    kv[:Y - 2] = np.abs(dvX[:Y - 2] - dvY)                # combined for d<=Y-1
    # NOTE: combined-small-prime kernel valid for z<=Y only where prefix stops at z-2<=Y-2 -> fine
    pref_kv = np.zeros(X + 2); pref_kv[4:X + 2] = np.cumsum(kv * eb)
    pref_kvX = np.zeros(X + 2); pref_kvX[4:X + 2] = np.cumsum(np.abs(dvX) * eb)
    # W kernels (suffix, d=z..X-1)
    kg = np.abs(dgX.copy())
    kg[:Y - 2] = np.abs(dgX[:Y - 2] - dgY)
    suf_kg = np.zeros(X + 2); suf_kg[2:X] = np.cumsum((kg * eb)[::-1])[::-1]
    suf_kgX = np.zeros(X + 2); suf_kgX[2:X] = np.cumsum((np.abs(dgX) * eb)[::-1])[::-1]
    # PP kernels (constants)
    def cpp(S, Eb):
        tot = 0.0
        for a, Ma, vpa in S['pp']:
            tot += abs(vpa[-1]) * Eb[Ma]
            if Ma > 2:
                d = np.arange(2, Ma)
                tot += np.dot(np.abs(vpa[1:] - vpa[:-1]), Eb[d])
        return tot
    CPP = cpp(SX, EbX) + cpp(SY, EbX[:Y + 1])
    CPPX = cpp(SX, EbX)
    z = np.arange(2, X + 1)
    C = np.empty(X - 1)
    mask = z <= Y
    # boundary coefficient of E(z-1)
    bc = np.where(mask,
                  np.abs((g_X[z] - np.where(mask, g_Y[np.minimum(z, Y)], 0.0))
                         - (np.where(z >= 3, v_X[z - 1], 0.0) - np.where(mask & (z >= 3), v_Y[np.minimum(z - 1, Y)], 0.0))),
                  np.abs(g_X[z] - np.where(z >= 3, v_X[z - 1], 0.0)))
    C = bc * EbX[z - 1] + np.where(mask, pref_kv[z] + suf_kg[z] + CPP,
                                   pref_kvX[z] + suf_kgX[z] + CPPX)
    return C


def run(X, table=False):
    SX = build(X)
    Y = X // 2
    SY = build(Y)
    X_ = SX['X']
    # ---- exactness checks, X and Y separately ----
    errX = np.abs(SX['Traw'][2:X + 1] - SX['Tdec']).max()
    errY = np.abs(SY['Traw'][2:Y + 1] - SY['Tdec']).max()
    scale = max(1.0, np.abs(SX['Traw'][2:X + 1]).max())
    # Identity-1 internal check
    P = SX['P']
    Qdir = 0.0
    for a, Ma, vpa in SX['pp']:
        pp = P[P <= Ma]
        Qdir += float(np.dot(np.log(pp.astype(float)), SX['v'][pp ** a]))
    V2dir = float(np.dot(np.log(P.astype(float)), SX['v'][P]))
    id1err = abs(V2dir - (SX['A'] - Qdir))
    id2err = abs(Qdir - (SX['PPS'] + SX['PP_E']))
    # ---- s-version ----
    z = np.arange(2, X + 1)
    TsRaw = SX['Traw'][2:X + 1] - np.where(z <= Y, SY['Traw'][np.minimum(z, Y)], 0.0)
    TsDec = SX['Tdec'] - np.where(z <= Y, (SY['Tdec'][np.minimum(z, Y) - 2]), 0.0)
    errS = np.abs(TsRaw - TsDec).max()
    B = max(0.0, TsRaw.max())
    PhiS = SX['Phi'] - np.where(z <= Y, SY['Phi'][np.minimum(z, Y) - 2], 0.0)
    FS = SX['F'] - np.where(z <= Y, SY['F'][np.minimum(z, Y) - 2], 0.0)
    C = certificate(SX, SY)
    ceil = PhiS + C
    print(f"X={X}  Y={Y}  #primes={len(P)}")
    print(f"  exactness: max|Traw-Tdec| X: {errX:.3e}  Y: {errY:.3e}  s: {errS:.3e}"
          f"   (scale {scale:.3g})")
    print(f"  Identity1 |V(2)-(A-Q)| = {id1err:.3e}   Id2(Q Stieltjes) = {id2err:.3e}")
    print(f"  B_X(raw) = {B:.6g}   max_z T^s = {TsRaw.max():.6g} at z={z[TsRaw.argmax()]}")
    print(f"  max_z Phi^s = {PhiS.max():.6g} at z={z[PhiS.argmax()]}   "
          f"min Phi^s = {PhiS.min():.6g}")
    print(f"  max_z |F^s| = {np.abs(FS).max():.6g}   max_z C^s (RH majorant) = {C.max():.6g}")
    print(f"  CERTIFIED RH CEILING max_z[Phi^s+C^s] = {ceil.max():.6g} at z={z[ceil.argmax()]}")
    print(f"  A_X={SX['A']:.6f}  Q_X={Qdir:.6f}  4*sqrt(X)={4*np.sqrt(X):.3f}")
    if table:
        print("    z      T_X(z)      Phi_X(z)    F_X(z)  |  T^s(z)      Phi^s       F^s        C^s")
        for frac in (0.0005, 0.002, 0.01, 0.05, 0.1, 0.2, 0.35, 0.5, 0.52, 0.7, 0.9, 0.99):
            zz = max(2, int(frac * X))
            i = zz - 2
            print(f"  {zz:6d} {SX['Traw'][zz]:11.4f} {SX['Phi'][i]:11.4f} {SX['F'][i]:9.4f} |"
                  f" {TsRaw[i]:10.4f} {PhiS[i]:11.4f} {FS[i]:9.4f} {C[i]:9.3f}")
    return dict(errX=errX, errY=errY, errS=errS, B=B, PhiSmax=PhiS.max(), ceil=ceil.max())


if __name__ == "__main__":
    import sys
    for X in (500, 2000, 10000, 50000):
        run(X, table=(X in (10000, 50000)))
        print()
