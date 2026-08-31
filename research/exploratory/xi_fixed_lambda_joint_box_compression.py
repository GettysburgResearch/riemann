"""One exact lambda64: three complete boxes and joint global compression."""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path

import xi_companion_box_count_compression as bc
from flint import acb, acb_mat, arb

oa = bc.oa

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
STEM = "xi_fixed_lambda_joint_box_compression"
NOTE = HERE / "XI_FIXED_LAMBDA_JOINT_BOX_COMPRESSION.md"
MANIFEST = HERE / (STEM + ".sources.json")
FIXTURE = HERE / (STEM + ".json")
TEST = ROOT / "tests" / ("test_" + STEM + ".py")
BASE = "7fbcd592042a5cc98c17d0db2fac62f8171267f2"
PREREG = "e669d257711d8d4a6a0ab7aeb21254fd220f7dc3"
BINDINGS = [
    {
        "id": "BC1",
        "commit": "7fbcd592042a5cc98c17d0db2fac62f8171267f2",
        "path": "research/exploratory/XI_COMPANION_BOX_COUNT_COMPRESSION.md",
        "git_blob": "2860d9c9bb90f4423f17f0d272229e78a30ae62b",
        "sha256_lf": "22d11bf3dccb72fa25633deeee063164611dbaa977c5e66fca84f4350ae79c65",
        "role": "complete parent proof and global projection convention",
    },
    {
        "id": "BC2",
        "commit": "7fbcd592042a5cc98c17d0db2fac62f8171267f2",
        "path": "research/exploratory/xi_companion_box_count_compression.py",
        "git_blob": "698211f63f2268f421faa1ed76d4dd8749a4b311",
        "sha256_lf": "cea67ec0b5335ecef7a6df8d453859a249b73d1b716b8c87565709d27ec95e58",
        "role": "executed ball boundary and authenticated source helpers",
    },
    {
        "id": "BC3",
        "commit": "7fbcd592042a5cc98c17d0db2fac62f8171267f2",
        "path": "research/exploratory/xi_companion_box_count_compression.json",
        "git_blob": "346a452e1c3136f19139debe1620577ef41e6b43",
        "sha256_lf": "9148321153c7319518dc9475adee61f2ba5b646663f1cb35b762f31f280834e4",
        "role": "frozen comparison fixture",
    },
    {
        "id": "BC4",
        "commit": "7fbcd592042a5cc98c17d0db2fac62f8171267f2",
        "path": "research/exploratory/xi_companion_box_count_compression.sources.json",
        "git_blob": "fcbfb819e09f97f9f4e9af60141ffe198238bf1c",
        "sha256_lf": "b916af0286ddd686e700b56032a2f10f9b0bc08212bed6ca60bb99270b85299f",
        "role": "transitive source closure",
    },
    {
        "id": "BC5",
        "commit": "7fbcd592042a5cc98c17d0db2fac62f8171267f2",
        "path": "tests/test_xi_companion_box_count_compression.py",
        "git_blob": "ea093cc50fb8b9de415ce4e71bc370ffe456d8ed",
        "sha256_lf": "e9b40aaa100f1f8ae74ad2d90978b8e7621303ac750a847cbfc8ec045a2e05b5",
        "role": "independent outward rational finite-matrix controls",
    },
    {
        "id": "PREREG",
        "commit": "e669d257711d8d4a6a0ab7aeb21254fd220f7dc3",
        "path": "research/exploratory/XI_FIXED_LAMBDA_JOINT_BOX_COMPRESSION.md",
        "git_blob": "a11b631e88343ad0782e2d7db511282eb473a30c",
        "sha256_lf": "d8e1f3cc061fc0671b45ef26e09c83b0e165545e3c56e049cf301221377ebc95",
        "role": "fixed boxes and ONE lambda declared before new computations",
    },
]
CONTRACT = {
    "primitive": "actual unrescaled Xi; ONE exact lambda64 independent of z and box",
    "coverage": "complete R5 counts 3/5/6 in (26,38),(58,70),(122,134) plus i(0,1); zero-free FULL closed boundaries",
    "roots": "14 individually certified simple R5 zeros, C5/R0/C0/f6/W/R5prime nonzero throughout each rectangle",
    "boundary": "416 exact arcs each; 32 Taylor terms and analytic Cauchy tail; rational polygon homotopy",
    "arithmetic": "pinned FLINT complex balls; exact Fraction guards; outward Fraction matrix test route",
    "metric": "boundary dx Hardy norm; global P_U=P_(U H2); H_raw=V_raw G V_rawstar",
    "common_factor": "conditional component innerness; raw local nonvanishing survives any common inner divisor; P_U >= P_raw globally",
    "joint": "all cross-box entries of one fixed-source operator; 3/8/14-dimensional nested input spans",
    "increments": "orthogonal INPUT span increments; Loewner applied to each difference projection before taking trace",
    "exclusions": "no Fourier-band, native outer-metric, cofinal, HS-infinity, global-parameter-nonexceptionality, stability or RH claim",
    "trust": "same pinned OA FLINT implementation; not formally verified special functions",
}
GROUPS = {
    "box32": tuple(range(3)),
    "box64": tuple(range(3, 8)),
    "box128": tuple(range(8, 14)),
    "prefix32_64": tuple(range(8)),
    "joint": tuple(range(14)),
}
RAYS = {
    "box32": ((116, -834), (-384, -1), (-33, 1023)),
    "box64": ((301, -269), (-466, -355), (-704, 743), (167, 160), (115, 5)),
    "box128": (
        (-131, 234),
        (605, 373),
        (483, -903),
        (-47, -536),
        (-292, 6),
        (-87, 103),
    ),
    "prefix32_64": (
        (-71, 59),
        (-8, 23),
        (-42, 91),
        (-336, 219),
        (402, 437),
        (830, -600),
        (-125, -190),
        (-105, -30),
    ),
    "joint": (
        (-89, 20),
        (-17, 17),
        (-76, 60),
        (-396, 38),
        (153, 573),
        (1014, -143),
        (-21, -226),
        (-79, -77),
        (13, 1),
        (12, -26),
        (-20, -12),
        (-5, -3),
        (-3, -5),
        (-7, -1),
    ),
}
THRESHOLDS = {
    "box32": (1098, 734),
    "box64": (1551, 816),
    "box128": (1638, 766),
    "prefix32_64": (2657, 818),
    "joint": (4298, 819),
}
canonical, load_json, validate_tree, seal = (
    bc.canonical,
    bc.load_json,
    bc.validate_tree,
    bc.seal,
)
NEW_DISKS = (
    (
        32,
        41604822217334456011589128240992253138971737193560738491,
        1018147158767209381993340102354794205936070205410979109,
        680,
    ),
    (
        32,
        48223911687111720327105633501975978364628230128824007050,
        1004952999167604488833045443694527260384379005173474148,
        342,
    ),
    (
        32,
        54550846805979741375421175295089476942596929877817058521,
        934749521267306393731969540314309879512366725593197737,
        698,
    ),
    (
        128,
        188523695159413619551114721400807375745049541772993399259,
        596086544987215647309502218297462791112464991589757988,
        448,
    ),
    (
        128,
        191707432599093273772740707032105522736397343837940149220,
        600889973116017672866326246112878287934142265772991935,
        275,
    ),
    (
        128,
        194842767302457621487208026895909817551431901559680471063,
        646541213346454248093866099400733965842621307283287480,
        603,
    ),
    (
        128,
        198114117625369503973538494265894044763004453111806921759,
        630473194304587340129886571361319428414087744161589985,
        575,
    ),
    (
        128,
        201405763362393967847038328880647651078612274883956922971,
        573535859386624320055021352772562767467600509862553615,
        279,
    ),
    (
        128,
        204507816620594086131425841774080446592828555661571352939,
        588241095553926755452235449556462183832396874450927676,
        519,
    ),
)
DISKS = tuple(sorted(NEW_DISKS + tuple(d for d in bc.DISKS if d[0] == 64)))


def root_record(data):
    oa.require(type(data) is tuple and len(data) == 4, "root tuple")
    window, nx, ny, coarse = data
    oa.integer(window, 32, 128)
    oa.require(window in (32, 64, 128), "root window")
    oa.integer(nx, 1, 2**200)
    oa.integer(ny, 1, 2**200)
    oa.integer(coarse, 1, 999)
    x, y, r = Q(nx, 2**180), Q(ny, 2**180), Q(1, 2**120)
    oa.require(window - 6 < x - r < x + r < window + 6, "root real domain")
    oa.require(0 < y - r < y + r < 1, "root imaginary domain")
    center = acb(oa.qarb(x), oa.qarb(y))
    box = acb(arb(center.real, oa.qarb(r)), arb(center.imag, oa.qarb(r)))
    lam = oa.frozen_lambda(64)
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
        "box_center": window,
        "parameter_anchor": 64,
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
    oa.require(1 <= n <= 14 and len(values) == n, "matrix order")
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


def gauss_jordan(matrix):
    """Second ball route, using explicit row arithmetic rather than acb_mat.inv."""
    n = matrix.nrows()
    oa.require(1 <= n <= 14 and matrix.ncols() == n, "inverse dimension")
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


def box_count(window):
    with oa.precision():
        lam = oa.frozen_lambda(64)
        path = bc.boundary(window)
        image = [bc.vertex(x, y, lam) for x, y in path]
        rows = []
        for j, (p, q) in enumerate(zip(path, path[1:] + path[:1])):
            value, mxi, error = bc.arc(p, q, lam)
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
            "box_center": window,
            "parameter_anchor": 64,
            "vertices": [[oa.pair(x), oa.pair(y)] for x, y in image],
            "arcs": rows,
            "count": bc.winding(image),
        }


def compression_report(label, records):
    oa.require(type(label) is str and label in GROUPS, "declared span")
    oa.require(type(records) is list and len(records) == 14, "complete ordered records")
    indices = GROUPS[label]
    nodes = [records[i][1] for i in indices]
    values = [records[i][2] for i in indices]
    gram, physical = physical_matrices(nodes, values)
    trace = (gram.inv() * physical).trace()
    oa.require(trace.is_finite() and trace.imag.contains(0), "real finite trace")
    product = arb(1)
    for j, b in enumerate(nodes):
        product /= 2 * b.imag
        for c in nodes[:j]:
            product *= abs(b - c) ** 2 / abs(b - c.conjugate()) ** 2
    det = gram.det()
    oa.require(
        product > 0
        and det.real > 0
        and det.imag.contains(0)
        and det.real.overlaps(product),
        "positive Cauchy determinant",
    )
    alt = (gauss_jordan(gram) * physical).trace()
    oa.require(trace.overlaps(alt), "row inverse trace agreement")
    coeff = RAYS[label]
    oa.require(len(coeff) == len(indices), "ray dimension")
    for pair in coeff:
        oa.require(type(pair) is tuple and len(pair) == 2, "Gaussian coefficient")
        for v in pair:
            oa.integer(v, -2048, 2048)
    ray = acb_mat([[acb(x, y)] for x, y in coeff])
    adjoint = ray.conjugate().transpose()
    numerator = (adjoint * physical * ray)[0, 0]
    denominator = (adjoint * gram * ray)[0, 0]
    oa.require(
        numerator.imag.contains(0)
        and denominator.imag.contains(0)
        and denominator.real > 0,
        "real positive Rayleigh denominator",
    )
    quotient = numerator.real / denominator.real
    tf, nf = THRESHOLDS[label]
    oa.require(oa.endpoint(trace.real.lower()) > Q(tf, 1000), "trace floor")
    oa.require(oa.endpoint(quotient.lower()) > Q(nf, 1000) ** 2, "norm floor")
    return {
        "label": label,
        "root_indices": list(indices),
        "gram": bc.matrix_bounds(gram),
        "raw_physical_gram": bc.matrix_bounds(physical),
        "gram_determinant": oa.cbounds(det),
        "cauchy_determinant_product": oa.rbounds(product),
        "raw_trace": oa.cbounds(trace),
        "row_inverse_trace": oa.cbounds(alt),
        "ray_gaussian_integer_coefficients": [list(v) for v in coeff],
        "ray_numerator": oa.cbounds(numerator),
        "ray_denominator": oa.cbounds(denominator),
        "ray_squared_norm_lower_enclosure": oa.rbounds(quotient),
        "conditional_reduced_global_trace_strict_lower": oa.pair(Q(tf, 1000)),
        "conditional_reduced_global_norm_strict_lower": oa.pair(Q(nf, 1000)),
    }, trace


def manifest():
    return {
        "schema": STEM + "-sources-v1",
        "authoring_base": BASE,
        "preregistration_commit": PREREG,
        "frozen_sources": BINDINGS,
        "contract": CONTRACT,
        "runtime": oa.RUNTIME,
        "documentation": bc.manifest()["documentation"],
    }


def lf(raw):
    oa.require(type(raw) is bytes and len(raw) <= bc.MAX_BYTES, "byte cap")
    normalized = raw.replace(b"\r\n", b"\n")
    text = normalized.decode("utf-8")
    oa.require(
        all(ord(c) in (9, 10) or ord(c) >= 32 for c in text)
        and not any(127 <= ord(c) <= 159 for c in text),
        "source control byte",
    )
    return normalized


def authenticate():
    oa.require(
        canonical(load_json(MANIFEST.read_bytes())) == canonical(manifest()),
        "manifest mismatch",
    )
    bc.authenticate()
    for binding in BINDINGS:
        raw = oa.read_source(binding)
        blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        oa.require(
            blob == binding["git_blob"] and oa.digest(lf(raw)) == binding["sha256_lf"],
            "source mismatch",
        )
        if binding["id"].startswith("BC"):
            oa.require(
                oa.digest(lf((ROOT / binding["path"]).read_bytes()))
                == binding["sha256_lf"],
                "executed parent/local mismatch",
            )


def build_report():
    authenticate()
    boxes = [box_count(w) for w in (32, 64, 128)]
    with oa.precision():
        records = [root_record(d) for d in DISKS]
        for box, expected in zip(boxes, (3, 5, 6)):
            subset = [r for r, _, _ in records if r["box_center"] == box["box_center"]]
            oa.require(box["count"] == expected == len(subset), "exhaustive root count")
        for j, (row, _, _) in enumerate(records):
            for other, _, _ in records[:j]:
                oa.require(
                    abs(oa.unpair(row["center"][0]) - oa.unpair(other["center"][0]))
                    > oa.unpair(row["radius"]) + oa.unpair(other["radius"]),
                    "disjoint root disks",
                )
        comps, traces = {}, {}
        for label in GROUPS:
            comps[label], traces[label] = compression_report(label, records)
        increments = []
        for before, after, floor in (
            ("box32", "prefix32_64", 1558),
            ("prefix32_64", "joint", 1641),
        ):
            value = traces[after] - traces[before]
            oa.require(
                value.imag.contains(0)
                and oa.endpoint(value.real.lower()) > Q(floor, 1000),
                "orthogonal input increment floor",
            )
            increments.append(
                {
                    "from": before,
                    "to": after,
                    "raw_increment_trace": oa.cbounds(value),
                    "conditional_reduced_increment_trace_strict_lower": oa.pair(
                        Q(floor, 1000)
                    ),
                }
            )
        coupling = traces["joint"] - sum(
            (traces[s] for s in ("box32", "box64", "box128")), acb(0)
        )
        oa.require(
            coupling.imag.contains(0)
            and oa.endpoint(coupling.real.lower()) > Q(10, 1000),
            "joint is not sum of individual traces",
        )
        lam = oa.rbounds(oa.frozen_lambda(64))
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
            "parameter_anchor": 64,
            "lambda_enclosure": lam,
            "boxes": boxes,
            "roots": [r for r, _, _ in records],
            "compressions": list(comps.values()),
            "orthogonal_input_increments": increments,
            "joint_minus_sum_individual_raw_traces": oa.cbounds(coupling),
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
            "PASS: ONE lambda64; complete counts3/5/6;14 surviving nodes; joint trace>4.298, norm>0.819; global finite only"
        )
        return
    print(json.dumps(value, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
