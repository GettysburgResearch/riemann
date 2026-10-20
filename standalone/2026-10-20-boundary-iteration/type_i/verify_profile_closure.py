"""Exact source-profile algebra; no analytic continuation certification."""
from fractions import Fraction as F
from itertools import product, permutations
from pathlib import Path
from hashlib import sha256
import json


def require(condition, detail="exact check failed"):
    if not condition:
        raise RuntimeError(detail)

# Z[rho], rho=exp(2*pi*i/9), Phi_9(rho)=rho^6+rho^3+1.
ZERO = (0,) * 6
ONE = (1, 0, 0, 0, 0, 0)


def reduce9(coefficients):
    a = [0] * 9
    for k, value in enumerate(coefficients):
        a[k % 9] += value
    for k in (8, 7, 6):
        a[k - 3] -= a[k]
        a[k - 6] -= a[k]
    return tuple(a[:6])


def rho(n):
    a = [0] * 9
    a[n % 9] = 1
    return reduce9(a)


def plus(x, y):
    return tuple(a + b for a, b in zip(x, y))


def times(x, y):
    a = [0] * 11
    for i, u in enumerate(x):
        for j, v in enumerate(y):
            a[i + j] += u * v
    return reduce9(a)


def scale(n, x):
    return tuple(n * a for a in x)


def conjugate(x):
    out = ZERO
    for i, a in enumerate(x):
        out = plus(out, scale(a, rho(-i)))
    return out


def total(xs):
    out = ZERO
    for x in xs:
        out = plus(out, x)
    return out


def determinant(m):
    out = ZERO
    for perm in permutations(range(3)):
        parity = sum(perm[i] > perm[j] for i in range(3) for j in range(i + 1, 3))
        term = ONE
        for i in range(3):
            term = times(term, m[i][perm[i]])
        out = plus(out, scale((-1) ** parity, term))
    return out


def mul_e(x, y):
    return (x[0] * y[0] - x[1] * y[1],
            x[0] * y[1] + x[1] * y[0] - x[1] * y[1])


def power_e(x, n):
    out = (F(1), F(0))
    if n < 0:
        x = (F(-1, 3), F(-2, 3))  # inverse of lambda
    for _ in range(abs(n)):
        out = mul_e(out, x)
    return out


LAMBDA = (F(1), F(2))
UNITS = [(1, 0), (0, 1), (-1, -1), (-1, 0), (0, -1), (1, 1)]


def additive(j, unit, a2, a3, rotation=0, sign=1):
    c = (1 - 3 * a2 - 3 * a3, -6 * a3)
    x = mul_e(power_e(LAMBDA, j),
              mul_e(UNITS[unit], mul_e(c, UNITS[rotation])))
    e = 9 * sign * (2 * x[0] - x[1])
    require(e.denominator == 1)
    return rho(int(e))


def rotate(unit, k):
    return (unit % 3 + k) % 3 + 3 * (unit // 3)


def tau_profile(j, unit, a2, a3, kind):
    """Source tau coefficient, removing its common positive real magnitude."""
    t, negative = unit % 3, unit // 3
    chi = rho(3 * (t * a2 + a3))
    if kind == 0:
        if j >= -3 and j % 3 == 0 and t == 0:
            return ONE
        if j >= -1 and j % 3 == 2:
            return times(rho([0, -1, 1][t]), chi)
        return ZERO
    if j != -4 or (kind == 1 and negative) or (kind == 2 and not negative):
        return ZERO
    phase = ([3, 5, 1] if kind == 1 else [6, -1, 4])[t]
    return times(rho(phase), chi)


# Exact transcription of DR arXiv:2109.07463v3, Appendix A.
# (tau kind, tau argument omega rotation, scalar omega exponent,
#  additive sign, additive omega rotation).
TABLE = [
    (0, 0, 0, 0, 0), (0, 0, 0, 1, 1), (0, 0, 0, -1, 1),
    (0, 1, 0, 0, 0), (0, 1, 0, -1, 0), (0, 1, 0, 1, 0),
    (0, 2, 0, 0, 0), (0, 2, 0, -1, 0), (0, 2, 0, 1, 0),
    (2, 1, 1, 1, 0), (2, 2, 1, 0, 0), (2, 1, 1, 0, 0),
    (2, 0, 1, 1, 2), (2, 0, 1, -1, 1), (2, 2, 0, -1, 2),
    (2, 0, 0, -1, 0), (2, 0, 0, 0, 0), (2, 0, 0, 1, 0),
    (1, 2, 2, 1, 0), (1, 1, 2, 0, 0), (1, 2, 2, 0, 0),
    (1, 0, 2, 1, 1), (1, 1, 2, 1, 2), (1, 2, 2, 1, 2),
    (1, 0, 0, -1, 0), (1, 0, 0, 0, 0), (1, 0, 0, 1, 0)
]


def raw_profile(row, j, a, ray_b, a2, a3):
    kind, rotation, scalar, sign, additive_rotation = TABLE[row - 1]
    out = ZERO
    for unit in range(6):
        minus_unit = (unit + 3) % 6
        coefficient = times(rho(3 * scalar),
                            tau_profile(j, rotate(minus_unit, rotation), a2, a3, kind))
        if sign:
            coefficient = times(coefficient,
                                additive(j, minus_unit, a2, a3, additive_rotation, sign))
        coefficient = conjugate(coefficient)
        # Actual primitive twist psi_r(unit), including row dependence.
        phase = scale((-1) ** ((unit // 3) * a),
                      rho(3 * (unit % 3) * (a - ray_b)))
        out = plus(out, times(coefficient, phase))
    return out


def minor(m):
    # Columns are kappa_(a,-1), a=0,1,2; rows are source cusps22,26,27.
    b_exponent = [6, 4, -1]  # (omega², rho*omega, rho^-1)
    trace = [2, -1, -1]
    out = [[], [], []]
    for a in range(3):
        t_shift = (2 - a) % 3
        t_plain = (-a) % 3
        out[0].append(rho(3 + b_exponent[t_shift] + 3 * t_shift * m
                          - trace[(t_shift + 1) % 3]))
        out[1].append(rho(b_exponent[t_plain] + 3 * t_plain * m))
        out[2].append(rho(b_exponent[t_shift] + 3 * t_shift * m - trace[t_shift]))
    return out


determinants = {}
for m in range(3):
    matrix = minor(m)
    for i, j in product(range(3), repeat=2):
        value = total(times(conjugate(matrix[k][i]), matrix[k][j]) for k in range(3))
        require(value == (scale(3, ONE) if i == j else ZERO))
    det = determinant(matrix)
    require(times(det, conjugate(det)) == scale(27, ONE))
    determinants[str(m)] = list(det)

minor_cases = 0
for a, ray_b, a2, a3 in product(range(6), range(3), range(3), range(3)):
    matrix = minor((a - ray_b) % 3)
    characters = [rho(3 * (column * a2 - a3)) for column in range(3)]
    for i, row in enumerate([22, 26, 27]):
        expected = scale((-1) ** a,
                         total(times(matrix[i][column], characters[column])
                               for column in range(3)))
        require(raw_profile(row, -4, a, ray_b, a2, a3) == expected)
        minor_cases += 1

# Exhaust all profile values in the fixed ramified strata. Higher j in each
# nonzero class differ by scalar geometric ratios and have trivial additive phase.
allowed = {(0, 0), (0, 2), (1, 2), (2, 2)}
support_cases = 0
for row, j, a, ray_b in product(range(1, 28), [-4, -3, -1, 0, 2], range(6), range(3)):
    values = {(a2, a3): raw_profile(row, j, a, ray_b, a2, a3)
              for a2, a3 in product(range(3), repeat=2)}
    for u, v in product(range(3), repeat=2):
        coefficient_times_nine = total(
            times(value, rho(-3 * (u * a2 + v * a3)))
            for (a2, a3), value in values.items())
        if (u, v) not in allowed:
            require(coefficient_times_nine == ZERO, (row, j, a, ray_b, u, v))
    support_cases += 1

directory = Path(__file__).resolve().parent
receipt = {
    "status": "PASS",
    "scope": "Exact finite coefficient algebra only; this does not certify the accompanying analytic argument.",
    "source": {
        "url": "https://arxiv.org/html/2109.07463v3",
        "html_sha256": "3949e0f0ae87808d84fe02c12a3b68c5b66aa8d967d8ecb5e1605f1d985b956d",
        "locations": ["(5.7)", "(5.13)", "(5.14)", "Appendix A"]
    },
    "minor_rows": [22, 26, 27],
    "minor_source_coefficient_cases": minor_cases,
    "full_table_profile_support_cases": support_cases,
    "matrix_identity": "M^* M = 3 I for all three effective angular residues",
    "determinants_in_basis_1_rho_rho2_rho3_rho4_rho5": determinants,
    "determinant_absolute_square": 27,
    "checker_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
    "proof_sha256": sha256((directory / "FINITE_PROFILE_CLOSURE.md").read_bytes()).hexdigest()
}
(directory / "profile_verification.json").write_text(json.dumps(receipt, indent=2) + "\n",
                                                     encoding="utf8")
print(json.dumps(receipt, indent=2))
