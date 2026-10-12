"""Exact native sextic R_2 witness; no asymptotic moment bound is claimed."""
from collections import Counter
from itertools import product
from pathlib import Path
import argparse
import hashlib
import json
from math import isqrt


def require(ok, label):
    if not ok:
        raise ArithmeticError(label)


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def mul(x, y):
    a, b = x
    c, d = y
    return a * c - b * d, a * d + b * c - b * d


def conjugate(x):
    return x[0] - x[1], -x[1]


def power(x, n):
    out = (1, 0)
    for _ in range(n):
        out = mul(out, x)
    return out


def norm(x):
    a, b = x
    return a * a - a * b + b * b


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source-root', type=Path, default=Path(
        '/workspace/.riemann-research/moment-sources/914/standalone'))
    args = parser.parse_args()
    source_dir = args.source_root / '2026-10-10-sextic-moment-conductor-core'
    source_hashes = {
        'CONDUCTOR_SECTORS.md':
        'c160bbb1b1d7c6bcc5514d496ad41f15fd17ea3d36206b0d05cfa0d7d6503983',
        'A2_COMPLETION.md':
        'd99eade56807077b07e5ec1325001f1592115db216e1e10e6a3906a3e01f0aad',
    }
    for filename, expected in source_hashes.items():
        actual = hashlib.sha256((source_dir / filename).read_bytes()).hexdigest()
        require(actual == expected, 'frozen source ' + filename)

    seeds = [(-2, -3), (1, -3), (-2, 3), (1, 6)]
    units = [(1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1)]
    require([power((1, 1), j) for j in range(6)] == units,
            'literal ordered sixth roots in Eisenstein ring')
    primes = []
    for seed in seeds:
        for pi in (seed, conjugate(seed)):
            a, b = pi
            q = norm(pi)
            require(q in (7, 13, 19, 31), 'prime norm support')
            require(all(q % d for d in range(2, isqrt(q) + 1)),
                    'rational prime norm')
            require(a % 3 == 1 and b % 3 == 0, 'primary generator')
            root = (-a * pow(b, -1, q)) % q
            require((root * root + root + 1) % q == 0 and root != 1,
                    'actual residue-field omega')
            lookup = {(ua + ub * root) % q: (ua, ub) for ua, ub in units}
            require(len(lookup) == 6, 'six distinct native unit residues')
            primes.append((pi, q, root, lookup))
    require(len({(q, root) for _, q, root, _ in primes}) == 8,
            'eight distinct prime ideals, including conjugates')

    rows = [(a, b) for a in range(-8, 9) for b in range(-8, 9)
            if 0 < norm((a, b)) <= 40]
    for a, b in rows:
        n = norm((a, b))
        require(4 * n - 3 * a * a == (a - 2 * b)**2 and
                4 * n - 3 * b * b == (2 * a - b)**2,
                'complete row box from exact norm inequalities')
    require(3 * 8**2 > 4 * 40, 'no lattice row can escape the box')
    require(len(rows) == 150, 'complete row count')

    def chi(p, u):
        _, q, root, lookup = p
        residue = (u[0] + u[1] * root) % q
        return (0, 0) if residue == 0 else lookup[pow(residue, (q - 1)//6, q)]

    characters = [[chi(p, u) for p in primes] for u in rows]
    moment = 0
    for cs in characters:
        inverse = (0, 0)
        for value in cs:
            inverse = add(inverse, (-value[0], -value[1]))
        square = mul(inverse, conjugate(inverse))
        require(square[1] == 0 and square[0] >= 0, 'native absolute square')
        moment += square[0]**2

    critical_total = controlled_total = diagonal_total = leading_total = (0, 0)
    counts = dict(tuples=0, critical=0, product_diagonal=0,
                  critical_removed_by_product_diagonal=0,
                  nonzero_critical_row_kernels=0, leading_pairwise_coprime=0)
    for t in product(range(8), repeat=4):
        left, right = Counter(t[:2]), Counter(t[2:])
        g1 = g2 = 1
        for i, p in enumerate(primes):
            r, s = left[i], right[i]
            if r + s == 1:
                g1 *= p[1]
            if r + s == 2 and (r - s) % 6:
                g2 *= p[1]
        critical = g1 != 1 and g1 * g1 * g2 > 40**2
        diagonal = left == right
        kernel = (0, 0)
        for cs in characters:
            literal = mul(mul(cs[t[0]], cs[t[1]]),
                          conjugate(mul(cs[t[2]], cs[t[3]])))
            residual = (1, 0)
            for i in set(t):
                if cs[i] == (0, 0):
                    residual = (0, 0)
                    break
                residual = mul(residual, power(cs[i], (left[i] - right[i]) % 6))
            require(literal == residual, 'literal tuple versus residual with zeros')
            kernel = add(kernel, literal)
        counts['tuples'] += 1
        if critical:
            critical_total = add(critical_total, kernel)
            counts['critical'] += 1
            counts['nonzero_critical_row_kernels'] += kernel != (0, 0)
        else:
            controlled_total = add(controlled_total, kernel)
        if diagonal:
            require(g1 == 1 and not critical, 'product diagonal disjoint from R2')
            diagonal_total = add(diagonal_total, kernel)
            counts['product_diagonal'] += 1
            counts['critical_removed_by_product_diagonal'] += critical
        if len(set(t)) == 4:
            require(critical and not diagonal, 'coprime leading face remains critical')
            leading_total = add(leading_total, kernel)
            counts['leading_pairwise_coprime'] += 1
    require(add(critical_total, controlled_total) == (moment, 0),
            'direct fourth moment equals full Hermitian tuple sum')
    require((moment, critical_total, controlled_total, diagonal_total, leading_total)
            == (16752, (1176, 0), (15576, 0), (15564, 0), (456, 0)),
            'frozen exact native witness')
    require(counts == dict(tuples=4096, critical=3696, product_diagonal=120,
                          critical_removed_by_product_diagonal=0,
                          nonzero_critical_row_kernels=560,
                          leading_pairwise_coprime=1680), 'all tuple regions')

    # Independent negative controls: exponent-zero still has a nonunit mask,
    # and odd residual sextic phases are not replaced by cubic phases.
    masked_row = next(cs for cs in characters if cs[0] == (0, 0))
    require(power(masked_row[0], 0) !=
            mul(mul(masked_row[0], masked_row[0]),
                conjugate(mul(masked_row[0], masked_row[0]))),
            'dropping principal zero extension must be rejected')
    require(any(value != (0, 0) and power(value, 5) != power(value, 2)
                for cs in characters for value in cs),
            'reducing odd sextic residual modulo three must be rejected')

    proof = Path(__file__).with_name('SIGNED_BALANCED_NATIVE_WITNESS.md')
    receipt = dict(
        source_commit='0cc0428fedbbfc340044c7451b3d392c1da9a103',
        source_hashes=source_hashes,
        checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        proof_sha256=hashlib.sha256(proof.read_bytes()).hexdigest(),
        D=30, H=40, rows=len(rows), columns=len(primes), counts=counts,
        full_native_fourth_moment=moment,
        critical_R_exact_Eisenstein_pair=critical_total,
        controlled_exact_Eisenstein_pair=controlled_total,
        product_diagonal_exact_Eisenstein_pair=diagonal_total,
        leading_pairwise_coprime_R=leading_total,
        negative_controls_passed=2,
        imported_controlled_sector_analysis_independently_rebuilt=False,
        generalized_moment_estimate_proved=False, rh_proved=False,
        arithmetic='integer Eisenstein pairs and exact prime residue fields')
    print(json.dumps(receipt, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
