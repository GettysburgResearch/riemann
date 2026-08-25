#!/usr/bin/env python3
"""Exact bounded proof of the marked genus-two Sym^6 trace.

For every odd prime power q this producer proves

    sum_(D monic squarefree, deg D=5) r_D(6) = -4*q*(q-1),

where 1/P_D(u)=sum r_D(n)u^n.  The theorem replay uses only exact
polynomial algebra, the source-locked genus-one cubic moment laws, and the
source-locked marked-root moments from the B4 packet.  The q=3,5,7 joint
coefficient laws are read only after the symbolic theorem is complete and
serve as held-out falsification controls.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import time
import unicodedata
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

Poly = tuple[Fraction, ...]

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT_PATH = HERE / "genus2_sym6_marked_trace_average.json"
NOTE_PATH = HERE / "GENUS2_SYM6_MARKED_TRACE_AVERAGE.md"
TEST_PATH = ROOT / "tests" / "test_genus2_sym6_marked_trace_average.py"

B4_JSON_PATH = HERE / "genus2_b4_triangular_trace_average.json"
B4_NOTE_PATH = HERE / "GENUS2_B4_TRIANGULAR_TRACE_AVERAGE.md"
GENUS1_JSON_PATH = HERE / "genus1_cubic_family_laws.json"
GENUS1_NOTE_PATH = HERE / "GENUS1_CUBIC_FAMILY_LAWS.md"
ADAPTER_JSON_PATH = HERE / "genus2_marked_weierstrass_stack_adapter.json"
ADAPTER_NOTE_PATH = HERE / "GENUS2_MARKED_WEIERSTRASS_STACK_ADAPTER.md"
CONTROL_JSON_PATH = HERE / "balanced_control_family_scan.json"

SOURCE_LOCKS: dict[str, dict[str, object]] = {
    "b4": {
        "path": B4_JSON_PATH,
        "lf": "31eec8f78bc81eb9d157f727c229efb16d112b94e7c27dbf0ea1f81f5005fde2",
        "payload": "d12099e24425badd5106f61caa151578ee04dd099a221eca7217b599783c5e5b",
    },
    "genus1": {
        "path": GENUS1_JSON_PATH,
        "lf": "b9016ae801cff40d15c53d96210b66a7d44fae7d916e827a0526b9dd42017227",
        "payload": "183ffb31ae2f5776944e162e59390c40bd7081827b8731246e72e25a882e50df",
    },
    "adapter": {
        "path": ADAPTER_JSON_PATH,
        "lf": "fe8f23f6379a70ea150a8e4f1b87054553536fde3bd23e6c1d21e252baf3b26c",
        "payload": "7b091cc158c7ff378774dcbaef5802c469c3d377384034bced1caf4fe92b3601",
    },
    "controls": {
        "path": CONTROL_JSON_PATH,
        "lf": "c3494ae852fda4e754b3b0da7cb30a26e3e38ec1c87e2619cd6fee6cdc68b68e",
        "payload": "50fd136eb0483387246766c5f2426c3e727c69cd9a89943f9268368db0f9d39c",
    },
}

MAX_SYMBOLIC_OPERATIONS_AND_INPUT_ATOMS = 4096
MAX_CONTROL_ATOMS = 512
MAX_WALL_SECONDS = 10.0


@dataclass
class ResourceGuard:
    symbolic_operations: int = 0
    input_atoms: int = 0

    def operation(self, amount: int = 1) -> None:
        if amount < 0:
            raise ValueError("operation increment must be nonnegative")
        self.symbolic_operations += amount
        self._check()

    def atoms(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("atom increment must be nonnegative")
        self.input_atoms += amount
        self._check()

    def _check(self) -> None:
        if (
            self.symbolic_operations + self.input_atoms
            > MAX_SYMBOLIC_OPERATIONS_AND_INPUT_ATOMS
        ):
            raise RuntimeError("symbolic-operation/input-atom cap exceeded")


def _canonical_bytes(value: object) -> bytes:
    def normalize(item: object) -> object:
        if isinstance(item, str):
            return unicodedata.normalize("NFC", item)
        if isinstance(item, list):
            return [normalize(entry) for entry in item]
        if isinstance(item, dict):
            return {
                unicodedata.normalize("NFC", str(key)): normalize(entry)
                for key, entry in item.items()
            }
        return item

    return json.dumps(
        normalize(value),
        allow_nan=False,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")


def _canonical_sha256(value: object) -> str:
    return hashlib.sha256(_canonical_bytes(value)).hexdigest()


def _lf_sha256(path: Path) -> str:
    data = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(data).hexdigest()


def _load_sources(names: tuple[str, ...]) -> dict[str, dict[str, object]]:
    sources: dict[str, dict[str, object]] = {}
    for name in names:
        lock = SOURCE_LOCKS[name]
        path = lock["path"]
        if not isinstance(path, Path) or _lf_sha256(path) != lock["lf"]:
            raise RuntimeError(f"source lock failed: {name}")
        value = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(value, dict):
            raise TypeError(f"source is not an object: {name}")
        claimed = value.get("payload_sha256")
        payload = dict(value)
        payload.pop("payload_sha256", None)
        if claimed != lock["payload"] or claimed != _canonical_sha256(payload):
            raise ValueError(f"source payload failed: {name}")
        sources[name] = value
    return sources


def _trim(coefficients: list[Fraction]) -> Poly:
    while len(coefficients) > 1 and coefficients[-1] == 0:
        coefficients.pop()
    return tuple(coefficients or [Fraction(0)])


def poly(*coefficients: int | Fraction) -> Poly:
    return _trim([Fraction(value) for value in coefficients])


def p_add(left: Poly, right: Poly, guard: ResourceGuard) -> Poly:
    guard.operation(max(len(left), len(right)))
    size = max(len(left), len(right))
    return _trim(
        [
            (left[index] if index < len(left) else Fraction(0))
            + (right[index] if index < len(right) else Fraction(0))
            for index in range(size)
        ]
    )


def p_scale(value: Poly, scalar: int | Fraction, guard: ResourceGuard) -> Poly:
    guard.operation(len(value))
    factor = Fraction(scalar)
    return _trim([factor * coefficient for coefficient in value])


def p_mul(left: Poly, right: Poly, guard: ResourceGuard) -> Poly:
    guard.operation(len(left) * len(right))
    result = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, a_coefficient in enumerate(left):
        for j, b_coefficient in enumerate(right):
            result[i + j] += a_coefficient * b_coefficient
    return _trim(result)


def p_sub(left: Poly, right: Poly, guard: ResourceGuard) -> Poly:
    return p_add(left, p_scale(right, -1, guard), guard)


def p_sum(values: list[Poly], guard: ResourceGuard) -> Poly:
    result = poly(0)
    for value in values:
        result = p_add(result, value, guard)
    return result


def p_eval(value: Poly, q_value: int) -> Fraction:
    result = Fraction(0)
    for coefficient in reversed(value):
        result = result * q_value + coefficient
    return result


def _pairs(value: Poly) -> list[list[int]]:
    return [[entry.numerator, entry.denominator] for entry in value]


def _assert_poly(actual: Poly, expected: Poly, label: str) -> None:
    if actual != expected:
        raise ArithmeticError(f"{label} failed: {actual!r} != {expected!r}")


def _validate_source_semantics(sources: dict[str, dict[str, object]]) -> None:
    genus1 = sources["genus1"].get("all_q_moment_theorem")
    if not isinstance(genus1, dict):
        raise TypeError("genus-one moment theorem missing")
    explicit = genus1.get("explicit_stack_sums")
    if not isinstance(explicit, dict):
        raise TypeError("genus-one explicit moment rows missing")
    expected_rows = {
        "W_2": "q^2-1",
        "W_4": "2*q^3-3*q-1",
        "W_6": "5*q^4-9*q^2-5*q-1",
    }
    if any(explicit.get(name) != value for name, value in expected_rows.items()):
        raise ValueError("genus-one cubic moment rows changed")

    b4 = sources["b4"].get("marked_root_cubic_lemma")
    if not isinstance(b4, dict):
        raise TypeError("B4 marked-root lemma missing")
    expected_b4 = {
        "M_111_2": [[0, 1], [1, 2], [-1, 6], [-1, 2], [1, 6]],
        "M_12_2": [[0, 1], [1, 2], [-1, 2], [-1, 2], [1, 2]],
        "three_M_111_4_plus_M_12_4": [
            [0, 1],
            [2, 1],
            [4, 1],
            [-4, 1],
            [-4, 1],
            [2, 1],
        ],
    }
    if any(b4.get(name) != value for name, value in expected_b4.items()):
        raise ValueError("B4 marked-root moments changed")

    adapter = sources["adapter"].get("trace_theorem")
    if not isinstance(adapter, dict):
        raise TypeError("marked-stack adapter theorem missing")
    if adapter.get("generic_groupoid_formula") != (
        "Tr_stack,q(V_lambda)=1/(q*(q-1))*sum_D Tr(Frob_D|V_lambda)"
    ):
        raise ValueError("marked-stack groupoid normalization changed")


def _symbolic_theorem(guard: ResourceGuard) -> dict[str, Poly]:
    one = poly(1)
    q_poly = poly(0, 1)
    q_minus_one = poly(-1, 1)
    q_minus_two = poly(-2, 1)

    # Total even trace moments over all monic squarefree cubics.  These are
    # q*(q-1)*W_(2j), source-locked to the genus-one packet.
    total_0 = p_mul(p_mul(q_poly, q_minus_one, guard), q_poly, guard)
    total_2 = p_mul(p_mul(q_poly, q_minus_one, guard), poly(-1, 0, 1), guard)
    total_4 = p_mul(p_mul(q_poly, q_minus_one, guard), poly(-1, -3, 0, 2), guard)
    total_6 = p_mul(p_mul(q_poly, q_minus_one, guard), poly(-1, -5, -9, 0, 5), guard)

    # J_(2j)=sum_h m_1(h)*a_h^(2j), where m_1 counts rational roots.
    # J_0 is the elementary type count; J_2 and J_4 are the B4 marked-root
    # lemma.  Only these marked moments survive the distinguished-factor
    # calculation.
    marked_0 = p_mul(q_poly, p_mul(q_minus_one, q_minus_one, guard), guard)
    marked_2 = p_mul(
        p_mul(p_mul(q_poly, q_minus_one, guard), poly(1, 1), guard),
        q_minus_two,
        guard,
    )
    marked_4 = p_scale(
        p_mul(
            p_mul(p_mul(q_poly, q_minus_one, guard), poly(1, 1), guard),
            poly(-1, -2, 1),
            guard,
        ),
        2,
        guard,
    )

    # For a squarefree cubic h, put s=sum_(P linear)(P/h) and
    # G_h(z)=1/(1+s*z+q*z^2).  Then
    # g_6=-q^3+6q^2s^2-5qs^4+s^6.
    squarefree_g6 = p_sum(
        [
            p_scale(p_mul(poly(0, 0, 0, 1), total_0, guard), -1, guard),
            p_scale(p_mul(poly(0, 0, 1), total_2, guard), 6, guard),
            p_scale(p_mul(q_poly, total_4, guard), -5, guard),
            total_6,
        ],
        guard,
    )
    _assert_poly(squarefree_g6, poly(0, 1, -1), "squarefree cubic g6 sum")

    def n_moment(total: Poly, marked: Poly) -> Poly:
        return p_sub(p_mul(q_poly, total, guard), marked, guard)

    n0 = n_moment(total_0, marked_0)
    n2 = n_moment(total_2, marked_2)
    n4 = n_moment(total_4, marked_4)

    # Mark one linear prime of the conductor f.  If N=q-m_1(h), then
    # ell_6=N*(-q^2+q-1+(3q-1)s^2-s^4)
    #       +(3q^2-2q+1)s^2+(1-4q)s^4+s^6.
    squarefree_ell6 = p_sum(
        [
            p_mul(poly(-1, 1, -1), n0, guard),
            p_mul(poly(-1, 3), n2, guard),
            p_scale(n4, -1, guard),
            p_mul(poly(1, -2, 3), total_2, guard),
            p_mul(poly(1, -4), total_4, guard),
            total_6,
        ],
        guard,
    )
    _assert_poly(
        squarefree_ell6,
        poly(0, 8, -9, 1),
        "squarefree cubic distinguished-linear sum",
    )

    # Repeated cubic moduli: h=L^3 has G_h=1; h=L^2*M has
    # G_h=(1-e*z)^(-1), e=(L/M).  The latter gives g_6=1 and
    # ell_6=9-3q independently of e.
    repeated_g6 = p_mul(q_poly, q_minus_one, guard)
    repeated_ell6_l3 = p_scale(p_mul(q_poly, q_minus_one, guard), -1, guard)
    repeated_ell6_l2m = p_mul(p_mul(q_poly, q_minus_one, guard), poly(9, -3), guard)

    all_cubic_g6 = p_add(squarefree_g6, repeated_g6, guard)
    all_cubic_ell6 = p_sum(
        [squarefree_ell6, repeated_ell6_l3, repeated_ell6_l2m], guard
    )
    _assert_poly(all_cubic_g6, poly(0), "all cubic g6 sum")
    _assert_poly(
        all_cubic_ell6,
        poly(0, 0, 2, -2),
        "all cubic distinguished-linear sum",
    )

    # A linear modulus has G=1, equally many positive and negative nonzero
    # linear signs, and quadratic-sign total -(q-1)/2.
    linear_ell6 = p_scale(q_minus_one, -1, guard)
    linear_choose2_ell6 = p_scale(
        p_mul(q_minus_one, poly(-7, 2), guard), Fraction(1, 2), guard
    )
    linear_k6 = p_scale(q_minus_one, Fraction(1, 2), guard)
    linear_weighted = p_sum(
        [
            linear_choose2_ell6,
            linear_k6,
            p_scale(p_mul(q_minus_one, linear_ell6, guard), -1, guard),
        ],
        guard,
    )
    _assert_poly(
        linear_weighted,
        p_scale(p_mul(q_minus_one, q_minus_two, guard), 2, guard),
        "linear modulus weighted row",
    )
    all_linear_weighted = p_mul(q_poly, linear_weighted, guard)

    # The C5 row vanishes after summing mu(f), and the squarefree sieve leaves
    # -q*sum_h g6(h)+sum_h ell6(h)+the linear-modulus weighted row.
    reciprocal_total = p_sum(
        [
            p_scale(p_mul(q_poly, all_cubic_g6, guard), -1, guard),
            all_cubic_ell6,
            all_linear_weighted,
        ],
        guard,
    )
    expected_total = p_scale(p_mul(q_poly, q_minus_one, guard), -4, guard)
    _assert_poly(reciprocal_total, expected_total, "Sym6 reciprocal total")

    # Sanity checks on the normalization consequences.
    family_size = p_mul(poly(0, 0, 0, 0, 1), q_minus_one, guard)
    if p_eval(reciprocal_total, 3) / p_eval(family_size, 3) != Fraction(-4, 27):
        raise ArithmeticError("mean normalization drifted")
    _assert_poly(one, poly(1), "constant polynomial")

    return {
        "total_0": total_0,
        "total_2": total_2,
        "total_4": total_4,
        "total_6": total_6,
        "marked_0": marked_0,
        "marked_2": marked_2,
        "marked_4": marked_4,
        "squarefree_cubic_g6": squarefree_g6,
        "squarefree_cubic_ell6": squarefree_ell6,
        "repeated_cubic_g6": repeated_g6,
        "repeated_cubic_ell6_l3": repeated_ell6_l3,
        "repeated_cubic_ell6_l2m": repeated_ell6_l2m,
        "all_cubic_g6": all_cubic_g6,
        "all_cubic_ell6": all_cubic_ell6,
        "linear_ell6": linear_ell6,
        "linear_choose2_ell6": linear_choose2_ell6,
        "linear_k6": linear_k6,
        "linear_weighted": linear_weighted,
        "all_linear_weighted": all_linear_weighted,
        "reciprocal_total": reciprocal_total,
        "family_size": family_size,
    }


def reciprocal_coefficient_6(a_coefficient: int, b_coefficient: int, q: int) -> int:
    values = [1]
    for degree in range(1, 7):
        value = -a_coefficient * values[degree - 1]
        if degree >= 2:
            value -= b_coefficient * values[degree - 2]
        if degree >= 3:
            value -= q * a_coefficient * values[degree - 3]
        if degree >= 4:
            value -= q * q * values[degree - 4]
        values.append(value)
    return values[6]


def _held_out_controls(
    controls: dict[str, object], guard: ResourceGuard
) -> list[dict[str, object]]:
    frozen = controls.get("frozen_enumeration_facts")
    if not isinstance(frozen, dict):
        raise TypeError("held-out control fixture lacks frozen facts")
    families = frozen.get("families")
    if not isinstance(families, list):
        raise TypeError("held-out control fixture lacks families")

    rows: list[dict[str, object]] = []
    for family in families:
        if not isinstance(family, dict):
            raise TypeError("invalid held-out family row")
        q = family.get("q")
        member_count = family.get("member_count")
        law = family.get("joint_a_D_b_D_law")
        if not isinstance(q, int) or q not in (3, 5, 7):
            raise ValueError("only q=3,5,7 may appear in held-out controls")
        if not isinstance(member_count, int) or not isinstance(law, dict):
            raise TypeError("invalid held-out family metadata")
        atoms = law.get("atoms")
        if not isinstance(atoms, list) or len(atoms) > MAX_CONTROL_ATOMS:
            raise RuntimeError("held-out atom cap exceeded")
        guard.atoms(len(atoms))
        observed = 0
        counted = 0
        for atom in atoms:
            if not isinstance(atom, dict):
                raise TypeError("invalid held-out coefficient atom")
            a_value = atom.get("a_D")
            b_value = atom.get("b_D")
            count = atom.get("member_count")
            if not all(isinstance(value, int) for value in (a_value, b_value, count)):
                raise TypeError("nonintegral held-out coefficient atom")
            observed += count * reciprocal_coefficient_6(a_value, b_value, q)
            counted += count
        if counted != member_count:
            raise ArithmeticError("held-out joint law lost family mass")
        expected = -4 * q * (q - 1)
        if observed != expected:
            raise ArithmeticError(f"held-out q={q} control failed")
        rows.append(
            {
                "q": q,
                "joint_law_atoms": len(atoms),
                "family_members": member_count,
                "observed_sum_r_D_6": observed,
                "theorem_value": expected,
                "difference": observed - expected,
                "status": "HELD_OUT_FALSIFICATION_CONTROL_ONLY",
            }
        )
    if [row["q"] for row in rows] != [3, 5, 7]:
        raise ArithmeticError("held-out field order drifted")
    return rows


def _source_manifest() -> list[dict[str, str]]:
    paths = (
        B4_JSON_PATH,
        B4_NOTE_PATH,
        GENUS1_JSON_PATH,
        GENUS1_NOTE_PATH,
        ADAPTER_JSON_PATH,
        ADAPTER_NOTE_PATH,
        CONTROL_JSON_PATH,
        NOTE_PATH,
        Path(__file__).resolve(),
        TEST_PATH,
    )
    return [
        {
            "path": path.relative_to(ROOT).as_posix(),
            "sha256_lf_normalized": _lf_sha256(path),
        }
        for path in paths
    ]


def build_fixture() -> dict[str, object]:
    started = time.perf_counter()
    sources = _load_sources(("b4", "genus1", "adapter"))
    _validate_source_semantics(sources)
    guard = ResourceGuard()
    theorem = _symbolic_theorem(guard)
    symbolic_operations_before_controls = guard.symbolic_operations
    control_source = _load_sources(("controls",))["controls"]
    controls = _held_out_controls(control_source, guard)

    polynomial_rows = {name: _pairs(value) for name, value in theorem.items()}
    payload: dict[str, object] = {
        "schema": "riemann.function_field.genus2_sym6_marked_trace_average.v1",
        "status": "PROVED_EXACTLY_FOR_EVERY_ODD_PRIME_POWER",
        "scope": {
            "q": "every odd prime power",
            "family": "all monic squarefree quintics D in F_q[T]",
            "theorem_replay_finite_fields_enumerated": 0,
            "theorem_replay_family_members_enumerated": 0,
            "sampled_q_values_used_as_theorem_input": [],
            "numeric_approximations": 0,
        },
        "definitions": {
            "curve_numerator": "P_D(u)=1+a_D*u+b_D*u^2+q*a_D*u^3+q^2*u^4",
            "reciprocal_series": "1/P_D(u)=sum_(n>=0) r_D(n)*u^n",
            "character_identity": "r_D(6)=q^3*chi_(6,0)(U_D)",
            "family_size": "#H_5(q)=q^4*(q-1)",
        },
        "theorem": {
            "reciprocal_total": "sum_D r_D(6)=-4*q*(q-1)",
            "reciprocal_mean": "E_D[r_D(6)]=-4/q^3",
            "character_mean": "E_D[chi_(6,0)(U_D)]=-4/q^6",
            "marked_stack_trace": "T_(6,0)(q)=-4",
            "raw_coefficient_identity": (
                "r_D(6)=a_D^6-5*a_D^4*b_D+4*q*a_D^4+6*a_D^2*b_D^2"
                "-6*q*a_D^2*b_D-2*q^2*a_D^2-b_D^3+2*q^2*b_D"
            ),
        },
        "mobius_euler_reduction": {
            "reciprocal_euler_coefficient": ("r_D(6)=sum_(deg f=6) mu(f)*(D/f)"),
            "squarefree_sieve": (
                "S_5(f)=C_5(f)-(q-l(f))*C_3(f)+(binom(l(f)+1,2)+k(f)-q*l(f))*C_1(f)"
            ),
            "C5_cancellation": ("C_5(f)=-q^2 and sum_(deg f=6)mu(f)=0"),
            "final_aggregate": ("sum_D r_D(6)=-q*G_3+L_3+Q_1"),
            "G_3": "sum_(deg h=3) g_6(h)=0",
            "L_3": "sum_(deg h=3) ell_6(h)=-2*q^2*(q-1)",
            "Q_1": "sum_(deg h=1) weighted_6(h)=2*q*(q-1)*(q-2)",
        },
        "cubic_channel_certificate": {
            "squarefree_g6": "-q*(q-1)",
            "repeated_g6": "q*(q-1)",
            "all_cubic_g6": "0",
            "squarefree_ell6": "q*(q-1)*(q-8)",
            "L_cubed_ell6": "-q*(q-1)",
            "L_squared_M_ell6": "q*(q-1)*(9-3*q)",
            "all_cubic_ell6": "-2*q^2*(q-1)",
            "only_marked_moments_used": ["J_0", "J_2", "J_4"],
            "higher_marked_moments_used": [],
        },
        "linear_modulus_certificate": {
            "per_modulus_ell6": "-(q-1)",
            "per_modulus_binom_ell_2_weighted": "(q-1)*(2*q-7)/2",
            "per_modulus_k6": "(q-1)/2",
            "per_modulus_combined": "2*(q-1)*(q-2)",
            "number_of_linear_moduli": "q",
        },
        "polynomials_low_to_high": polynomial_rows,
        "held_out_falsification_controls": controls,
        "literature_firewall": {
            "published_unmarked_result": (
                "Bergstrom Theorem 11.6 gives e_c(M_2,V_(6,0))=-1"
            ),
            "geometry_warning": (
                "the unmarked M_2 trace is not the marked-Weierstrass M_2(w^1) trace"
            ),
            "novelty_status": (
                "no external novelty claim; the packet proves the marked formula from source-locked branch identities"
            ),
        },
        "firewalls": [
            "This is an exact family average and marked-stack trace, not a memberwise sign theorem.",
            "The proof makes no RH, GRH, motive, compatible-system, or Euler-product transfer claim.",
            "The q=3,5,7 joint laws are held-out controls and do not enter the symbolic theorem.",
            "The theorem is not inferred from three-field interpolation.",
        ],
        "resource_contract": {
            "maximum_symbolic_operations_and_input_atoms": MAX_SYMBOLIC_OPERATIONS_AND_INPUT_ATOMS,
            "actual_symbolic_operations_before_controls": symbolic_operations_before_controls,
            "actual_symbolic_operations": guard.symbolic_operations,
            "actual_held_out_input_atoms": guard.input_atoms,
            "actual_operations_and_input_atoms": guard.symbolic_operations
            + guard.input_atoms,
            "held_out_fixture_loaded_after_symbolic_theorem": True,
            "maximum_held_out_atoms_per_field": MAX_CONTROL_ATOMS,
            "maximum_wall_seconds": MAX_WALL_SECONDS,
            "arithmetic": "exact Fraction and integer polynomial algebra",
        },
        "source_manifest": _source_manifest(),
    }
    payload["payload_sha256"] = _canonical_sha256(payload)
    if time.perf_counter() - started > MAX_WALL_SECONDS:
        raise RuntimeError("Sym6 marked-trace replay exceeded wall cap")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="write the canonical JSON")
    parser.add_argument("--check", action="store_true", help="check the canonical JSON")
    args = parser.parse_args()
    if args.write == args.check:
        parser.error("choose exactly one of --write or --check")

    fixture = build_fixture()
    rendered = json.dumps(fixture, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    if args.write:
        OUTPUT_PATH.write_text(rendered, encoding="utf-8", newline="\n")
        print(f"wrote {OUTPUT_PATH}")
        return
    if not OUTPUT_PATH.exists() or OUTPUT_PATH.read_text(encoding="utf-8") != rendered:
        raise SystemExit(f"fixture differs: {OUTPUT_PATH}")
    print(f"OK: exact Sym6 marked-trace fixture matches {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
