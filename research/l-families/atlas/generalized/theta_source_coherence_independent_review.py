"""Independent exact SC audit; no scientific-author module is imported."""

import hashlib
import itertools
import json
import subprocess
from pathlib import Path

import sympy as S

ROOT = Path(__file__).resolve().parents[4]
DIR = "research/l-families/atlas/generalized/"
SCIENCE = "b0e3b18e690accdee6d77b3b3c4c68850f6cb671"
STEM = "theta_source_quotient_tensor_coherence"
FIXTURE_SHA = "6413c704116108ab3f1a06400087b8154297ffe13f3631436a96b49502ee3419"
I = S.I
COUNT = {}
VALUES = []


def need(ok, label):
    if not ok:
        raise ValueError(label)
    COUNT[label] = COUNT.get(label, 0) + 1


def raw(path, commit=SCIENCE):
    return subprocess.check_output(["git", "show", commit + ":" + path], cwd=ROOT)


def lf(data):
    return data.replace(b"\r\n", b"\n")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def canon(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def clean(a):
    return S.Matrix(a).applyfunc(lambda x: S.cancel(S.expand_complex(x)))


def equal(a, b, label):
    need(clean(S.Matrix(a) - S.Matrix(b)) == S.zeros(*S.Matrix(a).shape), label)


def matrix(data):
    return S.Matrix(
        [[S.Rational(x) + I * S.Rational(y) for x, y in row] for row in data]
    )


def qp(h, p):
    h, p = clean(h), clean(p)
    n, r = h.rows, p.rows
    # Solve the constrained stationary-energy system, not the author's inverse formula.
    kkt = h.row_join(p.H).col_join(p.row_join(S.zeros(r)))
    solution = clean(kkt.inv(method="DM") * S.zeros(n, r).col_join(S.eye(r)))
    j = solution[:n, :]
    q = clean(j.H * h * j)
    equal(p * j, S.eye(r), "KKT_right_inverse")
    equal(h * j + p.H * solution[n:, :], S.zeros(n, r), "KKT_stationarity")
    equal(q, -solution[n:, :], "KKT_energy_multiplier")
    return q, j


def positive(h, strict, label):
    h = clean(h)
    equal(h, h.H, "Hermitian")
    for n in range(1, h.rows + 1):
        for ix in itertools.combinations(range(h.rows), n):
            d = S.factor(h.extract(ix, ix).det(method="bareiss"))
            need(d > 0 if strict else d >= 0, label)


def record_energy(h, p, record):
    q, j = qp(h, p)
    equal(q, matrix(record["quotient"]), "record_quotient")
    equal(j, matrix(record["lift"]), "record_lift")
    positive(q, True, "quotient_PD")
    positive(h - p.H * q * p, False, "maximal_metric_contraction")
    VALUES.append(str(q))


def main():
    fixture_bytes = raw(DIR + STEM + ".json")
    need(sha(lf(fixture_bytes)) == FIXTURE_SHA, "frozen_fixture_identity")
    report = json.loads(fixture_bytes)
    seal = report.pop("payload_sha256")
    need(sha(canon(report)) == seal, "full_payload_seal")
    for path, digest in report["artifact_sha256_lf"].items():
        need(sha(lf(raw(path))) == digest, "science_artifact_seal")
    need(len(report["sources"]) == 7, "source_count")
    for row in report["sources"]:
        data = raw(row["path"], row["commit"])
        blob = hashlib.sha1(
            b"blob " + str(len(data)).encode() + b"\0" + data
        ).hexdigest()
        need(
            blob == row["git_blob"] and sha(lf(data)) == row["sha256_lf"],
            "Git_source_identity",
        )
    need(report["coverage"]["parameters"] == ["3/2", "2", "3"], "full_parameter_panel")
    for row in report["base_cells"]:
        h, g, p, c, b = (matrix(row[k]) for k in ("H", "G", "pi", "C", "B"))
        record_energy(h, p, row["source"])
        record_energy(g, p, row["vacuum"])
        q, j = qp(h, p)
        gq, _ = qp(g, p)
        equal((q - gq) / 2, matrix(row["excess"]), "source_excess")
        t = S.Rational(row["t"])
        a = row["alpha"]
        equal(
            (t**a * q - gq) / 2, matrix(row["reciprocal_excess"]), "reciprocal_excess"
        )
        pp = clean(b.inv() * p * c)
        hqp, jp = qp(c.H * h * c, pp)
        gqp, _ = qp(c.H * g * c, pp)
        equal(hqp, b.H * q * b, "nonunitary_source_covariance")
        equal(gqp, b.H * gq * b, "nonunitary_vacuum_covariance")
        equal(jp, c.inv() * j * b, "nonunitary_lift_covariance")
    for row in report["tensor_cells"]:
        h, g, p = (matrix(row[k]) for k in ("H", "G", "pi"))
        record_energy(h, p, row["source"])
        record_energy(g, p, row["vacuum"])
        positive(h - g, False, "tensor_excess_PSD")
        q, _ = qp(h, p)
        equal(
            S.Rational(row["t"]) ** 3 * q,
            matrix(row["reciprocal_quotient"]),
            "tensor_reciprocity",
        )
    for row in report["same_weight_sums"]:
        t = S.Rational(row["t"])
        base = [r for r in report["base_cells"] if S.Rational(r["t"]) == t]
        h = S.diag(*(matrix(r["H"]) for r in base))
        g = S.diag(*(matrix(r["G"]) for r in base))
        p = S.diag(*(matrix(r["pi"]) for r in base))
        record_energy(h, p, row["source"])
        record_energy(g, p, row["vacuum"])
    for row in report["nested_chains"]:
        t = S.Rational(row["t"])
        base = [r for r in report["base_cells"] if S.Rational(r["t"]) == t]
        for chain in row["chains"]:
            key = "H" if chain["kind"] == "source" else "G"
            h = S.kronecker_product(*(matrix(r[key]) for r in base))
            current = h
            composite = S.eye(4)
            lift = S.eye(4)
            for stage in chain["stages"]:
                p = matrix(stage["map"])
                current, newlift = qp(current, p)
                lift = clean(lift * newlift)
                composite = p * composite
                q, j = qp(h, composite)
                equal(q, current, "nested_quotient_associativity")
                equal(j, lift, "nested_lift_associativity")
                equal(q, matrix(stage["quotient"]), "nested_record_quotient")
                equal(j, matrix(stage["lift"]), "nested_record_lift")
    for row in report["averaging"]:
        hs = [matrix(h) for h in row["H"]]
        ds = [matrix(d) for d in row["D"]]
        ls = [matrix(l) for l in row["L"]]
        weights = list(map(S.Rational, row["weights"]))
        hbar = sum((w * h for w, h in zip(weights, hs)), S.zeros(4))
        dbar = sum((w * d for w, d in zip(weights, ds)), S.zeros(2))
        dl = sum((w * d * l for w, d, l in zip(weights, ds, ls)), S.zeros(2))
        lbar = clean(dbar.inv() * dl)
        p = S.eye(4)[:2, :]
        q, _ = qp(hbar, p)
        meanq = sum((w * qp(h, p)[0] for w, h in zip(weights, hs)), S.zeros(2))
        defect = clean(q - meanq)
        variance = clean(
            sum(
                (w * (l - lbar).H * d * (l - lbar) for w, d, l in zip(weights, ds, ls)),
                S.zeros(2),
            )
        )
        equal(defect, variance, "independent_averaging_variance")
        equal(defect, matrix(row["defect"]), "averaging_record")
        need(
            S.factor(defect.det()) == S.Rational(row["determinant"]),
            "averaging_exact_determinant",
        )
        positive(defect, not row["common_lift"], "averaging_PSD_or_PD")
    s = S.symbols("s")
    l1 = 1 / (2 * s * (s - 1))
    l2 = 1 / (s * (s - 2))
    l3 = 3 / (2 * s * (s - 3))
    polynomial = S.expand(
        S.cancel((l3 - l1 * l2) * 2 * s * s * (s - 1) * (s - 2) * (s - 3))
    )
    need(
        polynomial == 3 * s**3 - 9 * s**2 + 5 * s + 3,
        "Mellin_nonmultiplicative_polynomial",
    )
    # Extra deterministic rational complex subspaces, outside the scientific panel.
    for j in range(1, 13):
        n = 2 + j % 3
        r = 1 + j % (n - 1)
        b = S.Matrix(
            n,
            n,
            lambda x, y, j=j: (
                S.Rational((x + 1) * (y + 2) + j, 13) + I * S.Rational(x - y, 7)
            ),
        )
        h = clean(S.eye(n) + b.H * b)
        p = S.eye(n)[:r, :]
        for x in range(r):
            for y in range(r, n):
                p[x, y] = S.Rational(j + x + y, 11) + I * S.Rational(x - y, 5)
        q, lift = qp(h, p)
        direct = clean((p * h.inv() * p.H).inv())
        equal(q, direct, "heldout_inverse_vs_KKT")
        positive(h - p.H * q * p, False, "heldout_maximality")
        c = S.eye(n)
        c[0, n - 1] = S.Rational(j, 9) + I
        qc, jc = qp(c.H * h * c, p * c)
        equal(qc, q, "heldout_coordinate_covariance")
        equal(jc, c.inv() * lift, "heldout_coordinate_lift")
    output = {
        "schema": "SC-independent-audit-v1",
        "science_head": SCIENCE,
        "fixture_sha256_lf": FIXTURE_SHA,
        "status": "PASS",
        "checks": COUNT,
        "extra_heldout_complex_subspaces": 12,
        "independent_quotient_method": "KKT constrained energy solve in SymPy",
        "author_arithmetic_imported": False,
        "quotient_stream_sha256": sha("\n".join(VALUES).encode()),
        "reviewer_sha256_lf": sha(lf(Path(__file__).read_bytes())),
        "scope": "Finite algebra/source identity only; analytic proof reviewed separately.",
    }
    print(json.dumps(output, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
