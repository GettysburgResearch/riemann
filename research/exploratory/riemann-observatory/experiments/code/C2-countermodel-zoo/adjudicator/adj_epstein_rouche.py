#!/usr/bin/env python3
"""ADJUDICATOR (C2-countermodel-zoo), skeptic finding F4.  NUMERICAL-RIGOROUS (Arb ball arithmetic, python-flint).

Second, independent certificate (after the skeptic's winding-number certificate) for zeros of Z_Q, Q = x^2 + 5y^2, with Re s > 1 at low height
(skeptic located t ~ 1193.9464 and t ~ 4108.1083; investigator's lowest certified one was at t ~ 3.59e6).

Evaluation route (different from both earlier codes): Hurwitz-zeta form of the genus decomposition
    Z_Q(s) = zeta(s) L(s, chi_-20) + L(s, chi_-4) L(s, chi_5),   L(s, chi mod q) = q^{-s} sum_a chi(a) zeta(s, a/q),
with chi_-4, chi_5 written out explicitly and chi_-20 = chi_-4 chi_5.

Certificate (Rouche with a Cauchy remainder bound; different from Krawczyk (investigator) and from the
winding-number argument principle (skeptic)):
  c = Newton-polished point, f(c), f'(c) as Arb balls (acb_series), M >= sup |f| over the square c + [-R,R]^2
  (one Arb evaluation of f on that square, which contains the closed disc |z-c| <= R).  For |z-c| <= r < R,
  |f''(z)| <= 2M/(R-r)^2 (Cauchy), so |f(z) - f(c) - f'(c)(z-c)| <= M r^2/(R-r)^2.  If
        |f'(c)| r - |f(c)| > M r^2/(R-r)^2   (all lower/upper bounds taken in Arb),
  then on |z-c| = r we have |f - lin| < |lin|, so f has exactly as many zeros in |z-c| < r as the linear
  function lin(z) = f(c) + f'(c)(z-c), namely one (its root lies inside because |f(c)| < |f'(c)| r).
  Off-line / sigma > 1 status: Re(c) - r > 1 checked in Arb.
The identity is sanity-checked at s = 3 against a direct lattice sum (non-rigorous, truncation |m|,|n| <= 400).

Usage: python3 adj_epstein_rouche.py OUTDIR
"""
import sys, os, json, time, hashlib
import flint
from flint import acb, arb, acb_series

PREC = 192
CANDIDATES = [complex(1.0110493, 1193.94640), complex(1.0150707, 4108.10828)]


def chi_m4(a):
    return {1: 1, 3: -1}.get(a % 4, 0)


def chi_5(a):
    return {1: 1, 2: -1, 3: -1, 4: 1}.get(a % 5, 0)


def chi_m20(a):
    return chi_m4(a) * chi_5(a)


def L_hurwitz(s, chi, q):
    """s: acb or acb_series. L(s, chi) = q^{-s} sum_{a=1}^{q} chi(a) zeta(s, a/q)."""
    tot = None
    for a in range(1, q + 1):
        c = chi(a)
        if c == 0:
            continue
        if isinstance(s, acb_series):
            term = acb_series.zeta(s, acb(a) / q) * c
        else:
            term = s.zeta(acb(a) / q) * c
        tot = term if tot is None else tot + term
    if isinstance(s, acb_series):
        return (-s * acb(q).log()).exp() * tot
    return (-s * acb(q).log()).exp() * tot


def Z(s):
    if isinstance(s, acb_series):
        zeta = acb_series.zeta(s)
    else:
        zeta = s.zeta()
    return zeta * L_hurwitz(s, chi_m20, 20) + L_hurwitz(s, chi_m4, 4) * L_hurwitz(s, chi_5, 5)


def f_and_df(z):
    c = Z(acb_series([z, 1], prec=2)).coeffs()
    while len(c) < 2:
        c.append(acb(0))
    return c[0], c[1]


def newton(z, steps=60):
    zc = acb(z.real, z.imag)
    for _ in range(steps):
        f, d = f_and_df(zc)
        st = f / d
        zc = acb(zc.real.mid(), zc.imag.mid()) - acb(st.real.mid(), st.imag.mid())
        if abs(complex(st)) < 1e-45:
            break
    return zc


def certify(z0, r=1e-12, R=1e-4):
    c = newton(z0)
    c = acb(c.real.mid(), c.imag.mid())          # exact binary point
    f0, d0 = f_and_df(c)
    box = acb(arb(c.real.mid(), R), arb(c.imag.mid(), R))
    M = abs(Z(box)).upper()
    lhs = abs(d0).lower() * arb(r) - abs(f0).upper()
    rhs = M * arb(r) ** 2 / (arb(R) - arb(r)) ** 2
    ok = bool(lhs > rhs)
    re_lo = (c.real - arb(r)).lower()
    return dict(ok=ok, centre_re=c.real.mid().str(40, radius=False), centre_im=c.imag.mid().str(40, radius=False),
                r=r, R=R, abs_f_c_upper=abs(f0).upper().str(5, radius=False),
                abs_df_c_lower=abs(d0).lower().str(10, radius=False), M_upper=M.str(10, radius=False),
                lhs_lower=lhs.str(10, radius=False), rhs_upper=rhs.str(10, radius=False),
                re_lower_bound=re_lo.str(25, radius=False),
                sigma_gt_1_certified=bool(ok and (c.real - arb(r)) > 1))


def lattice_check():
    import mpmath as mp
    mp.mp.dps = 30
    N = 400
    s = 3
    tot = mp.mpf(0)
    for m in range(-N, N + 1):
        for n in range(-N, N + 1):
            if m == 0 and n == 0:
                continue
            tot += mp.mpf(m * m + 5 * n * n) ** (-s)
    v = Z(acb(3))
    return dict(direct_truncated=mp.nstr(tot, 20), genus_hurwitz=v.str(20), truncation_bound_est='~pi/(2*sqrt5*N^4) ~ 1e-11')


def main():
    t0 = time.time()
    flint.ctx.prec = PREC
    res = dict(script='adj_epstein_rouche.py', prec_bits=PREC, versions=dict(python_flint=flint.__version__))
    res['identity_check_s3'] = lattice_check()
    certs = []
    for z in CANDIDATES:
        t1 = time.time()
        cert = certify(z)
        cert['candidate'] = [z.real, z.imag]
        cert['runtime_s'] = round(time.time() - t1, 1)
        certs.append(cert)
        print(cert, flush=True)
    res['certificates'] = certs
    res['runtime_s'] = round(time.time() - t0, 1)
    os.makedirs(sys.argv[1], exist_ok=True)
    fn = os.path.join(sys.argv[1], 'adj_epstein_rouche.json')
    with open(fn, 'w') as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps(res, indent=1))
    print(hashlib.sha256(open(fn, 'rb').read()).hexdigest(), fn)


if __name__ == '__main__':
    main()
