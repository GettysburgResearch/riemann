"""Bounded controls for the arithmetic review; Python standard library only.

Exact Fraction controls check native collar identities and the synthetic
square-dilation source. The larger synthetic norms are ORDINARY binary64
diagnostics, not directed certificates or proofs of any asymptotic estimate.
"""
from fractions import Fraction as F
from math import fsum, isqrt, log
from pathlib import Path
import argparse
import json


def need(test, label):
    if not test:
        raise ValueError(label)


def mu(n):
    sign, p = 1, 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            sign = -sign
            if n % p == 0:
                return 0
        p += 1
    return -sign if n > 1 else sign


def liouville(n):
    sign, p = 1, 2
    while p * p <= n:
        while n % p == 0:
            n //= p
            sign = -sign
        p += 1
    return -sign if n > 1 else sign


def convolution(a):
    out = {}
    for i, x in a.items():
        for j, y in a.items():
            out[i * j] = out.get(i * j, 0) + x * y
    return {n: x for n, x in out.items() if x}


def native_controls():
    rows = []
    for y in range(2, 18):
        b = (y + 1) ** 2 - 1
        m = [F(0)]
        for k in range(1, b + 1):
            m.append(m[-1] + F(mu(k), k))
        if not mu(y) or m[y - 1] * m[y] > 0:
            continue
        c = {k: F(mu(k)) for k in range(1, y + 1) if mu(k)}
        if m[y]:
            c[2 * y] = -2 * y * m[y]
        z = convolution(c)
        h = [F(0)]
        for k in range(1, b + 1):
            h.append(h[-1] + F(1, k))
        q2 = F(0)
        for k in range(y + 1, b + 1):
            q = sum((v * h[k // d] / d for d, v in z.items() if d <= k), F(0))
            q2 += q * q
        ann = sum((m[k] ** 2 for k in range(y + 1, b + 1)), F(0))
        correction = 4 * (y - 1) * m[y] ** 2 - 4 * m[y] * sum(m[y + 1:2 * y], F(0))
        need(q2 == ann + correction, 'complete native bounded-correction identity')
        need(abs(correction) < 4, 'uniform correction bound')
        rows.append({'Y': y, 'B': b, 'annular_energy': str(ann),
                     'Q_energy': str(q2), 'exact_correction': str(correction)})
    return rows


def synthetic(l):
    # a=3c, z=9(c*c); coefficients remain integer throughout construction.
    base = {1: 3, 2: -3, 3: -3, 5: -3, 10: 1}
    a = {}
    for n in range(1, l + 1):
        for j, value in base.items():
            index = j * n * n
            need(index not in a, 'unique squarefree kernel representation')
            a[index] = value
    y, b = 10 * l * l, (10 * l * l + 1) ** 2 - 1
    need(a[1] == 3 and max(map(abs, a.values())) <= 3, 'source normalization and cap')
    need(all(liouville(n) * value >= 0 for n, value in a.items()), 'Liouville coherence')
    need(sum((F(value, 3 * n) for n, value in a.items()), F(0)) == 0, 'source balance')
    need(sum((F(value, 3 * n) for n, value in a.items() if n < y), F(0)) == -F(1, 3 * y),
         'own reciprocal crossing')
    z = convolution(a)
    h = [0.0] * (b + 1)
    for k in range(1, b + 1):
        h[k] = h[k - 1] + 1.0 / k
    # Exact integer divisor sum, followed by ordinary floating integration.
    divisor = [0] * (b + 1)
    for d, value in z.items():
        for k in range(d, b + 1, d):
            divisor[k] += value
    qvalues = [0.0] * (b + 1)
    acc, compensation = 0.0, 0.0
    for k in range(1, b + 1):
        term = divisor[k] / (9.0 * k) - compensation
        new = acc + term
        compensation = (new - acc) - term
        acc = new
        qvalues[k] = acc
    # Independently evaluate the harmonic quotient formula at six points.
    sample_points = sorted(set([y + 1, 2 * y, b // 3, b // 2, b - 1, b]))
    discrepancy = max(abs(qvalues[k] - fsum(value * h[k // d] / (9.0 * d)
                                          for d, value in z.items() if d <= k))
                      for k in sample_points)
    need(discrepancy < 1e-10, 'ordinary two-formula diagnostic disagreement')

    def hsum(n):
        return (n + 1) * h[n] - n

    def hsum2(n):
        return (n + 1) * h[n] ** 2 - (2 * n + 1) * h[n] + 2 * n

    diagonal_terms, blocks = [], 0
    for d, value in z.items():
        if d == 1:
            continue  # K_1 is identically zero, including its complete diagonal.
        lo = y + 1
        while lo <= b:
            quotient = lo // d
            hi = min(b, (quotient + 1) * d - 1)
            center = h[quotient] + log(d)
            sq = fsum([(hi - lo + 1) * center * center,
                       -2 * center * (hsum(hi) - hsum(lo - 1)),
                       hsum2(hi) - hsum2(lo - 1)])
            diagonal_terms.append((value / (9.0 * d)) ** 2 * sq)
            blocks += 1
            lo = hi + 1
    diagonal = fsum(diagonal_terms)
    q2 = fsum(x * x for x in qvalues[y + 1:])
    subann = fsum(x * x for x in qvalues[y + 1:2 * y + 1])
    need(diagonal > 0 and q2 > 0, 'ordinary positive norm diagnostic')
    return {'L': l, 'Y': y, 'B': b, 'source_nonzero': len(a),
            'coalesced_products': len(z), 'complete_diagonal_quotient_blocks': blocks,
            'D_binary64': diagonal, 'C_binary64': q2 - diagonal,
            'C_over_D_binary64': (q2 - diagonal) / diagonal,
            'Q_energy_binary64': q2, 'first_doubling_energy_binary64': subann,
            'first_doubling_over_logL_squared': subann / log(l) ** 2 if l > 1 else None,
            'sampled_formula_discrepancy': discrepancy,
            'native_divisor_equation_failure_at_4': str(sum(F(a.get(d, 0), 3) for d in (1, 2, 4)))}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', type=Path, required=True)
    args = parser.parse_args()
    result = {'status': 'bounded controls; synthetic source is not Mobius; no RH estimate',
              'exact_native_identity_controls': native_controls(),
              'synthetic_exact_source_and_ordinary_norm_controls': [synthetic(l) for l in (1, 2, 4, 8)],
              'numerical_boundary': 'All norm values are ordinary binary64, not rigorous enclosures. The asymptotic obstruction is proved in arithmetic.md independently.'}
    args.write.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'completed': True, 'native_exact_panels': len(result['exact_native_identity_controls']),
                      'synthetic_panels': 4, 'largest_full_annulus_endpoint': 410880}))


if __name__ == '__main__':
    main()
