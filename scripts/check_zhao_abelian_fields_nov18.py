"""Enumerate abelian fields in the strict Zhao spectral test, using python-flint.

The inventory represents a field by its full group of nonidentity primitive
Dirichlet characters in Conrey notation. The quadratic seed is independently
reproducible with check_zhao_quadratic_fields_nov18.py.
"""
import json
from functools import cache
from math import gcd, lcm, prod
from pathlib import Path

from flint import acb_series, arb, ctx, dirichlet_char, fmpz

from check_zhao_quadratic_fields_nov18 import zeta_test_bound

DEGREE_BOUND = 15
PHASE_MODULUS = lcm(*range(1, DEGREE_BOUND + 1))
RESEARCH = Path(__file__).resolve().parents[1] / "research" / "explorations"


@cache
def factor(n):
    return tuple((int(p), e) for p, e in fmpz(n).factor())


@cache
def generators(p):
    if p == 2:
        return (-1, 5)
    order = p * (p - 1)
    divisors = [r for r, _ in factor(order)]
    for g in range(2, p*p):
        if g % p and all(pow(g, order // r, p*p) != 1 for r in divisors):
            return (g,)
    raise ArithmeticError("Missing primitive root")


def phases(character):
    q = int(character.modulus())
    exponent = int(character.group().exponent())
    signature = []
    for p, e in factor(q):
        modulus = p**e
        other = q // modulus
        for j, g in enumerate(generators(p)):
            # The chosen global unit equals g on this component and 1 elsewhere.
            unit = (1 + other * ((g - 1) * pow(other, -1, modulus) % modulus)) % q
            numerator = int(character.chi_exponent(unit)) * PHASE_MODULUS
            value, remainder = divmod(numerator, exponent)
            if remainder:
                raise ArithmeticError("Character phase denominator outside degree bound")
            if value % PHASE_MODULUS:
                signature.append((p, j, value % PHASE_MODULUS))
    return tuple(signature)


def product_phases(left, right):
    coords = {(p, j): v for p, j, v in left}
    for p, j, v in right:
        coords[p, j] = (coords.get((p, j), 0) + v) % PHASE_MODULUS
    return tuple((p, j, v) for (p, j), v in sorted(coords.items()) if v)


def below(value, threshold):
    if value < threshold:
        return True
    if value > threshold:
        return False
    raise ArithmeticError("Undecided interval comparison")


def spectral_weight(character):
    q = int(character.modulus())
    s = acb_series([1, 1], prec=2).dirichlet_l(character)
    return ((arb(q) / arb.pi()).log()
            + ((arb(1) + int(character.parity())) / 2).digamma()
            + 2 * (s[1] / s[0]).real)


def classify():
    ctx.prec = 96
    zeta_weight = 2 + arb.const_euler() - (4 * arb.pi()).log()
    target = 2 - zeta_weight
    # rows contain conductor, label, parity, spectral weight, local phases.
    rows = [(1, 1, 0, arb(0), ())]
    quadratic = json.loads((RESEARCH / "zhao-quadratic-fields-nov18.json").read_text())
    for d in quadratic["discriminants"]:
        q = abs(d)
        matches = []
        for label in range(1, q):
            if label * label % q != 1:
                continue
            chi = dirichlet_char(q, label)
            if chi.is_primitive() and chi.parity() == int(d < 0):
                matches.append(chi)
        if len(matches) != 1:
            raise ValueError(f"Ambiguous quadratic character at {d}")
        chi = matches[0]
        weight = spectral_weight(chi)
        if not below(weight, target):
            raise ValueError("Quadratic inventory mismatch")
        rows.append((q, int(chi.number()), int(chi.parity()), weight, phases(chi)))

    # Conjugate weights coincide. A nonreal member always brings its conjugate.
    limits = [int(zeta_test_bound(a, target/2).ceil().unique_fmpz()) for a in (0, 1)]
    candidates = 0
    for q in range(3, max(limits)):
        for label in range(2, q):
            if gcd(q, label) != 1:
                continue
            inverse = pow(label, -1, q)
            if inverse <= label:
                continue
            chi = dirichlet_char(q, label)
            if not chi.is_primitive() or chi.order() > DEGREE_BOUND or q >= limits[chi.parity()]:
                continue
            candidates += 1
            weight = spectral_weight(chi)
            if not below(2 * weight, target):
                continue
            for identifier in (label, inverse):
                c = dirichlet_char(q, identifier)
                rows.append((q, identifier, int(c.parity()), weight, phases(c)))

    lookup = {r[4]: i for i, r in enumerate(rows)}
    if len(lookup) != len(rows):
        raise ValueError("Primitive characters have duplicate coordinates")
    mult = [[lookup.get(product_phases(r[4], t[4]), -1) for t in rows] for r in rows]
    for i, r in enumerate(rows):
        if mult[i][0] != i or 0 not in mult[i]:
            raise ValueError("Failed identity or inverse check")

    groups = [frozenset({0})]
    seen = set(groups)
    for group in groups:
        for j in range(1, len(rows)):
            if j in group:
                continue
            extension = set(group)
            g = j
            while g not in group:
                coset = {mult[i][g] for i in group}
                if -1 in coset or len(extension) + len(group) > DEGREE_BOUND:
                    break
                extension.update(coset)
                g = mult[g][j]
                if g == -1:
                    break
            else:
                subgroup = frozenset(extension)
                if subgroup in seen:
                    continue
                seen.add(subgroup)
                if below(sum(rows[i][3] for i in subgroup), target):
                    groups.append(subgroup)

    fields = []
    for group in groups:
        chars = sorted((rows[i][0], rows[i][1]) for i in group if i)
        fields.append(dict(degree=len(group), conductor=lcm(*(q for q, _ in chars)),
                           abs_discriminant=prod(q for q, _ in chars),
                           totally_real=all(rows[i][2] == 0 for i in group),
                           characters=chars))
    fields.sort(key=lambda f: (f["degree"], f["conductor"], f["characters"]))
    return dict(nonreal_conductor_upper_exclusive=limits,
                conjugate_pairs_evaluated=candidates, fields=fields)


if __name__ == "__main__":
    print(json.dumps(classify(), separators=(",", ":")))
