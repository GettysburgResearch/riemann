"""Independent fixed-SHA review controls for the synthetic positive-source firewall."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
import subprocess
import types
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DIR = "research/l-families/atlas/generalized/"
SCIENCE = "dd498bdc20bdd658d34d0a56d7d22f3c5182b569"
DESIGN = "67f88c148bb5914897cc13b6cbce61960a277cd1"
STEM = "theta_positive_source_real_zero_firewall"
FIXTURE_SHA = "3987133d0fd7e71fcf17d05675ce9a10d3edfb0a906714eb6e13c997cc3e0dfc"
OUT = Path(__file__).with_suffix(".json")


def need(value, reason):
    if not value:
        raise ValueError(reason)


def raw(commit, path):
    return subprocess.check_output(
        ["git", "--no-replace-objects", "show", commit + ":" + path], cwd=ROOT
    )


def lf(value):
    return value.replace(b"\r\n", b"\n")


def sha(value):
    return hashlib.sha256(value).hexdigest()


def canonical(value):
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), allow_nan=False
    ).encode()


def horner(x, order):
    """Nested polynomial, independent of the producer's forward term recurrence."""
    result = Q(1)
    for j in range(order, 0, -1):
        result = 1 + x * result / j
    return result


def enclosure(x, order=16):
    lo = horner(x, order)
    factorial = math.prod(range(1, order + 2))
    return lo, lo + x ** (order + 1) / factorial / (1 - x / (order + 2))


def text_bounds(values):
    return [str(x) for x in values]


def antiderivative(degree):
    """Solve P'+P/2=x^degree by reverse triangular coefficient elimination."""
    result = [Q(0)] * (degree + 2)
    for j in range(degree, -1, -1):
        result[j] = 2 * (Q(j == degree) - (j + 1) * result[j + 1])
    return result[:-1]


def primitive_review(fixture):
    grid = [Q(1, 8), Q(3, 8), Q(1, 2), Q(5, 8), Q(7, 8), Q(1)]
    expected = [
        {
            "x": str(x),
            "N": 16,
            "enclosure": text_bounds(enclosure(x)),
            "both_inequalities_strict": True,
        }
        for x in grid
    ]
    need(
        fixture["exponential_enclosures"] == expected,
        "six independent Taylor intervals",
    )
    signs = []
    for a in (Q(1, 2), Q(1), Q(2)):
        for s in (Q(1, 8), Q(3, 8), Q(1, 2)):
            e, f = enclosure(s), enclosure(1 - s)
            ends = tuple(Q(1, 2) + a * (1 - (1 - s) * e[j] - s * f[j]) for j in (1, 0))
            need(ends[0] > 0 or ends[1] < 0, "strict independent sign")
            signs.append(
                {
                    "A": str(a),
                    "s": str(s),
                    "enclosure": text_bounds(ends),
                    "sign": 1 if ends[0] > 0 else -1,
                }
            )
    need(signs == fixture["Z_sign_panel"], "nine independent sign intervals")
    e = enclosure(Q(1, 2))
    threshold = (1 / (2 * (e[1] - 1)), 1 / (2 * (e[0] - 1)))
    need(text_bounds(threshold) == fixture["A_c_enclosure"], "threshold identity")
    need(Q(3, 4) < threshold[0] < threshold[1] < Q(4, 5), "threshold bracket")
    margins = [
        {
            "b_squared": str(b),
            "z": str(z),
            "margin": str(2 - b / 4 + b * z**2),
            "lower_bound": str(b * z**2),
        }
        for b in (Q(1), Q(4), Q(8))
        for z in (Q(1, 8), Q(1, 4), Q(3, 8))
    ]
    need(margins == fixture["monotonicity_margins"], "nine margins")
    need(
        [row["opposite_signs"] for row in fixture["candidate_brackets"]]
        == [True, False],
        "failed candidate retained",
    )
    p0, p2 = antiderivative(0), antiderivative(2)
    need(p0 == [2] and p2 == [16, -8, 2], "antiderivative elimination")
    j0 = [-p0[0], sum(p0)]
    j2 = [-p2[0], sum(p2)]
    c = [2 * j0[j] - j2[j] / 4 for j in range(2)]
    formal = fixture["formal"]
    need(list(map(Q, formal["J0_E"])) == j0, "J0")
    need(list(map(Q, formal["J2_E"])) == j2, "J2")
    need(list(map(Q, formal["curvature_E"])) == c, "curvature")
    need(formal["pitchfork_numerator_E"] == ["4", "-8", "4"], "implicit numerator")
    need(formal["pitchfork_denominator_E"] == ["0", "3"], "implicit denominator")
    # Before substituting b=1, J2 = exp(b/2)*P2(b)-P2(0).
    general_c = [Q(4), Q(0), Q(0)]
    general_c = [general_c[j] - p2[j] / 4 for j in range(3)]
    need(general_c == [0, 2, Q(-1, 2)], "general c_b polynomial")
    # Direct expansion of (z-1/2)e^(bz)-(z+1/2)e^(-bz).
    direct = {}
    for n in range(1, 9):
        first = Q(1 - (-1) ** (n - 1), math.factorial(n - 1))
        second = -Q(1 + (-1) ** n, 2 * math.factorial(n))
        direct[str(n)] = [str(first), str(second)]
        if n % 2:
            need(first == second == 0, "odd coefficient vanishes")
    need(direct["2"] == ["2", "-1/2"], "direct central expansion agrees")
    extra = 0
    for n in range(1, 33):
        for j in range(1, 17):
            x = Q(j, 16)
            lo, hi = enclosure(x, n)
            need(
                lo == sum((x**k / math.factorial(k) for k in range(n + 1)), Q(0)),
                "independent finite factorial identity",
            )
            need(lo < horner(x, n + 2) < hi, "strict higher Taylor tail control")
            extra += 1
    return {
        "Taylor_intervals": expected,
        "signs": [r["sign"] for r in signs],
        "threshold": text_bounds(threshold),
        "margins": margins,
        "independent_antiderivatives": [text_bounds(p0), [str(x) for x in p2]],
        "general_c_b": {
            "factor": "exp(b/2)",
            "polynomial_in_b": [str(x) for x in general_c],
        },
        "direct_z_coefficients": direct,
        "additional_Horner_factorial_tail_controls": extra,
        "analytic_all_b_and_smoothing_proofs_not_machine_certified": True,
    }


def replace(value, path, new):
    target = value
    for part in path[:-1]:
        target = target[part]
    target[path[-1]] = new


def hostile_review(module, fixture):
    attacks = []
    for i in range(9):
        attacks.append(
            (["Z_sign_panel", i, "sign"], -fixture["Z_sign_panel"][i]["sign"])
        )
    for i in range(6):
        attacks.append((["exponential_enclosures", i, "N"], 15))
    attacks += [
        (["Z_sign_panel"], list(reversed(fixture["Z_sign_panel"]))),
        (["A_c_enclosure"], list(reversed(fixture["A_c_enclosure"]))),
        (["candidate_brackets", 1, "opposite_signs"], True),
        (["candidate_brackets", 1, "candidate", 0], "0"),
        (["A_c_rational_outer_bracket", 0], "1/2"),
        (["monotonicity_margins", 0, "margin"], "0"),
        (["formal", "curvature_E", 1], "3"),
        (["formal", "J2_E", 1], "11"),
        (["work_units"], True),
        (["coverage", "exponentials"], 5),
        (["contract", "actual_modular_source"], True),
        (["contract", "RH_counterexample"], True),
        (["contract", "all_complex_zero_count"], True),
        (["sources", 0, "sha256_lf"], "0" * 64),
        (["artifact_sha256_lf", next(iter(fixture["artifact_sha256_lf"]))], "0" * 64),
        (["not_claimed"], []),
        (["undeclared"], 1),
    ]
    need(len(attacks) == 32, "hostile panel coverage")
    for path, new in attacks:
        forged = copy.deepcopy(fixture)
        replace(forged, path, new)
        forged.pop("payload_sha256")
        forged["payload_sha256"] = sha(canonical(forged))
        try:
            module.check(forged)  # Unmocked; fresh primitive/source replay every time.
        except ValueError:
            continue
        raise ValueError("accepted resealed mutation: " + repr(path))
    guards = [(module.rational, (v,)) for v in (True, False, 1.0, "1", None, 1j)]
    guards += [(module.exp_bounds, (Q(1, 2), n)) for n in (0, 33, True, 16.0)]
    guards += [(module.exp_bounds, (x,)) for x in (-1, Q(9, 8))]
    guards += [
        (module.interval, ([2, 1],)),
        (module.sign, ((-1, 1),)),
        (module.polynomial, ([1] * 9,)),
        (module.rational, (1 << 4096,)),
    ]
    guards += [
        (module.decode, (v,)) for v in (b"NaN", b"1.0", b'{"a":1,"a":2}', b"null")
    ]
    for func, args in guards:
        try:
            func(*args)
        except ValueError:
            continue
        raise ValueError("accepted primitive guard: " + func.__name__)
    return {
        "fully_resealed_unmocked_attacks": len(attacks),
        "primitive_type_cap_guards": len(guards),
    }


def replay():
    source = raw(SCIENCE, DIR + STEM + ".json")
    need(sha(lf(source)) == FIXTURE_SHA, "exact fixture LF identity")
    fixture = json.loads(source)
    manifest = json.loads(raw(SCIENCE, DIR + STEM + ".sources.json"))
    need(fixture["sources"] == manifest["frozen_sources"], "source-list identity")
    sources = []
    for row in fixture["sources"]:
        content = raw(row["commit"], row["path"])
        blob = hashlib.sha1(
            b"blob " + str(len(content)).encode() + b"\0" + content
        ).hexdigest()
        need(
            blob == row["git_blob"] and sha(lf(content)) == row["sha256_lf"],
            "source Git/LF identities",
        )
        sources.append(row)
    for path, wanted in fixture["artifact_sha256_lf"].items():
        content = raw(SCIENCE, path)
        need(sha(lf(content)) == wanted, "frozen artifact seal")
        need(
            not any(byte < 32 and byte not in (9, 10, 13) for byte in content),
            "C0 guard",
        )
    unsealed = copy.deepcopy(fixture)
    wanted = unsealed.pop("payload_sha256")
    need(sha(canonical(unsealed)) == wanted, "frozen payload seal")
    proof = lf(raw(SCIENCE, DIR + STEM.upper() + ".md")).decode()
    design = lf(raw(DESIGN, DIR + STEM.upper() + ".md")).decode()
    need(
        proof.split("## 1.", 1)[1].split("## 4.", 1)[0].strip()
        == design.split("## 1.", 1)[1].strip(),
        "unaltered design sections1-3",
    )
    independent = primitive_review(fixture)
    module = types.ModuleType("frozen_zf_review_target")
    module.__file__ = str(ROOT / (DIR + STEM + ".py"))
    exec(  # noqa: S102 - execute the personally reviewed, fixed-SHA producer, not user code
        compile(raw(SCIENCE, DIR + STEM + ".py"), module.__file__, "exec"),
        module.__dict__,
    )
    need(module.check(fixture), "baseline fresh authentication/reconstruction")
    hostile = hostile_review(module, fixture)
    out = {
        "science": SCIENCE,
        "fixture_sha256_lf": FIXTURE_SHA,
        "source_payload_sha256": wanted,
        "source_bindings": sources,
        "artifact_sha256_lf": fixture["artifact_sha256_lf"],
        "independent_controls": independent,
        "hostile_controls": hostile,
        "arithmetic_class": "MIXED",
        "arithmetic_components": ["EXACT_RATIONAL", "CERTIFIED_INTEGER_COVERAGE"],
        "rounding": "none",
        "scope": "finite independent review controls; analytic verdict resides in audit note",
    }
    return {**out, "payload_sha256": sha(canonical(out))}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = replay()
    if args.check:
        need(
            canonical(json.loads(OUT.read_bytes())) == canonical(result),
            "type-exact independent review report",
        )
        print(
            "PASS independent ZF controls: 6+9+9 primitives, 512 extra Taylor controls, 32 resealed attacks, 20 guards"
        )
    else:
        print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
