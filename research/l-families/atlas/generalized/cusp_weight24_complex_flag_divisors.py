"""Exact finite FC controls; analytic prime twists and divisor counts are not computed."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import subprocess
import sys
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DIR = "research/l-families/atlas/generalized"
STEM = "cusp_weight24_complex_flag_divisors"
FI = "cusp_weight24_fixed_divisor_infinity"
BASE = "ec5bdd9b02ea68bddfcf34ac40a85d283faf64cf"
REVIEW = "0f29fd2d687c57402a14723dde2bc2b7e74fa317"
CAPS = {
    "source_q_order": 64,
    "flag_count": 32,
    "integer_bits": 4096,
    "work": 1000000,
    "json_bytes": 3000000,
    "json_nodes": 150000,
    "json_depth": 24,
    "container_length": 1024,
    "string_length": 4096,
}
PINS = (
    (BASE, f"{DIR}/CUSP_WEIGHT24_FIXED_DIVISOR_INFINITY.md"),
    (BASE, f"{DIR}/{FI}.py"),
    (BASE, f"{DIR}/{FI}.json"),
    (BASE, f"{DIR}/{FI}.sources.json"),
    (BASE, f"tests/test_{FI}.py"),
    (REVIEW, f"{DIR}/CUSP_WEIGHT24_FIXED_DIVISOR_INFINITY_AUDIT_EC5BDD9B.md"),
)
ARTIFACTS = (
    f"{DIR}/CUSP_WEIGHT24_COMPLEX_FLAG_DIVISORS.md",
    f"{DIR}/{STEM}.py",
    f"{DIR}/{STEM}.sources.json",
    f"tests/test_{STEM}.py",
)
PRIMARY = (
    (
        "BT",
        "https://msp.org/ant/2014/8-9/ant-v8-n9-p01-s.pdf",
        "Proposition3.1; pp2040-2041",
    ),
    (
        "BT-correction",
        "https://msp.org/ant/2014/8-9/ant-v8-n9-x01-Correction-ZerosOfLFunctions.pdf",
        "both pages; corrected uniform error still tends to zero",
    ),
)
D0 = 144169


class Rejected(ValueError):
    """The input does not satisfy the exact finite acceptance contract."""


def need(ok: bool, why: str) -> None:
    if not ok:
        raise Rejected(why)


def integer(n: object, low: int | None = None, high: int | None = None) -> int:
    need(type(n) is int, "integer type")
    need(abs(n).bit_length() <= CAPS["integer_bits"], "integer bits")
    need(low is None or n >= low, "integer lower bound")
    need(high is None or n <= high, "integer upper bound")
    return n


def rational(x: object) -> F:
    need(type(x) is F, "rational type")
    integer(x.numerator)
    integer(x.denominator, 1)
    return x


def wire(x: F) -> list[int]:
    rational(x)
    return [x.numerator, x.denominator]


def unwire(x: object) -> F:
    need(type(x) is list and len(x) == 2, "rational wire")
    n, d = integer(x[0]), integer(x[1], 1)
    need(math.gcd(n, d) == 1, "reduced rational")
    return rational(F(n, d))


class Budget:
    def __init__(self, limit: int = CAPS["work"]):
        self.limit = integer(limit, 1, CAPS["work"])
        self.used = 0

    def charge(self, amount: int = 1) -> None:
        integer(amount, 0, CAPS["work"])
        need(self.used + amount <= self.limit, "work cap")
        self.used += amount


def pair(x: object) -> tuple[F, F]:
    need(type(x) is tuple and len(x) == 2, "pair type")
    return rational(x[0]), rational(x[1])


def add(x: tuple[F, F], y: tuple[F, F]) -> tuple[F, F]:
    a, b = pair(x)
    c, d = pair(y)
    return rational(a + c), rational(b + d)


def scale(x: tuple[F, F], a: F) -> tuple[F, F]:
    b, c = pair(x)
    rational(a)
    return rational(a * b), rational(a * c)


def mul(x: tuple[F, F], y: tuple[F, F], radicand: int = -1) -> tuple[F, F]:
    need(type(radicand) is int and radicand in (-1, D0), "typed field")
    a, b = pair(x)
    c, d = pair(y)
    return rational(a * c + radicand * b * d), rational(a * d + b * c)


def norm2(x: tuple[F, F]) -> F:
    a, b = pair(x)
    return rational(a * a + b * b)


def wp(x: tuple[F, F]) -> list[list[int]]:
    return list(map(wire, pair(x)))


def weights(p: F, q: F, d: F) -> tuple[F, F, F]:
    for value in (p, q, d):
        rational(value)
    need(p >= 0 and q >= 0 and p + q == 1 and d * d <= 4 * p * q, "line weights")
    return p, q, d


def line_weights(r: tuple[F, F] | None) -> tuple[F, F, F]:
    if r is None:
        return F(0), F(1), F(0)
    x, y = pair(r)
    size = 1 + x * x + y * y
    return weights(F(1) / size, (x * x + y * y) / size, 2 * x / size)


def target_values(p: F, q: F, d: F, target: tuple) -> tuple:
    weights(p, q, d)
    need(type(target) is tuple and len(target) == 4, "four common inputs")
    z, plus, minus, cross = map(pair, target)
    x, y = mul(z, plus), mul(z, minus)
    denominator = add(add(scale(x, p), scale(y, q)), scale(cross, d))
    numerator = add(mul(x, y), scale(mul(cross, cross), F(-1)))
    return denominator, numerator


def pole_target(p: F, q: F, d: F) -> tuple:
    weights(p, q, d)
    need(p > 0 and q > 0, "mixed line required")
    return tuple(
        map(pair, ((F(1), F(0)), (F(1), F(0)), (-p / q, -d / (q * q)), (F(0), 1 / q)))
    )


def zero_target(p: F, q: F, d: F) -> tuple:
    weights(p, q, d)
    e = F(1 if d >= 0 else -1)
    return ((F(1), F(0)), (F(1), F(0)), (F(1), F(0)), (e, F(0)))


def annulus(target: tuple, radius: F) -> None:
    rational(radius)
    need(radius > 1, "annulus radius")
    for coordinate in target:
        need(1 / (radius * radius) <= norm2(coordinate) <= radius * radius, "annulus")


def lf(raw: bytes) -> bytes:
    return raw.replace(b"\r\n", b"\n")


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def encoded(value: object) -> bytes:
    return (
        json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True) + "\n"
    ).encode("ascii")


def typed(value: object, depth: int = 0, nodes: list[int] | None = None) -> None:
    if nodes is None:
        nodes = [0]
    nodes[0] += 1
    need(
        nodes[0] <= CAPS["json_nodes"] and depth <= CAPS["json_depth"], "JSON tree cap"
    )
    if type(value) is int:
        integer(value)
    elif type(value) is str:
        need(len(value) <= CAPS["string_length"], "string cap")
    elif type(value) is list:
        need(len(value) <= CAPS["container_length"], "list cap")
        for v in value:
            typed(v, depth + 1, nodes)
    elif type(value) is dict:
        need(len(value) <= CAPS["container_length"], "dict cap")
        for key, v in value.items():
            need(type(key) is str, "key type")
            typed(key, depth + 1, nodes)
            typed(v, depth + 1, nodes)
    else:
        raise Rejected("bool/float/null/foreign type")


def unique_pairs(items: list[tuple[str, object]]) -> dict:
    out = {}
    for key, value in items:
        need(key not in out, "duplicate JSON key")
        out[key] = value
    return out


def decode(raw: bytes) -> object:
    need(type(raw) is bytes and len(raw) <= CAPS["json_bytes"], "JSON byte cap")
    try:
        out = json.loads(
            raw,
            object_pairs_hook=unique_pairs,
            parse_constant=lambda _: (_ for _ in ()).throw(Rejected("nonfinite JSON")),
        )
    except (ValueError, UnicodeError, RecursionError) as exc:
        raise Rejected("invalid JSON") from exc
    typed(out)
    return out


def file_bytes(path: Path) -> bytes:
    need(path.stat().st_size <= CAPS["json_bytes"], "file byte cap")
    raw = path.read_bytes()
    need(len(raw) <= CAPS["json_bytes"], "read byte cap")
    return raw


def git_bytes(commit: str, path: str) -> bytes:
    out = subprocess.run(
        ["git", "--no-replace-objects", "show", commit + ":" + path],
        cwd=ROOT,
        check=False,
        capture_output=True,
    )
    need(out.returncode == 0, "frozen Git source unavailable")
    need(len(out.stdout) <= CAPS["json_bytes"], "source byte cap")
    return out.stdout


def manifest() -> dict:
    rows = []
    for commit, path in PINS:
        raw = git_bytes(commit, path)
        rows.append(
            {
                "commit": commit,
                "path": path,
                "git_blob": hashlib.sha1(
                    b"blob " + str(len(raw)).encode() + b"\0" + raw
                ).hexdigest(),
                "sha256_lf": digest(lf(raw)),
            }
        )
    return {
        "schema": "complex-flag-sources-v1",
        "authoring_base": BASE,
        "frozen_sources": rows,
        "primary_references": [
            {"id": a, "url": b, "passage": c} for a, b, c in PRIMARY
        ],
        "remote_bytes": "not_authenticated_by_offline_git_checker",
    }


def authenticate() -> None:
    need(
        decode(file_bytes(ROOT / DIR / f"{STEM}.sources.json")) == manifest(),
        "source drift",
    )


def source_payload(budget: Budget) -> dict:
    # Compile the literal frozen producer bytes, not a possibly modified local
    # import. Its primitive payload replays q-series and all coefficient data.
    raw = git_bytes(BASE, f"{DIR}/{FI}.py")
    namespace = {
        "__file__": str(ROOT / DIR / f"{FI}.py"),
        "__name__": "frozen_fi_dependency",
    }
    exec(compile(raw, namespace["__file__"], "exec"), namespace)  # noqa: S102 - fixed frozen Git producer, never user-supplied code
    out = namespace["payload"]()
    frozen = decode(git_bytes(BASE, f"{DIR}/{FI}.json"))
    stripped = {
        key: v
        for key, v in frozen.items()
        if key not in ("payload_sha256", "artifact_sha256_lf")
    }
    need(
        out == stripped and out["q_order"] == CAPS["source_q_order"],
        "FI primitive replay",
    )
    budget.charge(out["work_used"])
    return out


def flag_grid() -> list[tuple[str, tuple[F, F] | None]]:
    rows = [(f"grid_{x}_{y}", (F(x), F(y))) for x in range(-2, 3) for y in range(-2, 3)]
    rows.append(("minus_eigenline", None))
    rows.extend(
        [
            ("near_real_plus", (F(1, 1000), F(0))),
            ("near_real_minus", (F(-1, 1000), F(0))),
            ("near_imag_plus", (F(0), F(1, 1000))),
            ("near_imag_minus", (F(0), F(-1, 1000))),
            ("near_complex", (F(1, 1000), F(2, 1000))),
            ("heldout_3minus4i_over7", (F(3, 7), F(-4, 7))),
        ]
    )
    need(len(rows) == CAPS["flag_count"], "complete fixed flag grid")
    return rows


def native_coefficients(source: dict, r: tuple[F, F] | None, budget: Budget) -> list:
    p, q, d = line_weights(r)
    g, b = source["basis"]
    out = []
    for row in source["dirichlet_coefficients"]:
        n = integer(row["n"], 1, CAPS["source_q_order"])
        predicted = (
            unwire(row["diag_rational"]) + d * unwire(row["cross"]),
            (p - q) * unwire(row["diag_sqrt"]),
        )
        literal = (F(0), F(0))
        for m in range(1, math.isqrt(n) + 1):
            budget.charge(20)
            if n % (m * m):
                continue
            h = n // (m * m)
            plus = (F(g[h] + 540 * b[h]), F(12 * b[h]))
            minus = (plus[0], -plus[1])
            if r is None:
                sq = mul(minus, minus, D0)
            else:
                x, y = r
                real = add(plus, scale(minus, x))
                imag = scale(minus, y)
                sq = scale(
                    add(mul(real, real, D0), mul(imag, imag, D0)),
                    1 / (1 + x * x + y * y),
                )
            literal = add(literal, scale(sq, F(1, h**23)))
        need(
            predicted == literal,
            "literal complex amplitude and square-divisor coefficient",
        )
        out.append(wp(literal))
    need(len(out) == 64, "complete source prefix")
    need(
        out[0] != [[0, 1], [0, 1]] or out[1] != [[0, 1], [0, 1]],
        "nonzero first two pivots",
    )
    return out


def flag_control(
    label: str, r: tuple[F, F] | None, source: dict, budget: Budget
) -> dict:
    p, q, d = line_weights(r)
    target = zero_target(p, q, d)
    denominator, numerator = target_values(p, q, d, target)
    need(numerator == (0, 0) and denominator == (1 + abs(d), 0), "protected zero")
    annulus(target, F(2))
    zero = {"target": list(map(wp, target)), "D": wp(denominator), "N": wp(numerator)}
    poles = []
    if p and q:
        target = pole_target(p, q, d)
        denominator, numerator = target_values(p, q, d, target)
        need(
            denominator == (0, 0)
            and numerator == ((1 - p * q) / (q * q), -d / (q * q)),
            "protected pole",
        )
        need(numerator[0] >= F(3, 4) / (q * q), "pole real reserve")
        epsilon, radius = min(p, q), 2 / min(p, q) ** 2
        annulus(target, radius)
        poles.append(
            {
                "target": list(map(wp, target)),
                "D": wp(denominator),
                "N": wp(numerator),
                "epsilon": wire(epsilon),
                "annulus_radius": wire(radius),
            }
        )
    budget.charge(200)
    return {
        "label": label,
        "chart": "b_over_a_infinite" if r is None else "b_over_a",
        "r": [] if r is None else wp(r),
        "weights": list(map(wire, (p, q, d))),
        "class": "mixed" if p and q else "Hecke_eigenline",
        "zero": zero,
        "pole": poles,
        "native_denominator_prefix": native_coefficients(source, r, budget),
    }


def elementary_controls() -> dict:
    local = []
    for t in (F(1, 2), F(1, 3), F(1, 5), F(1, 17)):
        ratio = (1 + t) / (1 - t)
        m4, m6, m8 = ratio**2, ratio**3, ratio**4
        need(m4 < m6 and m8 == m4 * m4, "shared zeta factor improvement")
        local.append(
            {
                "t": wire(t),
                "M4_local": wire(m4),
                "M6_local": wire(m6),
                "M8_local": wire(m8),
            }
        )
    escape = []
    for delta in (F(1), F(1, 2), F(1, 4), F(1, 8)):
        for kind, x, y in (
            ("real", delta**8 / 4**8, F(0)),
            ("imaginary", F(0), delta**2 / 16),
            ("complex", delta**8 / (2 * 4**8), delta**2 / 32),
        ):
            size2 = x * x + y * y
            need(
                size2 <= delta**4 / 256 and abs(x) <= delta**8 / 65536,
                "escape coordinate envelope",
            )
            first, second = 16 * size2 / delta**4, 512 * abs(x) / delta**8
            need(first <= F(1, 16) and second <= F(1, 128), "escape two budgets")
            escape.append(
                {
                    "kind": kind,
                    "delta": wire(delta),
                    "r": wp((x, y)),
                    "budgets": list(map(wire, (first, second, first + second))),
                }
            )
    return {
        "local_euler_bounds": local,
        "escape_controls": escape,
        "escape_reserve": wire(F(9, 128)),
        "source_majorants": {"D": [2, 4], "N": [2, 8]},
        "ratio_majorants": {
            "Y_over_X": [4, 2],
            "C_over_X": [8, 4],
            "weaker_Y_over_X": [6, 3],
        },
        "canonical_flag_quotient_scale": [2, 1],
        "analytic_prime_cutoff": [3, 2],
    }


def payload() -> dict:
    budget = Budget()
    source = source_payload(budget)
    rows = [flag_control(label, r, source, budget) for label, r in flag_grid()]
    need(sum(row["class"] == "mixed" for row in rows) == 30, "mixed grid count")
    out = {
        "schema": "weight24-complex-flag-divisors-v1",
        "authoring_base": BASE,
        "arithmetic_class": "MIXED",
        "components": ["EXACT_RATIONAL", "CERTIFIED_INTEGER_COVERAGE"],
        "rounding": "none",
        "analytic_claims_machine_certified": "no",
        "weight": 24,
        "quadratic_field": D0,
        "caps": CAPS.copy(),
        "flags": rows,
        "controls": elementary_controls(),
        "work_used": budget.used,
        "scope": "all_complex_lines_analytic_proof_with_complete_declared_finite_controls",
        "not_claimed": [
            "exhaustive_CP1_grid",
            "effective_BT_width",
            "numerical_divisor_location",
            "sharp_escape_exponent",
            "simplicity",
            "RH",
            "new_automorphic_family",
        ],
    }
    typed(out)
    return out


def fixture() -> dict:
    authenticate()
    out = payload()
    out["artifact_sha256_lf"] = {
        path: digest(lf(file_bytes(ROOT / path))) for path in ARTIFACTS
    }
    out["payload_sha256"] = digest(encoded(out))
    need(len(encoded(out)) <= CAPS["json_bytes"], "output cap")
    return out


def validate(value: object) -> None:
    typed(value)
    need(type(value) is dict and value == fixture(), "strict primitive reconstruction")


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
            raw = file_bytes(ROOT / DIR / f"{STEM}.json")
            validate(decode(raw))
            print(
                "PASS: 32 fixed flag controls, all 64 native coefficients, six pins and four artifacts"
            )
            print("fixture_sha256_lf=" + digest(lf(raw)))
        return 0
    except (Rejected, OSError, subprocess.SubprocessError) as exc:
        print("REJECTED: " + str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
