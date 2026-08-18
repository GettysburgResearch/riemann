from fractions import Fraction

# Exact safe-edge constant: 1/42 > 1/(8 sqrt(67)) iff 64*67 > 42^2.
assert 64 * 67 > 42 * 42


def hinge(x):
    return max(x, Fraction(0))


def deficit_plus(E, O, lam):
    TO = sum(a * t for a, t, r in O)
    RO = sum(a * r for a, t, r in O)
    return lam * TO + sum(a * hinge(r - lam * t) for a, t, r in E) - RO


def deficit_minus(E, O, lam):
    TE = sum(a * t for a, t, r in E)
    RE = sum(a * r for a, t, r in E)
    return lam * TE + sum(a * hinge(r - lam * t) for a, t, r in O) - RE


# Disjoint-union additivity and parity-swap identities.
A_E = [(Fraction(2), Fraction(3), Fraction(5)),
       (Fraction(1), Fraction(2), Fraction(7))]
A_O = [(Fraction(1), Fraction(4), Fraction(6))]
B_E = [(Fraction(3), Fraction(1), Fraction(2))]
B_O = [(Fraction(2), Fraction(5), Fraction(9))]

for lam in [Fraction(-3), Fraction(0), Fraction(1), Fraction(2), Fraction(10)]:
    assert deficit_plus(A_E + B_E, A_O + B_O, lam) == (
        deficit_plus(A_E, A_O, lam) + deficit_plus(B_E, B_O, lam)
    )
    assert deficit_minus(A_E + B_E, A_O + B_O, lam) == (
        deficit_minus(A_E, A_O, lam) + deficit_minus(B_E, B_O, lam)
    )
    assert deficit_plus(A_O, A_E, lam) == deficit_minus(A_E, A_O, lam)
    assert deficit_minus(A_O, A_E, lam) == deficit_plus(A_E, A_O, lam)


# One-parent / one-child exact Bellman equations with rational positive scale.
rho = Fraction(2, 7)
base_E = [(Fraction(1), Fraction(2), Fraction(5))]
base_O = [(Fraction(1), Fraction(1), Fraction(1))]
child_E = [(Fraction(2), Fraction(1), Fraction(4))]
child_O = [(Fraction(1), Fraction(3), Fraction(2))]

# Owner union = base + rho * parity-swapped child.  Source scaling is represented
# by capacity scaling, which is equivalent to scaling the entire finite ledger.
state_E = base_E + [(rho * a, t, r) for a, t, r in child_O]
state_O = base_O + [(rho * a, t, r) for a, t, r in child_E]

for lam in [Fraction(-5), Fraction(-1), Fraction(0), Fraction(1), Fraction(3), Fraction(9)]:
    assert deficit_plus(state_E, state_O, lam) == (
        deficit_plus(base_E, base_O, lam)
        + rho * deficit_minus(child_E, child_O, lam)
    )
    assert deficit_minus(state_E, state_O, lam) == (
        deficit_minus(base_E, base_O, lam)
        + rho * deficit_plus(child_E, child_O, lam)
    )


# Two-step elimination at one fixed hinge: D+ = g+ + R^2 D+.
r1 = Fraction(1, 5)
r2 = Fraction(1, 7)
fixtures = [
    tuple(map(Fraction, [3, -2, 4, 1, 5, -1])),
    tuple(map(Fraction, [1, 2, -3, 4, 6, 7])),
]
for d0p, d0m, d1p, d1m, d2p, d2m in fixtures:
    D2p, D2m = d2p, d2m
    D1p = d1p + r2 * D2m
    D1m = d1m + r2 * D2p
    D0p = d0p + r1 * D1m
    g0 = d0p + r1 * d1m
    assert D0p == g0 + (r1 * r2) * D2p

print("PASS_X_97700_FUTURE_PRIME_HINGE_BELLMAN")
print("safe_edge_square_gap=", 64 * 67 - 42 * 42)
