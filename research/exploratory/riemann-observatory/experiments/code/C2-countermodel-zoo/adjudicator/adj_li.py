#!/usr/bin/env python3
"""ADJUDICATOR (C2-countermodel-zoo), claim C2-16 / skeptic finding F3.  NUMERICAL-NONRIGOROUS (float64 + mpmath).

Independent recomputation of the Li coefficients of xi~ = xi * P_Q, with Q = {rho0, conj rho0, 1-rho0, 1-conj rho0}.

  lambda_n(xi) = sum_{0<gamma<=T*} 4 sin^2(n th(gamma)/2) + tail_n,   th(g) = 2 arctan(1/(2g)),
  tail_n       = int_{T*}^inf 4 sin^2(n th/2) dN_sm  -  4 sin^2(n th(T*)/2) S(T*)  +  E_n,

where N_sm(t) = vartheta(t)/pi + 1 (Riemann-Siegel theta), S(T*) = N(T*) - N_sm(T*) with N(T*) = 100000 exactly
(T* = gamma_100000 + 1e-9), and E_n = -int_{T*}^inf S(g) g_n'(g) dg.  This differs from BOTH earlier codes:
the investigator interpolated lambda_n(xi) on a 60-point grid; the skeptic computed every n exactly but started the
smooth tail at T = gamma_100000 WITHOUT the boundary term S(T*) g_n(T*).  We estimate |E_n| <= 2 (2.067 + 0.059 log T*)
int |g_n''| (Trudgian's bound for S_1; integration by parts), which is << 1e-3 for n <= 1.2e5.

Zero sums for all n = 1..NMAX use a complex rotation recurrence, re-anchored every 256 steps by direct exp(i n th).
The quadruple term sum_{rho in Q} [1 - (1-1/rho)^n] is exact (numpy complex; the values at the sign changes are
re-checked with mpmath at 50 digits).

Usage: python3 adj_li.py OUTDIR ZEROFILE1 ZEROFILE2
"""
import sys, os, json, time, math, hashlib
import numpy as np
import mpmath as mp

NMAX = 115000
CASES = [(0.6, 14.0), (0.75, 14.0), (0.6, 30.0), (0.75, 30.0)]
JOHANSSON_L1E5 = 462580.78240690223141   # Johansson arXiv:1309.2877 sect. 4 (his lambda_n is Li's lambda_n / n)


def load(files):
    g = []
    for fn in files:
        with open(fn) as fh:
            for line in fh:
                p = line.split()
                if len(p) >= 2:
                    g.append(float(p[1]))
    g = np.array(sorted(g))
    assert g.size == 100000
    return g


def zero_sums(theta, nmax, anchor=256):
    """C[n] = sum_k cos(n theta_k), n = 0..nmax."""
    C = np.empty(nmax + 1)
    w = np.exp(1j * theta)
    z = np.ones_like(w)
    C[0] = theta.size
    for n in range(1, nmax + 1):
        if n % anchor == 0:
            z = np.exp(1j * n * theta)
        else:
            z = z * w
        C[n] = z.real.sum()
    return C


def gl_nodes(u_star, J=62, m=30):
    x, w = np.polynomial.legendre.leggauss(m)
    U, W = [], []
    for j in range(J):
        a, b = u_star * 2.0 ** (-j - 1), u_star * 2.0 ** (-j)
        U.append(0.5 * (b - a) * x + 0.5 * (b + a)); W.append(0.5 * (b - a) * w)
    return np.concatenate(U), np.concatenate(W)


def smooth_tail(ns, T):
    """int_T^inf 4 sin^2(n arctan(1/(2g))) vartheta'(g)/pi dg, with vartheta'(g) = log(g/2pi)/2 - 1/(48 g^2)."""
    U, W = gl_nodes(1.0 / T)
    dens = (np.log(1.0 / (2 * np.pi * U)) / (2 * np.pi) - U ** 2 / (48 * np.pi)) / U ** 2
    out = np.empty(len(ns))
    for i0 in range(0, len(ns), 2000):
        nn = np.asarray(ns[i0:i0 + 2000], float)[:, None]
        out[i0:i0 + 2000] = (4 * np.sin(nn * np.arctan(U / 2)[None, :]) ** 2 * (dens * W)[None, :]).sum(axis=1)
    return out


def E_bound(n, T):
    """2 (2.067 + 0.059 log T) * int_T^inf |g_n''(g)| dg (numerical quadrature), g_n(g) = 4 sin^2(n arctan(1/(2g)))."""
    gfun = lambda x: 4 * mp.sin(n * mp.atan(1 / (2 * x))) ** 2
    d2 = lambda x: abs(mp.diff(gfun, x, 2))
    val = mp.quad(d2, [T, 2 * T, 10 * T, 100 * T, mp.inf])
    return float(2 * (2.067 + 0.059 * math.log(T)) * val)


def quad_term_np(ns, beta, gam):
    rho = complex(beta, gam)
    tot = np.zeros(len(ns))
    for r in (rho, rho.conjugate(), 1 - rho, 1 - rho.conjugate()):
        L = np.log(1 - 1 / r)
        tot += (1 - np.exp(np.asarray(ns, float) * L)).real
    return tot


def quad_term_mp(n, beta, gam):
    mp.mp.dps = 50
    rho = mp.mpc(beta, gam)
    return mp.re(sum(1 - (1 - 1 / r) ** n for r in (rho, mp.conj(rho), 1 - rho, 1 - mp.conj(rho))))


def main():
    t0 = time.time()
    outdir = sys.argv[1]
    g = load(sys.argv[2:])
    T = g[-1] + 1e-9
    theta = 2 * np.arctan(1 / (2 * g))
    mp.mp.dps = 30
    S_T = 100000 - (mp.siegeltheta(T) / mp.pi + 1)
    S_T = float(S_T)
    C = zero_sums(theta, NMAX)
    ns = np.arange(0, NMAX + 1)
    zs = 2 * g.size - 2 * C                      # sum 4 sin^2(n th/2) = 2N - 2 sum cos
    # direct check of the recurrence at a few n
    chk = {}
    for n in (1, 2, 7395, 7477, 20855, 100000, 112538):
        direct = float(np.sum(4 * np.sin(n * theta / 2) ** 2))
        chk[n] = dict(direct=direct, recurrence=float(zs[n]), diff=float(zs[n] - direct))
    tail_sm = smooth_tail(ns, T)
    gT = 4 * np.sin(ns * np.arctan(1 / (2 * T))) ** 2
    lam = zs + tail_sm - gT * S_T
    lam_skeptic_style = zs + tail_sm            # no boundary term (skeptic's convention, T = last zero)
    res = dict(script='adj_li.py', T_star=T, S_of_T_star=S_T, NMAX=NMAX,
               recurrence_check=chk,
               lambda_1=float(lam[1]), lambda_2=float(lam[2]),
               lambda_1_ref='0.0230957089661210338', lambda_2_ref='0.0923457352280327',
               lambda_1e5=float(lam[100000]), lambda_1e5_without_boundary_term=float(lam_skeptic_style[100000]),
               lambda_1e5_Johansson=JOHANSSON_L1E5,
               E_bound={str(n): E_bound(n, T) for n in (7477, 20855, 100000, 112538)})
    cases = []
    for beta, gam in CASES:
        q = quad_term_np(ns, beta, gam)
        tot = lam + q
        tot[0] = 1.0
        neg = np.nonzero(tot[1:] < 0)[0]
        first = int(neg[0] + 1) if neg.size else None
        rec = dict(beta=beta, gamma0=gam, first_negative_n=first)
        if first:
            prev = tot[1:first]
            rec['min_before_first'] = float(prev.min()); rec['argmin_before_first'] = int(np.argmin(prev) + 1)
            rec['value_at_first'] = float(tot[first]); rec['value_at_first_minus_1'] = float(tot[first - 1])
            rec['mp_check_quad_term_at_first'] = float(quad_term_mp(first, beta, gam))
            rec['np_quad_term_at_first'] = float(q[first])
            # skeptic-style (no boundary term) first negative, for comparison
            tot2 = lam_skeptic_style + q; tot2[0] = 1.0
            neg2 = np.nonzero(tot2[1:] < 0)[0]
            rec['first_negative_without_boundary_term'] = int(neg2[0] + 1) if neg2.size else None
        for n in (7395, 20857, 112929, 41098):
            if n <= NMAX:
                rec.setdefault('values_at_investigator_ns', {})[str(n)] = float(tot[n])
        cases.append(rec)
        print(rec, flush=True)
    res['cases'] = cases
    res['versions'] = dict(python=sys.version.split()[0], numpy=np.__version__, mpmath=mp.__version__)
    res['runtime_s'] = round(time.time() - t0, 1)
    os.makedirs(outdir, exist_ok=True)
    fn = os.path.join(outdir, 'adj_li.json')
    with open(fn, 'w') as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps({k: v for k, v in res.items() if k != 'cases'}, indent=1))
    print(hashlib.sha256(open(fn, 'rb').read()).hexdigest(), fn)


if __name__ == '__main__':
    main()
