"""C5 experiment E1: census of 'fake' curve zeta functions over F_q.

Question (function-field form of the Davenport-Heilbronn / Selberg-class obstruction): do the
formal properties
   (F1) rationality  Z(T) = P(T)/((1-T)(1-qT)),  P in Z[T], P(0)=1, deg P = 2g,
   (F2) curve functional equation  P(T) = q^g T^{2g} P(1/(qT)),
   (F3) Euler product over 'places' with nonnegative integer place counts,
        Z(T) = prod_{d>=1} (1-T^d)^{-B_d},  B_d in Z_{>=0} for ALL d >= 1,
imply RH (|alpha| = sqrt q)?  Answer: no; this script counts, for small (q,g), all P satisfying
(F1)-(F3) (certified for all d), split by RH true/false.

Parametrisation: every P with (F1)-(F2) is P(T) = T^g h(1/T + qT) with h monic in Z[x] of
degree g (report C5, Lemma C5-L0).  (F3) for all d forces max|alpha| <= q (Lemma C5-L1), hence
|x_i| <= q+1 and |c_k| <= binom(g,k) (q+1)^k for h(x) = sum_k c_k x^{g-k}.  Enumeration is
exhaustive in that box; pruning uses exact B_d, d <= k, which depend on c_1..c_k only.

Certification: B_d >= 0 for d <= D0 by exact integers; for d > D0 an explicit tail bound with
an Arb upper bound for max|alpha| < q (ff_common.positivity_all_degrees).  RH true/false is
decided with flint (exact-zero imaginary parts for real roots, Arb comparison with 2 sqrt q)
and, when undecided or for a random 5% audit sample, with sympy Sturm sequences (exact).
"""
import json, math, sys, time, random, hashlib, platform, os
from itertools import product
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import flint, sympy, numpy
from ff_common import (P_from_h, power_sums, place_counts, rh_exact, positivity_all_degrees,
                       weil_bound_first_violation, toeplitz_negative_witness, alpha_balls)

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'results',
                   'C5-function-field-transfer')


def B_prefix_ok(P, q, kmax):
    s, N, B = place_counts(P, q, kmax)
    return all(B[d] >= 0 for d in range(1, kmax + 1))


def rh_flint(hcoef, q):
    """Return True/False if decided by Arb, None if undecided."""
    roots = flint.fmpz_poly(hcoef).complex_roots()
    two_sqrt_q = 2 * flint.arb(q).sqrt()
    decided = True
    for z, m in roots:
        if z.imag != 0:          # flint returns exactly-zero imaginary part for real roots
            # non-real root: certainly violates (x_i must be real)
            if not z.imag.contains(0):
                return False
            decided = False
            continue
        a = abs(z.real)
        if a > two_sqrt_q:
            return False
        if not (a < two_sqrt_q):
            decided = False      # possible boundary x = +-2 sqrt q
    return True if decided else None


def census(q, g, audit_rate=0.05, seed=1):
    rng = random.Random(seed)
    bounds = [math.comb(g, k) * (q + 1) ** k for k in range(g + 1)]
    results = dict(q=q, g=g, enumerated_leaves=0, admissible=0, rh_true=0, rh_false=0,
                   undecided_positivity=0, rh_false_nonreal_x=0, rh_false_real_only=0,
                   audits=0, audit_mismatch=0, fakes=[], examples_rh_true=[])

    def rec(prefix):
        k = len(prefix)        # prefix = [c_0=1, c_1, ..., c_{k-1}]
        if k == g + 1:
            results['enumerated_leaves'] += 1
            h_desc = prefix            # descending: c_0 x^g + c_1 x^{g-1} + ...
            hcoef = list(reversed(h_desc))  # ascending
            P = P_from_h(hcoef, q)
            pos = positivity_all_degrees(P, q, g)
            if pos['status'] != 'positive_all_d':
                if pos['status'].startswith('undecided'):
                    results['undecided_positivity'] += 1
                    results.setdefault('undecided_list', []).append(dict(h_asc=hcoef, pos=pos))
                return
            results['admissible'] += 1
            rh = rh_flint(hcoef, q)
            audited = False
            if rh is None or rng.random() < audit_rate:
                rh_ex, nreal, nout = rh_exact(hcoef, q)
                if rh is not None:
                    results['audits'] += 1
                    if rh != rh_ex:
                        results['audit_mismatch'] += 1
                rh = rh_ex
                audited = True
            if rh:
                results['rh_true'] += 1
                if len(results['examples_rh_true']) < 3:
                    results['examples_rh_true'].append(dict(h_asc=hcoef, P_asc=P))
            else:
                results['rh_false'] += 1
                balls = alpha_balls(P)
                nonreal_x = any(z.imag != 0 for z, m in flint.fmpz_poly(hcoef).complex_roots())
                if nonreal_x:
                    results['rh_false_nonreal_x'] += 1
                else:
                    results['rh_false_real_only'] += 1
                mods = sorted(float(abs(z).mid()) for z in balls)
                s, N, B = place_counts(P, q, 6)
                kviol = weil_bound_first_violation(P, q, g, kmax=2000)
                Nwit, val = toeplitz_negative_witness(P, q, g, Nmax=60)
                results['fakes'].append(dict(h_asc=hcoef, P_asc=P, N1_6=N[1:], B1_6=B[1:],
                                             alpha_moduli_over_sqrtq=[m / math.sqrt(q) for m in mods],
                                             nonreal_x=nonreal_x, D0=pos['D0'],
                                             first_weil_bound_violation_k=kviol,
                                             first_indefinite_toeplitz_N=Nwit,
                                             certified_negative_value_upper=val))
            return
        b = bounds[k]
        for c in range(-b, b + 1):
            pre = prefix + [c]
            # prune: B_d >= 0 for d <= k depends only on c_1..c_k
            hpartial_desc = pre + [0] * (g + 1 - len(pre))
            P = P_from_h(list(reversed(hpartial_desc)), q)
            if not B_prefix_ok(P, q, k):
                continue
            rec(pre)

    rec([1])
    return results


def main():
    cases = [(q, 1) for q in [2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 25, 27, 32, 49]] + \
            [(q, 2) for q in [2, 3, 4, 5, 7, 8, 9]] + [(2, 3), (3, 3), (4, 3)]
    if len(sys.argv) > 1 and sys.argv[1] == 'quick':
        cases = [(2, 1), (9, 1), (2, 2), (3, 2)]
    t0 = time.time()
    allres = []
    for q, g in cases:
        t1 = time.time()
        r = census(q, g)
        r['runtime_s'] = round(time.time() - t1, 2)
        # keep file small: truncate fake list for large cases, keep summary stats
        nf = len(r['fakes'])
        if nf > 40:
            r['fakes_truncated_from'] = nf
            kv = [f['first_weil_bound_violation_k'] for f in r['fakes']]
            nw = [f['first_indefinite_toeplitz_N'] for f in r['fakes']]
            r['fake_stats'] = dict(max_first_weil_violation_k=max(x for x in kv if x is not None),
                                   max_first_indefinite_N=max(x for x in nw if x is not None),
                                   count_k_ge_2=sum(1 for x in kv if x and x >= 2),
                                   count_N_ge_3=sum(1 for x in nw if x and x >= 3))
            # keep the 40 'most hidden' fakes (largest first violation k)
            r['fakes'] = sorted(r['fakes'], key=lambda f: -(f['first_weil_bound_violation_k'] or 0))[:40]
        else:
            kv = [f['first_weil_bound_violation_k'] for f in r['fakes']]
            nw = [f['first_indefinite_toeplitz_N'] for f in r['fakes']]
            if kv:
                r['fake_stats'] = dict(max_first_weil_violation_k=max(x for x in kv if x is not None),
                                       max_first_indefinite_N=max(x for x in nw if x is not None),
                                       count_k_ge_2=sum(1 for x in kv if x and x >= 2),
                                       count_N_ge_3=sum(1 for x in nw if x and x >= 3))
        print(f"q={q} g={g}: leaves={r['enumerated_leaves']} admissible={r['admissible']} "
              f"RH-true={r['rh_true']} RH-false={r['rh_false']} (nonreal x: {r['rh_false_nonreal_x']}) "
              f"undecided={r['undecided_positivity']} audits={r['audits']} mismatch={r['audit_mismatch']} "
              f"stats={r.get('fake_stats')} t={r['runtime_s']}s", flush=True)
        allres.append(r)
    meta = dict(script='ff_fake_census.py', python=platform.python_version(), flint=flint.__version__,
                sympy=sympy.__version__, numpy=numpy.__version__, arb_prec_bits=flint.ctx.prec,
                total_runtime_s=round(time.time() - t0, 1), cases=cases)
    os.makedirs(OUT, exist_ok=True)
    fn = os.path.join(OUT, 'fake_census.json' if len(sys.argv) == 1 else 'fake_census_quick.json')
    with open(fn, 'w') as f:
        json.dump(dict(meta=meta, results=allres), f, indent=1, default=str)
    print('wrote', fn, hashlib.sha256(open(fn, 'rb').read()).hexdigest())


if __name__ == '__main__':
    main()
