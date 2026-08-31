"""Preregistered exact-quadratic critical transport at twenty-six actual Xi nodes."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import subprocess
import sys
import sysconfig
from fractions import Fraction as Q
from pathlib import Path

import xi_fixed_lambda_heldout_alignment as ha
from flint import acb, arb, ctx

oa = ha.oa
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
STEM = "xi_quadratic_critical_transport"
NOTE = HERE / "XI_QUADRATIC_CRITICAL_TRANSPORT.md"
MANIFEST = HERE / (STEM + ".sources.json")
FIXTURE = HERE / (STEM + ".json")
TEST = ROOT / "tests" / ("test_" + STEM + ".py")
BASE = "64165b8c805d182dbc43f2e5855e64a86cf1aaf9"
PREREG = "9162b5ea6112c346e200c044f9f3f2324ed4fc59"
REFINEMENT = "24c52d25f9cf606f5db9c40e4919a78c196b9565"
TIMEOUT_PREREG = "edb7d1ccffdc83c8e2b95e533da078508d009990"
BROAD_HISTORY_SHA256 = (
    "20e3b2d04d62b9b26119c77613a68fc9f4d76eba4be09bdee28d4f4bd7d8cd2e"
)
NATIVE_TIMEOUT = 30
EPS = Q(1, 2**120)
OUTER = Q(7, 8)
TERMS = 32
TIERS = (256, 512, 1024)
RATIOS = (Q(1, 16), Q(1, 8), Q(1, 4), Q(1, 2), Q(3, 4))
MAX_BYTES, MAX_SOURCE_BYTES = 12_000_000, 24_000_000
BINDINGS = [
    {
        "commit": BASE,
        "path": "research/exploratory/XI_FIXED_LAMBDA_HELDOUT_ALIGNMENT.md",
        "git_blob": "3e9a15404532e72255acb3e55751987eb29a4043",
        "sha256_lf": "592c8313e5e46c68af6e5b3b9aa46c2724e84f51394cac3bd6934d0139eb26b7",
    },
    {
        "commit": BASE,
        "path": "research/exploratory/xi_fixed_lambda_heldout_alignment.py",
        "git_blob": "b472d18a3404ceebbde76e02bd6346678f4bdcfa",
        "sha256_lf": "1ad06f941f1c24f4732ef4db772c915f8bdf080abbdf2b8754816ea70fff01f0",
    },
    {
        "commit": BASE,
        "path": "research/exploratory/xi_fixed_lambda_heldout_alignment.json",
        "git_blob": "e5f1bc4e97be9b92f715e24b3670d64171071334",
        "sha256_lf": "eb6464cc2eed61f8aecf2eff6e2f36a5ee5f850252237f0f95bd9b0e4e51b206",
    },
    {
        "commit": BASE,
        "path": "research/exploratory/xi_fixed_lambda_heldout_alignment.sources.json",
        "git_blob": "0dac7784b5c2a912d44c479e069e045b9f1b85e1",
        "sha256_lf": "3bb7fdccc56b8e7ac2e3c6fb1c0a62874645893683e8d626f4cdca8becdf9ad6",
    },
    {
        "commit": BASE,
        "path": "tests/test_xi_fixed_lambda_heldout_alignment.py",
        "git_blob": "c244417d71e8f31d59d3bbafb29543643bbb8c06",
        "sha256_lf": "8ece2393f6039ae3ea42b137cd079ef727a0db932de440f9a641020c9a0b0392",
    },
    {
        "commit": PREREG,
        "path": "research/exploratory/XI_QUADRATIC_CRITICAL_TRANSPORT.md",
        "git_blob": "171f69088e6d4becd2043cbdf14a3581c364846e",
        "sha256_lf": "66c966140b2c4ec60cf9b4b47f00710dc8caf85b6a38a3cd2a07f0f26be56ccd",
    },
    {
        "commit": REFINEMENT,
        "path": "research/exploratory/XI_QUADRATIC_CRITICAL_TRANSPORT.md",
        "git_blob": "d9bbf53508c079e2558526baaa6a77e86249e71d",
        "sha256_lf": "d6483e2ca82beb4d889842a635fdfd30688e51b06ad7327f222d3164864328ba",
    },
    {
        "commit": TIMEOUT_PREREG,
        "path": "research/exploratory/XI_QUADRATIC_CRITICAL_TRANSPORT.md",
        "git_blob": "679022e3a03c263270aba6ebd61548080ebca71a",
        "sha256_lf": "768df469cd46943918fba844f392be6f8a762a5a9dd8898007d083b7ecf9ad4a",
    },
]
CONTRACT = {
    "primitive": "actual unrescaled Xi(1/2+iz), g=f5, one fixed calibrated lambda_(64), not lambda=64",
    "panel": "exactly26 new HA nodes in frozen order; boxes256/512/1024 only",
    "critical": "real Newton from HA real center;24steps/256bits;2^-170stop;2^-180center;2^-120certification disc",
    "ratios": [oa.pair(q) for q in RATIOS],
    "tiers": list(TIERS),
    "third_derivative": "actual f8: direct full square AND32term Taylor/Cauchy with fixed outer radius7/8 including real critical uncertainty",
    "outer_refinement": "post-scout fixed16x16 complete SAME-rectangle cover; every256cells replayed; original direct failure retained",
    "broad_history": "pinned canonical environmental attempt ledger;30s wallcap only for broad outer-Xi and broad f8; historical unresolved supplies no bound; every historical success freshly reproduced",
    "geometry": "r=ratio*y exact unknown radius; upper-error/lower-margin guards and whole HA rectangle containment",
    "linear": "originalHA3 independently tested on2q region at same criticalpoint/lambda",
    "postresult_diagnostic": "same26 certified criticalpoints only,1024bits; point|f8(t)| lower may obstruct the sufficient inequality, otherwise unresolved; not a transport certificate",
    "domain": "20<Re z<1100,-1<Im z<2, unchanged HA wrapper; series cap40",
    "arithmetic_class": "MIXED",
    "arithmetic_components": [
        "DIRECTED_BALL_ENCLOSURES",
        "EXACT_RATIONAL",
        "CERTIFIED_INTEGER_COVERAGE",
    ],
    "rounding": "FLINT outward balls; exact rational endpoints and strict comparisons; Newton midpoints scout only",
    "source_quantifiers": "finite local actual-source certificates only; quadratic theorem alone gives no C5/noncommon guarantee",
    "exclusions": "no extra boxes, cofinal transport, uniform asymptotics, raw-alignment eta, physical capture or RH",
    "caps": {
        "nodes": 26,
        "newton_steps": 24,
        "series_cap": 40,
        "taylor_terms": 32,
        "outer_cover_cells": 256,
        "broad_tasks": 546,
        "json_bytes": MAX_BYTES,
        "source_bytes": MAX_SOURCE_BYTES,
        "json_nodes": 300000,
        "json_depth": 24,
        "container": 20000,
        "string": 4096,
        "integer_bits": 4096,
    },
    "trust": "source-pinned FLINT special functions and native binary lock, not formal verification",
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def validate_tree(value, depth=0, visits=None):
    visits = [0] if visits is None else visits
    visits[0] += 1
    require(depth <= 24 and visits[0] <= 300000, "JSON depth/node cap")
    if value is None or type(value) is bool:
        return
    if type(value) is str:
        require(len(value) <= 4096 and value.isascii(), "JSON string cap/ASCII")
        return
    if type(value) is int:
        require(value.bit_length() <= 4096, "JSON integer bit cap")
        return
    require(
        type(value) in (dict, list) and len(value) <= 20000, "JSON container type/cap"
    )
    if type(value) is dict:
        require(
            all(type(k) is str and len(k) <= 4096 and k.isascii() for k in value),
            "JSON key type/cap",
        )
        children = value.values()
    else:
        children = value
    for child in children:
        validate_tree(child, depth + 1, visits)


def canonical(value):
    validate_tree(value)
    raw = json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode()
    require(len(raw) <= MAX_BYTES, "JSON byte cap")
    return raw


def decode(raw):
    require(type(raw) is bytes and len(raw) <= MAX_BYTES, "input bytes cap/type")

    def reject(_):
        raise ValueError("noninteger JSON numeric primitive")

    value = json.loads(
        raw,
        object_pairs_hook=oa.pairs_unique,
        parse_float=reject,
        parse_constant=reject,
    )
    validate_tree(value)
    return value


def lf(raw):
    require(type(raw) is bytes and len(raw) <= MAX_SOURCE_BYTES, "source byte cap")
    return ha.lf(raw)


def manifest():
    return {
        "schema": STEM + "-sources-v1",
        "authoring_base": BASE,
        "preregistration": PREREG,
        "post_scout_refinement": REFINEMENT,
        "timeout_preregistration": TIMEOUT_PREREG,
        "broad_history_sha256": BROAD_HISTORY_SHA256,
        "frozen_sources": BINDINGS,
        "runtime": oa.RUNTIME,
        "contract": CONTRACT,
        "documentation": ha.manifest()["documentation"],
    }


def authenticate():
    require(
        canonical(decode(MANIFEST.read_bytes())) == canonical(manifest()),
        "manifest mismatch",
    )
    ha.authenticate()
    for j, binding in enumerate(BINDINGS):
        raw = oa.read_source(binding)
        require(len(raw) <= MAX_SOURCE_BYTES, "frozen source cap")
        blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        require(
            blob == binding["git_blob"] and oa.digest(lf(raw)) == binding["sha256_lf"],
            "source mismatch",
        )
        if j < 5:
            require(
                oa.digest(lf((ROOT / binding["path"]).read_bytes()))
                == binding["sha256_lf"],
                "local HA executable/source drift",
            )


def parent_panel():
    raw = oa.read_source(BINDINGS[2])
    require(oa.digest(lf(raw)) == BINDINGS[2]["sha256_lf"], "parent fixture lock")
    rows = [
        r for r in ha.load_json(raw)["roots"] if r["box_center"] in (256, 512, 1024)
    ]
    require(len(rows) == 26, "26-node panel")
    require(
        [sum(r["box_center"] == w for r in rows) for w in (256, 512, 1024)]
        == [8, 9, 9],
        "panel box counts",
    )
    require(
        rows
        == sorted(rows, key=lambda r: (r["box_center"], oa.unpair(r["center"][0]))),
        "fixed parent order",
    )
    return rows


def scalar_upper(value):
    require(type(value) is arb and value.is_finite(), "finite upper real")
    return oa.endpoint(value.upper())


def scalar_lower(value):
    require(type(value) is arb and value.is_finite(), "finite lower real")
    return oa.endpoint(value.lower())


def region(center, radius):
    center, radius = oa.rational(center), oa.rational(radius)
    require(radius > 0, "positive region radius")
    return acb(arb(oa.qarb(center), oa.qarb(radius + EPS)), arb(0, oa.qarb(radius)))


class ReplayFailure(RuntimeError):
    """A formerly successful bound failed replay; never a scientific failure."""


def native_task(task):
    require(
        type(task) is dict and set(task) == {"route", "center", "radius", "bits"},
        "native task shape",
    )
    require(task["route"] in ("outer_direct", "third_direct"), "native route")
    require(type(task["bits"]) is int and task["bits"] in TIERS, "native precision")
    center, radius = oa.unpair(task["center"]), oa.unpair(task["radius"])
    require(20 < center < 1100 and 0 < radius < 2, "native task domain cap")
    require(task["route"] != "outer_direct" or radius == OUTER, "fixed outer radius")
    return center, radius


def native_worker(task):
    center, radius = native_task(task)
    try:
        with ha.precision(task["bits"]):
            z = region(center, radius)
            value = (
                ha.xi_value(z) if task["route"] == "outer_direct" else ha.xi_jet(z)[8]
            )
            upper = oa.endpoint(value.abs_upper())
            return {"status": "PASS", "upper": oa.pair(upper)}
    except (ValueError, ZeroDivisionError, OverflowError) as error:
        return {"status": "UNRESOLVED_NATIVE", "reason": str(error)}


def execute_native(task):
    native_task(task)
    # Run the real CPython binary, not the Windows venv redirector: killing
    # a timed-out redirector could leave its native child holding stdout.
    boot = (
        "import sys,runpy;"
        + "sys.path.insert(0,"
        + repr(sysconfig.get_path("purelib"))
        + ");"
        + "sys.path.insert(0,"
        + repr(str(HERE))
        + ");"
        + "sys.argv=["
        + repr(__file__)
        + ",'--native-task'];"
        + "runpy.run_path("
        + repr(__file__)
        + ",run_name='__main__')"
    )
    try:
        run = subprocess.run(
            [
                sys._base_executable,
                "-B",
                *(["-O"] if sys.flags.optimize else []),
                "-c",
                boot,
            ],
            input=canonical(task),
            capture_output=True,
            timeout=NATIVE_TIMEOUT,
            check=False,
        )
    except subprocess.TimeoutExpired:
        return {
            "status": "TIMEOUT_UNRESOLVED",
            "reason": "historical30s wallcap; environmental, not mathematical",
        }
    if run.returncode != 0:
        return {
            "status": "UNRESOLVED_WORKER",
            "reason": "native subprocess did not complete normally",
        }
    result = decode(run.stdout)
    validate_native_result(result)
    return result


def validate_native_result(result):
    require(type(result) is dict and "status" in result, "native result shape")
    if result["status"] == "PASS":
        require(set(result) == {"status", "upper"}, "native success shape")
        require(oa.unpair(result["upper"]) >= 0, "native nonnegative upper")
    else:
        require(
            result["status"]
            in ("UNRESOLVED_NATIVE", "TIMEOUT_UNRESOLVED", "UNRESOLVED_WORKER"),
            "native historical status",
        )
        require(
            set(result) == {"status", "reason"} and type(result["reason"]) is str,
            "native unresolved shape",
        )
    canonical(result)


class NativeRunner:
    def __init__(self, history=None):
        self.collecting = history is None
        self.entries, self.used = {}, set()
        if history is not None:
            require(
                type(history) is dict
                and set(history) == {"schema", "wallcap_seconds", "entries"},
                "history shape",
            )
            require(
                history["schema"] == STEM + "-environmental-history-v1",
                "history schema",
            )
            require(
                type(history["wallcap_seconds"]) is int
                and history["wallcap_seconds"] == NATIVE_TIMEOUT,
                "historical wallcap",
            )
            require(
                oa.digest(canonical(history)) == BROAD_HISTORY_SHA256,
                "frozen environmental history pin",
            )
            require(
                type(history["entries"]) is list and len(history["entries"]) <= 546,
                "history task cap",
            )
            for entry in history["entries"]:
                require(
                    type(entry) is dict
                    and set(entry) == {"task_id", "task", "outcome"},
                    "history entry shape",
                )
                native_task(entry["task"])
                validate_native_result(entry["outcome"])
                key = oa.digest(canonical(entry["task"]))
                require(
                    entry["task_id"] == key and key not in self.entries,
                    "history task identity/duplicate",
                )
                self.entries[key] = entry
            require(
                list(self.entries) == sorted(self.entries), "canonical history ordering"
            )

    def evaluate(self, route, center, radius):
        task = {
            "route": route,
            "center": oa.pair(center),
            "radius": oa.pair(radius),
            "bits": ctx.prec,
        }
        native_task(task)
        key = oa.digest(canonical(task))
        if key not in self.used:
            if self.collecting:
                require(len(self.entries) < 546, "native task cap")
                self.entries[key] = {
                    "task_id": key,
                    "task": task,
                    "outcome": execute_native(task),
                }
            else:
                if key not in self.entries:
                    raise ReplayFailure(
                        "new task absent from frozen environmental history"
                    )
                old = self.entries[key]["outcome"]
                if old["status"] == "PASS" and canonical(
                    execute_native(task)
                ) != canonical(old):
                    raise ReplayFailure(
                        "historically successful native bound did not reproduce"
                    )
            self.used.add(key)
        return dict(self.entries[key]["outcome"])

    def history(self):
        require(
            self.used == set(self.entries),
            "every historical task requested by fresh panel",
        )
        return {
            "schema": STEM + "-environmental-history-v1",
            "wallcap_seconds": NATIVE_TIMEOUT,
            "entries": [self.entries[k] for k in sorted(self.entries)],
        }


def newton(parent):
    x = oa.unpair(parent["center"][0])
    out = {"start": oa.pair(x), "steps": []}
    with ha.precision(256):
        for step in range(24):
            try:
                require(20 < x < 1100, "Newton domain")
                jets = ha.xi_jet(acb(oa.qarb(x)))
                f6, f7 = jets[6].real, jets[7].real
                require(
                    jets[6].imag.contains(0) and jets[7].imag.contains(0),
                    "real source symmetry enclosure",
                )
                require(f7.abs_lower() > 0, "Newton derivative obstruction")
                correction = f6 / f7
                next_x = oa.endpoint((oa.qarb(x) - correction).mid())
                out["steps"].append(
                    {
                        "index": step,
                        "x": oa.pair(x),
                        "correction": oa.rbounds(correction),
                        "next": oa.pair(next_x),
                    }
                )
                x = next_x
                if correction.abs_upper() < oa.qarb(Q(1, 2**170)):
                    out.update(
                        status="CONVERGED_SCOUT",
                        center=oa.pair(Q(round(x * 2**180), 2**180)),
                    )
                    return out
            except (ValueError, ZeroDivisionError, OverflowError) as error:
                out.update(status="FAILED", reason=str(error))
                return out
    out.update(status="FAILED", reason="24-step iteration limit")
    return out


def certify_critical(center):
    center = oa.rational(center)
    attempts = []
    for bits in TIERS:
        try:
            with ha.precision(bits):
                point = ha.xi_jet(acb(oa.qarb(center)))
                square = acb(arb(oa.qarb(center), oa.qarb(EPS)), arb(0, oa.qarb(EPS)))
                around = ha.xi_jet(square)
                a = oa.endpoint(point[6].abs_upper())
                d = oa.endpoint(point[7].abs_lower())
                m = oa.endpoint(around[8].abs_upper())
                left, right = a + m * EPS**2 / 2, d * EPS
                record = {
                    "bits": bits,
                    "residual": oa.pair(a),
                    "derivative_lower": oa.pair(d),
                    "second_upper": oa.pair(m),
                    "left": oa.pair(left),
                    "right": oa.pair(right),
                }
                if left < right:
                    record["status"] = "PASS"
                    attempts.append(record)
                    return {
                        "center": oa.pair(center),
                        "radius": oa.pair(EPS),
                        "simple_real_critical": True,
                        "attempts": attempts,
                    }
                record.update(status="FAILED", reason="critical Rouche inequality")
                attempts.append(record)
        except (ValueError, ZeroDivisionError, OverflowError) as error:
            attempts.append({"bits": bits, "status": "FAILED", "reason": str(error)})
    return {
        "center": oa.pair(center),
        "radius": oa.pair(EPS),
        "simple_real_critical": False,
        "attempts": attempts,
    }


def taylor_tail(m, h, outer=OUTER, terms=TERMS):
    m, h, outer = map(oa.rational, (m, h, outer))
    require(
        type(terms) is int and terms == TERMS and outer == OUTER, "fixed Cauchy design"
    )
    require(m >= 0 and 0 <= h < outer, "Cauchy radius guard")
    # Directed ball powers prevent denominator blow-up from repeated exact
    # powers of high-precision dyadics; the returned endpoint is exact.
    x = oa.qarb(h) / oa.qarb(outer)
    result = oa.qarb(m) * math.factorial(8) / oa.qarb(outer) ** 8
    result *= math.comb(terms + 8, 8) * x**terms / (1 - x) ** 9
    return scalar_upper(result)


def outer_cells(center):
    center = oa.rational(center)
    for i in range(16):
        left = center - OUTER - EPS + Q(i, 8) * (OUTER + EPS)
        right = center - OUTER - EPS + Q(i + 1, 8) * (OUTER + EPS)
        for j in range(16):
            bottom = -OUTER + Q(j, 8) * OUTER
            top = -OUTER + Q(j + 1, 8) * OUTER
            yield i, j, left, right, bottom, top


def outer_cover(center):
    stream = hashlib.sha256()
    failed = []
    maximum = Q(0)
    finite = 0
    for i, j, left, right, bottom, top in outer_cells(center):
        item = {
            "i": i,
            "j": j,
            "rectangle": [oa.pair(q) for q in (left, right, bottom, top)],
        }
        try:
            cell = acb(
                arb(oa.qarb((left + right) / 2), oa.qarb((right - left) / 2)),
                arb(oa.qarb((bottom + top) / 2), oa.qarb((top - bottom) / 2)),
            )
            upper = oa.endpoint(ha.xi_value(cell).abs_upper())
            item.update(status="PASS", upper=oa.pair(upper))
            finite += 1
            maximum = max(maximum, upper)
        except (ValueError, ZeroDivisionError, OverflowError) as error:
            item.update(status="FAILED", reason=str(error))
            failed.append([i, j, str(error)])
        stream.update(canonical(item) + b"\n")
    record = {
        "cells_attempted": 256,
        "finite_cells": finite,
        "failed_cells": failed,
        "ordered_cell_stream_sha256": stream.hexdigest(),
    }
    if finite == 256:
        record.update(status="PASS", upper=oa.pair(maximum))
        return record, maximum
    record.update(status="FAILED", reason="nonfinite outer-cover cell")
    return record, None


def prepared(center, runner):
    t = arb(oa.qarb(center), oa.qarb(EPS))
    coeff = ha.xi_series(acb(t), 40)
    require(all(v.imag.contains(0) for v in coeff), "real Taylor coefficients")
    lam = ha.fixed_lambda()
    a, c = (coeff[5] * math.factorial(5)).real, (coeff[7] * math.factorial(7)).real
    data = {
        "bits": ctx.prec,
        "T": oa.rbounds(t),
        "lambda": oa.rbounds(lam),
        "a": oa.rbounds(a),
        "c": oa.rbounds(c),
        "coefficient_modulus_upper_8_to39": [
            oa.pair(oa.endpoint(v.abs_upper())) for v in coeff[8:]
        ],
    }
    choices = []
    outer_record = {}
    direct = runner.evaluate("outer_direct", center, OUTER)
    outer_record["direct"] = direct
    if direct["status"] == "PASS":
        upper = oa.unpair(direct["upper"])
        choices.append((upper, "direct"))
    cover, bound = outer_cover(center)
    outer_record["fixed_cover"] = cover
    if bound is not None:
        choices.append((bound, "fixed_cover"))
    upper = None
    if choices:
        upper, method = min(choices)
        outer_record.update(
            status="PASS",
            chosen_method=method,
            upper=oa.pair(upper),
            radius=oa.pair(OUTER),
        )
    else:
        outer_record.update(
            status="FAILED",
            reason="both outer scalar bounds failed",
            radius=oa.pair(OUTER),
        )
    data["outer_scalar_bound"] = outer_record
    require(a * c < 0, "critical opposite signs")
    q = -a / (lam * c)
    require(q > 0, "positive q")
    data["q"] = oa.rbounds(q)
    return data, t, lam, a, c, q, coeff, upper


def third_bound(center, h, coeff, outer_upper, runner):
    h = oa.rational(h)
    require(h > 0, "positive third derivative radius")
    record = {"radius_upper": oa.pair(h)}
    choices = []
    direct = runner.evaluate("third_direct", center, h)
    record["direct"] = direct
    if direct["status"] == "PASS":
        choices.append((oa.unpair(direct["upper"]), "direct"))
    try:
        require(outer_upper is not None, "missing outer scalar bound")
        tail = taylor_tail(outer_upper, h)
        polynomial_ball = arb(0)
        for n in reversed(range(TERMS)):
            polynomial_ball = polynomial_ball * oa.qarb(h)
            polynomial_ball += coeff[n + 8].abs_upper() * (
                math.factorial(n + 8) // math.factorial(n)
            )
        polynomial = scalar_upper(polynomial_ball)
        bound = oa.rational(polynomial + tail)
        record["taylor_cauchy"] = {
            "status": "PASS",
            "polynomial": oa.pair(polynomial),
            "tail": oa.pair(tail),
            "upper": oa.pair(bound),
        }
        choices.append((bound, "taylor_cauchy"))
    except (ValueError, ZeroDivisionError, OverflowError) as error:
        record["taylor_cauchy"] = {"status": "FAILED", "reason": str(error)}
    if choices:
        bound, method = min(choices)
        record.update(status="PASS", chosen_method=method, upper=oa.pair(bound))
        return record, oa.qarb(bound)
    record.update(status="FAILED", reason="both actual third-derivative routes failed")
    return record, None


def parent_rectangle(parent):
    x, y = map(oa.unpair, parent["center"])
    radius = oa.unpair(parent["radius"])
    return acb(arb(oa.qarb(x), oa.qarb(radius)), arb(oa.qarb(y), oa.qarb(radius)))


def quadratic_attempt(center, parent, prep, ratio, runner=None):
    require(type(ratio) is Q and ratio in RATIOS, "declared radius ratio")
    _, t, lam, _, c, q, coeff, outer_upper = prep
    record = {
        "bits": ctx.prec,
        "ratio": oa.pair(ratio),
        "transport_certified": False,
        "parent_matched": False,
    }
    try:
        require(2 * q < lam, "quadratic discriminant 2q<lambda")
        d = (lam * lam - 2 * lam * q).sqrt()
        y = 2 * lam * q / (lam + d)
        r = oa.qarb(ratio) * y
        require(r > 0 and r < y and r < 2 * d, "quadratic radius geometry")
        h = scalar_upper(y + r)
        record.update(d=oa.rbounds(d), y=oa.rbounds(y), radius=oa.rbounds(r))
        bounds, m3 = third_bound(center, h, coeff, outer_upper, runner)
        record["third_derivative"] = bounds
        require(m3 is not None, "no valid third-derivative bound")
        left = m3 * (y + r) ** 2 * ((y + r) / 6 + lam / 2)
        right = abs(c) * r * (d - r / 2)
        error_upper, margin_lower = scalar_upper(left), scalar_lower(right)
        displacement = oa.endpoint((parent_rectangle(parent) - acb(t, y)).abs_upper())
        radius_lower = scalar_lower(r)
        record.update(
            error_upper=oa.pair(error_upper),
            margin_lower=oa.pair(margin_lower),
            parent_displacement_upper=oa.pair(displacement),
            radius_lower=oa.pair(radius_lower),
        )
        record["transport_certified"] = error_upper < margin_lower
        record["parent_matched"] = displacement < radius_lower
        require(record["transport_certified"], "quadratic Rouche inequality")
        require(record["parent_matched"], "whole HA rectangle not contained")
        record["status"] = "PASS"
    except (ValueError, ZeroDivisionError, OverflowError) as error:
        record.update(status="FAILED", reason=str(error))
    return record


def linear_attempt(center, parent, prep, runner):
    _, t, lam, _, c, q, coeff, outer_upper = prep
    record = {"bits": ctx.prec, "transport_certified": False, "parent_matched": False}
    try:
        bounds, m3 = third_bound(
            center, scalar_upper(2 * q), coeff, outer_upper, runner
        )
        record["third_derivative"] = bounds
        require(m3 is not None, "no valid linear third-derivative bound")
        delta = 2 * q / lam + m3 / abs(c) * (4 * q * q / (3 * lam) + 2 * q)
        r = 2 * delta * q
        displacement = oa.endpoint((parent_rectangle(parent) - acb(t, q)).abs_upper())
        record.update(
            delta=oa.rbounds(delta),
            radius=oa.rbounds(r),
            parent_displacement_upper=oa.pair(displacement),
            radius_lower=oa.pair(scalar_lower(r)),
        )
        record["transport_certified"] = bool(delta < oa.qarb(Q(1, 2)))
        record["parent_matched"] = displacement < scalar_lower(r)
        require(record["transport_certified"], "HA linear Delta<1/2")
        require(
            record["parent_matched"], "whole HA rectangle not contained in linear disc"
        )
        record["status"] = "PASS"
    except (ValueError, ZeroDivisionError, OverflowError) as error:
        record.update(status="FAILED", reason=str(error))
    return record


def node_record(index, parent, runner):
    oa.integer(index, 0, 25)
    nums = [oa.unpair(v) * 2**180 for v in parent["center"]]
    require(all(v.denominator == 1 for v in nums), "frozen dyadic parent center")
    rebuilt, box, theta = ha.root_record(
        parent["box_center"], *(v.numerator for v in nums)
    )
    require(
        box is not None
        and theta is not None
        and canonical(rebuilt) == canonical(parent),
        "fresh literal HA root reconstruction",
    )
    record = {
        "index": index,
        "box_center": parent["box_center"],
        "HA_center": parent["center"],
        "HA_radius": parent["radius"],
        "HA_record_sha256": oa.digest(canonical(rebuilt)),
        "newton": newton(parent),
        "quadratic": [{"ratio": oa.pair(q), "attempts": []} for q in RATIOS],
        "linear": {"attempts": []},
        "jet_tiers": [],
    }
    if record["newton"]["status"] != "CONVERGED_SCOUT":
        record["status"] = "NO_CRITICAL_CANDIDATE"
        return record
    center = oa.unpair(record["newton"]["center"])
    critical = certify_critical(center)
    record["critical"] = critical
    if not critical["simple_real_critical"]:
        record["status"] = "CRITICAL_CERTIFICATE_FAILED"
        return record
    for bits in TIERS:
        with ha.precision(bits):
            try:
                prep = prepared(center, runner)
                record["jet_tiers"].append(prep[0])
                for item, ratio in zip(record["quadratic"], RATIOS):
                    if not item["attempts"] or item["attempts"][-1]["status"] != "PASS":
                        item["attempts"].append(
                            quadratic_attempt(center, parent, prep, ratio, runner)
                        )
                item = record["linear"]
                if not item["attempts"] or item["attempts"][-1]["status"] != "PASS":
                    item["attempts"].append(
                        linear_attempt(center, parent, prep, runner)
                    )
            except (ValueError, ZeroDivisionError, OverflowError) as error:
                failure = {
                    "bits": bits,
                    "status": "FAILED",
                    "reason": str(error),
                    "transport_certified": False,
                    "parent_matched": False,
                }
                record["jet_tiers"].append(
                    {"bits": bits, "status": "FAILED", "reason": str(error)}
                )
                for item in record["quadratic"] + [record["linear"]]:
                    if not item["attempts"] or item["attempts"][-1]["status"] != "PASS":
                        item["attempts"].append(dict(failure))
            if all(
                item["attempts"][-1]["status"] == "PASS"
                for item in record["quadratic"] + [record["linear"]]
            ):
                break
    record["status"] = "COMPLETE_DECLARED_ATTEMPTS"
    return record


def summary(records):
    require(type(records) is list and len(records) == 26, "complete node coverage")
    require([r["index"] for r in records] == list(range(26)), "complete node indices")

    def passed(item):
        return bool(item["attempts"] and item["attempts"][-1]["status"] == "PASS")

    def transported(item):
        return any(a.get("transport_certified", False) for a in item["attempts"])

    return {
        "nodes": 26,
        "newton_converged": sum(
            r["newton"]["status"] == "CONVERGED_SCOUT" for r in records
        ),
        "simple_real_critical": sum(
            r.get("critical", {}).get("simple_real_critical", False) for r in records
        ),
        "critical_intervals_pairwise_disjoint": all(
            abs(oa.unpair(a["critical"]["center"]) - oa.unpair(b["critical"]["center"]))
            > 2 * EPS
            for i, a in enumerate(records)
            for b in records[i + 1 :]
            if a.get("critical", {}).get("simple_real_critical", False)
            and b.get("critical", {}).get("simple_real_critical", False)
        ),
        "quadratic_matched_by_ratio": [
            {
                "ratio": oa.pair(q),
                "count": sum(passed(r["quadratic"][j]) for r in records),
            }
            for j, q in enumerate(RATIOS)
        ],
        "quadratic_transport_by_ratio": [
            {
                "ratio": oa.pair(q),
                "count": sum(transported(r["quadratic"][j]) for r in records),
            }
            for j, q in enumerate(RATIOS)
        ],
        "quadratic_any_transport": sum(
            any(transported(x) for x in r["quadratic"]) for r in records
        ),
        "linear_transport": sum(transported(r["linear"]) for r in records),
        "quadratic_any_matched": sum(
            any(passed(x) for x in r["quadratic"]) for r in records
        ),
        "linear_matched": sum(passed(r["linear"]) for r in records),
        "quadratic_only_matched": sum(
            any(passed(x) for x in r["quadratic"]) and not passed(r["linear"])
            for r in records
        ),
    }


def polynomial_control():
    lam, q, d, y, c, m3 = Q(1), Q(3, 8), Q(1, 2), Q(1, 2), Q(-1), Q(1, 100)
    rows = []
    for ratio in RATIOS:
        r = ratio * y
        left = m3 * (y + r) ** 2 * ((y + r) / 6 + lam / 2)
        right = abs(c) * r * (d - r / 2)
        require(0 < r < min(y, 2 * d) and left < right, "exact polynomial control")
        rows.append(
            {"ratio": oa.pair(ratio), "left": oa.pair(left), "right": oa.pair(right)}
        )
    delta = 2 * q / lam + m3 / abs(c) * (4 * q * q / (3 * lam) + 2 * q)
    require(
        delta == Q(243, 320) and delta > Q(1, 2), "linear strict-improvement control"
    )
    return {
        "g": "3/8-w^2/2+w^3/600",
        "lambda": [1, 1],
        "quadratic": rows,
        "linear_delta": oa.pair(delta),
    }


def necessary_bound_diagnostics(records):
    """Post-result pointwise obstructions, not favorable source resampling."""
    output = []
    for row in records:
        entry = {
            "index": row["index"],
            "bits": 1024,
            "ratios": [
                {
                    "ratio": oa.pair(ratio),
                    "criterion_impossible": False,
                    "status": "UNRESOLVED",
                }
                for ratio in RATIOS
            ],
        }
        output.append(entry)
        try:
            require(
                row.get("critical", {}).get("simple_real_critical", False),
                "missing real critical certificate",
            )
            center = oa.unpair(row["critical"]["center"])
            entry["critical_center"] = oa.pair(center)
            with ha.precision(1024):
                coeff = ha.xi_series(acb(arb(oa.qarb(center), oa.qarb(EPS))), 40)
                require(all(v.imag.contains(0) for v in coeff), "real point jets")
                require(coeff[6].real.contains(0), "critical interval consistency")
                a, c = (
                    (coeff[5] * math.factorial(5)).real,
                    (coeff[7] * math.factorial(7)).real,
                )
                m_lower = oa.endpoint(coeff[8].abs_lower()) * math.factorial(8)
                lam = ha.fixed_lambda()
                require(a * c < 0, "diagnostic opposite signs")
                q = -a / (lam * c)
                require(q > 0 and 2 * q < lam, "diagnostic discriminant")
                d = (lam * lam - 2 * lam * q).sqrt()
                y = 2 * lam * q / (lam + d)
                entry["point_f8_lower"] = oa.pair(m_lower)
                for ratio, result in zip(RATIOS, entry["ratios"]):
                    r = oa.qarb(ratio) * y
                    if not (r > 0 and r < y and r < 2 * d):
                        result.update(
                            status="UNRESOLVED", reason="radius geometry not certified"
                        )
                        continue
                    left = scalar_lower(
                        oa.qarb(m_lower) * (y + r) ** 2 * ((y + r) / 6 + lam / 2)
                    )
                    right = scalar_upper(abs(c) * r * (d - r / 2))
                    impossible = left >= right
                    result.update(
                        left_lower=oa.pair(left),
                        right_upper=oa.pair(right),
                        criterion_impossible=impossible,
                        status="CRITERION_IMPOSSIBLE" if impossible else "UNRESOLVED",
                    )
                entry["status"] = "COMPLETE"
        except (ValueError, ZeroDivisionError, OverflowError) as error:
            entry.update(status="UNRESOLVED", reason=str(error))
    return {
        "design": CONTRACT["postresult_diagnostic"],
        "records": output,
        "impossible_by_ratio": [
            {
                "ratio": oa.pair(ratio),
                "count": sum(
                    any(
                        r["ratio"] == oa.pair(ratio) and r["criterion_impossible"]
                        for r in e["ratios"]
                    )
                    for e in output
                ),
            }
            for ratio in RATIOS
        ],
    }


def build_with_runner(runner):
    authenticate()
    records = [node_record(i, row, runner) for i, row in enumerate(parent_panel())]
    return assemble_report(records, runner.history())


def assemble_report(records, history):
    value = {
        "schema": STEM + "-v1",
        "contract": CONTRACT,
        "frozen_sources": BINDINGS,
        "runtime": oa.RUNTIME,
        "environmental_attempt_history": history,
        "records": records,
        "summary": summary(records),
        "exact_polynomial_control": polynomial_control(),
        "postresult_necessary_bound": necessary_bound_diagnostics(records),
        "artifacts": {
            p.relative_to(ROOT).as_posix(): oa.digest(lf(p.read_bytes()))
            for p in (NOTE, Path(__file__), MANIFEST, TEST)
        },
    }
    return {**value, "payload_sha256": oa.digest(canonical(value))}


def build_report():
    history = decode(FIXTURE.read_bytes())["environmental_attempt_history"]
    return build_with_runner(NativeRunner(history))


def check_report(value):
    validate_tree(value)
    require(type(value) is dict and "payload_sha256" in value, "report shape")
    unsigned = {k: v for k, v in value.items() if k != "payload_sha256"}
    require(value["payload_sha256"] == oa.digest(canonical(unsigned)), "payload seal")
    require(
        canonical(value) == canonical(build_report()), "fresh primitive reconstruction"
    )
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--emit", action="store_true")
    mode.add_argument("--emit-sources", action="store_true")
    mode.add_argument("--native-task", action="store_true")
    args = parser.parse_args()
    if args.native_task:
        value = native_worker(decode(sys.stdin.buffer.read(MAX_BYTES + 1)))
    elif args.emit_sources:
        value = manifest()
    elif args.emit:
        value = build_report()
    else:
        value = decode(FIXTURE.read_bytes())
        check_report(value)
        print("PASS fresh fixed26-node quadratic/linear critical transport panel")
        print("fixture_sha256_lf=" + oa.digest(lf(FIXTURE.read_bytes())))
        return
    print(json.dumps(value, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
