"""Exact controls and a source-bound interval certificate for pass4.
The infinite PNT/CLT/inertia proofs remain human mathematical arguments.
Standard library only. No assert-based acceptance. No float acceptance.
"""
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json
import re
import sys
import tempfile
import unittest

HERE = Path(__file__).resolve().parent
LOCKS = {
    'pass2/source_certificate.py': '128df4f27cc62683a58ef74c1f374910db13b507208e00535df3e1c9a9b3c6e5',
    'pass3/source_moments.py': '1d7b36a0bfc3abca254912aaa5756fe24b7b3180aea2a1fc9edf6c51b830ce4d',
}

def require(ok, message):
    if not ok:
        raise ArithmeticError(message)


def locked_bytes(path, expected):
    data = path.read_bytes()
    if hashlib.sha256(data).hexdigest() != expected:
        raise ValueError('source hash mismatch: ' + str(path))
    return data


def load_parent():
    for name, sha in LOCKS.items():
        locked_bytes(HERE.parent / name, sha)
    p = HERE.parent / 'pass3/source_moments.py'
    spec = importlib.util.spec_from_file_location('locked_pass3_moments_p4', p)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def mul(a, b, n):
    return [sum((a[k]*b[j-k] for k in range(j+1)), F(0)) for j in range(n+1)]


def inv(a, n):
    if a[0] == 0:
        raise ValueError('zero series constant')
    b = [1/a[0]]
    for j in range(1, n+1):
        b.append(-sum((a[k]*b[j-k] for k in range(1, j+1)), F(0))/a[0])
    return b


def exp_zero(a, n):
    if a[0] != 0:
        raise ValueError('exponential requires zero constant')
    b = [F(1)]
    for j in range(1, n+1):
        b.append(sum((k*a[k]*b[j-k] for k in range(1, j+1)), F(0))/j)
    return b


def sqrt_series(a, root, n):
    if root*root != a[0] or root == 0:
        raise ValueError('incorrect nonzero square root')
    out = [F(root)]
    for j in range(1, n+1):
        out.append((a[j]-sum((out[k]*out[j-k] for k in range(1, j)), F(0)))/(2*root))
    return out


def transpose(a):
    return [list(r) for r in zip(*a)]


def matmul(a, b):
    bt = transpose(b)
    return [[sum((x*y for x, y in zip(r, c)), F(0)) for c in bt] for r in a]


def det(a):
    a = [list(row) for row in a]
    out = F(1)
    for j in range(len(a)):
        k = next((k for k in range(j, len(a)) if a[k][j]), None)
        if k is None:
            return F(0)
        if k != j:
            a[k], a[j] = a[j], a[k]
            out = -out
        pivot = a[j][j]
        out *= pivot
        for k in range(j+1, len(a)):
            ratio = a[k][j]/pivot
            for ell in range(j+1, len(a)):
                a[k][ell] -= ratio*a[j][ell]
    return out


def degree_bound(x):
    if type(x) is not int or x < 2:
        raise ValueError('integer cutoff >=2 required')
    q = F(16,17)
    factor = 36*(9+8*x)
    n, v = 1, q
    while factor*v >= 1:
        n += 1
        v *= q
    return n


def exact_controls():
    counts = {}
    def check(group, statement):
        require(statement, group + ' failed')
        counts[group] = counts.get(group, 0) + 1
    n = 14
    rad = [F(9), F(-8)] + [F(0)]*(n-1)
    r = sqrt_series(rad, F(3), n)
    ri = inv(r, n)
    g = [(F(3) if j == 0 else F(0))-r[j] for j in range(n+1)]
    g = [v/2 for v in g]
    h = [(F(1) if j == 0 else F(0))/2+ri[j]/2 for j in range(n+1)]
    d = inv([F(1)-g[0]/2]+[-v/2 for v in g[1:]], n)
    for j in range(n+1):
        check('sqrt_and_pgf', mul(r,r,n)[j] == rad[j])
        check('sqrt_and_pgf', g[j] >= 0 and h[j] >= 0 and d[j] >= 0)
        check('cdf_boundary_identity', d[j] == 1-sum(g[:j+1]))
    for y in [F(0), F(1,2), F(1), F(3), F(10)]:
        ftilde = mul(h, exp_zero([y*v for v in g], n), n)
        rhs = mul(d, ftilde, n)
        # With e^-y suppressed, -(d/dy)CDF equals cumulative (1-g)F.
        diff = mul([1-g[0]]+[-v for v in g[1:]], ftilde, n)
        for j in range(n+1):
            check('cdf_boundary_identity', rhs[j] == sum(diff[:j+1]))
            check('pgf_positivity', ftilde[j] >= 0)
    # Exact Taylor expansions about z=1 determine factorial moments.
    rr = sqrt_series([F(1), F(-8), F(0), F(0)], F(1), 3)
    gg = [(F(3) if j == 0 else F(0))-rr[j] for j in range(4)]
    gg = [v/2 for v in gg]
    hh = inv(rr,3)
    hh = [(F(1) if j == 0 else F(0))/2+hh[j]/2 for j in range(4)]
    jump = [gg[1], 2*gg[2]+gg[1], 6*gg[3]+6*gg[2]+gg[1]]
    check('distribution_moments', jump == [F(2),F(10),F(122)])
    check('distribution_moments', hh[1] == 2)
    check('distribution_moments', 2*hh[2]+hh[1]-hh[1]**2 == 22)
    for x in [2,4,10,100,1000,10**6]:
        k = degree_bound(x)
        check('explicit_cutoff_bound', 36*(9+8*x)*F(16,17)**k < 1)
        check('explicit_cutoff_bound', 36*(9+8*x)*F(16,17)**(k-1) >= 1)
    for size in range(3,10):
        # Synthetic, not an actual-prime matrix: two exponential moments annihilated.
        cosh = [[(F(2)**(i-j)+F(2)**(j-i))/2 for j in range(size)] for i in range(size)]
        decay = [[F(2)**(-abs(i-j)) for j in range(size)] for i in range(size)]
        v = [[F(1) if i in (j,j+2) else F(-5,2) if i == j+1 else F(0)
              for j in range(size-2)] for i in range(size)]
        zero = matmul(transpose(v), matmul(cosh,v))
        check('synthetic_rank_two_inertia', all(x == 0 for row in zero for x in row))
        positive = matmul(transpose(v), matmul(decay,v))
        for k in range(1,size-1):
            check('synthetic_rank_two_inertia', det([row[:k] for row in positive[:k]]) > 0)
    # Standard Laguerre generating function, in rational finite coefficients.
    for t in [F(0),F(1,2),F(1),F(2),F(5)]:
        a = [F(0)]+[-t]*n
        ex = exp_zero(a,n)
        for j in range(n+1):
            poly = sum((F(comb(j,k),factorial(k))*(-t)**k for k in range(j+1)),F(0))
            check('laguerre_generating', poly == sum(ex[:j+1]))
    check('reciprocal_residue', F(2)/(1+F(1,3))**2 == F(9,8))
    check('reciprocal_residue', (F(8,9)/F(4,3))*3 == 2)
    check('full_source_uniform_square', F(1,50)-F(5,78)*(F(2,8)+F(1,64)) > 0)
    return counts, {str(x):degree_bound(x) for x in [2,4,10,100,1000,10**6]}


def source_certificate():
    mod = load_parent()
    p, _ = mod.source_moments()
    old = mod.mod
    gamma, _, _, pi, z3 = old.constants()
    lnpi, ln2 = old.log_ball(pi), old.log_rational(F(2))
    g0 = -(gamma+lnpi)/2-ln2/4
    g1 = pi**2/24+ln2**2/4
    g2 = -z3/4-ln2**3/4
    truncated = F(11,81)*g0+F(8,27)*g1+F(2,27)*g2
    full1 = p[0]-4*p[1]+4*p[2]
    full2 = p[0]-8*p[2]+16*p[4]
    d2 = (gamma+lnpi+ln2/2)/3
    balanced_trace = F(1,2)+g0/3-F(1,6)
    checks = {
        'full_m0_gt_one_fiftieth':p[0].lo > F(1,50),
        'full_m0_lt_one_fortieth':p[0].hi < F(1,40),
        'full_sparse_square_n1_positive':full1.lo > 0,
        'full_sparse_square_n2_positive':full2.lo > 0,
        'cutoff_X2_sparse_square_n1_negative':truncated.hi < F(-1,100),
        'operator_cutoff_residual_D2_positive':d2.lo > 0,
        'balanced_cutoff_X2_trace_negative':balanced_trace.hi < 0,
        'safe_xi_value_less_than_four_thirds':(2*pi/5).hi < F(4,3),
    }
    require(all(checks.values()), 'actual interval certificate failed')
    intervals = { 'full_m0':p[0].decimal(), 'full_sparse_square_n1':full1.decimal(),
        'full_sparse_square_n2':full2.decimal(), 'cutoff_X2_sparse_square_n1':truncated.decimal(),
        'operator_residual_D2':d2.decimal(), 'balanced_cutoff_X2_trace':balanced_trace.decimal() }
    return checks, intervals


def reconstruct():
    counts, bounds = exact_controls()
    checks, intervals = source_certificate()
    counts['source_interval_signs'] = len(checks)
    return {'status':'PASS_PASS4_TRUNCATION_CONTROLS', 'arithmetic':'EXACT_RATIONAL_AND_SOURCE_BOUND_INTERVAL',
            'counts':counts, 'total_distinct_controls':sum(counts.values()),
            'source_checks':checks, 'source_intervals':intervals, 'explicit_degree_bounds':bounds,
            'parent_sha256':LOCKS, 'RH_proved':False, 'full_source_Hankel_PSD_proved':False,
            'infinite_analytic_proofs_machine_checked':False}


def parse_json(text):
    def pairs(items):
        out = {}
        for k,v in items:
            if k in out:
                raise ValueError('duplicate JSON key')
            out[k] = v
        return out
    return json.loads(text, object_pairs_hook=pairs)


def strict_equal(a,b):
    if type(a) is not type(b):
        return False
    if type(a) is dict:
        return a.keys()==b.keys() and all(strict_equal(a[k],b[k]) for k in a)
    if type(a) is list:
        return len(a)==len(b) and all(strict_equal(x,y) for x,y in zip(a,b))
    return a==b


def manifest_check(root):
    manifest = root/'SHA256SUMS'
    lines = manifest.read_text().splitlines()
    seen = set()
    for line in lines:
        match = re.fullmatch(r'([0-9a-f]{64})  ([A-Za-z0-9_.-]+)', line)
        if not match:
            raise ValueError('invalid manifest entry')
        sha,name = match.groups()
        if name in seen or name == 'SHA256SUMS':
            raise ValueError('duplicate/self manifest entry')
        seen.add(name)
        locked_bytes(root/name,sha)
    actual = {p.name for p in root.iterdir() if p.is_file() and p.name != 'SHA256SUMS'}
    if actual != seen:
        raise ValueError('manifest coverage mismatch')


class Tests(unittest.TestCase):
    def test_bool_alias(self):
        self.assertFalse(strict_equal({'n':1},{'n':True}))
    def test_float_alias(self):
        self.assertFalse(strict_equal({'n':1},{'n':1.0}))
    def test_duplicate_json(self):
        with self.assertRaisesRegex(ValueError,'duplicate'):
            parse_json('{"a":1,"a":2}')
    def test_bad_cutoff(self):
        for x in [True,1,1.5,'2']:
            with self.assertRaises(ValueError): degree_bound(x)
    def test_bad_square_root(self):
        with self.assertRaises(ValueError): sqrt_series([F(9),F(-8)],F(2),1)
    def test_source_corruption(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'x';p.write_bytes(b'new')
            with self.assertRaisesRegex(ValueError,'source hash'):
                locked_bytes(p,hashlib.sha256(b'old').hexdigest())
    def test_missing_manifest_coverage(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); (root/'x').write_text('x');(root/'SHA256SUMS').write_text('')
            with self.assertRaisesRegex(ValueError,'coverage'):
                manifest_check(root)
    def test_changed_result(self):
        self.assertFalse(strict_equal({'RH_proved':False},{'RH_proved':True}))


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--write',action='store_true')
    parser.add_argument('--check',type=Path)
    parser.add_argument('--manifest',action='store_true')
    parser.add_argument('--self-test',action='store_true')
    args=parser.parse_args()
    if args.self_test:
        suite=unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
        ok=unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful()
        if not ok: raise SystemExit(1)
        return
    result=reconstruct()
    text=json.dumps(result,sort_keys=True,indent=2)+'\n'
    path=args.check or HERE/'RESULTS.json'
    if args.write:
        path.write_text(text)
    else:
        saved=parse_json(path.read_text())
        if not strict_equal(result,saved):
            raise SystemExit('reconstructed result mismatch')
    if args.manifest: manifest_check(HERE)
    print(text,end='')


if __name__=='__main__':
    main()
