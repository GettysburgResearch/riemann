"""Directed polynomial certificate for the fixed k(u)=3u^2 dual."""

import argparse
import importlib.util
import json
import sys
from fractions import Fraction as F
from hashlib import sha256
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE / "variational_certificate.py"
BASE_SHA = "aa25f2aec339ca0502f1591d6219bfe9a0b883a7ec19528383ac9c2230db04db"
ROOT_FILE = HERE / "variational_ordered_dual_refutation.verification.json"
ROOT_SHA = "6bdceb004b51241de904383f2a7318c52077e2c3adbcf7ea8dc9b06582c8769c"
CAP = 200000
MAX_DEPTH = 20


def require(ok, why):
    if not ok:
        raise ValueError(why)


def load_module():
    require(sha256(BASE.read_bytes()).hexdigest() == BASE_SHA, "pinned base")
    spec = importlib.util.spec_from_file_location("quadratic_pinned_base", BASE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


base = load_module()


def inverse_vandermonde(n):
    matrix = [
        [F(i) ** j for j in range(n + 1)] + [F(int(i == j)) for j in range(n + 1)]
        for i in range(n + 1)
    ]
    for p in range(n + 1):
        pivot = next(i for i in range(p, n + 1) if matrix[i][p])
        matrix[p], matrix[pivot] = matrix[pivot], matrix[p]
        q = matrix[p][p]
        matrix[p] = [x / q for x in matrix[p]]
        for i in range(n + 1):
            if i != p:
                q = matrix[i][p]
                matrix[i] = [x - q * y for x, y in zip(matrix[i], matrix[p])]
    return [row[n + 1 :] for row in matrix]


def interpolate(du, dv, function, arb):
    iu, iv = inverse_vandermonde(du), inverse_vandermonde(dv)
    values = [[function(arb(i), arb(j)) for j in range(dv + 1)] for i in range(du + 1)]
    return [
        [
            sum(
                values[i][j] * base.arb_fraction(iu[a][i] * iv[b][j], arb)
                for i in range(du + 1)
                for j in range(dv + 1)
            )
            for b in range(dv + 1)
        ]
        for a in range(du + 1)
    ]


def bernstein_range(coeff, urange, vrange, arb):
    du, dv = len(coeff) - 1, len(coeff[0]) - 1
    ua, ub = (base.arb_fraction(z, arb) for z in urange)
    va, vb = (base.arb_fraction(z, arb) for z in vrange)
    hu, hv = ub - ua, vb - va
    shifted = [[arb(0) for _ in range(dv + 1)] for _ in range(du + 1)]
    for r in range(du + 1):
        for s in range(dv + 1):
            shifted[r][s] = sum(
                coeff[i][j]
                * comb(i, r)
                * ua ** (i - r)
                * hu**r
                * comb(j, s)
                * va ** (j - s)
                * hv**s
                for i in range(r, du + 1)
                for j in range(s, dv + 1)
            )
    values = []
    for m in range(du + 1):
        for n in range(dv + 1):
            values.append(
                sum(
                    shifted[r][s]
                    * base.arb_fraction(
                        F(comb(m, r), comb(du, r)) * F(comb(n, s), comb(dv, s)), arb
                    )
                    for r in range(m + 1)
                    for s in range(n + 1)
                )
            )
    return min(base.bounds(x)[0] for x in values), max(
        base.bounds(x)[1] for x in values
    )


def polynomial_value(coeff, u, v, arb):
    return sum(
        (
            coeff[i][j] * u**i * v**j
            for i in range(len(coeff))
            for j in range(len(coeff[0]))
        ),
        arb(0),
    )


def holdout(coeff, function, arb, label):
    for a, b in ((F(1, 2), F(1, 3)), (F(2, 3), F(2, 5))):
        u, v = base.arb_fraction(a, arb), base.arb_fraction(b, arb)
        require(
            polynomial_value(coeff, u, v, arb).overlaps(function(u, v)),
            label + " degree holdout",
        )


def context():
    raw = ROOT_FILE.read_bytes()
    require(sha256(raw).hexdigest() == ROOT_SHA, "pinned root artifact")
    root = json.loads(raw, object_pairs_hook=base.unique_object)
    require(
        root["schema"] == "native-ordered-linear-dual-refutation/v1"
        and root["status"] == "CERTIFIED_REGISTERED_K1_K2_K3_DUALS_ALL_FAIL",
        "authenticated ordered root interface",
    )
    data = base.read_authenticated(base.GRAM_FILE, base.GRAM_SHA)
    sys.path.insert(0, str(Path.home() / ".cache/riemann-five-hour-deps"))
    from flint import arb, ctx

    ctx.prec = 192
    G = [[base.from_pair(x, arb) for x in row] for row in data["gram21_intervals"]]
    P = [[arb(0) for _ in range(7)] for _ in range(21)]
    for j in (0, 10, 12, 13, 14, 18, 20):
        P[j][0] = 1
    P[1][1] = 1
    P[10][2] = -2
    P[7][3] = 2
    for j in (2, 4, 17):
        P[j][4] = 1
    P[18][4] = -1
    for j in (13, 14, 20):
        P[j][5] = -2
    for j in (6, 8, 15):
        P[j][6] = 2
    y = [base.from_pair(pair, arb) for pair in root["krawczyk_image"]]
    a, b, c, d, t = y
    z = -a / b
    f = a + b * t
    x = [
        arb(1),
        1 - t + f * f / (2 * b),
        (1 - t * t) / 2 + a * (t * t - z * z) / 2 + b * (t**3 - z**3) / 3,
        (1 - t + f**3 / (3 * b)) / 2,
        c * (1 - t) + d * (1 - t * t) / 2,
        c * (1 - t * t) / 2 + d * (1 - t**3) / 3,
        (c * c * (1 - t) + c * d * (1 - t * t) + d * d * (1 - t**3) / 3) / 2,
    ]
    moments = [sum(P[i][j] * x[j] for j in range(7)) for i in range(21)]
    theta = base.matvec(G, moments, arb)
    return arb, theta, t, -a / b, root, y, moments, G


def build():
    arb, h, t, u0, _root, y, moments, G = context()
    cv = h[7]
    cw = h[6] + h[8] + h[15]
    require(cv > 0 and cw > 0, "positive profile coefficients")

    def ingredients(u, v):
        Lv = h[1] - 2 * h[10] * u
        p = (
            h[2]
            - 2 * u * h[13]
            + (h[4] - 2 * u * h[20]) * v
            + (h[17] - h[18] - 2 * u * h[14]) * v * v
            + 6 * u * (1 - v)
        )
        q = h[6] + h[15] * v + h[8] * v * v
        Lw = h[2] + h[4] + h[17] - h[18] - 2 * u * (h[13] + h[14] + h[20])
        x = 1 - v
        H0 = -Lv - cv * (v + 1)
        H1 = 6 * u - (h[4] - 2 * u * h[20]) - (h[17] - h[18] - 2 * u * h[14]) * (v + 1)
        H2 = -h[15] - h[8] * (v + 1)
        C = cw + x * H2
        L = Lw + x * H1
        N0 = Lw * Lw + 4 * cw * x * H0
        return Lv, p, q, Lw, C, L, N0, H0, H1, H2

    # Direct residual B-k on its four affine (v,w) corners.
    b_margins = []
    for v in (arb(0), arb(1)):
        for w in (arb(0), arb(1)):
            poly = interpolate(
                2,
                0,
                lambda u, _, v=v, w=w: (
                    h[3]
                    + h[5] * u
                    + (h[19] - h[20]) * u * u
                    - 2 * v * (h[12] + h[18] * u + h[14] * u * u)
                    + w * (h[9] + h[16] * u + h[11] * u * u)
                    - 3 * u * u
                ),
                arb,
            )
            holdout(
                poly,
                lambda u, _, v=v, w=w: (
                    h[3]
                    + h[5] * u
                    + (h[19] - h[20]) * u * u
                    - 2 * v * (h[12] + h[18] * u + h[14] * u * u)
                    + w * (h[9] + h[16] * u + h[11] * u * u)
                    - 3 * u * u
                ),
                arb,
                "B-k corner",
            )
            margin = bernstein_range(poly, (F(0), F(1)), (F(0), F(1)), arb)[0]
            require(margin > 0, "strict B-k residual")
            b_margins.append(margin)
    # Global easy sign gates.
    p2q = interpolate(
        1,
        2,
        lambda r, x: ingredients(t - r, 1 - x)[1] + 2 * ingredients(t - r, 1 - x)[2],
        arb,
    )
    holdout(
        p2q,
        lambda r, x: ingredients(t - r, 1 - x)[1] + 2 * ingredients(t - r, 1 - x)[2],
        arb,
        "p+2q",
    )
    require(
        bernstein_range(p2q, (F(0), base.bounds(t)[1]), (F(0), F(1)), arb)[0] > 0,
        "no early endpoint case",
    )
    qpoly = interpolate(0, 2, lambda _r, x: ingredients(t, 1 - x)[2], arb)
    holdout(qpoly, lambda _r, x: ingredients(t, 1 - x)[2], arb, "q")
    q_lower = bernstein_range(qpoly, (F(0), F(1)), (F(0), F(1)), arb)[0]
    require(q_lower > 0, "strict positive w-profile quadratic on the cube")
    l2c = interpolate(
        1,
        2,
        lambda r, x: ingredients(t + r, 1 - x)[5] + 2 * ingredients(t + r, 1 - x)[4],
        arb,
    )
    holdout(
        l2c,
        lambda r, x: ingredients(t + r, 1 - x)[5] + 2 * ingredients(t + r, 1 - x)[4],
        arb,
        "L+2C",
    )
    require(
        bernstein_range(l2c, (F(0), 1 - base.bounds(t)[0]), (F(0), F(1)), arb)[0] > 0,
        "no late endpoint case",
    )
    # Polynomial gates. Their exact calibrated constants/factors are installed below.
    ppoly = interpolate(1, 2, lambda r, x: ingredients(t - r, 1 - x)[1], arb)
    N = interpolate(
        2,
        4,
        lambda r, x: (
            ingredients(t - r, 1 - x)[2]
            * (2 * cv * (1 - x) + ingredients(t - r, 1 - x)[0]) ** 2
            - cv * ingredients(t - r, 1 - x)[1] ** 2
        ),
        arb,
    )
    holdout(ppoly, lambda r, x: ingredients(t - r, 1 - x)[1], arb, "early p")
    holdout(
        N,
        lambda r, x: (
            ingredients(t - r, 1 - x)[2]
            * (2 * cv * (1 - x) + ingredients(t - r, 1 - x)[0]) ** 2
            - cv * ingredients(t - r, 1 - x)[1] ** 2
        ),
        arb,
        "early N",
    )
    lo, hi = base.bounds(N[0][0])
    require(lo <= 0 <= hi, "fifth root equality enclosed")
    N[0][0] = arb(0)  # exact fifth root equation at (r,x)=(0,0)
    # Late N0 is an exact square at r=0 plus r times a polynomial.
    r0 = 1 + ingredients(t, arb(1))[0] / (2 * cv)

    def qn_parts(x):
        square = 4 * cw * cv * (x - r0) ** 2
        q1 = ingredients(t + 1, 1 - x)[6] - square
        q2 = (ingredients(t + 2, 1 - x)[6] - square) / 2
        return 2 * q1 - q2, q2 - q1

    qna = interpolate(0, 2, lambda _r, x: qn_parts(x)[0], arb)[0]
    qnb = interpolate(0, 2, lambda _r, x: qn_parts(x)[1], arb)[0]
    Qn = [qna, qnb]
    for xcheck in (arb(0), base.arb_fraction(F(1, 3), arb)):
        require(
            ingredients(t, 1 - xcheck)[6].overlaps(4 * cw * cv * (xcheck - r0) ** 2),
            "late calibrated square identity enclosed",
        )
    holdout(
        Qn,
        lambda r, x: (ingredients(t + r, 1 - x)[6] - 4 * cw * cv * (x - r0) ** 2) / r,
        arb,
        "late N0 quotient",
    )
    Gfull = interpolate(
        2,
        4,
        lambda r, x: (
            ingredients(t + r, 1 - x)[4] * ingredients(t + r, 1 - x)[6]
            - cw * ingredients(t + r, 1 - x)[5] ** 2
        ),
        arb,
    )
    # G(r,0)=0 identically; divide by x exactly.
    for row in Gfull:
        lo, hi = base.bounds(row[0])
        require(lo <= 0 <= hi, "late exact x factor enclosed")
        row[0] = arb(0)
    Gn = [row[1:] for row in Gfull]
    holdout(
        Gn,
        lambda r, x: (
            (
                ingredients(t + r, 1 - x)[4] * ingredients(t + r, 1 - x)[6]
                - cw * ingredients(t + r, 1 - x)[5] ** 2
            )
            / x
        ),
        arb,
        "late vertex x quotient",
    )
    # Adaptive cells use Bernstein ranges and retain UNKNOWN at the cap.
    counters = {
        "clipped_cells": 0,
        "early_cells": 0,
        "late_cells": 0,
        "maximum_depth": 0,
    }
    Lpoly = interpolate(1, 2, lambda r, x: ingredients(t + r, 1 - x)[5], arb)
    holdout(Lpoly, lambda r, x: ingredients(t + r, 1 - x)[5], arb, "late L")

    def early(cell, depth=0):
        counters["early_cells"] += 1
        counters["maximum_depth"] = max(counters["maximum_depth"], depth)
        require(
            sum(counters[k] for k in ("clipped_cells", "early_cells", "late_cells"))
            <= CAP,
            "subdivision cap UNKNOWN",
        )
        pr = bernstein_range(ppoly, *cell, arb)
        nr = bernstein_range(N, *cell, arb)
        if pr[0] >= 0 or nr[0] >= 0:
            return
        require(depth < MAX_DEPTH, "early unresolved UNKNOWN")
        (a, b), (c, d) = cell
        if b - a >= d - c:
            m = (a + b) / 2
            early(((a, m), (c, d)), depth + 1)
            early(((m, b), (c, d)), depth + 1)
        else:
            m = (c + d) / 2
            early(((a, b), (c, m)), depth + 1)
            early(((a, b), (m, d)), depth + 1)

    def late(cell, depth=0):
        counters["late_cells"] += 1
        counters["maximum_depth"] = max(counters["maximum_depth"], depth)
        require(
            sum(counters[k] for k in ("clipped_cells", "early_cells", "late_cells"))
            <= CAP,
            "subdivision cap UNKNOWN",
        )
        # N0 square plus positive-r guard, and factored vertex gate.
        qnr = bernstein_range(Qn, *cell, arb)
        gnr = bernstein_range(Gn, *cell, arb)
        lr = bernstein_range(Lpoly, *cell, arb)
        if qnr[0] >= 0 and (lr[0] >= 0 or gnr[0] >= 0):
            return
        require(depth < MAX_DEPTH, "late unresolved UNKNOWN")
        (a, b), (c, d) = cell
        if b - a >= d - c:
            m = (a + b) / 2
            late(((a, m), (c, d)), depth + 1)
            late(((m, b), (c, d)), depth + 1)
        else:
            m = (c + d) / 2
            late(((a, b), (c, m)), depth + 1)
            late(((a, b), (m, d)), depth + 1)

    # Below u0, the true clipped v-profile is zero; certify A_K>=0.
    pclip = interpolate(1, 2, lambda u, x: ingredients(u, 1 - x)[1], arb)
    Nclip = interpolate(
        2,
        4,
        lambda u, x: (
            4
            * ingredients(u, 1 - x)[2]
            * (ingredients(u, 1 - x)[0] * (1 - x) + cv * (1 - x) ** 2)
            - ingredients(u, 1 - x)[1] ** 2
        ),
        arb,
    )
    holdout(pclip, lambda u, x: ingredients(u, 1 - x)[1], arb, "clipped p")
    holdout(
        Nclip,
        lambda u, x: (
            4
            * ingredients(u, 1 - x)[2]
            * (ingredients(u, 1 - x)[0] * (1 - x) + cv * (1 - x) ** 2)
            - ingredients(u, 1 - x)[1] ** 2
        ),
        arb,
        "clipped N",
    )

    def clipped(cell, depth=0):
        counters["clipped_cells"] += 1
        counters["maximum_depth"] = max(counters["maximum_depth"], depth)
        require(
            sum(counters[k] for k in ("clipped_cells", "early_cells", "late_cells"))
            <= CAP,
            "subdivision cap UNKNOWN",
        )
        pr = bernstein_range(pclip, *cell, arb)
        nr = bernstein_range(Nclip, *cell, arb)
        if pr[0] >= 0 or nr[0] >= 0:
            return
        require(depth < MAX_DEPTH, "clipped unresolved UNKNOWN")
        (a, b), (c, d) = cell
        if b - a >= d - c:
            m = (a + b) / 2
            clipped(((a, m), (c, d)), depth + 1)
            clipped(((m, b), (c, d)), depth + 1)
        else:
            m = (c + d) / 2
            clipped(((a, b), (c, m)), depth + 1)
            clipped(((a, b), (m, d)), depth + 1)

    clipped(((F(0), base.bounds(u0)[1]), (F(0), F(1))))
    # In r=t-u coordinates, the unclipped branch begins at u0.
    early(((F(0), base.bounds(t)[1] - base.bounds(u0)[0]), (F(0), F(1))))
    late(((F(0), 1 - base.bounds(t)[0]), (F(0), F(1))))
    energy = base.bilinear(moments, G, moments, arb)
    return {
        "schema": "native-quadratic-dual-global-certificate/v1",
        "status": "CERTIFIED_GLOBAL_ORIGINAL_OPTIMIZER",
        "root_input_sha256": ROOT_SHA,
        "variational_base_sha256": BASE_SHA,
        "k_of_u": "3*u^2",
        "B_minus_k_lower": str(min(b_margins)),
        "w_quadratic_lower": str(q_lower),
        "subdivision": counters,
        "ordered_parameters": list(map(base.encoded, y)),
        "ordered_moment21": list(map(base.encoded, moments)),
        "ordered_energy": base.encoded(energy),
        "global_all_monotone_paths": True,
        "full_retained_gamma_identified": False,
    }


def main():
    parser = argparse.ArgumentParser()
    m = parser.add_mutually_exclusive_group(required=True)
    m.add_argument("--write", action="store_true")
    m.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build()
    result["producer_sha256"] = sha256(Path(__file__).read_bytes()).hexdigest()
    result["preregistration_sha256"] = sha256(
        (HERE / "variational_QUADRATIC_DUAL_PREREGISTRATION.md").read_bytes()
    ).hexdigest()
    result["ordered_dual_theorem_sha256"] = sha256(
        (HERE / "variational_ORDERED_DUAL_THEOREM.md").read_bytes()
    ).hexdigest()
    result["global_theorem_sha256"] = sha256(
        (HERE / "INFINITE_GLOBAL_OPTIMAL_ACTIVATION_PATH.md").read_bytes()
    ).hexdigest()
    result["preserved_invalid_first_output_sha256"] = sha256(
        (
            HERE / "variational_quadratic_dual.invalid_missing_lower_clip.v1.json"
        ).read_bytes()
    ).hexdigest()
    path = HERE / "variational_quadratic_dual.verification.json"
    if args.write:
        path.write_text(
            json.dumps(result, indent=2, allow_nan=False) + "\n", encoding="utf8"
        )
    else:
        require(
            base.typed_equal(
                json.loads(path.read_text(), object_pairs_hook=base.unique_object),
                result,
            ),
            "typed replay",
        )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
