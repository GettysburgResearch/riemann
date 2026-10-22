#!/usr/bin/env python3
"""Exact compact moments for the tensor/symmetric-power ladder.

For independent Haar elements ``u,v`` of SU(2), compare

    X_r = chi_1(u) * chi_r(v)

with ``Y_r = chi_(2r+1)(w)`` for Haar ``w`` in SU(2).  The producer proves
closed formulas through degree eight, an all-even-moment coefficient formula,
the first universal split at degree six, and the low-rank corrections for the
generic USp(2r+2) standard trace.  Every runtime calculation is exact,
stdlib-only, bounded by ``r <= 16``, and protected by a logical-work cap.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import Counter, defaultdict
from pathlib import Path
from typing import Mapping, Sequence


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT_PATH = HERE / "elliptic_tensor_symmetric_power_moment_ladder.json"
NOTE_PATH = HERE / "ELLIPTIC_TENSOR_SYMMETRIC_POWER_MOMENT_LADDER.md"
TEST_PATH = ROOT / "tests" / "test_elliptic_tensor_symmetric_power_moment_ladder.py"

SCHEMA = "riemann.function_field.elliptic_tensor_symmetric_power_moment_ladder.v1"
FROZEN_MAX_R = 16
WEIGHT_FORMULA_MAX_N = 2 * FROZEN_MAX_R + 1
CG_REGRESSION_MAX_N = 16
MAX_HALF_MOMENT_ORDER = 4
ACCOUNTED_WORK_CAP_EXCLUSIVE = 30_000
CG_TRANSITION_CAP_INCLUSIVE = 21_000
CHARACTER_STATE_CAP_INCLUSIVE = 128
USp_STATE_CAP_INCLUSIVE = 64


SOURCE_LOCKS = {
    "all_r_subtorus_rigidity": {
        "fixture": HERE / "elliptic_tensor_symmetric_power_subtorus_rigidity.json",
        "producer": HERE / "elliptic_tensor_symmetric_power_subtorus_rigidity.py",
        "schema": "riemann.function_field.elliptic_tensor_symmetric_power_subtorus_rigidity.v1",
        "payload": "f05eea9c197c95af54e874bea437b7547acf42b5ccad50b29f7031b54d5c695d",
        "fixture_file": "59518d2a83fc11922b7ccb357b2fb11470725fc51c16803eccc9de5c6bad470d",
        "producer_file": "a9410d146fb9152c0ea835b48564343a8867c30d12e46798990a0c991463643b",
    },
    "r3_tensor_sym3_sym7": {
        "fixture": HERE / "elliptic_tensor_sym3_sym7_spectral_intersection.json",
        "producer": HERE / "elliptic_tensor_sym3_sym7_spectral_intersection.py",
        "schema": "riemann.function_field.elliptic_tensor_sym3_sym7_spectral_intersection.v1",
        "payload": "a1ec101912ba9712c015c2cbbd81022097ad113f2d6d0d9178ad7be4b43cfdbf",
        "fixture_file": "56837ead694fc113a5c3b82eee87c6a39b5af1a6a07564c4d78250f86ae9cb3e",
        "producer_file": "9d78faf0ca23c86060050d8420d6127e959062c0cf3829f97cc5986e0db47956",
    },
    "r2_tensor_sym2_sym5": {
        "fixture": HERE / "elliptic_tensor_sym2_sym5_spectral_intersection.json",
        "producer": HERE / "elliptic_tensor_sym2_sym5_spectral_intersection.py",
        "schema": "riemann.function_field.elliptic_tensor_sym2_sym5_spectral_intersection.v1",
        "payload": "e2c9c7ac3d1329b7b911a5214d36935d2694436cbe6d9cce551b94f8486b01ba",
        "fixture_file": "e583220e7df56765ef198d71a4a94887e8246992ba8fd9d127e8c1ce4e09cc32",
        "producer_file": "d414807d8c2bb41ee075c5526e22b243204f3e587e5988a55f91245a99f6d9e7",
    },
    "r1_so4_rankin_moments": {
        "fixture": HERE / "elliptic_pair_rankin_so4_family.json",
        "producer": HERE / "elliptic_pair_rankin_so4_family.py",
        "schema": "riemann.function_field.elliptic_pair_rankin_so4_family.v2",
        "payload": "3634ab438de17596fa7a616130a318b85b579178b6d87f017523dae25c53e028",
        "fixture_file": "6f10140f9ebcde3a85feadd3498c43214617cb62305cb8c610308c229d175a38",
        "producer_file": "2f3b0bab10135a626d0a05cde2a2fa75aa07e9bc62276411c1d0874bc2078545",
    },
}


def _canonical_sha256(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def _lf_sha256(path: Path) -> str:
    normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(normalized).hexdigest()


def _relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def _require_plain_int(name: str, value: object) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be a plain integer")
    return value


def _require_r(value: object) -> int:
    r = _require_plain_int("r", value)
    if r < 1 or r > FROZEN_MAX_R:
        raise ValueError(f"r must lie in 1..{FROZEN_MAX_R}")
    return r


def _require_n(value: object) -> int:
    n = _require_plain_int("highest weight", value)
    if n < 0 or n > WEIGHT_FORMULA_MAX_N:
        raise ValueError(f"highest weight must lie in 0..{WEIGHT_FORMULA_MAX_N}")
    return n


def _require_half_order(value: object, *, allow_zero: bool = False) -> int:
    k = _require_plain_int("half moment order", value)
    minimum = 0 if allow_zero else 1
    if k < minimum or k > MAX_HALF_MOMENT_ORDER:
        raise ValueError(
            f"half moment order must lie in {minimum}..{MAX_HALF_MOMENT_ORDER}"
        )
    return k


class ResourceGuard:
    """Fail closed on exact representation-ring work."""

    def __init__(self, cap: object = ACCOUNTED_WORK_CAP_EXCLUSIVE) -> None:
        cap_value = _require_plain_int("work cap", cap)
        if cap_value < 1:
            raise ValueError("work cap must be positive")
        self.cap = cap_value
        self.ledger: Counter[str] = Counter()
        self.cg_transitions = 0

    @property
    def total(self) -> int:
        return sum(self.ledger.values())

    def charge(self, name: object, units: object = 1) -> None:
        if not isinstance(name, str) or not name:
            raise TypeError("resource name must be a nonempty string")
        count = _require_plain_int("resource units", units)
        if count < 0:
            raise ValueError("resource units must be nonnegative")
        if self.total + count >= self.cap:
            raise RuntimeError(
                f"accounted work would meet or exceed exclusive cap {self.cap}"
            )
        self.ledger[name] += count

    def charge_cg_transition(self) -> None:
        if self.cg_transitions + 1 > CG_TRANSITION_CAP_INCLUSIVE:
            raise RuntimeError(
                "Clebsch-Gordan transition cap exceeded: "
                f"{self.cg_transitions + 1}>{CG_TRANSITION_CAP_INCLUSIVE}"
            )
        self.cg_transitions += 1
        self.charge("clebsch_gordan_tensor_summands")


def catalan_number(k: object) -> int:
    order = _require_half_order(k, allow_zero=True)
    return math.comb(2 * order, order) // (order + 1)


def su2_weight_difference_multiplicity(
    highest_weight: object,
    half_order: object,
    guard: ResourceGuard | None = None,
) -> int:
    """Multiplicity of V_0 in V_n^(tensor 2k), by adjacent weights.

    This is the coefficient of q^(k*n) in
    ``(1-q)*(1+q+...+q^n)^(2k)``.  Expanding the bounded geometric series
    gives the finite inclusion-exclusion sum used here.
    """

    n = _require_n(highest_weight)
    k = _require_half_order(half_order)
    degree = 2 * k - 2
    maximum_j = (k * n) // (n + 1)
    total = 0
    for j in range(maximum_j + 1):
        top = k * n - j * (n + 1) + degree
        term = math.comb(2 * k, j) * math.comb(top, degree)
        total = total - term if j % 2 else total + term
        if guard is not None:
            guard.charge("weight_difference_terms")
    if total < 1:
        raise ArithmeticError("SU(2) invariant multiplicity must be positive")
    return total


def su2_closed_even_moment(highest_weight: object, half_order: object) -> int:
    """Closed V_n trace moments for orders 0,2,4,6,8."""

    n = _require_n(highest_weight)
    k = _require_half_order(half_order, allow_zero=True)
    if k == 0 or k == 1:
        return 1
    if k == 2:
        return n + 1
    if k == 3:
        return (n + 1) * (n * n + 2 * n + 2) // 2
    numerator = (n + 1) * (n * n + n + 1) * (n * n + 3 * n + 3)
    if numerator % 3:
        raise ArithmeticError("the eighth-moment numerator lost divisibility by 3")
    return numerator // 3


def su2_cg_even_moments(
    highest_weight: object, guard: ResourceGuard | None = None
) -> dict[int, int]:
    """Independent Clebsch-Gordan recursion through tensor degree eight."""

    n = _require_n(highest_weight)
    if n > CG_REGRESSION_MAX_N:
        raise ValueError(
            f"Clebsch-Gordan regression is capped at n={CG_REGRESSION_MAX_N}"
        )
    multiplicities = {0: 1}
    moments = {0: 1}
    for tensor_degree in range(1, 2 * MAX_HALF_MOMENT_ORDER + 1):
        next_multiplicities: defaultdict[int, int] = defaultdict(int)
        for source_weight, multiplicity in multiplicities.items():
            for target_weight in range(
                abs(source_weight - n), source_weight + n + 1, 2
            ):
                next_multiplicities[target_weight] += multiplicity
                if guard is not None:
                    guard.charge_cg_transition()
        multiplicities = dict(next_multiplicities)
        if len(multiplicities) > CHARACTER_STATE_CAP_INCLUSIVE:
            raise RuntimeError(
                "character-state cap exceeded: "
                f"{len(multiplicities)}>{CHARACTER_STATE_CAP_INCLUSIVE}"
            )
        if tensor_degree % 2 == 0:
            moments[tensor_degree] = multiplicities.get(0, 0)
    return moments


def product_and_principal_moment_rows(r: object) -> dict[str, list[int]]:
    """Moments 0..8 of X_r and Y_r in the packet normalization."""

    index = _require_r(r)
    product: list[int] = []
    principal: list[int] = []
    for degree in range(2 * MAX_HALF_MOMENT_ORDER + 1):
        if degree % 2:
            product.append(0)
            principal.append(0)
            continue
        k = degree // 2
        product.append(catalan_number(k) * su2_closed_even_moment(index, k))
        principal.append(su2_closed_even_moment(2 * index + 1, k))
    return {"independent_product": product, "principal_symmetric_power": principal}


def moment_gap_formulas(r: object) -> dict[int, int]:
    """Principal minus product gaps in degrees six and eight."""

    index = _require_r(r)
    s = index + 1
    return {
        6: 3 * s * (s * s - 1) // 2,
        8: 2 * s * (s * s - 1) * (3 * s * s + 2),
    }


def _partition_neighbors(partition: tuple[int, ...], rank: int) -> tuple[tuple[int, ...], ...]:
    neighbors: list[tuple[int, ...]] = []
    for row in range(len(partition)):
        if row == 0 or partition[row] < partition[row - 1]:
            candidate = list(partition)
            candidate[row] += 1
            neighbors.append(tuple(candidate))
    if len(partition) < rank:
        neighbors.append(partition + (1,))
    for row in range(len(partition)):
        if row == len(partition) - 1 or partition[row] > partition[row + 1]:
            candidate = list(partition)
            candidate[row] -= 1
            if candidate[row] == 0:
                candidate = candidate[:row]
            neighbors.append(tuple(candidate))
    return tuple(neighbors)


def usp_standard_even_moments(
    rank: object, guard: ResourceGuard | None = None
) -> dict[int, int]:
    """USp(2g) standard moments from bounded oscillating tableaux."""

    g = _require_plain_int("symplectic rank", rank)
    if g < 2 or g > FROZEN_MAX_R + 1:
        raise ValueError(f"symplectic rank must lie in 2..{FROZEN_MAX_R + 1}")
    paths: dict[tuple[int, ...], int] = {(): 1}
    moments = {0: 1}
    for step in range(1, 2 * MAX_HALF_MOMENT_ORDER + 1):
        next_paths: defaultdict[tuple[int, ...], int] = defaultdict(int)
        for partition, count in paths.items():
            for neighbor in _partition_neighbors(partition, g):
                next_paths[neighbor] += count
                if guard is not None:
                    guard.charge("symplectic_oscillating_tableau_edges")
        paths = dict(next_paths)
        if len(paths) > USp_STATE_CAP_INCLUSIVE:
            raise RuntimeError(
                f"USp tableau-state cap exceeded: {len(paths)}>{USp_STATE_CAP_INCLUSIVE}"
            )
        if step % 2 == 0:
            moments[step] = paths.get((), 0)
    return moments


def usp_closed_even_moments(rank: object) -> dict[int, int]:
    """Closed USp(2g) standard moments through degree eight for g>=2."""

    g = _require_plain_int("symplectic rank", rank)
    if g < 2 or g > FROZEN_MAX_R + 1:
        raise ValueError(f"symplectic rank must lie in 2..{FROZEN_MAX_R + 1}")
    return {
        0: 1,
        2: 1,
        4: 3,
        6: 14 if g == 2 else 15,
        8: 84 if g == 2 else 104 if g == 3 else 105,
    }


def _load_authenticated_source(lock: Mapping[str, object]) -> dict[str, object]:
    fixture_path = lock.get("fixture")
    producer_path = lock.get("producer")
    if not isinstance(fixture_path, Path) or not isinstance(producer_path, Path):
        raise RuntimeError("internal source-lock path is malformed")
    if _lf_sha256(fixture_path) != lock.get("fixture_file"):
        raise RuntimeError(f"locked fixture file changed: {fixture_path.name}")
    if _lf_sha256(producer_path) != lock.get("producer_file"):
        raise RuntimeError(f"locked producer file changed: {producer_path.name}")
    fixture = json.loads(fixture_path.read_text(encoding="utf-8"))
    if fixture.get("schema") != lock.get("schema"):
        raise RuntimeError(f"locked fixture schema changed: {fixture_path.name}")
    if fixture.get("payload_sha256") != lock.get("payload"):
        raise RuntimeError(f"locked fixture payload changed: {fixture_path.name}")
    unhashed = dict(fixture)
    claimed = unhashed.pop("payload_sha256", None)
    if claimed != _canonical_sha256(unhashed):
        raise RuntimeError(f"locked fixture is internally inauthentic: {fixture_path.name}")
    return fixture


def load_locked_sources() -> dict[str, dict[str, object]]:
    sources = {
        name: _load_authenticated_source(lock) for name, lock in SOURCE_LOCKS.items()
    }
    rigidity = sources["all_r_subtorus_rigidity"].get(
        "primitive_subtorus_rigidity_theorem", {}
    )
    if rigidity.get("classification") != (
        "W_r(a,b)=O_r iff (|a|,|b|)=(r+1,1) or (1,2)"
    ):
        raise RuntimeError("locked all-r subtorus classification changed")

    r3 = sources["r3_tensor_sym3_sym7"].get("compact_trace_moment_context", {})
    if r3.get("Std_SU2_tensor_Sym3_SU2_independent_product") != [
        1, 0, 1, 0, 8, 0, 170, 0, 5096
    ] or r3.get("Sym7_SU2") != [1, 0, 1, 0, 8, 0, 260, 0, 11096]:
        raise RuntimeError("locked r=3 moment rows changed")

    r2 = sources["r2_tensor_sym2_sym5"].get("compact_trace_moment_fingerprint", {})
    if r2.get("Std_SU2_tensor_Sym2_SU2_independent_product") != [
        1, 0, 1, 0, 6, 0, 75, 0, 1274
    ] or r2.get("Sym5_SU2") != [1, 0, 1, 0, 6, 0, 111, 0, 2666]:
        raise RuntimeError("locked r=2 moment rows changed")

    r1 = sources["r1_so4_rankin_moments"].get("compact_image_discriminator", {})
    if r1.get("SO4_standard") != [1, 0, 1, 0, 4, 0, 25]:
        raise RuntimeError("locked r=1 product moments changed")
    if r1.get("Sym3_SU2") != [1, 0, 1, 0, 4, 0, 34]:
        raise RuntimeError("locked r=1 principal moments changed")
    if r1.get("generic_USp4_standard") != [1, 0, 1, 0, 3, 0, 14]:
        raise RuntimeError("locked r=1 generic USp moments changed")
    return sources


def _source_lock_payload() -> dict[str, object]:
    output: dict[str, object] = {}
    for name, lock in SOURCE_LOCKS.items():
        fixture = lock["fixture"]
        producer = lock["producer"]
        if not isinstance(fixture, Path) or not isinstance(producer, Path):
            raise RuntimeError("internal source-lock path is malformed")
        output[name] = {
            "fixture_path": _relative(fixture),
            "producer_path": _relative(producer),
            "schema": lock["schema"],
            "fixture_payload_sha256": lock["payload"],
            "fixture_sha256_lf_normalized": lock["fixture_file"],
            "producer_sha256_lf_normalized": lock["producer_file"],
        }
    return output


def _owned_file_locks() -> dict[str, object]:
    return {
        "note": {
            "path": _relative(NOTE_PATH),
            "sha256_lf_normalized": _lf_sha256(NOTE_PATH),
        },
        "producer": {
            "path": _relative(Path(__file__).resolve()),
            "sha256_lf_normalized": _lf_sha256(Path(__file__).resolve()),
        },
        "test": {
            "path": _relative(TEST_PATH),
            "sha256_lf_normalized": _lf_sha256(TEST_PATH),
        },
    }


def _predecessor_reproduction_rows() -> dict[str, object]:
    return {
        "r1": product_and_principal_moment_rows(1),
        "r2": product_and_principal_moment_rows(2),
        "r3": product_and_principal_moment_rows(3),
        "authentication": (
            "the r=1, r=2, r=3, and all-r rigidity fixtures are schema-, "
            "payload-, canonical-payload-, and LF-file-locked; each producer "
            "is independently LF-file-locked"
        ),
    }


def build_fixture() -> dict[str, object]:
    """Build the canonical exact moment-ladder packet."""

    guard = ResourceGuard()
    load_locked_sources()
    guard.charge("authenticated_predecessor_file_pairs", 2 * len(SOURCE_LOCKS))

    coefficient_checks = 0
    for n in range(WEIGHT_FORMULA_MAX_N + 1):
        for k in range(1, MAX_HALF_MOMENT_ORDER + 1):
            observed = su2_weight_difference_multiplicity(n, k, guard)
            expected = su2_closed_even_moment(n, k)
            if observed != expected:
                raise ArithmeticError(
                    f"weight-difference and closed formulas disagree at n={n}, k={k}"
                )
            coefficient_checks += 1
            guard.charge("closed_formula_comparisons")

    cg_selected_rows: list[dict[str, object]] = []
    for n in range(CG_REGRESSION_MAX_N + 1):
        moments = su2_cg_even_moments(n, guard)
        expected = {
            2 * k: su2_closed_even_moment(n, k)
            for k in range(MAX_HALF_MOMENT_ORDER + 1)
        }
        if moments != expected:
            raise ArithmeticError(f"Clebsch-Gordan regression failed at n={n}")
        guard.charge("clebsch_gordan_closed_formula_rows")
        if n in (0, 1, 2, 3, 5, 7, 16):
            cg_selected_rows.append(
                {"highest_weight_n": n, "even_moments_0_2_4_6_8": list(moments.values())}
            )

    ladder_rows: list[dict[str, object]] = []
    for r in range(1, FROZEN_MAX_R + 1):
        rows = product_and_principal_moment_rows(r)
        gaps = moment_gap_formulas(r)
        product = rows["independent_product"]
        principal = rows["principal_symmetric_power"]
        if product[:6] != principal[:6]:
            raise ArithmeticError(f"moment alias through degree four failed at r={r}")
        if principal[6] - product[6] != gaps[6] or principal[8] - product[8] != gaps[8]:
            raise ArithmeticError(f"closed moment gap failed at r={r}")
        if gaps[6] <= 0 or gaps[8] <= 0:
            raise ArithmeticError(f"moment gap lost positivity at r={r}")
        ladder_rows.append(
            {
                "r": r,
                "dimension": 2 * r + 2,
                "independent_product_moments_0_through_8": product,
                "principal_Sym_2r_plus_1_moments_0_through_8": principal,
                "principal_minus_product_degree_6": gaps[6],
                "principal_minus_product_degree_8": gaps[8],
            }
        )
        guard.charge("moment_ladder_rows")

    predecessor_rows = _predecessor_reproduction_rows()
    locked_expectations = {
        1: ([1, 0, 1, 0, 4, 0, 25], [1, 0, 1, 0, 4, 0, 34]),
        2: (
            [1, 0, 1, 0, 6, 0, 75, 0, 1274],
            [1, 0, 1, 0, 6, 0, 111, 0, 2666],
        ),
        3: (
            [1, 0, 1, 0, 8, 0, 170, 0, 5096],
            [1, 0, 1, 0, 8, 0, 260, 0, 11096],
        ),
    }
    for r, (product_expected, principal_expected) in locked_expectations.items():
        rows = predecessor_rows[f"r{r}"]
        product = rows["independent_product"]
        principal = rows["principal_symmetric_power"]
        if product[: len(product_expected)] != product_expected:
            raise RuntimeError(f"r={r} product predecessor reproduction failed")
        if principal[: len(principal_expected)] != principal_expected:
            raise RuntimeError(f"r={r} principal predecessor reproduction failed")
        guard.charge("predecessor_moment_reproductions", 2)

    usp_rows: list[dict[str, object]] = []
    for g in range(2, FROZEN_MAX_R + 2):
        observed = usp_standard_even_moments(g, guard)
        expected = usp_closed_even_moments(g)
        if observed != expected:
            raise ArithmeticError(f"USp oscillating-tableau count failed at rank {g}")
        structured_fourth = 2 * g
        if structured_fourth == expected[4]:
            raise ArithmeticError("structured and generic fourth moments unexpectedly agree")
        usp_rows.append(
            {
                "rank_g": g,
                "group": f"USp({2 * g})",
                "standard_even_moments_0_2_4_6_8": list(observed.values()),
                "structured_product_and_principal_fourth_moment": structured_fourth,
                "first_structured_vs_generic_separation_degree": 4,
            }
        )
        guard.charge("generic_USp_rows")

    fixture: dict[str, object] = {
        "schema": SCHEMA,
        "packet_id": "elliptic-tensor-symmetric-power-moment-ladder-v1",
        "status": (
            "EXACT_COMPACT_REPRESENTATION_THEOREM_WITH_BOUNDED_STDLIB_REGRESSIONS"
        ),
        "rigor_level": {
            "all_even_moment_coefficient_formula": "PROVED_FOR_EVERY_n_AND_k_BY_SU2_WEIGHT_DIFFERENCE",
            "closed_moments_through_degree_8": "PROVED_FOR_EVERY_n_GE_0",
            "product_principal_first_split": "PROVED_FOR_EVERY_r_GE_1",
            "generic_USp_comparison": "PROVED_BY_SYMPLECTIC_OSCILLATING_TABLEAUX",
            "bounded_runtime_checks": f"EXACT_FOR_1_LE_r_LE_{FROZEN_MAX_R}",
        },
        "normalization": {
            "SU2_character": "chi_n is the trace of V_n=Sym^n(Std), of dimension n+1",
            "independent_product": "X_r=chi_1(u)*chi_r(v), with u,v independent Haar SU(2)",
            "principal_slice": "Y_r=chi_(2r+1)(w), with w Haar SU(2)",
            "common_dimension": "dim(V_1 tensor V_r)=dim(V_(2r+1))=2r+2",
            "moments": "normalized Haar probability; traces are not divided by representation dimension",
        },
        "all_even_SU2_moment_theorem": {
            "notation": "B_k(n)=dim((V_n)^(tensor 2k))^SU(2)",
            "weight_difference": "B_k(n)=[q^(kn)] (1-q)*(1+q+...+q^n)^(2k)",
            "finite_sum": (
                "B_k(n)=sum_{0<=j<=floor(kn/(n+1))} (-1)^j*binom(2k,j)*"
                "binom(kn-j(n+1)+2k-2,2k-2)"
            ),
            "scope": "every integer n>=0 and k>=1; the producer evaluates only k<=4",
            "closed_B1": "1",
            "closed_B2": "n+1",
            "closed_B3": "(n+1)*(n^2+2n+2)/2",
            "closed_B4": "(n+1)*(n^2+n+1)*(n^2+3n+3)/3",
            "sixth_moment_triangle_certificate": (
                "B_3(n) counts triangle triples (a,b,c) in [0,n]^3: "
                "(n+1)^3-3*binom(n+2,3)"
            ),
        },
        "product_principal_all_moment_law": {
            "even_orders": "E[X_r^(2k)]=Catalan(k)*B_k(r); E[Y_r^(2k)]=B_k(2r+1)",
            "odd_orders": "both vanish: chi_1 and chi_(2r+1) change sign under the SU(2) center",
            "scope": "every r>=1 and k>=0",
        },
        "closed_moment_ladder_through_degree_8": {
            "put_s": "s=r+1",
            "common_degree_2": "1",
            "common_degree_4": "2s",
            "product_degree_6": "5*s*(s^2+1)/2",
            "principal_degree_6": "s*(4s^2+1)",
            "degree_6_gap_principal_minus_product": "3*s*(s^2-1)/2 = 3*r*(r+1)*(r+2)/2",
            "product_degree_8": "14*s*(s^4+s^2+1)/3",
            "principal_degree_8": "2*s*(16s^4+4s^2+1)/3",
            "degree_8_gap_principal_minus_product": (
                "2*s*(s^2-1)*(3s^2+2) = "
                "2*r*(r+1)*(r+2)*(3r^2+6r+5)"
            ),
            "universal_first_separation": (
                "the two laws agree in every degree <=4 and first differ in degree 6 for every r>=1"
            ),
            "frozen_exact_rows": ladder_rows,
        },
        "generic_USp_comparison": {
            "rank_convention": "g=r+1>=2 and the group is USp(2g)",
            "even_moments": {
                "degree_2": "1",
                "degree_4": "3",
                "degree_6": "14 for g=2; 15 for g>=3",
                "degree_8": "84 for g=2; 104 for g=3; 105 for g>=4",
            },
            "stable_range": (
                "the degree-2k moment is (2k-1)!! when g>=k; below stable range, "
                "partition-height/Pfaffian relations cause the displayed corrections"
            ),
            "detector_hierarchy": {
                "degree_2": "all three laws have moment 1",
                "degree_4": "both structured laws have 2g, versus generic USp moment 3",
                "degree_6": "the structured product and principal laws first separate",
            },
            "polarization_caveat": (
                "V_1 tensor V_r is symplectic only for even r and orthogonal for odd r; "
                "the USp comparison is polarization-matched to the product only when r is even, "
                "while V_(2r+1) is always symplectic"
            ),
            "frozen_exact_rows": usp_rows,
        },
        "bounded_exact_regressions": {
            "weight_difference_vs_closed": {
                "highest_weights_checked": f"0..{WEIGHT_FORMULA_MAX_N}",
                "half_orders_checked": "1..4",
                "exact_comparisons": coefficient_checks,
            },
            "Clebsch_Gordan_vs_closed": {
                "highest_weights_checked": f"0..{CG_REGRESSION_MAX_N}",
                "tensor_degrees_checked": [2, 4, 6, 8],
                "selected_rows": cg_selected_rows,
            },
            "predecessor_reproductions": predecessor_rows,
        },
        "source_and_owned_file_locks": {
            "source_locks": _source_lock_payload(),
            "owned_file_locks": _owned_file_locks(),
            "authentication": (
                "source fixtures are schema-, payload-, canonical-payload-, and LF-file-locked; "
                "source producers and this packet's note, producer, and test are LF-file-locked"
            ),
        },
        "resource_contract": {
            "frozen_maximum_r": FROZEN_MAX_R,
            "maximum_runtime_moment_order": 2 * MAX_HALF_MOMENT_ORDER,
            "exclusive_accounted_work_unit_cap": guard.cap,
            "inclusive_Clebsch_Gordan_transition_cap": CG_TRANSITION_CAP_INCLUSIVE,
            "inclusive_character_state_cap": CHARACTER_STATE_CAP_INCLUSIVE,
            "inclusive_USp_tableau_state_cap": USp_STATE_CAP_INCLUSIVE,
            "accounted_work_unit_ledger": {
                **dict(sorted(guard.ledger.items())),
                "total_accounted_work_units": guard.total,
            },
            "actual_Clebsch_Gordan_transitions": guard.cg_transitions,
            "floating_point_results": 0,
            "random_samples": 0,
            "runtime_symbolic_packages": 0,
            "numerical_integrations": 0,
            "finite_fields_curves_or_models_enumerated": 0,
        },
        "scope_firewall": {
            "compact_not_arithmetic": (
                "these are Haar laws of compact representation images, not finite-family moment theorems"
            ),
            "no_monodromy_recovery": (
                "a finite trace-moment fingerprint does not determine arithmetic origin or monodromy"
            ),
            "no_pointwise_alias_from_moments": (
                "moment matching through degree four is not equality of spectra or probability laws"
            ),
            "no_all_r_computation_claim": (
                "the formulas are proved symbolically for all r, but runtime regression is capped at r<=16"
            ),
            "no_analytic_or_RH_claim": (
                "compact representation identities imply no analytic continuation, automorphy, zero-free region, RH, or GRH theorem"
            ),
            "no_novelty_priority_claim": (
                "the elementary representation-ring formulas are recorded without a literature-priority claim"
            ),
        },
        "next_targets": [
            "translate the degree-six detector into finite-family centered moments with explicit error terms",
            "classify the correct generic orthogonal comparison for odd r",
            "extend the closed B_k(n) factorization study beyond k=4 without fitting finite data",
        ],
    }
    fixture["payload_sha256"] = _canonical_sha256(fixture)
    return fixture


def _write_fixture(fixture: Mapping[str, object]) -> None:
    OUTPUT_PATH.write_text(
        json.dumps(fixture, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


def _check_fixture(fixture: Mapping[str, object]) -> None:
    if not OUTPUT_PATH.exists():
        raise RuntimeError(f"missing fixture: {OUTPUT_PATH}")
    stored = json.loads(OUTPUT_PATH.read_text(encoding="utf-8"))
    if stored != fixture:
        raise RuntimeError("stored moment-ladder fixture is stale")


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true", help="write the canonical JSON")
    mode.add_argument("--check", action="store_true", help="check the stored JSON")
    args = parser.parse_args(argv)
    fixture = build_fixture()
    if args.write:
        _write_fixture(fixture)
        print(f"wrote {OUTPUT_PATH}")
    elif args.check:
        _check_fixture(fixture)
        print(f"PASS {fixture['payload_sha256']}")
    else:
        print(json.dumps(fixture, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
