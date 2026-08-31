"""Independent finite-field atlas for the actual AFTER-completion theorem."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from fractions import Fraction
from functools import lru_cache
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
FREEZE = "7b320b3a9a55a16e73d99dd9bbab5bf592d50c93"
PREFIX = "research/l-families/atlas/generalized/koszul-analytic-parent/"
PINS = {
    "COHERENT_QUADRATIC_PLACE_EULER.md": "2b5b7ef94b0c4c6326a0e06221d01d23475ec58e",
    "GLOBAL_KOSZUL_LIE_COHOMOLOGY.md": "6fc43276dc337c68ae4c3d9f70de22a114d14fa3",
    "CONSTRUCTIBLE_POLE_CLEARING_SOURCE.md": "7ed7f6d68327df4c5f395142503253b19e8938e4",
    "FINITE_RESONANT_COHERENT_POLES.md": "c415abc8a9b363a1cef6e0cd52adca16a4f6c754",
    "S3_WEIGHT_CIRCLE_POLE_DIVISOR.md": "381ee262cbd59f671a23f29fa19a9dd6f856463b",
}
DISCOVERY = HERE / "arithmetic_phase.discovery.json"
FIXTURE = HERE / "arithmetic_radius.verification.json"
OWNED = (
    HERE / "ARITHMETIC_RADIUS_DICHOTOMY.md",
    HERE / "ARITHMETIC_RADIUS_REPLAY.md",
    HERE / "ARITHMETIC_PHASE_PREREGISTRATION.md",
    HERE / "arithmetic_phase.discovery.js",
    DISCOVERY,
    HERE / "arithmetic_radius_replay.py",
    ROOT / "tests/test_graded_completion_arithmetic_radius.py",
)
PRIMES = (5, 7, 11, 13, 17, 19, 23, 29, 31)
RAW_KEYS = (
    "p",
    "A",
    "B",
    "pointsE",
    "pointsD",
    "aE",
    "aD",
    "tZ",
    "split",
    "splitPlus",
    "splitMinus",
    "splitZero",
    "oldPlus",
    "oldMinus",
    "delta",
    "zPoints",
    "class",
)
SELECTED = (
    (5, 1, 0),
    (7, 1, 0),
    (11, 1, 3),
    (11, 1, 4),
    (13, 1, 5),
    (13, 4, 1),
    (31, 1, 2),
)
MAX_BYTES = 12_000_000
MAX_BITS = 4096
SCOPE = "complete finite parameter scout; exact rational-fibre and genus-three checks; no analytic proof"


def need(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def integer(value: object, low: int, high: int) -> int:
    need(type(value) is int and low <= value <= high, "integer outside declared cap")
    return value


def digest(data: bytes) -> str:
    return hashlib.sha256(data.replace(b"\r\n", b"\n")).hexdigest()


def authenticate() -> dict:
    result = {}
    for name, blob in PINS.items():
        path = PREFIX + name
        actual = subprocess.check_output(
            ["git", "rev-parse", f"{FREEZE}:{path}"], cwd=ROOT, text=True
        ).strip()
        need(actual == blob, "frozen theorem blob changed")
        frozen = subprocess.check_output(["git", "cat-file", "blob", blob], cwd=ROOT)
        need(len(frozen) < MAX_BYTES, "frozen source byte cap")
        need(
            digest((ROOT / path).read_bytes()) == digest(frozen),
            "working theorem differs from freeze",
        )
        result[name] = {"blob": blob, "sha256_lf": digest(frozen)}
    return result


def parameters(p: int, a: int, b: int) -> None:
    need(type(p) is int and p in PRIMES, "declared prime panel required")
    integer(a, 1, p - 1)
    integer(b, 0, p - 1)
    need((4 * a**3 + 27 * b * b) % p != 0, "singular cubic source excluded")


def quadratic_character(value: int, p: int) -> int:
    need(type(p) is int and p in PRIMES, "declared prime required")
    need(type(value) is int, "integer residue required")
    value %= p
    return 0 if value == 0 else 1 if pow(value, (p - 1) // 2, p) == 1 else -1


@lru_cache(maxsize=4096)
def _raw_tuple(p: int, a: int, b: int) -> tuple:
    # Literal ordered quadratic solutions are independent of the JS square-count
    # lookup. Cubic fibres come from a complete polynomial preimage table.
    points_e = 1 + sum(
        1 for x in range(p) for y in range(p) if (y * y - x**3 - a * x - b) % p == 0
    )
    points_d = (
        1
        + quadratic_character(-27, p)
        + sum(
            1
            for u in range(p)
            for v in range(p)
            if (v * v + 4 * a**3 + 27 * (b - u * u) ** 2) % p == 0
        )
    )
    preimages = [[] for _ in range(p)]
    for x in range(p):
        preimages[(x**3 + a * x + b) % p].append(x)
    split = plus = minus = zero = old_plus = old_minus = 0
    for u in range(p):
        roots = preimages[u * u % p]
        disc = (-4 * a**3 - 27 * (b - u * u) ** 2) % p
        sign = quadratic_character(u, p)
        if disc == 0:
            need(len(roots) == 2 and sign != 0, "old simple ramification source")
            old_plus += int(sign == 1)
            old_minus += int(sign == -1)
        else:
            need(len(roots) in (0, 1, 3), "unramified cubic splitting type")
            if len(roots) == 3:
                split += 1
                plus += int(sign == 1)
                minus += int(sign == -1)
                zero += int(sign == 0)
    delta = int(p % 3 == 1)
    ae, ad = p + 1 - points_e, p + 1 - points_d
    trace = ad + 2 * ae
    zpoints = 6 * split + 3 * (old_plus + old_minus) + 2 * delta
    need(trace == p + 1 - zpoints, "proper genus-three source identity")
    need(ae * ae <= 4 * p and ad * ad <= 4 * p, "elliptic source bound")
    label = (
        "zero"
        if trace == 0
        else "fractional"
        if trace % 12
        else "negative_integer"
        if trace < 0
        else "positive_integer"
    )
    return (
        p,
        a,
        b,
        points_e,
        points_d,
        ae,
        ad,
        trace,
        split,
        plus,
        minus,
        zero,
        old_plus,
        old_minus,
        delta,
        zpoints,
        label,
    )


def raw_row(p: int, a: int, b: int) -> dict:
    parameters(p, a, b)
    # Return a fresh dict: callers cannot mutate the cached source data.
    return dict(zip(RAW_KEYS, _raw_tuple(p, a, b), strict=True))


def atlas() -> dict:
    panels, examples = [], {}
    total = 0
    for p in PRIMES:
        rows = [
            raw_row(p, a, b)
            for a in range(1, p)
            for b in range(p)
            if (4 * a**3 + 27 * b * b) % p
        ]
        classes, traces = {}, {}
        for row in rows:
            classes[row["class"]] = classes.get(row["class"], 0) + 1
            key = str(row["tZ"])
            traces[key] = traces.get(key, 0) + 1
            key = row["class"] + (
                "_ramified"
                if row["oldPlus"] + row["oldMinus"] + row["delta"]
                else "_no_rational_ramification"
            )
            if key not in examples:
                examples[key] = row
        panels.append(
            {
                "p": p,
                "count": len(rows),
                "classes": classes,
                "traces": traces,
                "rows": rows,
            }
        )
        total += len(rows)
    need(total == 3044, "complete preregistered parameter count")
    return {"scope": SCOPE, "panels": panels, "examples": examples, "total": total}


def fraction_pair(value: Fraction) -> list[int]:
    return [value.numerator, value.denominator]


def nonnegative_integer(value: Fraction) -> bool:
    return value.denominator == 1 and value >= 0


def local_behavior(value: Fraction) -> str:
    return (
        "branch"
        if value.denominator != 1
        else "pole"
        if value < 0
        else "unit"
        if value == 0
        else "removable_zero"
    )


def classify_after(row: dict) -> dict:
    need(
        type(row) is dict and all(key in row for key in RAW_KEYS),
        "complete raw source row required",
    )
    p, a, b = (row[key] for key in ("p", "A", "B"))
    parameters(p, a, b)
    for key in RAW_KEYS[:-1]:
        need(type(row[key]) is int, "raw source fields must be strict integers")
    for key in ("split", "splitPlus", "splitMinus", "splitZero", "oldPlus", "oldMinus"):
        integer(row[key], 0, p)
    need(
        row["aE"] == p + 1 - row["pointsE"] and row["aD"] == p + 1 - row["pointsD"],
        "proper count/trace identity",
    )
    need(row["aE"] ** 2 <= 4 * p and row["aD"] ** 2 <= 4 * p, "elliptic trace range")
    need(
        row["split"] == row["splitPlus"] + row["splitMinus"] + row["splitZero"],
        "split zero/sign partition",
    )
    need(row["splitZero"] in (0, 1), "zero is a single place")
    need(row["delta"] == int(p % 3 == 1), "infinity splitting source")
    ae, ad, trace = row["aE"], row["aD"], row["tZ"]
    need(
        trace == ad + 2 * ae and trace == p + 1 - row["zPoints"],
        "trace source mismatch",
    )
    need(
        row["zPoints"]
        == 6 * row["split"] + 3 * (row["oldPlus"] + row["oldMinus"]) + 2 * row["delta"],
        "normalized Galois fibre count",
    )
    need(
        (row["oldPlus"] + row["oldMinus"]) % 2 == 0 and trace % 6 == 0,
        "source six-divisibility",
    )
    if p % 4 == 3:
        need(
            row["splitPlus"] == row["splitMinus"] and row["oldPlus"] == row["oldMinus"],
            "u-minus-u source symmetry",
        )
    else:
        need(
            all(
                row[key] % 2 == 0
                for key in ("splitPlus", "splitMinus", "oldPlus", "oldMinus")
            ),
            "paired equal-sign source symmetry",
        )
    alpha = Fraction(trace, 12)
    beta = Fraction(ad - ae, 6)
    trace2 = ad * ad + 2 * ae * ae - 6 * p
    gamma = Fraction(trace2, 24)
    nu_plus, nu_minus = alpha + row["splitMinus"], alpha + row["splitPlus"]
    k = trace // 6
    need(beta == k - Fraction(ae, 2), "secondary coefficient identity")
    need(
        gamma == Fraction(6 * k * k - 4 * k * ae + ae * ae - p, 4),
        "second-power coefficient identity",
    )
    need((4 * gamma).denominator == 1, "gamma must be a quarter-integer")
    need(
        gamma.denominator != 1 or (gamma + beta).denominator != 1,
        "second-circle parity obstruction",
    )
    removable = nonnegative_integer(nu_plus) and nonnegative_integer(nu_minus)
    return {
        "alpha": fraction_pair(alpha),
        "beta": fraction_pair(beta),
        "gamma": fraction_pair(gamma),
        "trace_Z_squared": trace2,
        "nu_plus": fraction_pair(nu_plus),
        "nu_minus": fraction_pair(nu_minus),
        "positive_first_behavior": local_behavior(nu_plus),
        "negative_first_behavior": local_behavior(nu_minus),
        "pure_multiplier_first_behavior": local_behavior(alpha),
        "second_real_exponent": fraction_pair(gamma),
        "second_imaginary_exponent": fraction_pair(gamma + beta),
        "second_nonintegral_real": gamma.denominator != 1,
        "second_nonintegral_imaginary": (gamma + beta).denominator != 1,
        "after_radius": "1/sqrt(2)" if removable else "1/2",
        "negative_multiplier_canceled_by_finite_source": alpha < 0
        and alpha.denominator == 1
        and removable,
    }


def mobius(n: int) -> int:
    integer(n, 1, 128)
    rest, sign, prime = n, 1, 2
    while prime * prime <= rest:
        if rest % prime == 0:
            rest //= prime
            sign = -sign
            if rest % prime == 0:
                return 0
        prime += 1
    return -sign if rest > 1 else sign


def source_power(kind: str, n: int) -> str:
    need(kind in ("e", "s", "c"), "S3 source class required")
    integer(n, 1, 128)
    return (
        "e"
        if kind == "e" or (kind == "s" and n % 2 == 0) or (kind == "c" and n % 3 == 0)
        else kind
    )


def log_source(kind: str, n: int) -> int:
    need(kind in ("e", "s", "c"), "S3 source class required")
    integer(n, 1, 128)
    return (
        4 - (-2) ** n
        if kind == "e"
        else (4 if n % 2 == 0 else 0)
        if kind == "s"
        else (3 if n % 3 == 0 else 0)
    )


def source_characters(n: int) -> list[int]:
    integer(n, 1, 128)
    out = []
    for kind in ("e", "s", "c"):
        top = (-1) ** (n + 1) * sum(
            mobius(h) * log_source(source_power(kind, h), n // h)
            for h in range(1, n + 1)
            if n % h == 0
        )
        need(top % n == 0, "integral source character")
        out.append(top // n)
    return out


def restricted_characters(n: int) -> list[int]:
    integer(n, 2, 128)
    need(n % 2 == 0, "even grade required")
    out = []
    for divisor_condition in (1, 2, 3):
        top = sum(
            mobius(h) * (-2) ** (n // h)
            for h in range(1, n + 1)
            if n % h == 0 and h % divisor_condition == 0
        )
        need(top % n == 0, "restricted-divisor integrality")
        out.append(top // n)
    return out


def multiplicities(n: int) -> tuple[int, int, int]:
    d, s, c = source_characters(n)
    tops = (d + 3 * s + 2 * c, d - 3 * s + 2 * c, 2 * (d - c))
    need(all(x >= 0 and x % 6 == 0 for x in tops), "actual S3 multiplicities")
    return tuple(x // 6 for x in tops)


def character_controls() -> list:
    rows = []
    for n in range(2, 129, 2):
        direct, restricted = source_characters(n), restricted_characters(n)
        need(direct == restricted, "PBW versus restricted-divisor source mismatch")
        d, s, c = direct
        leading = Fraction(2**n, n)
        secondary = Fraction((-2) ** (n // 2), n)
        ed, es = Fraction(d) - leading + secondary, Fraction(s) + secondary
        bd, bs = Fraction(2 ** (n // 3 + 1) - 2, n), Fraction(2 ** (n // 6 + 1) - 2, n)
        need(
            abs(ed) <= bd and abs(c) <= bd and abs(es) <= bs,
            "proved character remainder bound",
        )
        rows.append(
            {
                "grade": n,
                "characters": direct,
                "multiplicities": list(multiplicities(n)),
                "dimension_error": fraction_pair(ed),
                "transposition_error": fraction_pair(es),
                "dimension_cycle_bound": fraction_pair(bd),
                "transposition_bound": fraction_pair(bs),
            }
        )
    return rows


def multiply(a: list[int], b: list[int], cut: int) -> list[int]:
    integer(cut, 0, 32)
    need(len(a) <= cut + 1 and len(b) <= cut + 1, "polynomial length cap")
    out = [0] * (cut + 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b[: cut - i + 1]):
            out[i + j] += x * y
    need(all(abs(x).bit_length() <= MAX_BITS for x in out), "coefficient bit cap")
    return out


def power(a: list[int], exponent: int, cut: int) -> list[int]:
    integer(exponent, 0, 2**32)
    integer(cut, 0, 32)
    out = [1] + [0] * cut
    base = a
    while exponent:
        if exponent % 2:
            out = multiply(out, base, cut)
        exponent //= 2
        if exponent:
            base = multiply(base, base, cut)
    return out


def frobenius_traces(trace: int, p: int, cut: int) -> list[int]:
    need(type(p) is int and p in PRIMES, "declared field required")
    need(type(trace) is int and trace * trace <= 4 * p, "elliptic trace required")
    integer(cut, 1, 32)
    out = [2, trace]
    for _ in range(2, cut + 1):
        out.append(trace * out[-1] - p * out[-2])
    return out[: cut + 1]


def finite_ladder(row: dict, cap: int, cut: int, newton: bool = False) -> list[int]:
    classify_after(row)
    integer(cap, 4, 12)
    integer(cut, 0, 32)
    need(
        cap % 2 == 0 and type(newton) is bool,
        "even cutoff and Boolean algorithm selector",
    )
    p, ae, ad = row["p"], row["aE"], row["aD"]
    out = [1] + [0] * cut
    if newton:
        derivative = [0] * (cut + 1)
        te, td = (
            frobenius_traces(ae, p, max(1, cut)),
            frobenius_traces(ad, p, max(1, cut)),
        )
        for n in range(4, cap + 1, 2):
            _, b, c = multiplicities(n)
            for k in range(1, cut // n + 1):
                derivative[n * k] -= n * (b * td[k] + c * te[k])
        for n in range(1, cut + 1):
            top = sum(derivative[k] * out[n - k] for k in range(1, n + 1))
            need(top % n == 0, "Newton coefficient integrality")
            out[n] = top // n
    else:
        for n in range(4, cap + 1, 2):
            _, b, c = multiplicities(n)
            for trace, exponent in ((ad, b), (ae, c)):
                factor = [0] * (cut + 1)
                factor[0] = 1
                if n <= cut:
                    factor[n] = -trace
                if 2 * n <= cut:
                    factor[2 * n] = p
                out = multiply(out, power(factor, exponent, cut), cut)
    return out


def closure_control(p: int, a: int, b: int) -> dict:
    row = raw_row(p, a, b)
    # Actual affine Galois source: y²=f3(x), v²=-3x²-4A.
    # Its two normalized infinity points are rational iff delta=1.
    fibres = []
    for x in range(p):
        ys = [y for y in range(p) if (y * y - x**3 - a * x - b) % p == 0]
        vs = [v for v in range(p) if (v * v + 3 * x * x + 4 * a) % p == 0]
        fibres.append({"x": x, "ys": ys, "vs": vs, "ordered_pairs": len(ys) * len(vs)})
    count = sum(x["ordered_pairs"] for x in fibres) + 2 * row["delta"]
    need(count == row["zPoints"], "independent normalized Galois closure count")
    return {
        "parameters": [p, a, b],
        "affine_fibres": fibres,
        "infinity_count": 2 * row["delta"],
        "proper_count": count,
    }


def _json_tree(value) -> bool:
    if type(value) in (type(None), bool, int, float, str):
        return True
    if type(value) is list:
        return all(_json_tree(item) for item in value)
    if type(value) is dict:
        return all(type(key) is str and _json_tree(item) for key, item in value.items())
    return False


def strict_equal(a, b) -> bool:
    if not _json_tree(a) or not _json_tree(b):
        return False
    try:
        return json.dumps(
            a, sort_keys=True, separators=(",", ":"), allow_nan=False
        ) == json.dumps(b, sort_keys=True, separators=(",", ":"), allow_nan=False)
    except (TypeError, ValueError):
        return False


def check_discovery(candidate: object, expected: dict | None = None) -> None:
    need(
        strict_equal(candidate, atlas() if expected is None else expected),
        "independent Python rows differ from preregistered JS capture",
    )


def build_payload() -> dict:
    provenance = authenticate()
    data = DISCOVERY.read_bytes()
    need(len(data) <= MAX_BYTES, "discovery byte cap")
    source = atlas()
    check_discovery(json.loads(data), source)
    panels, totals = [], {"1/2": 0, "1/sqrt(2)": 0}
    for panel in source["panels"]:
        counts = {"1/2": 0, "1/sqrt(2)": 0}
        rows = []
        for raw in panel["rows"]:
            analytic = classify_after(raw)
            counts[analytic["after_radius"]] += 1
            totals[analytic["after_radius"]] += 1
            rows.append({**raw, "analytic": analytic})
        panels.append({**panel, "rows": rows, "after_radius_counts": counts})
    selected = []
    for params in SELECTED:
        row = raw_row(*params)
        controls = []
        for cap in (4, 8, 12):
            coefficients = finite_ladder(row, cap, 24)
            need(
                coefficients == finite_ladder(row, cap, 24, True),
                "proper polynomial product versus Newton mismatch",
            )
            controls.append(
                {
                    "grade_cap": cap,
                    "coefficient_cutoff": 24,
                    "coefficients": coefficients,
                }
            )
        selected.append(
            {
                "row": row,
                "analytic": classify_after(row),
                "closure": closure_control(*params),
                "finite_ladders": controls,
            }
        )
    canceled = classify_after(raw_row(11, 1, 3))
    pole = classify_after(raw_row(13, 4, 1))
    need(
        canceled["alpha"] == [-1, 1]
        and canceled["nu_plus"] == canceled["nu_minus"] == [1, 1],
        "negative multiplier/full-source cancellation control",
    )
    need(
        canceled["after_radius"] == "1/sqrt(2)"
        and pole["positive_first_behavior"] == "pole"
        and pole["after_radius"] == "1/2",
        "full-source radius counterfeits",
    )
    return {
        "schema": "actual-after-arithmetic-radius-v1",
        "scope": "AFTER extension only; actual finite parameter sources and proved two-radius theorem",
        "source_commit": FREEZE,
        "source": provenance,
        "owned_sha256_lf": {
            str(p.relative_to(ROOT)).replace("\\", "/"): digest(p.read_bytes())
            for p in OWNED
        },
        "discovery_reconstructed_exactly": True,
        "total": source["total"],
        "panels": panels,
        "after_radius_counts": totals,
        "character_controls": character_controls(),
        "selected_source_controls": selected,
        "counterfeits": {
            "negative_multiplier_canceled": canceled,
            "genuine_full_source_pole": pole,
        },
        "analytic_results_proved_not_inferred_from_atlas": [
            "all-field character remainders",
            "three-log analytic continuation",
            "finite-source zero orders",
            "exact two-radius theorem",
            "second-circle parity obstruction",
        ],
        "not_claimed": [
            "BEFORE-extension classification",
            "3044 distinct isomorphism classes",
            "larger trace-class domain",
            "archimedean completion",
            "number-field transfer",
            "RH",
        ],
    }


def check_payload(candidate: object) -> None:
    need(
        strict_equal(candidate, build_payload()),
        "strict arithmetic-radius replay differs",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    actions = parser.add_mutually_exclusive_group(required=True)
    actions.add_argument("--write", action="store_true")
    actions.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.write:
        encoded = (
            json.dumps(build_payload(), indent=2, sort_keys=True, allow_nan=False)
            + "\n"
        ).encode()
        need(len(encoded) <= MAX_BYTES, "artifact byte cap")
        FIXTURE.write_bytes(encoded)
    else:
        encoded = FIXTURE.read_bytes()
        need(len(encoded) <= MAX_BYTES, "artifact byte cap")
        check_payload(json.loads(encoded))
    print("arithmetic AFTER-radius replay PASS")


if __name__ == "__main__":
    main()
