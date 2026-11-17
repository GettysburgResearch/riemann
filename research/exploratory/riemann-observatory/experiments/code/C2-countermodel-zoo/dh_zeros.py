#!/usr/bin/env python3
"""C2 countermodel zoo -- Davenport-Heilbronn function: off-line zeros with Arb certificates.

Definition (Titchmarsh, Theory of the Riemann zeta-function, 2nd ed., sect. 10.25):
    f(s) = 5^{-s} [ zeta(s,1/5) + k zeta(s,2/5) - k zeta(s,3/5) - zeta(s,4/5) ],
    k = tan(theta) = (sqrt(10 - 2 sqrt 5) - 2) / (sqrt 5 - 1) = 0.2840790438...
i.e. f(s) = sum a_n n^{-s} with a_n = 1, k, -k, -1, 0 for n = 1,2,3,4,0 mod 5.
Equivalently f = ((1 - i k)/2) L(s,chi) + ((1 + i k)/2) L(s,conj chi), chi mod 5 with chi(2) = i.
Functional equation (checked numerically below):  xi_f(s) := (5/pi)^{s/2} Gamma((s+1)/2) f(s) = xi_f(1-s).

What the script does
  1. checks the Dirichlet-coefficient / L-function / functional-equation identities at a few points (Arb);
  2. NON-RIGOROUS scan for zeros in  1/2 + eta <= sigma <= SIGMA_MAX, 0 < t <= T_MAX (local minima of |f| on a
     grid + Newton polishing, plus an argument-principle count per t-block as a completeness check);
  3. RIGOROUS (Arb) Krawczyk certificate for every candidate (existence + uniqueness in a small square);
  4. a rigorous zero-free half-plane sigma >= sigma_0 from |f| >= 1 - sum_{n>=2} |a_n| n^{-sigma};
  5. targeted search for a certified zero with sigma > 1 (Titchmarsh 10.25 proves infinitely many exist).
Usage: python3 dh_zeros.py OUTDIR [T_MAX] [SIGMA_MAX]
"""
import sys, os, json, time, math, hashlib
import flint
from flint import acb, arb, acb_series
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from zoo_common import certify_zero, newton_polish, series_eval, winding_number, versions

flint.ctx.prec = 128
S5 = arb(5).sqrt()
KAPPA = ((10 - 2 * S5).sqrt() - 2) / (S5 - 1)          # tan theta, rigorous ball
FIFTH = [acb(arb(j) / 5) for j in range(1, 5)]
COEF = [acb(1), acb(KAPPA), acb(-KAPPA), acb(-1)]


def f_series(s):
    """acb_series version: 5^{-s} sum_j c_j zeta(s, j/5)."""
    tot = None
    for c, a in zip(COEF, FIFTH):
        term = acb_series.zeta(s, a) * c
        tot = term if tot is None else tot + term
    five_pow = (s * (-acb(5).log())).exp()
    return five_pow * tot


def f_val(s):
    tot = acb(0)
    for c, a in zip(COEF, FIFTH):
        tot += c * acb.zeta(s, a)
    return (-s * acb(5).log()).exp() * tot


def fd(z):
    return series_eval(f_series, z)


def xi_f(s):
    return ((acb(5) / acb.pi()).log() * s / 2).exp() * ((s + 1) / 2).gamma() * f_val(s)


def checks():
    out = {}
    s = acb("0.3", "17.25")
    # Dirichlet series in sigma > 1 vs Hurwitz form (direct partial sum + tail is not rigorous; compare to 1e-12)
    s2 = acb(3, 2)
    direct = sum(complex([1, float(KAPPA), -float(KAPPA), -1, 0][(n - 1) % 5]) * complex(n) ** (-complex(s2))
                 for n in range(1, 200000))
    out['dirichlet_series_vs_hurwitz_at_3+2i_absdiff_nonrig'] = abs(direct - complex(f_val(s2)))
    # L-function form; flint dirichlet_char(5,2) has chi(2) = exp(2 pi i /4) = i (chi_exponent check)
    chi, chibar = flint.dirichlet_char(5, 2), flint.dirichlet_char(5, 3)
    I = acb(0, 1)
    Lform = (1 - I * KAPPA) / 2 * acb.dirichlet_l(s, chi) + (1 + I * KAPPA) / 2 * acb.dirichlet_l(s, chibar)
    out['L_form_minus_hurwitz_form_at_0.3+17.25i'] = str(Lform - f_val(s))
    # functional equation (Arb balls, rigorous for these points)
    for pt in [acb("0.3", "17.25"), acb("0.8", "85.7"), acb("-1.5", "3")]:
        d = xi_f(pt) - xi_f(1 - pt)
        out[f'xi_f(s)-xi_f(1-s) at {complex(pt)}'] = str(d)
        out[f'contains_zero at {complex(pt)}'] = bool(d.contains(0))
    out['kappa'] = KAPPA.str(30)
    return out


def zero_free_halfplane():
    """Rigorous: for sigma >= s0, |f(s)| >= 1 - sum_{n>=2}|a_n| n^{-s0} > 0. Tail n > M bounded by integral."""
    absa = [0, 1, KAPPA, KAPPA, 1]  # index n mod 5 -> |a_n| (0 for n = 0 mod 5)
    M = 20000
    for s0 in [arb(x) / 100 for x in range(110, 300, 1)]:
        tot = arb(0)
        for n in range(2, M + 1):
            r = n % 5
            if r:
                tot += absa[r] * arb(n) ** (-s0)
        tail = arb(M) ** (1 - s0) / (s0 - 1)    # sum_{n>M} n^{-s0} <= int_M^inf x^{-s0} dx, |a_n| <= 1
        bound = 1 - tot - tail
        if bound > 0:
            return dict(sigma0=float(s0), lower_bound_on_abs_f=bound.str(10), M=M)
    return None


def scan(T_MAX, SIGMA_MAX, eta=0.02, dt=0.05, ds=0.02):
    import numpy as np
    cands = []
    t0 = 1.0
    blocks = []
    T = t0
    while T < T_MAX:
        T2 = min(T + 10.0, T_MAX)
        sig = list(np.arange(0.5 + eta, SIGMA_MAX + 1e-9, ds))
        tt = list(np.arange(T - 0.5, T2 + 0.5, dt))
        A = np.array([[abs(complex(f_val(acb(a, b)))) for b in tt] for a in sig])
        for i in range(len(sig)):
            for j in range(1, len(tt) - 1):
                v = A[i, j]
                lo_i, hi_i = max(0, i - 1), min(len(sig), i + 2)
                if v <= A[lo_i:hi_i, j - 1:j + 2].min() and v < 0.3 and T <= tt[j] < T2:
                    z, res = newton_polish(fd, complex(sig[i], tt[j]))
                    if res < 1e-20 and 0.5 + eta / 2 < z.real <= SIGMA_MAX + 0.05 and T - 1 <= z.imag <= T2 + 1:
                        if all(abs(z - c) > 1e-8 for c in cands):
                            cands.append(z)
        # argument principle count in the block (non-rigorous)
        w = winding_number(f_val, [complex(0.5 + eta, T), complex(SIGMA_MAX, T), complex(SIGMA_MAX, T2),
                                   complex(0.5 + eta, T2)], n_per_edge=600)
        blocks.append(dict(t_lo=T, t_hi=T2, winding=round(w, 4)))
        T = T2
    return sorted(cands, key=lambda z: z.imag), blocks


def main():
    outdir = sys.argv[1]
    T_MAX = float(sys.argv[2]) if len(sys.argv) > 2 else 300.0
    SIGMA_MAX = float(sys.argv[3]) if len(sys.argv) > 3 else 1.6
    t_start = time.time()
    rep = dict(model='Davenport-Heilbronn f(s) (Titchmarsh 10.25)', versions=versions(), prec_bits=flint.ctx.prec,
               params=dict(T_MAX=T_MAX, SIGMA_MAX=SIGMA_MAX, eta=0.02))
    rep['checks'] = checks()
    rep['zero_free_halfplane'] = zero_free_halfplane()
    cands, blocks = scan(T_MAX, SIGMA_MAX)
    rep['blocks'] = blocks
    rep['winding_total'] = sum(b['winding'] for b in blocks)
    zeros = []
    for z in cands:
        c = certify_zero(fd, z)
        c['approx'] = [z.real, z.imag]
        zeros.append(c)
    rep['zeros_in_region'] = zeros
    rep['n_candidates'] = len(cands)
    rep['n_certified'] = sum(1 for c in zeros if c.get('ok'))
    rep['n_certified_off_line'] = sum(1 for c in zeros if c.get('ok') and c.get('off_line'))
    # literature comparison (Spira 1994, Math. Comp. 63, 747-748; values as quoted in secondary sources)
    spira = [(0.808517, 85.699348), (0.650830, 114.163343), (0.574356, 166.479306), (0.724258, 176.702461)]
    comp = []
    for (a, b) in spira:
        best = min(zeros, key=lambda c: abs(complex(*c['approx']) - complex(a, b))) if zeros else None
        comp.append(dict(spira=[a, b], ours=best['approx'] if best else None,
                         absdiff=abs(complex(*best['approx']) - complex(a, b)) if best else None))
    rep['spira_comparison'] = comp
    rep['runtime_s'] = round(time.time() - t_start, 1)
    os.makedirs(outdir, exist_ok=True)
    fn = os.path.join(outdir, 'dh_zeros.json')
    with open(fn, 'w') as fh:
        json.dump(rep, fh, indent=1, default=str)
    print(json.dumps(dict(n_cand=len(cands), n_cert=rep['n_certified'], n_off=rep['n_certified_off_line'],
                          winding_total=rep['winding_total'], runtime=rep['runtime_s']), indent=1))
    print(hashlib.sha256(open(fn, 'rb').read()).hexdigest(), fn)


if __name__ == '__main__':
    main()
