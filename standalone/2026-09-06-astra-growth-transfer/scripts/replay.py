#!/usr/bin/env python3
"""Bounded exact arithmetic replay. It does not establish any unbounded estimate."""
from __future__ import annotations
import argparse
import hashlib
import json
import sys
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = 'gt26-exact-transfer-v1'
SCOPE = {'arithmetic_limit': 96, 'operator_limit': 81, 'cutoff_limit': 32,
         'dual_limit': 32, 'dictionary_limit': 48}
INVENTORY = {'PROOF.md', 'README.md', 'SOURCES.md', 'SOURCE_LOCK.json',
             'VALIDATION.md', 'scripts/replay.py', 'scripts/test_replay.py',
             'verification.json'}
PARENT_SHA256 = {
 '2026-09-06-astra-dilation-observability/PROOF.md':
 'be2fbf1f146c412cfdda0cfd9c613a4beb88c7b77191c4eb2af3e769c6d71b22',
 # Replaced with the authenticated parent digest during packet assembly.
 '2026-09-06-astra-block-gain/PROOF.md': '4843591a9cf21122d5b0e695d3d93c93f53ba89ba542a77a994d67672d07078a'}


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def integer(n: object, low: int = 0) -> int:
    if type(n) is not int or n < low:
        raise TypeError('exact integer required, not bool/float')
    return n


def exact(x: object) -> F:
    if type(x) is int or type(x) is F:
        return F(x)
    raise TypeError('exact rational required')


@lru_cache(maxsize=None)
def factors(n: int) -> tuple[tuple[int, int], ...]:
    integer(n, 1)
    ans, p = [], 2
    while p*p <= n:
        r = 0
        while n % p == 0:
            n //= p
            r += 1
        if r:
            ans.append((p, r))
        p += 1
    if n > 1:
        ans.append((n, 1))
    return tuple(ans)


def mu(n: int) -> int:
    fs = factors(n)
    return 0 if any(r > 1 for _, r in fs) else (-1)**len(fs)


def divisors(n: int) -> list[int]:
    integer(n, 1)
    return [d for d in range(1, n+1) if n % d == 0]


def j2(n: int) -> int:
    out = n*n
    for p, _ in factors(n):
        out = out // (p*p) * (p*p-1)
    return out


def phi(n: int) -> int:
    out = n
    for p, _ in factors(n):
        out = out // p * (p-1)
    return out


# Exact polynomial algebra of commuting dilations: D_i D_j = D_(ij).
Poly = dict[int, F]
ONE: Poly = {1: F(1)}


def clean(a: Poly) -> Poly:
    return {integer(k, 1): exact(v) for k, v in sorted(a.items()) if v}


def add(a: Poly, b: Poly) -> Poly:
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, F(0)) + v
    return clean(out)


def scale(a: Poly, b: F | int) -> Poly:
    return clean({k: v*exact(b) for k, v in a.items()})


def mul(a: Poly, b: Poly) -> Poly:
    out: Poly = {}
    for k, v in a.items():
        for ell, w in b.items():
            out[k*ell] = out.get(k*ell, F(0)) + v*w
    return clean(out)


def power(a: Poly, r: int) -> Poly:
    integer(r)
    out = ONE
    for _ in range(r):
        out = mul(out, a)
    return out


def prime_operator(p: int) -> Poly:
    require(factors(p) == ((p, 1),) and p > 2, 'odd prime required')
    return {1: F(1, p*p-1), p: -F(p*p, p*p-1)}


@lru_cache(maxsize=None)
def op(kind: str, n: int) -> Poly:
    integer(n, 1)
    require(kind in {'T', 'U', 'V', 'B'}, 'bad operator kind')
    if n % 2 == 0:
        return {}
    out = ONE
    for p, r in factors(n):
        pp = prime_operator(p)
        if kind == 'T':
            local = pp if r == 1 else {}
        elif kind == 'B':
            local = {p: F(-1)} if r == 1 else {}
        elif kind == 'U':
            local = {p**(r-1): F(1, p*p-1), p**r: -F(1, p*p-1)}
        else:
            local = scale(mul({1: F(1), p: F(-1)},
                              power(scale(pp, -1), r-1)), -F(1, p*p-1))
        out = mul(out, local)
    return out


def conv(a: str, b: str, n: int) -> Poly:
    out: Poly = {}
    for d in divisors(n):
        out = add(out, mul(op(a, d), op(b, n//d)))
    return out


def partial(kind: str, n: int) -> Poly:
    out: Poly = {}
    for k in range(1, n+1):
        out = add(out, op(kind, k))
    return out


def raw(n: int, odd: bool = False) -> Poly:
    return {k: F(mu(k)) for k in range(1, n+1)
            if (not odd or k % 2) and mu(k)}


def a_hat(k: int, n: int) -> F:
    """a_(k,n) / (8/pi^2), calculated from the primitive divisor formula."""
    require(k % 2 == 1 and 1 <= k <= n, 'invalid odd index')
    return k*k*sum((F(mu(ell//k)*mu(ell), j2(ell))
                   for ell in range(k, n+1, k) if ell % 2), F(0))


def value(a: Poly, t: F) -> F:
    """Evaluate sum a_k {t/k}; no tail or floating-point approximation."""
    t = exact(t)
    return sum((v*(t/k - (t/k).__floor__()) for k, v in a.items()), F(0))


def specialization(a: Poly, weight: int) -> F:
    return sum((v/F(k)**weight for k, v in a.items()), F(0))


def m0(n: int, odd: bool = False) -> F:
    return sum((F(mu(k), k) for k in range(1, n+1)
                if not odd or k % 2), F(0))


def dual(q: int) -> dict[int, F]:
    out: dict[int, F] = {}
    for d in divisors(q):
        v = mu(q//d)
        if d > 1:
            out[d-1] = out.get(d-1, F(0)) + v*d*(d-1)
        out[d] = out.get(d, F(0)) - v*d*(d+1)
    return clean(out)


def h(k: int, n: int) -> F:
    return F(n % k, k)


def poly_record(a: Poly) -> list[list[object]]:
    return [[k, v.numerator, v.denominator] for k, v in sorted(a.items())]


def qrecord(q: F) -> list[int]:
    return [q.numerator, q.denominator]


def compute(scope: dict[str, int] | None = None) -> dict[str, object]:
    scope = dict(SCOPE) if scope is None else scope
    require(type(scope) is dict and set(scope) == set(SCOPE), 'bad coverage keys')
    for key, val in SCOPE.items():
        require(type(scope[key]) is int and scope[key] == val,
                'coverage must equal the fixed nonempty scope')
    counts: Counter[str] = Counter()
    def check(name: str, ok: bool) -> None:
        require(ok, name)
        counts[name] += 1

    # Independent elementary Mobius recursion, separate from prime factorization.
    mm = {1: 1}
    for n in range(2, scope['arithmetic_limit']+1):
        mm[n] = -sum(mm[d] for d in range(1, n) if n % d == 0)
    for n in range(1, scope['arithmetic_limit']+1):
        check('primitive_mobius', mu(n) == mm[n])
        check('jordan_divisor_identity', sum(j2(d) for d in divisors(n)) == n*n)
        check('mobius_floor_identity', sum(mu(d)*(n//d) for d in range(1, n+1)) == 1)
        check('harmonic_mobius_bound', abs(m0(n)) <= 1)
        check('odd_harmonic_bound', abs(m0(n, True)) <= 2)
        check('odd_harmonic_recursion', m0(n) == m0(n, True)-m0(n//2, True)/2)
        total, two = F(0), 1
        while two <= n:
            total += m0(n//two)/two
            two *= 2
        check('odd_harmonic_inverse', total == m0(n, True))
        for eps in (0, 1, 2):
            damped = sum((F(mu(k), k**(eps+1)) for k in range(1, n+1)), F(0))
            check('damped_harmonic_bound', abs(damped) <= 1)

    for n in range(1, scope['operator_limit']+1):
        check('operator_forward', conv('U', 'B', n) == op('T', n))
        check('operator_inverse', conv('V', 'T', n) == op('B', n))
        check('operator_unit', conv('U', 'V', n) == (ONE if n == 1 else {}))
        check('scalar_u_positive', specialization(op('U', n), 1) >= 0)
        check('scalar_total_mobius', specialization(op('T', n), 0) ==
              (mu(n) if n % 2 else 0))

    # The initial horizon is exact; a finite horizon is not global norm convergence.
    for n in range(1, scope['cutoff_limit']+1):
        rr = raw(n)
        for j in range(0, n+1):
            t = F(2*j+1, 2)
            check('raw_exact_initial_horizon', value(rr,t)+int(t>=1) == t*m0(n))
        b = sum(mu(k)*(n//k) for k in range(1,n+1,2))
        check('dyadic_staircase_identity', b == n.bit_length())
    for depth in range(0,17):
        norm = sum((F(1,2**max(i,j)) for i in range(depth+1) for j in range(depth+1)),F(0))
        check('staircase_norm_partial_sum', norm == 6-F(2*depth+5,2**depth))
    check('initial_horizon_does_not_remove_tail', value(raw(2),F(7,2))+1 != F(7,2)*m0(2))

    records = []
    for n in range(1, scope['cutoff_limit']+1):
        ah = {k: a_hat(k, n) for k in range(1, n+1, 2)}
        sp = clean(ah)
        check('optimizer_from_operator', sp == partial('T', n))
        forward: Poly = {}
        inverse: Poly = {}
        for d in range(1, n+1):
            forward = add(forward, mul(op('U', d), raw(n//d, True)))
            inverse = add(inverse, mul(op('V', d), partial('T', n//d)))
        check('cutoff_forward', sp == forward)
        check('cutoff_inverse', raw(n, True) == inverse)
        aa = sum((v/k for k, v in ah.items()), F(0))
        check('signed_normalization_identity', aa == sum(
            (F(mu(k)*phi(k), j2(k)) for k in range(1, n+1, 2)), F(0)))
        check('normalization_convolution', aa == sum(
            (specialization(op('U', d), 1)*m0(n//d, True)
             for d in range(1, n+1)), F(0)))
        check('coefficient_total', sum(ah.values(), F(0)) ==
              sum(mu(k) for k in range(1, n+1, 2)))
        for k, ak in ah.items():
            check('nonsquarefree_zero', mu(k) != 0 or ak == 0)
        check('odd_full_decomposition', raw(n) ==
              add(raw(n, True), scale(mul({2: F(1)}, raw(n//2, True)), -1)))
        dyadic: Poly = {}
        two = 1
        while two <= n:
            dyadic = add(dyadic, mul({two: F(1)}, raw(n//two)))
            two *= 2
        check('odd_full_inverse', raw(n, True) == dyadic)
        lift = add({2: 2*aa}, scale(sp, -1))
        for t in (F(1, 3), F(3, 2), F(5, 2), F(17, 3), F(65, 4)):
            direct = sum((ak*(2*value({2: F(1)}, t)/k-value({k: F(1)}, t))
                          for k, ak in ah.items()), F(0))
            check('full_lift_values', value(lift, t) == direct)
            cell = t.__floor__()
            if cell >= 1:
                check('lift_is_step', value(lift, t) == value(lift, F(cell)))
            else:
                check('lift_below_one_zero', value(lift, t) == 0)
        if n in (1, 3, 8, 16, 32):
            records.append({'cutoff': n, 'normalized_coefficients': poly_record(sp),
                            'normalization_over_cstar': qrecord(aa),
                            'coefficient_sum_over_cstar': sum(mu(k) for k in range(1,n+1,2))})

    for q in range(2, scope['dual_limit']+1):
        dq = dual(q)
        pairing = sum((v/F(n*(n+1)) for n, v in dq.items()), F(0))
        check('dual_target_pairing', pairing == -mu(q))
        for k in range(2, scope['dictionary_limit']+1):
            check('dual_dictionary_pairing', sum(
                (h(k,n)*v/F(n*(n+1)) for n,v in dq.items()), F(0)) == int(k == q))
        if q in (2, 5):
            check('dual_overlap_norm', sum((v*v/F(n*(n+1)) for n,v in dq.items()), F(0)) ==
                  (14 if q == 2 else 52))
    check('nonsquarefree_annihilator_nonzero', bool(dual(4)))
    check('prime_power_inverse_necessary', bool(op('U', 9)) and bool(op('V', 9)))
    check('elementary_log_bound_margin', F(1,2)-F(7,10)**2 == F(1,100))
    for p in (3,5,7,11,13):
        check('operator_norm_scalar_margin', (F(4,5)-(1+F(3,5)*p*p)/(p*p-1)) ==
              F(p*p-9, 5*(p*p-1)))
    for j in range(1, 33):
        check('prime_majorant_telescope', sum((F(1, (2*k+1)**2-1) for k in range(1,j+1)),F(0)) ==
              F(1,4)*(1-F(1,j+1)))
    payload = {
        'schema': SCHEMA, 'rh_proved': False, 'uniform_full_gain_proved': False,
        'subpower_growth_proved': False, 'infinite_proofs_machine_verified': False,
        'arithmetic': 'exact_integer_and_fraction', 'scope': scope,
        'normalization': 'a_hat = a / (8/pi^2); no approximation of pi is used',
        'proof_status': 'proposed_component_proofs_pending_independent_review',
        'control_counts': dict(sorted(counts.items())), 'total_controls': sum(counts.values()),
        'sample_operator_inverse_at_9': poly_record(op('V',9)), 'sample_cutoffs': records,
        'dual_5': poly_record(dual(5)), 'source_binding': 'Mobius independently rebuilt by divisor recursion; polynomial dilation algebra; finite fractional parts',
    }
    return payload


def no_duplicates(pairs: list[tuple[str, object]]) -> dict[str, object]:
    out = {}
    for k, v in pairs:
        require(k not in out, 'duplicate JSON key')
        out[k] = v
    return out


def forbidden_float(_: str) -> object:
    raise ValueError('floating-point/nonfinite JSON numbers forbidden')


def load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=no_duplicates,
                      parse_float=forbidden_float, parse_constant=forbidden_float)


def canonical(obj: object) -> str:
    return json.dumps(obj, indent=2, sort_keys=True, ensure_ascii=False) + '\n'


def validate_structure(obj: object) -> None:
    require(type(obj) is dict, 'JSON object required')
    for key in ('rh_proved','uniform_full_gain_proved','subpower_growth_proved','infinite_proofs_machine_verified'):
        require(type(obj.get(key)) is bool and obj[key] is False, f'false scope flag required: {key}')
    scope = obj.get('scope')
    require(type(scope) is dict and set(scope) == set(SCOPE), 'scope keys mismatch')
    for key, val in SCOPE.items():
        require(type(scope[key]) is int and scope[key] == val, 'fixed integer scope mismatch')
    require(type(obj.get('total_controls')) is int and obj['total_controls'] > 0, 'nonempty controls required')


def authenticate(root: Path = ROOT, include_verification: bool = True) -> None:
    require(root.is_dir(), 'packet missing')
    require(not any(p.is_symlink() for p in root.rglob('*')), 'symlink in packet')
    paths = {p.relative_to(root).as_posix() for p in root.rglob('*')
             if p.is_file() and '__pycache__' not in p.parts}
    require(paths == INVENTORY | {'SHA256SUMS'}, 'exact nonempty packet inventory mismatch')
    lines = (root/'SHA256SUMS').read_text(encoding='utf-8').splitlines()
    bound = {}
    for line in lines:
        digest, rel = line.split('  ',1)
        require(rel in INVENTORY and rel not in bound, 'unrecognized or duplicate manifest path')
        require(len(digest) == 64 and all(c in '0123456789abcdef' for c in digest), 'bad digest')
        bound[rel] = digest
    require(set(bound) == INVENTORY, 'manifest coverage mismatch')
    for rel, digest in bound.items():
        if rel != 'verification.json' or include_verification:
            require(hashlib.sha256((root/rel).read_bytes()).hexdigest() == digest, f'changed packet bytes: {rel}')
    for rel, digest in PARENT_SHA256.items():
        p = root.parent/rel
        require(p.is_file() and hashlib.sha256(p.read_bytes()).hexdigest() == digest,
                f'changed/missing parent proof: {rel}')
    lock = load_json(root/'SOURCE_LOCK.json')
    require(type(lock) is dict and lock.get('schema') == 'gt26-source-lock-v1' and
            lock.get('repository') == 'GettysburgResearch/riemann' and
            type(lock.get('parent_pr')) is int and lock['parent_pr'] == 805, 'source lock type mismatch')
    require(type(lock) is dict and lock.get('parent_commit') == '0f8724bbd86c1de8f40eacbf30129321e0ebc8aa', 'parent commit mismatch')
    require(lock.get('proof_sha256') == PARENT_SHA256, 'parent digest lock mismatch')


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--check', type=Path, default=ROOT/'verification.json')
    ap.add_argument('--write', type=Path)
    args = ap.parse_args()
    authenticate(include_verification=args.write is None)
    fresh = compute()
    if args.write is not None:
        args.write.write_text(canonical(fresh), encoding='utf-8')
    else:
        retained = load_json(args.check)
        validate_structure(retained)
        require(canonical(retained) == canonical(fresh), 'primitive replay differs from retained result')
    print(f"PASS_GT26_EXACT_TRANSFER controls={fresh['total_controls']} rh_proved=false full_gain_proved=false")
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (ValueError, TypeError, KeyError, OSError) as exc:
        print(f'REJECT_GT26: {exc}', file=sys.stderr)
        raise SystemExit(2)
