"""Exact finite checks of the two divisor inversions, not analytic bounds."""
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def main():
    # Two distinct prime ideals can have the SAME norm in the Eisenstein
    # field. Their labels remain distinct; norm-only gcds would be wrong.
    primes = (7, 7, 13, 13, 19, 19, 31, 31)
    universe = range(1 << len(primes))

    def norm(s):
        z = 1
        for j, q in enumerate(primes):
            if s >> j & 1:
                z *= q
        return z

    def mu(s):
        return -1 if s.bit_count() % 2 else 1

    def f(s):
        z = F(1)
        for j, q in enumerate(primes):
            if s >> j & 1:
                z /= q + 1
        return z

    def v(s):
        z = F(1)
        for j, q in enumerate(primes):
            if s >> j & 1:
                z *= F(q * q, q * q + q - 1)
        return z

    labels = tuple(s for s in universe if norm(s) <= 300)
    divides = lambda a, b: a & b == a
    matrix = {(g, h): f(g | h) for g in labels for h in labels}
    inv = {
        (g, h): F(mu(g) * mu(h), 1) / (f(g) * f(h))
        * sum((F(1, norm(d)) for d in labels if divides(g | h, d)), F(0))
        for g in labels for h in labels
    }
    count_inverse = 0
    for g in labels:
        for h in labels:
            z = sum((matrix[g, k] * inv[k, h] for k in labels), F(0))
            require(z == int(g == h), "exact inverse identity")
            count_inverse += 1

    # The response comes from an ACTUAL finite Mobius head. This check
    # retains every shared prime in g|a and all eight distinct primes.
    heads = tuple(a for a in universe if 5000 <= norm(a) <= 10000)
    require(heads and any(mu(a) < 0 for a in heads), "nontrivial signed head")
    z = {g: sum((F(mu(a)) * v(a) / norm(a)
                 for a in heads if divides(g, a)), F(0)) for g in labels}
    aa = {g: -z[g] / (f(g) * mu(g)) for g in labels}
    xi = {
        g: F(mu(g)) / f(g)
        * sum((F(1, norm(d))
               * sum((aa[e] for e in labels if divides(e, d)), F(0))
               for d in labels if divides(g, d)), F(0))
        for g in labels
    }
    count_response = 0
    for g in labels:
        require(sum((matrix[g, h] * xi[h] for h in labels), F(0)) == -z[g],
                "specific-head response inversion")
        count_response += 1

    # Independent evaluation by the exact inverse must agree as well.
    for g in labels:
        require(xi[g] == -sum((inv[g, h] * z[h] for h in labels), F(0)),
                "two inversion paths differ")

    # Mutations test that the identities would reject lost Mobius signs,
    # a norm-only prime identification, and the wrong common-prime law.
    mutations = []
    bad_xi = {
        g: xi[g] * mu(g) for g in labels
    }
    mutations.append(any(sum((matrix[g, h] * bad_xi[h] for h in labels), F(0))
                         != -z[g] for g in labels))
    mutations.append(any(matrix[g, h] != f(g) * f(h)
                         for g in labels for h in labels))
    mutations.append(any(inv[g, h] != F(mu(g) * mu(h), 1)
                         / (f(g) * f(h) * norm(g | h))
                         for g in labels for h in labels))
    # Distinct split primes both have norm 7, yet intersect in the UNIT.
    mutations.append(norm(1) == norm(2) and (1 & 2) == 0
                     and matrix[1, 2] != matrix[1, 1])
    require(all(mutations), "a structural mutation escaped")
    records = {
        "status": "PASS",
        "scope": "exact finite arithmetic only; no asymptotic or row mean",
        "prime_ideal_norms": primes,
        "downward_closed_labels": len(labels),
        "actual_head_ideals": len(heads),
        "inverse_entries_checked": count_inverse,
        "specific_head_responses_checked": count_response,
        "structural_mutations_rejected": len(mutations),
        "response_digest": sha256("\n".join(
            f"{g}:{xi[g].numerator}/{xi[g].denominator}" for g in labels
        ).encode()).hexdigest(),
    }
    output = Path(__file__).with_name("PROFILE_INVERSE_CHECKS.json")
    output.write_text(json.dumps(records, sort_keys=True, indent=2) + "\n",
                      encoding="utf-8")
    print(json.dumps(records, sort_keys=True))


if __name__ == "__main__":
    main()
