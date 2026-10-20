#!/usr/bin/env python3
"""Exact, source-free finite certificate for a nonmonomial A5 Brauer identity.

Uses the 60 even permutations and integer arithmetic in Z[z]/Phi_15(z).
No analytic statement about L-functions is tested by this program.
"""
import itertools
import json


def require(value, message):
    if not value:
        raise ArithmeticError(message)


# Phi_15(z)=z^8-z^7+z^5-z^4+z^3-z+1, low coefficients first.
MODULUS = (1, -1, 0, 1, -1, 1, 0, -1, 1)
ZERO = (0,) * 8
ONE = (1,) + (0,) * 7


def reduce_poly(coeffs):
    coeffs = list(coeffs) + [0] * max(0, 8 - len(coeffs))
    for i in range(len(coeffs) - 1, 7, -1):
        q = coeffs[i]
        if q:
            for j in range(9):
                coeffs[i - 8 + j] -= q * MODULUS[j]
    return tuple(coeffs[:8])


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def neg(a):
    return tuple(-x for x in a)


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    c = [0] * 15
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            c[i + j] += ai * bj
    return reduce_poly(c)


def root_power(n):
    coeffs = [0] * (n % 15 + 1)
    coeffs[n % 15] = 1
    return reduce_poly(coeffs)


def conjugate(a):
    result = ZERO
    for i, ai in enumerate(a):
        result = add(result, tuple(ai * t for t in root_power(-i)))
    return result


def exact_div(a, n):
    require(all(x % n == 0 for x in a), "nonintegral cyclotomic division")
    return tuple(x // n for x in a)


def integer(n):
    return (n,) + (0,) * 7


def compose(a, b):
    return tuple(a[b[i]] for i in range(5))


ID = tuple(range(5))


def inverse(a):
    result = [0] * 5
    for i, ai in enumerate(a):
        result[ai] = i
    return tuple(result)


def power(a, n):
    result = ID
    for _ in range(n):
        result = compose(result, a)
    return result


def order(a):
    b = a
    for n in range(1, 61):
        if b == ID:
            return n
        b = compose(b, a)
    raise ArithmeticError("unbounded permutation order")


def even(a):
    return sum(a[i] > a[j] for i in range(5) for j in range(i + 1, 5)) % 2 == 0


def induced_character(group, subgroup_values):
    result = {}
    for g in group:
        total = ZERO
        for x in group:
            y = compose(compose(inverse(x), g), x)
            if y in subgroup_values:
                total = add(total, subgroup_values[y])
        result[g] = exact_div(total, len(subgroup_values))
    return result


def inner_product(group, a, b):
    total = ZERO
    for g in group:
        total = add(total, mul(a[g], conjugate(b[g])))
    return exact_div(total, len(group))


def main():
    group = tuple(p for p in itertools.permutations(range(5)) if even(p))
    require(len(group) == 60, "A5 cardinality")
    group_set = set(group)
    require(all(compose(a, b) in group_set for a in group for b in group), "A5 closure")
    z = root_power(1)
    zp = ONE
    for _ in range(15):
        zp = mul(zp, z)
    require(zp == ONE, "cyclotomic fifteenth power")
    require(all(root_power(n) != ONE for n in (1, 3, 5)), "cyclotomic primitive order")
    require(all(mul(root_power(n), root_power(-n)) == ONE for n in range(15)), "cyclotomic inverses")

    h = tuple(g for g in group if g[4] == 4)
    v4 = tuple(g for g in h if order(g) in (1, 2))
    a = (1, 2, 0, 3, 4)
    require(len(h) == 12 and len(v4) == 4, "A4 and V4 cardinalities")
    lambda_values = {}
    for j in range(3):
        for v in v4:
            p = compose(power(a, j), v)
            require(p not in lambda_values, "distinct V4 cosets")
            lambda_values[p] = root_power(5 * j)
    require(set(lambda_values) == set(h), "A4 quotient coverage")
    require(all(lambda_values[compose(u, v)] == mul(lambda_values[u], lambda_values[v])
                for u in h for v in h), "lambda is a homomorphism")
    require(lambda_values[a] != ONE, "lambda nontrivial")

    c = (1, 2, 3, 4, 0)
    cyclic = tuple(power(c, j) for j in range(5))
    theta_values = {power(c, j): root_power(3 * j) for j in range(5)}
    theta2_values = {power(c, j): root_power(6 * j) for j in range(5)}
    require(len(set(cyclic)) == 5, "C5 cardinality")
    for values in (theta_values, theta2_values):
        require(all(values[compose(u, v)] == mul(values[u], values[v])
                    for u in cyclic for v in cyclic), "theta is a homomorphism")

    a1 = induced_character(group, {u: ONE for u in h})
    alam = induced_character(group, lambda_values)
    ac = induced_character(group, theta_values)
    ac2 = induced_character(group, theta2_values)
    chi = {g: add(sub(sub(ac[g], alam[g]), a1[g]), ONE) for g in group}
    chip = {g: add(sub(sub(ac2[g], alam[g]), a1[g]), ONE) for g in group}
    trivial = {g: ONE for g in group}
    chi4 = {g: sub(a1[g], ONE) for g in group}
    basis = [trivial, chi, chip, chi4, alam]
    require([values[ID][0] for values in basis] == [1, 3, 3, 4, 5], "complete character degrees")
    require(sum(values[ID][0] ** 2 for values in basis) == 60, "degree square sum")
    require(all(inner_product(group, lhs, rhs) == (ONE if i == j else ZERO)
                for i, lhs in enumerate(basis) for j, rhs in enumerate(basis)), "complete irreducible character orthogonality")
    require(chi[ID] == integer(3) and chip[ID] == integer(3), "positive degree three")
    require(inner_product(group, chi, chi) == ONE, "chi irreducible norm")
    require(inner_product(group, chip, chip) == ONE, "chi prime irreducible norm")
    require(inner_product(group, chi, chip) == ZERO, "distinct irreducibles")
    require(inner_product(group, chi, trivial) == ZERO, "no invariant vector")
    require(inner_product(group, chip, trivial) == ZERO, "no invariant vector prime")

    unseen = set(group)
    classes = []
    while unseen:
        g = min(unseen)
        conjugacy_class = {compose(compose(inverse(x), g), x) for x in group}
        require(conjugacy_class <= unseen, "conjugacy partition")
        unseen -= conjugacy_class
        require(all(chi[u] == chi[g] and chip[u] == chip[g] for u in conjugacy_class), "class functions")
        classes.append((g, conjugacy_class))
    classes.sort(key=lambda item: (order(item[0]), min(item[1])))
    require(sorted(len(cl) for _, cl in classes) == [1, 12, 12, 15, 20], "A5 class sizes")
    phi = add(ONE, add(root_power(3), root_power(12)))
    phip = sub(ONE, phi)
    require(mul(phi, phi) == add(phi, ONE), "golden ratio quadratic equation")
    require(chi[c] == phi and chi[power(c, 2)] == phip, "five-cycle traces")
    require(chip[c] == phip and chip[power(c, 2)] == phi, "conjugate five-cycle traces")
    for g in group:
        if order(g) == 2:
            require(chi[g] == integer(-1), "involution trace")
        elif order(g) == 3:
            require(chi[g] == ZERO, "order three trace")
    # Every normal subgroup is a union of conjugacy classes containing identity.
    # Lagrange and the enumerated sizes exclude all proper nontrivial choices.
    nonidentity_sizes = [len(cl) for g, cl in classes if g != ID]
    candidate_normal_orders = []
    for mask in itertools.product((0, 1), repeat=len(nonidentity_sizes)):
        n = 1 + sum(m * s for m, s in zip(mask, nonidentity_sizes))
        if 60 % n == 0:
            candidate_normal_orders.append(n)
    require(sorted(set(candidate_normal_orders)) == [1, 60], "A5 simplicity class-size proof")
    require(60 > 6, "no faithful A5 action on three points")

    report = {
        "status": "EXACT_FINITE_CHARACTER_CERTIFICATE_PASSED",
        "arithmetic": "integers in Z[z]/(z^8-z^7+z^5-z^4+z^3-z+1)",
        "group_order": 60,
        "subgroup_orders": {"A4_point_stabilizer": 12, "V4": 4, "C5": 5},
        "identity": "chi3 = Ind_C5(theta) - Ind_A4(lambda) - Ind_A4(1) + 1",
        "conjugate_identity": "chi3prime uses theta^2",
        "character_inner_products": {"chi3_norm": 1, "chi3prime_norm": 1, "cross": 0, "trivial": 0},
        "complete_irreducible_degrees": [1, 3, 3, 4, 5],
        "all_25_character_orthogonality_pairs": "verified exactly",
        "classes": [{"representative": list(g), "element_order": order(g), "size": len(cl),
                     "chi3_in_z_basis": list(chi[g]), "chi3prime_in_z_basis": list(chip[g])}
                    for g, cl in classes],
        "candidate_normal_subgroup_orders": sorted(set(candidate_normal_orders)),
        "nonmonomial_reason": "A degree-three monomial character requires an index-three subgroup; simplicity forbids a nontrivial action on three points.",
        "analytic_scope": "No L-value, zero-free theorem, analytic continuation, or infinite-family statement is verified by this finite computation."
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
