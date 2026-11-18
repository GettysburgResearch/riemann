#!/usr/bin/env python3
"""Skeptic independent checks for C3 witnesses (different methods from the investigator's witnesses.py).
 rouche_zeta19 : Rouche-type certification of a zeta_19 zero with Re>1 (Arb; explicit second-derivative bound
                 |F''| <= sum (log n)^2 n^{-sigma_min}; no Krawczyk), plus mpmath findroot.
 rouche_dh     : Rouche certification of the Davenport-Heilbronn zero by ball evaluation of F and of its
                 linearisation on a cover of a small circle (Arb), plus a numerical check of the functional
                 equation Lambda(s)=Lambda(1-s), Lambda(s)=(5/pi)^{s/2} Gamma((s+1)/2) f(s) (mpmath).
 chengraham    : mpmath recomputation of |S| for the smooth monotone phase.
 atiyah        : exact rational recursion for h(2s+s^2)=h(2s) to degree 40.
 bbm           : mpmath Hurwitz zeta ratio |zeta(rho1,x+1)| |rho1-1| / sqrt(x).
 queme         : Taylor coefficients of zeta'/zeta at rho1+3/2 by a Cauchy-integral (trapezoid) rule.
 micheas       : partial products in mpmath with TSV ordinates; also tail estimate.
 oliva         : h_n in extended precision (np.longdouble) for p <= 2e7 and analytic f'(x) sign changes.
Usage: python3 sk_witnesses.py ZEROS_TSV out.json [sections]"""
import sys, json, time, math
import numpy as np, mpmath as mp, sympy
import flint
from flint import acb, arb, ctx

R = {}

def rouche_zeta19():
    ctx.prec = 128
    N = 19
    mp.mp.dps = 40
    f = lambda s: sum(mp.power(n, -s) for n in range(1, N+1))
    z = mp.findroot(f, mp.mpc("1.0010955115364764", "600884.2034277758"))
    m = acb(arb(str(z.real)), arb(str(z.imag)))
    Fm = sum((-m*acb(n).log()).exp() for n in range(1, N+1))
    Fpm = sum(-acb(n).log()*(-m*acb(n).log()).exp() for n in range(1, N+1))
    r = arb("1e-15")
    smin = arb(m.real.mid()) - r
    M2 = sum(arb(n).log()**2 * (-(smin)*arb(n).log()).exp() for n in range(1, N+1))
    lhs = M2*r*r/2                     # max |F - lin| on the circle |s-m|=r
    rhs = abs(Fpm)*r - abs(Fm)         # min |lin| on the circle
    ok = bool(lhs < rhs)
    return {"mpmath_zero": mp.nstr(z, 25), "radius": "1e-15", "|F(m)|": str(abs(Fm)), "|F'(m)|": str(abs(Fpm)),
            "M2_bound": str(M2), "rouche_ok_unique_zero_in_disc": ok,
            "Re_lower_bound_of_disc": str(arb(m.real.mid()) - r), "Re_gt_1": bool(arb(m.real.mid()) - r > 1)}

def rouche_dh():
    ctx.prec = 160
    mp.mp.dps = 40
    k = (mp.sqrt(10-2*mp.sqrt(5))-2)/(mp.sqrt(5)-1)
    a = [0, 1, k, -k, -1]
    fm = lambda s: mp.power(5, -s)*sum(a[j]*mp.zeta(s, mp.mpf(j)/5) for j in range(1, 5))
    z = mp.findroot(fm, mp.mpc("0.808517", "85.699348"))
    # functional equation check at a few points
    Lam = lambda s: (5/mp.pi)**(s/2)*mp.gamma((s+1)/2)*fm(s)
    fe = [mp.nstr(abs(Lam(s)-Lam(1-s))/abs(Lam(s)), 5) for s in (mp.mpc(0.3, 7.1), mp.mpc(0.9, 23.4), mp.mpc(-0.4, 3.3))]
    # Arb Rouche on circle |s-m|=r, cover by boxes
    r5 = arb(5).sqrt(); kap = ((10-2*r5).sqrt()-2)/(r5-1)
    co = [acb(1), acb(kap), acb(-kap), acb(-1)]
    def F(s):
        return sum(c*s.zeta(acb(j)/5) for c, j in zip(co, (1, 2, 3, 4)))*((-s)*acb(5).log()).exp()
    m = acb(arb(mp.nstr(z.real, 35)), arb(mp.nstr(z.imag, 35)))
    Fm = F(m)
    h = arb("1e-20")
    Fpm = (F(m + acb(h)) - F(m - acb(h)))/(2*h)     # any complex number works as 'slope' for Rouche (no rigor needed)
    Fpm = acb(Fpm.real.mid(), Fpm.imag.mid())
    r = 1e-10; K = 400; ok = True; worst = 0.0
    for j in range(K):
        th0 = 2*math.pi*j/K; th1 = 2*math.pi*(j+1)/K; thm = (th0+th1)/2
        # box covering the arc: centre at r e^{i thm}, radius r*(th1-th0)/2*1.01 in each coordinate
        cx = r*math.cos(thm); cy = r*math.sin(thm); rad = r*(th1-th0)*0.51
        B = m + acb(arb(cx, rad), arb(cy, rad))
        lin = Fm + Fpm*(B - m)
        d = abs(F(B) - lin); l = abs(lin)
        if not (d < l): ok = False
        worst = max(worst, float(d.upper())/float(l.lower()) if l.lower() > 0 else float('inf'))
    return {"mpmath_zero": mp.nstr(z, 25), "fe_rel_residuals": fe, "rouche_radius": r, "arcs": K,
            "rouche_ok": ok, "worst_ratio_|F-lin|/|lin|": worst,
            "Re_minus_half_lower": mp.nstr(z.real - r - mp.mpf(1)/2, 12)}

def chengraham():
    mp.mp.dps = 40
    th = mp.mpf("0.02"); w = mp.mpf("0.05")
    f = lambda x: th*x + (1-2*th)*w*mp.log(1+mp.exp((x-1000)/w))
    S = sum(mp.expjpi(2*f(n)) for n in range(975, 1026))
    fp_lo = th + (1-2*th)/(1+mp.exp(25/w)); fp_hi = th + (1-2*th)/(1+mp.exp(-25/w))
    return {"|S|": mp.nstr(abs(S), 25), "CG_bound": mp.nstr(1/(mp.pi*th)+1, 15), "Landau": mp.nstr(mp.cot(mp.pi*th/2), 15),
            "f'_range_on_[975,1025]": [mp.nstr(fp_lo, 12), mp.nstr(fp_hi, 12)], "theta<=f'<=1-theta": bool(fp_lo >= th and fp_hi <= 1-th)}

def atiyah():
    # exact integer linear algebra: coefficient of s^m in h(2s+s^2)-h(2s) is sum_{m/2<=k<=m-1} c_k C(k,m-k) 2^{2k-m}
    # build the (D-1)x(D-1) matrix for unknowns c_1..c_{D-1} (m=2..D) and verify it is nonsingular (=> only c=0)
    from math import comb
    D = 60
    A = sympy.zeros(D-1, D-1)
    for m in range(2, D+1):
        for k in range((m+1)//2, m):
            A[m-2, k-1] = comb(k, m-k) * sympy.Integer(2)**(2*k-m)
    det = A.det(method="bareiss")
    return {"degree": D, "matrix_lower_triangular_in_c_{m-1}": True, "det": str(det)[:40], "nonsingular": det != 0}

def bbm():
    # mpmath Hurwitz zeta for x <= 1e6 (mpmath's sieve overflows memory for a ~ 1e10); for larger x an explicit
    # Euler-Maclaurin sum: zeta(s,a) = sum_{n<M} (a+n)^{-s} + (a+M)^{1-s}/(s-1) + (a+M)^{-s}/2
    #   + sum_k B_{2k}/(2k)! (s)_{2k-1} (a+M)^{-s-2k+1}   with M = 0 (a is huge), 8 Bernoulli terms.
    mp.mp.dps = 30
    rho = mp.zetazero(1); out = {}
    for x in (1e2, 1e4, 1e6, 1e8, 1e10):
        a = mp.mpf(x) + 1
        if x <= 1e6:
            z = mp.zeta(rho, a); how = "mpmath.zeta(s,a)"
        else:
            z = a**(1-rho)/(rho-1) + a**(-rho)/2
            for k in range(1, 9):
                z += mp.bernoulli(2*k)/mp.factorial(2*k)*mp.rf(rho, 2*k-1)*a**(-rho-2*k+1)
            how = "explicit Euler-Maclaurin"
        out[str(x)] = [mp.nstr(abs(z)*abs(rho-1)/mp.sqrt(x), 15), how]
    return out

def queme():
    mp.mp.dps = 30
    rho = mp.zetazero(1); v = mp.mpf(3)/2; c = rho+v
    f = lambda z: mp.zeta(z, derivative=1)/mp.zeta(z)
    Np = 192; rr = mp.mpf("1.2")
    vals = [f(c + rr*mp.expjpi(2*mp.mpf(j)/Np)) for j in range(Np)]
    out = []
    for k in range(0, 27):
        ak = sum(vals[j]*mp.expjpi(-2*mp.mpf(j*k)/Np) for j in range(Np))/Np/rr**k
        out.append(float(abs(ak*(-v)**k)))
    return {"abs_terms_k=0..26": out, "note": "trapezoid Cauchy integral, radius 1.2, 192 nodes; aliasing error ~ (1.2/1.5)^192"}

def micheas(path):
    mp.mp.dps = 30
    t = []
    for line in open(path):
        t.append(mp.mpf(line.split()[1]))
        if len(t) >= 100000: break
    t1 = t[0]; P = mp.mpf(1); ck = {}
    for n, tn in enumerate(t, start=1):
        tau = tn - mp.mpf(1)/(2*n)
        P *= (tau**2 - t1**2)/(mp.mpf(1)/4 + tau**2)
        if n in (1, 100, 1000, 10000, 100000): ck[str(n)] = mp.nstr(P, 15)
    return {"partial_products": ck}

def oliva(PMAX=20_000_000):
    s = np.ones(PMAX+1, dtype=bool); s[:2] = False
    for i in range(2, int(PMAX**0.5)+1):
        if s[i]: s[i*i::i] = False
    P = np.nonzero(s)[0].astype(np.longdouble)
    th = np.cumsum(np.log(P))
    p1 = P[1:]; L1 = th[1:]; L0 = th[:-1]
    h = (1-1/p1)*np.log(L1) - np.log(L0)
    i = int(np.argmin(h))
    # analytic derivative sign of f(x) = (1 - a/log x - 1/b)/(1 - a/log(x - log b)) at x = b and turning point
    mp.mp.dps = 50
    a = mp.exp(-mp.euler)
    def fprime(x, b):
        u = mp.log(x); w = mp.log(x - mp.log(b))
        N = 1 - a/u - 1/b; D = 1 - a/w
        return (a/(x*u**2))*D - N*(a/((x-mp.log(b))*w**2))
    tp = {}
    for b in (10**4, 10**6, 10**8, 10**12):
        b = mp.mpf(b)
        g = lambda y: fprime(mp.exp(y), b)
        y0 = mp.findroot(g, (mp.log(b*mp.log(b)*0.9), mp.log(b*mp.log(b)*1.5)), solver='anderson')
        tp[mp.nstr(b, 3)] = {"f'(b)_sign": int(mp.sign(fprime(b, b))), "turning_x/(b log b)": mp.nstr(mp.exp(y0)/(b*mp.log(b)), 6)}
    return {"longdouble_eps": float(np.finfo(np.longdouble).eps), "min_h": float(h[i]), "p_at_min": float(p1[i]),
            "all_positive": bool((h > 0).all()), "turning_points": tp}

if __name__ == "__main__":
    path = sys.argv[1]; out = sys.argv[2]
    secs = sys.argv[3].split(",") if len(sys.argv) > 3 else ["rouche_zeta19", "rouche_dh", "chengraham", "atiyah", "bbm", "queme", "micheas", "oliva"]
    for sname in secs:
        t0 = time.time()
        fn = globals()[sname]
        R[sname] = fn(path) if sname == "micheas" else fn()
        R[sname]["runtime_s"] = round(time.time()-t0, 1)
        print(sname, json.dumps(R[sname]), flush=True)
    R["versions"] = {"mpmath": mp.__version__, "flint": flint.__version__, "sympy": sympy.__version__, "numpy": np.__version__}
    json.dump(R, open(out, "w"), indent=1)
