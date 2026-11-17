#!/usr/bin/env python3
"""C2 countermodel zoo -- explicit continuous Beurling system with an Euler product and an off-line zero.

System (in the extended/continuous sense of Beurling; cf. Diamond-Zhang 2016, Broucke-Debruyne-Revesz 2023):
    dPi(x) = [ (1 - 1/x)/log x  -  2 Re(x^{rho-1}) 1_{x >= x0} / log x ] dx,     x >= 1,  rho = beta + i gamma.
    zeta_Pi(s) := exp( int_1^inf x^{-s} dPi(x) ) = s/(s-1) * exp( -E1((s-rho)L) - E1((s-conj rho)L) ),  L = log x0.
Since exp(-E1(w)) = e^{gamma_E} w exp(-Ein(w)) with Ein entire, zeta_Pi is meromorphic on C with a simple pole at 1,
simple zeros exactly at 0, rho, conj rho and no other zeros or poles.
dPi >= 0 iff 1 - 1/x >= 2 x^{beta-1} cos(gamma log x) for x >= x0; sufficient: 1 - 1/x0 >= 2 x0^{beta-1}.
This script: (1) certifies the sufficient positivity condition in Arb for the chosen (beta, x0);
(2) checks the Mellin identity numerically (mpmath quad, NON-RIGOROUS) at a few s with Re s > 1;
(3) evaluates zeta_Pi at rho (exactly 0 by the closed form) and at nearby points (Arb);
(4) records A = exp(-2 Re E1((1-rho)L)) (density of the integers) and the exact Chebyshev function
    psi(x) = x - 1 - log x - 2 Re((x^rho - x0^rho)/rho)  for x >= x0.
Usage: python3 beurling_toy.py OUTDIR
"""
import sys, os, json, time, hashlib
import mpmath as mp
import flint
from flint import acb, arb
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from zoo_common import versions

flint.ctx.prec = 128
CASES = [dict(beta="0.75", gamma="10", x0=32), dict(beta="0.6", gamma="25", x0=16)]


def E1(w):
    """Exponential integral E1(w) = Gamma(0, w) (principal branch), Arb."""
    return w.gamma_upper(0)


def zeta_entire_form(s, beta, gamma, x0):
    """s/(s-1) * prod_{r in {rho, conj rho}} e^{gamma_E} (s-r)L exp(-Ein((s-r)L)), Ein(w) = E1(w)+gamma_E+log w.
    Evaluated through E1 away from w = 0; at w = 0 the factor is 0 exactly."""
    rho = acb(arb(beta), arb(gamma)); L = acb(x0).log()
    out = s / (s - 1)
    for r in (rho, rho.conjugate()):
        w = (s - r) * L
        if w.is_zero():
            return acb(0)
        out *= (-E1(w)).exp()
    return out


def main():
    outdir = sys.argv[1]
    t0 = time.time()
    rep = dict(model='continuous Beurling system with zeros at rho, conj rho', versions=versions(), cases=[])
    mp.mp.dps = 25
    for C in CASES:
        beta, gamma, x0 = C['beta'], C['gamma'], C['x0']
        rec = dict(C)
        # (1) positivity certificate
        lhs = 1 - arb(1) / x0
        rhs = 2 * arb(x0) ** (arb(beta) - 1)
        rec['positivity_lhs_minus_rhs'] = (lhs - rhs).str(15)
        rec['positivity_certified'] = bool(lhs > rhs)
        # (2) Mellin identity check, NON-RIGOROUS (mpmath)
        rho = mp.mpc(beta, gamma); L = mp.log(x0)
        chk = []
        for s in [mp.mpc(2, 0), mp.mpc(1.5, 3), mp.mpc(3, 11)]:
            lhs_int = mp.quad(lambda v: mp.e ** (-(s - 1) * v) * (1 - mp.e ** (-v)) / v, [0, 1, 10, mp.inf])  # x = e^v
            corr = mp.quad(lambda v: -2 * mp.re(mp.e ** ((rho - 1) * v)) * mp.e ** (-(s - 1) * v) / v,
                           [L, L + 5, L + 50, mp.inf])
            closed = mp.log(s / (s - 1)) - mp.e1((s - rho) * L) - mp.e1((s - mp.conj(rho)) * L)
            chk.append(dict(s=str(s), quad=str(lhs_int + corr), closed=str(closed),
                            absdiff=float(abs(lhs_int + corr - closed))))
        rec['mellin_identity_checks'] = chk
        # (3) zeta at rho and nearby (Arb)
        r = acb(arb(beta), arb(gamma))
        rec['zeta_at_rho'] = str(zeta_entire_form(r, beta, gamma, x0))
        rec['zeta_near_rho_+1e-6'] = str(zeta_entire_form(r + acb("1e-6"), beta, gamma, x0))
        rec['zeta_at_2'] = str(zeta_entire_form(acb(2), beta, gamma, x0))
        # (4) density A
        A = (-2 * E1((1 - r) * acb(x0).log()).real).exp()
        rec['integer_density_A'] = A.str(20)
        rep['cases'].append(rec)
        print(json.dumps(rec, indent=1, default=str), flush=True)
    rep['runtime_s'] = round(time.time() - t0, 1)
    os.makedirs(outdir, exist_ok=True)
    fn = os.path.join(outdir, 'beurling_toy.json')
    json.dump(rep, open(fn, 'w'), indent=1, default=str)
    print(hashlib.sha256(open(fn, 'rb').read()).hexdigest(), fn)


if __name__ == '__main__':
    main()
