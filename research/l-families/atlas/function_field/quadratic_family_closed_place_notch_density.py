#!/usr/bin/env python3
"""Count closed-place odd-notch support zeros by bounded exact DP.

The producer source-locks the committed closed-place weight-notch packet and
counts monic primitive squarefree conductors whose irreducible factor degrees
all exceed the support threshold.  It evaluates only the irreducible-count
formula and a truncated coefficient dynamic program: no polynomial or
irreducible is enumerated.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import time
from fractions import Fraction
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT = HERE / "quadratic_family_closed_place_notch_density.json"
NOTE = HERE / "QUADRATIC_FAMILY_CLOSED_PLACE_NOTCH_DENSITY.md"
TEST = ROOT / "tests" / "test_quadratic_family_closed_place_notch_density.py"
SOURCE = HERE / "quadratic_family_closed_place_weight_notch.json"

SOURCE_COMMIT = "9716d2261e9e7843a6c1ffffd67ee8d6756060aa"
SOURCE_BLOB = "964935a3a936f03011366546d966ef1473c4e832"
SOURCE_LF_SHA256 = "3a024c4661a89d57943e15af829bffd2108b063156748322bb80637eed4e332b"
SOURCE_PAYLOAD_SHA256 = (
    "510f35eacebfdb18d5d5c622a37c2c43c687f960e3959684949d118a7106d4b3"
)
SOURCE_BYTES = 21_795
SOURCE_SCHEMA = "riemann.function_field.quadratic_family_closed_place_weight_notch.v1"

SCHEMA = "riemann.function_field.quadratic_family_closed_place_notch_density.v1"
REPLAY_QS = (3, 5, 7)
MIN_N = 2
MAX_N = 80
MAX_M = 2 * MAX_N - 1
SERIALIZED_NS = tuple(range(2, 11)) + (20, 21, 40, 41, 79, 80)
MAX_SOURCE_BYTES = 32_768
MAX_OUTPUT_BYTES = 65_536
MAX_DP_TRANSITIONS_PER_ROW = 100_000
MAX_TOTAL_DP_TRANSITIONS = 8_000_000
MAX_REPLAY_ROWS = len(REPLAY_QS) * (MAX_N - MIN_N + 1)
MAX_SERIALIZED_ROWS = len(REPLAY_QS) * len(SERIALIZED_NS)
WALL_SECONDS = 10.0


def _validate_q(q: int) -> None:
    if type(q) is not int or q not in REPLAY_QS:
        raise ValueError(f"bounded replay requires q in {REPLAY_QS}")


def _validate_n(n: int) -> None:
    if type(n) is not int or not MIN_N <= n <= MAX_N:
        raise ValueError(f"bounded replay requires {MIN_N}<=n<={MAX_N}")


def notch_parameters(n: int) -> tuple[int, int, int]:
    """Return M=2n-1, h=floor(n/2), and the first allowed degree h+1."""
    _validate_n(n)
    conductor_degree = 2 * n - 1
    threshold = n // 2
    return conductor_degree, threshold, threshold + 1


def _divisors(integer: int) -> tuple[int, ...]:
    if type(integer) is not int or integer < 1 or integer > MAX_M:
        raise ValueError(f"divisor replay requires 1<=degree<={MAX_M}")
    return tuple(divisor for divisor in range(1, integer + 1) if integer % divisor == 0)


def _mobius(integer: int) -> int:
    if type(integer) is not int or integer < 1 or integer > MAX_M:
        raise ValueError(f"Mobius replay requires 1<=input<={MAX_M}")
    remaining = integer
    prime_factors = 0
    prime = 2
    while prime * prime <= remaining:
        if remaining % prime == 0:
            remaining //= prime
            prime_factors += 1
            if remaining % prime == 0:
                return 0
            while remaining % prime == 0:
                remaining //= prime
        prime += 1
    if remaining > 1:
        prime_factors += 1
    return -1 if prime_factors % 2 else 1


def irreducible_count(q: int, degree: int) -> int:
    """Return I_q(degree) from the Mobius formula, without listing factors."""
    _validate_q(q)
    if type(degree) is not int or not 1 <= degree <= MAX_M:
        raise ValueError(f"irreducible-count replay requires 1<=degree<={MAX_M}")
    count = (
        sum(
            _mobius(divisor) * q ** (degree // divisor) for divisor in _divisors(degree)
        )
        // degree
    )
    if count < 0:
        raise ArithmeticError("irreducible-count formula returned a negative value")
    return count


def _support_forced_zero_dp(q: int, n: int) -> tuple[int, dict[str, int]]:
    """Compute the required coefficient and a deterministic resource ledger."""
    _validate_q(q)
    conductor_degree, _, first_allowed_degree = notch_parameters(n)
    coefficients = [0] * (conductor_degree + 1)
    coefficients[0] = 1
    transitions = 0
    peak_nonzero_states = 1
    maximum_local_multiplicity = 0
    formula_evaluations = 0

    for degree in range(first_allowed_degree, conductor_degree + 1):
        available = irreducible_count(q, degree)
        formula_evaluations += 1
        local_cap = min(available, conductor_degree // degree)
        maximum_local_multiplicity = max(maximum_local_multiplicity, local_cap)
        local_coefficients = tuple(
            comb(available, count) for count in range(local_cap + 1)
        )
        updated = [0] * (conductor_degree + 1)
        for subtotal, coefficient in enumerate(coefficients):
            if coefficient == 0:
                continue
            allowed = min(local_cap, (conductor_degree - subtotal) // degree)
            for multiplicity in range(allowed + 1):
                transitions += 1
                if transitions > MAX_DP_TRANSITIONS_PER_ROW:
                    raise RuntimeError("per-row DP transition cap exceeded")
                updated[subtotal + multiplicity * degree] += (
                    coefficient * local_coefficients[multiplicity]
                )
        coefficients = updated
        peak_nonzero_states = max(
            peak_nonzero_states,
            sum(coefficient != 0 for coefficient in coefficients),
        )

    count = coefficients[conductor_degree]
    if count <= 0:
        raise ArithmeticError("support-forced zero count must be positive")
    return count, {
        "factor_degrees_processed": formula_evaluations,
        "irreducible_formula_evaluations": formula_evaluations,
        "transitions": transitions,
        "peak_nonzero_states": peak_nonzero_states,
        "maximum_local_multiplicity": maximum_local_multiplicity,
    }


def support_forced_zero_count(q: int, n: int) -> int:
    """Return [x^(2n-1)] product_(d>floor(n/2))(1+x^d)^I_q(d)."""
    return _support_forced_zero_dp(q, n)[0]


def primitive_squarefree_conductor_count(q: int, n: int) -> int:
    """Count monic squarefree degree-(2n-1) primitive conductors."""
    _validate_q(q)
    conductor_degree, _, _ = notch_parameters(n)
    return q**conductor_degree - q ** (conductor_degree - 1)


def support_forced_zero_density(q: int, n: int) -> Fraction:
    return Fraction(
        support_forced_zero_count(q, n),
        primitive_squarefree_conductor_count(q, n),
    )


def _fraction_pair(value: Fraction) -> list[int]:
    return [value.numerator, value.denominator]


def exact_density_row(q: int, n: int) -> tuple[dict[str, object], dict[str, int]]:
    count, statistics = _support_forced_zero_dp(q, n)
    conductor_degree, threshold, first_allowed_degree = notch_parameters(n)
    total = primitive_squarefree_conductor_count(q, n)
    if count > total:
        raise ArithmeticError("certified subset exceeds the ambient conductor family")
    density = Fraction(count, total)
    row: dict[str, object] = {
        "q": q,
        "n": n,
        "conductor_degree_M": conductor_degree,
        "support_threshold_h": threshold,
        "first_allowed_factor_degree": first_allowed_degree,
        "certified_zero_count": count,
        "primitive_squarefree_conductor_count": total,
        "certified_density": _fraction_pair(density),
        "M_times_certified_density": _fraction_pair(conductor_degree * density),
    }
    return row, statistics


def _canonical_sha256(payload: object) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def _lf_sha256(data: bytes) -> str:
    return hashlib.sha256(data.replace(b"\r\n", b"\n")).hexdigest()


def _file_sha256(path: Path) -> str:
    return _lf_sha256(path.read_bytes())


def _git_blob(path: Path, commit: str) -> str:
    relative = path.relative_to(ROOT).as_posix()
    result = subprocess.run(
        ["git", "rev-parse", f"{commit}:{relative}"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def _git_file(path: Path, commit: str) -> bytes:
    relative = path.relative_to(ROOT).as_posix()
    result = subprocess.run(
        ["git", "show", f"{commit}:{relative}"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    return result.stdout


def load_locked_source() -> dict[str, object]:
    if _git_blob(SOURCE, SOURCE_COMMIT) != SOURCE_BLOB:
        raise RuntimeError("closed-place source git blob drifted")
    source_bytes = _git_file(SOURCE, SOURCE_COMMIT)
    if len(source_bytes) > MAX_SOURCE_BYTES:
        raise RuntimeError("source-byte cap exceeded")
    if len(source_bytes) != SOURCE_BYTES:
        raise RuntimeError("closed-place source byte count drifted")
    if _lf_sha256(source_bytes) != SOURCE_LF_SHA256:
        raise RuntimeError("closed-place source LF hash drifted")
    payload = json.loads(source_bytes.decode("utf-8"))
    claimed = payload.get("payload_sha256")
    without_hash = dict(payload)
    without_hash.pop("payload_sha256", None)
    if claimed != SOURCE_PAYLOAD_SHA256 or _canonical_sha256(without_hash) != claimed:
        raise RuntimeError("closed-place source payload lock failed")
    if payload.get("schema") != SOURCE_SCHEMA:
        raise RuntimeError("closed-place source schema drifted")
    notch = payload.get("primitive_conductor_weight_notch")
    if not isinstance(notch, dict):
        raise TypeError("closed-place source notch section is not an object")
    odd = notch.get("odd_M_2n_minus_1")
    expected = {
        "exact_residual": "S_(n,Q)=sum_(k=1..floor(n/2)) a_k*D_(n-2*k)",
        "exact_zero": "If min_i d_i>floor(n/2), then every relevant a_k vanishes and S_(n,Q)=0 exactly.",
    }
    if not isinstance(odd, dict):
        raise TypeError("closed-place odd-notch source section is not an object")
    if any(odd.get(key) != value for key, value in expected.items()):
        raise RuntimeError("locked odd-notch support theorem drifted")
    return payload


def build_payload() -> dict[str, object]:
    started = time.monotonic()
    source = load_locked_source()
    rows: list[dict[str, object]] = []
    all_replayed_digest_rows: list[list[int]] = []
    total_transitions = 0
    total_formula_evaluations = 0
    maximum_row_transitions = 0
    maximum_peak_nonzero_states = 0
    maximum_local_multiplicity = 0
    replayed_rows = 0

    for q in REPLAY_QS:
        for n in range(MIN_N, MAX_N + 1):
            row, statistics = exact_density_row(q, n)
            replayed_rows += 1
            conductor_degree, _, first_allowed_degree = notch_parameters(n)
            certified_count = row["certified_zero_count"]
            total_count = row["primitive_squarefree_conductor_count"]
            if type(certified_count) is not int or type(total_count) is not int:
                raise TypeError("all-row digest requires exact integer counts")
            all_replayed_digest_rows.append(
                [
                    q,
                    n,
                    conductor_degree,
                    first_allowed_degree,
                    certified_count,
                    total_count,
                ]
            )
            if n in SERIALIZED_NS:
                rows.append(row)
            total_transitions += statistics["transitions"]
            total_formula_evaluations += statistics["irreducible_formula_evaluations"]
            maximum_row_transitions = max(
                maximum_row_transitions, statistics["transitions"]
            )
            maximum_peak_nonzero_states = max(
                maximum_peak_nonzero_states,
                statistics["peak_nonzero_states"],
            )
            maximum_local_multiplicity = max(
                maximum_local_multiplicity,
                statistics["maximum_local_multiplicity"],
            )
            if total_transitions > MAX_TOTAL_DP_TRANSITIONS:
                raise RuntimeError("aggregate DP transition cap exceeded")

    if replayed_rows != MAX_REPLAY_ROWS:
        raise ArithmeticError("bounded DP replay coverage drifted")
    if len(rows) != MAX_SERIALIZED_ROWS:
        raise ArithmeticError("serialized density-row coverage drifted")

    payload: dict[str, object] = {
        "schema": SCHEMA,
        "status": "EXACT_FINITE_COUNTS_FROM_SOURCE_LOCKED_SUPPORT_THEOREM_AND_BOUNDED_COEFFICIENT_DP",
        "scope": "monic primitive squarefree closed-place conductors Q over F_q, q in {3,5,7}, at odd notch degree M=2*n-1; DP-replayed for every 2<=n<=80 with a deterministic sparse exact table serialized",
        "source_lock": {
            "path": SOURCE.relative_to(ROOT).as_posix(),
            "commit": SOURCE_COMMIT,
            "git_blob": SOURCE_BLOB,
            "sha256_lf_normalized": SOURCE_LF_SHA256,
            "payload_sha256": SOURCE_PAYLOAD_SHA256,
            "schema": source["schema"],
            "imported_exact_residual": source["primitive_conductor_weight_notch"][
                "odd_M_2n_minus_1"
            ]["exact_residual"],
            "imported_support_zero": source["primitive_conductor_weight_notch"][
                "odd_M_2n_minus_1"
            ]["exact_zero"],
            "transitive_packet_files": source["packet_files_lf_sha256"],
        },
        "exact_finite_count": {
            "parameters": "M=2*n-1, h=floor(n/2), L=h+1",
            "dp_replay_n_range": [MIN_N, MAX_N],
            "serialized_n_values": list(SERIALIZED_NS),
            "certified_subset": "all irreducible factor degrees d of Q satisfy d>=L, equivalently min_i d_i>h",
            "coefficient_formula": "Z_(q,n)=[x^M] product_(d=L..M) (1+x^d)^(I_q(d))",
            "multiset_formula": "Z_(q,n)=sum_(m_L,...,m_M>=0; sum_d d*m_d=M) product_(d=L..M) binom(I_q(d),m_d), with sum_d m_d<=3",
            "irreducible_count_formula": "I_q(d)=(1/d)*sum_(e|d) mobius(e)*q^(d/e)",
            "ambient_count": "|H_M(q)|=q^M-q^(M-1)",
            "density": "delta_(q,n)=Z_(q,n)/(q^M-q^(M-1))",
            "factor_bound": "4*L>M, so every counted conductor has at most three irreducible factors",
            "semantics": "Z_(q,n) counts conductors certified to have S_(n,Q)=0 by coefficient support; it is not asserted to count every conductor whose raw sum vanishes for any reason",
            "all_replayed_rows_digest": {
                "algorithm": "sha256",
                "canonical_encoding": "compact JSON of the q-major, then n-major ordered list [q,n,M,L,Z,total] for every replayed row",
                "row_count": len(all_replayed_digest_rows),
                "sha256": _canonical_sha256(all_replayed_digest_rows),
            },
            "rows": rows,
        },
        "rigorous_fixed_q_asymptotic": {
            "regime": "fix an odd prime power q and let n tend to infinity through integers, with M=2*n-1 and L=floor(n/2)+1",
            "theorem": "Z_(q,n)/q^M=C0/M+O_q(M^(-2)), hence delta_(q,n)=C0/((1-q^(-1))*M)+O_q(M^(-2))",
            "constant": "C0=1+log(3)+(1/2)*(log(3)^2-log(2)^2)+Li_2(1/3)-Li_2(1/2)",
            "constant_decimal_noncanonical": "2.24583296562735",
            "buchstab_identification": "C0=4*omega(4), the standard rough-polynomial Buchstab constant at M/L tending to 4",
            "direct_proof": [
                "Because 4*L>M, decompose the exact coefficient into one-, two-, and three-factor contributions only.",
                "For fixed q, I_q(d)=q^d/d+O_q(q^(d/2)); since every d>=L=M/4+O(1), all replacement and repeated-factor errors are exponentially small after division by q^M.",
                "The one-factor contribution is 1/M+o(M^-2); the ordered two-factor Riemann sum contributes log(3)/M+O(M^-2).",
                "The ordered three-factor Riemann sum contributes A3/M+O(M^-2), where A3=(1/6)*integral_(x,y,1-x-y>=1/4) dx*dy/(x*y*(1-x-y)).",
                "Elementary integration gives A3=(1/2)*(log(3)^2-log(2)^2)+Li_2(1/3)-Li_2(1/2); division by the exact squarefree count q^M*(1-q^-1) gives the density theorem.",
            ],
            "first_parity_correction": {
                "theorem": "Z_(q,n)/q^M=C0/M+D_eps/M^2+O_q(M^-3), and delta_(q,n)=C0/((1-q^-1)*M)+D_eps/((1-q^-1)*M^2)+O_q(M^-3)",
                "n_even": "D_even=-4*(1+log(2))",
                "n_odd": "D_odd=-(4/3)*(1+log(2))",
                "cutoff_offset": "Writing eta=L-M/4 gives eta=5/4 for even n and eta=3/4 for odd n.",
                "proof": "The two-factor harmonic sum has M^-2 coefficient B_eta=(8-16*eta)/3. Put alpha_M=L/M. Euler--Maclaurin is applied on the actual lattice-aligned triangle D_(alpha_M): its half-boundary coefficient tends to 16*log(2), while expanding the interior integral from alpha_0=1/4 to alpha_M=1/4+eta/M contributes -32*eta*log(2)/M. Boundary variation and corners are O(M^-2) before the outer factor 1/(6*M). Thus the three-factor M^-2 coefficient is B_eta*log(2), D_eps=B_eta*(1+log(2)), the remaining Euler--Maclaurin term is O(M^-3), and the irreducible-count/repetition error is exponentially small.",
                "finite_row_residual_controls_noncanonical": {
                    "definition": "R_(q,n)=M^2*(Z_(q,n)/q^M-C0/M), evaluated from exact stored Z and the displayed decimal C0; values are rounded and are controls, not proof",
                    "n_79_odd": {
                        "target_D_odd": "-2.257529574",
                        "q_3": "-2.253376622",
                        "q_5": "-2.253376619",
                        "q_7": "-2.253376619",
                    },
                    "n_80_even": {
                        "target_D_even": "-6.772588722",
                        "q_3": "-6.664475255",
                        "q_5": "-6.664475254",
                        "q_7": "-6.664475254",
                    },
                },
            },
            "literature_boundary": "The leading C0/M=4*omega(4)/M rough-polynomial law is standard; see Panario--Richmond, Analysis of Ben-Or's polynomial irreducibility test, Random Structures & Algorithms 13 (1998), 439--456, DOI 10.1002/(SICI)1098-2418(199810/12)13:3/4<439::AID-RSA13>3.0.CO;2-U, and Weingartner, On the degrees of polynomial divisors over finite fields, arXiv:1507.01920. The squarefree specialization and explicit parity-sensitive M^-2 refinement are derived here, but no external priority is claimed for the refinement absent a comprehensive literature review.",
            "finite_table_role": "The bounded rows are exact evaluations, not a fit, interpolation proof, or numerical evidence used to justify the asymptotic theorem.",
            "conjectural_extrapolation": None,
        },
        "resource_contract": {
            "q_values": list(REPLAY_QS),
            "minimum_n": MIN_N,
            "maximum_n": MAX_N,
            "maximum_conductor_degree": MAX_M,
            "replayed_rows": replayed_rows,
            "maximum_replay_rows": MAX_REPLAY_ROWS,
            "serialized_n_values": list(SERIALIZED_NS),
            "serialized_rows": len(rows),
            "maximum_serialized_rows": MAX_SERIALIZED_ROWS,
            "irreducible_formula_evaluations": total_formula_evaluations,
            "dp_transitions": total_transitions,
            "maximum_row_dp_transitions_observed": maximum_row_transitions,
            "maximum_row_dp_transitions": MAX_DP_TRANSITIONS_PER_ROW,
            "maximum_total_dp_transitions": MAX_TOTAL_DP_TRANSITIONS,
            "maximum_peak_nonzero_states_observed": maximum_peak_nonzero_states,
            "maximum_local_multiplicity_observed": maximum_local_multiplicity,
            "source_files_read": 1,
            "source_content_reads": 1,
            "source_git_commands": 2,
            "source_bytes_read": SOURCE_BYTES,
            "maximum_source_bytes": MAX_SOURCE_BYTES,
            "maximum_output_bytes": MAX_OUTPUT_BYTES,
            "payload_build_wall_seconds_cap": WALL_SECONDS,
            "wall_clock_semantics": "post-build acceptance ceiling checked after payload construction; not a preemptive process timeout",
            "enumeration_flag_semantics": "recorded code-path ledger authenticated by packet hashes; absence of hidden work also requires source inspection and is not proved by these booleans alone",
            "finite_field_element_enumeration": False,
            "polynomial_enumeration": False,
            "irreducible_enumeration": False,
            "factorization": False,
            "curve_enumeration": False,
            "root_enumeration": False,
            "zero_enumeration": False,
            "sampling": False,
            "floating_point_arithmetic_in_exact_counts": False,
        },
        "claim_boundary": [
            "Every finite numerator, denominator, and density fraction in the table is exact integer arithmetic for the stated monic conductor family.",
            "The support condition is sufficient for the source-locked raw family sum S_(n,Q) to vanish exactly; no converse for all accidental or representation-theoretic cancellations is claimed.",
            "The exact zero is a raw family-sum statement, not a connected-cumulant zero and not a zero of any individual L-function.",
            "The leading fixed-q C0/M term is the standard rough-polynomial/Buchstab law and is not inferred from the finite table. The squarefree specialization and parity-sensitive M^-2 refinement are derived here, with no external priority claim absent a comprehensive literature review.",
            "Conductors are monic squarefree polynomials, not affine-isomorphism classes of curves or a quotient by twists.",
            "No memberwise sign, zero-distribution theorem, number-field transfer, RH, or GRH statement is proved.",
        ],
        "packet_files_lf_sha256": {
            "note": _file_sha256(NOTE),
            "producer": _file_sha256(Path(__file__).resolve()),
            "test": _file_sha256(TEST),
        },
    }
    payload["payload_sha256"] = _canonical_sha256(payload)
    rendered = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()
    if len(rendered) > MAX_OUTPUT_BYTES:
        raise RuntimeError("output-byte cap exceeded")
    if time.monotonic() - started > WALL_SECONDS:
        raise RuntimeError("payload-build wall-clock cap exceeded")
    return payload


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    payload = build_payload()
    rendered = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_bytes() != rendered:
            raise SystemExit("canonical payload drift")
        print(f"verified {OUTPUT}")
    else:
        OUTPUT.write_bytes(rendered)
        print(f"wrote {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
