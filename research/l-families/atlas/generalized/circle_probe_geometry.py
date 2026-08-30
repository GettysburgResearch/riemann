"""Exact bounded controls for circle-probe degeneracy and its held-out test.

The nonrational cases specialize the separately proved residue theorem;
finite samples do not establish nonrationality or a natural boundary.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
STEM = "circle_probe_geometry"
NOTE = HERE / "CIRCLE_PROBE_GEOMETRY.md"
MANIFEST = HERE / (STEM + ".sources.json")
FIXTURE = HERE / (STEM + ".json")
TEST = ROOT / "tests" / ("test_" + STEM + ".py")
BASE = "8834fdc7a0dfe15f6bb95eefe0729cb77c93c807"
SOURCE_ROWS = (
    (
        "research/l-families/atlas/generalized/MULTIPLICATIVE_RECURRENCE_AND_MIXED_PARENTS.md",
        "e34fa2ba38981f37109d6f734c03a67a240e02f3",
        "bcd7ae6890bad68b9b52f896f59cd305edbb7b3d5a5d4f32210e0afef1135b2f",
    ),
    (
        "research/l-families/atlas/generalized/multiplicative_recurrence_mixed_parents.py",
        "1601a04b0167039470c5b3b8bcade3f86d7aa162",
        "8ea27b6b3a18bb124ccc3016fab0f7d62df324cda527774e5282bc8227030290",
    ),
)
MAX_DEGREE = 6
MAX_WEIGHT = 32
G = tuple[Fraction, Fraction]


def need(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw.replace(b"\r\n", b"\n")).hexdigest()


def canonical(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")


def sources_contract() -> dict[str, object]:
    return {
        "schema": "riemann.glo764.circle_geometry.sources.v1",
        "base_commit": BASE,
        "sources": [
            {"path": path, "git_blob": blob, "sha256_lf": sha}
            for path, blob, sha in SOURCE_ROWS
        ],
        "normalization": "continuous normalized multiplicative maps; irrational orbit; c>=0; constant-one value at zero retained",
        "scope": "exact finite algebra and specialization of a prose theorem; no analytic nonrationality certificate from samples",
    }


def authenticate() -> dict[str, object]:
    contract = sources_contract()
    need(
        json.loads(MANIFEST.read_text(encoding="utf-8")) == contract,
        "source manifest differs from compiled contract",
    )
    for path, blob, sha in SOURCE_ROWS:
        result = subprocess.run(
            ["git", "rev-parse", "--verify", BASE + ":" + path],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
            timeout=15,
        )
        need(
            result.returncode == 0 and result.stdout.strip() == blob,
            "source commit/blob mismatch: " + path,
        )
        raw = subprocess.run(
            ["git", "cat-file", "blob", blob],
            cwd=ROOT,
            capture_output=True,
            check=False,
            timeout=15,
        )
        need(
            raw.returncode == 0 and digest(raw.stdout) == sha,
            "frozen source content mismatch: " + path,
        )
        need(
            digest((ROOT / path).read_bytes()) == sha,
            "current primitive differs from frozen source: " + path,
        )
    return contract


def load_precursor():
    # Authentication is deliberately before exec_module, not after importing code.
    authenticate()
    source = ROOT / SOURCE_ROWS[1][0]
    spec = importlib.util.spec_from_file_location("circle_geometry_precursor", source)
    need(spec is not None and spec.loader is not None, "precursor import unavailable")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


C = load_precursor()
UNIT_POINTS: tuple[G, ...] = (
    (Fraction(1), Fraction(0)),
    (Fraction(-1), Fraction(0)),
    (Fraction(3, 5), Fraction(4, 5)),
    (Fraction(5, 13), Fraction(12, 13)),
)


def gaussian(value: G) -> G:
    need(isinstance(value, tuple) and len(value) == 2, "Gaussian pair required")
    return C.rational(value[0]), C.rational(value[1])


def unit(value: G) -> G:
    value = gaussian(value)
    need(value[0] ** 2 + value[1] ** 2 == 1, "unit-circle point required")
    return value


def signed_power(value: G, power: int) -> G:
    value = gaussian(value)
    power = C.integer(power, "signed power", -40, 40)
    if power < 0:
        return C.gpow(C.gdiv(C.ONE, value), -power)
    return C.gpow(value, power)


def degree_weight(degree: int, weight: int) -> tuple[int, int]:
    degree = C.integer(degree, "degree", 0, MAX_DEGREE)
    weight = C.integer(weight, "weight", -MAX_WEIGHT, MAX_WEIGHT)
    need((degree - weight) % 2 == 0, "degree/weight parity mismatch")
    need(degree > 0 or weight == 0, "degree zero admits only the constant-one map")
    return degree, weight


def touching_spectrum(degree: int, weight: int) -> dict[int, Fraction]:
    degree, weight = degree_weight(degree, weight)
    shift = (weight - degree) // 2
    return {shift + i: Fraction(math.comb(degree, i)) for i in range(degree + 1)}


def monomial_map(value: G, degree: int, weight: int) -> G:
    """Evaluate the continuous map exactly, including negative formal exponents."""
    degree, weight = degree_weight(degree, weight)
    value = gaussian(value)
    if value == C.ZERO:
        return C.ONE if degree == 0 else C.ZERO
    return C.gmul(
        signed_power(value, (degree + weight) // 2),
        signed_power(C.gconj(value), (degree - weight) // 2),
    )


def laurent_value(spectrum: dict[int, Fraction], point: G) -> G:
    point = unit(point)
    need(
        isinstance(spectrum, dict) and len(spectrum) <= 2 * MAX_DEGREE + 1,
        "spectrum cap",
    )
    answer = C.ZERO
    for label, coefficient in spectrum.items():
        coefficient = C.rational(coefficient)
        answer = C.gadd(
            answer, C.gmul((coefficient, Fraction(0)), signed_power(point, label))
        )
    return answer


def polynomial_spectrum(center: int | Fraction, m: int, n: int) -> dict[int, Fraction]:
    C.bidegree(m, n)
    center = C.rational(center)
    need(center >= 0, "nonnegative real center required")
    answer: dict[int, Fraction] = {}
    for i in range(m + 1):
        for j in range(n + 1):
            value = math.comb(m, i) * math.comb(n, j) * center ** (m + n - i - j)
            answer[i - j] = answer.get(i - j, Fraction(0)) + value
    return {label: value for label, value in sorted(answer.items()) if value != 0}


def specialize_theorem(
    real_a: int | Fraction, imag_a: int | Fraction, weight: int, center: int | Fraction
) -> dict[str, object]:
    """Exact theorem specialization, expressly not a sample-based analytic proof."""
    real_a, imag_a, center = map(C.rational, (real_a, imag_a, center))
    weight = C.integer(weight, "weight", -MAX_WEIGHT, MAX_WEIGHT)
    need(center >= 0, "nonnegative real center required")
    constant = real_a == imag_a == 0 and weight == 0
    need(constant or real_a > 0, "not a continuous normalized map at zero")
    need(real_a <= MAX_DEGREE and abs(imag_a) <= MAX_DEGREE, "parameter cap")
    degree_integer = imag_a == 0 and real_a.denominator == 1
    parity = degree_integer and (real_a.numerator - weight) % 2 == 0
    polynomial = constant or (parity and abs(weight) <= real_a)
    if constant or center == 0:
        order = 1
    elif center == 1 and parity or center != 1 and polynomial:
        order = real_a.numerator + 1
    else:
        order = None
    return {
        "a_real": C.qjson(real_a),
        "a_imag": C.qjson(imag_a),
        "weight": weight,
        "center": C.qjson(center),
        "polynomial_map": bool(polynomial),
        "recurrent": order is not None,
        "order": order,
        "evidence_kind": "specialization_of_prose_theorem_not_finite_sample_certificate",
    }


def touching_control(degree: int, weight: int) -> dict[str, object]:
    spectrum = touching_spectrum(degree, weight)
    rows = []
    for point in UNIT_POINTS:
        actual = monomial_map(C.gadd(C.ONE, point), degree, weight)
        expected = laurent_value(spectrum, point)
        need(actual == expected, "origin-touching identity failed")
        rows.append({"w": C.gjson(point), "value": C.gjson(actual)})
    return {
        "degree": degree,
        "weight": weight,
        "order": len(spectrum),
        "spectrum": [[label, C.qjson(value)] for label, value in spectrum.items()],
        "values": rows,
    }


def polynomial_control(center: Fraction, m: int, n: int) -> dict[str, object]:
    spectrum = polynomial_spectrum(center, m, n)
    expected_order = 1 if center == 0 else m + n + 1
    need(len(spectrum) == expected_order, "polynomial probe order failed")
    rows = []
    for point in UNIT_POINTS:
        value = C.gadd((center, Fraction(0)), point)
        actual = C.gmul(C.gpow(value, m), C.gpow(C.gconj(value), n))
        expected = laurent_value(spectrum, point)
        need(actual == expected, "polynomial probe evaluation failed")
        rows.append({"w": C.gjson(point), "value": C.gjson(actual)})
    return {
        "center": C.qjson(center),
        "m": m,
        "n": n,
        "order": len(spectrum),
        "values": rows,
    }


def moved_circle_control(center: Fraction) -> dict[str, object]:
    center = C.rational(center)
    need(center > 0 and center != 1, "held-out center must be nondegenerate")
    point = (Fraction(0), Fraction(1))
    actual = monomial_map(C.gadd((center, Fraction(0)), point), 1, 3)
    touching_prediction = laurent_value(touching_spectrum(1, 3), point)
    need(actual != touching_prediction, "held-out false-positive control failed")
    return {
        "center": C.qjson(center),
        "w": C.gjson(point),
        "actual": C.gjson(actual),
        "incorrect_transplanted_c1_formula": C.gjson(touching_prediction),
        "scope": "this one formula fails; full nonrecurrence follows only from the theorem",
    }


def produce() -> dict[str, object]:
    sources = authenticate()
    parameters = (
        (0, 0, 0),
        (1, 0, 1),
        (2, 0, 0),
        (1, 0, 3),
        (1, 0, -3),
        (3, 0, 7),
        (Fraction(1, 2), 0, 0),
        (2, 1, 0),
        (2, 0, 1),
    )
    centers = (Fraction(0), Fraction(1, 2), Fraction(1), Fraction(2))
    payload: dict[str, object] = {
        "schema": "riemann.glo764.circle_geometry.v1",
        "claims": [
            "GLO764.PROBE.CIRCLE_GEOMETRY_CLASSIFICATION",
            "GLO764.PROBE.CONNECTED_DEGENERATE_FAMILIES",
        ],
        "arithmetic": "EXACT_GAUSSIAN_RATIONAL",
        "theorem_status": "prose proof; analytic classifications are not inferred from finite samples",
        "caps": {
            "degree": MAX_DEGREE,
            "absolute_weight": MAX_WEIGHT,
            "signed_power": 40,
        },
        "touching": [touching_control(0, 0)]
        + [
            touching_control(degree, degree + 2 * shift)
            for degree in range(1, 5)
            for shift in range(-3, 4)
        ],
        "polynomial_probes": [
            polynomial_control(center, m, n)
            for center in centers
            for m, n in ((0, 0), (1, 0), (0, 1), (1, 1), (2, 1), (3, 3))
        ],
        "theorem_specializations": [
            specialize_theorem(real_a, imag_a, weight, center)
            for real_a, imag_a, weight in parameters
            for center in centers
        ],
        "moved_circle_controls": [
            moved_circle_control(center) for center in (Fraction(1, 2), Fraction(2))
        ],
        "source_manifest": sources,
        "owned_files": {
            path.relative_to(ROOT).as_posix(): digest(path.read_bytes())
            for path in (NOTE, Path(__file__), TEST, MANIFEST)
        },
        "firewalls": [
            "no computation of noninteger powers",
            "no natural-boundary theorem",
            "no pointwise-family local-constancy assertion in the degenerate chamber",
            "no global L-function, completion, or RH/GRH consequence",
            "no external publication priority claim",
        ],
    }
    payload["payload_sha256"] = hashlib.sha256(canonical(payload)).hexdigest()
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = produce()
    if args.write:
        FIXTURE.write_text(
            json.dumps(payload, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        print("wrote exact circle-probe geometry controls")
    else:
        need(
            json.loads(FIXTURE.read_text(encoding="utf-8")) == payload,
            "fixture differs from full exact replay",
        )
        print("exact circle-probe geometry controls: PASS")


if __name__ == "__main__":
    main()
