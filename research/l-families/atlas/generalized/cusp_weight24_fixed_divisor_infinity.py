"""Exact finite controls for FI; no numerical zero, pole, phase or onset claim."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import subprocess
import sys
from fractions import Fraction as F
from pathlib import Path

STEM = "cusp_weight24_fixed_divisor_infinity"
BASE = "eaa8e8263bb34b8b669f911580c9dd9e55766ba2"
DIR = "research/l-families/atlas/generalized"
ROOT = Path(__file__).resolve().parents[4]
CAPS = {
    "q_order": 64,
    "integer_bits": 4096,
    "work": 2000000,
    "json_bytes": 2000000,
    "json_nodes": 100000,
    "json_depth": 24,
    "container_length": 1024,
    "string_length": 4096,
}
D0 = 144169
DELTA2 = 576 * D0
PINS = (
    (
        "b62dfc6348661992bca659c99de226a1b6b22e14",
        f"{DIR}/RANKIN_SELBERG_QUOTIENT_GLOBAL_PARENT.md",
    ),
    (
        "b69c854d9e3dd1db7b82d95fe6f032fe47d5306b",
        f"{DIR}/CUSP_FLAG_QUOTIENT_GLOBAL_FAMILY.md",
    ),
    (BASE, f"{DIR}/CUSP_FLAG_HECKE_SOURCE_CONCENTRATION.md"),
    (BASE, f"{DIR}/cusp_flag_hecke_source_concentration.py"),
    (BASE, f"{DIR}/cusp_flag_hecke_source_concentration.json"),
    (BASE, "tests/test_cusp_flag_hecke_source_concentration.py"),
)
PRIMARY = (
    (
        "BT",
        "https://msp.org/ant/2014/8-9/ant-v8-n9-p01-s.pdf",
        "Theorem1.2 hypotheses; Proposition3.1 p2034; pp2040-2041",
    ),
    (
        "BT-correction",
        "https://msp.org/ant/2014/8-9/ant-v8-n9-x01-Correction-ZerosOfLFunctions.pdf",
        "both pages; corrected Lemma2.1 leaves Proposition3.1 intact",
    ),
    (
        "GJ",
        "https://www.numdam.org/article/ASENS_1978_4_11_4_471_0.pdf",
        "p472 adjoint normalization; Theorem9.3(3) p534",
    ),
    (
        "R",
        "https://www.maths.tcd.ie/EMIS/journals/Annals/152_1/ramak.pdf",
        "Proposition2.3.1(2) and TheoremM pp53-54",
    ),
    (
        "R-correction",
        "https://emis.muni.cz/journals/Annals/152_3/correction.pdf",
        "one-page running-header correction",
    ),
    (
        "HS",
        "https://annals.math.princeton.edu/wp-content/uploads/annals-v172-n2-p18-p.pdf",
        "section2 unitary normalization and Deligne bounds",
    ),
)
ARTIFACTS = (
    f"{DIR}/CUSP_WEIGHT24_FIXED_DIVISOR_INFINITY.md",
    f"{DIR}/{STEM}.py",
    f"{DIR}/{STEM}.sources.json",
    f"tests/test_{STEM}.py",
)


class Rejected(ValueError):
    """Malformed or unauthenticated input, also under optimized Python."""


def require(ok: bool, message: str) -> None:
    if not ok:
        raise Rejected(message)


def bounded(value: int) -> int:
    require(type(value) is int, "integer type")
    require(abs(value).bit_length() <= CAPS["integer_bits"], "integer bits")
    return value


def integer(value: object, low: int, high: int) -> int:
    require(type(value) is int and low <= value <= high, "integer domain")
    return bounded(value)


class Budget:
    def __init__(self, limit: int = CAPS["work"]):
        self.limit = integer(limit, 1, CAPS["work"])
        self.used = 0

    def charge(self, amount: int = 1) -> None:
        integer(amount, 0, CAPS["work"])
        require(self.used + amount <= self.limit, "work cap")
        self.used += amount


def rat(value: F) -> F:
    require(type(value) is F, "rational type")
    bounded(value.numerator)
    bounded(value.denominator)
    return value


def wire(value: F) -> list[int]:
    rat(value)
    return [value.numerator, value.denominator]


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
        raise Rejected("unsupported JSON type including bool/float/null")


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


def artifact_bytes(path: Path) -> bytes:
    require(path.stat().st_size <= CAPS["json_bytes"], "file byte cap")
    data = path.read_bytes()
    require(len(data) <= CAPS["json_bytes"], "read byte cap")
    return data


def read_json(path: Path) -> object:
    return decode(artifact_bytes(path))


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
        rows.append(
            {
                "commit": commit,
                "path": path,
                "git_blob": hashlib.sha1(
                    f"blob {len(raw)}\0".encode("ascii") + raw
                ).hexdigest(),
                "sha256_lf": digest(lf(raw)),
            }
        )
    return {
        "schema": "fixed-divisor-sources-v1",
        "authoring_base": BASE,
        "frozen_sources": rows,
        "primary_references": [
            {"id": key, "url": url, "passage": passage} for key, url, passage in PRIMARY
        ],
        "remote_bytes": "not_authenticated_by_offline_git_checker",
    }


def authenticate_sources() -> None:
    require(
        read_json(ROOT / DIR / f"{STEM}.sources.json") == manifest(), "source drift"
    )


def qmul(a: list[int], b: list[int], budget: Budget) -> list[int]:
    require(type(a) is list and type(b) is list, "q series type")
    n = integer(len(a) - 1, 1, CAPS["q_order"])
    require(len(b) == n + 1, "q series length")
    for x in a + b:
        bounded(x)
    budget.charge((n + 1) * (n + 2) // 2)
    out = [0] * (n + 1)
    for i in range(n + 1):
        for j in range(n + 1 - i):
            out[i + j] = bounded(out[i + j] + bounded(a[i] * b[j]))
    return out


def source_basis(order: int, budget: Budget) -> tuple[list[int], list[int]]:
    order = integer(order, 4, CAPS["q_order"])
    budget.charge(10 * (order + 1) ** 2)
    s1 = [0] * (order + 1)
    s3 = [0] * (order + 1)
    for d in range(1, order + 1):
        for n in range(d, order + 1, d):
            s1[n] += d
            s3[n] += d**3
    delta = [0, 1] + [0] * (order - 1)
    for n in range(2, order + 1):
        value = -24 * sum(s1[h] * delta[n - h] for h in range(1, n))
        require(value % (n - 1) == 0, "Delta recurrence integrality")
        delta[n] = bounded(value // (n - 1))
    e4 = [1] + [240 * s3[n] for n in range(1, order + 1)]
    cube = qmul(qmul(e4, e4, budget), e4, budget)
    b = qmul(delta, delta, budget)
    g = [bounded(x - 696 * y) for x, y in zip(qmul(delta, cube, budget), b)]
    require(g[1:3] == [1, 0] and b[1:3] == [0, 1], "canonical pivots")
    return g, b


def dseries(a: object) -> list[F]:
    require(type(a) is list and 2 <= len(a) <= CAPS["q_order"] + 1, "DS length/type")
    for x in a:
        rat(x)
    require(a[0] == 0, "DS zero index")
    return a


def dconv(a: list[F], b: list[F], budget: Budget) -> list[F]:
    dseries(a)
    dseries(b)
    require(len(a) == len(b), "DS lengths")
    n = len(a) - 1
    budget.charge((n + 1) ** 2)
    out = [F(0)] * (n + 1)
    for i in range(1, n + 1):
        for j in range(1, n // i + 1):
            out[i * j] = rat(out[i * j] + rat(a[i] * b[j]))
    return out


def square_lift(a: list[F], budget: Budget) -> list[F]:
    dseries(a)
    n = len(a) - 1
    zeta2 = [F(int(i > 0 and math.isqrt(i) ** 2 == i)) for i in range(n + 1)]
    return dconv(zeta2, a, budget)


def primepowers(order: int, u: list[F], c: list[F], budget: Budget) -> list[dict]:
    order = integer(order, 2, CAPS["q_order"])
    dseries(u)
    dseries(c)
    require(len(u) == len(c) == order + 1, "local prefix lengths")
    rows = []
    for p in range(2, order + 1):
        if any(p % d == 0 for d in range(2, math.isqrt(p) + 1)):
            continue
        # The tensor characteristic polynomial from the two Hecke traces.
        polynomial = [F(1), -c[p], 2 * u[p] - 2, -c[p], F(1)]
        inverse = [F(1)]
        powers = [1]
        while powers[-1] * p <= order:
            powers.append(powers[-1] * p)
            e = len(powers) - 1
            budget.charge(4)
            inverse.append(
                rat(
                    -sum(
                        (
                            polynomial[j] * inverse[e - j]
                            for j in range(1, min(e, 4) + 1)
                        ),
                        F(),
                    )
                )
            )
        for power, value in zip(powers, inverse):
            require(c[power] == value, "complete tensor prime-power recurrence")
        rows.append(
            {
                "prime": p,
                "powers": powers,
                "denominator": list(map(wire, polynomial)),
                "coefficients": list(map(wire, inverse)),
            }
        )
    return rows


def scalar_controls(budget: Budget) -> dict:
    budget.charge(10000)
    targets = []
    for label, cv in (("pole", F(5, 2)), ("zero", F(2)), ("cancelled", F(1))):
        z, x, y = F(1), F(1), F(1 if label == "cancelled" else 4)
        h, n = z * (x + y) - 2 * cv, z * z * x * y - cv * cv
        require(
            4 * n == h * (z * (x + y) + 2 * cv) - z * z * (x - y) ** 2, "Schur identity"
        )
        targets.append(
            {
                "purpose": label,
                "tuple": list(map(wire, (z, x, y, cv))),
                "H": wire(h),
                "N": wire(n),
            }
        )
    require(targets[0]["H"] == [0, 1] and targets[0]["N"] == [-9, 4], "pole target")
    require(targets[1]["H"] == [1, 1] and targets[1]["N"] == [0, 1], "zero target")
    valuations = [
        [m, r, max(m - r, 0), max(m - 2 * r, 0)]
        for m in range(1, 13)
        for r in range(13)
    ]
    # Exact upper controls for FI13 at a=2,M=2^j, using log(2)<1.
    tails = []
    for degree in (4, 8):
        for j in range(1, 17):
            bound = F(2, 2**j) * sum(
                math.comb(degree - 1, h)
                * (1 + j) ** (degree - 1 - h)
                * math.factorial(h)
                for h in range(degree)
            )
            tails.append([degree, j, wire(bound)])
    return {
        "targets": targets,
        "valuation_rows_m_r_poleJoverH_poleQ": valuations,
        "tail_majorant_a2_M2powerj": tails,
        "degrees": [1, 3, 3, 4],
        "coefficient_majorants": [[4, 4], [2, 8]],
        "prime_cutoff": [3, 2],
        "target_annulus_radius": [4, 1],
        "arithmetic": "MIXED: EXACT_RATIONAL / CERTIFIED_INTEGER_COVERAGE",
        "rounding": "none",
        "analytic_imports_machine_certified": "no",
    }


def payload() -> dict:
    budget = Budget()
    order = CAPS["q_order"]
    g, b = source_basis(order, budget)
    frozen = decode(
        git_bytes(f"{BASE}:{DIR}/cusp_flag_hecke_source_concentration.json")
    )
    source = frozen["q_rows"][0]
    require(
        source["k"] == 24 and source["basis"] == [g[:13], b[:13]], "frozen native chart"
    )
    t2 = [[g[2], b[2]], [g[4] + 2**23 * g[1], b[4] + 2**23 * b[1]]]
    require(t2 == [[0, 1], [20468736, 1080]], "native T2")
    for n in range(1, order // 2 + 1):
        for a, col in ((g, 0), (b, 1)):
            require(
                a[2 * n] + (2**23 * a[n // 2] if n % 2 == 0 else 0)
                == t2[0][col] * g[n] + t2[1][col] * b[n],
                "held-out T2",
            )
    u, v, c, gg, bb, gb = ([F(0)] for _ in range(6))
    for n in range(1, order + 1):
        a, e = g[n] + 540 * b[n], 12 * b[n]
        u.append(F(a * a + D0 * e * e, n**23))
        v.append(F(2 * a * e, n**23))
        c.append(F(a * a - D0 * e * e, n**23))
        gg.append(F(g[n] ** 2, n**23))
        bb.append(F(b[n] ** 2, n**23))
        gb.append(F(g[n] * b[n], n**23))
    u, v, c, gg, bb, gb = (square_lift(a, budget) for a in (u, v, c, gg, bb, gb))
    h = [rat(2 * x - 2 * y) for x, y in zip(u, c)]
    ncoef = [
        rat(x - D0 * y - z)
        for x, y, z in zip(
            dconv(u, u, budget), dconv(v, v, budget), dconv(c, c, budget)
        )
    ]
    require(h == [DELTA2 * x for x in bb], "source denominator identity")
    require(
        ncoef
        == [
            DELTA2 * (x - y)
            for x, y in zip(dconv(gg, bb, budget), dconv(gb, gb, budget))
        ],
        "complete source determinant identity",
    )
    require(
        h[1] == ncoef[1] == 0 and h[2] == ncoef[2] == F(1297521, 131072),
        "leading coefficient",
    )
    local = primepowers(order, u, c, budget)
    controls = scalar_controls(budget)
    out = {
        "schema": "weight24-fixed-divisor-infinity-v1",
        "authoring_base": BASE,
        "caps": CAPS.copy(),
        "weight": 24,
        "dimension": 2,
        "q_order": order,
        "basis": [g, b],
        "T2": t2,
        "held_out_T2_through": order // 2,
        "eigen_equation": [1, -1080, -20468736],
        "quadratic_field": D0,
        "eigenvalue_alpha_pairs": [[540, 12], [540, -12]],
        "delta_squared": DELTA2,
        "square_difference_sqrt_coefficient": 25920,
        "dirichlet_coefficients": [
            {
                "n": n,
                "diag_rational": wire(u[n]),
                "diag_sqrt": wire(v[n]),
                "cross": wire(c[n]),
                "H": wire(h[n]),
                "N": wire(ncoef[n]),
            }
            for n in range(1, order + 1)
        ],
        "local_tensor_rows": local,
        "controls": controls,
        "scope": "fixed_weight24_separate_distinct_zero_pole_linear_lower_bounds",
        "not_claimed": [
            "explicit_eta",
            "effective_onset",
            "certified_divisor_location",
            "simplicity",
            "unsigned_asymptotic",
            "RH",
            "new_automorphic_representation",
        ],
        "work_used": budget.used,
    }
    typed(out)
    return out


def fixture() -> dict:
    authenticate_sources()
    out = payload()
    out["artifact_sha256_lf"] = {
        p: digest(lf(artifact_bytes(ROOT / p))) for p in ARTIFACTS
    }
    out["payload_sha256"] = digest(encoded(out))
    require(len(encoded(out)) <= CAPS["json_bytes"], "output cap")
    return out


def validate(value: object) -> None:
    typed(value)
    require(
        type(value) is dict and value == fixture(),
        "strict authenticated reconstruction mismatch",
    )


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
                "PASS: 64 complete coefficients, guarded targets, 6 source pins, 4 artifacts"
            )
            print("fixture_sha256_lf=" + digest(lf(artifact_bytes(path))))
        return 0
    except (Rejected, OSError, subprocess.SubprocessError) as exc:
        print(f"REJECTED: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
