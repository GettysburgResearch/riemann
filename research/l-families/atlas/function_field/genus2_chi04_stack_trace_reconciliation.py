#!/usr/bin/env python3
"""Guarded primary-source reconciliation for the marked genus-two chi_(0,4) trace.

This producer performs no finite-field enumeration and no network access.  It
source-locks the exact project theorem and marked-stack adapter, records the
manually audited primary-source ledger, verifies the relevant Sp4 branching
identity in a bounded Laurent ring, and checks the exact motivic bookkeeping
that relates the BFG ambient conjecture to the marked-curve theorem.

The literature statements remain manually audited dependencies.  The packet
does not turn a conjectural source formula into a proof and makes no novelty
claim.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import unicodedata
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from itertools import pairwise
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT_PATH = HERE / "genus2_chi04_stack_trace_reconciliation.json"
NOTE_PATH = HERE.parent / "GENUS2_CHI04_STACK_TRACE_RECONCILIATION.md"
TEST_PATH = ROOT / "tests" / "test_genus2_chi04_stack_trace_reconciliation.py"

B4_FIXTURE_PATH = HERE / "genus2_b4_triangular_trace_average.json"
B4_PRODUCER_PATH = HERE / "genus2_b4_triangular_trace_average.py"
B4_NOTE_PATH = HERE / "GENUS2_B4_TRIANGULAR_TRACE_AVERAGE.md"
B4_TEST_PATH = ROOT / "tests" / "test_genus2_b4_triangular_trace_average.py"
ADAPTER_PATH = HERE / "genus2_marked_weierstrass_stack_adapter.json"

MAX_EXACT_OPERATIONS = 1_024

SOURCE_LOCKS: dict[str, dict[str, str]] = {
    "genus2_b4_triangular_trace_average.json": {
        "lf_sha256": "31eec8f78bc81eb9d157f727c229efb16d112b94e7c27dbf0ea1f81f5005fde2",
        "payload_sha256": "d12099e24425badd5106f61caa151578ee04dd099a221eca7217b599783c5e5b",
        "schema": "riemann.function_field.genus2_b4_triangular_trace_average.v1",
    },
    "genus2_b4_triangular_trace_average.py": {
        "lf_sha256": "2f9435fa90b608bfa641d16bc64bc1e5c2c5898432be0e7c1ce99bd61c81591a",
    },
    "GENUS2_B4_TRIANGULAR_TRACE_AVERAGE.md": {
        "lf_sha256": "d24d668837b5291609074481282f44588f37a886bb81f4565fc4d1b1efdc4811",
    },
    "test_genus2_b4_triangular_trace_average.py": {
        "lf_sha256": "e7f56eba47af85a706de9b3e673e3673e0b75d3664fde9a2a7e2e12caa2053f5",
    },
    "genus2_marked_weierstrass_stack_adapter.json": {
        "lf_sha256": "fe8f23f6379a70ea150a8e4f1b87054553536fde3bd23e6c1d21e252baf3b26c",
        "payload_sha256": "7b091cc158c7ff378774dcbaef5802c469c3d377384034bced1caf4fe92b3601",
        "schema": "riemann.function_field.genus2_marked_weierstrass_stack_adapter.v1",
    },
}

LITERATURE_ARTIFACTS: tuple[dict[str, object], ...] = (
    {
        "key": "bergstrom_pointed_hyperelliptic",
        "authors": "Jonas Bergstrom",
        "title": (
            "Equivariant counts of points of the moduli spaces of pointed "
            "hyperelliptic curves"
        ),
        "url": "https://arxiv.org/abs/math/0611813",
        "version": "arXiv v2, 30 November 2011",
        "pdf_sha256": (
            "12457527533aa0898375b5085c29cd0dec88e77ef4612a8810baac01ba92d5cd"
        ),
        "locators": [
            "Introduction and Section 7: local systems only through weight 7",
            (
                "Theorem 11.6 (arXiv PDF p. 29): only weights 4 and 6, "
                "hence no V_(4,4) row"
            ),
            ("Section 2: H_(g,n) marks arbitrary curve points, not Weierstrass points"),
            (
                "Definition 12.1, Lemma 12.8, Remark 12.9 "
                "(arXiv PDF pp. 29-31): ramification coordinates only"
            ),
        ],
        "claim_boundary": (
            "proves arbitrary-point and unmarked results through weight 7; "
            "does not print V_(4,4) or an all-q M_2(w^1) trace"
        ),
    },
    {
        "key": "faber_vandergeer_level_one",
        "authors": "Carel Faber, Gerard van der Geer",
        "title": (
            "Sur la cohomologie des systemes locaux sur les espaces des "
            "modules des courbes de genre 2 et des surfaces abeliennes"
        ),
        "url": "https://arxiv.org/abs/math/0305094",
        "version": "arXiv v1, 6 May 2003",
        "pdf_sha256": (
            "986f0f98303db367099ffa676fff0cbb19857e9ebd830082a4213c04cb053021"
        ),
        "eprint_source_sha256": (
            "0a4ab2c29f192423d3069c157caf2cdae09dfd1353fde51dff5280590a2e20fc"
        ),
        "locators": [
            "Section 1: level-one M_2 and A_2 and local systems V_(l,m)",
            (
                "Section 2 (arXiv PDF p. 2): Eisenstein theorem is regular; "
                "l=m>0 even is explicitly exceptional in the expected extension"
            ),
            ("Section 4: endoscopic contribution and total formula are conjectural"),
            "Section 5: finite-field computations for selected q, not all-q theorems",
            "Section 8: M_(2,n) has n arbitrary ordered points",
        ],
        "claim_boundary": (
            "contains no w^1 moduli problem and no printed V_(4,4) formula; "
            "its relevant level-one framework is partly conjectural"
        ),
    },
    {
        "key": "bergstrom_faber_vandergeer_level_two",
        "authors": "Jonas Bergstrom, Carel Faber, Gerard van der Geer",
        "title": (
            "Siegel modular forms of genus 2 and level 2: cohomological "
            "computations and conjectures"
        ),
        "url": "https://arxiv.org/abs/0803.0917",
        "version": "arXiv v2, 20 April 2008",
        "pdf_sha256": (
            "f6294c69e2cafe16b4b0dc1ba1692a46813ba6e467e546aa548442d1a4f2a19e"
        ),
        "eprint_source_sha256": (
            "5780b581522ec17d4dfacc202b277f92e9b464fc54ef5f60dcc8ef56b660e5f0"
        ),
        "locators": [
            (
                "Section 2 (arXiv PDF pp. 2-3): definitions of M_2(w^n), "
                "A_2(w^n), and A_2[2]"
            ),
            (
                "Theorem 4.2 and Theorem 4.4: proved only for regular (l,m); "
                "the l=m convention is explicitly conjectural"
            ),
            (
                "Corollary 4.5: A_2(w^1) Eisenstein formula, again only for "
                "regular (l,m)"
            ),
            "Section 5: exact computer data only for odd q<=37",
            (
                "Section 9 (arXiv PDF p. 12): numerical Euler checks on the "
                "ambient A_2(w^1)"
            ),
            (
                "Section 10 (arXiv PDF p. 12): explicitly conjectural "
                "A_2[2], V_(4,4) example row"
            ),
        ],
        "claim_boundary": (
            "defines the target geometry and predicts ambient cohomology, but "
            "does not print or prove an all-q M_2(w^1), V_(4,4) formula"
        ),
    },
    {
        "key": "bergstrom_2025_author_erratum",
        "authors": "Jonas Bergstrom",
        "title": "Erratum",
        "url": (
            "https://www.su.se/download/18.1f09f4df19a7bbe0dfd6a83e/"
            "1764771423396/Erratum.pdf"
        ),
        "version": "2 December 2025",
        "pdf_sha256": (
            "b064eef272d63a2a9b604647d25a346b825f48cba430399c14b144d477af16a3"
        ),
        "locators": [
            (
                "p. 1: corrected conjectural A_2[2], V_(4,4) row "
                "15L^6-45L^5+30+15Phi_(4,6)-5Phi_(4,12)"
            ),
            "p. 2: correction to Example 7.10 of the pointed paper",
        ],
        "claim_boundary": (
            "corrects an ambient full-level example table; it does not add an "
            "M_2(w^1) theorem"
        ),
    },
)


@dataclass
class OperationGuard:
    limit: int = MAX_EXACT_OPERATIONS
    used: int = 0

    def consume(self, amount: int = 1) -> None:
        if amount < 0:
            raise ValueError("operation increment must be nonnegative")
        self.used += amount
        if self.used > self.limit:
            raise RuntimeError(
                f"exact operation cap exceeded: {self.used}>{self.limit}"
            )


def _normalize_json(value: object) -> object:
    if isinstance(value, str):
        return unicodedata.normalize("NFC", value)
    if isinstance(value, list):
        return [_normalize_json(item) for item in value]
    if isinstance(value, tuple):
        return [_normalize_json(item) for item in value]
    if isinstance(value, dict):
        return {
            unicodedata.normalize("NFC", str(key)): _normalize_json(item)
            for key, item in value.items()
        }
    return value


def _canonical_bytes(value: object) -> bytes:
    return json.dumps(
        _normalize_json(value),
        allow_nan=False,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")


def _canonical_sha256(value: object) -> str:
    return hashlib.sha256(_canonical_bytes(value)).hexdigest()


def _lf_normalized_sha256(path: Path) -> str:
    data = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(data).hexdigest()


def _load_locked_fixture(path: Path, lock: Mapping[str, str]) -> dict[str, object]:
    if _lf_normalized_sha256(path) != lock["lf_sha256"]:
        raise RuntimeError(f"source-locked file changed: {path}")
    fixture = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(fixture, dict):
        raise TypeError(f"expected object fixture at {path}")
    if fixture.get("schema") != lock["schema"]:
        raise ValueError(f"source-locked schema mismatch at {path}")
    claimed = fixture.get("payload_sha256")
    payload = dict(fixture)
    payload.pop("payload_sha256", None)
    if claimed != _canonical_sha256(payload) or claimed != lock["payload_sha256"]:
        raise ValueError(f"source-locked payload mismatch at {path}")
    return fixture


Polynomial = tuple[int, ...]
Laurent = dict[tuple[int, int], int]

S6_PARTITIONS: dict[str, tuple[int, ...]] = {
    "[6]": (6,),
    "[5,1]": (5, 1),
    "[4,2]": (4, 2),
    "[4,1^2]": (4, 1, 1),
    "[3^2]": (3, 3),
    "[3,2,1]": (3, 2, 1),
    "[3,1^3]": (3, 1, 1, 1),
    "[2^3]": (2, 2, 2),
    "[2,1^4]": (2, 1, 1, 1, 1),
    "[1^6]": (1, 1, 1, 1, 1, 1),
}


def _trim(poly: Sequence[int]) -> Polynomial:
    result = list(poly)
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return tuple(result) if result else (0,)


def _poly_add(left: Polynomial, right: Polynomial, guard: OperationGuard) -> Polynomial:
    guard.consume(max(len(left), len(right)))
    return _trim(
        tuple(
            (left[index] if index < len(left) else 0)
            + (right[index] if index < len(right) else 0)
            for index in range(max(len(left), len(right)))
        )
    )


def _poly_scale(poly: Polynomial, scalar: int, guard: OperationGuard) -> Polynomial:
    guard.consume(len(poly))
    return _trim(tuple(scalar * coefficient for coefficient in poly))


def _poly_shift(poly: Polynomial, power: int, guard: OperationGuard) -> Polynomial:
    if power < 0:
        raise ValueError("negative Tate shift")
    guard.consume(len(poly))
    return _trim((0,) * power + poly)


def _poly_pairs(poly: Polynomial) -> list[list[int]]:
    return [[coefficient, 1] for coefficient in poly]


def _laurent_add(
    left: Mapping[tuple[int, int], int],
    right: Mapping[tuple[int, int], int],
    guard: OperationGuard,
    scale: int = 1,
) -> Laurent:
    result = dict(left)
    for exponent, coefficient in right.items():
        guard.consume()
        result[exponent] = result.get(exponent, 0) + scale * coefficient
        if result[exponent] == 0:
            del result[exponent]
    return result


def _laurent_mul(
    left: Mapping[tuple[int, int], int],
    right: Mapping[tuple[int, int], int],
    guard: OperationGuard,
) -> Laurent:
    result: Laurent = {}
    for (left_x, left_y), left_coefficient in left.items():
        for (right_x, right_y), right_coefficient in right.items():
            guard.consume()
            exponent = (left_x + right_x, left_y + right_y)
            result[exponent] = (
                result.get(exponent, 0) + left_coefficient * right_coefficient
            )
            if result[exponent] == 0:
                del result[exponent]
    return result


def _axis_difference(axis: int, power: int) -> Laurent:
    if axis == 0:
        return {(power, 0): 1, (-power, 0): -1}
    if axis == 1:
        return {(0, power): 1, (0, -power): -1}
    raise ValueError("axis must be zero or one")


def _su2_character(axis: int, degree: int) -> Laurent:
    if degree < 0:
        raise ValueError("negative SU2 degree")
    if axis == 0:
        return {(power, 0): 1 for power in range(degree, -degree - 1, -2)}
    if axis == 1:
        return {(0, power): 1 for power in range(degree, -degree - 1, -2)}
    raise ValueError("axis must be zero or one")


def _verify_branching(guard: OperationGuard) -> dict[str, object]:
    numerator = _laurent_add(
        _laurent_mul(_axis_difference(0, 6), _axis_difference(1, 5), guard),
        _laurent_mul(_axis_difference(1, 6), _axis_difference(0, 5), guard),
        guard,
        scale=-1,
    )
    denominator = _laurent_add(
        _laurent_mul(_axis_difference(0, 2), _axis_difference(1, 1), guard),
        _laurent_mul(_axis_difference(1, 2), _axis_difference(0, 1), guard),
        guard,
        scale=-1,
    )
    branch: Laurent = {}
    for degree in range(5):
        branch = _laurent_add(
            branch,
            _laurent_mul(
                _su2_character(0, degree),
                _su2_character(1, degree),
                guard,
            ),
            guard,
        )
    if _laurent_mul(denominator, branch, guard) != numerator:
        raise ArithmeticError("Sp4-to-SL2xSL2 branching identity failed")
    if sum((degree + 1) ** 2 for degree in range(5)) != 55:
        raise ArithmeticError("branch dimensions do not sum to 55")
    return {
        "weyl_identity": ("chi_(0,4)|_(SL2xSL2)=sum_(r=0)^4 chi_r(x)*chi_r(y)"),
        "local_system_identity": (
            "V_(4,4)|_(A1xA1)=direct_sum_(r=0)^4 "
            "(W_r external_tensor W_r) tensor L^(4-r)"
        ),
        "summand_degrees": list(range(5)),
        "summand_dimensions": [(degree + 1) ** 2 for degree in range(5)],
        "summand_tate_twists": [4 - degree for degree in range(5)],
        "total_dimension": 55,
        "exact_laurent_terms_after_division": len(branch),
    }


def _s5_invariant_multiplicity(partition: str) -> int:
    # By the S_n branching rule, the trivial S5 representation occurs in
    # Res^(S6)_(S5) s[lambda] exactly for lambda=[6] or [5,1].
    return 1 if partition in {"[6]", "[5,1]"} else 0


def _combo_invariants(partitions: Sequence[str]) -> int:
    return sum(_s5_invariant_multiplicity(partition) for partition in partitions)


def _symmetric_group_dimension(partition: Sequence[int]) -> int:
    """Return the Specht-module dimension from the hook-length formula."""
    if not partition or any(row <= 0 for row in partition):
        raise ValueError("partition rows must be positive")
    if any(left < right for left, right in pairwise(partition)):
        raise ValueError("partition rows must be weakly decreasing")
    hook_product = 1
    for row_index, row_length in enumerate(partition):
        for column_index in range(row_length):
            boxes_below = sum(
                lower_row > column_index for lower_row in partition[row_index + 1 :]
            )
            hook_product *= row_length - column_index + boxes_below
    return math.factorial(sum(partition)) // hook_product


def _combo_dimension(partitions: Sequence[str]) -> int:
    return sum(
        _symmetric_group_dimension(S6_PARTITIONS[partition]) for partition in partitions
    )


def _build_payload() -> dict[str, object]:
    guard = OperationGuard()
    b4 = _load_locked_fixture(
        B4_FIXTURE_PATH, SOURCE_LOCKS["genus2_b4_triangular_trace_average.json"]
    )
    adapter = _load_locked_fixture(
        ADAPTER_PATH,
        SOURCE_LOCKS["genus2_marked_weierstrass_stack_adapter.json"],
    )
    for path, lock_key in (
        (B4_PRODUCER_PATH, "genus2_b4_triangular_trace_average.py"),
        (B4_NOTE_PATH, "GENUS2_B4_TRIANGULAR_TRACE_AVERAGE.md"),
        (B4_TEST_PATH, "test_genus2_b4_triangular_trace_average.py"),
    ):
        if _lf_normalized_sha256(path) != SOURCE_LOCKS[lock_key]["lf_sha256"]:
            raise RuntimeError(f"source-locked B4 artifact changed: {path}")

    theorem = b4.get("theorem")
    if not isinstance(theorem, dict):
        raise TypeError("B4 fixture lost theorem object")
    if theorem.get("chi_(0,4)_mean") != "-(2*q^2+1)/q^7":
        raise ValueError("B4 chi_(0,4) mean changed")
    if theorem.get("marked_stack_trace_chi_(0,4)") != "-(2*q^2+1)":
        raise ValueError("B4 marked-stack trace changed")

    trace_theorem = adapter.get("trace_theorem")
    if not isinstance(trace_theorem, dict):
        raise TypeError("adapter lost trace theorem")
    channels = trace_theorem.get("even_channels_closed_by_adapter")
    if not isinstance(channels, dict) or not isinstance(
        channels.get("chi_(0,4)"), dict
    ):
        raise TypeError("adapter lost chi_(0,4) channel")
    chi04_adapter = channels["chi_(0,4)"]
    if chi04_adapter.get("highest_weight_e_basis") != [4, 4]:
        raise ValueError("adapter V_(4,4) label changed")
    if chi04_adapter.get("local_system_weight") != 8:
        raise ValueError("adapter V_(4,4) weight changed")

    branching = _verify_branching(guard)

    representation_combinations = {
        "A": ["[3,1^3]", "[2,1^4]"],
        "B": ["[4,2]", "[3,2,1]", "[2^3]"],
        "C": ["[6]", "[5,1]", "[4,2]"],
        "A_prime": ["[4,1^2]", "[3^2]"],
        "B_prime": ["[5,1]", "[4,2]", "[3,2,1]"],
        "C_prime": ["[6]", "[4,2]", "[2^3]"],
    }
    invariant_multiplicities = {
        key: _combo_invariants(partitions)
        for key, partitions in representation_combinations.items()
    }
    expected_multiplicities = {
        "A": 0,
        "B": 0,
        "C": 2,
        "A_prime": 0,
        "B_prime": 1,
        "C_prime": 1,
    }
    if invariant_multiplicities != expected_multiplicities:
        raise ArithmeticError("S5-invariant projection changed")

    representation_dimensions = {
        key: _combo_dimension(partitions)
        for key, partitions in representation_combinations.items()
    }
    expected_dimensions = {
        "A": 15,
        "B": 30,
        "C": 15,
        "A_prime": 15,
        "B_prime": 30,
        "C_prime": 15,
    }
    if representation_dimensions != expected_dimensions:
        raise ArithmeticError("S6 representation dimensions changed")

    # Reconstruct both the S5 quotient and the dimension-forgotten corrected
    # erratum row from the BFG representation channels.  At weight 12 the
    # expanded-endoscopy channel is s[2^3]+s[4,2]+s[6], while the cuspidal
    # Phi_(4,12) channel is -s[3^2].
    expanded_partitions = ("[2^3]", "[4,2]", "[6]")
    expanded_full_multiplicity = _combo_dimension(expanded_partitions)
    expanded_s5_multiplicity = _combo_invariants(expanded_partitions)
    eisenstein_constant_full = (
        -representation_dimensions["C_prime"]
        + representation_dimensions["B"]
        + representation_dimensions["C"]
    )
    eisenstein_constant_s5 = (
        -invariant_multiplicities["C_prime"]
        + invariant_multiplicities["B"]
        + invariant_multiplicities["C"]
    )
    eisenstein_l5_full = -sum(
        representation_dimensions[key] for key in ("A_prime", "B_prime", "C_prime")
    )
    eisenstein_l5_s5 = -sum(
        invariant_multiplicities[key] for key in ("A_prime", "B_prime", "C_prime")
    )
    phi_4_6_full = representation_dimensions["A"]
    phi_4_6_s5 = invariant_multiplicities["A"]
    phi_4_12_full = -_symmetric_group_dimension(S6_PARTITIONS["[3^2]"])
    phi_4_12_s5 = -_s5_invariant_multiplicity("[3^2]")
    if (phi_4_6_s5, phi_4_12_s5) != (0, 0):
        raise ArithmeticError("unexpected S5-invariant cuspidal channel")

    # Polynomial coefficients are in increasing powers of the Tate motive L.
    bfg_eisenstein = _trim((eisenstein_constant_s5, 0, 0, 0, 0, eisenstein_l5_s5))
    bfg_expanded_endoscopy = _trim(
        (0, 0, 0, 0, 0, expanded_s5_multiplicity, expanded_s5_multiplicity)
    )
    bfg_siegel_cusp = _trim((phi_4_12_s5,))
    bfg_ambient = _poly_add(
        _poly_add(bfg_eisenstein, bfg_expanded_endoscopy, guard),
        bfg_siegel_cusp,
        guard,
    )
    expected_ambient = _trim((1, 0, 0, 0, 0, -1, 1))
    if bfg_ambient != expected_ambient:
        raise ArithmeticError("BFG ambient reconciliation failed")

    # Exact decomposable boundary.  Odd r vanish on the unmarked A1 factor.
    boundary_r0 = _trim((0, 0, 0, 0, 0, -1, 1))
    boundary_r2 = _trim((0, 0, 2))
    boundary_r4 = (2,)
    boundary = _poly_add(_poly_add(boundary_r0, boundary_r2, guard), boundary_r4, guard)
    expected_boundary = _trim((2, 0, 2, 0, 0, -1, 1))
    if boundary != expected_boundary:
        raise ArithmeticError("decomposable boundary reconciliation failed")
    marked_curve = _poly_add(bfg_ambient, _poly_scale(boundary, -1, guard), guard)
    expected_marked_curve = _trim((-1, 0, -2))
    if marked_curve != expected_marked_curve:
        raise ArithmeticError("marked-curve motivic difference failed")

    # Dimension-forgetting check against the corrected A2[2] row.
    pure_tate_full_level = _trim(
        (
            eisenstein_constant_full,
            0,
            0,
            0,
            0,
            eisenstein_l5_full + expanded_full_multiplicity,
            expanded_full_multiplicity,
        )
    )
    if pure_tate_full_level != (30, 0, 0, 0, 0, -45, 15):
        raise ArithmeticError("corrected A2[2] Tate row changed")
    if (phi_4_6_full, phi_4_12_full) != (15, -5):
        raise ArithmeticError("corrected A2[2] modular row changed")

    source_files = {
        "B4_fixture": {
            "path": B4_FIXTURE_PATH.relative_to(ROOT).as_posix(),
            **SOURCE_LOCKS["genus2_b4_triangular_trace_average.json"],
        },
        "B4_producer": {
            "path": B4_PRODUCER_PATH.relative_to(ROOT).as_posix(),
            **SOURCE_LOCKS["genus2_b4_triangular_trace_average.py"],
        },
        "B4_note": {
            "path": B4_NOTE_PATH.relative_to(ROOT).as_posix(),
            **SOURCE_LOCKS["GENUS2_B4_TRIANGULAR_TRACE_AVERAGE.md"],
        },
        "B4_test": {
            "path": B4_TEST_PATH.relative_to(ROOT).as_posix(),
            **SOURCE_LOCKS["test_genus2_b4_triangular_trace_average.py"],
        },
        "marked_stack_adapter": {
            "path": ADAPTER_PATH.relative_to(ROOT).as_posix(),
            **SOURCE_LOCKS["genus2_marked_weierstrass_stack_adapter.json"],
        },
    }

    return {
        "schema": "riemann.function_field.genus2_chi04_stack_trace_reconciliation.v1",
        "status": "PRIMARY_SOURCE_RECONCILIATION_COMPLETE",
        "scope": {
            "base_fields": "every finite field F_q of odd characteristic",
            "target_stack": "M_2(w^1), one rational marked Weierstrass point",
            "local_system": "V_(4,4), equivalently chi_(0,4), weight 8",
            "finite_field_enumeration": False,
            "network_access_during_replay": False,
            "global_novelty_claim": False,
        },
        "project_theorem": {
            "status": "PROVED_IN_SOURCE_LOCKED_B4_PACKET",
            "mean": "<chi_(0,4)>=-(2*q^2+1)/q^7",
            "marked_stack_trace": "T_(0,4)(q)=-(2*q^2+1)",
            "cohomological_meaning": (
                "alternating compactly-supported geometric-Frobenius trace "
                "on e_c(M_2(w^1),V_(4,4))"
            ),
        },
        "primary_source_verdict": {
            "printed_all_q_M_2(w^1)_V_(4,4)_formula_found": False,
            "bergstrom_2006": (
                "V_(4,4) has weight 8 and lies outside the printed weight<=7 "
                "scope; Theorem 11.6 stops at weights 4 and 6"
            ),
            "faber_vandergeer_2003": (
                "level one only; no w^1 formula, no printed V_(4,4) row, and "
                "l=m=4 is in the explicitly exceptional nonregular range"
            ),
            "BFG_2008": (
                "defines M_2(w^1), but gives bounded q<=37 data, ambient "
                "A_2(w^1) numerical Euler checks, and conjectural A_2[2] formulas"
            ),
            "erratum_2025": (
                "corrects the conjectural ambient A_2[2], V_(4,4) row only"
            ),
            "relative_assessment": (
                "the project theorem is an independent all-q proof relative to "
                "these audited sources, but no wider novelty claim is made"
            ),
        },
        "moduli_firewall": {
            "M_2(w^1)": (
                "smooth genus-two curve plus one ordered rational Weierstrass "
                "point; this is the project theorem's target"
            ),
            "M_(2,1)": (
                "smooth genus-two curve plus one arbitrary marked point; its "
                "forgetful fibre is C(F_q), not the rational Weierstrass set"
            ),
            "M_2": "unmarked smooth genus-two curves",
            "A_2(w^1)": (
                "ambient principally polarized abelian surfaces with one partial "
                "level-two/Weierstrass label; contains a decomposable locus"
            ),
            "A_2[2]": (
                "full level-two cover with S6 action; A_2(w^1) is its S5 quotient, "
                "not its dimension-forgotten total"
            ),
        },
        "BFG_conjectural_reconciliation": {
            "logical_status": (
                "CONJECTURAL_AMBIENT_PREDICTION_PLUS_EXACT_BOUNDARY; "
                "NOT_A_SOURCE_PROOF_OF_THE_TARGET"
            ),
            "S5_projection_rule": (
                "only s[6] and s[5,1] contain the trivial S5 representation"
            ),
            "representation_combinations": representation_combinations,
            "representation_dimensions": representation_dimensions,
            "S5_invariant_multiplicities": invariant_multiplicities,
            "elementary_modular_dimensions": {
                "dim_S_6_SL2Z": 0,
                "dim_S_12_SL2Z": 1,
                "dim_S_4_Gamma0(2)": 0,
                "dim_S_6_Gamma0(2)": 0,
                "dim_S_12_Gamma0(2)": 2,
                "dim_S_12_Gamma0(2)_new": 0,
                "explanation": (
                    "M_(2k)(Gamma0(2)) has dimension floor(k/2)+1; at "
                    "weight 12 the two cusp forms are the two level-one oldforms"
                ),
            },
            "A_2(w^1)_components_low_to_high": {
                "expected_Eisenstein": _poly_pairs(bfg_eisenstein),
                "expected_expanded_endoscopy": _poly_pairs(bfg_expanded_endoscopy),
                "expected_Siegel_cusp": _poly_pairs(bfg_siegel_cusp),
                "expected_total": _poly_pairs(bfg_ambient),
            },
            "expected_A_2(w^1)_class": "L^6-L^5+1",
            "corrected_A_2[2]_V_(4,4)_row": ("15L^6-45L^5+30+15Phi_(4,6)-5Phi_(4,12)"),
            "dimension_forgetting_Tate_part_low_to_high": _poly_pairs(
                pure_tate_full_level
            ),
            "dimension_forgetting_modular_coefficients": {
                "Phi_(4,6)": phi_4_6_full,
                "Phi_(4,12)": phi_4_12_full,
            },
            "erratum_relevance": (
                "the corrected +15Phi_(4,6) term lies in the BFG A representation, "
                "whose S5-invariant multiplicity is zero; the correction is still "
                "required for the full-level ledger but does not alter A_2(w^1)"
            ),
        },
        "exact_decomposable_boundary": {
            "geometry": "A_(1,1)(w^1) is Y_0(2) times A_1",
            "reason": (
                "the marked nonzero two-torsion point distinguishes one elliptic "
                "component; the other component is unmarked"
            ),
            "branching": branching,
            "elliptic_euler_inputs": {
                "A_1_W_0": "L",
                "A_1_W_2": "-1",
                "A_1_W_4": "-1",
                "Y_0(2)_W_0": "L-1",
                "Y_0(2)_W_2": "-2",
                "Y_0(2)_W_4": "-2",
                "odd_r": "zero on the unmarked A_1 factor",
            },
            "even_branch_contributions_low_to_high": {
                "r=0": _poly_pairs(boundary_r0),
                "r=2": _poly_pairs(boundary_r2),
                "r=4": _poly_pairs(boundary_r4),
            },
            "class_low_to_high": _poly_pairs(boundary),
            "class": "L^6-L^5+2L^2+2",
        },
        "reconciled_difference": {
            "identity": ("(L^6-L^5+1)-(L^6-L^5+2L^2+2)=-2L^2-1"),
            "M_2(w^1)_predicted_class_low_to_high": _poly_pairs(marked_curve),
            "M_2(w^1)_predicted_class": "-2L^2-1",
            "geometric_Frobenius_trace": "-(2*q^2+1)",
            "interpretation": (
                "the project theorem proves exactly the all-q Frobenius trace "
                "of the marked-curve class predicted by the conjectural BFG "
                "ambient formalism; it does not itself prove equality of "
                "motivic Grothendieck classes"
            ),
        },
        "literature_artifacts": list(LITERATURE_ARTIFACTS),
        "source_files": source_files,
        "firewalls": [
            "No statement for M_(2,1), M_2, A_2(w^1), or A_2[2] is silently substituted for M_2(w^1).",
            "The BFG nonregular and endoscopic formulas are labelled conjectural.",
            "A numerical Euler characteristic is not an all-q Frobenius trace.",
            "The corrected A_2[2] example row is not a marked-curve theorem.",
            "The all-q trace theorem is not asserted to prove equality of motivic Grothendieck classes.",
            "No claim is made that the motivic class -2L^2-1 was previously unknown.",
            "No RH, GRH, memberwise-sign, or global-motive claim is made.",
        ],
        "resource_audit": {
            "exact_operations": guard.used,
            "operation_cap": guard.limit,
            "finite_fields_enumerated": 0,
            "curves_enumerated": 0,
            "source_documents": len(LITERATURE_ARTIFACTS),
        },
        "provenance": {
            "producer_lf_sha256": _lf_normalized_sha256(Path(__file__)),
            "note_lf_sha256": _lf_normalized_sha256(NOTE_PATH),
            "test_lf_sha256": _lf_normalized_sha256(TEST_PATH),
            "hash_convention": "SHA-256 after CRLF/CR normalization to LF",
        },
    }


def build_fixture() -> dict[str, object]:
    payload = _build_payload()
    result = dict(payload)
    result["payload_sha256"] = _canonical_sha256(payload)
    return result


def _render_json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def _check_or_write(*, check: bool) -> int:
    rendered = _render_json(build_fixture())
    if check:
        if not OUTPUT_PATH.exists():
            raise FileNotFoundError(f"missing fixture: {OUTPUT_PATH}")
        if OUTPUT_PATH.read_text(encoding="utf-8") != rendered:
            raise RuntimeError(f"fixture is stale: {OUTPUT_PATH}")
    else:
        OUTPUT_PATH.write_text(rendered, encoding="utf-8", newline="\n")
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="refuse unless the committed fixture is current",
    )
    arguments = parser.parse_args(argv)
    return _check_or_write(check=arguments.check)


if __name__ == "__main__":
    raise SystemExit(main())
