"""Exact bounded controls for the analytic far-zero reserve theorem."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import subprocess
from fractions import Fraction as Q
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
STEM = "xi_four_node_far_zero_reserve"
NOTE = HERE / "XI_FOUR_NODE_FAR_ZERO_RESERVE.md"
FIXTURE = HERE / (STEM + ".json")
MANIFEST = HERE / (STEM + ".sources.json")
TEST = ROOT / "tests" / ("test_" + STEM + ".py")
BASE = "8f01064df805624c045877655893c324a220975d"
SP = "e5e43625b157ecc5f602532e16a1197679594824"
PREREG = "79345ae1fd7f1721b5ef3d89f135f74c0ebd02e8"
MAX_BYTES = 1_000_000
H = 3_000_000_000_000
QS = (0, 1)
TS = (Q(1, 4), Q(1), Q(10), Q(100))
QUADS = (
    (Q(1), Q(2), Q(3), Q(4)),
    (Q(1), Q(3, 2), Q(5, 2), Q(5)),
    (Q(2), Q(3), Q(7), Q(11)),
)
POLE_MODELS = (
    ((Q(1), Q(0), 2), (Q(4), Q(0), 4)),
    ((Q(1), Q(1, 4), 2), (Q(1), Q(-1, 4), 2), (Q(9), Q(0), 2)),
    ((Q(4), Q(1, 3), 6), (Q(4), Q(-1, 3), 6), (Q(25), Q(0), 4)),
    ((Q(9), Q(1, 5), 2), (Q(9), Q(-1, 5), 2), (Q(16), Q(0), 8)),
    ((Q(1), Q(0), 2), (Q(4), Q(0), 2), (Q(16), Q(0), 2)),
    ((Q(1), Q(1, 10), 4), (Q(1), Q(-1, 10), 4), (Q(36), Q(0), 6)),
)
ATOM_MODELS = (
    ((Q(1), Q(2)), (Q(4), Q(4))),
    ((Q(1), Q(2)), (Q(4), Q(2)), (Q(9), Q(6))),
    ((Q(1), Q(4)), (Q(3), Q(2)), (Q(7), Q(8)), (Q(13), Q(2))),
)
SOURCES = (
    (PREREG, "research/exploratory/XI_FOUR_NODE_FAR_ZERO_RESERVE.md"),
    (SP, "research/exploratory/XI_SOURCE_POLARIZATION_FOUR_NODE.md"),
    (SP, "research/exploratory/xi_source_polarization_four_node.py"),
    (BASE, "research/integrated/xi_pick/ORDER_THREE_CANONICAL.md"),
    (BASE, "research/integrated/xi_pick/SOURCE_MANIFEST.tsv"),
    (
        "c079c2ef21022be951027de1316aecf1168422c1",
        "claims/lemmas/L-92000-three-node-caratheodory-determinant-factors-into-two-scalar-curvatures.md",
    ),
    (
        "880d14cb4bcbf542ec199137d60c58d9a8fd723d",
        "claims/lemmas/L-92102-the-complete-hypothetical-off-line-curvature-budget-uses-less-than-one-critical-orbit.md",
    ),
    (
        "db9a767e312d9928f5ef827762dcb4ef95494af0",
        "claims/lemmas/L-92202-verified-critical-reserve-closes-the-schwarzian-xi-impedance-curvature.md",
    ),
)
EXTERNAL = (
    {
        "url": "https://arxiv.org/pdf/2004.09765",
        "sha256": "3362f66af9fa9373977eee70e2282ec33989d5d8b97e0852df9e32cc25b52885",
        "read": "Theorem 1 rendered page 2",
    },
    {
        "url": "https://www.cs.uleth.ca/~kadiri/articles/New-Bounds-for-Psi-Math-Comp-Faber-Sept2013.pdf",
        "sha256": "a1d3f37e458d43a87bc33d5fe9c0d0d8d52ec34e8f610053dbdcb0f72a7c5be",
        "read": "Theorem 1.5 rendered page 3",
    },
    {
        "url": "https://www.cs.uleth.ca/~kadiri/articles/New-Bounds-for-Psi-Math-Comp-Faber-Corrigendum-Nov2017.pdf",
        "sha256": "d8f1c4ca69f53346465ec6fa1bbcdcc3c12946c51be56d6a8205efc826a95ddc",
        "read": "complete four-page corrigendum; zero-count constants retained",
    },
)
CONTRACT = {
    "schema": "xi-four-node-far-zero-reserve-v1",
    "arithmetic_class": "EXACT_RATIONAL",
    "normalization": "Y(x)=xi_R(1/2+x); p(t)=Y'(sqrt(t))/(sqrt(t)Y(sqrt(t)))",
    "native_domain": "analytic theorem t>1/4 and ordinary real safe-axis matrices of order at most four",
    "finite_scope": "six exact synthetic pole models, three atom models, four t values, fixed graph controls",
    "finite_role": "regression controls only; no zero computation and no machine proof of the analytic theorem",
    "published_inputs": "Platt-Trudgian partial RH and Rosser count via Faber-Kadiri; PDFs read but not downloaded by checker",
    "multiplicity": "w=2m retained; selected resources are distinct unordered pair terms, not scalar anchor reuse",
    "no_claim": "RH, order five or higher, source-kernel PSD, an independently rerun zero census, external novelty",
    "caps": {"bytes": MAX_BYTES, "integer_bits": 8192, "nodes": 100000, "depth": 24},
}


class C:
    __slots__ = ("i", "r")

    def __init__(self, r=0, i=0):
        self.r, self.i = Q(r), Q(i)

    def __add__(self, other):
        other = cc(other)
        return C(self.r + other.r, self.i + other.i)

    __radd__ = __add__

    def __neg__(self):
        return C(-self.r, -self.i)

    def __sub__(self, other):
        return self + (-cc(other))

    def __rsub__(self, other):
        return cc(other) - self

    def __mul__(self, other):
        other = cc(other)
        return C(
            self.r * other.r - self.i * other.i, self.r * other.i + self.i * other.r
        )

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = cc(other)
        d = other.r * other.r + other.i * other.i
        require(d != 0, "zero complex denominator")
        return C(
            (self.r * other.r + self.i * other.i) / d,
            (self.i * other.r - self.r * other.i) / d,
        )

    def __pow__(self, n):
        require(type(n) is int and n >= 0, "complex power cap")
        out, base = C(1), self
        while n:
            if n & 1:
                out = out * base
            base = base * base
            n //= 2
        return out

    def __eq__(self, other):
        other = cc(other)
        return self.r == other.r and self.i == other.i


def cc(value):
    return value if type(value) is C else C(value)


def require(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(value):
    return (
        json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True) + "\n"
    ).encode()


def sha(data):
    return hashlib.sha256(data).hexdigest()


def lf(data):
    return data.replace(b"\r\n", b"\n")


def pack(q):
    q = Q(q)
    return [q.numerator, q.denominator]


def unpack(pair):
    require(
        type(pair) is list and len(pair) == 2 and all(type(x) is int for x in pair),
        "rational shape",
    )
    require(pair[1] > 0, "rational denominator")
    q = Q(*pair)
    require(pack(q) == pair, "noncanonical rational")
    return q


def packc(z):
    return {"re": pack(z.r), "im": pack(z.i)}


def validate_tree(value, depth=0, visits=None):
    visits = [0] if visits is None else visits
    visits[0] += 1
    require(depth <= 24 and visits[0] <= 100000, "tree cap")
    if value is None or type(value) is bool:
        return
    if type(value) is int:
        require(value.bit_length() <= 8192, "integer cap")
        return
    if type(value) is str:
        require(value.isascii() and len(value) <= 4096, "string cap")
        return
    require(type(value) in (dict, list) and len(value) <= 4096, "container/type cap")
    if type(value) is dict:
        require(
            all(type(k) is str and k.isascii() and len(k) <= 4096 for k in value),
            "key cap",
        )
    for item in value.values() if type(value) is dict else value:
        validate_tree(item, depth + 1, visits)


def load(path):
    data = path.read_bytes()
    require(len(data) <= MAX_BYTES, "file cap")

    def pairs(items):
        out = {}
        for key, value in items:
            require(key not in out, "duplicate JSON key")
            out[key] = value
        return out

    value = json.loads(
        data,
        object_pairs_hook=pairs,
        parse_constant=lambda _: require(False, "nonfinite JSON"),
    )
    validate_tree(value)
    return value


def determinant(matrix):
    a = [list(row) for row in matrix]
    out = Q(1)
    for col in range(len(a)):
        pivot = next((i for i in range(col, len(a)) if a[i][col] != 0), None)
        if pivot is None:
            return Q(0)
        if pivot != col:
            a[pivot], a[col] = a[col], a[pivot]
            out = -out
        p = a[col][col]
        out *= p
        for j in range(col, len(a)):
            a[col][j] /= p
        for i in range(col + 1, len(a)):
            f = a[i][col]
            for j in range(col, len(a)):
                a[i][j] -= f * a[col][j]
    return out


def dispersion(poles, t, q):
    sr = {2: C(), 3: C(), 4: C()}
    for re, im, w in poles:
        s = C(re, im)
        r = Q(w) * (s**q)
        for k in sr:
            sr[k] += r / ((t + s) ** k)
    direct = 12 * (sr[2] * sr[4] - sr[3] * sr[3])
    paired = C()
    for left, right in itertools.combinations(poles, 2):
        si, sj = C(left[0], left[1]), C(right[0], right[1])
        paired += (
            12
            * left[2]
            * right[2]
            * ((si * sj) ** q)
            * ((si - sj) ** 2)
            / (((t + si) ** 4) * ((t + sj) ** 4))
        )
    require(direct.i == 0 and paired.i == 0, "conjugation failure")
    require(direct == paired, "pair dispersion mismatch")
    return direct.r


def p_atom(t, atoms):
    return sum(w / (t + s) for s, w in atoms)


def atom_control(atoms, xs):
    ts = [x * x for x in xs]
    ps = [p_atom(t, atoms) for t in ts]
    fs = [x * p for x, p in zip(xs, ps, strict=True)]
    h = [[(fs[i] + fs[j]) / (xs[i] + xs[j]) for j in range(4)] for i in range(4)]
    aa = determinant([[Q(1), ts[i], ps[i], ts[i] * ps[i]] for i in range(4)])
    ca = determinant(
        [[Q(1), ts[i], ts[i] * ps[i], ts[i] * ts[i] * ps[i]] for i in range(4)]
    )
    den = Q(1)
    for i, j in itertools.combinations(range(4), 2):
        den *= (xs[i] + xs[j]) ** 2
    dh = determinant(h)
    require(
        aa < 0 and ca < 0 and dh > 0 and dh == aa * ca / den, "atom factor/sign failure"
    )
    return {
        "atoms": [[pack(s), pack(w)] for s, w in atoms],
        "x": [pack(x) for x in xs],
        "A": pack(aa),
        "C": pack(ca),
        "det": pack(dh),
    }


def source_manifest():
    rows = []
    for commit, path in SOURCES:
        data = subprocess.check_output(["git", "show", f"{commit}:{path}"], cwd=ROOT)
        blob = subprocess.check_output(
            ["git", "rev-parse", f"{commit}:{path}"], cwd=ROOT, text=True
        ).strip()
        rows.append(
            {
                "commit": commit,
                "path": path,
                "git_blob": blob,
                "sha256_lf": sha(lf(data)),
            }
        )
    return {
        "schema": "xi-four-node-far-zero-reserve-sources-v1",
        "authoring_base": SP,
        "preregistered_design": PREREG,
        "sources": rows,
        "external_primary": list(EXTERNAL),
        "external_content_machine_authenticated": False,
    }


def artifact_seals():
    return {
        str(path.relative_to(ROOT)).replace("\\", "/"): sha(lf(path.read_bytes()))
        for path in (NOTE, Path(__file__), TEST, MANIFEST)
    }


def build():
    pair_rows = []
    for mi, poles in enumerate(POLE_MODELS):
        for t in TS:
            for q in QS:
                pair_rows.append(
                    {
                        "model": mi,
                        "t": pack(t),
                        "q": q,
                        "value": pack(dispersion(poles, t, q)),
                    }
                )
    atoms = [atom_control(model, xs) for model in ATOM_MODELS for xs in QUADS]
    negative = []
    for q in QS:
        value = dispersion(((Q(100), Q(5), 6), (Q(100), Q(-5), 6)), Q(1), q)
        require(value < 0, "missing negative-pair control")
        negative.append({"q": q, "value": pack(value)})
    cneg = {str(q): pack(Q(12 * 32 * (6**q) * 16) * Q(64, 9) ** 4) for q in QS}
    cpos = {str(q): pack(Q(84 * (2**q), 24**4)) for q in QS}
    require(all(unpack(cneg[str(q)]) < 2**28 for q in QS), "negative coefficient cap")
    require(
        all(unpack(cpos[str(q)]) > Q(1, 2**12) for q in QS),
        "positive coefficient floor",
    )
    require(H + 3 < 2**64 and H * H > 2**46, "height integer margin")
    shared = [(10, 25), (11, 25), (12, 25)]
    require(
        len({tuple(sorted(edge)) for edge in shared}) == len(shared),
        "shared edge collision",
    )
    reverse = [(10, 25), (25, 10)]
    require(
        len({tuple(sorted(edge)) for edge in reverse}) != len(reverse),
        "reverse must collide",
    )
    output = {
        "schema": CONTRACT["schema"],
        "contract": CONTRACT,
        "constants": {
            "H": H,
            "negative_coefficients": cneg,
            "positive_coefficients": cpos,
            "margin": {"H_plus_3_lt_2_pow_64": True, "H_sq_gt_2_pow_46": True},
            "phase": {
                "separated_numerator_lt": pack(Q(6, 5)),
                "denominator_weight_lt": pack(Q(1, 10)),
                "total_lt": pack(Q(13, 10)),
            },
            "count": {
                "rosser": [pack(Q(137, 1000)), pack(Q(443, 1000)), pack(Q(1588, 1000))],
                "local_weight_constant": 16,
            },
        },
        "dispersion": pair_rows,
        "atom_controls": atoms,
        "negative_without_reserve": negative,
        "allocation": {
            "shared_anchor_distinct": [list(x) for x in shared],
            "reverse_collision": [list(x) for x in reverse],
            "multiplicity_weights": [2, 4, 8],
        },
        "artifacts": artifact_seals(),
    }
    output["payload_sha256"] = sha(canonical(output))
    return output


def validate(value):
    require(
        type(value) is dict
        and set(value)
        == {
            "schema",
            "contract",
            "constants",
            "dispersion",
            "atom_controls",
            "negative_without_reserve",
            "allocation",
            "artifacts",
            "payload_sha256",
        },
        "top schema",
    )
    require(
        value["schema"] == CONTRACT["schema"] and value["contract"] == CONTRACT,
        "contract",
    )
    require(value == build(), "fresh exact reconstruction mismatch")
    payload = {k: v for k, v in value.items() if k != "payload_sha256"}
    require(value["payload_sha256"] == sha(canonical(payload)), "payload seal")
    require(load(MANIFEST) == source_manifest(), "source lock")
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--emit", action="store_true")
    parser.add_argument("--emit-sources", action="store_true")
    parser.add_argument("--write-fixture", action="store_true")
    args = parser.parse_args()
    if args.write_fixture:
        FIXTURE.write_bytes(canonical(build()))
    elif args.emit_sources:
        print(canonical(source_manifest()).decode(), end="")
    elif args.emit:
        print(canonical(build()).decode(), end="")
    elif args.check:
        validate(load(FIXTURE))
        print("PASS")
    else:
        print(canonical(build()).decode(), end="")


if __name__ == "__main__":
    main()
