#!/usr/bin/env python3
"""Exact bounded controls for PROOF.md; not a machine proof of its analytic limits.
Standard library only. No success gate depends on Python assert statements.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib
import itertools
import json
from math import comb, factorial, isqrt
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parent


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def natural(n: int) -> None:
    require(type(n) is int and n >= 0, "expected a nonnegative integer")


def trim(a):
    a = list(map(F, a))
    while len(a) > 1 and not a[-1]:
        a.pop()
    return tuple(a or [F(0)])


def add(a, b):
    return trim([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])


def scale(a, s):
    return trim([s*x for x in a])


def mul(a, b):
    out = [F(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return trim(out)


def derivative(a):
    return trim([i*a[i] for i in range(1, len(a))])


def evaluate(a, x):
    ans = F(0)
    for v in reversed(a):
        ans = ans*x+v
    return ans


def laguerre(n: int, argument_scale=F(1)):
    natural(n)
    return trim([F(comb(n, j), factorial(j))*(-argument_scale)**j
                 for j in range(n+1)])


def tail_polynomial(n: int):
    """I_n(U)=exp(-U/2)*P_n(U), by termwise integration of a finite polynomial."""
    natural(n)
    out = [F(0)]*(n+1)
    for j, a in enumerate(laguerre(n, F(2))):
        for k in range(j+1):
            out[k] += a*F(factorial(j), factorial(k))*2**(j-k+1)
    return trim(out)


def tail_from_generating(n: int):
    out = (F(0),)
    for k in range(n+1):
        dif = add(laguerre(k, F(2)),
                  scale(laguerre(k-1, F(2)), -1) if k else (F(0),))
        out = add(out, scale(dif, 2*(-3)**(n-k)))
    return out


def normalized_integral_moment(n: int, k: int):
    natural(n); natural(k)
    return sum((a*factorial(j+k)*2**(j+k+1)
                for j, a in enumerate(laguerre(n, F(2)))), F(0))/(2*(-3)**n)


def cumulant_moments(n: int, degree: int):
    natural(n); natural(degree)
    cumulants = [F(0)] + [factorial(k-1)*(n*(-1)**(k+1)*F(2, 3)**k
                                          +(n+1)*F(2)**k)
                                 for k in range(1, degree+1)]
    m = [F(1)]
    for r in range(1, degree+1):
        m.append(sum((comb(r-1, j-1)*cumulants[j]*m[r-j]
                      for j in range(1, r+1)), F(0)))
    return m


def log_unit_interval(x: F, terms: int):
    require(F(1) <= x <= F(2), "log reduction outside [1,2]")
    z = (x-1)/(x+1)
    partial = 2*sum((z**(2*j+1)/F(2*j+1) for j in range(terms)), F(0))
    error = 2*z**(2*terms+1)/(F(2*terms+1)*(1-z*z))
    return partial, partial+error


def log_interval(x: F, terms: int = 80):
    require(type(x) is F and x > 0, "log input must be a positive Fraction")
    require(type(terms) is int and terms >= 1, "invalid logarithm term count")
    y, power = x, 0
    while y < 1:
        y *= 2; power -= 1
    while y > 2:
        y /= 2; power += 1
    lo, hi = log_unit_interval(y, terms)
    l2, h2 = log_unit_interval(F(2), terms)
    if power >= 0:
        return lo+power*l2, hi+power*h2
    return lo+power*h2, hi+power*l2


def c_of_p(p):
    return (1+p)**2/(2*p)


def phi_interval(p):
    lo, hi = log_interval(p)
    q = (1+p)*(1-3*p)/(4*p)
    return -hi-q, -lo-q


def mu(n):
    require(type(n) is int and n >= 1, "mu requires a positive integer")
    v, d, sign = n, 2, 1
    while d*d <= v:
        if v % d == 0:
            v //= d; sign = -sign
            if v % d == 0:
                return 0
        d += 1
    return -sign if v > 1 else sign


def squarefree_direct(n):
    return all(n % (d*d) for d in range(2, isqrt(n)+1))


def strict_equal(a, b):
    if type(a) is not type(b):
        return False
    if isinstance(a, dict):
        return a.keys() == b.keys() and all(strict_equal(a[k], b[k]) for k in a)
    if isinstance(a, list):
        return len(a) == len(b) and all(strict_equal(x, y) for x, y in zip(a, b))
    return a == b


def no_duplicate_pairs(pairs):
    ans = {}
    for k, v in pairs:
        require(k not in ans, "duplicate JSON key")
        ans[k] = v
    return ans


def read_json(path):
    return json.loads(Path(path).read_text(), object_pairs_hook=no_duplicate_pairs)


def check_record(actual, expected):
    require(strict_equal(actual, expected), "saved result differs in type, coverage, or value")


def check_manifest(root: Path):
    lines = (root / 'SHA256SUMS').read_text().splitlines()
    named = set()
    for line in lines:
        parts = line.split('  ')
        require(len(parts) == 2, "bad manifest line")
        digest, name = parts
        require(len(digest) == 64 and all(c in '0123456789abcdef' for c in digest),
                "bad manifest hash")
        require(name and '/' not in name and '\\' not in name and name not in ('.', '..', 'SHA256SUMS'),
                "unsafe manifest path")
        require(name not in named, "duplicate manifest path")
        named.add(name)
        file = root / name
        require(file.is_file(), "missing manifest file")
        require(hashlib.sha256(file.read_bytes()).hexdigest() == digest,
                "manifest content mismatch: " + name)
    actual = {f.name for f in root.iterdir() if f.is_file() and f.name != 'SHA256SUMS'}
    require(named == actual, "manifest coverage mismatch")


def build_result():
    counts = {}
    def check(group, condition):
        require(bool(condition), 'control failure: '+group)
        counts[group] = counts.get(group, 0)+1

    # Independent finite integration vs. exact generating function.
    for n in range(25):
        p = tail_polynomial(n)
        check('integrated_generating_polynomial', p == tail_from_generating(n))
        check('tail_derivative_boundary',
              add(derivative(p), scale(p, F(-1, 2))) == scale(laguerre(n, F(2)), -1))
        check('complete_integral', p[0] == 2*(-3)**n)

    # Moments reconstructed independently from cumulants and monomial integrals.
    for n in range(13):
        cm = cumulant_moments(n, 4)
        for k in range(5):
            check('signed_measure_moments', cm[k] == normalized_integral_moment(n, k))
        check('mean_variance', cm[1] == F(8, 3)*n+2
              and cm[2]-cm[1]**2 == F(32, 9)*n+4)

    # Monic Jacobi characteristic recurrence, not a zero scan.
    older, current = (F(1),), (F(-1), F(1))
    check('jacobi_laguerre', current == scale(laguerre(1), -1))
    for n in range(2, 21):
        nxt = add(mul((F(-(2*n-1)), F(1)), current), scale(older, -(n-1)**2))
        check('jacobi_laguerre', nxt == scale(laguerre(n), (-1)**n*factorial(n)))
        older, current = current, nxt

    # Exact all-phase saddle algebra on rational cosine panels.
    for p in [F(1, 5), F(1, 8), F(1, 11), F(1, 20)]:
        c, beta = c_of_p(p), (1-p)/(1+p)
        check('saddle_stationarity', 2*c*p/(1+p)**2 == 1)
        check('saddle_curvature', 2*c*p*(1-p)/(1+p)**3 == beta)
        for h in [F(0), F(1, 4), F(1), F(3)]:
            cost = (1-h*h)/(1+h*h)
            direct = 2*c*(p/(1+p)-(p*cost+p*p)/(1+2*p*cost+p*p))
            gap = 2*c*p*(1-p)*(1-cost)/((1+p)*(1+2*p*cost+p*p))
            check('saddle_global_gap', direct == gap and gap >= beta*(1-cost))
        beta2 = 1-2*p/(1+p)
        alpha = (1-3*p)/(2*(1+p))
        check('arithmetic_exponent_gap', beta2 == beta and beta-alpha == F(1, 2))

    p = F(1, 11); alpha = (1-3*p)/(2*(1+p))
    check('rational_uniform_budget', alpha == F(1, 3))
    check('rational_uniform_budget', 1/(alpha*(1-p)) == F(33, 10))
    check('rational_uniform_budget', F(33, 10)**2/(1-p*p) < F(10, 3)**2)
    for n in range(1, 13):
        check('integer_cutoff_schedule', 1728**n == 12**(3*n))
        check('integer_cutoff_schedule', F(11, 12)**n == F(11**n, 12**n))
    p = F(1, 3); beta = (1-p)/(1+p)
    kp = 4/(1-p)+4/beta*(F(3, 2)/(1-p)+2*p/(1-p)**2)
    check('arithmetic_transfer_constant', kp == 36)

    # Strict critical-root certificate, analytic tails included.
    plo = F(81469666777975167, 10**18)
    phi = F(81469666777975168, 10**18)
    clo, chi = c_of_p(phi), c_of_p(plo)
    cdeclo, cdechi = F('7.17798836313058'), F('7.17798836313060')
    check('critical_interval', phi_interval(plo)[1] < 0)
    check('critical_interval', phi_interval(phi)[0] > 0)
    check('critical_interval', cdeclo < clo < chi < cdechi)
    check('critical_interval', F(8, 3) < cdeclo)
    check('critical_interval', 3*log_interval(F(12))[0] > cdechi)

    # Squarefree source is checked by two different finite definitions.
    for q in [2, 3, 67]:
        for x in [1, 2, 4, 17, 67, 128, 255, 512]:
            direct = sum(int(squarefree_direct(k) and k % q != 0) for k in range(1, x+1))
            inverse = sum(mu(d)*(x//(d*d)-x//(q*d*d))
                          for d in range(1, isqrt(x)+1) if d % q)
            check('squarefree_count_identity', direct == inverse)

    # Finite geometry controls: the one positive source maximizes all rows.
    for N in [1, 2, 4, 8]:
        for c in [F(3), F(4), F(8)]:
            nodes = [2*c*N+F(j+1, 2) for j in range(4)]
            matrix = [[F(1, j+2)*evaluate(laguerre(n), t)
                       for j, t in enumerate(nodes)] for n in range(N+1)]
            best = sum(sum(row)**2 for row in matrix)
            for signs in itertools.product([-1, 1], repeat=4):
                val = sum(sum(x*s for x, s in zip(row, signs))**2 for row in matrix)
                check('simultaneous_vector_extremizer', val <= best)
            for t in nodes:
                vs = [(-1)**n*evaluate(laguerre(n), t) for n in range(N+1)]
                check('degree_tail_domination', all(vs[n] >= (2*c-3)*vs[n-1] > 0
                                                  for n in range(1, N+1)))

    return {
        'status': 'PASS_BOUNDED_EXACT_CONTROLS',
        'arithmetic': 'EXACT_RATIONAL_WITH_LOG_SERIES_REMAINDERS',
        'counts': counts,
        'distinct_controls': sum(counts.values()),
        'critical_constant': {
            'p_lower': str(plo), 'p_upper': str(phi),
            'c_lower': str(cdeclo), 'c_upper': str(cdechi),
            'inequalities': 'strict', 'log_terms': 80,
        },
        'source_cutoff': '1728^N',
        'vector_error_bound': '(10/3)*(11/12)^N',
        'RH_proved': False,
        'analytic_limits_machine_proved': False,
        'actual_mobius_energy_evaluated': False,
    }


class RejectTests(unittest.TestCase):
    def test_known_tail(self):
        self.assertEqual(tail_polynomial(1), (F(-6), F(-4)))
    def test_negative_degree(self):
        self.assertRaises(ValueError, laguerre, -1)
    def test_boolean_degree(self):
        self.assertRaises(ValueError, laguerre, True)
    def test_bad_log_domain(self):
        self.assertRaises(ValueError, log_interval, F(0))
    def test_float_log_rejected(self):
        self.assertRaises(ValueError, log_interval, 1.0)
    def test_log_enclosure(self):
        lo, hi = log_interval(F(2))
        self.assertTrue(F(69, 100) < lo < hi < F(70, 100))
    def test_changed_result(self):
        self.assertRaises(ValueError, check_record, {'x': 2}, {'x': 1})
    def test_bool_alias(self):
        self.assertRaises(ValueError, check_record, {'x': True}, {'x': 1})
    def test_float_alias(self):
        self.assertRaises(ValueError, check_record, {'x': 1.0}, {'x': 1})
    def test_duplicate_json(self):
        self.assertRaises(ValueError, json.loads, '{"x":1,"x":2}', object_pairs_hook=no_duplicate_pairs)
    def test_missing_field(self):
        self.assertRaises(ValueError, check_record, {}, {'x': 1})
    def test_source_mutation(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d); (p/'a').write_text('original')
            digest = hashlib.sha256((p/'a').read_bytes()).hexdigest()
            (p/'SHA256SUMS').write_text(digest+'  a\n')
            check_manifest(p)
            (p/'a').write_text('changed')
            self.assertRaises(ValueError, check_manifest, p)
    def test_manifest_extra_file(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d); (p/'SHA256SUMS').write_text(''); (p/'extra').write_text('x')
            self.assertRaises(ValueError, check_manifest, p)
    def test_manifest_traversal(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d); (p/'SHA256SUMS').write_text('0'*64+'  ../a\n')
            self.assertRaises(ValueError, check_manifest, p)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', type=Path)
    parser.add_argument('--check', type=Path)
    parser.add_argument('--manifest', action='store_true')
    parser.add_argument('--self-test', action='store_true')
    args = parser.parse_args()
    require(not (args.write and args.check), 'choose --write or --check, not both')
    if args.self_test:
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(RejectTests)
        result = unittest.TextTestRunner(verbosity=2).run(suite)
        require(result.wasSuccessful(), 'unit/rejection test failure')
        return
    result = build_result()
    text = json.dumps(result, indent=2, sort_keys=True)+'\n'
    if args.write:
        args.write.write_text(text)
    if args.check:
        check_record(read_json(args.check), result)
    if args.manifest:
        check_manifest(ROOT)
    print(text, end='')


if __name__ == '__main__':
    main()
