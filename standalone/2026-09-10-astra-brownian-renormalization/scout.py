#!/usr/bin/env python3
"""NONCERTIFYING binary64 exploration of the explicit Brownian cascade.

No zeta oracle or supplied zero ordinates are used. Roots are local solver
outputs, not isolations, a census, or an RH test. See PROOF.md and VALIDATION.md.
Requires NumPy and SciPy. This script is not imported by the exact checker.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import json
import math
from pathlib import Path
import platform


def main() -> None:
    import numpy as np
    import scipy
    from numpy.polynomial.legendre import leggauss
    from scipy.optimize import root

    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--step', type=float, default=0.01)
    ap.add_argument('--angle', type=float, default=-1.4)
    ap.add_argument('--depth', type=int, default=20)
    ap.add_argument('--seed', choices=('upper', 'lower'), default='upper')
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    if not (0.002 <= args.step <= 0.04 and 0 <= args.depth <= 30):
        ap.error('step/depth outside this bounded scouting interface')
    if not (-math.pi / 2 < args.angle < -0.5):
        ap.error('this scout stays strictly in the Laplace half-plane')

    xmin, xmax = -40.0, 28.0
    h = args.step
    x = np.linspace(xmin, xmax, round((xmax-xmin)/h)+1)
    h = float(x[1]-x[0])
    t = np.exp(x + 1j*args.angle)
    idx = np.arange(len(x))
    offsets = np.arange(-5, 7)
    v, wg = leggauss(48)
    u, weights = (v+3)/2, wg/2
    shifts = 2*np.log(u)/h
    params = []
    for sh, wt in zip(shifts, weights):
        base = math.floor(-sh)
        frac = -sh-base
        cs = []
        for off in offsets:
            c = 1.0
            for other in offsets:
                if other != off:
                    c *= (frac-other)/(off-other)
            cs.append(c)
        params.append((base, np.array(cs), wt))

    order = 16
    moments = [Fraction(math.factorial(j) if args.seed == 'upper' else 1)
               for j in range(order+1)]

    def power_series(tt, mm):
        coeff = np.array([float(mm[j])/math.factorial(j)*(-1)**j
                          for j in range(order+1)])
        return (np.polynomial.polynomial.polyval(tt, coeff),
                np.polynomial.polynomial.polyval(tt, coeff*np.arange(order+1)))

    if args.seed == 'upper':
        L, D = 1/(1+t), -t/(1+t)**2
    else:
        L = np.exp(-t)
        D = -t*L

    def shift(a, k, derivative):
        ii = idx+k
        out = a[np.clip(ii, 0, len(a)-1)].copy()
        mask = ii < 0
        if np.any(mask):
            tt = np.exp(xmin+ii[mask]*h+1j*args.angle)
            vv = power_series(tt, moments)
            out[mask] = vv[int(derivative)]
        return out

    def iterate():
        ln, dn = np.zeros_like(L), np.zeros_like(D)
        for base, cs, wt in params:
            a, b = np.zeros_like(L), np.zeros_like(D)
            for off, c in zip(offsets, cs):
                a += c*shift(L, base+off, False)
                b += c*shift(D, base+off, True)
            ln += wt*a*a
            dn += 2*wt*a*b
        return ln, dn

    def next_moments(mm):
        out = [Fraction(1)]
        for j in range(1, order+1):
            aj = (1-Fraction(1, 2**(2*j-1)))/(2*j-1)
            out.append(aj*sum(Fraction(math.comb(j,k))*mm[k]*mm[j-k]
                              for k in range(j+1)))
        return out

    # Fixed, rounded search guesses; labels are guesses, NOT zero indices.
    guesses = [complex(.32,6.37), complex(.3,7.1), complex(.3,10.5),
               complex(.3,12.5), complex(.2,15.15)]
    records = []
    for depth in range(args.depth+1):
        small = abs(t) < 0.001
        L[small], D[small] = power_series(t[small], moments)
        integrand = -2*L*D
        # Complete finite polynomial integral over (-infinity,xmin).
        # Its omitted Taylor terms and the right tail are NOT certified here.
        sum_moments = [sum(Fraction(math.comb(j,k))*moments[k]*moments[j-k]
                           for k in range(j+1)) for j in range(order+1)]
        tail_coeff = [0.0]+[(-1)**(j+1)*float(sum_moments[j])/math.factorial(j-1)
                            for j in range(1,order+1)]
        def value(q):
            if not (-0.08 < q.real < 0.92 and 1 < q.imag < 18):
                return complex(1e5,1e5)
            value0 = np.trapezoid(np.exp(-q*x)*integrand, x)
            return value0 + sum(tail_coeff[j]*np.exp(1j*args.angle*j+(j-q)*xmin)/(j-q)
                                for j in range(1,order+1))
        panels = []
        for guess in guesses:
            def residual(yy):
                z = value(complex(*yy))
                return [float(z.real),float(z.imag)]
            rr = root(residual, [guess.real, guess.imag], tol=1e-10)
            q = complex(*rr.x)
            res = float(abs(value(q)))
            ok = bool(rr.success and res < 1e-8)
            panels.append({'guess':[guess.real,guess.imag], 'converged':ok,
                           'root':[q.real,q.imag] if ok else None,
                           'residual':res if ok else None})
        records.append({'depth':depth,'panels':panels})
        print(args.seed, depth, [p['root'] for p in panels], flush=True)
        if depth < args.depth:
            L,D = iterate()
            moments = next_moments(moments)

    # An independently reduced depth-one upper integral, no log-grid recursion.
    direct = []
    if args.seed == 'upper':
        for nodes in (96,160):
            z,w = leggauss(nodes)
            r,wr = (z+3)/2,w/2
            b,wb = (z+1)/2,w/2
            ell = np.log(1-b[None,:]+b[None,:]/r[:,None]**2)
            ww = wr[:,None]*(6*b*(1-b)*wb)[None,:]
            lr = np.log(2/r)
            def dval(q):
                factor = np.expm1((2-2*q)*lr)/(2-2*q)
                return np.sum(ww*factor[:,None]*np.exp(q*ell))
            def fun(yy):
                zz = dval(complex(*yy)); return [zz.real,zz.imag]
            sol = root(fun,[.32,6.37],tol=1e-11)
            q = complex(*sol.x)
            direct.append({'nodes_each':nodes,'converged':bool(sol.success),
                           'root':[q.real,q.imag],'residual':float(abs(dval(q)))})

    result = {'status':'EMPIRICAL_NOT_CERTIFIED','rh_proved':False,
              'seed':args.seed, 'depth':args.depth,'step':h,'angle':args.angle,
              'xmin':xmin,'xmax':xmax,'grid_points':len(x),'u_gauss_nodes':48,
              'interpolation_nodes':12,'series_order':order,
              'python':platform.python_version(),'numpy':np.__version__,
              'scipy':scipy.__version__,'records':records,
              'direct_upper_depth_one':direct}
    args.out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n',encoding='utf-8')

if __name__ == '__main__':
    main()
