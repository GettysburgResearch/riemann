"""Complete fixed-box Xi companion counts and finite physical compression."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction as Q
from pathlib import Path

import xi_companion_off_axis_ball_certificates as oa
from flint import acb, acb_mat, acb_series, arb, ctx

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
STEM = "xi_companion_box_count_compression"
NOTE = HERE / "XI_COMPANION_BOX_COUNT_COMPRESSION.md"
MANIFEST = HERE / (STEM + ".sources.json")
FIXTURE = HERE / (STEM + ".json")
TEST = ROOT / "tests" / ("test_" + STEM + ".py")
BASE = "134a55016b4f3ea970dc8e5f03505d4e97afff07"
MAX_BYTES, MAX_NODES, MAX_DEPTH = 12_000_000, 300_000, 24
BINDINGS = [
    {
        "commit": "134a55016b4f3ea970dc8e5f03505d4e97afff07",
        "git_blob": "625cc29f67510bd58ed667f6f5fec242b84e4a11",
        "id": "OA1",
        "path": "research/exploratory/XI_COMPANION_OFF_AXIS_BALL_CERTIFICATES.md",
        "role": "complete parent proof and normalization",
        "sha256_lf": "020597b67044d996e12e2f76655550557cc33cd52cf717553e2fc6be9d48e396",
    },
    {
        "commit": "134a55016b4f3ea970dc8e5f03505d4e97afff07",
        "git_blob": "b0cecac35dcdb3a583ae891609d7d89b378b537b",
        "id": "OA2",
        "path": "research/exploratory/xi_companion_off_axis_ball_certificates.py",
        "role": "executed frozen ball/runtime/source helpers",
        "sha256_lf": "319e9abf775199e1747b0642dd99f24e52d9700bf71c04385d02cf5be9aac15f",
    },
    {
        "commit": "134a55016b4f3ea970dc8e5f03505d4e97afff07",
        "git_blob": "e7cdd61fcc046d142ccc95b5796d3106a79139c4",
        "id": "OA3",
        "path": "research/exploratory/xi_companion_off_axis_ball_certificates.json",
        "role": "frozen nine-node fixture",
        "sha256_lf": "268e67f84bdae5d41a4acb95df96fff18e00c3d0ae3430a9be8c89f633ff7c5b",
    },
    {
        "commit": "134a55016b4f3ea970dc8e5f03505d4e97afff07",
        "git_blob": "06434dc776028d155b8107f8cb5ea8687a3ce9dc",
        "id": "OA4",
        "path": "research/exploratory/xi_companion_off_axis_ball_certificates.sources.json",
        "role": "parent transitive source manifest",
        "sha256_lf": "eec3231292d8d5b030c68ffaed9520dd5697657dcd17f15c91e4f34ee8f9be4c",
    },
    {
        "commit": "134a55016b4f3ea970dc8e5f03505d4e97afff07",
        "git_blob": "f1f323d579968949cf07c662dd245172380759ba",
        "id": "OA5",
        "path": "tests/test_xi_companion_off_axis_ball_certificates.py",
        "role": "frozen parent tests",
        "sha256_lf": "3cfd3a3c2177ccbb242aeb5a9fa7e83b27859f9485a532489304019499b8dcd7",
    },
    {
        "commit": "7aed2ec0b99b9d7f2fb94a774922a83d5b84a870",
        "git_blob": "cd74bd06267eb4d60bc977353d11f6a0fb72ba6a",
        "id": "CP",
        "path": "research/exploratory/COPRIME_INFINITE_HEIGHT_PHYSICAL_CAPTURE.md",
        "role": "CP2-4 coprime infinite-height does not imply corrected physical trace divergence",
        "sha256_lf": "b9ab266898129389b94a9ed494b140422fc823552c6b69bf22ed36a9dbb2e7f7",
    },
    {
        "commit": "81d52e569cc8bb566e54043fd692fd6157406aab",
        "git_blob": "7fbf3731f286ddfc9eb1d10ede5941ab2156817a",
        "id": "L106620",
        "path": "claims/lemmas/L-106620-mesoscopic-frozen-riemann-siegel-gauge.md",
        "role": "L106620.1,.4-.6 constant positive lambda and native Theta0/Theta5",
        "sha256_lf": "23e368f246606b0a8b4f53bec9e65e1dec21bdd207197387461268b4ca1bb7d0",
    },
    {
        "commit": "81d52e569cc8bb566e54043fd692fd6157406aab",
        "git_blob": "16ab64a193e59608c9e2c9fd9762addc58809c3f",
        "id": "L106610",
        "path": "claims/lemmas/L-106610-riemann-siegel-gauge-factorization.md",
        "role": "Exact Riemann-Siegel phase and digamma derivative of the native freezing scale",
        "sha256_lf": "11c87fd9b50c309249b76f39fd87c3d20953779355a39a0338ef281d3cb57c87",
    },
]
CONTRACT = {
    "primitive": "actual unrescaled Xi and exact fixed inverse phase derivative",
    "coverage": "complete three open boxes (a-6,a+6)+i(0,1), anchors32/64/128, zero-free closed boundaries",
    "counts": "3/5/6 R5 zeros, all individually simple and locally noncommon",
    "boundary": "416 exact arcs each, 32-term point Taylor plus Cauchy analytic remainder, rational polygon winding",
    "arithmetic": "pinned FLINT complex balls plus exact Fraction winding and acceptance",
    "metric": "boundary dx Hardy norm; physical P_U=P_(U H2), input Gram H=V G Vstar",
    "common_factor": "conditional global Loewner comparison H_reduced >= H_raw without parameter nonexceptionality",
    "compression": "finite input space, global output; trace and rational Rayleigh lower bounds",
    "exclusions": "no Fourier-band/outer-metric/high-T/cofinal/HS-infinity/RH inference",
    "trust": "same OA pinned FLINT implementation, not a formally verified special-function implementation",
}
RAYS = {
    32: ((-213, -576), (-273, 208), (408, 939)),
    64: ((301, -269), (-466, -355), (-704, 743), (167, 160), (115, 5)),
    128: ((-203, 212), (539, 575), (623, -813), (-11, -502), (-282, -66), (-102, 83)),
}
THRESHOLDS = {32: (1193, 748), 64: (1551, 816), 128: (1343, 747)}

EXTRA_DISKS = (
    (
        64,
        89246822394291085971055228598899229934890421865207527222,
        831971810680942459148832997870701903337308494688414735,
        593,
    ),
    (
        64,
        102004593390668729235740140353283653476191447323278731032,
        816690616333815252293049344731810989125916276635365620,
        472,
    ),
    (
        128,
        188328005253439789770602052305798809772619070813439148964,
        697729877234208526671834124481848784867283726271264107,
        366,
    ),
    (
        128,
        194622930381077233407594944948225595830262815486617994846,
        753286813314656565110293595763335624692968643841769266,
        544,
    ),
    (
        128,
        201221008365065741142160803773279886369888352856018278912,
        679064127394664641078002091564309487657666541070583972,
        194,
    ),
)
DISKS = tuple(sorted(oa.DISKS + EXTRA_DISKS))


def root_record(data):
    oa.require(type(data) is tuple and len(data) == 4, "root tuple")
    anchor, nx, ny, coarse = data
    oa.integer(anchor, 32, 128)
    oa.require(anchor in (32, 64, 128), "root anchor")
    oa.integer(nx, 1, 2**200)
    oa.integer(ny, 1, 2**200)
    oa.integer(coarse, 1, 999)
    x, y, r = Q(nx, 2**180), Q(ny, 2**180), Q(1, 2**120)
    oa.require(anchor - 6 < x - r < x + r < anchor + 6, "root real domain")
    oa.require(0 < y - r < y + r < 1, "root imaginary domain")
    center = acb(oa.qarb(x), oa.qarb(y))
    box = acb(arb(center.real, oa.qarb(r)), arb(center.imag, oa.qarb(r)))
    lam = oa.frozen_lambda(anchor)
    point, region = oa.xi_jet(center), oa.xi_jet(box)
    reflected = oa.xi_jet(box, reflected=True)
    oa.require(all(v.overlaps(w) for v, w in zip(region, reflected)), "reflected jet")
    p, q = oa.companions(point, lam), oa.companions(region, lam)
    a, d, m = (
        oa.endpoint(p["R5"].abs_upper()),
        oa.endpoint(p["R5prime"].abs_lower()),
        oa.endpoint(q["R5second"].abs_upper()),
    )
    left, right = oa.rouche_bounds(a, d, m, r)
    oa.require(oa.unpair(left) * 2**50 < oa.unpair(right), "root slack")
    nonzero = {}
    for key in ("C5", "R0", "C0", "f6", "W", "R5prime"):
        bound = oa.endpoint(q[key].abs_lower())
        oa.require(bound > 0, "root noncommon: " + key)
        nonzero[key] = oa.pair(bound)
    theta = oa.theta_jets(region, lam)[0]
    oa.require(
        abs(theta) > oa.qarb(Q(coarse, 1000))
        and abs(theta) < oa.qarb(Q(coarse + 1, 1000)),
        "raw corridor",
    )
    row = {
        "anchor": anchor,
        "center": [oa.pair(x), oa.pair(y)],
        "radius": oa.pair(r),
        "point_derivatives": [oa.cbounds(v) for v in point],
        "rectangle_derivatives": [oa.cbounds(v) for v in region],
        "reflected_rectangle_derivatives": [oa.cbounds(v) for v in reflected],
        "rouche": {
            "residual": oa.pair(a),
            "derivative": oa.pair(d),
            "second": oa.pair(m),
            "left": left,
            "right": right,
        },
        "nonzero": nonzero,
        "raw_theta": oa.cbounds(theta),
        "raw_modulus": oa.rbounds(abs(theta)),
        "raw_corridor": [oa.pair(Q(coarse, 1000)), oa.pair(Q(coarse + 1, 1000))],
    }
    return row, box, theta


def physical_matrices(nodes, values):
    oa.require(type(nodes) is list and type(values) is list, "matrix input lists")
    n = len(nodes)
    oa.require(1 <= n <= 6 and len(values) == n, "matrix order")
    oa.require(
        all(type(z) is acb and z.is_finite() and z.imag > 0 for z in nodes),
        "upper half-plane nodes",
    )
    oa.require(all(type(z) is acb and z.is_finite() for z in values), "finite values")
    gram = acb_mat(
        [
            [
                1
                / (
                    nodes[i].imag
                    + nodes[j].imag
                    + acb(0, 1) * (nodes[j].real - nodes[i].real)
                )
                for j in range(n)
            ]
            for i in range(n)
        ]
    )
    physical = acb_mat(
        [
            [values[i] * gram[i, j] * values[j].conjugate() for j in range(n)]
            for i in range(n)
        ]
    )
    return gram, physical


def compression(anchor):
    with oa.precision():
        records = [root_record(d) for d in DISKS if d[0] == anchor]
        rows, nodes, values = map(list, zip(*records))
        gram, physical = physical_matrices(nodes, values)
        inverse = gram.inv()
        value = (inverse * physical).trace()
        oa.require(
            value.is_finite() and value.imag.contains(0),
            "finite real compression trace",
        )
        return rows, gram, physical, value


def xi_series(z, cap=39, reflected=False):
    oa.require(type(z) is acb and z.is_finite(), "finite input")
    oa.integer(cap, 9, 64)
    oa.require(192 <= ctx.prec <= 512, "precision cap")
    oa.require(type(reflected) is bool, "strict route")
    oa.require(20 < z.real and z.real < 150 and -1 < z.imag and z.imag < 2, "domain")
    previous = ctx.cap
    ctx.cap = cap
    try:
        s = acb(arb(1) / 2) + acb(0, 1) * acb_series([z, 1])
        if reflected:
            s = 1 - s
        v = s * (s - 1) / 2 * (-s / 2 * arb.pi().log()).exp()
        v = v * (s / 2).gamma() * s.zeta()
        result = [v[j] for j in range(cap)]
        oa.require(all(v.is_finite() for v in result), "nonfinite series")
        return result
    finally:
        ctx.cap = previous


def xi_value(z):
    oa.require(type(z) is acb and z.is_finite(), "finite scalar input")
    oa.require(
        20 < z.real and z.real < 150 and -1 < z.imag and z.imag < 2, "scalar domain"
    )
    oa.require(192 <= ctx.prec <= 512, "scalar precision")
    s = acb(arb(1) / 2) + acb(0, 1) * z
    return (
        s * (s - 1) / 2 * (-s / 2 * arb.pi().log()).exp() * (s / 2).gamma() * s.zeta()
    )


def fcoeff(z, lam, terms=32):
    oa.integer(terms, 2, 32)
    oa.require(type(lam) is arb and lam > 0, "positive lambda")
    v = xi_series(z, terms + 7)
    return [
        v[n + 5] * (math.factorial(n + 5) // math.factorial(n))
        - acb(0, 1) * lam * v[n + 6] * (math.factorial(n + 6) // math.factorial(n))
        for n in range(terms)
    ]


def vertex(x, y, lam):
    v = xi_series(acb(oa.qarb(x), oa.qarb(y)), 9)
    value = 120 * v[5] - acb(0, 1) * lam * 720 * v[6]
    return [oa.endpoint(value.real.mid()), oa.endpoint(value.imag.mid())]


def arc(p, q, lam):
    for point in (p, q):
        oa.require(type(point) in (list, tuple) and len(point) == 2, "arc point shape")
        for v in point:
            oa.rational(v)
    oa.require(type(lam) is arb and lam > 0, "arc positive lambda")
    x, y = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2
    dx, dy = abs(p[0] - q[0]) / 2, abs(p[1] - q[1]) / 2
    oa.require(dx == 0 or dy == 0, "axis aligned arc")
    h = dx + dy
    oa.require(0 < h <= Q(1, 32), "arc length")
    c = acb(oa.qarb(x), oa.qarb(y))
    coeff = fcoeff(c, lam)
    delta = acb(arb(0, oa.qarb(dx)), arb(0, oa.qarb(dy)))
    value = acb(0)
    for v in reversed(coeff):
        value = value * delta + v
    outer = acb(arb(c.real, arb(1) / 4), arb(c.imag, arb(1) / 4))
    mxi = xi_value(outer).abs_upper()
    mf = mxi * (120 * 8**5 + lam * 720 * 8**6)
    t = oa.qarb(8 * h)
    error = mf * t**32 / (1 - t)
    err = error.upper()
    value += acb(arb(0, err), arb(0, err))
    oa.require(
        value.is_finite() and not value.contains(0), "boundary image excludes zero"
    )
    return value, oa.endpoint(mxi), oa.endpoint(err)


def boundary(anchor):
    oa.integer(anchor, 32, 128)
    oa.require(anchor in (32, 64, 128), "anchor set")
    left, right = Q(anchor - 6), Q(anchor + 6)
    points = []
    points.extend((left + Q(j, 16), Q(0)) for j in range(192))
    points.extend((right, Q(j, 16)) for j in range(16))
    points.extend((right - Q(j, 16), Q(1)) for j in range(192))
    points.extend((left, Q(16 - j, 16)) for j in range(16))
    return points


def winding(points):
    oa.require(type(points) is list and 3 <= len(points) <= 500, "polygon order")
    for p in points:
        oa.require(type(p) in (tuple, list) and len(p) == 2, "point shape")
        for x in p:
            oa.rational(x)
    result = 0
    for p, q in zip(points, points[1:] + points[:1]):
        cross = p[0] * q[1] - p[1] * q[0]
        oa.require(
            cross != 0 or p[0] * q[0] + p[1] * q[1] > 0, "polygon edge through origin"
        )
        if p[1] <= 0 < q[1] and cross > 0:
            result += 1
        elif q[1] <= 0 < p[1] and cross < 0:
            result -= 1
    return result


def box_count(anchor):
    with oa.precision():
        lam = oa.frozen_lambda(anchor)
        path = boundary(anchor)
        image = [vertex(x, y, lam) for x, y in path]
        rows = []
        for j, (p, q) in enumerate(zip(path, path[1:] + path[:1])):
            value, mxi, error = arc(p, q, lam)
            bounds = oa.cbounds(value)
            rlo, rhi = map(oa.unpair, bounds["real"])
            ilo, ihi = map(oa.unpair, bounds["imag"])
            rlo = min(rlo, image[j][0], image[(j + 1) % len(path)][0])
            rhi = max(rhi, image[j][0], image[(j + 1) % len(path)][0])
            ilo = min(ilo, image[j][1], image[(j + 1) % len(path)][1])
            ihi = max(ihi, image[j][1], image[(j + 1) % len(path)][1])
            oa.require(
                rlo > 0 or rhi < 0 or ilo > 0 or ihi < 0,
                "convex homotopy zero exclusion",
            )
            rows.append(
                {
                    "image": {
                        "real": [oa.pair(rlo), oa.pair(rhi)],
                        "imag": [oa.pair(ilo), oa.pair(ihi)],
                    },
                    "xi_sup": oa.pair(mxi),
                    "tail": oa.pair(error),
                }
            )
        return {
            "anchor": anchor,
            "vertices": [[oa.pair(x), oa.pair(y)] for x, y in image],
            "arcs": rows,
            "count": winding(image),
        }


def matrix_bounds(matrix):
    return [
        [oa.cbounds(matrix[i, j]) for j in range(matrix.ncols())]
        for i in range(matrix.nrows())
    ]


def gauss_jordan(matrix):
    """Second ball route, using explicit row arithmetic rather than acb_mat.inv."""
    n = matrix.nrows()
    oa.require(1 <= n <= 6 and matrix.ncols() == n, "inverse dimension")
    rows = [
        [matrix[i, j] for j in range(n)] + [acb(int(i == j)) for j in range(n)]
        for i in range(n)
    ]
    for j in range(n):
        pivot = rows[j][j]
        oa.require(pivot.abs_lower() > 0, "certified nonzero pivot")
        rows[j] = [v / pivot for v in rows[j]]
        for i in range(n):
            if i != j:
                scale = rows[i][j]
                rows[i] = [v - scale * w for v, w in zip(rows[i], rows[j])]
    return acb_mat([row[n:] for row in rows])


def compression_report(anchor):
    rows, gram, physical, trace = compression(anchor)
    with oa.precision():
        nodes = [
            acb(
                arb(
                    oa.qarb(oa.unpair(row["center"][0])),
                    oa.qarb(oa.unpair(row["radius"])),
                ),
                arb(
                    oa.qarb(oa.unpair(row["center"][1])),
                    oa.qarb(oa.unpair(row["radius"])),
                ),
            )
            for row in rows
        ]
        product = arb(1)
        for j, b in enumerate(nodes):
            product /= 2 * b.imag
            for c in nodes[:j]:
                product *= abs(b - c) ** 2 / abs(b - c.conjugate()) ** 2
        determinant = gram.det()
        oa.require(
            product > 0
            and determinant.real > 0
            and determinant.imag.contains(0)
            and determinant.real.overlaps(product),
            "Cauchy determinant crosscheck",
        )
        alt = (gauss_jordan(gram) * physical).trace()
        oa.require(trace.overlaps(alt), "independent row inverse trace")
        ray = acb_mat([[acb(x, y)] for x, y in RAYS[anchor]])
        adjoint = ray.conjugate().transpose()
        numerator = (adjoint * physical * ray)[0, 0]
        denominator = (adjoint * gram * ray)[0, 0]
        oa.require(
            numerator.imag.contains(0)
            and denominator.imag.contains(0)
            and denominator.real > 0,
            "real Rayleigh form",
        )
        quotient = numerator.real / denominator.real
        trace_floor, norm_floor = THRESHOLDS[anchor]
        oa.require(
            oa.endpoint(trace.real.lower()) > Q(trace_floor, 1000), "strict trace floor"
        )
        oa.require(
            oa.endpoint(quotient.lower()) > Q(norm_floor, 1000) ** 2,
            "strict norm floor",
        )
        return {
            "anchor": anchor,
            "roots": rows,
            "gram": matrix_bounds(gram),
            "raw_physical_gram": matrix_bounds(physical),
            "gram_determinant": oa.cbounds(determinant),
            "cauchy_determinant_product": oa.rbounds(product),
            "raw_trace": oa.cbounds(trace),
            "row_inverse_raw_trace": oa.cbounds(alt),
            "ray_gaussian_integer_coefficients": [list(v) for v in RAYS[anchor]],
            "ray_numerator": oa.cbounds(numerator),
            "ray_denominator": oa.cbounds(denominator),
            "ray_squared_norm_lower_enclosure": oa.rbounds(quotient),
            "conditional_reduced_global_trace_strict_lower": oa.pair(
                Q(trace_floor, 1000)
            ),
            "conditional_reduced_global_norm_strict_lower": oa.pair(
                Q(norm_floor, 1000)
            ),
        }


def validate_tree(value, depth=0, budget=None):
    budget = [0] if budget is None else budget
    budget[0] += 1
    oa.require(depth <= MAX_DEPTH and budget[0] <= MAX_NODES, "JSON tree cap")
    if value is None or type(value) is bool:
        return
    if type(value) is str:
        oa.require(len(value) <= MAX_BYTES, "JSON string cap")
        return
    if type(value) is int:
        oa.require(value.bit_length() <= oa.MAX_BITS, "JSON integer cap")
        return
    oa.require(type(value) in (list, dict) and len(value) <= MAX_NODES, "JSON type/cap")
    if type(value) is dict:
        oa.require(all(type(k) is str and len(k) <= 1024 for k in value), "JSON keys")
        children = value.values()
    else:
        children = value
    for item in children:
        validate_tree(item, depth + 1, budget)


def canonical(value):
    validate_tree(value)
    raw = json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode()
    oa.require(len(raw) <= MAX_BYTES, "canonical byte cap")
    return raw


def load_json(raw):
    oa.require(type(raw) is bytes and len(raw) <= MAX_BYTES, "input byte cap")

    def reject(_):
        raise ValueError("noninteger JSON number")

    value = json.loads(
        raw,
        object_pairs_hook=oa.pairs_unique,
        parse_float=reject,
        parse_constant=reject,
    )
    validate_tree(value)
    return value


def manifest():
    return {
        "schema": STEM + "-sources-v1",
        "authoring_base": BASE,
        "frozen_sources": BINDINGS,
        "contract": CONTRACT,
        "runtime": oa.RUNTIME,
        "documentation": oa.REFERENCES
        + [
            {
                "url": "https://python-flint.readthedocs.io/en/latest/acb_mat.html",
                "role": "rigorous non-approx matrix inverse and arithmetic API",
            }
        ],
    }


def authenticate():
    oa.require(
        canonical(load_json(MANIFEST.read_bytes())) == canonical(manifest()),
        "manifest mismatch",
    )
    oa.authenticate()
    for binding in BINDINGS:
        raw = oa.read_source(binding)
        blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        oa.require(
            blob == binding["git_blob"]
            and oa.digest(oa.lf(raw)) == binding["sha256_lf"],
            "frozen source mismatch",
        )
        if binding["id"].startswith("OA"):
            oa.require(
                oa.digest(oa.lf((ROOT / binding["path"]).read_bytes()))
                == binding["sha256_lf"],
                "executed parent/local source mismatch",
            )


def seal(value):
    oa.require(type(value) is dict and "payload_sha256" not in value, "seal input")
    return {**value, "payload_sha256": oa.digest(canonical(value))}


def build_report():
    authenticate()
    boxes, compressions = [], []
    for anchor, expected in ((32, 3), (64, 5), (128, 6)):
        box = box_count(anchor)
        comp = compression_report(anchor)
        oa.require(
            box["count"] == expected == len(comp["roots"]),
            "complete count equals disjoint certified root list",
        )
        for j, row in enumerate(comp["roots"]):
            for other in comp["roots"][:j]:
                oa.require(
                    abs(oa.unpair(row["center"][0]) - oa.unpair(other["center"][0]))
                    > oa.unpair(row["radius"]) + oa.unpair(other["radius"]),
                    "disjoint root disks",
                )
        boxes.append(box)
        compressions.append(comp)
    artifacts = {
        p.relative_to(ROOT).as_posix(): oa.digest(oa.lf(p.read_bytes()))
        for p in (NOTE, Path(__file__), MANIFEST, TEST)
    }
    return seal(
        {
            "schema": STEM + "-v1",
            "contract": CONTRACT,
            "frozen_sources": BINDINGS,
            "runtime": oa.RUNTIME,
            "precision_bits": 256,
            "boxes": boxes,
            "compressions": compressions,
            "artifacts": artifacts,
        }
    )


def check_report(report):
    validate_tree(report)
    oa.require(type(report) is dict and "payload_sha256" in report, "report shape")
    unsigned = {k: v for k, v in report.items() if k != "payload_sha256"}
    oa.require(
        report["payload_sha256"] == oa.digest(canonical(unsigned)), "payload seal"
    )
    oa.require(
        canonical(report) == canonical(build_report()), "fresh primitive reconstruction"
    )
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--emit", action="store_true")
    mode.add_argument("--emit-sources", action="store_true")
    args = parser.parse_args()
    if args.emit_sources:
        value = manifest()
    elif args.emit:
        value = build_report()
    else:
        check_report(load_json(FIXTURE.read_bytes()))
        print(
            "PASS: complete box counts3/5/6,14 simple noncommon nodes; conditional global finite compression only"
        )
        return
    print(json.dumps(value, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
