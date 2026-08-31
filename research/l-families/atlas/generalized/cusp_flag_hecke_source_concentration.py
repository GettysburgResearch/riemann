"""Exact bounded controls; the analytic theorem is in the accompanying note."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import subprocess
import sys
from fractions import Fraction
from pathlib import Path

STEM = "cusp_flag_hecke_source_concentration"
BASE = "070751bf7e96c1dbd6d4b3cfbb05dc70f5a2aa22"
DIR = "research/l-families/atlas/generalized"
ROOT = Path(__file__).resolve().parents[4]
CAPS = {
    "dimension": 4,
    "q_order": 18,
    "integer_bits": 4096,
    "work": 8000000,
    "json_bytes": 2000000,
    "json_nodes": 100000,
    "json_depth": 24,
    "container_length": 1024,
    "string_length": 4096,
}
CLASSES = ((0, 0, 0), (4, 1, 0), (6, 0, 1), (8, 2, 0), (10, 1, 1), (14, 2, 1))
PINS = (
    (
        "c29ae6f3d134e076fa41aef9ae39920478f16ac0",
        f"{DIR}/CUSP_FLAG_FIXED_DEPTH_DIVISOR_LADDER_AUDIT.md",
    ),
    (BASE, f"{DIR}/CUSP_FLAG_FIXED_DEPTH_DIVISOR_LADDER.md"),
    (BASE, f"{DIR}/cusp_flag_fixed_depth_divisor_ladder.py"),
    (BASE, "tests/test_cusp_flag_fixed_depth_divisor_ladder.py"),
    (
        "b69c854d9e3dd1db7b82d95fe6f032fe47d5306b",
        f"{DIR}/CUSP_FLAG_QUOTIENT_GLOBAL_FAMILY.md",
    ),
    (
        "1653565cc80cde6fa882ae9e150626187d3071d0",
        f"{DIR}/CUSP_FLAG_LOCAL_SIMPLE_ENDPOINT_ZERO.md",
    ),
    (
        "b62dfc6348661992bca659c99de226a1b6b22e14",
        f"{DIR}/RANKIN_SELBERG_QUOTIENT_GLOBAL_PARENT.md",
    ),
)
PRIMARY = (
    (
        "HS",
        "https://annals.math.princeton.edu/wp-content/uploads/annals-v172-n2-p18-p.pdf",
        "section2 (2.1)-(2.2), p1523; holomorphic weight-aspect imports",
    ),
    (
        "GHL",
        "https://www.math.columbia.edu/~goldfeld/EffectiveZeroFreeRegion.pdf",
        "pp177-180; p178 holomorphic-weight remark and level-one exclusion",
    ),
    (
        "ILS",
        "https://www.numdam.org/article/PMIHES_2000__91__55_0.pdf",
        "section2 Proposition2.1, (2.14)-(2.20), Lemma2.5; pp68,71,74",
    ),
)
ARTIFACTS = (
    f"{DIR}/CUSP_FLAG_HECKE_SOURCE_CONCENTRATION.md",
    f"{DIR}/{STEM}.py",
    f"{DIR}/{STEM}.sources.json",
    f"tests/test_{STEM}.py",
)


class Rejected(ValueError):
    """Malformed, drifted, or out-of-contract input."""


def require(ok: bool, message: str) -> None:
    if not ok:
        raise Rejected(message)


def integer(value: object, low: int, high: int) -> int:
    require(type(value) is int and low <= value <= high, "integer domain")
    require(abs(value).bit_length() <= CAPS["integer_bits"], "integer bits")
    return value


class Budget:
    def __init__(self, limit: int = CAPS["work"]):
        self.limit = integer(limit, 1, CAPS["work"])
        self.used = 0

    def charge(self, amount: int = 1) -> None:
        integer(amount, 0, CAPS["work"])
        require(self.used + amount <= self.limit, "work cap")
        self.used += amount


def bounded(value: int) -> int:
    require(type(value) is int, "arithmetic type")
    require(abs(value).bit_length() <= CAPS["integer_bits"], "arithmetic bits")
    return value


def lf(data: bytes) -> bytes:
    return data.replace(b"\r\n", b"\n")


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def encoded(value: object) -> bytes:
    return (
        json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True, allow_nan=False)
        + "\n"
    ).encode("ascii")


def typed(value: object, depth: int = 0, nodes: list[int] | None = None) -> None:
    if nodes is None:
        nodes = [0]
    nodes[0] += 1
    require(nodes[0] <= CAPS["json_nodes"], "json nodes")
    require(depth <= CAPS["json_depth"], "json depth")
    if type(value) is int:
        bounded(value)
    elif type(value) is str:
        require(len(value) <= CAPS["string_length"], "string cap")
    elif type(value) is list:
        require(len(value) <= CAPS["container_length"], "list cap")
        for item in value:
            typed(item, depth + 1, nodes)
    elif type(value) is dict:
        require(len(value) <= CAPS["container_length"], "dict cap")
        for key, item in value.items():
            require(type(key) is str, "key type")
            typed(key, depth + 1, nodes)
            typed(item, depth + 1, nodes)
    else:
        raise Rejected("unsupported JSON type, including bool/float/null")


def pairs(items: list[tuple[str, object]]) -> dict:
    out = {}
    for key, value in items:
        require(key not in out, "duplicate JSON key")
        out[key] = value
    return out


def decode(data: bytes) -> object:
    require(type(data) is bytes and len(data) <= CAPS["json_bytes"], "json byte cap")
    try:
        value = json.loads(
            data,
            object_pairs_hook=pairs,
            parse_constant=lambda _: (_ for _ in ()).throw(Rejected("nonfinite JSON")),
        )
    except (UnicodeError, json.JSONDecodeError, RecursionError, ValueError) as exc:
        raise Rejected("invalid JSON") from exc
    typed(value)
    return value


def read_json(path: Path) -> object:
    require(path.stat().st_size <= CAPS["json_bytes"], "json file cap")
    return decode(path.read_bytes())


def artifact_bytes(path: Path) -> bytes:
    require(path.stat().st_size <= CAPS["json_bytes"], "artifact file cap")
    data = path.read_bytes()
    require(len(data) <= CAPS["json_bytes"], "artifact read cap")
    return data


def git_bytes(spec: str) -> bytes:
    result = subprocess.run(
        ["git", "--no-replace-objects", "show", spec],
        cwd=ROOT,
        check=False,
        capture_output=True,
    )
    require(result.returncode == 0, "frozen Git source unavailable")
    require(len(result.stdout) <= CAPS["json_bytes"], "source byte cap")
    return result.stdout


def manifest() -> dict:
    rows = []
    for commit, path in PINS:
        raw = git_bytes(f"{commit}:{path}")
        header = f"blob {len(raw)}\0".encode("ascii")
        rows.append(
            {
                "commit": commit,
                "path": path,
                "git_blob": hashlib.sha1(header + raw).hexdigest(),
                "sha256_lf": digest(lf(raw)),
            }
        )
    return {
        "schema": "hecke-source-manifest-v1",
        "authoring_base": BASE,
        "frozen_sources": rows,
        "primary_references": [
            {"id": key, "url": url, "passage": passage} for key, url, passage in PRIMARY
        ],
        "remote_bytes": "not_authenticated_by_offline_git_checker",
    }


def authenticate_sources() -> None:
    actual = read_json(ROOT / DIR / f"{STEM}.sources.json")
    require(actual == manifest(), "source manifest drift")


def series(value: object) -> list[int]:
    require(
        type(value) is list and 2 <= len(value) <= CAPS["q_order"] + 1,
        "series length/type",
    )
    for item in value:
        bounded(item)
    return value


def mul(a: list[int], b: list[int], budget: Budget) -> list[int]:
    series(a)
    series(b)
    require(len(a) == len(b), "series length mismatch")
    n = len(a) - 1
    budget.charge((n + 1) * (n + 2) // 2)
    out = [0] * (n + 1)
    for i in range(n + 1):
        for j in range(n + 1 - i):
            out[i + j] = bounded(out[i + j] + bounded(a[i] * b[j]))
    return out


def power(a: list[int], exponent: int, budget: Budget) -> list[int]:
    series(a)
    exponent = integer(exponent, 0, 16)
    out = [1] + [0] * (len(a) - 1)
    for _ in range(exponent):
        out = mul(out, a, budget)
    return out


def sigma(n: int, exponent: int) -> int:
    integer(n, 1, CAPS["q_order"])
    integer(exponent, 1, 5)
    return sum(d**exponent for d in range(1, n + 1) if n % d == 0)


def modular_series(
    order: int, budget: Budget
) -> tuple[list[int], list[int], list[int]]:
    order = integer(order, 1, CAPS["q_order"])
    budget.charge(10 * (order + 1) ** 2)
    e4 = [1] + [240 * sigma(n, 3) for n in range(1, order + 1)]
    e6 = [1] + [-504 * sigma(n, 5) for n in range(1, order + 1)]
    cube = power(e4, 3, budget)
    square = power(e6, 2, budget)
    require(all((x - y) % 1728 == 0 for x, y in zip(cube, square)), "Delta integrality")
    delta = [(x - y) // 1728 for x, y in zip(cube, square)]
    recurrence = [0, 1] + [0] * (order - 1)
    for n in range(2, order + 1):
        value = -24 * sum(sigma(h, 1) * recurrence[n - h] for h in range(1, n))
        require(value % (n - 1) == 0, "Delta recurrence integrality")
        recurrence[n] = value // (n - 1)
    require(delta == recurrence, "independent Delta recurrence")
    return e4, e6, delta


def echelon(
    d: int, residual: int, order: int, alternate: int, budget: Budget
) -> list[list[int]]:
    d = integer(d, 2, CAPS["dimension"])
    integer(alternate, 0, 1)
    integer(residual, 0, 14)
    parameters = {r: (a, b) for r, a, b in CLASSES}
    require(residual in parameters, "residual class")
    integer(order, d, CAPS["q_order"])
    e4, e6, delta = modular_series(order, budget)
    a, b = parameters[residual]
    basis = []
    for j in range(1, d + 1):
        p4, p6 = (3 * (d - j) + a, b) if not alternate else (a, 2 * (d - j) + b)
        basis.append(
            mul(
                power(delta, j, budget),
                mul(power(e4, p4, budget), power(e6, p6, budget), budget),
                budget,
            )
        )
    for j in range(d - 1, -1, -1):
        for i in range(j + 1, d):
            scalar = basis[j][i + 1]
            budget.charge(order + 1)
            basis[j] = [
                bounded(x - bounded(scalar * y)) for x, y in zip(basis[j], basis[i])
            ]
    require(
        all(basis[j][i + 1] == int(i == j) for i in range(d) for j in range(d)),
        "echelon pivot",
    )
    return basis


def matmul(a: list[list[int]], b: list[list[int]], budget: Budget) -> list[list[int]]:
    require(type(a) is list and type(b) is list, "matrix type")
    d = len(a)
    require(1 <= d <= CAPS["dimension"] and len(b) == d, "matrix dimension")
    require(all(type(row) is list and len(row) == d for row in a + b), "square matrix")
    for row in a + b:
        for value in row:
            bounded(value)
    budget.charge(d**3)
    out = [[0] * d for _ in range(d)]
    for i in range(d):
        for j in range(d):
            for h in range(d):
                out[i][j] = bounded(out[i][j] + bounded(a[i][h] * b[h][j]))
    return out


def hecke(
    basis: list[list[int]], k: int, prime: int, budget: Budget
) -> list[list[int]]:
    integer(k, 24, 62)
    require(type(prime) is int and prime in (2, 3), "Hecke prime")
    d = integer(len(basis), 2, CAPS["dimension"])
    for row in basis:
        series(row)
    require(all(len(row) == len(basis[0]) for row in basis), "basis lengths")
    require(len(basis[0]) > prime * (d + 2), "complete action source prefix")
    budget.charge(d * (d + 2) * (d + 1))

    def action(j: int, n: int) -> int:
        return bounded(
            basis[j][prime * n]
            + (
                bounded(prime ** (k - 1) * basis[j][n // prime])
                if n % prime == 0
                else 0
            )
        )

    matrix = [[action(j, i + 1) for j in range(d)] for i in range(d)]
    for n in range(1, d + 3):
        for j in range(d):
            reconstructed = 0
            for i in range(d):
                reconstructed = bounded(
                    reconstructed + bounded(matrix[i][j] * basis[i][n])
                )
            require(action(j, n) == reconstructed, "Hecke action beyond pivots")
    return matrix


def rational(value: Fraction) -> list[int]:
    return [bounded(value.numerator), bounded(value.denominator)]


def arithmetic_controls(budget: Budget) -> dict:
    budget.charge(100000)
    floor_rows = []
    for n in range(65):
        u = Fraction(n, 2)
        left = (n // 2) * (n // 2 + 1) // 2
        require(left <= u * u, "floor majorant")
        floor_rows.append([n, left, rational(u * u - left)])
    divisor_rows = []
    for a in range(65):
        gap = math.comb(a + 3, 3) - (a + 1) ** 2
        require(6 * gap == a * (a - 1) * (a + 1) and gap >= 0, "d4 domination")
        divisor_rows.append([a, gap])
    harmonic_rows = []
    for n in range(1, 33):
        harmonic = sum((Fraction(1, h) for h in range(1, n + 1)), Fraction())
        actual = Fraction()
        for a in range(1, n + 1):
            for b in range(1, n // a + 1):
                for c in range(1, n // (a * b) + 1):
                    for d in range(1, n // (a * b * c) + 1):
                        budget.charge()
                        actual += Fraction(1, a * b * c * d)
        require(actual <= harmonic**4, "complete divisor harmonic majorant")
        harmonic_rows.append([n, rational(actual), rational(harmonic**4)])
    gamma_rows = []
    for k in range(1, 129):
        fourth = Fraction(k * (k + 1) * (k + 2) * (k + 3), k**4)
        require(fourth <= 24, "Gamma fourth moment")
        gamma_rows.append([k, rational(fourth)])
    cusp_rows = []
    for j in range(1, 5):
        k = 1000000
        eta = Fraction(1, 10000 * (j + 1))
        constant = Fraction(2 * 4 * (k - 1) * k, 16 * (k - 1) * k * k) / eta**2
        require(constant == 1 / (2 * eta**2 * k), "complete cusp normalization")
        cusp_rows.append(
            {
                "j": j,
                "k": k,
                "eta": rational(eta),
                "mass_coefficient_over_L": rational(constant),
            }
        )
    return {
        "floor": floor_rows,
        "prime_exponent": divisor_rows,
        "harmonic": harmonic_rows,
        "gamma_fourth": gamma_rows,
        "cusp_constants": cusp_rows,
        "moment_majorant_constants": [8, 24, 200, 100],
        "analytic_onset_certified": "no",
    }


def payload() -> dict:
    budget = Budget()
    rows = []
    for d in range(2, 5):
        for residual, _, _ in CLASSES:
            k, order = 12 * d + residual, 3 * (d + 2)
            basis = echelon(d, residual, order, 0, budget)
            require(
                basis == echelon(d, residual, order, 1, budget),
                "independent modular chart",
            )
            t2, t3 = (hecke(basis, k, p, budget) for p in (2, 3))
            require(
                matmul(t2, t3, budget) == matmul(t3, t2, budget), "Hecke commutation"
            )
            rows.append(
                {
                    "d": d,
                    "residual": residual,
                    "k": k,
                    "q_order": order,
                    "action_through": d + 2,
                    "basis": basis,
                    "T2": t2,
                    "T3": t3,
                }
            )
    require(rows[0]["T2"] == [[0, 1], [20468736, 1080]], "weight24 T2 calibration")
    require(
        rows[0]["T3"] == [[195660, -48], [-982499328, 143820]],
        "weight24 T3 calibration",
    )
    controls = arithmetic_controls(budget)
    out = {
        "schema": "hecke-source-concentration-v1",
        "authoring_base": BASE,
        "caps": CAPS.copy(),
        "q_rows": rows,
        "controls": controls,
        "weight24_eigen_equation": [1, -1080, -20468736],
        "completion_ratio_exponent": "-k-1",
        "support_threshold": "k/log(k)",
        "operator_threshold": "o(k/log(k)^5)",
        "scope": "fixed_depth_actual_period_sources_no_effective_onset",
        "work_used": budget.used,
    }
    typed(out)
    return out


def fixture() -> dict:
    authenticate_sources()
    out = payload()
    out["artifact_sha256_lf"] = {
        path: digest(lf(artifact_bytes(ROOT / path))) for path in ARTIFACTS
    }
    out["payload_sha256"] = digest(encoded(out))
    require(len(encoded(out)) <= CAPS["json_bytes"], "output byte cap")
    return out


def validate(value: object) -> None:
    typed(value)
    require(type(value) is dict, "fixture object")
    require(value == fixture(), "strict authenticated reconstruction mismatch")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--check", action="store_true")
    group.add_argument("--emit-fixture", action="store_true")
    group.add_argument("--emit-sources", action="store_true")
    args = parser.parse_args()
    try:
        if args.emit_sources:
            sys.stdout.buffer.write(encoded(manifest()))
        elif args.emit_fixture:
            sys.stdout.buffer.write(encoded(fixture()))
        else:
            path = ROOT / DIR / f"{STEM}.json"
            validate(read_json(path))
            print(
                "PASS: 18 exact Hecke charts, complete finite controls, 7 source pins, 4 artifacts"
            )
            print("fixture_sha256_lf=" + digest(lf(path.read_bytes())))
        return 0
    except (Rejected, OSError, subprocess.SubprocessError) as exc:
        print(f"REJECTED: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
