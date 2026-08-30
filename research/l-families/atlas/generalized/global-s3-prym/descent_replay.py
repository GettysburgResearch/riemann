"""Exact arithmetic descent with a separately bounded degree-six field model."""

from __future__ import annotations

import argparse
import importlib.util
import json
import subprocess
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[4]
PRECURSOR = "ed8139953de75d5ef0d1c9fab5402360b7b7e9b7"
EXPECTED_SOURCE_HASH = (
    "6b96c1d6c437e88f36b3d8a76683e6f15a3c1d1238f771d74099a268b483b39e"
)
FIELD_CAP = 15625


def load_frozen_kummer():
    path = ROOT / "kummer_replay.py"
    relative = path.relative_to(REPO).as_posix()
    result = subprocess.run(
        ["git", "show", f"{PRECURSOR}:{relative}"],
        cwd=REPO,
        capture_output=True,
        check=False,
    )

    def normalize(data):
        return data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")

    if result.returncode or normalize(result.stdout) != normalize(path.read_bytes()):
        raise ValueError("Kummer helper differs from the frozen source")
    spec = importlib.util.spec_from_file_location("descent_frozen_kummer", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K = load_frozen_kummer()
P = K.P


class DescentField(P.Field):
    """Same frozen field arithmetic, new explicit p5/n<=6 allocation contract.

    The predecessor's constructor and power cap remain unchanged. This source
    subclass adds only the audited larger bounds and owns all its allocations.
    """

    def __init__(self, p: int, n: int):
        self.p = P.require_int(p, "descent prime", 5, 5)
        self.n = P.require_int(n, "descent field degree", 1, 6)
        self.q = p**n
        if self.q > FIELD_CAP:
            raise ValueError("descent field exceeds its separate allocation cap")
        self.modulus = P.first_modulus(p, n)
        if not P.irreducible(self.modulus, p):
            raise ArithmeticError("descent modulus is not irreducible")
        self.table = [P.digits(x, p, n) for x in range(self.q)]

    def power(self, a: int, exponent: int) -> int:
        P.require_int(a, "descent field element", 0, self.q - 1)
        P.require_int(exponent, "descent field exponent", 0, FIELD_CAP)
        value = 1
        while exponent:
            if exponent & 1:
                value = self.mul(value, a)
            a = self.mul(a, a)
            exponent >>= 1
        return value


def cube_character(field):
    if field.n % 2:
        raise ValueError(
            "nontrivial cubic character is not defined over an odd p5 extension"
        )
    exponent = (field.q - 1) // 3
    eta = None
    for t in range(2, field.q):
        candidate = field.power(t, exponent)
        if candidate != 1:
            eta = min(candidate, field.mul(candidate, candidate))
            break
    if eta is None or field.power(eta, 3) != 1 or eta == 1:
        raise ArithmeticError("nontrivial cube root construction failed")
    roots = {1: 0, eta: 1, field.mul(eta, eta): 2}
    if len(roots) != 3:
        raise ArithmeticError("cube root labels are not distinct")
    exponents = [None] + [roots[field.power(t, exponent)] for t in range(1, field.q)]
    return {"eta": eta, "exponents": exponents}


def power_histograms(field):
    squares, cubes, sixths = [0] * field.q, [0] * field.q, [0] * field.q
    for w in range(field.q):
        w2 = field.mul(w, w)
        w3 = field.mul(w2, w)
        squares[w2] += 1
        cubes[w3] += 1
        sixths[field.mul(w3, w3)] += 1
    return squares, cubes, sixths


def count_curves(field, A, B, histograms, character=None):
    P.require_int(A, "A", -100, 100)
    P.require_int(B, "B", -100, 100)
    if A % 5 == 0 or (-4 * A**3 - 27 * B**2) % 5 == 0:
        raise ValueError("descent source must be in the smooth S3 stratum")
    square, cube, sixth = histograms
    infinity = gcd(3, field.q - 1)
    elliptic, second, tower = 1, infinity, infinity
    f_hist = [0] * field.q
    for x in range(field.q):
        fx = field.cubic(x, A, B)
        f_hist[fx] += 1
        elliptic += square[fx]
        second += cube[fx]
        tower += sixth[fx]
    row = {
        "degree": field.n,
        "field_order": field.q,
        "modulus": field.modulus,
        "E_points": elliptic,
        "Eprime_points": second,
        "C_points": tower,
        "E_infinity_points": 1,
        "Eprime_and_C_infinity_points": infinity,
        "descended_infinity_trace": infinity - 1,
    }
    if field.n % 2:
        if tower != elliptic or second != field.q + 1:
            raise ArithmeticError("odd-extension cube bijection failed")
        row["geometric_character_sums"] = None
    else:
        if character is None:
            raise ValueError("even-extension character source is missing")
        ring = K.Cyclotomic(3)
        sums = [K.ONE, K.ONE]  # the two actual infinity invariant traces
        for t in range(1, field.q):
            trace = f_hist[field.mul(t, t)] - 1
            e = character["exponents"][t]
            for j in (1, 2):
                sums[j - 1] = ring.add(
                    sums[j - 1], ring.scale(ring.roots[j * e % 3], trace)
                )
        if sums[0] != sums[1] or sums[0][1] != 0 or 2 * sums[0][0] != tower - elliptic:
            raise ArithmeticError(
                "special inverse-character rational descent identity failed"
            )
        row["eta"] = character["eta"]
        row["geometric_character_sums"] = [list(s) for s in sums]
    return row


def int_product(left, right):
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out


def substitute_degree(polynomial, degree):
    P.require_int(degree, "Frobenius orbit length", 1, 6)
    out = [0] * ((len(polynomial) - 1) * degree + 1)
    for i, c in enumerate(polynomial):
        out[i * degree] = c
    return out


def reciprocal_completion(first_half, q, genus):
    if len(first_half) != genus + 1 or first_half[0] != 1:
        raise ValueError(
            "reciprocal completion needs exactly the first half of the source polynomial"
        )
    out = first_half + [0] * genus
    for k in range(genus):
        out[2 * genus - k] = q ** (genus - k) * first_half[k]
    return out


def build(source):
    if P.digest(source) != EXPECTED_SOURCE_HASH:
        raise ValueError("descent source differs from its frozen canonical identity")
    if (
        source["p"] != 5
        or source["extensions"] != list(range(1, 7))
        or source["maximum_field_order"] != FIELD_CAP
    ):
        raise ValueError("unreviewed descent coverage")
    models = {n: DescentField(5, n) for n in range(1, 7)}
    histograms = {n: power_histograms(f) for n, f in models.items()}
    characters = {n: cube_character(f) for n, f in models.items() if n % 2 == 0}
    panels = []
    for curve in source["curves"]:
        counts = [
            count_curves(
                models[n], curve["A"], curve["B"], histograms[n], characters.get(n)
            )
            for n in range(1, 7)
        ]
        even_sums = [
            row["geometric_character_sums"][0][0]
            for row in counts
            if row["degree"] % 2 == 0
        ]
        q_cubic = P.newton_from_local_sums(even_sums)
        orbit = substitute_degree(q_cubic, 2)
        differences = [row["C_points"] - row["E_points"] for row in counts]
        if P.local_sums_from_polynomial(orbit, 6) != differences:
            raise ArithmeticError(
                "cyclic Frobenius block determinant does not recover all primitive differences"
            )
        e_sums = [row["E_points"] - row["field_order"] - 1 for row in counts]
        e_poly = P.newton_from_local_sums(e_sums[:2])
        second_poly = [1, 0, 5]
        second_sums = [row["Eprime_points"] - row["field_order"] - 1 for row in counts]
        if (
            P.local_sums_from_polynomial(e_poly, 6) != e_sums
            or P.local_sums_from_polynomial(second_poly, 6) != second_sums
        ):
            raise ArithmeticError("elliptic quotient extension prediction failed")
        if q_cubic[2] != 5 * q_cubic[1] or q_cubic[3] != 125:
            raise ArithmeticError(
                "odd cubic over F25 has the wrong descended reciprocity"
            )
        b = q_cubic[1] - 5
        residual = [1, 0, b, 0, 25]
        if b * b > 100 or int_product(second_poly, residual) != orbit:
            raise ArithmeticError(
                "forced second elliptic factor or residual weight bound failed"
            )
        c_sums = [row["C_points"] - row["field_order"] - 1 for row in counts]
        c_poly = reciprocal_completion(P.newton_from_local_sums(c_sums[:4]), 5, 4)
        if P.local_sums_from_polynomial(c_poly, 6) != c_sums or c_poly != int_product(
            e_poly, orbit
        ):
            raise ArithmeticError(
                "independent genus-four reconstruction or held-out extensions failed"
            )
        panels.append(
            {
                "source": curve,
                "counts": counts,
                "F25_geometric_character_polynomial": q_cubic,
                "F5_orbit_polynomial": orbit,
                "P_E": e_poly,
                "P_Eprime": second_poly,
                "P_residual": residual,
                "P_C": c_poly,
                "residual_b": b,
                "genus_four_held_out_degrees": [5, 6],
                "scope": "Three even extensions reconstruct the F25 cubic; the genus-four F5 polynomial independently uses four counts plus proved reciprocity and predicts two held-out extensions.",
            }
        )
    return {
        "schema": "cubic-kummer-descent-replay-v1",
        "source_hash": P.digest(source),
        "field_cap": FIELD_CAP,
        "panels": panels,
    }


def bindings():
    names = (
        "descent_source.json",
        "descent_replay.py",
        "test_descent_replay.py",
        "FROBENIUS_DESCENT_AND_SECOND_ELLIPTIC_QUOTIENT.md",
        "descent_artifact.json",
    )
    return {
        "schema": "cubic-descent-binding-v1",
        "precursor_commit": PRECURSOR,
        "files": {name: P.lf_hash(ROOT / name) for name in names},
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write", action="store_true")
    group.add_argument("--check", action="store_true")
    args = parser.parse_args()
    source = json.loads((ROOT / "descent_source.json").read_text(encoding="utf-8"))
    artifact = build(source)
    artifact_path, binding_path = (
        ROOT / "descent_artifact.json",
        ROOT / "descent_provenance.json",
    )
    if args.write:
        artifact_path.write_text(
            json.dumps(artifact, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        binding_path.write_text(
            json.dumps(bindings(), indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
    else:
        P.require_same_json(
            json.loads(artifact_path.read_text(encoding="utf-8")),
            artifact,
            "descent artifact",
        )
        P.require_same_json(
            json.loads(binding_path.read_text(encoding="utf-8")),
            bindings(),
            "descent binding",
        )
    print(
        "PASS: two complete cubic Kummer descents through F5^6, second elliptic quotient and forced factor"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
