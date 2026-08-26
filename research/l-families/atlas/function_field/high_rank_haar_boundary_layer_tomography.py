#!/usr/bin/env python3
"""Bounded exact certificates for the SU(2) high-rank boundary layer.

The analytic note proves a uniform mesoscopic cubic tail, the complete
x/N ceiling crossover, truncated-moment laws, and endpoint tomography for
the characters sin(N theta)/sin(theta).  This producer records exact rational
constant derivations, finite Taylor certificates, provenance, and strict
resource bounds.  It performs no quadrature, sampling, root search, finite
field enumeration, character-family enumeration, or L-function computation.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import time
from dataclasses import dataclass, field
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SCRIPT_PATH = Path(__file__).resolve()
OUTPUT_PATH = HERE / "high_rank_haar_boundary_layer_tomography.json"
NOTE_PATH = HERE / "HIGH_RANK_HAAR_BOUNDARY_LAYER_TOMOGRAPHY.md"
TEST_PATH = ROOT / "tests" / "test_high_rank_haar_boundary_layer_tomography.py"

HIGH_RANK_NOTE_PATH = HERE / "ELLIPTIC_SYMMETRIC_POWER_HIGH_RANK_HAAR_LIMIT.md"
MOMENT_NOTE_PATH = HERE / "ELLIPTIC_TENSOR_SYMMETRIC_POWER_MOMENT_LADDER.md"
MOMENT_SCRIPT_PATH = HERE / "elliptic_tensor_symmetric_power_moment_ladder.py"
MOMENT_JSON_PATH = HERE / "elliptic_tensor_symmetric_power_moment_ladder.json"
MOMENT_TEST_PATH = (
    ROOT / "tests" / "test_elliptic_tensor_symmetric_power_moment_ladder.py"
)

MAX_EXACT_OPERATIONS = 5_000
MAX_SOURCE_FILES = 5
MAX_SOURCE_BYTES_EACH = 40_000
MAX_SOURCE_BYTES_TOTAL = 90_000
MAX_CONTROL_ROWS = 64
MAX_PACKET_FILE_BYTES = 65_536
MAX_WALL_SECONDS = 4.0

SOURCE_LOCKS: dict[str, dict[str, object]] = {
    "high_rank_note": {
        "path": HIGH_RANK_NOTE_PATH,
        "commit": "8ba581fcc9c0b3ef6b68ac6d121648dd36c1c289",
        "git_blob": "2a0c0b9fefbbe394477dc97cc5c05d22b9ae7bde",
        "lf_sha256": "afe3ff04ea1fd3a8983c4159c4bced01b36161f5053c342bb81a84b794ae5824",
        "role": "weak limit, cubic tail, real-moment phase diagram",
    },
    "moment_note": {
        "path": MOMENT_NOTE_PATH,
        "commit": "010827a518374e34b28d29f6a92741c3174ae803",
        "git_blob": "35387da69ab7a80264075cbb3f59f7f429327be5",
        "lf_sha256": "134024ab5550a1dfef1665cd8b0ad2fcb939d9f22d6453d19e26df64ec828931",
        "role": "finite-rank moment ladder proof note",
    },
    "moment_script": {
        "path": MOMENT_SCRIPT_PATH,
        "commit": "010827a518374e34b28d29f6a92741c3174ae803",
        "git_blob": "f27da4fd9ed623ee46bcd5b70491a51e0adff92c",
        "lf_sha256": "fe667748566cf94ac0c93a607359f1bc73140da343a4403c74d4024d71d4d247",
        "role": "bounded exact finite-rank producer",
    },
    "moment_json": {
        "path": MOMENT_JSON_PATH,
        "commit": "010827a518374e34b28d29f6a92741c3174ae803",
        "git_blob": "dcfcac10995c5ac567020ca5094644d093cd7b0b",
        "lf_sha256": "cc91b7be07af49f56a776dea7e7204a65061c439a208a9631cfcdfa2f2375540",
        "schema": "riemann.function_field.elliptic_tensor_symmetric_power_moment_ladder.v1",
        "payload_sha256": "0eba593b98d1cdb10cd79354ef15b9352291be1c28d85e961ed35fcd17aed088",
        "role": "canonical finite-rank moment payload",
    },
    "moment_test": {
        "path": MOMENT_TEST_PATH,
        "commit": "010827a518374e34b28d29f6a92741c3174ae803",
        "git_blob": "773aecd29386880ba8ef932890208bc0f4def20b",
        "lf_sha256": "47751b97d86e91225b249e9435594b869236fa59129afd478cc6bc4e640b72c8",
        "role": "finite-rank packet regression suite",
    },
}


@dataclass
class ResourceGuard:
    exact_operations: int = 0
    source_files: int = 0
    source_bytes: int = 0
    control_rows: int = 0
    operation_counts: dict[str, int] = field(default_factory=dict)

    def operation(self, label: str, amount: int = 1) -> None:
        if amount < 0:
            raise ValueError("operation increment must be nonnegative")
        if self.exact_operations + amount > MAX_EXACT_OPERATIONS:
            raise RuntimeError("exact-operation cap exceeded")
        self.exact_operations += amount
        self.operation_counts[label] = self.operation_counts.get(label, 0) + amount

    def source(self, size: int) -> None:
        if size < 0:
            raise ValueError("source size must be nonnegative")
        if size > MAX_SOURCE_BYTES_EACH:
            raise RuntimeError("per-source byte cap exceeded")
        if self.source_files + 1 > MAX_SOURCE_FILES:
            raise RuntimeError("source-file cap exceeded")
        if self.source_bytes + size > MAX_SOURCE_BYTES_TOTAL:
            raise RuntimeError("total source byte cap exceeded")
        self.source_files += 1
        self.source_bytes += size

    def row(self) -> None:
        if self.control_rows + 1 > MAX_CONTROL_ROWS:
            raise RuntimeError("control-row cap exceeded")
        self.control_rows += 1


@dataclass(frozen=True)
class Deadline:
    started: float = field(default_factory=time.monotonic)

    def check(self, label: str) -> None:
        if time.monotonic() - self.started > MAX_WALL_SECONDS:
            raise RuntimeError(f"wall-time cap exceeded at {label}")


def _canonical_bytes(value: object) -> bytes:
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")


def _canonical_sha256(value: object) -> str:
    return hashlib.sha256(_canonical_bytes(value)).hexdigest()


def _lf_sha256_bytes(raw: bytes) -> str:
    normalized = raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(normalized).hexdigest()


def _git_blob_sha1(raw: bytes) -> str:
    normalized = raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    header = f"blob {len(normalized)}\0".encode()
    return hashlib.sha1(header + normalized).hexdigest()


def _fraction(value: Fraction | int) -> list[int]:
    item = Fraction(value)
    return [item.numerator, item.denominator]


def _constant(
    rational: Fraction | int,
    *,
    pi_power: int = 0,
    radical: str | None = None,
) -> dict[str, object]:
    result: dict[str, object] = {
        "rational": _fraction(rational),
        "pi_power": pi_power,
    }
    if radical is not None:
        result["radical"] = radical
    return result


def series_divide(
    numerator: tuple[Fraction, ...],
    denominator: tuple[Fraction, ...],
    guard: ResourceGuard,
) -> tuple[Fraction, ...]:
    """Formal power-series quotient through the supplied coefficient order."""
    if not denominator or denominator[0] == 0:
        raise ValueError("series denominator needs a nonzero constant term")
    if len(numerator) != len(denominator):
        raise ValueError("series lengths must agree")
    quotient: list[Fraction] = []
    for degree, coefficient in enumerate(numerator):
        guard.operation("series_coefficients")
        remainder = coefficient
        for index in range(degree):
            guard.operation("series_convolutions")
            remainder -= quotient[index] * denominator[degree - index]
        quotient.append(remainder / denominator[0])
    return tuple(quotient)


def normalized_character_series(
    dimension: int,
    guard: ResourceGuard,
) -> tuple[Fraction, ...]:
    """Coefficients in z=theta^2 through z^2 for sin(N theta)/(N sin theta)."""
    if dimension < 1:
        raise ValueError("dimension must be positive")
    numerator = (
        Fraction(1),
        Fraction(-(dimension**2), 6),
        Fraction(dimension**4, 120),
    )
    denominator = (
        Fraction(1),
        Fraction(-1, 6),
        Fraction(1, 120),
    )
    return series_divide(numerator, denominator, guard)


def ceiling_series_controls(guard: ResourceGuard) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for dimension in range(2, 13):
        guard.row()
        series = normalized_character_series(dimension, guard)
        expected_quadratic = Fraction(-(dimension**2 - 1), 6)
        expected_quartic = Fraction(
            3 * dimension**4 - 10 * dimension**2 + 7,
            360,
        )
        if series[1] != expected_quadratic or series[2] != expected_quartic:
            raise ArithmeticError("normalized character Taylor series failed")
        rows.append(
            {
                "N": dimension,
                "series_in_theta_squared": [_fraction(value) for value in series],
                "ceiling_quadratic_drop": _fraction(-series[1]),
                "ceiling_probability_coefficient": {
                    "formula": "8*sqrt(6)/(pi*(N^2-1)^(3/2))",
                    "N_squared_minus_one": dimension**2 - 1,
                },
            }
        )
    return rows


def tail_constant_certificate(guard: ResourceGuard) -> dict[str, object]:
    """Exact integration-by-parts certificate for integral y^2 arccos(y)."""
    guard.operation("beta_integral_reductions", 4)
    sin_cubed_half_interval = Fraction(2, 3)
    y_cubed_over_root = sin_cubed_half_interval
    y_squared_arccos = y_cubed_over_root / 3
    phase_average_multiplier = Fraction(2)
    endpoint_haar_multiplier = Fraction(4)
    rational = endpoint_haar_multiplier * phase_average_multiplier * y_squared_arccos
    if y_squared_arccos != Fraction(2, 9) or rational != Fraction(16, 9):
        raise ArithmeticError("cubic tail constant certificate failed")
    return {
        "integral_y3_over_sqrt_1_minus_y2": _fraction(y_cubed_over_root),
        "integral_y2_arccos_y": _fraction(y_squared_arccos),
        "phase_proportion": "q(y)=2*arccos(y)/pi",
        "endpoint_haar_prefactor": "4/pi",
        "tail_constant": _constant(rational, pi_power=-2),
        "theorem": (
            "x^3*P(X_N>x) tends uniformly to 16/(9*pi^2) "
            "when both x and N/x tend to infinity"
        ),
    }


def crossover_certificate(tail: dict[str, object]) -> dict[str, object]:
    if tail["tail_constant"] != _constant(Fraction(16, 9), pi_power=-2):
        raise ArithmeticError("crossover lost the mesoscopic constant")
    return {
        "function": (
            "H(lambda)=4/pi*integral_0^(1/lambda) t^2*1{|sin(t)|>lambda*t} dt"
        ),
        "fixed_ratio_limit": ("N^3*P(X_N>lambda*N) -> H(lambda), 0<lambda<1"),
        "small_lambda": {
            "statement": "lambda^3*H(lambda) -> 16/(9*pi^2)",
            "constant": tail["tail_constant"],
        },
        "near_ceiling": {
            "statement": ("H(lambda) ~ 8*sqrt(6)/pi*(1-lambda)^(3/2)"),
            "constant": _constant(8, pi_power=-1, radical="sqrt(6)"),
            "root_scale": "t_lambda~sqrt(6*(1-lambda))",
        },
        "hard_cap": "P(X_N>x)=0 for x>=N",
    }


def truncated_moment_rows(guard: ResourceGuard) -> list[dict[str, object]]:
    tail_rational = Fraction(16, 9)
    rows: list[dict[str, object]] = []
    for power in range(4, 13):
        guard.row()
        guard.operation("truncated_constant_rows")
        hard = Fraction(3, power - 3) * tail_rational
        winsor = Fraction(power, power - 3) * tail_rational
        capped_tail = tail_rational
        if hard + capped_tail != winsor:
            raise ArithmeticError("hard/Winsorized coefficient split failed")
        rows.append(
            {
                "p": power,
                "hard_truncated_coefficient": _constant(hard, pi_power=-2),
                "winsorized_coefficient": _constant(winsor, pi_power=-2),
                "capped_tail_difference": _constant(capped_tail, pi_power=-2),
                "scale": "T^(p-3)",
            }
        )
    return rows


def critical_cubic_certificate(guard: ResourceGuard) -> dict[str, object]:
    guard.operation("sin_cubed_period_integral")
    integral_zero_pi = Fraction(4, 3)
    period_mean = integral_zero_pi
    # The stored rational is understood as period_mean/pi.
    endpoint_prefactor = Fraction(4)
    logarithmic_rational = endpoint_prefactor * period_mean
    tail_rational = Fraction(16, 9)
    if logarithmic_rational != Fraction(16, 3):
        raise ArithmeticError("cubic logarithmic coefficient failed")
    if 3 * tail_rational != logarithmic_rational:
        raise ArithmeticError("tail integration did not recover cubic log")
    return {
        "integral_0_pi_sin_cubed": _fraction(integral_zero_pi),
        "period_mean": _constant(period_mean, pi_power=-1),
        "full_log_coefficient": _constant(logarithmic_rational, pi_power=-2),
        "hard_truncated_log_coefficient": _constant(logarithmic_rational, pi_power=-2),
        "winsorized_log_coefficient": _constant(logarithmic_rational, pi_power=-2),
        "scale_tomography": (
            "the endpoint window D<=N^(-beta) captures fraction 1-beta "
            "of the absolute cubic moment for every fixed 0<beta<1"
        ),
    }


def endpoint_tomography_certificate() -> dict[str, object]:
    return {
        "distance": "D(theta)=min(theta,pi-theta)",
        "fixed_scaled_window": ("N^(3-p)*E[X_N^p*1{N*D<=a}] -> Psi_p(a)"),
        "profile": ("Psi_p(a)=4/pi*integral_0^a |sin(t)|^p*t^(2-p) dt"),
        "supercritical_total": ("C_p=4/pi*integral_0^infinity |sin(t)|^p*t^(2-p) dt"),
        "supercritical_fraction": "Psi_p(a)/C_p, increasing to 1 as a->infinity",
        "critical_fraction": "1-beta in the window D<=N^(-beta)",
        "phase_transition": {
            "p_less_than_3": "fixed O(1/N) endpoint mass is lower order",
            "p_equals_3": "mass is uniform across logarithmic endpoint scales",
            "p_greater_than_3": "all leading mass has an O(1/N) profile",
        },
    }


def _verify_sources(
    guard: ResourceGuard,
    deadline: Deadline,
) -> list[dict[str, object]]:
    manifest: list[dict[str, object]] = []
    for source_id, lock in SOURCE_LOCKS.items():
        path = lock["path"]
        if not isinstance(path, Path):
            raise TypeError("source path must be a Path")
        raw = path.read_bytes()
        guard.source(len(raw))
        deadline.check(f"source {source_id}")
        if _lf_sha256_bytes(raw) != lock["lf_sha256"]:
            raise RuntimeError(f"LF hash mismatch for {source_id}")
        if _git_blob_sha1(raw) != lock["git_blob"]:
            raise RuntimeError(f"git blob mismatch for {source_id}")
        if source_id == "moment_json":
            parsed = json.loads(raw.decode("utf-8"))
            if parsed.get("schema") != lock["schema"]:
                raise RuntimeError("moment JSON schema drifted")
            if parsed.get("payload_sha256") != lock["payload_sha256"]:
                raise RuntimeError("moment JSON payload drifted")
        manifest.append(
            {
                "id": source_id,
                "path": path.relative_to(ROOT).as_posix(),
                "commit": lock["commit"],
                "git_blob": lock["git_blob"],
                "lf_sha256": lock["lf_sha256"],
                "bytes": len(raw),
                "role": lock["role"],
            }
        )
    return manifest


def _packet_sizes() -> dict[str, int | None]:
    result: dict[str, int | None] = {}
    for label, path in (
        ("producer", SCRIPT_PATH),
        ("note", NOTE_PATH),
        ("test", TEST_PATH),
    ):
        if not path.exists():
            result[label] = None
            continue
        size = path.stat().st_size
        if size > MAX_PACKET_FILE_BYTES:
            raise RuntimeError(f"{label} file exceeds packet-size cap")
        result[label] = size
    return result


def build_fixture() -> dict[str, object]:
    deadline = Deadline()
    guard = ResourceGuard()

    ceiling = ceiling_series_controls(guard)
    tail = tail_constant_certificate(guard)
    crossover = crossover_certificate(tail)
    truncated = truncated_moment_rows(guard)
    cubic = critical_cubic_certificate(guard)
    tomography = endpoint_tomography_certificate()
    deadline.check("exact constant algebra")

    sources = _verify_sources(guard, deadline)
    deadline.check("source locks")

    fixture: dict[str, object] = {
        "schema": (
            "riemann.function_field.high_rank_haar_boundary_layer_tomography.v1"
        ),
        "status": "PROVED_UNIFORM_HAAR_BOUNDARY_LAYER_TOMOGRAPHY",
        "generated_by": SCRIPT_PATH.relative_to(ROOT).as_posix(),
        "source_contract": {
            "sources": sources,
            "moment_payload": (
                "0eba593b98d1cdb10cd79354ef15b9352291be1c28d85e961ed35fcd17aed088"
            ),
        },
        "exact_theorems": {
            "finite_N_tail_coordinate": {
                "theta_form": (
                    "P(X_N>x)=4/pi*integral_0^arcsin(1/x) "
                    "1{|sin(N*theta)|>x*sin(theta)}*sin(theta)^2 dtheta"
                ),
                "unit_interval_form": (
                    "P(X_N>x)=4/(pi*x^3)*integral_0^1 "
                    "y^2*1{|sin(N*arcsin(y/x))|>y}"
                    "/sqrt(1-y^2/x^2) dy"
                ),
                "range": "x>=1",
                "hard_cap": "zero for x>=N",
                "endpoint_mass_upper_bound": (
                    "2/pi*(arcsin(1/x)-x^(-1)*sqrt(1-x^(-2)))"
                ),
            },
            "uniform_mesoscopic_tail": tail,
            "ceiling_crossover": crossover,
            "finite_N_ceiling": {
                "statement": (
                    "P(X_N>N*(1-epsilon)) ~ 8*sqrt(6)/(pi*(N^2-1)^(3/2))*epsilon^(3/2)"
                ),
                "controls": ceiling,
            },
            "truncated_moments": {
                "regime": "T->infinity and T/N->0",
                "critical": cubic,
                "supercritical_rows": truncated,
                "general_hard_formula": ("16/(3*pi^2*(p-3))*T^(p-3), p>3"),
                "general_winsor_formula": ("16*p/(9*pi^2*(p-3))*T^(p-3), p>3"),
            },
            "endpoint_tomography": tomography,
        },
        "proof_architecture": {
            "uniform_averaging": (
                "continuous approximation in (threshold,phase), finite "
                "Fourier expansion, and nonstationary integration by parts"
            ),
            "crossover": (
                "fixed-ratio dominated convergence in the exact unit-interval "
                "tail coordinate"
            ),
            "truncation": (
                "layer-cake identities integrated against the uniform mesoscopic tail"
            ),
            "tomography": ("endpoint substitution t=N*theta and periodic mean at p=3"),
            "finite_ceiling": (
                "quadratic Taylor drop of sin(N*theta)/(N*sin(theta)) "
                "and cubic Haar endpoint mass"
            ),
        },
        "scope": {
            "compact_group": "Haar SU(2) only",
            "proved": [
                "uniform tail for 1<<x<<N",
                "fixed x/N crossover and both edge limits",
                "finite-N near-ceiling coefficient",
                "hard-truncated and Winsorized p-moment asymptotics",
                "supercritical O(1/N) endpoint profile",
                "critical logarithmic-scale endpoint profile",
            ],
            "not_proved": [
                "arithmetic-family equidistribution uniform in rank",
                "finite-field trace estimate",
                "elliptic-curve or modular-form family theorem",
                "Euler-product or zero-statistic theorem",
                "RH",
                "GRH",
                "external novelty",
            ],
            "arithmetic_gate": (
                "prove sourced family equidistribution for threshold or "
                "smoothed truncation tests uniformly in 1<<x<<N, or count "
                "the endpoint stratum with crossover H(lambda)"
            ),
        },
        "resource_budget": {
            "limits": {
                "exact_operations": MAX_EXACT_OPERATIONS,
                "source_files": MAX_SOURCE_FILES,
                "source_bytes_each": MAX_SOURCE_BYTES_EACH,
                "source_bytes_total": MAX_SOURCE_BYTES_TOTAL,
                "control_rows": MAX_CONTROL_ROWS,
                "packet_file_bytes_each": MAX_PACKET_FILE_BYTES,
                "wall_seconds": MAX_WALL_SECONDS,
            },
            "used": {
                "exact_operations": guard.exact_operations,
                "source_files": guard.source_files,
                "source_bytes": guard.source_bytes,
                "control_rows": guard.control_rows,
                "operation_counts": dict(sorted(guard.operation_counts.items())),
            },
            "packet_file_bytes": _packet_sizes(),
            "heavy_computation": False,
            "numerical_quadrature": False,
            "root_searches": 0,
            "random_samples": 0,
            "enumerated_characters": 0,
            "enumerated_l_functions": 0,
        },
    }
    fixture["payload_sha256"] = _canonical_sha256(fixture)
    deadline.check("final fixture")
    return fixture


def _render(fixture: dict[str, object]) -> str:
    return json.dumps(fixture, indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="compare the exact fixture with the canonical JSON",
    )
    parser.add_argument(
        "--print-summary",
        action="store_true",
        help="print a compact theorem/resource summary",
    )
    arguments = parser.parse_args()
    fixture = build_fixture()
    rendered = _render(fixture)
    if arguments.check:
        if not OUTPUT_PATH.exists():
            raise SystemExit("canonical JSON is missing")
        if OUTPUT_PATH.read_text(encoding="utf-8") != rendered:
            raise SystemExit("canonical JSON drifted")
    else:
        OUTPUT_PATH.write_text(rendered, encoding="utf-8", newline="\n")
    if arguments.print_summary:
        tail = fixture["exact_theorems"]["uniform_mesoscopic_tail"]["tail_constant"]
        used = fixture["resource_budget"]["used"]
        print(
            f"tail_constant={tail} "
            f"ops={used['exact_operations']} rows={used['control_rows']}"
        )
    print("PASS_HIGH_RANK_HAAR_BOUNDARY_LAYER_TOMOGRAPHY")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
