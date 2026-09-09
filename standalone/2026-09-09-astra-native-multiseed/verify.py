"""NM26 exact finite controls and a full-tail audit of the actual small seed.

The analytic domain and recurrence theorems are paper proofs, not conclusions
of these finite tests. --emit produces a receipt; --check authenticates and
reconstructs it. Standard library only; no floating values enter acceptance.
"""
import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from math import gcd, lcm
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
SCALE = 1 << 128
HORIZON = 1 << 20
DEN = 562949953421312
NUM = (562949953421312, -562949953421312, -532205406349296,
       -58291156654044, -441882648513420, 328445548501212,
       -366102615428543, 18872698772432, -57317966477307,
       250457476590930, -252425357406167, 20023818681228,
       -248939343231540, 204789481170078, 157840018622805,
       -149164455120992)
FILES = {'README.md', 'PROOF.md', 'SEED.md', 'ATTEMPT.md', 'SOURCES.json',
         'VALIDATION.md', 'verify.py', 'test_rejections.py', 'result.json', 'SHA256SUMS'}


def require(ok, why):
    if not ok:
        raise ValueError(why)


def pairs(items):
    result = {}
    for key, value in items:
        require(key not in result, 'duplicate JSON key')
        result[key] = value
    return result


def load(path):
    require(path.is_file() and not path.is_symlink(), 'nonregular receipt')
    def bad(_):
        raise ValueError('floating/nonfinite JSON is forbidden')
    return json.loads(path.read_text(), object_pairs_hook=pairs,
                      parse_float=bad, parse_constant=bad)


def canonical(x):
    return json.dumps(x, sort_keys=True, separators=(',', ':'), ensure_ascii=True)


def typed_equal(a, b):
    if type(a) is not type(b):
        return False
    if type(a) is dict:
        return a.keys() == b.keys() and all(typed_equal(a[k], b[k]) for k in a)
    if type(a) is list:
        return len(a) == len(b) and all(typed_equal(x, y) for x, y in zip(a, b))
    return a == b


def fp(q):
    return [str(q.numerator), str(q.denominator)]


def enclose_log(n):
    require(type(n) is int and n >= 1, 'log argument')
    k = n.bit_length() - 1
    def series(q):
        total = F(0)
        power = q
        for j in range(100):
            total += 2 * power / (2*j+1)
            power *= q*q
        remainder = 2*power / (201*(1-q*q))
        return total, total + remainder
    a, b = series(F(1, 3))
    c, d = series(F(n-(1 << k), n+(1 << k)))
    low, high = k*a+c, k*b+d
    lo = (low.numerator*SCALE)//low.denominator
    hi = -((-high.numerator*SCALE)//high.denominator)
    return F(lo, SCALE), F(hi, SCALE)


def mobius_trial(n):
    value, p = 1, 2
    while p*p <= n:
        if n % p == 0:
            n //= p
            value = -value
            if n % p == 0:
                return 0
        p += 1
    return -value if n > 1 else value


def mobius_linear(N):
    least = [0]*(N+1)
    mu = [0]*(N+1)
    mu[1] = 1
    primes = []
    for n in range(2, N+1):
        if least[n] == 0:
            least[n] = n
            primes.append(n)
            mu[n] = -1
        for p in primes:
            if p*n > N:
                break
            least[p*n] = p
            if n % p == 0:
                mu[p*n] = 0
                break
            mu[p*n] = -mu[n]
    return mu


def period_mean(a, b=F(1)):
    """Independent pairwise-gcd formula; not the parent's Jordan loops."""
    N = len(a)
    require(sum(a[n-1]/n for n in range(1, N+1)) == 0, 'balance')
    coherent = b + sum(a)/2
    return coherent*coherent + sum(
        a[i-1]*a[j-1]*F(gcd(i, j)**2, 12*i*j)
        for i in range(1, N+1) for j in range(1, N+1))


def audit_seed():
    require(len(NUM) == 16 and NUM[0] == DEN and NUM[1] == -DEN, 'seed prefix')
    a = [F(n, DEN) for n in NUM]
    require(sum(a) == -2 and sum(a[n-1]/n for n in range(1, 17)) == 0,
            'seed rational constraints')
    lo = hi = F(1)
    for n in range(1, 17):
        l, h = enclose_log(n)
        c = a[n-1]/n
        lo += c*(l if c >= 0 else h)
        hi += c*(h if c >= 0 else l)
    l2, h2 = enclose_log(2)
    corners = [x/y for x in (lo, hi) for y in (l2, h2)]
    clo, chi = min(corners), max(corners)
    D = DEN*(1 << 64)
    middle = (clo+chi)*D/2
    k = (2*middle.numerator+middle.denominator)//(2*middle.denominator)
    c = F(k, D)
    eta = 6*max(abs(c-clo), abs(c-chi))
    A = [n*(1 << 64) for n in NUM]
    for index, coefficient in ((3, 6), (6, -18), (12, 12)):
        A[index-1] += coefficient*k
    aa = [F(n, D) for n in A]
    require(sum(aa) == -2 and sum(aa[n-1]/n for n in range(1, 17)) == 0,
            'rationalized exact constraints')
    V = period_mean(aa)
    lower = 0
    rounds = 0
    D2 = D*D
    # Direct floor evaluation at EVERY cell, unlike the old divisor-event code.
    for j in range(1, HORIZON):
        residual = D - sum(a*(j//n) for n, a in enumerate(A, 1))
        quotient, remainder = divmod((residual*residual)*SCALE,
                                     D2*j*(j+1))
        lower += quotient
        rounds += int(remainder != 0)
    C = 16**2*(1+2*4)
    tail = V/HORIZON
    radius = C*V/F(HORIZON*(HORIZON+1))
    low = F(lower, SCALE)+tail-radius
    high = F(lower+rounds, SCALE)+tail+radius
    require(high < 1, 'seed comparison premise')
    low -= 2*eta+eta*eta
    high += 2*eta+eta*eta
    require(F(19530763932, 10**12) < low < high < F(19530764725, 10**12),
            'full seed-energy enclosure')
    require(high < F(49, 2500), 'seed norm budget')
    bank_upper = (F(7, 50)+F(1, 2048))**2
    require(bank_upper < F(1, 50), 'three-seed budget')
    return {'integrated_cells': HORIZON-1, 'horizon': HORIZON,
            'period_mean': fp(V), 'tail_error_radius': fp(radius),
            'coefficient_ratio_interval': [fp(clo), fp(chi)],
            'rationalized_denominator': str(D), 'rationalized_k': str(k),
            'full_norm_difference': fp(eta),
            'seed_energy_interval': [fp(low), fp(high)],
            'three_seed_energy_upper': fp(bank_upper),
            'seed_support': 16, 'bank_supports': [16, 24, 81],
            'native_prefix_through': 2}


def convolve(a, b, N):
    out = [F(0)]*(N+1)
    for i in range(1, N+1):
        if a[i]:
            for j in range(1, N//i+1):
                if b[j]:
                    out[i*j] += a[i]*b[j]
    return out


def finite_checks():
    mu = mobius_linear(256)
    require(all(mu[n] == mobius_trial(n) for n in range(1, 257)), 'Mobius input')
    deformations = 0
    for r in (2, 3, 5):
        coeff = (1, -(2*r+1), r*r+2*r, -r*r)
        require(sum(coeff) == 0, 'value at zero')
        require(sum(F(coeff[j], r**j) for j in range(4)) == 0, 'balance')
        require(sum(F(j*coeff[j], r**j) for j in range(4)) == 0, 'derivative jet')
        require(sum(abs(c) for c in coeff) == 2*(r+1)**2, 'whole profile bound')
        for x in range(2*r**3+1):
            profile = sum(coeff[j]*(x//(r**j)) for j in range(4))
            require(abs(profile) <= 2*(r+1)**2, 'profile bound')
            deformations += 1
    periods = 0
    filters = 0
    for N in range(2, 8):
        a = [F(n*((n%3)-1)) for n in range(1, N+1)]
        a[-1] = -N*sum(a[n-1]/n for n in range(1, N))
        Q = lcm(*range(1, N+1))
        direct = sum((1-sum(a[n-1]*(j//n) for n in range(1, N+1)))**2
                     for j in range(Q))/Q
        require(direct == period_mean(a), 'CRT complete period mean')
        periods += 1
        for sigma in range(2, 7):
            value = sum(a[n-1]/n**sigma for n in range(1, N+1))
            density = sum(a[n-1]/n *
                          (F(N)**(1-sigma)-F(n)**(1-sigma))/(1-sigma)
                          for n in range(1, N+1))
            require(value+density == F(sigma, sigma-1)*value,
                    'compact source-filter transform')
            filters += 1
    delay_cases = 0
    N = 256
    for Y in range(2, 8):
        a = [F(0)]*(N+1)
        for n in range(1, Y+1):
            a[n] = F(mu[n])
        a[Y+1] = -(Y+1)*sum(a[n]/n for n in range(1, Y+1))
        ff = [F(0)]*(N+1)
        ff[1] = 1
        for n in range(1, N+1):
            ff[n] -= sum(a[d] for d in range(1, n+1) if n%d == 0)
        power = [F(0)]*(N+1)
        power[1] = 1
        for m in range(1, 4):
            power = convolve(power, ff, N)
            require(all(power[n] == 0 for n in range(1, min(N+1, (Y+1)**m))),
                    'complete Dirichlet delay')
            delay_cases += 1
    # Rational telescoping instances behind the complex-polynomial estimate.
    products = 0
    for A in range(1, 7):
        for D in range(1, 9):
            eta = F(1, 24*(1+A*D))
            require(A*((1+eta)**D-1) < F(1, 12), 'multivariate continuity budget')
            products += 1
    return {'independent_mobius_values': 256,
            'deformation_profile_cells': deformations,
            'complete_period_panels': periods,
            'compact_filter_panels': filters,
            'Dirichlet_delay_panels': delay_cases,
            'polynomial_budget_panels': products}


def produce():
    return {'schema': 'NM26.result.v1', 'rh_proved': False,
            'global_feedback_bound_proved': False,
            'integer_dilation_cyclicity_proved': False,
            'analytic_results_are_machine_proved': False,
            'checks': finite_checks(), 'seed': audit_seed()}


def authenticate():
    items = list(ROOT.iterdir())
    require({p.name for p in items} == FILES, 'packet inventory')
    require(all(p.is_file() and not p.is_symlink() for p in items), 'nonregular packet')
    entries = {}
    for line in (ROOT/'SHA256SUMS').read_text().splitlines():
        pieces = line.split('  ')
        require(len(pieces) == 2, 'manifest syntax')
        digest, name = pieces
        require(name in FILES-{'SHA256SUMS'} and name not in entries, 'manifest names')
        require(len(digest) == 64 and all(c in '0123456789abcdef' for c in digest), 'digest format')
        entries[name] = digest
    require(set(entries) == FILES-{'SHA256SUMS'}, 'manifest coverage')
    for name, digest in entries.items():
        require(sha256((ROOT/name).read_bytes()).hexdigest() == digest, 'hash mismatch: '+name)


def main():
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--emit', action='store_true')
    mode.add_argument('--check', type=Path)
    mode.add_argument('--inventory-only', action='store_true')
    args = parser.parse_args()
    if args.inventory_only:
        authenticate()
        print('PASS inventory only; no mathematical replay')
        return
    if args.check:
        authenticate()
        retained = load(args.check)
        require(type(retained) is dict and retained.get('schema') == 'NM26.result.v1', 'schema')
        for flag in ('rh_proved', 'global_feedback_bound_proved',
                     'integer_dilation_cyclicity_proved', 'analytic_results_are_machine_proved'):
            require(type(retained.get(flag)) is bool and retained[flag] is False, 'status flag')
        actual = produce()
        require(typed_equal(retained, actual), 'receipt differs from reconstruction')
    else:
        actual = produce()
    print(canonical(actual))


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, TypeError, KeyError, json.JSONDecodeError) as exc:
        print('REJECT: '+str(exc), file=sys.stderr)
        sys.exit(2)
