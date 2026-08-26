#!/usr/bin/env python3
"""Exact repeated-factor tomography on frozen genus-two coefficient histograms.

The only arithmetic family data read here are the complete, source-locked
``(a_D,b_D)`` histograms for q=3,5,7.  No field, polynomial, curve, orbit, or
family member is enumerated.  For the repository convention

    P(T) = 1 + a*T + b*T^2 + q*a*T^3 + q^2*T^4,

the packet proves algebraically that the repeated-cosine certificate

    G = (a^2 - 4*b + 8*q)/q

vanishes exactly when ``P`` is the square of an integral reciprocal
q-elliptic-form quadratic.  It also restricts the locked root-free selectors
P,D,S to the complete repeated-factor compact line and gives exact sign
chambers.  Every claimed value is integral or rational; algebraic endpoints
are retained symbolically rather than rounded.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from collections import Counter
from collections.abc import Mapping, Sequence
from dataclasses import dataclass, field
from fractions import Fraction
from pathlib import Path
from types import ModuleType

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]

INPUT_PATH = HERE / "balanced_control_family_scan.json"
INPUT_PRODUCER_PATH = HERE / "balanced_control_family_scan.py"
COEFFICIENT_ARITHMETIC_PATH = HERE / "genus2_q_scan.py"
AFFINE_ACTION_PATH = HERE / "genus2_affine_orbits.py"

ZERO_FIXTURE_PATH = HERE / "genus2_detector_zero_geometry_conditioning.json"
ZERO_PRODUCER_PATH = HERE / "genus2_detector_zero_geometry_conditioning.py"
ZERO_NOTE_PATH = HERE / "GENUS2_DETECTOR_ZERO_GEOMETRY_CONDITIONING.md"

SELECTOR_PRODUCER_PATH = HERE / "frobenius_interferometry_subgroup_selectors.py"
SELECTOR_NOTE_PATH = HERE / "FROBENIUS_INTERFEROMETRY_SUBGROUP_SELECTORS.md"

SPLIT_FIXTURE_PATH = HERE / "genus2_endoscopic_split_locus.json"
SPLIT_PRODUCER_PATH = HERE / "genus2_endoscopic_split_locus.py"
SPLIT_NOTE_PATH = HERE / "GENUS2_ENDOSCOPIC_SPLIT_LOCUS.md"

OUTPUT_PATH = HERE / "genus2_repeated_factor_tomography.json"
NOTE_PATH = HERE / "GENUS2_REPEATED_FACTOR_TOMOGRAPHY.md"
TEST_PATH = ROOT / "tests" / "test_genus2_repeated_factor_tomography.py"

SCHEMA = "riemann.function_field.genus2_repeated_factor_tomography.v1"
FROZEN_Q_VALUES = (3, 5, 7)
SELECTOR_ORDER = ("P", "D", "S")
SOURCE_ATOM_CAP_INCLUSIVE = 4_096

EXPECTED_INPUT_PAYLOAD_SHA256 = (
    "50fd136eb0483387246766c5f2426c3e727c69cd9a89943f9268368db0f9d39c"
)
EXPECTED_ZERO_PAYLOAD_SHA256 = (
    "712a2aaa42500355b6eba4bc05043ec54de88ef43de0907c9b8812d10f134c92"
)
EXPECTED_SPLIT_PAYLOAD_SHA256 = (
    "01ccb19f591f48682fa79dbef306880e924282184352cb992e3f66153ceae5c3"
)
EXPECTED_MEMBER_LEDGER_SHA256 = {
    3: "e38543c4526e6b330f012274398a258f2d021ddae18442d2f0094d42ec229790",
    5: "69fe496e1cca2090ca62bf7622ff34c3ab3aef1b9268dfb41c4df94d380a9d0a",
    7: "c1d4ca30f45341de53af20ab4e4ca3f9bff79542146f1ac2230169eec9669655",
}
EXPECTED_ATOM_COUNTS = {3: 32, 5: 81, 7: 138}
EXPECTED_MEMBER_COUNTS = {3: 162, 5: 2_500, 7: 14_406}
EXPECTED_REPEATED_ATOMS = {
    3: (),
    5: ((-4, 14, 5), (0, 10, 5), (4, 14, 5)),
    7: ((-4, 18, 21), (0, 14, 42), (4, 18, 21)),
}
EXPECTED_SELECTOR_SIGNATURES = {
    "product_selector": (0, 2, 0, 0, 0, 0, 0),
    "doubled_selector": (0, 0, 2, 0, 0, 0, 0),
    "sym3_selector": (0, 0, 0, 2, 0, 0, 0),
}
EXPECTED_LF_SHA256 = {
    "histogram_fixture": "c3494ae852fda4e754b3b0da7cb30a26e3e38ec1c87e2619cd6fee6cdc68b68e",
    "histogram_producer": "7192fa26b0ea17cb68cff288620ea4dfb124e07807986d9c74fbd37e66087d3b",
    "coefficient_arithmetic": "f595dbf52d4265cfe2ea6888255f53df887fed77e204103f2b0dfd95e961f935",
    "affine_action": "32e440750b2832ec4cc84473187b4b1aa6396eda87c64f5ac845b2a96dc88f08",
    "zero_fixture": "a790c769e03927f8be8e21c8b0517b89aba0a7aa3301032230834a722f56c6ba",
    "zero_producer": "a19d1ea055a66d7d743e5ed4c8261c8b4fa95269e78f2ed5ff124df63e20b2d8",
    "zero_note": "646017184761427a214350eb356606c20a335fe0918172213caa7505362736be",
    "selector_producer": "48474ebcbb99efea23227126f66f566fdb525a3c9ae9e81a77bf83d4075f55e7",
    "selector_note": "c7637d454f1fb102555e6723dd8d93a4b6a27363d80cbbb9a03061f614bd3221",
    "split_fixture": "10edc162a37403c3c2af1bfa1051dfb07b1b75dbdea181dc673585dde70fd2f4",
    "split_producer": "4489c109f25f8e0ca3051dc9983a8738b7aaee941a351959c552aa19b001e4de",
    "split_note": "b6be33305cacf1b541aad630587be04375eddc527c64fd1eb9d5ce1337772ff7",
    "note": "ec266f56baece1f5057a63535c78a0e2f6e0671a054ee71c0c4b466c67644482",
    "test": "4422f51955041fc1316f12fe98265c2e57fa1b651d12c36464709d99cb655b3c",
}


def _pair(value: Fraction | int) -> list[int]:
    rational = Fraction(value)
    return [rational.numerator, rational.denominator]


def _canonical_sha256(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def _lf_sha256(path: Path) -> str:
    normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(normalized).hexdigest()


def _plain_int(name: str, value: object) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be a plain integer")
    return value


def _sign(value: Fraction) -> str:
    return "negative" if value < 0 else "positive" if value > 0 else "zero"


def _assert_no_float(value: object) -> None:
    if isinstance(value, float):
        raise TypeError("claim payload must not contain floats")
    if isinstance(value, Mapping):
        for item in value.values():
            _assert_no_float(item)
    elif isinstance(value, (list, tuple)):
        for item in value:
            _assert_no_float(item)


@dataclass
class SourceAtomGuard:
    cap: int = SOURCE_ATOM_CAP_INCLUSIVE
    counts: Counter[str] = field(default_factory=Counter)

    @property
    def total(self) -> int:
        return sum(self.counts.values())

    def preflight(self, amount: int) -> None:
        amount = _plain_int("source atom count", amount)
        if amount < 0:
            raise ValueError("source atom count must be nonnegative")
        if amount > self.cap:
            raise RuntimeError(
                f"source atom count {amount} exceeds inclusive cap {self.cap}"
            )

    def charge(self, name: str, amount: int = 1) -> None:
        amount = _plain_int("source atom charge", amount)
        if amount < 0:
            raise ValueError("source atom charge must be nonnegative")
        if self.total + amount > self.cap:
            raise RuntimeError(
                f"source atom transform would exceed inclusive cap {self.cap}"
            )
        self.counts[name] += amount

    def snapshot(self) -> dict[str, int]:
        result = {name: self.counts[name] for name in sorted(self.counts)}
        result["total"] = self.total
        return result


@dataclass(frozen=True)
class RepeatedFactor:
    q: int
    a: int
    b: int
    trace: int

    @property
    def low_polynomial(self) -> tuple[int, ...]:
        return (1, self.a, self.b, self.q * self.a, self.q * self.q)

    @property
    def quadratic(self) -> tuple[int, ...]:
        return (1, -self.trace, self.q)

    @property
    def compact_z(self) -> Fraction:
        return Fraction(self.trace * self.trace, 4 * self.q)


def _multiply_low(left: Sequence[int], right: Sequence[int]) -> tuple[int, ...]:
    product = [0] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            product[left_index + right_index] += left_value * right_value
    return tuple(product)


def repeated_factor(q: int, a: int, b: int) -> RepeatedFactor | None:
    """Return the integral repeated q-factor exactly when G=0.

    If ``a^2-4*b+8*q=0``, then ``a^2`` is divisible by four, hence ``a`` is
    even.  With ``r=-a/2``, the same equation gives ``b=r^2+2q`` and direct
    multiplication proves ``P(T)=(1-rT+qT^2)^2``.
    """

    q = _plain_int("q", q)
    a = _plain_int("a", a)
    b = _plain_int("b", b)
    if q <= 0:
        raise ValueError("q must be positive")
    delta = a * a - 4 * b + 8 * q
    if delta != 0:
        return None
    if a % 2:
        raise ArithmeticError("Delta=0 failed to force even a")
    trace = -a // 2
    result = RepeatedFactor(q=q, a=a, b=b, trace=trace)
    if b != trace * trace + 2 * q:
        raise ArithmeticError("Delta=0 failed to recover the middle coefficient")
    if _multiply_low(result.quadratic, result.quadratic) != result.low_polynomial:
        raise ArithmeticError("repeated factor failed coefficient reconstruction")
    return result


def selector_values_on_repeated_line(z: Fraction | int) -> dict[str, Fraction]:
    """Evaluate P,D,S on the doubled compact line, with z=x^2 in [0,1]."""

    z = Fraction(z)
    if z < 0 or z > 1:
        raise ValueError("compact repeated-line coordinate z must lie in [0,1]")
    product = -32 * z * (z - 1) * (4 * z - 3) * (4 * z - 1)
    doubled = 8 * (4 * z - 1) * (16 * z**3 - 20 * z**2 + 7 * z - 2)
    sym3 = -8 * (2 * z - 1) * (256 * z**4 - 512 * z**3 + 336 * z**2 - 80 * z + 3)
    return {"P": product, "D": doubled, "S": sym3}


def _polynomial_evaluate(coefficients_low: Sequence[int], value: Fraction) -> Fraction:
    total = Fraction(0)
    for coefficient in reversed(coefficients_low):
        total = total * value + coefficient
    return total


def _scaled_polynomial_product(
    scale: int, *factors_low: Sequence[int]
) -> tuple[int, ...]:
    product: tuple[int, ...] = (scale,)
    for factor in factors_low:
        product = _multiply_low(product, factor)
    return product


def selector_line_certificate() -> dict[str, object]:
    """Return exact factorization, root isolation, and sign-chamber data."""

    expanded = {
        "P": (0, 96, -608, 1_024, -512),
        "D": (16, -120, 384, -768, 512),
        "S": (24, -688, 3_968, -9_472, 10_240, -4_096),
    }
    factored = {
        "P": _scaled_polynomial_product(-32, (0, 1), (-1, 1), (-3, 4), (-1, 4)),
        "D": _scaled_polynomial_product(8, (-1, 4), (-2, 7, -20, 16)),
        "S": _scaled_polynomial_product(-8, (-1, 2), (3, -80, 336, -512, 256)),
    }
    if factored != expanded:
        raise ArithmeticError("selector-line factorization expansion drifted")

    h = (-2, 7, -20, 16)
    k = (3, -80, 336, -512, 256)
    h_left = _polynomial_evaluate(h, Fraction(11, 12))
    h_right = _polynomial_evaluate(h, Fraction(12, 13))
    if h_left != Fraction(-7, 108) or h_right != Fraction(10, 2_197):
        raise ArithmeticError("D root-isolation endpoint certificate drifted")
    k_1_25 = _polynomial_evaluate(k, Fraction(1, 25))
    k_1_20 = _polynomial_evaluate(k, Fraction(1, 20))
    if k_1_25 != Fraction(119_331, 390_625) or k_1_20 != Fraction(-139, 625):
        raise ArithmeticError("S root-isolation endpoint certificate drifted")

    return {
        "coordinate": {
            "spectrum": "(exp(+/-i*theta)) each with multiplicity two",
            "x": "cos(theta)",
            "z": "x^2=r^2/(4*q)",
            "domain": "0<=z<=1",
            "coefficient_substitution": "e1^2=16*z, e2=2+4*z",
        },
        "factorized_restrictions": {
            "P": "-32*z*(z-1)*(4*z-1)*(4*z-3)",
            "D": "8*(4*z-1)*h(z), h(z)=16*z^3-20*z^2+7*z-2",
            "S": "-8*(2*z-1)*k(z), k(z)=256*z^4-512*z^3+336*z^2-80*z+3",
        },
        "expanded_coefficients_low_to_high": {
            name: list(coefficients) for name, coefficients in expanded.items()
        },
        "D_algebraic_root_certificate": {
            "h_discriminant": -13_360,
            "consequence": "h has exactly one real root rho_D",
            "isolating_interval": [[11, 12], [12, 13]],
            "endpoint_values": [_pair(h_left), _pair(h_right)],
            "zeros_in_0_1": ["1/4", "rho_D"],
            "sign_chambers": [
                {"interval": "[0,1/4)", "sign": "positive"},
                {"interval": "{1/4}", "sign": "zero"},
                {"interval": "(1/4,rho_D)", "sign": "negative"},
                {"interval": "{rho_D}", "sign": "zero"},
                {"interval": "(rho_D,1]", "sign": "positive"},
            ],
        },
        "S_algebraic_root_certificate": {
            "symmetric_transform": "k((1+y)/2)=16*y^4-12*y^2-1",
            "alpha": "(1-sqrt((3+sqrt(13))/8))/2",
            "beta": "(1+sqrt((3+sqrt(13))/8))/2=1-alpha",
            "alpha_isolating_interval": [[1, 25], [1, 20]],
            "beta_isolating_interval": [[19, 20], [24, 25]],
            "k_endpoint_values_alpha_interval": [_pair(k_1_25), _pair(k_1_20)],
            "zeros_in_0_1": ["alpha", "1/2", "beta"],
            "sign_chambers": [
                {"interval": "[0,alpha)", "sign": "positive"},
                {"interval": "{alpha}", "sign": "zero"},
                {"interval": "(alpha,1/2)", "sign": "negative"},
                {"interval": "{1/2}", "sign": "zero"},
                {"interval": "(1/2,beta)", "sign": "positive"},
                {"interval": "{beta}", "sign": "zero"},
                {"interval": "(beta,1]", "sign": "negative"},
            ],
        },
        "P_rational_root_certificate": {
            "zeros_in_0_1": ["0", "1/4", "3/4", "1"],
            "sign_chambers": [
                {"interval": "{0}", "sign": "zero"},
                {"interval": "(0,1/4)", "sign": "positive"},
                {"interval": "{1/4}", "sign": "zero"},
                {"interval": "(1/4,3/4)", "sign": "negative"},
                {"interval": "{3/4}", "sign": "zero"},
                {"interval": "(3/4,1)", "sign": "positive"},
                {"interval": "{1}", "sign": "zero"},
            ],
        },
    }


def _verify_primitive_hashes() -> None:
    paths = {
        "histogram_fixture": INPUT_PATH,
        "histogram_producer": INPUT_PRODUCER_PATH,
        "coefficient_arithmetic": COEFFICIENT_ARITHMETIC_PATH,
        "affine_action": AFFINE_ACTION_PATH,
        "zero_fixture": ZERO_FIXTURE_PATH,
        "zero_producer": ZERO_PRODUCER_PATH,
        "zero_note": ZERO_NOTE_PATH,
        "selector_producer": SELECTOR_PRODUCER_PATH,
        "selector_note": SELECTOR_NOTE_PATH,
        "split_fixture": SPLIT_FIXTURE_PATH,
        "split_producer": SPLIT_PRODUCER_PATH,
        "split_note": SPLIT_NOTE_PATH,
        "note": NOTE_PATH,
        "test": TEST_PATH,
    }
    for name, path in paths.items():
        if not path.is_file():
            raise FileNotFoundError(f"required source is missing: {path}")
        actual = _lf_sha256(path)
        expected = EXPECTED_LF_SHA256[name]
        if actual != expected:
            raise ValueError(
                f"source digest mismatch for {name}: {actual} != {expected}"
            )


def _load_module(path: Path, name: str) -> ModuleType:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"could not construct module specification for {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _payload_checked(path: Path, required_hash: str, schema: str) -> dict[str, object]:
    data = json.loads(path.read_text(encoding="utf-8"))
    payload = dict(data)
    claimed = payload.pop("payload_sha256", None)
    if claimed != _canonical_sha256(payload) or claimed != required_hash:
        raise ValueError(f"payload/source pin mismatch for {path.name}")
    if data.get("schema") != schema:
        raise ValueError(f"unexpected schema for {path.name}")
    return data


def _validated_sources() -> tuple[
    dict[str, object],
    list[Mapping[str, object]],
    dict[int, Mapping[str, object]],
    dict[int, Mapping[str, object]],
    ModuleType,
    ModuleType,
]:
    _verify_primitive_hashes()
    source = _payload_checked(
        INPUT_PATH,
        EXPECTED_INPUT_PAYLOAD_SHA256,
        "riemann.function_field.balanced_control_family_scan.v1",
    )
    zero = _payload_checked(
        ZERO_FIXTURE_PATH,
        EXPECTED_ZERO_PAYLOAD_SHA256,
        "riemann.function_field.genus2_detector_zero_geometry_conditioning.v1",
    )
    split = _payload_checked(
        SPLIT_FIXTURE_PATH,
        EXPECTED_SPLIT_PAYLOAD_SHA256,
        "riemann.function_field.genus2_endoscopic_split_locus.v1",
    )

    frozen = source.get("frozen_enumeration_facts")
    if not isinstance(frozen, Mapping):
        raise TypeError("frozen enumeration facts must be an object")
    if frozen.get("status") != "EXHAUSTIVE_ONLY_FOR_Q_3_5_7":
        raise ValueError("source exhaustive-coverage status drifted")
    if tuple(frozen.get("q_values", ())) != FROZEN_Q_VALUES:
        raise ValueError("source q ladder drifted")
    families = sorted(frozen.get("families", []), key=lambda row: int(row["q"]))
    if tuple(int(row["q"]) for row in families) != FROZEN_Q_VALUES:
        raise ValueError("source family rows drifted")
    for family in families:
        q = _plain_int("q", family.get("q"))
        atoms = family["joint_a_D_b_D_law"]["atoms"]
        if len(atoms) != EXPECTED_ATOM_COUNTS[q]:
            raise ValueError(f"q={q} source atom count drifted")
        if (
            sum(_plain_int("member_count", atom["member_count"]) for atom in atoms)
            != EXPECTED_MEMBER_COUNTS[q]
        ):
            raise ValueError(f"q={q} source member mass drifted")
        if (
            family.get("member_coefficient_ledger_sha256")
            != EXPECTED_MEMBER_LEDGER_SHA256[q]
        ):
            raise ValueError(f"q={q} member ledger drifted")

    zero_rows = {
        int(row["q"]): row
        for row in zero["exact_frozen_member_weight_laws"]["families"]
    }
    split_rows = {
        int(row["q"]): row for row in split["frozen_histogram_results"]["families"]
    }
    if (
        tuple(sorted(zero_rows)) != FROZEN_Q_VALUES
        or tuple(sorted(split_rows)) != FROZEN_Q_VALUES
    ):
        raise ValueError("downstream cross-check q ladder drifted")

    selector_module = _load_module(
        SELECTOR_PRODUCER_PATH, "_locked_repeated_factor_selector_adapter"
    )
    if dict(selector_module.SELECTOR_EXPECTATIONS) != EXPECTED_SELECTOR_SIGNATURES:
        raise ValueError("selector signature sentinel drifted")
    if not callable(selector_module.selector_values_from_squared_first_elementary):
        raise TypeError("locked rational selector adapter is missing")

    split_module = _load_module(
        SPLIT_PRODUCER_PATH, "_locked_repeated_factor_split_classifier"
    )
    if not callable(split_module.classify_factorization):
        raise TypeError("locked integral split classifier is missing")
    return source, families, zero_rows, split_rows, selector_module, split_module


def _fractional_law(counter: Counter[Fraction]) -> list[dict[str, object]]:
    return [{"z": _pair(z), "member_count": counter[z]} for z in sorted(counter)]


def _family_packet(
    family: Mapping[str, object],
    zero_row: Mapping[str, object],
    split_row: Mapping[str, object],
    selector_module: ModuleType,
    split_module: ModuleType,
    guard: SourceAtomGuard,
) -> dict[str, object]:
    q = _plain_int("q", family["q"])
    repeated_rows: list[dict[str, object]] = []
    z_law: Counter[Fraction] = Counter()
    sign_counts = {name: Counter() for name in SELECTOR_ORDER}
    source_atoms = family["joint_a_D_b_D_law"]["atoms"]

    observed_sentinel: list[tuple[int, int, int]] = []
    for atom in source_atoms:
        guard.charge(f"q={q}_source_atoms")
        a = _plain_int("a_D", atom["a_D"])
        b = _plain_int("b_D", atom["b_D"])
        weight = _plain_int("member_count", atom["member_count"])
        factor = repeated_factor(q, a, b)
        if factor is None:
            continue
        if factor.trace * factor.trace > 4 * q:
            raise ArithmeticError(f"q={q} repeated factor violates Hasse interval")
        z = factor.compact_z
        values = selector_values_on_repeated_line(z)
        adapter = selector_module.selector_values_from_squared_first_elementary(
            Fraction(a * a, q), Fraction(b, q)
        )
        adapter_values = {
            "P": Fraction(adapter["product_selector"]),
            "D": Fraction(adapter["doubled_selector"]),
            "S": Fraction(adapter["sym3_selector"]),
        }
        if adapter_values != values:
            raise ArithmeticError("repeated-line selector substitution drifted")
        classification = split_module.classify_factorization(q, a, b)
        if classification.kind != "split_repeated":
            raise ArithmeticError("G=0 row left the existing repeated split class")
        if classification.elliptic_traces != (factor.trace, factor.trace):
            raise ArithmeticError("existing split classifier trace diagonal drifted")

        z_law[z] += weight
        for name, value in values.items():
            sign_counts[name][_sign(value)] += weight
        observed_sentinel.append((a, b, weight))
        repeated_rows.append(
            {
                "a_D": a,
                "b_D": b,
                "member_count": weight,
                "Delta": 0,
                "G": [0, 1],
                "parity_forced_even_a": a % 2 == 0,
                "repeated_trace_r": factor.trace,
                "compact_z": _pair(z),
                "hasse_admissible_trace": factor.trace * factor.trace <= 4 * q,
                "quadratic_coefficients_low_to_high": list(factor.quadratic),
                "quartic_coefficients_low_to_high": list(factor.low_polynomial),
                "selectors": {name: _pair(values[name]) for name in SELECTOR_ORDER},
            }
        )

    if tuple(observed_sentinel) != EXPECTED_REPEATED_ATOMS[q]:
        raise ValueError(f"q={q} repeated-atom sentinel drifted")
    repeated_member_count = sum(row[2] for row in observed_sentinel)
    repeated_atom_count = len(observed_sentinel)

    zero_count = zero_row["full_proxy_law"]["certificate_member_counts"][
        "G_zero_repeated_cosine_certificate"
    ]
    if zero_count != repeated_member_count:
        raise ArithmeticError("zero-geometry G=0 census disagrees")
    split_class = split_row["factorization_classification"]["classes"]["split_repeated"]
    if (
        split_class["member_count"] != repeated_member_count
        or split_class["signed_coefficient_atom_count"] != repeated_atom_count
    ):
        raise ArithmeticError("integral split repeated census disagrees")
    integral_split_count = split_row["factorization_classification"][
        "integral_split_locus"
    ]["member_count"]

    return {
        "q": q,
        "input_signed_source_atom_count": len(source_atoms),
        "input_member_count": EXPECTED_MEMBER_COUNTS[q],
        "repeated_signed_atom_count": repeated_atom_count,
        "repeated_member_count": repeated_member_count,
        "repeated_member_fraction_of_full_family": _pair(
            Fraction(repeated_member_count, EXPECTED_MEMBER_COUNTS[q])
        ),
        "repeated_member_fraction_of_integral_split_locus": (
            _pair(Fraction(repeated_member_count, integral_split_count))
            if integral_split_count
            else None
        ),
        "compact_z_member_law": _fractional_law(z_law),
        "selector_sign_member_counts": {
            name: {
                sign: sign_counts[name][sign]
                for sign in ("negative", "zero", "positive")
            }
            for name in SELECTOR_ORDER
        },
        "complete_repeated_signed_atoms": repeated_rows,
        "cross_checks": {
            "zero_geometry_G_zero_member_count": zero_count,
            "split_locus_repeated_member_count": split_class["member_count"],
            "split_locus_repeated_signed_atom_count": split_class[
                "signed_coefficient_atom_count"
            ],
        },
    }


def _counterexample_packet() -> dict[str, object]:
    q, trace = 5, 4
    a = -2 * trace
    b = trace * trace + 2 * q
    factor = repeated_factor(q, a, b)
    if factor is None:
        raise ArithmeticError("counterexample failed repeated-factor theorem")
    z = factor.compact_z
    values = selector_values_on_repeated_line(z)
    if z != Fraction(4, 5) or values["D"] != Fraction(-11_088, 625):
        raise ArithmeticError("D-sign counterexample drifted")
    return {
        "purpose": "refutes universal D>0 on the integral Hasse-admissible repeated-factor locus",
        "q": q,
        "trace_r": trace,
        "a": a,
        "b": b,
        "G": [0, 1],
        "compact_z": _pair(z),
        "hasse_admissible_trace": trace * trace <= 4 * q,
        "quadratic_coefficients_low_to_high": list(factor.quadratic),
        "quartic_coefficients_low_to_high": list(factor.low_polynomial),
        "selectors": {name: _pair(values[name]) for name in SELECTOR_ORDER},
        "not_claimed": "no curve realization, Jacobian interpretation, isogeny, endomorphism, monodromy, automorphism, or compatible system",
    }


def build_fixture() -> dict[str, object]:
    source, families, zero_rows, split_rows, selector_module, split_module = (
        _validated_sources()
    )
    source_atom_total = sum(EXPECTED_ATOM_COUNTS.values())
    guard = SourceAtomGuard()
    guard.preflight(source_atom_total)
    family_packets = [
        _family_packet(
            family,
            zero_rows[int(family["q"])],
            split_rows[int(family["q"])],
            selector_module,
            split_module,
            guard,
        )
        for family in families
    ]
    if guard.total != source_atom_total:
        raise ArithmeticError("source atom accounting drifted")

    payload: dict[str, object] = {
        "schema": SCHEMA,
        "raw_fixture_id": "genus2-repeated-factor-tomography-v1",
        "status": "EXACT_FINITE_BOUNDED_SOURCE_LOCKED_LOCAL_POLYNOMIAL_THEOREM",
        "scope": {
            "theorem": "all positive integer q and integral reciprocal coefficient pairs (a,b)",
            "finite_census": "complete monic squarefree quintic member histograms only at q=3,5,7",
            "selector_line": "the full real doubled/repeated-factor compact line 0<=z<=1",
        },
        "exact_repeated_factor_theorem": {
            "source_polynomial": "P(T)=1+a*T+b*T^2+q*a*T^3+q^2*T^4",
            "certificate": "G=(a^2-4*b+8*q)/q",
            "equivalence": "G=0 iff a is even and, for r=-a/2, b=r^2+2*q and P(T)=(1-r*T+q*T^2)^2",
            "parity_proof": "G=0 gives a^2=4*(b-2*q), hence 4 divides a^2 and therefore 2 divides a",
            "existing_split_predicate_bridge": "the locked +q factorization has Delta=(r-s)^2; G=Delta/q, so G=0 is exactly its diagonal r=s sublocus",
            "normalization_bridge": "on a q-Weil repeated factor, x=r/(2*sqrt(q)), z=x^2=r^2/(4*q), e1^2=16*z, e2=2+4*z",
        },
        "selector_restriction_theorem": selector_line_certificate(),
        "finite_histogram_tomography": {
            "status": "EXACT_ONLY_FOR_Q_3_5_7",
            "weighting": "uniform monic squarefree quintic members inherited from the locked histogram",
            "families": family_packets,
            "strongest_incidence_explanation": "the observed repeated-factor supports have z in {0,1/5,1/7}, all inside the exact D-positive chamber [0,1/4); this is a finite-support arithmetic fact",
        },
        "universal_D_positivity_no_go": _counterexample_packet(),
        "interpretation_firewall": {
            "exact": "local polynomial square criterion, parity, diagonal relation to the integral +q factor predicate, full compact-line selector sign chambers, and q=3,5,7 source-weighted census",
            "not_claimed": "no Jacobian splitting, product decomposition, isogeny, endomorphism algebra, extra automorphism, monodromy reduction, geometric stratum theorem, curve realization of the counterexample, global compatible system, asymptotic density, zero theorem, or RH implication",
            "factor_language": "elliptic-form means only the reciprocal quadratic shape 1-r*T+q*T^2 with integral Hasse-admissible trace when stated; it is not silently promoted to an elliptic curve",
        },
        "resource_contract": {
            "finite_field_enumeration": False,
            "polynomial_curve_or_member_enumeration": False,
            "root_finding": False,
            "random_sampling": False,
            "floating_point_arithmetic": False,
            "source_atom_cap_inclusive": SOURCE_ATOM_CAP_INCLUSIVE,
            "source_atom_preflight_count": source_atom_total,
            "guarded_source_atom_visits": guard.snapshot(),
            "external_dependencies": "none; Python 3.11+ standard library",
        },
        "producer_and_source_locks": {
            "validation_order": "all LF-normalized primitive digests are checked before JSON parsing or dynamic module execution; canonical payload, schema, q-ladder, member-ledger, atom-count, and mass checks follow",
            "required_payload_sha256": {
                "histogram": EXPECTED_INPUT_PAYLOAD_SHA256,
                "zero_geometry": EXPECTED_ZERO_PAYLOAD_SHA256,
                "integral_split": EXPECTED_SPLIT_PAYLOAD_SHA256,
            },
            "required_member_ledger_sha256": {
                str(q): EXPECTED_MEMBER_LEDGER_SHA256[q] for q in FROZEN_Q_VALUES
            },
            "required_lf_sha256": dict(EXPECTED_LF_SHA256),
            "locks": {
                "histogram_fixture": {
                    "path": "research/l-families/atlas/function_field/balanced_control_family_scan.json",
                    "sha256_lf_normalized": _lf_sha256(INPUT_PATH),
                    "payload_sha256": source["payload_sha256"],
                },
                "zero_geometry_fixture": {
                    "path": "research/l-families/atlas/function_field/genus2_detector_zero_geometry_conditioning.json",
                    "sha256_lf_normalized": _lf_sha256(ZERO_FIXTURE_PATH),
                    "payload_sha256": EXPECTED_ZERO_PAYLOAD_SHA256,
                },
                "selector_producer": {
                    "path": "research/l-families/atlas/function_field/frobenius_interferometry_subgroup_selectors.py",
                    "sha256_lf_normalized": _lf_sha256(SELECTOR_PRODUCER_PATH),
                },
                "integral_split_fixture": {
                    "path": "research/l-families/atlas/function_field/genus2_endoscopic_split_locus.json",
                    "sha256_lf_normalized": _lf_sha256(SPLIT_FIXTURE_PATH),
                    "payload_sha256": EXPECTED_SPLIT_PAYLOAD_SHA256,
                },
                "integral_split_producer": {
                    "path": "research/l-families/atlas/function_field/genus2_endoscopic_split_locus.py",
                    "sha256_lf_normalized": _lf_sha256(SPLIT_PRODUCER_PATH),
                },
                "producer": {
                    "path": "research/l-families/atlas/function_field/genus2_repeated_factor_tomography.py",
                    "sha256_lf_normalized": _lf_sha256(Path(__file__)),
                },
                "note": {
                    "path": "research/l-families/atlas/function_field/GENUS2_REPEATED_FACTOR_TOMOGRAPHY.md",
                    "sha256_lf_normalized": _lf_sha256(NOTE_PATH),
                },
                "test": {
                    "path": "tests/test_genus2_repeated_factor_tomography.py",
                    "sha256_lf_normalized": _lf_sha256(TEST_PATH),
                },
            },
        },
    }
    _assert_no_float(payload)
    payload["payload_sha256"] = _canonical_sha256(payload)
    return payload


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true", help="write deterministic JSON")
    mode.add_argument("--check", action="store_true", help="check committed JSON")
    parser.add_argument("path", nargs="?", type=Path, default=OUTPUT_PATH)
    args = parser.parse_args(argv)
    fixture = build_fixture()
    rendered = json.dumps(fixture, indent=2, sort_keys=True) + "\n"
    if args.write:
        args.path.write_text(rendered, encoding="utf-8", newline="\n")
        print(
            "genus2 repeated factor tomography: "
            f"q={FROZEN_Q_VALUES} atoms={fixture['resource_contract']['source_atom_preflight_count']} "
            f"payload_sha256={fixture['payload_sha256']}"
        )
        return 0
    if not args.path.is_file() or args.path.read_text(encoding="utf-8") != rendered:
        print(f"stale or missing fixture: {args.path}")
        return 1
    print(
        "genus2 repeated factor tomography check: ok "
        f"payload_sha256={fixture['payload_sha256']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
