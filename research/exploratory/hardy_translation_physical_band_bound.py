#!/usr/bin/env python3
"""Exact bounded Gaussian-rational controls, not a formal analytic prover."""

import argparse
import ast
import collections
import hashlib
import json
import math
import subprocess
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
NOTE = HERE / "HARDY_TRANSLATION_PHYSICAL_BAND_BOUND.md"
MANIFEST = HERE / "hardy_translation_physical_band_bound.sources.json"
FIXTURE = HERE / "hardy_translation_physical_band_bound.json"
TEST = ROOT / "tests/test_hardy_translation_physical_band_bound.py"
BASE = "8ef225b8753e2cd1f9c031fbb8038d1321c7f308"
MAX_DEGREE, MAX_POLY, INPUT_BITS, INTERMEDIATE_BITS = 6, 13, 16, 2048
SOURCE_ROWS = (
    (
        "frozen_gauge",
        "81d52e569cc8bb566e54043fd692fd6157406aab",
        "claims/lemmas/L-106620-mesoscopic-frozen-riemann-siegel-gauge.md",
        "7fbf3731f286ddfc9eb1d10ede5941ab2156817a",
        "23e368f246606b0a8b4f53bec9e65e1dec21bdd207197387461268b4ca1bb7d0",
    ),
    (
        "source_Pick_and_confluent_jets",
        "81d52e569cc8bb566e54043fd692fd6157406aab",
        "claims/lemmas/L-106671-endpoint-free-energy-is-a-source-evaluation-pick-determinant.md",
        "d0488eccf2507bcb71c7e46f3f6f9c7013dd3998",
        "fc9bc89d9129ca22a9ededed2e3a6daf78c1371c9582d023487c326309d42764",
    ),
    (
        "Hardy_Laplace_normalization",
        "81d52e569cc8bb566e54043fd692fd6157406aab",
        "claims/lemmas/L-106673-unregularized-cauchy-volume-is-logarithmic-laplace-transport.md",
        "cadbbee0c5864d4cdb9b110bc0ddc0938e0bcb54",
        "f7d68d9e64c2fb31da6db72bcd93971630cac2273fcb789052baa0679ad36b20",
    ),
    (
        "value_nonnormality_boundary",
        "81d52e569cc8bb566e54043fd692fd6157406aab",
        "claims/lemmas/L-106650-truncated-toeplitz-value-nonnormality-split.md",
        "8e80ee4e7460618807e8a041197ec6a63137672c",
        "178dd723a0e255bc897145a9459e03b685f6f03e75fa463aa2d42c8b7472dfe2",
    ),
    (
        "physical_free_energy_target",
        "81d52e569cc8bb566e54043fd692fd6157406aab",
        "claims/theorems/T-106670-regularized-pick-free-energy-ninety-percent-equivalence.md",
        "9a61689c19b244f0176f753cef146b252256eab0",
        "b96ffe1ec8e5fc7d825e521c57c956066e25f0494e80aa4c13d4017ea98c8ae7",
    ),
    (
        "open_Xi_transfer",
        "81d52e569cc8bb566e54043fd692fd6157406aab",
        "claims/theorems/T-106710-xi-carrier-adapted-source-softening-frontier.md",
        "b06d973198898a93d584b67dbe26ce24823e2ffc",
        "1a1f27c31dccd2a3393675acfc444e712a1449b476a2e1d7812f0e4c5559eb9f",
    ),
    (
        "source_softening_firewall",
        "81d52e569cc8bb566e54043fd692fd6157406aab",
        "claims/refutations/R-106710-diagonal-source-softening-does-not-control-topological-free-energy.md",
        "e17fdf16e87d6791c64fbb6f0ac8f604ca46c396",
        "889fd0cf65cefcf83705e54d0dda5525880fc94c4542ca0be6fa40724e1107c1",
    ),
    (
        "reviewed_actual_Xi_concentration",
        "3b6972320899a82c6caa3a98e2ada5ff703a605a",
        "research/exploratory/XI_ACTUAL_KERNEL_LAPLACE_CONCENTRATION.md",
        "fa24f9c8e0a87709d1a297a4e72136c1135d066c",
        "f7f89abe2e54d0d8df72dc830162b2083bc4f05d402c3aa70eca464678e80246",
    ),
    (
        "independent_concentration_review",
        "f3d074190e64a97ac935b93c5b628568cde90858",
        "research/exploratory/XI_ACTUAL_KERNEL_LAPLACE_CONCENTRATION_AUDIT.md",
        "da9032e15eb7be89557a54120b74fc9596c527d9",
        "aaf60c26b34296aa2e23bdad1469fce8ed3efe5ec27063d14d666f3fa5ce0536",
    ),
    (
        "earlier_single_kernel_scout",
        "939a24962a4c6a449c0b56e3b20f78b936f35f6c",
        "research/exploratory/XI_NEAR_ADAPTED_SCALE_FIREWALL.md",
        "0461a5c159d9d1094a9849e362d02ac1149a0143",
        "b770dc30ee6ab5406e159230c6ea617a1e5b1616b818dabb4c4c7f37f4408eac",
    ),
    (
        "frozen_confluent_source_and_uniform_envelope",
        "8ef225b8753e2cd1f9c031fbb8038d1321c7f308",
        "research/exploratory/XI_CONFLUENT_SOURCE_BAND_OBSTRUCTION.md",
        "76152f000c026c4a68ade2593b16ffbd7e0de528",
        "750f7e22c14adcb8d3748e29d7a6b5b5e808fcab4998660c759a484800ef6146",
    ),
    (
        "cofinal_exhaustion_not_degree_bound",
        "81d52e569cc8bb566e54043fd692fd6157406aab",
        "claims/theorems/T-106620-mesoscopic-riemann-siegel-gauge-ninety-percent-frontier.md",
        "8db4fc42c3ea964c592224b64d0ad92b6c264018",
        "f926698271d06b2db02bd1d7e00a05034934d8b77a75496e137d127c565795b0",
    ),
    (
        "topological_charge_not_removed",
        "81d52e569cc8bb566e54043fd692fd6157406aab",
        "claims/lemmas/L-106674-topological-factor-and-balanced-phase-free-energy.md",
        "813d7af130c880e013de165ce3be831a8ebe03ed",
        "3015f3b0e5f6e15f0065090ef70b2d175f70d3fd0894db4f483a681f73135f5d",
    ),
)
EXTERNAL_CONTRACTS = (
    (
        "https://people.tamu.edu/~terdelyi/papers-online/shift_sub.pdf",
        "Borwein-Erdelyi 2006: finite-interval Nikolskii theorem; dimension/evaluation/translation proof, not an attributed exact half-line constant",
    ),
    (
        "https://arxiv.org/pdf/1605.07418v2",
        "Fricain-Hartmann-Ross v2: (2.12) K_uv=K_u orthogonal_plus u K_v; (2.18)-(2.19) finite Blaschke models",
    ),
)


def integer(value, low, high):
    if type(value) is not int or not low <= value <= high:
        raise ValueError("integer outside declared resource/domain cap")
    return value


def rational(value):
    if type(value) not in (int, F):
        raise TypeError("exact int/Fraction required; bool/float rejected")
    value = F(value)
    if max(value.numerator.bit_length(), value.denominator.bit_length()) > INPUT_BITS:
        raise ValueError("rational input bit cap")
    return value


@dataclass(frozen=True)
class Q:
    r: F = F(0)
    i: F = F(0)

    def __post_init__(self):
        for item in (self.r, self.i):
            if type(item) is not F:
                raise TypeError("Gaussian components must be Fractions")
            if (
                max(item.numerator.bit_length(), item.denominator.bit_length())
                > INTERMEDIATE_BITS
            ):
                raise ValueError("Gaussian intermediate bit cap")

    def __bool__(self):
        return bool(self.r or self.i)

    def __add__(self, other):
        other = gaussian(other)
        return Q(self.r + other.r, self.i + other.i)

    __radd__ = __add__

    def __neg__(self):
        return Q(-self.r, -self.i)

    def __sub__(self, other):
        return self + (-gaussian(other))

    def __rsub__(self, other):
        return gaussian(other) + (-self)

    def __mul__(self, other):
        other = gaussian(other)
        return Q(
            self.r * other.r - self.i * other.i, self.r * other.i + self.i * other.r
        )

    __rmul__ = __mul__

    def conjugate(self):
        return Q(self.r, -self.i)

    def __truediv__(self, other):
        other = gaussian(other)
        norm = other.r**2 + other.i**2
        if not norm:
            raise ZeroDivisionError("zero Gaussian denominator")
        value = self * other.conjugate()
        return Q(value.r / norm, value.i / norm)

    def __rtruediv__(self, other):
        return gaussian(other) / self

    def __pow__(self, exponent):
        exponent = integer(exponent, 0, 2 * MAX_DEGREE + 1)
        result = gaussian(1)
        for _ in range(exponent):
            result *= self
        return result


def gaussian(value):
    if type(value) is Q:
        return value
    if type(value) in (int, F):
        return Q(F(value))
    raise TypeError("Gaussian rational required; no binary complex values")


ZERO, ONE = gaussian(0), gaussian(1)


def poles(values, allow_empty=False):
    if type(allow_empty) is not bool:
        raise TypeError("allow_empty must be boolean")
    if type(values) not in (tuple, list):
        raise TypeError("pole list required")
    integer(len(values), 0 if allow_empty else 1, MAX_DEGREE)
    result = []
    for pair in values:
        if type(pair) not in (tuple, list) or len(pair) != 2:
            raise ValueError("pole needs exact (positive height, real phase)")
        y, a = map(rational, pair)
        if y <= 0:
            raise ValueError("strictly positive pole height required")
        result.append(Q(y, a))
    return tuple(result)


def basis_from_poles(items):
    integer(len(items), 1, MAX_DEGREE)
    if any(type(z) is not Q or z.r <= 0 for z in items):
        raise ValueError("positive-height Gaussian poles required")
    counts = collections.Counter(items)
    return tuple(
        (z, r)
        for z in sorted(counts, key=lambda z: (z.r, z.i))
        for r in range(1, counts[z] + 1)
    )


def matrix(values):
    if type(values) not in (tuple, list):
        raise TypeError("matrix list or tuple required")
    rows = integer(len(values), 1, MAX_DEGREE)
    if type(values[0]) not in (tuple, list):
        raise ValueError("matrix row required")
    cols = integer(len(values[0]), 1, MAX_DEGREE)
    if any(type(row) not in (tuple, list) or len(row) != cols for row in values):
        raise ValueError("ragged matrix")
    return tuple(tuple(gaussian(value) for value in values[i]) for i in range(rows))


def adjoint(mat):
    mat = matrix(mat)
    return tuple(
        tuple(mat[i][j].conjugate() for i in range(len(mat)))
        for j in range(len(mat[0]))
    )


def mm(left, right):
    left, right = matrix(left), matrix(right)
    if len(left[0]) != len(right):
        raise ValueError("matrix dimensions do not conform")
    return tuple(
        tuple(
            sum((left[i][k] * right[k][j] for k in range(len(right))), ZERO)
            for j in range(len(right[0]))
        )
        for i in range(len(left))
    )


def ma(left, right):
    left, right = matrix(left), matrix(right)
    if (len(left), len(left[0])) != (len(right), len(right[0])):
        raise ValueError("matrix shapes differ")
    return tuple(tuple(a + b for a, b in zip(r, s)) for r, s in zip(left, right))


def ms(mat, scalar):
    mat, scalar = matrix(mat), gaussian(scalar)
    return tuple(tuple(value * scalar for value in row) for row in mat)


def eye(size):
    size = integer(size, 1, MAX_DEGREE)
    return tuple(
        tuple(ONE if i == j else ZERO for j in range(size)) for i in range(size)
    )


def inv(mat):
    mat = matrix(mat)
    size = len(mat)
    if len(mat[0]) != size:
        raise ValueError("inverse requires square matrix")
    work = [list(row) + list(unit) for row, unit in zip(mat, eye(size))]
    for k in range(size):
        pivot = next((j for j in range(k, size) if work[j][k]), None)
        if pivot is None:
            raise ValueError("singular matrix")
        work[k], work[pivot] = work[pivot], work[k]
        divisor = work[k][k]
        work[k] = [value / divisor for value in work[k]]
        for j in range(size):
            if j != k:
                scale = work[j][k]
                work[j] = [a - scale * b for a, b in zip(work[j], work[k])]
    return tuple(tuple(row[size:]) for row in work)


def tr(mat):
    mat = matrix(mat)
    if len(mat) != len(mat[0]):
        raise ValueError("trace requires square matrix")
    return sum((mat[i][i] for i in range(len(mat))), ZERO)


def hpd_pivots(mat):
    mat = matrix(mat)
    if mat != adjoint(mat):
        raise ValueError("Hermitian matrix required")
    work = [list(row) for row in mat]
    pivots = []
    for k in range(len(work)):
        pivot = work[k][k]
        if pivot.i or pivot.r <= 0:
            raise ValueError("matrix is not positive definite")
        pivots.append(pivot.r)
        for i in range(k + 1, len(work)):
            for j in range(k + 1, len(work)):
                work[i][j] -= work[i][k] * work[k][j] / pivot
    return tuple(pivots)


def checked_basis(basis):
    if type(basis) not in (tuple, list):
        raise TypeError("finite basis list or tuple required")
    integer(len(basis), 1, MAX_DEGREE)
    result = []
    for item in basis:
        if type(item) not in (tuple, list) or len(item) != 2:
            raise ValueError("basis element needs pole and order")
        z, r = item
        if type(z) is not Q or z.r <= 0:
            raise ValueError("positive-height Gaussian pole required")
        result.append((z, integer(r, 1, MAX_DEGREE)))
    expected = basis_from_poles(tuple(z for z, _ in result))
    if len(set(result)) != len(result) or set(result) != set(expected):
        raise ValueError("basis orders must exhaust each confluent block exactly")
    return tuple(result)


def gram(basis):
    basis = checked_basis(basis)
    return tuple(
        tuple(
            gaussian(
                F(
                    math.factorial(r + s - 2),
                    math.factorial(r - 1) * math.factorial(s - 1),
                )
            )
            / (z.conjugate() + v) ** (r + s - 1)
            for v, s in basis
        )
        for z, r in basis
    )


def generator(basis):
    basis = checked_basis(basis)
    size = integer(len(basis), 1, MAX_DEGREE)
    return tuple(
        tuple(
            -z if i == j else ONE if basis[i] == (z, r - 1) else ZERO
            for j, (z, r) in enumerate(basis)
        )
        for i in range(size)
    )


def translation_control(items):
    basis = basis_from_poles(items)
    g, a = gram(basis), generator(basis)
    c = (tuple(ONE if r == 1 else ZERO for _, r in basis),)
    pivots, gi = hpd_pivots(g), inv(g)
    boundary = mm(adjoint(c), c)
    if ma(mm(adjoint(a), g), mm(g, a)) != ms(boundary, -1):
        raise ArithmeticError("native Lyapunov identity failed")
    derivative = ma(mm(a, gi), mm(gi, adjoint(a)))
    if derivative != ms(mm(mm(gi, boundary), gi), -1):
        raise ArithmeticError("phase-safe kernel derivative identity failed")
    origin = mm(mm(c, gi), adjoint(c))[0][0]
    if origin != gaussian(2 * sum(z.r for z in items)):
        raise ArithmeticError("origin normalization failed")
    if tr(mm(gi, g)) != gaussian(len(items)):
        raise ArithmeticError("integrated diagonal dimension failed")
    return {
        "dimension": len(items),
        "basis_poles_and_orders": basis,
        "G": g,
        "A": a,
        "c": c,
        "positive_LDL_pivots": pivots,
        "origin_kernel": origin,
        "integrated_kernel": len(items),
        "both_Lyapunov_identities_exact": True,
    }


def poly(values):
    if type(values) not in (tuple, list):
        raise TypeError("polynomial list or tuple required")
    integer(len(values), 1, MAX_POLY)
    out = [gaussian(v) for v in values]
    while len(out) > 1 and not out[-1]:
        out.pop()
    return tuple(out)


def pa(left, right):
    left, right = poly(left), poly(right)
    return poly(
        tuple(
            (left[i] if i < len(left) else ZERO)
            + (right[i] if i < len(right) else ZERO)
            for i in range(max(len(left), len(right)))
        )
    )


def ps(values, scalar):
    return poly(tuple(value * gaussian(scalar) for value in poly(values)))


def pm(left, right):
    left, right = poly(left), poly(right)
    size = len(left) + len(right) - 1
    integer(size, 1, MAX_POLY)
    result = [ZERO] * size
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return poly(result)


def product_linear(items):
    result = (ONE,)
    for z in items:
        result = pm(result, (z, ONE))
    return result


def divide_monic(numerator, denominator):
    numerator, denominator = poly(numerator), poly(denominator)
    if denominator[-1] != ONE or len(numerator) < len(denominator):
        raise ValueError("exact monic division required")
    remainder = list(numerator)
    quotient = [ZERO] * (len(numerator) - len(denominator) + 1)
    for j in range(len(quotient) - 1, -1, -1):
        value = remainder[j + len(denominator) - 1]
        quotient[j] = value
        for k, coefficient in enumerate(denominator):
            remainder[j + k] -= value * coefficient
    if any(remainder):
        raise ValueError("polynomial division has nonzero remainder")
    return poly(quotient)


def multiply_inner(image, pole):
    out = dict(image)
    for (z, r), coefficient in image.items():
        terms = {}
        if pole == z:
            terms[(z, r + 1)] = ONE
        else:
            delta = pole - z
            for k in range(1, r + 1):
                terms[(z, k)] = gaussian((-1) ** (r - k)) / delta ** (r - k + 1)
            terms[(pole, 1)] = gaussian((-1) ** r) / delta**r
        for key, value in terms.items():
            out[key] = out.get(key, ZERO) - 2 * pole.r * coefficient * value
    return {key: value for key, value in out.items() if value}


def physical_control(denominator, numerator):
    # Count before allocation; multiplicities are pole-list repetition, not duplicate columns.
    if type(denominator) not in (tuple, list) or type(numerator) not in (tuple, list):
        raise TypeError("pole lists required")
    integer(len(denominator) + len(numerator), 1, MAX_DEGREE)
    den, num = poles(denominator), poles(numerator, allow_empty=True)
    source_basis, target_basis = basis_from_poles(den), basis_from_poles(den + num)
    images = []
    for basis_item in source_basis:
        image = {basis_item: ONE}
        for pole in num:
            image = multiply_inner(image, pole)
        if any(key not in target_basis for key in image):
            raise ArithmeticError("physical image escaped product model")
        images.append(image)
    inclusion = tuple(
        tuple(image.get(key, ZERO) for image in images) for key in target_basis
    )
    gs, gt = gram(source_basis), gram(target_basis)
    if mm(mm(adjoint(inclusion), gt), inclusion) != gs:
        raise ArithmeticError("physical inner multiplication lost exact isometry")
    common = product_linear(den + num)
    inner_numerator = product_linear(tuple(-z.conjugate() for z in num))
    for (z, r), image in zip(source_basis, images):
        direct_denominator = product_linear((z,) * r + num)
        direct = pm(divide_monic(common, direct_denominator), inner_numerator)
        reconstructed = (ZERO,)
        for (v, s), coefficient in image.items():
            reconstructed = pa(
                reconstructed,
                ps(divide_monic(common, product_linear((v,) * s)), coefficient),
            )
        if direct != reconstructed:
            raise ArithmeticError("full cross-multiplied rational identity failed")
    return {
        "n_denominator": len(den),
        "m_numerator": len(num),
        "d_product": len(den + num),
        "denominator_poles": den,
        "numerator_poles": num,
        "translation": translation_control(den + num),
        "physical_inclusion_matrix": inclusion,
        "J_star_G_product_J_equals_G_denominator": True,
        "rational_identity_columns_checked": len(source_basis),
    }


def band_factor(degree, a, b):
    degree = integer(degree, 1, MAX_DEGREE)
    a, b = rational(a), rational(b)
    if not 0 < a < b:
        raise ValueError("band requires 0<A<B")
    raw = degree * (b - a) / b
    return {
        "degree": degree,
        "A": a,
        "B": b,
        "trace_bound": raw,
        "unit_vector_bound": min(F(1), raw),
    }


def countercontrols():
    # M_b exp(-t)=exp(-t)*(1-2t); no exponential is numerically evaluated.
    p_half, p_one = 1 - 2 * F(1, 2), 1 - 2 * F(1)
    if p_half != 0 or p_one != -1:
        raise ArithmeticError("nonmonotone physical image control failed")
    return {
        "physical_rank_one_polynomial": (1, -2),
        "zero_at_t_half": p_half,
        "square_coefficient_at_t_one_before_exp_minus_two": 2 * p_one**2,
        "delay_family": "[-(x-i*(2*m/T))/(x+i*(2*m/T))]^m",
        "denominator_rank_and_height": (1, 1),
        "ideal_shift_band_mass": "1-exp(-2*L)",
        "relative_band_width": "L/(T+L)",
        "order_of_choices": "fixed L>0; T tends to infinity; then m sufficiently large for each T",
        "finite_degree_needed_not_actual_Xi_example": True,
    }


def source_covariance_control():
    # Genuine complex confluent jets commute with each other, not with G/H.
    g = gram(basis_from_poles(poles(((1, 1), (1, 1)))))
    c = matrix(((Q(F(1), F(1)), Q(F(2), F(-1))), (0, Q(F(1), F(1)))))
    v = matrix(((Q(F(2), F(-1)), Q(F(1), F(1))), (0, Q(F(2), F(-1)))))
    h = ma(ms(g, F(1, 4)), matrix(((0, 0), (0, F(1, 64)))))
    hpd_pivots(h)
    hpd_pivots(ma(ms(g, F(1, 2)), ms(h, -1)))
    if mm(c, v) != mm(v, c):
        raise ArithmeticError("jet algebra commutation failed")
    if any(mm(j, g) == mm(g, j) or mm(j, h) == mm(h, j) for j in (c, v)):
        raise ArithmeticError("held-out noncommutation control degenerated")
    go, jr = mm(mm(adjoint(c), g), c), mm(c, v)
    literal = tr(mm(mm(mm(inv(go), adjoint(jr)), h), jr))
    reduced = tr(mm(mm(mm(inv(g), adjoint(v)), h), v))
    dropped = tr(mm(mm(mm(inv(g), adjoint(jr)), h), jr))
    total = tr(mm(mm(mm(inv(go), adjoint(jr)), g), jr))
    if literal != reduced or dropped == literal:
        raise ArithmeticError(
            "source metric covariance or dropping-outer control failed"
        )
    if literal.i or total.i or not 0 < literal.r <= total.r / 2:
        raise ArithmeticError("exact source relative-band inequality failed")
    return {
        "G": g,
        "C": c,
        "V": v,
        "H": h,
        "G_O": go,
        "J_R": jr,
        "literal_and_reduced_trace": literal,
        "incorrect_dropped_outer_trace": dropped,
        "total_trace": total,
        "H_below_half_G_by_positive_exact_LDL": True,
        "C_V_commute_but_neither_commutes_G_or_H": True,
        "H_is_abstract_positive_weight_not_claimed_actual_Xi_band": True,
    }


def canonical(data):
    return json.dumps(data, sort_keys=True, separators=(",", ":"), allow_nan=False)


def sha256_lf(raw):
    return hashlib.sha256(raw.replace(b"\r\n", b"\n")).hexdigest()


def read_json(path):
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise ValueError("duplicate JSON key")
            result[key] = value
        return result

    def constant(value):
        raise ValueError("nonfinite JSON constant: " + value)

    return json.loads(
        path.read_text(encoding="utf-8"),
        object_pairs_hook=pairs,
        parse_constant=constant,
    )


def expected_manifest():
    return {
        "schema": "hardy-translation-physical-band-sources-v1",
        "authoring_base": BASE,
        "source_scope": "finite Blaschke numerator and finite denominator subfactor; no Xi cofinal degree bound",
        "sources": [
            {
                "role": role,
                "commit": commit,
                "path": path,
                "git_blob": blob,
                "sha256_lf": digest,
            }
            for role, commit, path, blob, digest in SOURCE_ROWS
        ],
        "external_contracts": [
            {"url": url, "contract": contract, "remote_bytes_authenticated": False}
            for url, contract in EXTERNAL_CONTRACTS
        ],
    }


def authenticate_sources(manifest=None):
    if manifest is None:
        manifest = read_json(MANIFEST)
    if canonical(manifest) != canonical(expected_manifest()):
        raise ValueError("complete typed source contract differs")
    for _, commit, path, blob, digest in SOURCE_ROWS:
        ref = f"{commit}:{path}"
        actual = (
            subprocess.check_output(["git", "rev-parse", ref], cwd=ROOT, timeout=15)
            .decode()
            .strip()
        )
        raw = subprocess.check_output(["git", "show", ref], cwd=ROOT, timeout=15)
        if actual != blob or sha256_lf(raw) != digest:
            raise ValueError("frozen primitive source identity mismatch")
    return {
        "source_count": len(SOURCE_ROWS),
        "manifest_sha256_canonical_json": hashlib.sha256(
            canonical(manifest).encode()
        ).hexdigest(),
        "remote_bytes_authenticated": False,
    }


def serialize(data):
    if type(data) is Q:
        return {"re": str(data.r), "im": str(data.i)}
    if type(data) is F:
        return str(data)
    if type(data) in (list, tuple):
        return [serialize(value) for value in data]
    if type(data) is dict:
        return {key: serialize(value) for key, value in data.items()}
    return data


CASES = (
    (((1, 0),), ()),
    (((1, 0), (2, 3)), ((F(1, 2), 1),)),
    (((1, 1), (1, 1)), ((1, 1),)),
    (((1, 0), (1, 0), (F(3, 2), -2)), ((2, 1), (2, 1))),
    (((F(1, 2), -7), (F(1, 3), 11)), ((F(1, 5), -7), (5, 2))),
)


def build_report():
    auth = authenticate_sources()
    if any(
        isinstance(item, ast.Assert)
        for item in ast.walk(ast.parse(Path(__file__).read_text(encoding="utf-8")))
    ):
        raise ValueError("result-bearing assertions cannot disappear under -O")
    controls = [physical_control(den, num) for den, num in CASES]
    return serialize(
        {
            "schema": "hardy-translation-physical-band-v1",
            "status": "NATIVE_ANALYTIC_PROOF_WITH_BOUNDED_EXACT_CONTROLS",
            "arithmetic_class": "EXACT_RATIONAL",
            "arithmetic_domain": "Gaussian rationals represented by exact Fraction pairs; complex matrices and polynomials",
            "rounding_contract": "no float/complex approximations, quadrature, numerical exponentials or eigenvalues",
            "source_authentication": auth,
            "artifact_sha256_lf": {
                path.relative_to(ROOT).as_posix(): sha256_lf(path.read_bytes())
                for path in (NOTE, Path(__file__), TEST, MANIFEST)
            },
            "caps": {
                "total_degree": MAX_DEGREE,
                "polynomial_coefficients": MAX_POLY,
                "rational_input_bits": INPUT_BITS,
                "Gaussian_intermediate_bits": INTERMEDIATE_BITS,
            },
            "coverage": {
                "predeclared_native_cases": len(CASES),
                "rational_identity_columns": sum(
                    row["n_denominator"] for row in controls
                ),
                "band_rows": MAX_DEGREE * 3,
                "unbounded_search": False,
            },
            "native_controls": controls,
            "band_factors": [
                band_factor(d, a, b)
                for d in range(1, MAX_DEGREE + 1)
                for a, b in ((1, 2), (10, 11), (100, 101))
            ],
            "countercontrols": countercontrols(),
            "source_covariance_control": source_covariance_control(),
            "scope": {
                "arbitrary_finite_nodes_phases_and_confluence": True,
                "kernel_diagonal_monotone_by_native_proof": True,
                "pointwise_degree_coefficient": 1,
                "pointwise_constant_claimed_optimal": False,
                "finite_numerator_degree_is_paid": True,
                "finite_physical_inner_band_Gram_controlled": True,
                "literal_outer_source_jet_metric_retained": True,
                "unweighted_cutoff": "n=o(X^2*exp(X))",
                "physical_cutoff": "m+n=o(X^2*exp(X))",
                "actual_Xi_degree_bound_proved": False,
                "height_sum_used_as_degree_bound": False,
                "infinite_inner_approximation_error_controlled": False,
                "outer_or_inner_commuted_with_projection": False,
                "total_free_energy_bound": False,
                "topological_index_removed": False,
                "analytic_proof_formally_machine_verified": False,
                "novelty_claim": False,
                "RH_or_critical_line_percentage": False,
                "Xi_numerical_samples": 0,
            },
        }
    )


def validate_report(report):
    if canonical(report) != canonical(build_report()):
        raise ValueError("complete source-authenticated typed rebuild differs")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--emit-report", action="store_true")
    mode.add_argument("--emit-manifest", action="store_true")
    args = parser.parse_args()
    if args.emit_manifest:
        print(json.dumps(expected_manifest(), indent=2, sort_keys=True))
    elif args.emit_report:
        print(json.dumps(build_report(), indent=2, sort_keys=True))
    else:
        validate_report(read_json(FIXTURE))
        print(
            "Hardy translation: exact source/complex Gram/inner controls PASS; Xi degree/free-energy/RH OPEN"
        )


if __name__ == "__main__":
    main()
