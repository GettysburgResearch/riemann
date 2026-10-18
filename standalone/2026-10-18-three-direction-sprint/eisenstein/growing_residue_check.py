"""Exact finite ideal Gram/tail responses. Does not test an asymptotic moment."""
from fractions import Fraction as F
from pathlib import Path
from math import gcd
import hashlib
import json
from verify import hnf_ideals, norm, subset, hnf_mobius, prime_ideals
from tail_mollifier_check import V, W


def req(value, message):
    if not value:
        raise ArithmeticError(message)


def solve_positive(matrix, target):
    """Exact LDL elimination checks positivity and solves the actual matrix."""
    n = len(target)
    a = [list(row) + [target[i]] for i, row in enumerate(matrix)]
    pivots = []
    for k in range(n):
        pivot = a[k][k]
        req(pivot > 0, 'actual finite Gram is not positive definite')
        pivots.append(pivot)
        for i in range(k + 1, n):
            multiplier = a[i][k] / pivot
            for j in range(k, n + 1):
                a[i][j] -= multiplier * a[k][j]
    x = [F(0)] * n
    for i in reversed(range(n)):
        x[i] = (a[i][n] - sum((a[i][j] * x[j] for j in range(i + 1, n)), F(0))) / a[i][i]
    return x, pivots


def main():
    cap = 1536
    ideals = [a for a in hnf_ideals(cap) if gcd(norm(a), 6) == 1]
    primes = prime_ideals(cap)
    mu = {a: hnf_mobius(a, primes) for a in ideals}
    factors = {a: tuple(p for p in primes if subset(a, p)) for a in ideals}
    v, f = {}, {}
    for a in ideals:
        z, y = F(1), F(1)
        for p in factors[a]:
            q = norm(p)
            z *= F(q * q, q * q + q - 1)
            y /= q + 1
        v[a], f[a] = z, y
    records = []
    prefix_gates = response_gates = cholesky_gates = polar_gates = 0
    mutation_controls = 0
    for D, G in [(128, 13), (256, 19), (512, 25)]:
        outer = [a for a in ideals if norm(a) <= 3 * D]
        labels = [g for g in ideals if mu[g] and norm(g) <= G]
        B = [[sum((mu[a] ** 2 * W(F(norm(a), D)) / norm(a)
                   for a in outer if subset(a, g) and subset(a, h)), F(0))
              for h in labels] for g in labels]
        Z = [sum((mu[a] * V(F(norm(a), D)) * v[a] / norm(a)
                  for a in outer if subset(a, g)), F(0)) for g in labels]
        xi, pivots = solve_positive(B, [-z for z in Z])
        coeff = {a: mu[a] * V(F(norm(a), D)) + mu[a] ** 2 / v[a] * W(F(norm(a), D)) *
                 sum((xi[i] for i, g in enumerate(labels) if subset(a, g)), F(0))
                 for a in outer}
        for i, g in enumerate(labels):
            response = sum((coeff[a] * v[a] / norm(a) for a in outer if subset(a, g)), F(0))
            req(response == 0, 'simultaneous exact divisor response not zero')
            req(sum((B[i][j] * xi[j] for j in range(len(labels))), F(0)) == -Z[i], 'linear solve mismatch')
            response_gates += 1
        for a in outer:
            if norm(a) <= D:
                req(coeff[a] == mu[a], 'low prefix changed')
                conv = sum((coeff[b] for b in outer if subset(a, b)), F(0))
                req(conv == (1 if norm(a) == 1 else 0), 'complete low unit convolution failed')
                prefix_gates += 1
        for g in labels:
            for h in labels:
                common = set(factors[g]) & set(factors[h])
                union = set(factors[g]) | set(factors[h])
                left = F(1)
                for p in union:
                    left /= norm(p) + 1
                divisor_sum = sum((F(norm(d)) for d in labels if subset(g, d) and subset(h, d)), F(0))
                req(left == f[g] * f[h] * divisor_sum, 'main GCD Cholesky identity failed')
                cholesky_gates += 1
        for R in labels:
            direct = F(0)
            for a in outer:
                common = set(factors[a]) & set(factors[R])
                vgcd = F(1)
                for p in common:
                    q = norm(p)
                    vgcd *= F(q * q, q * q + q - 1)
                expansion = F(0)
                for g in labels:
                    if subset(a, g) and subset(R, g):
                        c = F(1)
                        for p in factors[g]:
                            q = norm(p)
                            c *= F(q - 1, q * q)
                        expansion += c
                req(expansion == 1 / vgcd, 'full shared-prime Boolean expansion failed')
                direct += coeff[a] * v[a] / norm(a) * v[R] / vgcd
                polar_gates += 1
            req(direct == 0, 'actual squarefree-label polar response not zero')
        wrong = {a: mu[a] * V(F(norm(a), D)) + mu[a] ** 2 * W(F(norm(a), D)) *
                 sum((xi[i] for i, g in enumerate(labels) if subset(a, g)), F(0)) for a in outer}
        req(any(sum((wrong[a] * v[a] / norm(a) for a in outer if subset(a, g)), F(0)) != 0
                for g in labels), 'missing inverse-v mutation not detected')
        mutation_controls += 1
        # Deliberately omit one nonunit probe. This changes actual coefficients.
        omit = next(i for i, g in enumerate(labels) if norm(g) > 1 and xi[i])
        changed = [xi[i] if i != omit else F(0) for i in range(len(labels))]
        req(any(sum((B[i][j] * changed[j] for j in range(len(labels))), F(0)) != -Z[i]
                for i in range(len(labels))), 'omitted arithmetic probe mutation not detected')
        mutation_controls += 1
        records.append({'D': D, 'G': G, 'complete_outer_ideals': len(outer),
                        'labels': [list(g) for g in labels],
                        'xi': [str(x) for x in xi], 'positive_pivots': [str(x) for x in pivots],
                        'exact_responses': ['0'] * len(labels)})
    # Every prime-unit character of exponent1 or2 is nonprincipal, including
    # its lift to a prime-square quotient. Count in the exact Phi_6 basis.
    orthogonality = 0
    roots = [(1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1)]
    for q in [7, 13, 19, 31, 37, 43]:
        for j in [1, 2]:
            for modulus_exponent in [1, 2]:
                repeat = q ** (modulus_exponent - 1) * (q - 1) // 6
                total = [0, 0]
                for k in range(6):
                    z = roots[(j * k) % 6]
                    total[0] += repeat * z[0]
                    total[1] += repeat * z[1]
                req(total == [0, 0], 'nonprincipal cusp unit sum failed')
                orthogonality += 1
    out = {'status': 'PASS', 'scope': 'Exact finite complete ideal Gram, tail and polar-response algebra only; no global covariance claim.',
           'complete_ideal_cap': cap, 'complete_exterior_ideals': len(ideals),
           'prefix_unit_gates': prefix_gates, 'divisibility_responses': response_gates,
           'main_gcd_cholesky_gates': cholesky_gates, 'shared_prime_polar_gates': polar_gates,
           'nonprincipal_cusp_unit_sums': orthogonality, 'mutations_rejected': mutation_controls,
           'records': records, 'profile_note': 'Exact rational finite C2/C3 fixtures; theorem assumes smooth profiles.'}
    out['records_sha256'] = hashlib.sha256(json.dumps(records, separators=(',', ':')).encode()).hexdigest()
    Path(__file__).with_name('GROWING_RESIDUE_CHECKS.json').write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps({k: v for k, v in out.items() if k != 'records'}, indent=2))


if __name__ == '__main__':
    main()
