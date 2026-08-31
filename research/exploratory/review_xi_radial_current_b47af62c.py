"""Independent stdlib finite reconstruction of frozen b47af62c, without author imports.

The Gaussian squared-radius MGF gives rising-factorial coefficients. The current
MLR determinant is reconstructed by antisymmetric coefficient pairs from the
integral-polynomial coefficients, not the producer's derivative convolution.
This is a finite audit, not a machine proof of analytic convergence.
"""

from __future__ import annotations

import hashlib
import json
import math
import subprocess
from fractions import Fraction as Q
from itertools import pairwise
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SHA = "b47af62c6efa225d731f2813e8bdf7f8b2a9a308"
BASE = "af809698fe6cb5046a5bcc00e9175296e4597060"
STEM = "research/exploratory/xi_current_radial_semigroup"
FIXTURE_HASH = "250a86b6c704e8ab8e3391ebaa4c41cc3039f73b8739d73770430fab2143f320"
PAYLOAD_HASH = "3f0f9ab847109b9d26b2800530a8c3b8b66ec7acf62adf4139def00acbc30cf5"


def require(ok, why):
    if not ok:
        raise ValueError(why)


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def blob(commit, path):
    return git("show", commit + ":" + path)


def lf(raw):
    return raw.replace(b"\r\n", b"\n")


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), allow_nan=False
    ).encode()


def rising(a, n):
    return math.prod((a + j for j in range(n)), start=Q(1))


def moments(m):
    # m! [z^m] (1-tz)^(-3/2) exp[xz/(1-tz)].
    return [Q(math.comb(m, d)) * rising(Q(d) + Q(3, 2), m - d) for d in range(m + 1)]


def compose(coefficients, time):
    answer = [Q(0)] * len(coefficients)
    for m, a in enumerate(coefficients):
        for d, c in enumerate(moments(m)):
            answer[d] += a * c * time ** (m - d)
    return answer


def mlr(k):
    # F_K(sqrt(z))=integral_(-1)^1(1+t sqrt(z))^(K-1)dt/2.
    a = [Q(math.comb(k - 1, 2 * j), 2 * j + 1) for j in range((k + 1) // 2)]
    b = [Q(math.comb(k + 1, 2 * j), 2 * j + 1) for j in range((k + 3) // 2)]
    a.append(Q(0))
    out = [Q(0)] * k
    for i in range(len(b)):
        for j in range(i):
            out[i + j - 1] += (i - j) * (b[i] * a[j] - b[j] * a[i])
    ratios = [b[j] / a[j] for j in range(len(a) - 1)]
    require(all(v > 0 for v in out), "strict MLR coefficients")
    return ratios, out


def run():
    raw = blob(SHA, STEM + ".json")
    require(digest(lf(raw)) == FIXTURE_HASH, "exact frozen fixture")
    report = json.loads(raw)
    payload = report.pop("payload_sha256")
    require(payload == PAYLOAD_HASH == digest(canonical(report)), "payload seal")
    changed = set(git("diff", "--name-only", BASE, SHA).decode().splitlines())
    expected = {
        STEM + ".py",
        STEM + ".json",
        STEM + ".sources.json",
        "research/exploratory/XI_CURRENT_RADIAL_SEMIGROUP.md",
        "tests/test_xi_current_radial_semigroup.py",
    }
    require(changed == expected, "exact five-file base delta")
    for path, checksum in report["artifacts"].items():
        require(digest(lf(blob(SHA, path))) == checksum, "frozen artifact " + path)
        require(
            digest(lf((ROOT / path).read_bytes())) == checksum, "local artifact " + path
        )
    manifest = json.loads(blob(SHA, STEM + ".sources.json"))
    require(report["sources"] == manifest["sources"], "same direct sources")
    sources = list(manifest["sources"])
    historical = json.loads(
        blob(BASE, "research/exploratory/xi_odd_current_scaling.sources.json")
    )
    sources += historical["sources"]
    require(len(sources) == 11, "direct and transitive source coverage")
    for row in sources:
        data = blob(row["commit"], row["path"])
        got = hashlib.sha1(
            b"blob " + str(len(data)).encode() + b"\0" + data
        ).hexdigest()
        require(
            got == row["git_blob"] and digest(lf(data)) == row["sha256_lf"],
            "source identity",
        )
    require(
        report["coverage"]
        == {
            "moments": 13,
            "moment_compositions": 117,
            "adjacent_odd_orders": 31,
            "laplace_compositions": 36,
        },
        "coverage",
    )
    require(
        [r["moment_index"] for r in report["moments"]] == list(range(13)), "all moments"
    )
    for row in report["moments"]:
        require(
            list(map(Q, row["x_d_t_m_minus_d_coefficients"]))
            == moments(row["moment_index"]),
            "MGF moments",
        )
    times = (Q(1, 3), Q(1), Q(2))
    require(
        [
            (r["moment_index"], Q(r["s"]), Q(r["t"]))
            for r in report["moment_compositions"]
        ]
        == [(m, s, t) for m in range(13) for s in times for t in times],
        "all compositions",
    )
    for row in report["moment_compositions"]:
        m, s, t = row["moment_index"], Q(row["s"]), Q(row["t"])
        single = [c * t ** (m - d) for d, c in enumerate(moments(m))]
        two = compose(single, s)
        require(
            two == [c * (s + t) ** (m - d) for d, c in enumerate(moments(m))],
            "composition algebra",
        )
        require(two == list(map(Q, row["x_coefficients"])), "stored composition")
    require(
        [r["K"] for r in report["mlr_controls"]] == list(range(1, 62, 2)),
        "all MLR orders",
    )
    for row in report["mlr_controls"]:
        ratios, coefficients = mlr(row["K"])
        require(row["next_K"] == row["K"] + 2, "adjacent order")
        require(
            ratios == list(map(Q, row["coefficient_ratios"])),
            "integral ratio coefficients",
        )
        require(
            coefficients == list(map(Q, row["derivative_numerator"])),
            "antisymmetric determinant",
        )
    alphas = (Q(0), Q(1, 7), Q(1), Q(3))
    require(
        [(Q(r["a"]), Q(r["s"]), Q(r["t"])) for r in report["laplace_controls"]]
        == [(a, s, t) for a in alphas for s in times for t in times],
        "all Laplace controls",
    )
    for row in report["laplace_controls"]:
        a, s, t = (Q(row[k]) for k in ("a", "s", "t"))
        one, both = 1 + a * t, 1 + a * (s + t)
        require(
            Q(row["first_base"]) == one
            and Q(row["second_base"]) == both / one
            and Q(row["combined_base"]) == both
            and Q(row["combined_rate"]) == a / both,
            "Laplace MGF composition",
        )
    extra = []
    for m in range(17):
        a = [Q(0)] * m + [Q(1)]
        for t in (Q(2, 7), Q(3, 5), Q(11, 13)):
            a = compose(a, t)
        total = Q(2, 7) + Q(3, 5) + Q(11, 13)
        require(
            a == [c * total ** (m - d) for d, c in enumerate(moments(m))],
            "heldout three-time identity",
        )
        extra.append(list(map(str, a)))
    for k in (65, 81, 127):
        ratios, _ = mlr(k)
        require(all(x < y for x, y in pairwise(ratios)), "heldout MLR order")
    # Exact rational point 5delta/4 replaces the irrational point in the proof.
    require(
        Q(5, 4) > 1 and Q(5, 4) ** 2 < 2, "quantized semigroup counterexample geometry"
    )
    return {
        "source_sha": SHA,
        "verdict": "PASS_FINITE_RECONSTRUCTION_ONLY",
        "frozen_fixture_lf": FIXTURE_HASH,
        "payload_sha256": PAYLOAD_HASH,
        "source_bindings": 11,
        "artifact_locks": 4,
        "moments": 13,
        "moment_compositions": 117,
        "mlr_polynomials": 31,
        "laplace_compositions": 36,
        "heldout_three_time_moments": 17,
        "heldout_mlr_orders": [65, 81, 127],
        "heldout_coefficients_sha256": digest(canonical(extra)),
        "author_imports": False,
        "analytic_quantifiers_machine_proved": False,
    }


if __name__ == "__main__":
    print(json.dumps(run(), sort_keys=True, indent=2))
