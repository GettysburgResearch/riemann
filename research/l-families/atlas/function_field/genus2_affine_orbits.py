#!/usr/bin/env python3
"""Exact affine-orbit certificate for the frozen genus-two q-scan families.

For a monic squarefree quintic D over F_q and g=(alpha,beta) in
AGL(1,F_q), use the right action

    (D | g)(T) = alpha^(-5) D(alpha*T + beta).

The exact character-sum coefficients then satisfy

    a_(D|g) = chi(alpha) * a_D,
    b_(D|g) = b_D,
    K_(D|g) = q*a_(D|g)^2 - b_(D|g)^2 = K_D.

This module exhausts q=3,5,7 only.  It reuses the q-scan's exact finite-field
tables and coefficient reconstruction, checks every member/action pair, and
partitions each family into exact AGL(1,q) orbits.  It uses neither numerical
roots nor per-member Euler enumeration.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import time
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Sequence

import genus2_q_scan as q_scan


Poly = tuple[int, ...]
AffineElement = tuple[int, int]
AffineMatrix = tuple[tuple[int, ...], ...]
FROZEN_Q_VALUES = (3, 5, 7)
DEFAULT_CANDIDATE_CAP = 20_000
MAX_WALL_SECONDS = 8.0
DEFAULT_GUARD_INTERVAL = 256
HERE = Path(__file__).resolve().parent
FIXTURE = HERE / "genus2_affine_orbits.json"
Q_SCAN_FIXTURE = HERE / "genus2_q_scan.json"
Q_SCAN_SOURCE = HERE / "genus2_q_scan.py"


@dataclass(frozen=True)
class OrbitAnalysis:
    payload: dict[str, object]
    k_histogram: dict[str, int]


def _canonical_sha256(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _lf_normalized_sha256(path: Path) -> str:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _guard(
    *,
    clock: Callable[[], float],
    deadline: float,
    q: int,
    stage: str,
    work_items: int,
) -> None:
    if clock() >= deadline:
        raise TimeoutError(
            f"q={q} affine-orbit certificate exceeded its monotonic wall deadline "
            f"during {stage} after {work_items} work items"
        )


def _validate_q(q: int) -> None:
    if q not in FROZEN_Q_VALUES:
        raise ValueError(
            f"refusing q={q}; frozen affine-orbit certificate supports only {FROZEN_Q_VALUES}"
        )


def affine_elements(q: int) -> tuple[AffineElement, ...]:
    """Return AGL(1,F_q) in deterministic multiplier-major order."""

    _validate_q(q)
    return tuple((alpha, beta) for alpha in range(1, q) for beta in range(q))


def compose_affine(left: AffineElement, right: AffineElement, q: int) -> AffineElement:
    """Compose for the right action: (D|left)|right = D|(left*right)."""

    _validate_q(q)
    alpha, beta = left
    gamma, delta = right
    if not (1 <= alpha < q and 1 <= gamma < q and 0 <= beta < q and 0 <= delta < q):
        raise ValueError("affine elements must have nonzero multipliers and residues in F_q")
    return alpha * gamma % q, (alpha * delta + beta) % q


def inverse_affine(element: AffineElement, q: int) -> AffineElement:
    _validate_q(q)
    alpha, beta = element
    if not (1 <= alpha < q and 0 <= beta < q):
        raise ValueError("affine element must have a nonzero multiplier and residues in F_q")
    inverse = pow(alpha, -1, q)
    return inverse, (-inverse * beta) % q


def _affine_matrix(q: int, alpha: int, beta: int) -> AffineMatrix:
    """Coefficient matrix for alpha^(-5) D(alpha*T+beta)."""

    scale = pow(alpha, -5, q)
    return tuple(
        tuple(
            0
            if column < row
            else (
                scale
                * math.comb(column, row)
                * pow(alpha, row, q)
                * pow(beta, column - row, q)
            )
            % q
            for column in range(6)
        )
        for row in range(6)
    )


def _apply_matrix(conductor: Poly, matrix: AffineMatrix, q: int) -> Poly:
    return tuple(
        sum(matrix[row][column] * conductor[column] for column in range(6)) % q
        for row in range(6)
    )


def affine_transform(
    conductor: Poly,
    q: int,
    alpha: int,
    beta: int,
) -> Poly:
    """Apply the exact monic-quintic affine action."""

    _validate_q(q)
    if len(conductor) != 6 or conductor[-1] % q != 1:
        raise ValueError("expected a monic quintic")
    if not (1 <= alpha < q and 0 <= beta < q):
        raise ValueError("alpha must be nonzero and beta must be a residue in F_q")
    return _apply_matrix(conductor, _affine_matrix(q, alpha, beta), q)


def _histogram(values: Counter[int]) -> dict[str, int]:
    return {str(key): values[key] for key in sorted(values)}


def _sign(value: int) -> str:
    return "negative" if value < 0 else "positive" if value > 0 else "zero"


def analyze_q(
    q: int,
    *,
    candidate_cap: int = DEFAULT_CANDIDATE_CAP,
    wall_limit_seconds: float = MAX_WALL_SECONDS,
    guard_interval: int = DEFAULT_GUARD_INTERVAL,
    clock: Callable[[], float] = time.monotonic,
    deadline: float | None = None,
) -> OrbitAnalysis:
    """Build one exhaustive exact affine-orbit certificate."""

    _validate_q(q)
    if candidate_cap <= 0 or q**5 > candidate_cap:
        raise ValueError(
            f"q={q} requires {q**5} monic candidates, above candidate cap {candidate_cap}"
        )
    if not 0 < wall_limit_seconds <= MAX_WALL_SECONDS:
        raise ValueError(f"wall limit must lie in (0,{MAX_WALL_SECONDS}]")
    if guard_interval < 1:
        raise ValueError("guard interval must be positive")
    start = clock()
    local_deadline = start + wall_limit_seconds
    if deadline is not None:
        local_deadline = min(local_deadline, deadline)

    tables = q_scan.build_field_tables(q)
    _guard(
        clock=clock,
        deadline=local_deadline,
        q=q,
        stage="field-table construction",
        work_items=0,
    )
    statistics: dict[Poly, tuple[int, int, int]] = {}
    sum_a_squared = 0
    sum_b_squared = 0
    sum_k = 0
    k_histogram: Counter[int] = Counter()
    for candidate_index, low_coefficients in enumerate(
        itertools.product(range(q), repeat=5), start=1
    ):
        if candidate_index % guard_interval == 0:
            _guard(
                clock=clock,
                deadline=local_deadline,
                q=q,
                stage="family enumeration",
                work_items=candidate_index,
            )
        conductor = tuple(low_coefficients) + (1,)
        if not q_scan.is_squarefree_quintic(conductor, q):
            continue
        a_d, b_d = q_scan.coefficients_from_character_sums(conductor, tables)
        k_d = q * a_d * a_d - b_d * b_d
        statistics[conductor] = (a_d, b_d, k_d)
        sum_a_squared += a_d * a_d
        sum_b_squared += b_d * b_d
        sum_k += k_d
        k_histogram[k_d] += 1
    expected_member_count = q**5 - q**4
    if len(statistics) != expected_member_count:
        raise ArithmeticError(
            f"q={q} squarefree count {len(statistics)} differs from {expected_member_count}"
        )
    _guard(
        clock=clock,
        deadline=local_deadline,
        q=q,
        stage="family enumeration",
        work_items=q**5,
    )

    actions = tuple(
        (
            alpha,
            beta,
            tables.base_character[alpha],
            _affine_matrix(q, alpha, beta),
        )
        for alpha, beta in affine_elements(q)
    )
    group_order = q * (q - 1)
    if len(actions) != group_order:
        raise ArithmeticError(f"q={q} affine group enumeration has the wrong order")

    action_edge_count = 0
    nontrivial_a_flip_checks = 0
    for conductor, (a_d, b_d, k_d) in statistics.items():
        for _alpha, _beta, character, matrix in actions:
            transformed = _apply_matrix(conductor, matrix, q)
            transformed_statistics = statistics.get(transformed)
            if transformed_statistics is None:
                raise ArithmeticError(f"q={q} affine action left the squarefree monic family")
            expected_statistics = character * a_d, b_d, k_d
            if transformed_statistics != expected_statistics:
                raise ArithmeticError(
                    f"q={q} affine coefficient law failed for {conductor}, "
                    f"expected {expected_statistics}, got {transformed_statistics}"
                )
            if character == -1 and a_d != 0:
                nontrivial_a_flip_checks += 1
            action_edge_count += 1
            if action_edge_count % guard_interval == 0:
                _guard(
                    clock=clock,
                    deadline=local_deadline,
                    q=q,
                    stage="exhaustive coefficient transformation checks",
                    work_items=action_edge_count,
                )
    expected_edge_count = expected_member_count * group_order
    if action_edge_count != expected_edge_count:
        raise ArithmeticError(f"q={q} affine action edge coverage is incomplete")

    unseen = set(statistics)
    orbit_records: list[dict[str, object]] = []
    assignment_records: list[list[list[int]]] = []
    orbit_size_histogram: Counter[int] = Counter()
    stabilizer_histogram: Counter[int] = Counter()
    sign_summaries: dict[str, dict[str, object]] = {
        sign: {
            "member_count": 0,
            "orbit_count": 0,
            "orbit_size_histogram": Counter(),
            "stabilizer_order_histogram": Counter(),
        }
        for sign in ("negative", "zero", "positive")
    }
    a_zero_member_count = 0
    a_zero_orbit_count = 0
    stabilizer_witnesses: dict[int, dict[str, object]] = {}

    while unseen:
        _guard(
            clock=clock,
            deadline=local_deadline,
            q=q,
            stage="orbit partition",
            work_items=len(orbit_records),
        )
        representative = min(unseen)
        orbit = {
            _apply_matrix(representative, matrix, q)
            for _alpha, _beta, _character, matrix in actions
        }
        if any(member not in statistics for member in orbit):
            raise ArithmeticError(f"q={q} orbit contains a nonmember")
        if any(member not in unseen for member in orbit):
            raise ArithmeticError(f"q={q} orbit partition overlaps a previous orbit")
        unseen.difference_update(orbit)
        stabilizer_elements = [
            [alpha, beta]
            for alpha, beta, _character, matrix in actions
            if _apply_matrix(representative, matrix, q) == representative
        ]
        orbit_size = len(orbit)
        stabilizer_order = len(stabilizer_elements)
        if orbit_size * stabilizer_order != group_order:
            raise ArithmeticError(f"q={q} orbit-stabilizer identity failed")

        a_squared_values = {statistics[member][0] ** 2 for member in orbit}
        b_values = {statistics[member][1] for member in orbit}
        k_values = {statistics[member][2] for member in orbit}
        if len(a_squared_values) != 1 or len(b_values) != 1 or len(k_values) != 1:
            raise ArithmeticError(f"q={q} an affine orbit changed an invariant")
        a_squared = next(iter(a_squared_values))
        b_d = next(iter(b_values))
        k_d = next(iter(k_values))
        sign = _sign(k_d)
        representative_a = statistics[representative][0]
        record: dict[str, object] = {
            "representative_coefficients_low_to_high": list(representative),
            "orbit_size": orbit_size,
            "stabilizer_order": stabilizer_order,
            "representative_a_D": representative_a,
            "a_D_squared": a_squared,
            "b_D": b_d,
            "K_D": k_d,
            "sign": sign,
        }
        orbit_records.append(record)
        for member in sorted(orbit):
            assignment_records.append([list(member), list(representative)])
        orbit_size_histogram[orbit_size] += 1
        stabilizer_histogram[stabilizer_order] += 1
        sign_row = sign_summaries[sign]
        sign_row["member_count"] = int(sign_row["member_count"]) + orbit_size
        sign_row["orbit_count"] = int(sign_row["orbit_count"]) + 1
        sign_row["orbit_size_histogram"][orbit_size] += 1  # type: ignore[index]
        sign_row["stabilizer_order_histogram"][stabilizer_order] += 1  # type: ignore[index]
        if a_squared == 0:
            a_zero_member_count += orbit_size
            a_zero_orbit_count += 1
        if stabilizer_order > 1 and stabilizer_order not in stabilizer_witnesses:
            stabilizer_witnesses[stabilizer_order] = {
                **record,
                "stabilizer_elements_alpha_beta": stabilizer_elements,
            }

    if sum(record["orbit_size"] for record in orbit_records) != expected_member_count:
        raise ArithmeticError(f"q={q} orbit sizes do not reconstruct the family")
    if len(assignment_records) != expected_member_count:
        raise ArithmeticError(f"q={q} member-to-orbit assignment is incomplete")
    if sum(int(row["member_count"]) for row in sign_summaries.values()) != expected_member_count:
        raise ArithmeticError(f"q={q} sign summaries do not reconstruct the family")

    serialized_sign_summaries = {
        sign: {
            "member_count": int(row["member_count"]),
            "orbit_count": int(row["orbit_count"]),
            "orbit_size_histogram": _histogram(row["orbit_size_histogram"]),  # type: ignore[arg-type]
            "stabilizer_order_histogram": _histogram(
                row["stabilizer_order_histogram"]  # type: ignore[arg-type]
            ),
        }
        for sign, row in sign_summaries.items()
    }
    member_sign_counts = {
        sign: int(row["member_count"]) for sign, row in serialized_sign_summaries.items()
    }
    nonzero_a_member_count = expected_member_count - a_zero_member_count
    expected_nontrivial_flips = nonzero_a_member_count * group_order // 2
    if nontrivial_a_flip_checks != expected_nontrivial_flips:
        raise ArithmeticError(f"q={q} nonsquare multiplier flip coverage is incomplete")

    _guard(
        clock=clock,
        deadline=local_deadline,
        q=q,
        stage="certificate finalization",
        work_items=action_edge_count,
    )
    return OrbitAnalysis(
        payload={
            "q": q,
            "candidate_count": q**5,
            "member_count": expected_member_count,
            "group": {
                "name": "AGL(1,F_q)",
                "order": group_order,
                "element_count": len(actions),
                "right_action": "(D|g)|h=D|(g*h), g*h=(alpha*gamma,alpha*delta+beta)",
            },
            "moment_sums": {
                "a_D_squared": sum_a_squared,
                "b_D_squared": sum_b_squared,
                "K_D": sum_k,
            },
            "action_checks": {
                "member_action_pairs_checked": action_edge_count,
                "expected_member_action_pairs": expected_edge_count,
                "family_closure_checks": action_edge_count,
                "a_D_character_law_checks": action_edge_count,
                "b_D_invariance_checks": action_edge_count,
                "K_D_invariance_checks": action_edge_count,
                "nontrivial_nonsquare_a_D_flip_checks": nontrivial_a_flip_checks,
            },
            "orbit_partition": {
                "orbit_count": len(orbit_records),
                "member_count_reconstructed": expected_member_count,
                "orbit_size_histogram": _histogram(orbit_size_histogram),
                "stabilizer_order_histogram": _histogram(stabilizer_histogram),
                "free_orbit_count": stabilizer_histogram[1],
                "nontrivial_stabilizer_orbit_count": (
                    len(orbit_records) - stabilizer_histogram[1]
                ),
                "orbit_stabilizer_checks": len(orbit_records),
                "canonical_orbit_records_sha256": _canonical_sha256(orbit_records),
                "member_to_representative_sha256": _canonical_sha256(assignment_records),
            },
            "a_D_zero_partition": {
                "zero_member_count": a_zero_member_count,
                "nonzero_member_count": nonzero_a_member_count,
                "zero_orbit_count": a_zero_orbit_count,
                "nonzero_orbit_count": len(orbit_records) - a_zero_orbit_count,
            },
            "sign_summaries": serialized_sign_summaries,
            "member_sign_counts": member_sign_counts,
            "nontrivial_stabilizer_witnesses": {
                str(order): stabilizer_witnesses[order]
                for order in sorted(stabilizer_witnesses)
            },
        },
        k_histogram=_histogram(k_histogram),
    )


def _q_scan_regression(
    analysis: OrbitAnalysis,
    expected: dict[str, object],
) -> dict[str, bool]:
    payload = analysis.payload
    moments = expected["moments"]
    checks = {
        "member_count": payload["member_count"] == expected["member_count"],
        "sum_a_squared": payload["moment_sums"]["a_D_squared"]  # type: ignore[index]
        == moments["a_squared"]["sum"],  # type: ignore[index]
        "sum_b_squared": payload["moment_sums"]["b_D_squared"]  # type: ignore[index]
        == moments["b_squared"]["sum"],  # type: ignore[index]
        "sum_K": payload["moment_sums"]["K_D"] == moments["K"]["sum"],  # type: ignore[index]
        "K_histogram": analysis.k_histogram == expected["K_histogram"],
        "sign_counts": payload["member_sign_counts"] == expected["sign_counts"],
    }
    if not all(checks.values()):
        raise ArithmeticError(
            f"q={payload['q']} affine-orbit statistics differ from the exact q-scan fixture"
        )
    return checks


def build_fixture(
    *,
    q_values: Sequence[int] = FROZEN_Q_VALUES,
    candidate_cap: int = DEFAULT_CANDIDATE_CAP,
    wall_limit_seconds: float = MAX_WALL_SECONDS,
    guard_interval: int = DEFAULT_GUARD_INTERVAL,
    clock: Callable[[], float] = time.monotonic,
) -> dict[str, object]:
    if tuple(q_values) != FROZEN_Q_VALUES:
        raise ValueError(f"frozen fixture requires exactly q={FROZEN_Q_VALUES}")
    if not 0 < wall_limit_seconds <= MAX_WALL_SECONDS:
        raise ValueError(f"wall limit must lie in (0,{MAX_WALL_SECONDS}]")
    start = clock()
    deadline = start + wall_limit_seconds
    q_scan_fixture = json.loads(Q_SCAN_FIXTURE.read_text(encoding="utf-8"))
    expected_by_q = {int(row["q"]): row for row in q_scan_fixture["families"]}
    analyses: list[OrbitAnalysis] = []
    regression_controls: dict[str, dict[str, bool]] = {}
    for q in q_values:
        analysis = analyze_q(
            q,
            candidate_cap=candidate_cap,
            wall_limit_seconds=wall_limit_seconds,
            guard_interval=guard_interval,
            clock=clock,
            deadline=deadline,
        )
        analyses.append(analysis)
        regression_controls[str(q)] = _q_scan_regression(analysis, expected_by_q[q])
        _guard(
            clock=clock,
            deadline=deadline,
            q=q,
            stage="global fixture assembly",
            work_items=int(analysis.payload["member_count"]),
        )

    source_path = Path(__file__).resolve()
    payload: dict[str, object] = {
        "schema": "riemann.function_field.genus2_affine_orbits.v1",
        "raw_fixture_id": "FUNCTION_FIELD.GENUS2.Q3_Q5_Q7.AFFINE_ORBITS.V1",
        "rigor_level": "RIGOROUS_CERTIFIED",
        "scope": "all monic squarefree quintics over F_q for exactly q=3,5,7",
        "action": {
            "definition": "D^{alpha,beta}(T)=alpha^(-5)*D(alpha*T+beta)",
            "group": "AGL(1,F_q), alpha in F_q^*, beta in F_q",
            "convention": "right action",
            "coefficient_formula": (
                "c'_j=alpha^(j-5)*sum_{i=j}^5 binom(i,j)*c_i*beta^(i-j)"
            ),
            "transformation_law": {
                "a_D": "a_{D^{alpha,beta}}=chi_q(alpha)*a_D",
                "b_D": "b_{D^{alpha,beta}}=b_D",
                "K_D": "K_{D^{alpha,beta}}=K_D for K_D=q*a_D^2-b_D^2",
            },
        },
        "exact_proof": {
            "status": "PROVED_EXACTLY_AND_EXHAUSTIVELY_REPLAYED_ON_FROZEN_FIELDS",
            "base_sum": (
                "x->alpha*x+beta permutes F_q and chi_q(alpha^(-5))=chi_q(alpha), "
                "so a transforms by chi_q(alpha)"
            ),
            "extension_sum": (
                "z->alpha*z+beta permutes F_(q^2) and every alpha in F_q^* is a square "
                "in F_(q^2), so the second character sum is fixed"
            ),
            "coefficient_consequence": (
                "b=(S_2+a^2)/2 is fixed and therefore K=q*a^2-b^2 is fixed"
            ),
            "squarefree_closure": (
                "invertible affine substitution and nonzero scalar multiplication preserve "
                "degree, monicity after normalization, and squarefreeness"
            ),
            "scope_boundary": (
                "The algebra is exact on the declared finite fields; the orbit tables do not "
                "assert an equidistribution law or any analytic-detector consequence."
            ),
        },
        "odd_trace_cancellation_corollary": {
            "status": "PROVED_FOR_EVERY_ODD_PRIME_POWER",
            "statement": (
                "For every r>=0 and every function Phi, the uniform family sum "
                "of a_D^(2r+1)*Phi(a_D^2,b_D) is zero whenever the sum is defined."
            ),
            "special_cases": [
                "every odd moment of a_D is exactly zero",
                "the joint distribution of (a_D,b_D) is invariant under (a,b)->(-a,b)",
            ],
            "proof": (
                "Choose a nonsquare alpha in F_q^* and beta=0. The affine action "
                "permutes the family, sends a_D to -a_D, and fixes both a_D^2 and b_D."
            ),
            "scope_boundary": (
                "This is an exact finite-family symmetry statement; it supplies no "
                "equidistribution rate or number-field transfer."
            ),
        },
        "method": {
            "family_arithmetic": (
                "reuse genus2_q_scan exact squarefree gcd, F_q/F_(q^2) character tables, "
                "and a_D,b_D reconstruction"
            ),
            "coverage": (
                "every family member against every affine group element, followed by a complete "
                "orbit partition and exact orbit-stabilizer checks"
            ),
            "excluded_algorithms": [
                "numerical root finding",
                "per-member Euler coefficient enumeration",
                "floating-point arithmetic",
            ],
        },
        "resource_contract": {
            "frozen_q_values": list(FROZEN_Q_VALUES),
            "candidate_cap": candidate_cap,
            "candidate_cap_scope": "PER_FIELD",
            "maximum_global_wall_seconds": wall_limit_seconds,
            "clock": "time.monotonic",
            "guard_interval_work_items": guard_interval,
            "larger_q_policy": "refuse every q outside 3,5,7",
            "runtime_not_in_identity": True,
        },
        "producer": {
            "source": "research/l-families/atlas/function_field/genus2_affine_orbits.py",
            "source_sha256_lf_normalized": _lf_normalized_sha256(source_path),
            "shared_q_scan_source": (
                "research/l-families/atlas/function_field/genus2_q_scan.py"
            ),
            "shared_q_scan_source_sha256_lf_normalized": _lf_normalized_sha256(
                Q_SCAN_SOURCE
            ),
            "shared_q_scan_fixture": (
                "research/l-families/atlas/function_field/genus2_q_scan.json"
            ),
            "shared_q_scan_fixture_canonical_sha256": _canonical_sha256(q_scan_fixture),
            "runtime_contract": "Python 3.11+ standard library; exact integer arithmetic",
            "input_provenance": "complete deterministic generation, no external data",
        },
        "families": [analysis.payload for analysis in analyses],
        "q_scan_regression_controls": regression_controls,
        "firewall": (
            "These are exact finite affine-orbit and coefficient identities for q=3,5,7. "
            "K is the existing toy coefficient minor, not a Pick/Loewner, XD, HCNC, or "
            "number-field analytic kernel. Orbit counts and stabilizers are not asymptotic laws."
        ),
    }
    payload["payload_sha256"] = _canonical_sha256(payload)
    _guard(
        clock=clock,
        deadline=deadline,
        q=FROZEN_Q_VALUES[-1],
        stage="global fixture finalization",
        work_items=sum(int(analysis.payload["member_count"]) for analysis in analyses),
    )
    return payload


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", type=Path, help="compare with this exact JSON fixture")
    parser.add_argument("--write", type=Path, help="write this exact JSON fixture")
    args = parser.parse_args(argv)
    if args.check and args.write:
        parser.error("--check and --write are mutually exclusive")
    fixture = build_fixture()
    if args.check:
        expected = json.loads(args.check.read_text(encoding="utf-8"))
        if fixture != expected:
            raise SystemExit(f"genus-two affine-orbit fixture mismatch: {args.check}")
        print(f"OK: exact genus-two affine orbits match {args.check}")
        return 0
    if args.write:
        args.write.parent.mkdir(parents=True, exist_ok=True)
        args.write.write_text(
            json.dumps(fixture, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        print(f"OK: wrote exact genus-two affine orbits {args.write}")
        return 0
    print(json.dumps(fixture, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
