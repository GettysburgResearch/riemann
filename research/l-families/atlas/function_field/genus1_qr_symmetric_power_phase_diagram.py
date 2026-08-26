"""Exact q-versus-r diagnostics from locked genus-one trace histograms.

No finite field, curve, or polynomial is enumerated here.  The only finite
input is the q=3,5,7 portion of ``genus1_cubic_family_laws.json``.  Every
symmetric-power trace is obtained from the integral Dickson recurrence, and
all reported finite-family statistics use integers or ``Fraction`` objects.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from collections.abc import Mapping
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
DEFAULT_OUTPUT = HERE / "genus1_qr_symmetric_power_phase_diagram.json"
SOURCE_FIXTURE = HERE / "genus1_cubic_family_laws.json"
HAAR_NOTE = HERE / "ELLIPTIC_SYMMETRIC_POWER_HIGH_RANK_HAAR_LIMIT.md"
NOTE = HERE / "GENUS1_QR_SYMMETRIC_POWER_PHASE_DIAGRAM.md"
TEST = ROOT / "tests" / "test_genus1_qr_symmetric_power_phase_diagram.py"

Q_VALUES = (3, 5, 7)
RANK_CAP = 32
TAIL_LEVELS = (1, 2, 3, 4)
CAPPED_SQUARE_LEVELS = (1, 2, 4)
EVEN_MOMENT_ORDERS = (2, 4, 6)
MAX_TRANSFORMED_SOURCE_ATOMS = 4096

EXPECTED_SOURCE_SCHEMA = "riemann.function_field.genus1_cubic_family_laws.v1"
EXPECTED_SOURCE_PAYLOAD_SHA256 = (
    "183ffb31ae2f5776944e162e59390c40bd7081827b8731246e72e25a882e50df"
)
EXPECTED_SOURCE_FILE_SHA256_LF = (
    "b9016ae801cff40d15c53d96210b66a7d44fae7d916e827a0526b9dd42017227"
)
EXPECTED_HAAR_NOTE_SHA256_LF = (
    "afe3ff04ea1fd3a8983c4159c4bced01b36161f5053c342bb81a84b794ae5824"
)

EXPECTED_HISTOGRAMS: dict[int, dict[int, int]] = {
    3: {-3: 1, -2: 3, -1: 3, 0: 4, 1: 3, 2: 3, 3: 1},
    5: {-4: 5, -3: 10, -2: 15, -1: 10, 0: 20, 1: 10, 2: 15, 3: 10, 4: 5},
    7: {
        -5: 7,
        -4: 28,
        -3: 21,
        -2: 42,
        -1: 28,
        0: 42,
        1: 28,
        2: 42,
        3: 21,
        4: 28,
        5: 7,
    },
}


def _canonical_sha256(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def _lf_sha256(path: Path) -> str:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    return hashlib.sha256(text.encode()).hexdigest()


def _fraction(value: Fraction | int) -> list[int]:
    fraction = Fraction(value)
    return [fraction.numerator, fraction.denominator]


def _decode_fraction(value: list[int]) -> Fraction:
    if len(value) != 2:
        raise ValueError("encoded fraction must contain numerator and denominator")
    return Fraction(value[0], value[1])


def _load_locked_histograms(
    source_fixture: Path = SOURCE_FIXTURE,
    haar_note: Path = HAAR_NOTE,
) -> dict[int, dict[int, int]]:
    if _lf_sha256(source_fixture) != EXPECTED_SOURCE_FILE_SHA256_LF:
        raise RuntimeError("source genus-one fixture file hash changed")
    if _lf_sha256(haar_note) != EXPECTED_HAAR_NOTE_SHA256_LF:
        raise RuntimeError("high-rank Haar note hash changed")

    source = json.loads(source_fixture.read_text(encoding="utf-8"))
    if source.get("schema") != EXPECTED_SOURCE_SCHEMA:
        raise RuntimeError("source genus-one fixture schema changed")
    if source.get("payload_sha256") != EXPECTED_SOURCE_PAYLOAD_SHA256:
        raise RuntimeError("source genus-one fixture payload lock changed")
    unhashed = dict(source)
    payload_hash = unhashed.pop("payload_sha256")
    if _canonical_sha256(unhashed) != payload_hash:
        raise RuntimeError("source genus-one fixture is not internally authentic")

    normalization = source.get("normalization")
    if not isinstance(normalization, dict):
        raise TypeError("source normalization is absent")
    if normalization.get("l_polynomial") != "L_D(T)=1-a_D*T+q*T^2":
        raise RuntimeError("source L-polynomial normalization changed")
    if normalization.get("model_count") != "q^2*(q-1)":
        raise RuntimeError("source model measure normalization changed")
    if not str(normalization.get("trace", "")).startswith("a_D=q+1-#E_D"):
        raise RuntimeError("source trace sign normalization changed")

    regressions = source.get("finite_regressions")
    if not isinstance(regressions, list):
        raise TypeError("source finite regressions are absent")
    rows: dict[int, dict[str, object]] = {}
    for row in regressions:
        if not isinstance(row, dict) or not isinstance(row.get("q"), int):
            raise TypeError("source finite regression row is malformed")
        rows[int(row["q"])] = row
    if any(q not in rows for q in Q_VALUES):
        raise RuntimeError("source fixture lost one of q=3,5,7")

    output: dict[int, dict[int, int]] = {}
    for q in Q_VALUES:
        raw_histogram = rows[q].get("model_trace_histogram")
        if not isinstance(raw_histogram, dict):
            raise TypeError(f"source trace histogram is absent at q={q}")
        try:
            histogram = {
                int(trace): int(count) for trace, count in raw_histogram.items()
            }
        except (TypeError, ValueError) as error:
            raise RuntimeError(
                f"source trace histogram is malformed at q={q}"
            ) from error
        if histogram != EXPECTED_HISTOGRAMS[q]:
            raise RuntimeError(f"source trace histogram atoms changed at q={q}")
        if any(count <= 0 for count in histogram.values()):
            raise RuntimeError(f"source histogram has nonpositive mass at q={q}")
        model_count = q * q * (q - 1)
        if sum(histogram.values()) != model_count:
            raise RuntimeError(f"source histogram mass changed at q={q}")
        if rows[q].get("squarefree_model_count") != model_count:
            raise RuntimeError(f"source model count field changed at q={q}")
        if any(histogram.get(-trace) != count for trace, count in histogram.items()):
            raise RuntimeError(f"source trace symmetry changed at q={q}")
        if max(trace * trace for trace in histogram) >= 4 * q:
            raise RuntimeError(f"source support reached a Hasse endpoint at q={q}")
        output[q] = histogram
    return output


def symmetric_power_trace(trace: int, q: int, rank: int) -> int:
    """Return q^(rank/2) chi_rank from the integral Dickson recurrence."""

    if q <= 0:
        raise ValueError("q must be positive")
    if rank < 0:
        raise ValueError("symmetric-power rank must be nonnegative")
    if rank == 0:
        return 1
    previous = 1
    current = trace
    for _ in range(2, rank + 1):
        previous, current = current, trace * current - q * previous
    return current


def normalized_trace_square(trace: int, q: int, rank: int) -> Fraction:
    value = symmetric_power_trace(trace, q, rank)
    return Fraction(value * value, q**rank)


def _mean(weighted_sum: Fraction, mass: int) -> Fraction:
    if mass <= 0:
        raise ValueError("mean mass must be positive")
    return weighted_sum / mass


def _rank_row(
    q: int,
    histogram: Mapping[int, int],
    trace_values: Mapping[int, int],
    rank: int,
    endpoint_trace: int,
) -> dict[str, object]:
    if set(trace_values) != set(histogram):
        raise ValueError("rank trace values do not match the locked support")
    mass = sum(histogram.values())
    sign_counts = {"negative": 0, "zero": 0, "positive": 0}
    tail_counts = {level: 0 for level in TAIL_LEVELS}
    capped_sums = {level: Fraction(0) for level in CAPPED_SQUARE_LEVELS}
    raw_sums = {order: Fraction(0) for order in EVEN_MOMENT_ORDERS}
    endpoint_sums = {order: Fraction(0) for order in EVEN_MOMENT_ORDERS}
    trimmed_sums = {order: Fraction(0) for order in EVEN_MOMENT_ORDERS}
    endpoint_mass = 0
    endpoint_square: Fraction | None = None

    for trace, count in sorted(histogram.items()):
        value = trace_values[trace]
        if value < 0:
            sign_counts["negative"] += count
        elif value > 0:
            sign_counts["positive"] += count
        else:
            sign_counts["zero"] += count
        square = Fraction(value * value, q**rank)
        for level in TAIL_LEVELS:
            if square > level * level:
                tail_counts[level] += count
        for level in CAPPED_SQUARE_LEVELS:
            capped_sums[level] += count * min(square, Fraction(level * level))
        is_endpoint = abs(trace) == endpoint_trace
        if is_endpoint:
            endpoint_mass += count
            if endpoint_square is None:
                endpoint_square = square
            elif endpoint_square != square:
                raise ArithmeticError("central sign changed endpoint trace square")
        for order in EVEN_MOMENT_ORDERS:
            term = count * square ** (order // 2)
            raw_sums[order] += term
            if is_endpoint:
                endpoint_sums[order] += term
            else:
                trimmed_sums[order] += term

    if sum(sign_counts.values()) != mass:
        raise ArithmeticError("sign counts lost histogram mass")
    if endpoint_square is None or endpoint_mass <= 0 or endpoint_mass >= mass:
        raise ArithmeticError("endpoint trace-class split is invalid")
    if any(raw_sums[order] <= 0 for order in EVEN_MOMENT_ORDERS):
        raise ArithmeticError("positive even moment vanished")

    raw_moments = {
        str(order): _mean(raw_sums[order], mass) for order in EVEN_MOMENT_ORDERS
    }
    endpoint_contributions = {
        str(order): _mean(endpoint_sums[order], mass) for order in EVEN_MOMENT_ORDERS
    }
    endpoint_shares = {
        str(order): endpoint_sums[order] / raw_sums[order]
        for order in EVEN_MOMENT_ORDERS
    }
    trimmed_mass = mass - endpoint_mass
    trimmed_moments = {
        str(order): _mean(trimmed_sums[order], trimmed_mass)
        for order in EVEN_MOMENT_ORDERS
    }

    return {
        "rank_r": rank,
        "frequency_N": rank + 1,
        "sign_counts": sign_counts,
        "sign_masses": {
            key: _fraction(Fraction(count, mass)) for key, count in sign_counts.items()
        },
        "strict_tail_abs_gt": {
            str(level): {
                "count": tail_counts[level],
                "mass": _fraction(Fraction(tail_counts[level], mass)),
            }
            for level in TAIL_LEVELS
        },
        "bounded_capped_square_means": {
            f"min_x2_{level * level}": _fraction(_mean(capped_sums[level], mass))
            for level in CAPPED_SQUARE_LEVELS
        },
        "raw_even_moments": {
            order: _fraction(value) for order, value in raw_moments.items()
        },
        "endpoint_trace_classes": {
            "normalized_trace_square": _fraction(endpoint_square),
            "raw_even_moment_contributions": {
                order: _fraction(value)
                for order, value in endpoint_contributions.items()
            },
            "shares_of_raw_even_moments": {
                order: _fraction(value) for order, value in endpoint_shares.items()
            },
        },
        "endpoint_trimmed_conditional_even_moments": {
            order: _fraction(value) for order, value in trimmed_moments.items()
        },
        "haar_boundary_scalings": {
            "raw_fourth_over_N": _fraction(raw_moments["4"] / (rank + 1)),
            "raw_sixth_over_N_cubed": _fraction(raw_moments["6"] / (rank + 1) ** 3),
        },
    }


def _first_adjacent_change(
    rows: list[dict[str, object]],
    field: str,
    key: str,
    direction: str,
) -> dict[str, object] | None:
    if direction not in {"increase", "decrease"}:
        raise ValueError("direction must be increase or decrease")
    for previous, current in itertools.pairwise(rows):
        previous_container = previous.get(field)
        current_container = current.get(field)
        if not isinstance(previous_container, dict) or not isinstance(
            current_container, dict
        ):
            raise TypeError("summary field is malformed")
        previous_value = _decode_fraction(previous_container[key])
        current_value = _decode_fraction(current_container[key])
        changed = (
            current_value > previous_value
            if direction == "increase"
            else current_value < previous_value
        )
        if changed:
            return {
                "from_rank": previous["rank_r"],
                "to_rank": current["rank_r"],
                "from_value": _fraction(previous_value),
                "to_value": _fraction(current_value),
            }
    return None


def _extremum(
    rows: list[dict[str, object]], field: str, key: str, maximum: bool
) -> dict[str, object]:
    values: list[tuple[int, Fraction]] = []
    for row in rows:
        container = row.get(field)
        if not isinstance(container, dict):
            raise TypeError("extremum field is malformed")
        values.append((int(row["rank_r"]), _decode_fraction(container[key])))
    target = (
        max(value for _, value in values)
        if maximum
        else min(value for _, value in values)
    )
    return {
        "value": _fraction(target),
        "ranks": [rank for rank, value in values if value == target],
    }


def _nonzero_trace_zero_resonances(
    histogram: Mapping[int, int],
    trace_trajectories: Mapping[int, tuple[int, ...]],
) -> list[dict[str, object]]:
    if set(trace_trajectories) != set(histogram):
        raise ValueError("trace trajectories do not match the locked support")
    output = []
    for trace in sorted(histogram):
        if trace == 0:
            continue
        ranks = [
            rank for rank, value in enumerate(trace_trajectories[trace]) if value == 0
        ]
        if ranks:
            output.append(
                {
                    "trace": trace,
                    "source_count": histogram[trace],
                    "zero_ranks_through_cap": ranks,
                }
            )
    return output


def _q_row(q: int, histogram: Mapping[int, int], rank_cap: int) -> dict[str, object]:
    endpoint_trace = max(abs(trace) for trace in histogram)
    endpoint_mass = sum(
        count for trace, count in histogram.items() if abs(trace) == endpoint_trace
    )
    model_count = sum(histogram.values())
    bound_square = Fraction(4 * q, 4 * q - endpoint_trace * endpoint_trace)
    trace_trajectories = {
        trace: tuple(
            symmetric_power_trace(trace, q, rank) for rank in range(rank_cap + 1)
        )
        for trace in sorted(histogram)
    }
    rows = [
        _rank_row(
            q,
            histogram,
            {trace: values[rank] for trace, values in trace_trajectories.items()},
            rank,
            endpoint_trace,
        )
        for rank in range(rank_cap + 1)
    ]
    snapshots = {}
    for rank in (8, 16, 32):
        if rank <= rank_cap:
            scaling = rows[rank]["haar_boundary_scalings"]
            if not isinstance(scaling, dict):
                raise RuntimeError("Haar boundary scaling row is malformed")
            snapshots[str(rank)] = scaling

    return {
        "q": q,
        "source_model_count": model_count,
        "source_trace_histogram": {
            str(trace): count for trace, count in sorted(histogram.items())
        },
        "source_histogram_atom_count": len(histogram),
        "extreme_observed_source_trace_classes": {
            "absolute_trace": endpoint_trace,
            "combined_count": endpoint_mass,
            "combined_mass": _fraction(Fraction(endpoint_mass, model_count)),
            "hasse_endpoint_is_absent": endpoint_trace * endpoint_trace < 4 * q,
            "uniform_character_square_upper_bound": _fraction(bound_square),
            "bound_formula": "4q/(4q-t_max^2)",
        },
        "rank_rows_0_through_32": rows,
        "bounded_cap_summary": {
            "raw_fourth_moment_minimum": _extremum(
                rows, "raw_even_moments", "4", False
            ),
            "raw_fourth_moment_maximum": _extremum(rows, "raw_even_moments", "4", True),
            "endpoint_fourth_share_maximum": _extremum(
                [
                    {
                        "rank_r": row["rank_r"],
                        "share": row["endpoint_trace_classes"][
                            "shares_of_raw_even_moments"
                        ],
                    }
                    for row in rows
                ],
                "share",
                "4",
                True,
            ),
            "capped_square_level_2_minimum": _extremum(
                rows, "bounded_capped_square_means", "min_x2_4", False
            ),
            "capped_square_level_2_maximum": _extremum(
                rows, "bounded_capped_square_means", "min_x2_4", True
            ),
            "first_raw_fourth_moment_decrease": _first_adjacent_change(
                rows, "raw_even_moments", "4", "decrease"
            ),
            "first_capped_square_level_2_decrease": _first_adjacent_change(
                rows,
                "bounded_capped_square_means",
                "min_x2_4",
                "decrease",
            ),
            "first_capped_square_level_2_increase": _first_adjacent_change(
                rows,
                "bounded_capped_square_means",
                "min_x2_4",
                "increase",
            ),
            "Haar_scaled_moment_snapshots": snapshots,
            "nonzero_trace_zero_resonances": _nonzero_trace_zero_resonances(
                histogram, trace_trajectories
            ),
        },
    }


def build_fixture(
    rank_cap: int = RANK_CAP,
    source_fixture: Path = SOURCE_FIXTURE,
    haar_note: Path = HAAR_NOTE,
) -> dict[str, object]:
    if rank_cap != RANK_CAP:
        raise ValueError(f"rank cap must equal the locked cap {RANK_CAP}")
    histograms = _load_locked_histograms(source_fixture, haar_note)
    source_atom_count = sum(len(histograms[q]) for q in Q_VALUES)
    transformed_atom_visits = source_atom_count * (rank_cap + 1)
    if transformed_atom_visits > MAX_TRANSFORMED_SOURCE_ATOMS:
        raise RuntimeError("transformed source-atom cap exceeded")

    q_rows = [_q_row(q, histograms[q], rank_cap) for q in Q_VALUES]
    payload: dict[str, object] = {
        "schema": "riemann.function_field.genus1_qr_symmetric_power_phase_diagram.v1",
        "status": "EXACT_LOCKED_Q3_Q5_Q7_DIAGNOSTICS_WITH_SEPARATE_HAAR_COMPARATOR",
        "scope": {
            "finite_facts": "exact uniform-model histogram transforms only at q=3,5,7 and 0<=r<=32",
            "compact_asymptotics": (
                "weak-limit, tail, and moment-growth statements imported from the "
                "pinned high-rank SU(2) Haar note; the exact fourth moment is also "
                "derived directly by character orthogonality in the proof note"
            ),
            "not_claimed": [
                "an arithmetic q-to-infinity limit",
                "uniform equidistribution with growing r",
                "monodromy, automorphy, Euler-product, zero, RH, or GRH consequences",
            ],
        },
        "source_locks": {
            "genus_one_fixture": {
                "path": SOURCE_FIXTURE.name,
                "schema": EXPECTED_SOURCE_SCHEMA,
                "payload_sha256": EXPECTED_SOURCE_PAYLOAD_SHA256,
                "file_sha256_lf_normalized": EXPECTED_SOURCE_FILE_SHA256_LF,
                "consumed_fields": ["q=3", "q=5", "q=7"],
            },
            "high_rank_Haar_note": {
                "path": HAAR_NOTE.name,
                "file_sha256_lf_normalized": EXPECTED_HAAR_NOTE_SHA256_LF,
            },
        },
        "normalization": {
            "base_trace": "t=a_D=q+1-#E_D(F_q)",
            "base_local_factor": "1-tT+qT^2",
            "normalized_symmetric_power_trace": "x_r=q^(-r/2) S_r(t,q)=U_r(t/(2sqrt(q)))",
            "integral_recurrence": "S_0=1, S_1=t, S_r=t*S_(r-1)-q*S_(r-2)",
            "exact_square": "x_r^2=S_r(t,q)^2/q^r",
            "measure": "uniform monic squarefree cubic models; equivalently the normalized elliptic stack measure in the source packet",
        },
        "diagnostic_definitions": {
            "bounded_transforms": [
                "E[min(x_r^2,1)]",
                "E[min(x_r^2,4)]",
                "E[min(x_r^2,16)]",
            ],
            "strict_tail_counts": ["|x_r|>1", "|x_r|>2", "|x_r|>3", "|x_r|>4"],
            "trim": "delete both observed extreme source-trace classes |t|=t_max, then renormalize the remaining source mass",
            "endpoint_contribution": "the unrenormalized contribution and share of the raw even moment from |t|=t_max",
            "all_finite_arithmetic": "integers and reduced rational pairs [numerator,denominator]; no binary floats",
        },
        "frozen_q3_q5_q7_facts": q_rows,
        "finite_q_resonance_certificates": {
            "trace_zero_all_three_fields": {
                "identity": "S_r(0,q)=0 for odd r and (-q)^(r/2) for even r",
                "normalized_square": "0 for odd r and 1 for even r",
                "source_masses": {
                    str(q): _fraction(
                        Fraction(histograms[q][0], sum(histograms[q].values()))
                    )
                    for q in Q_VALUES
                },
            },
            "q3_trace_plus_minus_3": {
                "angle": "theta=pi/6 or 5pi/6",
                "combined_source_mass": _fraction(Fraction(2, 18)),
                "normalized_square_by_N_mod_6": {
                    "0": [0, 1],
                    "1": [1, 1],
                    "2": [3, 1],
                    "3": [4, 1],
                    "4": [3, 1],
                    "5": [1, 1],
                },
                "annihilated_ranks_through_32": [5, 11, 17, 23, 29],
            },
            "bounded_scan_scope": "nonzero trace zeros were scanned exactly only through r=32; only q=3,t=+/-3 occur in that bounded scan",
        },
        "fixed_q_versus_Haar_high_rank": {
            "exact_fixed_q_fact": (
                "because every locked support has t^2<4q, |x_r|^2<=4q/(4q-t^2) "
                "uniformly in r; hence for p>3, E|x_r|^p/(r+1)^(p-3)->0 at each fixed locked q"
            ),
            "Haar_comparator": {
                "fourth_moment": "E_Haar[chi_r^4]=r+1, so division by r+1 is exactly 1",
                "sixth_moment": "E_Haar[|chi_r|^6]~(1/2)(r+1)^3",
                "weak_limit": "W=sin(U)/sin(Theta)",
                "tail": "P(|W|>x)~16/(9*pi^2)*x^(-3)",
                "support": "unbounded",
            },
            "common_locked_tail_cutoff": "P_q(|x_r|>4)=0 for every r at q=3,5,7",
            "arithmetic_iterated_limits_evaluated": False,
            "interpretation": (
                "this proves fixed-histogram/high-rank nonuniformity.  Calling it a q-versus-r "
                "order-of-limits theorem would additionally require an arithmetic q-to-infinity "
                "equidistribution statement, which this packet neither assumes nor proves"
            ),
        },
        "producer": {
            "script": Path(__file__).name,
            "source_sha256_lf_normalized": _lf_sha256(Path(__file__).resolve()),
            "note": NOTE.name,
            "note_sha256_lf_normalized": _lf_sha256(NOTE),
            "test": str(TEST.relative_to(ROOT)).replace("\\", "/"),
            "test_sha256_lf_normalized": _lf_sha256(TEST),
        },
        "resource_contract": {
            "rank_cap": rank_cap,
            "source_histogram_atoms_consumed": source_atom_count,
            "transformed_source_atom_visits": transformed_atom_visits,
            "transformed_source_atom_cap": MAX_TRANSFORMED_SOURCE_ATOMS,
            "cap_semantics": (
                "27 distinct source atoms times 33 ranks; rank diagnostics and the "
                "resonance scan reuse the same 891 materialized trace values"
            ),
            "new_finite_field_or_curve_enumerations": 0,
            "arithmetic": "exact integers and fractions",
        },
    }
    payload["payload_sha256"] = _canonical_sha256(payload)
    return payload


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", type=Path)
    parser.add_argument("--write", type=Path)
    args = parser.parse_args(argv)
    if args.check and args.write:
        parser.error("--check and --write are mutually exclusive")
    fixture = build_fixture()
    if args.check:
        expected = json.loads(args.check.read_text(encoding="utf-8"))
        if fixture != expected:
            raise SystemExit(f"q-r phase-diagram fixture mismatch: {args.check}")
        print(f"OK: exact q-r phase diagram matches {args.check}")
    elif args.write:
        args.write.write_text(json.dumps(fixture, indent=2) + "\n", encoding="utf-8")
        print(f"WROTE: {args.write}")
    else:
        print(json.dumps(fixture, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
