#!/usr/bin/env python3
"""Bounded exact all-inner width/source-duality controls; not an analytic prover."""

import argparse
import ast
import hashlib
import importlib.util
import itertools
import json
import math
import subprocess
import sys
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
NOTE = HERE / "HARDY_INNER_WIDTH_SOURCE_DUALITY.md"
MANIFEST = HERE / "hardy_inner_width_source_duality.sources.json"
FIXTURE = HERE / "hardy_inner_width_source_duality.json"
TEST = ROOT / "tests/test_hardy_inner_width_source_duality.py"
BASE = "58be12463b3ff909eff0d491f606e87149efa9e4"
MAX_N, MAX_NUM, MAX_RATIONAL_DEGREE = 4, 2, 8
SOURCE_ROWS = [
    [
        "finite_physical_theorem",
        "a07e9c3ba093abb348b849e0356f6babdf591e84",
        "research/exploratory/HARDY_TRANSLATION_PHYSICAL_BAND_BOUND.md",
        "95338634d08fb5bde4d56d10197833b44ec64788",
        "efa2a1535e30e12e0fa20b1fabf49762843b50c72d0c8f6e44a70bbaa2feba3c",
    ],
    [
        "exact_arithmetic_helper",
        "a07e9c3ba093abb348b849e0356f6babdf591e84",
        "research/exploratory/hardy_translation_physical_band_bound.py",
        "3e8dcb2ea93cfdf7421fef2e6e33fcd20774dc2a",
        "755bd0ed8ee76e612d2c0d65619e4b9492f8e0c08d4574758f9aac44e06dc2e7",
    ],
    [
        "historical_confluent_interface",
        "8ef225b8753e2cd1f9c031fbb8038d1321c7f308",
        "research/exploratory/XI_CONFLUENT_SOURCE_BAND_OBSTRUCTION.md",
        "76152f000c026c4a68ade2593b16ffbd7e0de528",
        "750f7e22c14adcb8d3748e29d7a6b5b5e808fcab4998660c759a484800ef6146",
    ],
    [
        "historical_value_coefficient_mismatch",
        "81d52e569cc8bb566e54043fd692fd6157406aab",
        "claims/lemmas/L-106671-endpoint-free-energy-is-a-source-evaluation-pick-determinant.md",
        "d0488eccf2507bcb71c7e46f3f6f9c7013dd3998",
        "fc9bc89d9129ca22a9ededed2e3a6daf78c1371c9582d023487c326309d42764",
    ],
    [
        "literal_frozen_gauge",
        "81d52e569cc8bb566e54043fd692fd6157406aab",
        "claims/lemmas/L-106620-mesoscopic-frozen-riemann-siegel-gauge.md",
        "7fbf3731f286ddfc9eb1d10ede5941ab2156817a",
        "23e368f246606b0a8b4f53bec9e65e1dec21bdd207197387461268b4ca1bb7d0",
    ],
    [
        "height_sum_not_count",
        "81d52e569cc8bb566e54043fd692fd6157406aab",
        "claims/lemmas/L-106621-constant-scale-companion-height-budget.md",
        "fafa4b390bc140c8bb514dba83d41a5643cb77f1",
        "e41462ea71fd1f46849f75f7ff5dd6189514743e27bd3292bd1aec9292ec9065",
    ],
    [
        "cofinal_frontier",
        "81d52e569cc8bb566e54043fd692fd6157406aab",
        "claims/theorems/T-106620-mesoscopic-riemann-siegel-gauge-ninety-percent-frontier.md",
        "8db4fc42c3ea964c592224b64d0ad92b6c264018",
        "f926698271d06b2db02bd1d7e00a05034934d8b77a75496e137d127c565795b0",
    ],
    [
        "free_energy_frontier",
        "81d52e569cc8bb566e54043fd692fd6157406aab",
        "claims/theorems/T-106670-regularized-pick-free-energy-ninety-percent-equivalence.md",
        "9a61689c19b244f0176f753cef146b252256eab0",
        "b96ffe1ec8e5fc7d825e521c57c956066e25f0494e80aa4c13d4017ea98c8ae7",
    ],
]
EXTERNAL = (
    (
        "https://annals.math.princeton.edu/1975/102-1/p11",
        "Beckner 1975 sharp Hausdorff-Young; only classical nonsharp interpolation is used",
    ),
    (
        "https://doi.org/10.4099/jjm1924.2.0_129",
        "Takenaka 1925 orthogonal rational system; no novelty claim",
    ),
    (
        "https://arxiv.org/pdf/1605.07418v2",
        "Fricain-Hartmann-Ross (2.12), p8 and (2.18)-(2.19), p9: model decomposition and finite models",
    ),
)


def lf_sha(raw):
    return hashlib.sha256(raw.replace(b"\r\n", b"\n")).hexdigest()


def load_helper():
    row = SOURCE_ROWS[1]
    path = ROOT / row[2]
    # Authenticate resident executable bytes before import, not only historical Git bytes.
    if lf_sha(path.read_bytes()) != row[4]:
        raise ValueError("resident exact-helper source mismatch")
    name = "_hardy_width_authenticated_helper"
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ValueError("helper import unavailable")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


h = load_helper()
Q, Z, ONE = h.Q, h.ZERO, h.ONE
IU = Q(F(0), F(1))


def require(ok, message):
    if not ok:
        raise ArithmeticError(message)


def declared_poles(values, *, numerator=False):
    if type(numerator) is not bool:
        raise TypeError("numerator flag must be bool")
    if type(values) not in (list, tuple):
        raise TypeError("declared finite pole list required")
    h.integer(len(values), 0 if numerator else 1, MAX_NUM if numerator else MAX_N)
    return h.poles(values, allow_empty=numerator)


def diagonal(values):
    h.integer(len(values), 1, MAX_N)
    return h.matrix(
        tuple(
            tuple(v if i == j else Z for j in range(len(values)))
            for i, v in enumerate(values)
        )
    )


def determinant(mat):
    if type(mat) not in (tuple, list):
        raise TypeError("matrix list required")
    h.integer(len(mat), 1, MAX_N)
    mat = h.matrix(mat)
    n = h.integer(len(mat), 1, MAX_N)
    if len(mat[0]) != n:
        raise ValueError("square determinant required")
    total = Z
    for permutation in itertools.permutations(range(n)):
        inversions = sum(
            permutation[i] > permutation[j] for i in range(n) for j in range(i + 1, n)
        )
        term = h.gaussian((-1) ** inversions)
        for i, j in enumerate(permutation):
            term *= mat[i][j]
        total += term
    return total


def psd_control(mat):
    if type(mat) not in (tuple, list):
        raise TypeError("matrix list required")
    h.integer(len(mat), 1, MAX_N)
    mat = h.matrix(mat)
    n = h.integer(len(mat), 1, MAX_N)
    if len(mat[0]) != n or mat != h.adjoint(mat):
        raise ValueError("Hermitian square matrix required")
    minors = []
    rank = 0
    for k in range(1, n + 1):
        for subset in itertools.combinations(range(n), k):
            value = determinant(tuple(tuple(mat[i][j] for j in subset) for i in subset))
            if value.i or value.r < 0:
                raise ValueError("negative/nonreal principal minor")
            if value:
                rank = k
            minors.append(value.r)
    return {"rank": rank, "principal_minors": minors}


def rational_poly(values):
    if type(values) not in (tuple, list):
        raise TypeError("finite polynomial coefficient list required")
    h.integer(len(values), 1, MAX_RATIONAL_DEGREE + 1)
    # Raw int/Fraction components are input-capped; Q objects are already
    # checked intermediate values from the authenticated exact field helper.
    return h.poly(
        tuple(v if type(v) is Q else h.gaussian(h.rational(v)) for v in values)
    )


def product(left, right):
    left, right = rational_poly(left), rational_poly(right)
    h.integer(len(left) + len(right) - 2, 0, MAX_RATIONAL_DEGREE)
    return h.pm(left, right)


def complex_nodes(items):
    return tuple(Q(z.i, z.r) for z in items)


def blaschke(items):
    num, den = (ONE,), (ONE,)
    for b in complex_nodes(items):
        num, den = product(num, (-b, ONE)), product(den, (-b.conjugate(), ONE))
    return num, den


def taylor(poly, b, order):
    poly = rational_poly(poly)
    h.integer(order, 1, MAX_N)
    if type(b) is not Q:
        raise TypeError("Gaussian node required")
    return tuple(
        sum(
            (
                coefficient * math.comb(d, r) * b ** (d - r)
                for d, coefficient in enumerate(poly)
                if d >= r
            ),
            Z,
        )
        for r in range(order)
    )


def rational_jet(num, den, b, order):
    order = h.integer(order, 1, MAX_N)
    n, d = taylor(num, b, order), taylor(den, b, order)
    if not d[0]:
        raise ValueError("rational source has a pole at retained node")
    values = []
    for r in range(order):
        values.append(
            (n[r] - sum((d[k] * values[r - k] for k in range(1, r + 1)), Z)) / d[0]
        )
    return tuple(values)


def value_jet(basis, num, den):
    # Basis is the checked HT4 list (Laplace pole, order starting at one).
    basis = h.checked_basis(basis)
    h.integer(len(basis), 1, MAX_N)
    series = {
        z: rational_jet(num, den, Q(z.i, z.r), max(r for v, r in basis if v == z))
        for z, _ in basis
    }
    return h.matrix(
        tuple(
            tuple(series[z][r - s] if z == v and r >= s else Z for v, s in basis)
            for z, r in basis
        )
    )


def derivative_gram(basis):
    basis = h.checked_basis(basis)
    h.integer(len(basis), 1, MAX_N)
    return h.matrix(
        tuple(
            tuple(
                IU
                * ((-1) ** (r - 1))
                * math.comb(r + s - 2, r - 1)
                / (Q(z.i, z.r) - Q(v.i, -v.r)) ** (r + s - 1)
                for v, s in basis
            )
            for z, r in basis
        )
    )


def charge(g, a, weight):
    return h.tr(h.mm(h.mm(h.mm(h.inv(g), h.adjoint(a)), weight), a))


def duality_control(denominator, numerator):
    den = declared_poles(denominator)
    num = declared_poles(numerator, numerator=True)
    # R=O(Bplus-Bminus) has denominator degree n+m+1.
    h.integer(len(den) + len(num) + 1, 1, MAX_RATIONAL_DEGREE)
    basis = h.basis_from_poles(den)
    g = derivative_gram(basis)
    h.hpd_pivots(g)
    np, dp = blaschke(num)
    nm, dm = blaschke(den)
    jo = value_jet(basis, (Q(F(3), F(2)),), (2, -IU))
    jv = value_jet(basis, np, dp)
    a, c = h.adjoint(jv), h.adjoint(jo)
    # Build the actual rational source independently of multiplying value jets.
    rn = product((Q(F(3), F(2)),), h.pa(product(np, dm), h.ps(product(nm, dp), -1)))
    rd = product((2, -IU), product(dp, dm))
    jr = value_jet(basis, rn, rd)
    require(
        jr == h.mm(jo, jv) == h.mm(jv, jo), "literal R=O(Bplus-Bminus) jet mismatch"
    )
    rc = h.adjoint(jr)
    require(rc == h.mm(c, a) == h.mm(a, c), "dual source product mismatch")
    deficit = h.ma(g, h.ms(h.mm(h.mm(h.adjoint(a), g), a), -1))
    positivity = psd_control(deficit)
    gi = h.inv(g)
    p = h.mm(h.mm(a, gi), h.adjoint(a))
    inverse_positivity = psd_control(h.ma(gi, h.ms(p, -1)))
    # Independently match the physical Laplace Gram, with all derivative phases.
    phase = diagonal(tuple(IU ** (r - 1) for _, r in basis))
    gh = h.mm(h.mm(h.adjoint(phase), g), phase)
    ah = h.mm(h.mm(h.adjoint(phase), a), phase)
    require(gh == h.gram(basis), "HT4 derivative phase Gram mismatch")
    require(charge(g, a, g) == charge(gh, ah, gh), "phase charge mismatch")
    # A strictly positive abstract band surrogate, NOT an asserted Fourier band.
    trace_gi = h.tr(gi)
    require(not trace_gi.i and trace_gi.r > 0, "inverse trace not positive real")
    epsilon = F(1, 16) / (1 + trace_gi.r)
    bump = diagonal(
        tuple(epsilon if i == len(basis) - 1 else F(0) for i in range(len(basis)))
    )
    weight = h.ma(h.ms(g, F(1, 4)), bump)
    psd_control(weight)
    psd_control(h.ma(h.ms(g, F(1, 2)), h.ms(weight, -1)))
    go = h.mm(h.mm(h.adjoint(c), g), c)
    literal = charge(go, rc, weight)
    reduced = charge(g, a, weight)
    total = charge(g, a, g)
    require(literal == reduced, "outer source covariance mismatch")
    require(
        not literal.i and not total.i and 0 <= literal.r <= total.r / 2,
        "relative abstract-band inequality failed",
    )
    require(total.r <= len(basis), "physical charge exceeds rank")
    weighted_trace = h.tr(h.mm(p, weight))
    require(weighted_trace == literal, "inverse metric weight mismatch")
    tau = F(1, 2)
    normalized_det = determinant(
        h.ma(g, h.ms(h.mm(h.mm(h.adjoint(a), g), a), -tau))
    ) / determinant(g)
    source_det = determinant(
        h.ma(go, h.ms(h.mm(h.mm(h.adjoint(rc), g), rc), -tau))
    ) / determinant(go)
    require(normalized_det == source_det, "outer determinant covariance mismatch")
    return {
        "denominator": den,
        "numerator": num,
        "G_derivative": g,
        "J_value": jv,
        "A_dual": a,
        "C_outer_dual": c,
        "R_source_dual": rc,
        "physical_deficit": positivity,
        "inverse_metric_deficit": inverse_positivity,
        "HT4_G": gh,
        "HT4_A": ah,
        "correct_physical_charge": total,
        "literal_and_reduced_band_surrogate": literal,
        "incorrect_outer_metric_dropped": charge(g, rc, weight),
        "correct_source_determinant_at_half": source_det,
        "source_rational_identity_not_only_fitted_jets": True,
        "weight_is_abstract_not_a_computed_band": True,
        "C_A_commute": True,
        "C_A_noncommutation_with_G": (
            h.mm(c, g) != h.mm(g, c),
            h.mm(a, g) != h.mm(g, a),
        ),
    }


def orientation_falsifier():
    row = duality_control(((1, 0), (1, 1), (1, 2)), ((2, 0),))
    g, v = row["G_derivative"], row["J_value"]
    wrong = h.ma(g, h.ms(h.mm(h.mm(h.adjoint(v), g), v), -1))
    bad_det, bad_charge = determinant(wrong), charge(g, v, g)
    require(bad_det == h.gaussian(F(-64, 14625)), "held-out wrong determinant changed")
    require(bad_charge == h.gaussian(F(1943, 585)), "held-out wrong charge changed")
    require(
        row["correct_physical_charge"] == h.gaussian(F(235, 117)),
        "held-out physical charge changed",
    )
    require(row["physical_deficit"]["rank"] == 1, "rank-one model deficit changed")
    return {
        "raw_values": tuple(v[i][i] for i in range(3)),
        "wrong_deficit_determinant": bad_det,
        "wrong_charge": bad_charge,
        "correct_charge": row["correct_physical_charge"],
        "correct_deficit_rank": 1,
        "raw_value_physical_identification_refuted_with_this_Gram": True,
    }


def mt_control(values):
    items = declared_poles(values)
    basis = h.basis_from_poles(items)
    g = h.gram(basis)
    images = []
    common = h.product_linear(items)
    for j, z in enumerate(items):
        image = {(z, 1): ONE}
        for prior in items[:j]:
            image = h.multiply_inner(image, prior)
        require(all(key in basis for key in image), "MT function escaped model")
        direct_den = h.product_linear((z,) + items[:j])
        direct_num = h.product_linear(tuple(-v.conjugate() for v in items[:j]))
        direct = h.pm(h.divide_monic(common, direct_den), direct_num)
        reconstructed = (Z,)
        for (v, r), coefficient in image.items():
            reconstructed = h.pa(
                reconstructed,
                h.ps(h.divide_monic(common, h.product_linear((v,) * r)), coefficient),
            )
        require(direct == reconstructed, "MT full rational identity failed")
        images.append(image)
    synthesis = h.matrix(tuple(tuple(im.get(key, Z) for im in images) for key in basis))
    cross = h.mm(h.mm(h.adjoint(synthesis), g), synthesis)
    norms = diagonal(tuple(F(1, 2) / z.r for z in items))
    require(cross == norms, "MT exact cross-orthogonality failed")
    return {
        "poles": items,
        "dimension": len(items),
        "rational_columns_checked": len(items),
        "all_cross_Gram_entries_exact": True,
        "unnormalized_squared_norms": tuple(F(1, 2) / z.r for z in items),
        "normalization": "multiply column j by sqrt(2*y_j); square roots not numerically evaluated",
    }


def square_height_bound(roots, delta):
    if type(roots) not in (tuple, list):
        raise TypeError("finite exact square-root panel required")
    h.integer(len(roots), 1, MAX_N)
    roots = tuple(h.rational(v) for v in roots)
    delta = h.rational(delta)
    if any(v <= 0 for v in roots) or delta < 0:
        raise ValueError("positive height roots and nonnegative width required")
    n, total_root = len(roots), sum(roots)
    total_height = sum(v * v for v in roots)
    gap = n * total_height - total_root**2
    require(gap >= 0, "Cauchy-Schwarz height bound failed")
    return {
        "rank": n,
        "Delta": delta,
        "S": total_height,
        "sum_sqrt_height": total_root,
        "Cauchy_Schwarz_gap": gap,
        "coarse_beta_squared_with_constant_4": 16 * delta * total_root**2,
        "coarse_rank_normalized_bound_squared": 16 * delta * total_height / n,
        "pi_and_exact_HY_constant_not_numerically_evaluated": True,
    }


MT_CASES = (
    ((1, 0),),
    ((1, 0), (1, 1), (1, 2)),
    ((1, 1), (1, 1)),
    ((1, 0), (1, 0), (1, 0), (1, 0)),
    ((F(1, 4), -2), (F(1, 2), 3), (F(1, 4), -2)),
    ((1, 0), (1, F(1, 8)), (2, -1), (F(3, 2), 2)),
)
DUAL_CASES = (
    (((1, 0),), ()),
    (((1, 0),), ((1, 0),)),
    (((1, 0), (1, 0)), ((2, 0),)),
    (((1, 0), (1, 1), (1, 2)), ((2, 0),)),
    (((1, 1), (1, 1), (F(1, 2), -2)), ((2, 0), (1, 1))),
    (((1, 0), (1, 0), (2, 3), (2, 3)), ((F(3, 2), -1),)),
)
BOUND_ROOTS = ((F(1),), (F(1), F(2)), (F(1, 2), F(1, 3), F(1, 4)), (F(1),) * 4)


def expected_manifest():
    return {
        "schema": "hardy-inner-width-source-duality-sources-v1",
        "authoring_base": BASE,
        "source_scope": "all-inner finite-denominator theorem; explicit historical raw-value mismatch correction",
        "sources": [
            dict(zip(("role", "commit", "path", "git_blob", "sha256_lf"), row))
            for row in SOURCE_ROWS
        ],
        "external_contracts": [
            {"url": url, "contract": contract, "remote_bytes_authenticated": False}
            for url, contract in EXTERNAL
        ],
    }


def authenticate_sources(manifest=None):
    if manifest is None:
        manifest = h.read_json(MANIFEST)
    if h.canonical(manifest) != h.canonical(expected_manifest()):
        raise ValueError("complete typed source manifest mismatch")
    for _, commit, path, blob, digest in SOURCE_ROWS:
        ref = f"{commit}:{path}"
        actual_blob = (
            subprocess.check_output(["git", "rev-parse", ref], cwd=ROOT, timeout=15)
            .decode()
            .strip()
        )
        raw = subprocess.check_output(["git", "show", ref], cwd=ROOT, timeout=15)
        if actual_blob != blob or lf_sha(raw) != digest:
            raise ValueError("frozen primitive source identity mismatch")
    # Recheck loaded helper currency when building, even after module import.
    if lf_sha((ROOT / SOURCE_ROWS[1][2]).read_bytes()) != SOURCE_ROWS[1][4]:
        raise ValueError("resident helper changed after load")
    return {
        "source_count": len(SOURCE_ROWS),
        "manifest_sha256_canonical_json": hashlib.sha256(
            h.canonical(manifest).encode()
        ).hexdigest(),
        "resident_executable_helper_authenticated": True,
        "remote_bytes_authenticated": False,
    }


def build_report():
    auth = authenticate_sources()
    if any(
        isinstance(n, ast.Assert)
        for n in ast.walk(ast.parse(Path(__file__).read_text(encoding="utf-8")))
    ):
        raise ValueError("result checks must survive -O")
    mt = [mt_control(case) for case in MT_CASES]
    duals = [duality_control(den, num) for den, num in DUAL_CASES]
    return h.serialize(
        {
            "schema": "hardy-inner-width-source-duality-v1",
            "status": "NATIVE_PROOF_AND_BOUNDED_EXACT_CONTROLS_REQUIRING_INDEPENDENT_REVIEW",
            "arithmetic_class": "EXACT_RATIONAL",
            "arithmetic_domain": "Gaussian rationals; exact Fraction pairs",
            "rounding_contract": "no float, binary complex, Fourier quadrature, numerical pi or Xi values",
            "source_authentication": auth,
            "artifact_sha256_lf": {
                p.relative_to(ROOT).as_posix(): lf_sha(p.read_bytes())
                for p in (NOTE, Path(__file__), TEST, MANIFEST)
            },
            "caps": {
                "denominator_degree": MAX_N,
                "numerator_degree": MAX_NUM,
                "rational_degree": MAX_RATIONAL_DEGREE,
                "input_bits": h.INPUT_BITS,
                "intermediate_bits": h.INTERMEDIATE_BITS,
            },
            "coverage": {
                "MT_cases": len(mt),
                "MT_columns": sum(len(v) for v in MT_CASES),
                "dual_source_cases": len(duals),
                "bound_rows": len(BOUND_ROOTS) * 3,
                "unbounded_search": False,
            },
            "MT_controls": mt,
            "dual_source_controls": duals,
            "orientation_falsifier": orientation_falsifier(),
            "square_height_bounds": [
                square_height_bound(roots, delta)
                for roots in BOUND_ROOTS
                for delta in (F(0), F(1, 100), F(1))
            ],
            "scope": {
                "any_genuine_inner_numerator_by_analytic_proof": True,
                "finite_denominator_with_complex_nodes_and_confluence": True,
                "historical_value_coefficient_physical_mismatch_explicit": True,
                "historical_covariance_algebra_preserved": True,
                "correct_physical_source_dual_jets_required": True,
                "height_sum_used_as_count": False,
                "source_relative_bound_divided_by_rank": False,
                "infinite_numerator_degree_or_phase_moment_needed": False,
                "native_cofinal_denominator_count": False,
                "total_charge_bound": False,
                "free_energy_or_descent_closure": False,
                "RH_or_percentage": False,
                "analytic_proof_formally_verified": False,
                "numerical_Xi_samples": 0,
                "novelty_claim": False,
            },
        }
    )


def validate_report(report):
    if h.canonical(report) != h.canonical(build_report()):
        raise ValueError("complete source-authenticated typed report mismatch")


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
        validate_report(h.read_json(FIXTURE))
        print(
            "All-inner width / corrected source duality exact controls PASS; cofinal/free-energy/RH OPEN"
        )


if __name__ == "__main__":
    main()
