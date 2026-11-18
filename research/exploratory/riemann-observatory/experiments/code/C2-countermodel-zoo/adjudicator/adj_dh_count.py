#!/usr/bin/env python3
"""ADJUDICATOR (C2-countermodel-zoo), skeptic finding F6 / claim C2-04.  NUMERICAL-RIGOROUS (Arb).

Re-runs the completeness count for the Davenport-Heilbronn function with (i) an independently written
argument-principle routine whose boundary segments close EXACTLY at the corners (the skeptic's sk_wind.py leaves
an uncovered ~1.1e-16 gap at the corner -0.6 + i y1, because -0.6 + 2.2*(n/n) evaluates to -0.6000000000000001 in
binary floating point; this is why sk_lowbox.json reports a winding enclosure [1.70e-17 +/- 3.25e-20] that
excludes 0), with segment balls built as exact Arb hulls of the two endpoints, and (ii) the Hurwitz form of f
(the skeptic used the L-function form):
    f(s) = 5^{-s} [zeta(s,1/5) + k zeta(s,2/5) - k zeta(s,3/5) - zeta(s,4/5)],  k = (sqrt(10-2 sqrt5)-2)/(sqrt5-1).
Certificate: for each boundary segment S, an Arb enclosure F(S) excluding 0 in its real or imaginary part puts
F(S) in an open half-plane, so the continuous change of arg F along S equals Arg(F(b)/F(a)); the sum over the
closed boundary is 2 pi (number of zeros inside).  Critical-line zeros: certified sign changes of the real function
xi_f(1/2+it) = (5/pi)^{s/2} Gamma((s+1)/2) f(s) on a grid of step 0.005.
Usage: python3 adj_dh_count.py OUTDIR [T]
"""
import sys, os, json, time, hashlib
import flint
from flint import acb, arb

PREC = 96


def kappa():
    s5 = arb(5).sqrt()
    return ((10 - 2 * s5).sqrt() - 2) / (s5 - 1)


def make_f():
    K = kappa()
    coeffs = [(acb(1) / 5, 1), (acb(2) / 5, K), (acb(3) / 5, -K), (acb(4) / 5, -1)]
    l5 = acb(5).log()

    def f(s):
        tot = acb(0)
        for a, c in coeffs:
            tot += s.zeta(a) * c
        return (-s * l5).exp() * tot
    return f


def hull(a, b):
    re = arb(a.real).union(arb(b.real))
    im = arb(a.imag).union(arb(b.imag))
    return acb(re, im)


def excl0(B):
    return bool(B.real > 0 or B.real < 0 or B.imag > 0 or B.imag < 0)


def winding(F, x0, x1, y0, y1, nseg, maxdepth=18):
    C = [complex(x0, y0), complex(x1, y0), complex(x1, y1), complex(x0, y1)]
    stack = []
    for k in range(4):
        a, b = C[k], C[(k + 1) % 4]
        pts = [a + (b - a) * j / nseg for j in range(nseg)] + [b]          # last point is the exact corner
        # force exact coordinates along the edge (one coordinate is constant on an axis-parallel edge)
        if a.real == b.real:
            pts = [complex(a.real, p.imag) for p in pts]
        else:
            pts = [complex(p.real, a.imag) for p in pts]
        for j in range(nseg):
            stack.append((pts[j], pts[j + 1], 0))
    cache = {}

    def Fp(z):
        if z not in cache:
            cache[z] = F(acb(z.real, z.imag))
        return cache[z]
    total = arb(0)
    nev = 0
    while stack:
        a, b, d = stack.pop()
        B = F(hull(a, b)); nev += 1
        if excl0(B):
            total += (Fp(b) / Fp(a)).arg()
        else:
            if d >= maxdepth:
                return dict(ok=False, seg=[repr(a), repr(b)], nevals=nev)
            m = complex((a.real + b.real) / 2, (a.imag + b.imag) / 2)
            stack.append((a, m, d + 1)); stack.append((m, b, d + 1))
    w = total / (2 * arb.pi())
    n = round(float(w.mid()))
    ok = bool(w.contains(arb(n)) and w.rad() < 0.25)
    return dict(ok=ok, count=n, enclosure=w.str(20), nevals=nev)


def main():
    flint.ctx.prec = PREC
    T = float(sys.argv[2]) if len(sys.argv) > 2 else 300.0
    f = make_f()
    t0 = time.time()
    res = dict(script='adj_dh_count.py', prec_bits=PREC, python_flint=flint.__version__, T=T)
    res['low_box_[-0.6,1.6]x[-1,1]'] = winding(f, -0.6, 1.6, -1.0, 1.0, nseg=16)
    print(res, flush=True)
    res['box_[-0.6,1.6]x[1,T]'] = winding(f, -0.6, 1.6, 1.0, T, nseg=400)
    print(res, flush=True)
    l5pi = (acb(5) / acb.pi()).log()
    signs, unc = [], 0
    N = int(round((T - 1.0) / 0.005))
    for j in range(N + 1):
        t = 1.0 + 0.005 * j
        s = acb(0.5, t)
        v = ((l5pi * s / 2).exp() * ((s + 1) / 2).gamma() * f(s)).real
        if v > 0:
            signs.append(1)
        elif v < 0:
            signs.append(-1)
        else:
            unc += 1
    sc = sum(1 for a, b in zip(signs, signs[1:]) if a != b)
    res.update(line_sign_changes=sc, uncertified_points=unc, line_step=0.005,
               N_box_minus_line=res['box_[-0.6,1.6]x[1,T]'].get('count', -1) - sc,
               runtime_s=round(time.time() - t0, 1))
    print(res, flush=True)
    os.makedirs(sys.argv[1], exist_ok=True)
    fn = os.path.join(sys.argv[1], f'adj_dh_count_T{int(T)}.json')
    with open(fn, 'w') as fh:
        json.dump(res, fh, indent=1)
    print(hashlib.sha256(open(fn, 'rb').read()).hexdigest(), fn)


if __name__ == '__main__':
    main()
