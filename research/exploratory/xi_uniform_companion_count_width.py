"""Bounded exact controls; the accompanying analytic proof is not machine verified."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import subprocess
from fractions import Fraction
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
STEM = "xi_uniform_companion_count_width"
MANIFEST = HERE / f"{STEM}.sources.json"
FIXTURE = HERE / f"{STEM}.json"
MANIFEST_SHA = "2a211e15a3fff291ca312dbc2991668bb7ad2c745409958f2ed71d07612d0516"
INPUT_BITS = 16
INTERNAL_BITS = 256
MAX_WINDOWS = 8
MAX_RANK = 1024
MAX_FILE_BYTES = 1_000_000
MAX_JSON_BYTES = 200_000
ARTIFACTS = (
    "research/exploratory/XI_UNIFORM_COMPANION_COUNT_WIDTH.md",
    f"research/exploratory/{STEM}.py",
    f"research/exploratory/{STEM}.sources.json",
    f"tests/test_{STEM}.py",
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def integer(value: Any, low: int, high: int) -> int:
    require(type(value) is int, "exact integer required")
    require(low <= value <= high, "integer outside public cap")
    return value


def rational(value: Any, *, internal: bool = False) -> Fraction:
    require(type(value) in (int, Fraction), "exact rational required")
    result = Fraction(value)
    bits = INTERNAL_BITS if internal else INPUT_BITS
    require(
        max(abs(result.numerator).bit_length(), result.denominator.bit_length())
        <= bits,
        "rational bit cap",
    )
    return result


def packed(value: Any) -> list[int]:
    value = rational(value, internal=True)
    return [value.numerator, value.denominator]


def derivative_phase(order: int, side: int) -> tuple[int, int]:
    """Phase multiplying a positive cosh/even or sinh/odd integral at side*i."""
    order = integer(order, 0, 6)
    side = integer(side, -1, 1)
    require(side != 0, "side must be +1 or -1")
    phase = ((1, 0), (0, 1), (-1, 0), (0, -1))[order % 4]
    factor = -side if order % 2 else 1
    return (factor * phase[0], factor * phase[1])


def anchor_control(order: int, sign: int, side: int) -> dict[str, Any]:
    order = integer(order, 0, 5)
    sign = integer(sign, -1, 1)
    require(sign != 0, "companion sign must be +1 or -1")
    base = derivative_phase(order, side)
    derivative = derivative_phase(order + 1, side)
    slope = (-sign * derivative[1], sign * derivative[0])
    require(base == slope or base == (-slope[0], -slope[1]), "phase algebra")
    return {
        "order": order,
        "sign": sign,
        "side": side,
        "base_phase": list(base),
        "lambda_phase": list(slope),
        "noncancelling": base == slope,
    }


def growth_control(radius: Any, order: int) -> dict[str, Any]:
    radius = rational(radius)
    require(radius >= 1, "growth radius must be at least one")
    order = integer(order, 0, 6)
    fact = math.factorial(order)
    require(Fraction(fact, math.factorial(order)) == 1, "Taylor coefficient witness")
    return {
        "radius": packed(radius),
        "derivative": order,
        "factorial": fact,
        "exp_series_coefficient": packed(Fraction(1, fact)),
        "gamma_parameter": packed(radius / 2 + Fraction(11, 4)),
        "coefficient_of_pi_squared": 6 * fact,
        "full_line_then_substitution_factor": packed(Fraction(2, 2)),
    }


def jensen_geometry(radius: Any, side: int) -> dict[str, Any]:
    radius = rational(radius)
    require(radius >= 1, "Jensen radius must be at least one")
    side = integer(side, -1, 1)
    require(side != 0, "Jensen center must be +i or -i")
    inner = radius + abs(side)
    outer = 2 * inner
    envelope = outer + abs(side)
    require(inner >= radius + 1 and outer / inner == 2, "disk containment")
    require(envelope == 2 * radius + 3, "shifted outer disk")
    gamma = envelope / 2 + Fraction(11, 4)
    require(gamma == radius + Fraction(17, 4), "shifted Gamma parameter")
    return {
        "radius": packed(radius),
        "center_imaginary": side,
        "inner_radius": packed(inner),
        "outer_radius": packed(outer),
        "origin_envelope_radius": packed(envelope),
        "jensen_ratio": packed(outer / inner),
        "outer_gamma_parameter": packed(gamma),
    }


def scale_control(omega: Any) -> dict[str, Any]:
    omega = rational(omega)
    require(omega >= 1, "omega must be at least one")
    lam, frequency = 1 / omega, 2 * omega
    require(0 < lam <= 1 and lam * frequency / 2 == 1, "fixed scale matching")
    return {
        "omega": packed(omega),
        "lambda": packed(lam),
        "X": packed(frequency),
        "lambda_X_over_two": [1, 1],
    }


def width_constant(order: int, bound: Any, t: Any, ell: Any, pi_symbol: Any) -> dict:
    order = integer(order, 1, 31)
    require(order % 2 == 1, "fixed odd source order required")
    bound, t, ell, pi_symbol = map(rational, (bound, t, ell, pi_symbol))
    require(min(bound, ell, pi_symbol) > 0 and t >= 1, "positive scale required")
    before = rational(
        order * bound / pi_symbol * (2 * pi_symbol / t) / ell, internal=True
    )
    after = rational(2 * order * bound / (t * ell), internal=True)
    require(before == after, "symbolic pi cancellation")
    return {
        "K": order,
        "M": packed(bound),
        "t": packed(t),
        "ell": packed(ell),
        "formal_pi": packed(pi_symbol),
        "before": packed(before),
        "after": packed(after),
    }


def squared_width_control(
    windows: Any, width: Any, normalizer: Any, eta: Any
) -> dict[str, Any]:
    require(type(windows) in (list, tuple), "window sequence required")
    require(len(windows) <= MAX_WINDOWS, "window count cap")
    width, normalizer, eta = map(rational, (width, normalizer, eta))
    require(width >= 0 and normalizer > 0 and eta > 0, "invalid width scales")
    rows = []
    for row in windows:
        require(type(row) in (list, tuple) and len(row) == 2, "window row shape")
        rank = integer(row[0], 0, MAX_RANK)
        height = rational(row[1])
        require(0 <= height <= eta * rank, "shallow-height condition")
        rows.append((rank, height))
    rank = sum(row[0] for row in rows)
    height = rational(sum((row[1] for row in rows), Fraction()), internal=True)
    coarse = rational(16 * width * rank * height / normalizer**2, internal=True)
    shallow = rational(16 * width * eta * rank**2 / normalizer**2, internal=True)
    require(0 <= coarse <= shallow, "squared shallow inequality")
    return {
        "windows": [[n, packed(s)] for n, s in rows],
        "width": packed(width),
        "normalizer": packed(normalizer),
        "eta": packed(eta),
        "rank_total": rank,
        "height_total": packed(height),
        "coarse_normalized_square": packed(coarse),
        "shallow_normalized_square": packed(shallow),
        "gap": packed(shallow - coarse),
    }


def cauchy_control(left: Any, right: Any) -> dict[str, Any]:
    require(
        type(left) in (list, tuple) and type(right) in (list, tuple), "vectors required"
    )
    require(len(left) == len(right) <= MAX_WINDOWS, "vector dimension cap")
    left, right = [rational(x) for x in left], [rational(x) for x in right]
    dot = rational(sum((a * b for a, b in zip(left, right)), Fraction()), internal=True)
    square_left = sum((a * a for a in left), Fraction())
    square_right = sum((b * b for b in right), Fraction())
    gap = rational(square_left * square_right - dot**2, internal=True)
    require(gap >= 0, "Cauchy-Schwarz finite control")
    return {
        "left": [packed(x) for x in left],
        "right": [packed(x) for x in right],
        "dot_squared": packed(dot**2),
        "norm_product": packed(square_left * square_right),
        "gap": packed(gap),
    }


def cosine_control(lam: Any) -> dict[str, Any]:
    lam = rational(lam)
    require(0 < lam < 1, "cosine lambda must be between zero and one")
    # Real multipliers of i in q^-2, q^0, q^2 for D=H0*H5, q=exp(i*z).
    h0 = [(1 + lam) / 2, (1 - lam) / 2]
    h5_over_i = [(lam - 1) / 2, (1 + lam) / 2]
    product = [
        h0[0] * h5_over_i[0],
        h0[0] * h5_over_i[1] + h0[1] * h5_over_i[0],
        h0[1] * h5_over_i[1],
    ]
    expected = [-(1 - lam**2) / 4, lam, (1 - lam**2) / 4]
    require(product == expected, "cosine Laurent factorization")
    upper_q2 = (1 - lam) / (1 + lam)
    lower_q2 = -(1 + lam) / (1 - lam)
    require(0 < upper_q2 < 1 and lower_q2 < -1, "upper/lower zero classification")
    return {
        "lambda": packed(lam),
        "D_over_i_laurent_minus2_0_2": [packed(x) for x in product],
        "upper_q_squared": packed(upper_q2),
        "lower_q_squared": packed(lower_q2),
        "height_upper_bound": packed(lam / (1 - lam**2)),
        "scope": "cosine atomic source, not Xi; entire shallow denominator is infinite",
    }


def lf_bytes(raw: bytes) -> bytes:
    require(type(raw) is bytes, "bytes required")
    require(len(raw) <= MAX_FILE_BYTES, "file size cap")
    raw.decode("utf-8")
    return raw.replace(b"\r\n", b"\n")


def file_bytes(path: Path) -> bytes:
    require(path.stat().st_size <= MAX_FILE_BYTES, "file size cap")
    return lf_bytes(path.read_bytes())


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _pairs_unique(pairs: list[tuple[str, Any]]) -> dict:
    result = {}
    for key, value in pairs:
        require(key not in result, "duplicate JSON key")
        result[key] = value
    return result


def _nonfinite(value: str) -> None:
    raise ValueError(f"nonfinite JSON: {value}")


def _json_types(value: Any, depth: int = 0) -> None:
    require(depth <= 12, "JSON depth cap")
    require(type(value) in (dict, list, str, int, bool, type(None)), "JSON scalar type")
    if type(value) is dict:
        require(len(value) <= 200, "JSON object cap")
        for key, child in value.items():
            require(type(key) is str and len(key) <= 2048, "JSON key cap")
            _json_types(child, depth + 1)
    elif type(value) is list:
        require(len(value) <= 2000, "JSON array cap")
        for child in value:
            _json_types(child, depth + 1)
    elif type(value) is str:
        require(len(value) <= 2048, "JSON string cap")
    elif type(value) is int:
        require(abs(value).bit_length() <= INTERNAL_BITS, "JSON integer cap")


def parse_json(raw: bytes) -> Any:
    require(type(raw) is bytes and len(raw) <= MAX_JSON_BYTES, "JSON byte cap")
    try:
        value = json.loads(
            raw, object_pairs_hook=_pairs_unique, parse_constant=_nonfinite
        )
        _json_types(value)
        return value
    except (UnicodeError, RecursionError, json.JSONDecodeError) as exc:
        raise ValueError("invalid bounded JSON") from exc


def canonical(value: Any) -> bytes:
    _json_types(value)
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), allow_nan=False
    ).encode()


def authenticate_sources(manifest_raw: bytes | None = None) -> dict:
    raw = file_bytes(MANIFEST) if manifest_raw is None else lf_bytes(manifest_raw)
    require(digest(raw) == MANIFEST_SHA, "frozen manifest identity")
    manifest = parse_json(raw)
    sources = manifest["sources"]
    require(
        type(sources) is list and len(sources) == 10, "complete ten-source contract"
    )
    for source in sources:
        spec = f"{source['commit']}:{source['path']}"
        result = subprocess.run(
            ["git", "show", spec], cwd=ROOT, check=True, capture_output=True, timeout=30
        ).stdout
        require(len(result) <= MAX_FILE_BYTES, "source size cap")
        header = f"blob {len(result)}\0".encode()
        require(
            hashlib.sha1(header + result).hexdigest() == source["git_blob"], "Git blob"
        )
        require(digest(lf_bytes(result)) == source["sha256_lf"], "source LF hash")
    return manifest


def build_report() -> dict[str, Any]:
    manifest = authenticate_sources()
    growth = [growth_control(radius, r) for radius in (1, 4, 16) for r in range(7)]
    geometry = [
        jensen_geometry(radius, side) for radius in (1, 2, 16, 256) for side in (-1, 1)
    ]
    anchors = [
        anchor_control(r, sign, side)
        for r in (0, 5)
        for sign in (-1, 1)
        for side in (-1, 1)
    ]
    for r, sign, side in ((0, 1, 1), (5, -1, -1)):
        require(anchor_control(r, sign, side)["noncancelling"], "native anchor")
    phases = [
        {"order": r, "side": side, "phase": list(derivative_phase(r, side))}
        for r in range(7)
        for side in (-1, 1)
    ]
    scales = [scale_control(x) for x in (1, Fraction(3, 2), 5, 32)]
    widths = [
        width_constant(k, m, 1024, 8, Fraction(22, 7))
        for k in (1, 5, 31)
        for m in (Fraction(1, 2), 1, 2)
    ]
    panels = [
        squared_width_control([], 0, 1, Fraction(1, 100)),
        squared_width_control(
            [(1, Fraction(1, 200))], Fraction(1, 1024), 10, Fraction(1, 100)
        ),
        squared_width_control(
            [(4, Fraction(1, 100)), (9, Fraction(1, 25))],
            Fraction(1, 4096),
            100,
            Fraction(1, 100),
        ),
        squared_width_control(
            [(1024, 10)] * 8, Fraction(1, 65535), 8192, Fraction(1, 100)
        ),
    ]
    cauchy = [
        cauchy_control([], []),
        cauchy_control([1, 2, 3], [Fraction(1, 10), Fraction(1, 5), Fraction(3, 10)]),
        cauchy_control([2, 3], [Fraction(1, 10), Fraction(1, 5)]),
    ]
    cosine = [
        cosine_control(x) for x in (Fraction(1, 200), Fraction(1, 201), Fraction(1, 2))
    ]
    require(
        Fraction(*cosine[0]["height_upper_bound"]) < Fraction(1, 100),
        "shallow cosine control",
    )
    return {
        "schema": "xi-uniform-companion-count-width-controls-v1",
        "scope": "bounded algebra/source replay; analytic proof and native cofinal capture not machine verified",
        "manifest_sha256_lf": MANIFEST_SHA,
        "source_bindings": manifest["sources"],
        "artifacts_sha256_lf": {
            path: digest(file_bytes(ROOT / path)) for path in ARTIFACTS
        },
        "caps": {
            "derivative_order": 6,
            "source_order": 31,
            "windows": MAX_WINDOWS,
            "rank_per_window": MAX_RANK,
            "input_bits": INPUT_BITS,
            "internal_bits": INTERNAL_BITS,
            "file_bytes": MAX_FILE_BYTES,
            "json_bytes": MAX_JSON_BYTES,
        },
        "counts": {
            "growth": len(growth),
            "geometry": len(geometry),
            "anchors": len(anchors),
            "phases": len(phases),
            "scales": len(scales),
            "widths": len(widths),
            "squared_width": len(panels),
            "cauchy": len(cauchy),
            "cosine": len(cosine),
        },
        "growth": growth,
        "geometry": geometry,
        "anchors": anchors,
        "phases": phases,
        "scales": scales,
        "widths": widths,
        "squared_width": panels,
        "cauchy": cauchy,
        "cosine": cosine,
    }


def check_fixture(raw: bytes | None = None) -> dict[str, Any]:
    raw = file_bytes(FIXTURE) if raw is None else raw
    supplied = parse_json(raw)
    rebuilt = build_report()
    require(
        canonical(supplied) == canonical(rebuilt), "complete canonical fixture mismatch"
    )
    return rebuilt


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--check", action="store_true")
    group.add_argument(
        "--emit", action="store_true", help="print rebuilt JSON; never writes files"
    )
    args = parser.parse_args()
    if args.check:
        report = check_fixture()
        print(
            json.dumps(
                {"status": "PASS bounded exact controls", "counts": report["counts"]},
                sort_keys=True,
            )
        )
    else:
        print(json.dumps(build_report(), sort_keys=True, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
