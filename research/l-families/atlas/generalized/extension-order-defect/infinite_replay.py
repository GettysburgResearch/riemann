"""Exact finite-generator controls for the infinite extension-order theorem."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
import math
import subprocess
import sys
from fractions import Fraction
from functools import lru_cache
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
FIXTURE = HERE / "infinite.verification.json"
OWNED = (
    HERE / "INFINITE_EXTENSION_ORDER.md",
    HERE / "INFINITE_REPLAY.md",
    HERE / "infinite_replay.py",
    ROOT / "tests/test_extension_order_infinite.py",
)
# Both parent-frozen dependencies are authenticated before either import.
PINS = {
    "finite_producer": {
        "freeze": "0018b73f60e42bc793d172c381547de34322d8ca",
        "path": "research/l-families/atlas/generalized/extension-order-defect/replay.py",
        "blob": "6df0f1746caf765efe960aee421323681a488202",
    },
    "finite_proof": {
        "freeze": "0018b73f60e42bc793d172c381547de34322d8ca",
        "path": "research/l-families/atlas/generalized/extension-order-defect/EXTENSION_ORDER_DEFECT.md",
        "blob": "dfb7fcbf1115846664fa99e71116a3635b14d7a0",
    },
    "completion_producer": {
        "freeze": "64075f1a3f81529f217dee1ae139656dfb9356f3",
        "path": "research/l-families/atlas/generalized/graded-completion-lab/replay.py",
        "blob": "18e370b9393d1a907b54c78bd66cc9450f3a624f",
    },
    "completion_proof": {
        "freeze": "64075f1a3f81529f217dee1ae139656dfb9356f3",
        "path": "research/l-families/atlas/generalized/graded-completion-lab/MATHEMATICS.md",
        "blob": "c0e6fe3bb24cbec75cee01ddac6f26ff5358264b",
    },
}


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
    for key, pin in PINS.items():
        need(
            all(v != "PENDING" for v in pin.values()), "source freeze is still pending"
        )
        actual = subprocess.check_output(
            ["git", "rev-parse", f"{pin['freeze']}:{pin['path']}"], cwd=ROOT, text=True
        ).strip()
        need(actual == pin["blob"], "frozen source blob changed")
        frozen = subprocess.check_output(["git", "cat-file", "blob", actual], cwd=ROOT)
        need(len(frozen) < 4_000_000, "source byte cap")
        need(
            digest((ROOT / pin["path"]).read_bytes()) == digest(frozen),
            "working source changed",
        )
        result[key] = {**pin, "sha256_lf": digest(frozen)}
    return result


def dependencies() -> tuple:
    # Every proof and producer is authenticated before either producer executes.
    authenticate()
    modules = []
    for key in ("finite_producer", "completion_producer"):
        name = "extension_infinite_" + key
        if name not in sys.modules:
            spec = importlib.util.spec_from_file_location(
                name, ROOT / PINS[key]["path"]
            )
            need(
                spec is not None and spec.loader is not None,
                "source import unavailable",
            )
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            sys.modules[name] = module
        modules.append(sys.modules[name])
    return tuple(modules)


def multiply(a: list[int], b: list[int], cut: int) -> list[int]:
    integer(cut, 0, 32)
    need(len(a) <= cut + 1 and len(b) <= cut + 1, "series length cap")
    out = [0] * (cut + 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b[: cut - i + 1]):
            out[i + j] += x * y
    need(all(abs(x).bit_length() <= 4096 for x in out), "series coefficient cap")
    return out


def quotient(a: list[int], b: list[int], cut: int) -> list[int]:
    integer(cut, 0, 32)
    need(b and b[0] == 1, "unit denominator required")
    out = [0] * (cut + 1)
    for n in range(cut + 1):
        out[n] = (a[n] if n < len(a) else 0) - sum(
            b[k] * out[n - k] for k in range(1, min(n + 1, len(b)))
        )
    return out


def substitute(a: list[int], degree: int, cut: int, sign: int = 1) -> list[int]:
    integer(degree, 1, 32)
    integer(cut, 0, 32)
    need(type(sign) is int and sign in (-1, 1), "sign required")
    return [
        a[n // degree] * sign ** (n // degree)
        if n % degree == 0 and n // degree < len(a)
        else 0
        for n in range(cut + 1)
    ]


def factor(degree: int, exponent: int, cut: int, sign: int = 1) -> list[int]:
    """Coefficients of (1-sign*t^degree)^(-exponent), signed exponent allowed."""
    integer(degree, 1, 96)
    integer(exponent, -(2**64), 2**64)
    integer(cut, 0, 32)
    need(type(sign) is int and sign in (-1, 1), "sign required")
    out = [0] * (cut + 1)
    out[0] = 1
    for k in range(1, cut // degree + 1):
        out[degree * k] = (
            math.comb(exponent + k - 1, k) * sign**k
            if exponent > 0
            else math.comb(-exponent, k) * (-sign) ** k
            if k <= -exponent
            else 0
        )
    return out


def power_class(kind: str, n: int) -> str:
    need(kind in ("e", "s", "c"), "S3 class required")
    integer(n, 1, 64)
    return (
        "e"
        if kind == "e" or (kind == "s" and n % 2 == 0) or (kind == "c" and n % 3 == 0)
        else kind
    )


def source_rows(cut: int) -> list[dict]:
    """Triangular PBW extraction, independent of the imported Mobius formula."""
    integer(cut, 1, 64)
    classes = ("e", "s", "c")
    rows = []
    for n in range(1, cut + 1):
        chars = []
        for kind in classes:
            logtop = (
                4 - (-2) ** n
                if kind == "e"
                else (4 if n % 2 == 0 else 0)
                if kind == "s"
                else (3 if n % 3 == 0 else 0)
            )
            lower = sum(
                d
                * (-1) ** (d + 1)
                * rows[d - 1]["characters"][classes.index(power_class(kind, n // d))]
                for d in range(1, n)
                if n % d == 0
            )
            top = (-1) ** (n + 1) * (logtop - lower)
            need(top % n == 0, "nonintegral source character")
            chars.append(top // n)
        dim, s, c = chars
        tops = (dim + 3 * s + 2 * c, dim - 3 * s + 2 * c, 2 * (dim - c))
        need(all(x >= 0 and x % 6 == 0 for x in tops), "invalid S3 multiplicity")
        rows.append(
            {"grade": n, "characters": chars, "multiplicities": [x // 6 for x in tops]}
        )
    return rows


def generators(kind: str, cap: int, cut: int) -> list[int]:
    need(kind in ("e", "s", "c"), "S3 class required")
    integer(cap, 2, 32)
    integer(cut, 0, 32)
    need(cap % 2 == 0, "even generator cutoff required")
    out = [1] + [0] * cut
    for row in source_rows(cap)[1::2]:
        n = row["grade"]
        _, b, c = row["multiplicities"]
        if kind == "e":
            factors = [factor(n, b + 2 * c, cut)]
        elif kind == "s":
            factors = [factor(n, b, cut, -1), factor(2 * n, c, cut)]
        else:
            factors = [factor(n, b - c, cut), factor(3 * n, c, cut)]
        for term in factors:
            out = multiply(out, term, cut)
    return out


def generators_newton(kind: str, cap: int, cut: int) -> list[int]:
    need(kind in ("e", "s", "c"), "S3 class required")
    integer(cap, 2, 32)
    integer(cut, 0, 32)
    need(cap % 2 == 0, "even generator cutoff required")
    logarithmic = [0] * (cut + 1)
    for row in source_rows(cap)[1::2]:
        n = row["grade"]
        _, b, c = row["multiplicities"]
        for k in range(1, cut // n + 1):
            h = power_class(kind, k)
            trace = b + 2 * c if h == "e" else -b if h == "s" else b - c
            logarithmic[n * k] += n * trace
    out = [1] + [0] * cut
    for n in range(1, cut + 1):
        top = sum(logarithmic[k] * out[n - k] for k in range(1, n + 1))
        need(top % n == 0, "nonintegral symmetric-algebra coefficient")
        out[n] = top // n
    return out


def segre(kind: str, cut: int, sign: int = 1, even: bool = False) -> list[int]:
    need(kind in ("e", "s", "c"), "S3 class required")
    integer(cut, 0, 32)
    need(type(sign) is int and sign in (-1, 1), "sign required")
    need(type(even) is bool, "boolean parity selector required")
    return [
        0
        if even and n % 2
        else sign**n
        * (
            (n + 1) * math.comb(n + 2, 2)
            if kind == "e"
            else (n // 2 + 1 if n % 2 == 0 else 0)
            if kind == "s"
            else int(n % 3 == 0)
        )
        for n in range(cut + 1)
    ]


def local_series(kind: str, cap: int, cut: int, epsilon: int = 1) -> dict:
    need(kind in ("old", "split", "nonsplit", "zero"), "local source type required")
    need(type(epsilon) is int and epsilon in (-1, 1), "quadratic sign required")
    integer(cap, 2, 32)
    integer(cut, 0, 32)
    need(cap % 2 == 0, "even generator cutoff required")
    ge, gs, gc = (generators(h, cap, cut) for h in ("e", "s", "c"))
    common = [1] + [0] * cut
    for row in source_rows(cap)[1::2]:
        n = row["grade"]
        _, b, c = row["multiplicities"]
        exponent = c if kind == "old" else b
        if kind != "zero":
            common = multiply(
                common, factor(n, exponent, cut, -1 if kind == "nonsplit" else 1), cut
            )
    if kind == "old":
        fe, fs = segre("e", cut, epsilon), segre("s", cut)
        numer = [
            a + b
            for a, b in zip(multiply(fe, ge, cut), multiply(fs, gs, cut), strict=True)
        ]
        need(all(x % 2 == 0 for x in numer), "C2 Reynolds integrality")
        before = [x // 2 for x in numer]
        base = [(a + b) // 2 for a, b in zip(fe, fs, strict=True)]
        after = multiply(base, common, cut)
    elif kind == "split":
        fe, fc = segre("e", cut, even=True), segre("c", cut, even=True)
        numer = [
            a + 2 * b
            for a, b in zip(multiply(fe, ge, cut), multiply(fc, gc, cut), strict=True)
        ]
        need(all(x % 3 == 0 for x in numer), "C3 Reynolds integrality")
        before = [x // 3 for x in numer]
        base = [(a + 2 * b) // 3 for a, b in zip(fe, fc, strict=True)]
        after = multiply(base, common, cut)
    elif kind == "nonsplit":
        before = multiply(segre("s", cut), gs, cut)
        after = multiply(segre("s", cut), common, cut)
    else:
        before = multiply(segre("e", cut, even=True), ge, cut)
        after = before[:]
    return {
        "before": before,
        "after": after,
        "difference": [c - b for c, b in zip(before, after, strict=True)],
        "ratio": quotient(before, after, cut),
    }


def reduced_ratio(kind: str, cap: int, cut: int, epsilon: int = 1) -> list[int]:
    need(kind in ("old", "split", "nonsplit"), "boundary type required")
    need(type(epsilon) is int and epsilon in (-1, 1), "quadratic sign required")
    integer(cap, 2, 32)
    integer(cut, 0, 32)
    need(cap % 2 == 0, "even generator cutoff required")
    v = w = x = y = z = [1] + [0] * cut
    for row in source_rows(cap)[1::2]:
        n = row["grade"]
        _, b, c = row["multiplicities"]
        v = multiply(v, factor(n, b + c, cut), cut)
        w = multiply(w, factor(n, b + c, cut, -1), cut)
        x = multiply(x, factor(n, 2 * c, cut), cut)
        y = multiply(multiply(y, factor(n, -c, cut), cut), factor(3 * n, c, cut), cut)
        z = multiply(z, factor(2 * n, c, cut), cut)
    if kind == "nonsplit":
        return z
    fe = segre("e", cut, epsilon if kind == "old" else 1, kind == "split")
    fh = segre("s" if kind == "old" else "c", cut, even=kind == "split")
    weight = 1 if kind == "old" else 2
    left, right = (v, w) if kind == "old" else (x, y)
    numerator = [
        a + weight * b
        for a, b in zip(multiply(fe, left, cut), multiply(fh, right, cut), strict=True)
    ]
    denominator = [a + weight * b for a, b in zip(fe, fh, strict=True)]
    divisor = 1 + weight
    need(
        all(t % divisor == 0 for t in numerator + denominator),
        "Molien ratio integrality",
    )
    return quotient(
        [t // divisor for t in numerator], [t // divisor for t in denominator], cut
    )


@lru_cache(maxsize=128)
def _compositions(total: int, length: int) -> tuple:
    if length == 1:
        return ((total,),)
    return tuple(
        (a, *tail)
        for a in range(total + 1)
        for tail in _compositions(total - a, length - 1)
    )


def monomial_control(kind: str, grade: int, cap: int) -> dict:
    """Literal eigenmonomials of A and T2=Std,T4=sign+Std; no Molien counts."""
    need(kind in ("old", "infinity"), "literal inertia type required")
    integer(grade, 0, 8)
    need(type(cap) is int and cap in (2, 4), "literal generator cap is 2 or 4")
    degrees = (2, 2) if cap == 2 else (2, 2, 4, 4, 4)
    before = after = trace_before = trace_after = 0
    for raw in itertools.product(*(range(grade // d + 1) for d in degrees)):
        cost = sum(d * e for d, e in zip(degrees, raw, strict=True))
        if cost > grade:
            continue
        g = (*raw, 0, 0, 0) if cap == 2 else raw
        r = grade - cost
        for v in _compositions(r, 2):
            for w in _compositions(r, 3):
                if kind == "old":
                    a_parity = (v[1] + w[2]) % 2
                    gen_parity = (g[1] + g[2] + g[4]) % 2
                    keep = (a_parity + gen_parity) % 2 == 0
                    keep_after = a_parity == 0 and g[1] == g[2] == g[4] == 0
                    trace = 1
                else:
                    a_weight = v[0] - v[1] + w[1] - w[2]
                    gen_weight = g[0] - g[1] + g[3] - g[4]
                    keep = r % 2 == 0 and (a_weight + gen_weight) % 3 == 0
                    keep_after = (
                        r % 2 == 0
                        and a_weight % 3 == 0
                        and g[0] == g[1] == g[3] == g[4] == 0
                    )
                    trace = (
                        (-1) ** g[2]
                        if v[0] == v[1]
                        and w[1] == w[2]
                        and g[0] == g[1]
                        and g[3] == g[4]
                        else 0
                    )
                need(not keep_after or keep, "literal comparison lost injectivity")
                before += int(keep)
                after += int(keep_after)
                trace_before += trace * int(keep)
                trace_after += trace * int(keep_after)
    return {
        "kind": kind,
        "grade": grade,
        "cap": cap,
        "before": before,
        "after": after,
        "cokernel_dimension": before - after,
        "before_residual_trace": trace_before,
        "after_residual_trace": trace_after,
        "cokernel_residual_trace": trace_before - trace_after,
    }


def actual_branches() -> dict:
    def chi(a: int) -> int:
        a %= 7
        return 0 if a == 0 else 1 if pow(a, 3, 7) == 1 else -1

    rational = [{"u": u, "chi": chi(u)} for u in range(7) if (u**4 - 4) % 7 == 0]
    need(
        rational == [{"u": 3, "chi": -1}, {"u": 4, "chi": 1}],
        "actual rational branch source",
    )
    # Polynomial multiplication, not a new extension-field enumeration.
    need(
        [(a % 7) for a in multiply([-2, 0, 1], [-5, 0, 1], 4)] == [3, 0, 0, 0, 1],
        "discriminant factorization",
    )
    need(chi(5) == -1 and chi(-5) == 1, "quadratic branch/norm sign")
    return {
        "field": 7,
        "rational_old": rational,
        "quadratic_old": {"polynomial": [2, 0, 1], "degree": 2, "norm": 2, "chi": 1},
        "infinity_split": True,
        "base_change_49": {
            "four_rational_old_signs": [1, 1, 1, 1],
            "new_field_count_performed": False,
        },
    }


def global_ratio(field: int, cap: int, cut: int) -> list[int]:
    need(type(field) is int and field in (7, 49), "actual field panel required")
    integer(cut, 0, 32)
    out = reduced_ratio("split", cap, cut)
    plus = reduced_ratio("old", cap, cut)
    if field == 7:
        for item in (
            plus,
            reduced_ratio("old", cap, cut, -1),
            substitute(plus, 2, cut),
        ):
            out = multiply(out, item, cut)
    else:
        for _ in range(4):
            out = multiply(out, plus, cut)
    return out


def scalar_base_change_control() -> dict:
    q7, q49 = (global_ratio(q, 12, 12) for q in (7, 49))
    wrong_left, wrong_right = substitute(q49, 2, 12), multiply(q7, q7, 12)
    need(
        q7[:5] == [1, 0, 0, 0, 13] and q49[:5] == [1, 0, 0, 12, 13],
        "first boundary source coefficients",
    )
    need(
        wrong_left[4] == 0 and wrong_right[4] == 26,
        "scalar base-change counterfeit not exposed",
    )
    return {
        "Xi7": q7,
        "Xi49": q49,
        "Xi49_z_squared": wrong_left,
        "Xi7_squared": wrong_right,
        "first_mismatch": 4,
        "sheaf_base_change_failure_claimed": False,
    }


def interval_log(value: Fraction, terms: int = 24) -> tuple[Fraction, Fraction]:
    need(
        type(value) is Fraction and Fraction(1, 2) <= value <= 2,
        "log argument in [1/2,2] required",
    )
    integer(terms, 4, 48)
    if value < 1:
        low, high = interval_log(1 / value, terms)
        return -high, -low
    y = (value - 1) / (value + 1)
    partial = 2 * sum(
        (y ** (2 * k + 1) / (2 * k + 1) for k in range(terms)), Fraction(0)
    )
    error = 2 * y ** (2 * terms + 1) / ((2 * terms + 1) * (1 - y * y))
    return partial, partial + error


def add_interval(a: tuple, b: tuple) -> tuple:
    return a[0] + b[0], a[1] + b[1]


def scale_interval(a: tuple, coefficient: Fraction | int) -> tuple:
    return (
        (coefficient * a[0], coefficient * a[1])
        if coefficient >= 0
        else (coefficient * a[1], coefficient * a[0])
    )


def outward(a: tuple, bits: int = 80) -> tuple:
    integer(bits, 32, 128)
    unit = 2**bits
    return Fraction(a[0].numerator * unit // a[0].denominator, unit), Fraction(
        -((-a[1].numerator * unit) // a[1].denominator), unit
    )


def unit_log_enclosures(cut: int = 24) -> dict:
    integer(cut, 4, 32)
    x = Fraction(1, 4)
    out = {name: (Fraction(0), Fraction(0)) for name in ("V", "W", "X", "Y")}
    for row in source_rows(2 * cut)[1::2]:
        j = row["grade"] // 2
        _, b, c = row["multiplicities"]
        a = b + c
        y = x**j
        minus = scale_interval(interval_log(1 - y), -1)
        plus = interval_log(1 + y)
        tri = interval_log(1 + y + y * y)
        # Subtraction is made before outward rounding; no multiplicity inflation.
        terms = {
            "V": add_interval(scale_interval(minus, a), (-Fraction(1, 4 * j),) * 2),
            "W": add_interval(scale_interval(plus, -a), (Fraction(1, 4 * j),) * 2),
            "X": add_interval(scale_interval(minus, 2 * c), (-Fraction(1, 3 * j),) * 2),
            "Y": add_interval(scale_interval(tri, -c), (Fraction(1, 6 * j),) * 2),
        }
        for name, current in out.items():
            out[name] = add_interval(current, outward(terms[name]))
    q, v = 2 * x, 4 * x * x
    eb = q ** (cut + 1) / (3 * (cut + 1) * (1 - q))
    ec = 2 * eb + 4 * x ** (cut + 1) / (3 * (1 - x))
    quadratic = 4 * v ** (cut + 1) / ((cut + 1) * (1 - v))
    errors = {
        "V": eb + quadratic,
        "W": eb + quadratic,
        "X": 2 * ec + quadratic,
        "Y": ec + quadratic,
    }
    result = {
        name: outward((value[0] - errors[name], value[1] + errors[name]))
        for name, value in out.items()
    }
    logc49 = add_interval(
        scale_interval(interval_log(Fraction(18, 19)), 4),
        interval_log(Fraction(63, 71)),
    )
    logc49 = add_interval(
        add_interval(logc49, scale_interval(result["V"], 4)), result["X"]
    )
    return {
        "cutoff_j": cut,
        "analytic_unit_logs": result,
        "log_c49": outward(logc49),
        "tail_bounds": errors,
        "infinite_boundary_product_evaluated": False,
    }


def finite_values(cap: int, t: Fraction) -> dict:
    need(type(cap) is int and cap in (2, 4, 6, 8), "exact-value generator cap at eight")
    need(
        type(t) is Fraction and 0 <= t <= Fraction(1, 2),
        "nonnegative rational t<=1/2 required",
    )
    v = w = x = y = Fraction(1)
    for row in source_rows(cap)[1::2]:
        n = row["grade"]
        _, b, c = row["multiplicities"]
        u = t**n
        v *= (1 - u) ** (-(b + c))
        w *= (1 + u) ** (-(b + c))
        x *= (1 - u) ** (-2 * c)
        y *= (1 + u + u * u) ** (-c)
    fe = (1 + 2 * t) / (1 - t) ** 4
    fem = (1 - 2 * t) / (1 + t) ** 4
    fs = 1 / (1 - t * t) ** 2
    even = (fe + fem) / 2
    cycle = 1 / (1 - t**6)
    plus, minus = (fe * v + fs * w) / (fe + fs), (fem * v + fs * w) / (fem + fs)
    infinity = (even * x + 2 * cycle * y) / (even + 2 * cycle)
    return {
        "V": v,
        "W": w,
        "X": x,
        "Y": y,
        "Rplus": plus,
        "Rminus": minus,
        "Rinf": infinity,
    }


def finite_critical_control() -> list:
    rows = []
    for cap in (2, 4, 6, 8):
        value = finite_values(cap, Fraction(1, 2))
        need(
            value["Rplus"] == (18 * value["V"] + value["W"]) / 19,
            "critical old-branch weights",
        )
        need(value["Rminus"] == value["W"], "vanishing negative Fe branch")
        need(
            value["Rinf"] == (63 * value["X"] + 8 * value["Y"]) / 71,
            "critical infinity weights",
        )
        xi7 = (
            value["Rplus"]
            * value["Rminus"]
            * finite_values(cap, Fraction(1, 4))["Rplus"]
            * value["Rinf"]
        )
        xi49 = value["Rplus"] ** 4 * value["Rinf"]
        rows.append(
            {
                "generator_grade_cap": cap,
                "harmonic_index": cap // 2,
                "Xi7_at_half": xi7,
                "Xi49_at_half": xi49,
                "finite_source_only": True,
            }
        )
    return rows


def primitive_controls() -> list:
    out = []
    for cap in (2, 4):
        for kind in ("old", "infinity"):
            for grade in range(9):
                row = monomial_control(kind, grade, cap)
                split = local_series("old" if kind == "old" else "split", cap, 8)
                residual = local_series("old" if kind == "old" else "nonsplit", cap, 8)
                need(
                    row["before"] == split["before"][grade]
                    and row["after"] == split["after"][grade],
                    "literal basis versus full Reynolds source",
                )
                need(
                    row["cokernel_residual_trace"] == residual["difference"][grade],
                    "literal residual Frobenius trace",
                )
                out.append(row)
    old2, old4 = (monomial_control("old", 5, cap) for cap in (2, 4))
    need(
        old4["cokernel_dimension"] - old2["cokernel_dimension"] == 6,
        "T4 crossed-sector first defect",
    )
    return out


def encode(value):
    if isinstance(value, Fraction):
        return [value.numerator, value.denominator]
    if isinstance(value, dict):
        return {k: encode(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [encode(v) for v in value]
    return value


def build() -> dict:
    provenance = authenticate()
    finite, completion = dependencies()
    rows = source_rows(48)
    for row in rows:
        need(
            row == completion.source_row(row["grade"]),
            "triangular versus Mobius source mismatch",
        )
        if row["grade"] % 2 == 0:
            need(
                sum(row["multiplicities"][1:])
                == completion.anti_dimension(row["grade"]),
                "anti-invariant odd-divisor mismatch",
            )
    for kind in ("e", "s", "c"):
        need(
            generators(kind, 24, 24) == generators_newton(kind, 24, 24),
            "symmetric generator determinant versus Newton mismatch",
        )
    comparisons = []
    for kind in ("old", "split", "nonsplit"):
        for sign in (-1, 1) if kind == "old" else (1,):
            local = local_series(kind, 24, 24, sign)
            need(
                local["ratio"] == reduced_ratio(kind, 24, 24, sign),
                "full source versus reduced ratio mismatch",
            )
            if kind == "old":
                need(
                    local_series(kind, 2, 8, sign)["ratio"]
                    == finite.rational_local("old", "ratio", 8, sign),
                    "frozen finite generator mismatch",
                )
            comparisons.append({"kind": kind, "epsilon": sign, **local})
    return encode(
        {
            "schema": "infinite-extension-order-v1",
            "scope": "actual S3 F7 and F49; finite source controls and proved infinite tails",
            "source": provenance,
            "owned_sha256_lf": {
                str(p.relative_to(ROOT)).replace("\\", "/"): digest(p.read_bytes())
                for p in OWNED
            },
            "characters": rows,
            "literal_sources": primitive_controls(),
            "all_grade_formal_controls": comparisons,
            "actual_branches": actual_branches(),
            "scalar_base_change": scalar_base_change_control(),
            "unit_log_bounds": unit_log_enclosures(),
            "finite_critical_products": finite_critical_control(),
            "ordinary_boundary_Fredholm_claimed": False,
        }
    )


def typed_equal(a, b) -> bool:
    if type(a) is not type(b):
        return False
    if isinstance(a, dict):
        return a.keys() == b.keys() and all(typed_equal(a[k], b[k]) for k in a)
    if isinstance(a, list):
        return len(a) == len(b) and all(
            typed_equal(x, y) for x, y in zip(a, b, strict=True)
        )
    return a == b


def main() -> None:
    parser = argparse.ArgumentParser()
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--write", action="store_true")
    action.add_argument("--check", action="store_true")
    args = parser.parse_args()
    payload = build()
    if args.write:
        FIXTURE.write_text(
            json.dumps(payload, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
            newline="\n",
        )
    else:
        need(FIXTURE.stat().st_size < 4_000_000, "fixture byte cap")
        need(
            typed_equal(json.loads(FIXTURE.read_text(encoding="utf-8")), payload),
            "infinite source fixture changed",
        )
    print("infinite extension-order replay PASS")


if __name__ == "__main__":
    main()
