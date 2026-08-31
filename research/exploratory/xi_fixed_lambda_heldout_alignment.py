"""Held-out fixed-lambda Xi evaluation; bounded source-domain extension."""

from __future__ import annotations

import math
from contextlib import contextmanager
from fractions import Fraction as Q

import xi_companion_box_count_compression as bc
from flint import acb, acb_mat, acb_series, arb, ctx

oa = bc.oa
import argparse
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
STEM = "xi_fixed_lambda_heldout_alignment"
NOTE = HERE / "XI_FIXED_LAMBDA_HELDOUT_ALIGNMENT.md"
MANIFEST = HERE / (STEM + ".sources.json")
FIXTURE = HERE / (STEM + ".json")
TEST = ROOT / "tests" / ("test_" + STEM + ".py")
BASE = "0e3fc9b482f0f115a49a6209ccbfeffae640014a"
PREREG = "24544028cd033ea66a6b64bec254da5ea43230c9"
MAX_BYTES, MAX_NODES, MAX_DEPTH = 24_000_000, 600_000, 24
BINDINGS = [
    {
        "id": "FC1",
        "commit": "0e3fc9b482f0f115a49a6209ccbfeffae640014a",
        "path": "research/exploratory/XI_FIXED_LAMBDA_JOINT_BOX_COMPRESSION.md",
        "git_blob": "27e4db71377788b6e03b14005035d59c9e930611",
        "sha256_lf": "7f6efdcd6375d14db36ade51c073d3c04dc73f5e2c9c5cd27aa94d8107497460",
        "role": "complete prior fixed-source proof",
    },
    {
        "id": "FC2",
        "commit": "0e3fc9b482f0f115a49a6209ccbfeffae640014a",
        "path": "research/exploratory/xi_fixed_lambda_joint_box_compression.py",
        "git_blob": "62f94b71810a49646830694cab25bb14c1eab470",
        "sha256_lf": "69e51a36a9180df97ae6b994104308a46b9ab84331027e1d8ed288c6490d5300",
        "role": "historical producer, authenticated but not executed",
    },
    {
        "id": "FC3",
        "commit": "0e3fc9b482f0f115a49a6209ccbfeffae640014a",
        "path": "research/exploratory/xi_fixed_lambda_joint_box_compression.json",
        "git_blob": "d3ef5908f68a7b3025428bf55e8e1fa81970e273",
        "sha256_lf": "504071292138882ad5192fc62f765edc5615c3140542c7f597651679ba682cdb",
        "role": "frozen fourteen-node reference",
    },
    {
        "id": "FC4",
        "commit": "0e3fc9b482f0f115a49a6209ccbfeffae640014a",
        "path": "research/exploratory/xi_fixed_lambda_joint_box_compression.sources.json",
        "git_blob": "62eb2fa59113bc87158659e538fb1fea5b7f7ca4",
        "sha256_lf": "b775a9c8bc054312644116b362960b1c1e950d23a8dfc82d556d86f67a30c819",
        "role": "transitive source closure",
    },
    {
        "id": "FC5",
        "commit": "0e3fc9b482f0f115a49a6209ccbfeffae640014a",
        "path": "tests/test_xi_fixed_lambda_joint_box_compression.py",
        "git_blob": "6cdac911a7e62d12273d7eafd2fdef199b282d33",
        "sha256_lf": "deb2696c5c160e0da970c31f35e5ed472baabc4fb1d3db831b4e48371935ae80",
        "role": "frozen finite controls",
    },
    {
        "id": "PREREG",
        "commit": "24544028cd033ea66a6b64bec254da5ea43230c9",
        "path": "research/exploratory/XI_FIXED_LAMBDA_HELDOUT_ALIGNMENT.md",
        "git_blob": "db03a1b0c1f5abc0e27be92c4232968f68f816b8",
        "sha256_lf": "714bf76812826957269bb26d10c3a919909ad7af97b0ec9becfb8a4e5f0c79bd",
        "role": "fixed heldout boxes, tiers and scouting schedule before computation",
    },
    {
        "id": "LB",
        "commit": "a7479e85fdc2a464cdc753021435cfef7a1f3910",
        "path": "research/exploratory/XI_LAPLACE_LOW_PASS_LOWER_BOUND.md",
        "git_blob": "90e6bd89ca9a23c401d6d947c04a9d548f6b3030",
        "sha256_lf": "c56d29037b85c45398bcb34dc7fb8450ba0e4b0f32fa7293edcaf5d1d2ea4b64",
        "role": "LB3 weighted native alignment criterion and unpaid cofinal hypotheses",
    },
]
CONTRACT = {
    "primitive": "actual unrescaled Xi; ONE fixed lambda64; new domain20<x<1100, no parent edits",
    "coverage": "three heldout full closed boxes256/512/1024,width12,y0..1; complete counts8/9/9",
    "arithmetic_class": "MIXED",
    "arithmetic_components": [
        "DIRECTED_BALL_ENCLOSURES",
        "EXACT_RATIONAL",
        "CERTIFIED_INTEGER_COVERAGE",
    ],
    "rounding": "FLINT outward complex/real balls; exact Fraction acceptance; no scout or floating value certifies a claim",
    "tiers": "fixed (256bits,1/16,32terms),(512,1/32,40),(1024,1/64,48); all failed tiers retained",
    "scouting": "fixed196seeds perbox; all588 terminal outcomes retained; 24Newtonsteps maximum; scouts are not proofs",
    "roots": "26 new and14 rebuilt old simple noncommon nodes; raw values on entire root rectangles",
    "metric": "complete40x40 normalized Hardy Gram including ALL old/new cross entries; finite Bessel row-sum ceilings only",
    "weight": "sum |rawTheta0(b)|^2 Im(b)/|Re(b)|; NOT a physical trace",
    "analytic": "conditional local derivative-jet transport lemma; actual cofinal jet hypotheses unpaid",
    "source_quantifiers": "finite evaluations unconditional; Hardy physical interpretation conditional on component innerness; no finite-to-cofinal implication",
    "source_execution": "FC5 historical files authenticated as frozen Git blobs; old14 rebuilt with this extended Xi wrapper; unchanged BC5/OA5 local executable locks retained",
    "exclusions": "no uniform infinite Bessel bound, weighted divergence, physical HS-infinity, native outer metric, parameter stability or RH",
    "trust": "pinned FLINT implementation, not formal verification of special functions",
}
WINDOWS = (256, 512, 1024)
SOURCE_WINDOWS = (32, 64, 128) + WINDOWS
TIERS = ((256, 16, 32), (512, 32, 40), (1024, 64, 48))
NEW_CENTERS = {
    256: [
        [
            383289837534981752829283253399982482889641139396010637796,
            416192284064506274546873476951999821124846781230515364,
        ],
        [
            385792195482436808403303089225704272319609866749941066156,
            459304653185949115111504096751483423892226202545037932,
        ],
        [
            388378560232595348157782366104128362560610079089905035585,
            482573797969912657930609893151133442620676298257298243,
        ],
        [
            391038277480518701392498048544806559727689416010526982610,
            475364542458315395318874605237695980489485437746184762,
        ],
        [
            393707451235731237538298866435692346126994706196083063036,
            445811829945445925085048077164511800731220227706703234,
        ],
        [
            396304601660569555771259632479588539290075763640505224633,
            430155063637765849127727093833676305924586525033028360,
        ],
        [
            398842190643044470837200145293942973863340378617696172623,
            436264520771836127206599243234869916413752409280059359,
        ],
        [
            401376413941209011878153381571765610356038209761918940996,
            454459174130842841012324140259313532997496375306255241,
        ],
    ],
    512: [
        [
            775492188476638841180383027642696424487641667078526514163,
            342573643733015840461943731812539634210400832019968409,
        ],
        [
            777679634520623400788724661956595945638589079647366668609,
            355122735344049492807461805906705980778069986780307941,
        ],
        [
            779906730917501434935406042113353997417675433226459887000,
            368155295275412783172588425771600113679482150773327761,
        ],
        [
            782177221829280983679744698857626780309899762126960344928,
            345320088846913375953267951727032613933188735459440547,
        ],
        [
            786508823039187802556590786680068912650798102044984729875,
            313839028727396291318117259996537876456580658596037970,
        ],
        [
            784395256761462257056838779330357672453225226392726885462,
            310485155467053572091517960646718383226788947687794220,
        ],
        [
            788618911664129571179941216248242412365743248355024242664,
            341759491999379406784038568714397421366020337317084642,
        ],
        [
            790796961917408800025396819785695845511768145502083388584,
            364445604704321741230748352910421017924303279420635566,
        ],
        [
            793040571747242261992507184731277524259013753728685219469,
            359958279992430261849177444042641255486908056719698064,
        ],
    ],
    1024: [
        [
            1561555708214038250922105110549313019354547213172322387231,
            252974744621108162283222157181122461402019400841498265,
        ],
        [
            1565251670956201697600951160919909328429757066997607084711,
            240379788332364593094655948945968131600977162422758385,
        ],
        [
            1563424535109555577258757522664298552069410125423695655678,
            241708900930705257373047161779664886399236572636157754,
        ],
        [
            1567078551590923844756268277073045759597293698581486766795,
            262634789485906471581027337506731563201271053164852138,
        ],
        [
            1568971545624690934268148927939436519782388083522991210769,
            287584557057520232603787570989680792311134914380377183,
        ],
        [
            1570935248017957305565243954476806548162773825007455495259,
            287384221597778858009117994435826467468814069726066124,
        ],
        [
            1572907699675554008972132241307664703657040492536366950717,
            261512152103600440758691648880608908296915879818259318,
        ],
        [
            1574809336473387966053743537234077589353615958333735973200,
            239712265735490679452933656167924982243311046836393493,
        ],
        [
            1576642628100502650019720799027654008636244640387214040856,
            243783508368855561213714629020174920375604011933272766,
        ],
    ],
}


@contextmanager
def precision(bits=256):
    oa.require(type(bits) is int and bits in (256, 512, 1024), "declared precision")
    previous = ctx.prec, ctx.cap
    ctx.prec, ctx.cap = bits, 9
    try:
        yield
    finally:
        ctx.prec, ctx.cap = previous


def fixed_lambda():
    oa.require(ctx.prec in (256, 512, 1024), "lambda precision")
    omega = (acb(oa.qarb(Q(1, 4)), 32).digamma().real - arb.pi().log()) / 2
    oa.require(omega > 0, "positive fixed phase derivative")
    return 1 / omega


def xi_series(z, cap=39, reflected=False):
    oa.require(type(z) is acb and z.is_finite(), "finite input")
    oa.integer(cap, 9, 55)
    oa.require(ctx.prec in (256, 512, 1024), "precision cap")
    oa.require(type(reflected) is bool, "strict route")
    oa.require(20 < z.real and z.real < 1100 and -1 < z.imag and z.imag < 2, "domain")
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
        20 < z.real and z.real < 1100 and -1 < z.imag and z.imag < 2, "scalar domain"
    )
    oa.require(ctx.prec in (256, 512, 1024), "scalar precision")
    s = acb(arb(1) / 2) + acb(0, 1) * z
    return (
        s * (s - 1) / 2 * (-s / 2 * arb.pi().log()).exp() * (s / 2).gamma() * s.zeta()
    )


def xi_jet(z, reflected=False):
    return [v * math.factorial(j) for j, v in enumerate(xi_series(z, 9, reflected))]


def fcoeff(z, lam, terms=32):
    oa.integer(terms, 2, 48)
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


def arc(p, q, lam, terms):
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
    coeff = fcoeff(c, lam, terms)
    delta = acb(arb(0, oa.qarb(dx)), arb(0, oa.qarb(dy)))
    value = acb(0)
    for v in reversed(coeff):
        value = value * delta + v
    outer = acb(arb(c.real, arb(1) / 4), arb(c.imag, arb(1) / 4))
    mxi = xi_value(outer).abs_upper()
    mf = mxi * (120 * 8**5 + lam * 720 * 8**6)
    t = oa.qarb(8 * h)
    error = mf * t**terms / (1 - t)
    err = error.upper()
    value += acb(arb(0, err), arb(0, err))
    oa.require(
        value.is_finite() and not value.contains(0), "boundary image excludes zero"
    )
    return value, oa.endpoint(mxi), oa.endpoint(err)


def boundary(window, den=16):
    oa.require(type(window) is int and window in WINDOWS, "heldout window")
    oa.require(type(den) is int and den in (16, 32, 64), "declared mesh")
    left, right = Q(window - 6), Q(window + 6)
    return (
        [(left + Q(j, den), Q(0)) for j in range(12 * den)]
        + [(right, Q(j, den)) for j in range(den)]
        + [(right - Q(j, den), Q(1)) for j in range(12 * den)]
        + [(left, Q(den - j, den)) for j in range(den)]
    )


def winding(points):
    oa.require(type(points) is list and 3 <= len(points) <= 1664, "polygon order")
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


def box_count(window):
    attempts = []
    for bits, den, terms in TIERS:
        failure_at = None
        try:
            with precision(bits):
                lam = fixed_lambda()
                path = boundary(window, den)
                image = [vertex(x, y, lam) for x, y in path]
                rows = []
                for j, (p, q) in enumerate(zip(path, path[1:] + path[:1])):
                    failure_at = j
                    value, mxi, error = arc(p, q, lam, terms)
                    bounds = oa.cbounds(value)
                    rlo, rhi = map(oa.unpair, bounds["real"])
                    ilo, ihi = map(oa.unpair, bounds["imag"])
                    rlo = min(rlo, image[j][0], image[(j + 1) % len(path)][0])
                    rhi = max(rhi, image[j][0], image[(j + 1) % len(path)][0])
                    ilo = min(ilo, image[j][1], image[(j + 1) % len(path)][1])
                    ihi = max(ihi, image[j][1], image[(j + 1) % len(path)][1])
                    oa.require(
                        rlo > 0 or rhi < 0 or ilo > 0 or ihi < 0,
                        "convex homotopy excludes zero",
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
                count = winding(image)
                attempts.append(
                    {
                        "bits": bits,
                        "mesh_denominator": den,
                        "terms": terms,
                        "status": "PASS",
                    }
                )
                return {
                    "box_center": window,
                    "parameter_anchor": 64,
                    "attempts": attempts,
                    "vertices": [[oa.pair(x), oa.pair(y)] for x, y in image],
                    "arcs": rows,
                    "count": count,
                }
        except (ValueError, ZeroDivisionError, OverflowError) as error:
            attempts.append(
                {
                    "bits": bits,
                    "mesh_denominator": den,
                    "terms": terms,
                    "status": "FAILED",
                    "arc_index": failure_at,
                    "reason": str(error),
                }
            )
    return {
        "box_center": window,
        "parameter_anchor": 64,
        "attempts": attempts,
        "count": None,
        "unresolved": "all declared boundary tiers failed",
    }


def scout(window):
    oa.require(type(window) is int and window in WINDOWS, "scout window")
    candidates = []
    log = []
    with precision():
        lam = fixed_lambda()
        for j in range(49):
            for seed_y in (Q(1, 8), Q(3, 8), Q(5, 8), Q(7, 8)):
                x = Q(window - 6) + Q(j, 4)
                y = seed_y
                record = {"seed": [oa.pair(x), oa.pair(y)]}
                for step in range(24):
                    if not (20 < x < 1100 and -1 < y < 2):
                        record.update(status="domain exit", steps=step)
                        break
                    try:
                        c = acb(oa.qarb(x), oa.qarb(y))
                        v = oa.companions(xi_jet(c), lam)
                        if not v["R5prime"].abs_lower() > 0:
                            record.update(status="derivative obstruction", steps=step)
                            break
                        correction = v["R5"] / v["R5prime"]
                        z = c - correction
                        x, y = oa.endpoint(z.real.mid()), oa.endpoint(z.imag.mid())
                        if correction.abs_upper() < oa.qarb(Q(1, 2**170)):
                            if not (window - 6 < x < window + 6 and 0 < y < 1):
                                record.update(
                                    status="candidate outside box", steps=step + 1
                                )
                                break
                            nx, ny = round(x * 2**180), round(y * 2**180)
                            found = None
                            for k, (a, b) in enumerate(candidates):
                                if abs(nx - a) + abs(ny - b) < 2**150:
                                    found = k
                                    break
                            if found is None:
                                found = len(candidates)
                                candidates.append((nx, ny))
                                status = "converged candidate"
                            else:
                                status = "duplicate"
                            record.update(
                                status=status, steps=step + 1, candidate=found
                            )
                            break
                    except (ValueError, ZeroDivisionError, OverflowError) as error:
                        record.update(
                            status="arithmetic obstruction",
                            steps=step,
                            reason=str(error),
                        )
                        break
                else:
                    record.update(status="iteration limit", steps=24)
                log.append(record)
    return {
        "box_center": window,
        "candidates": [list(v) for v in candidates],
        "seed_log": log,
    }


def root_record(window, nx, ny):
    oa.require(type(window) is int and window in SOURCE_WINDOWS, "source root window")
    for v in (nx, ny):
        oa.integer(v, 1, 2**200)
    x, y, r = Q(nx, 2**180), Q(ny, 2**180), Q(1, 2**120)
    oa.require(
        window - 6 < x - r < x + r < window + 6 and 0 < y - r < y + r < 1,
        "root rectangle inside",
    )
    attempts = []
    for bits in (256, 512, 1024):
        try:
            with precision(bits):
                c = acb(oa.qarb(x), oa.qarb(y))
                box = acb(arb(c.real, oa.qarb(r)), arb(c.imag, oa.qarb(r)))
                lam = fixed_lambda()
                point = xi_jet(c)
                region = xi_jet(box)
                reflected = xi_jet(box, True)
                oa.require(
                    all(v.overlaps(w) for v, w in zip(region, reflected)),
                    "reflected jets",
                )
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
                    v = oa.endpoint(q[key].abs_lower())
                    oa.require(v > 0, "local noncommon " + key)
                    nonzero[key] = oa.pair(v)
                theta = oa.theta_jets(region, lam)[0]
                weight = abs(theta) ** 2 * box.imag / box.real
                attempts.append({"bits": bits, "status": "PASS"})
                return (
                    {
                        "box_center": window,
                        "parameter_anchor": 64,
                        "center": [oa.pair(x), oa.pair(y)],
                        "radius": oa.pair(r),
                        "attempts": attempts,
                        "point_derivatives": [oa.cbounds(v) for v in point],
                        "rectangle_derivatives": [oa.cbounds(v) for v in region],
                        "reflected_rectangle_derivatives": [
                            oa.cbounds(v) for v in reflected
                        ],
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
                        "weighted_alignment": oa.rbounds(weight),
                    },
                    box,
                    theta,
                )
        except (ValueError, ZeroDivisionError, OverflowError) as error:
            attempts.append({"bits": bits, "status": "FAILED", "reason": str(error)})
    return (
        {
            "box_center": window,
            "center": [oa.pair(x), oa.pair(y)],
            "attempts": attempts,
            "unresolved": "all declared root tiers failed",
        },
        None,
        None,
    )


def normalized_gram(nodes):
    oa.require(type(nodes) is list and 1 <= len(nodes) <= 64, "normalized Gram order")
    oa.require(
        all(type(b) is acb and b.is_finite() and b.imag > 0 for b in nodes),
        "upper half-plane nodes",
    )
    n = len(nodes)
    return acb_mat(
        [
            [
                acb(1)
                if i == j
                else 2
                * (nodes[i].imag * nodes[j].imag).sqrt()
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


def transport_control(lam, a, c, m3, eta):
    lam, a, c, m3, eta = map(oa.rational, (lam, a, c, m3, eta))
    oa.require(lam > 0 and a * c < 0 and m3 >= 0 and 0 <= eta < 1, "transport signs")
    q = -a / (lam * c)
    delta = 2 * q / lam + (m3 / abs(c)) * (4 * q * q / (3 * lam) + 2 * q)
    oa.require(0 < delta < Q(1, 2), "transport smallness")
    return {
        "q": oa.pair(q),
        "delta": oa.pair(delta),
        "radius": oa.pair(2 * delta * q),
        "raw_alignment_floor": oa.pair((1 - eta) / (1 + eta)),
    }


def finite_summary(records):
    oa.require(
        type(records) is list and 14 < len(records) <= 64, "complete finite records"
    )
    with precision():
        rows, nodes, values = map(list, zip(*records))
        gram = normalized_gram(nodes)
        weights = [abs(v) ** 2 * b.imag / b.real for b, v in zip(nodes, values)]
        prefixes = []
        previous = arb(0)
        for window in (128, 256, 512, 1024):
            indices = [i for i, row in enumerate(rows) if row["box_center"] <= window]
            oa.require(bool(indices), "nonempty prefix")
            row_bounds = [
                sum((abs(gram[i, j]) for j in indices), arb(0)) for i in indices
            ]
            upper = max(oa.endpoint(v.upper()) for v in row_bounds)
            ceiling = Q((upper * 1000).__floor__() + 1, 1000)
            oa.require(ceiling > upper, "strict finite Bessel ceiling")
            weight = sum((weights[i] for i in indices), arb(0))
            increment = weight - previous
            oa.require(
                weight > 0 and increment > 0, "positive finite weighted increment"
            )
            lower = Q((oa.endpoint(weight.lower()) * 10**12).__floor__(), 10**12)
            inc_lower = Q((oa.endpoint(increment.lower()) * 10**12).__floor__(), 10**12)
            oa.require(
                0 < lower < oa.endpoint(weight.lower()), "strict partial sum floor"
            )
            oa.require(
                0 < inc_lower < oa.endpoint(increment.lower()), "strict increment floor"
            )
            prefixes.append(
                {
                    "through_box": window,
                    "root_indices": indices,
                    "normalized_gram_row_sums": [oa.rbounds(v) for v in row_bounds],
                    "finite_bessel_strict_upper": oa.pair(ceiling),
                    "weighted_alignment": oa.rbounds(weight),
                    "weighted_increment": oa.rbounds(increment),
                    "weighted_alignment_strict_lower": oa.pair(lower),
                    "weighted_increment_strict_lower": oa.pair(inc_lower),
                }
            )
            previous = weight
        return {
            "normalized_gram": bc.matrix_bounds(gram),
            "node_weighted_alignments": [oa.rbounds(v) for v in weights],
            "prefixes": prefixes,
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
        oa.require(value.bit_length() <= 4096, "JSON integer cap")
        return
    oa.require(type(value) in (list, dict) and len(value) <= MAX_NODES, "JSON type/cap")
    if type(value) is dict:
        oa.require(all(type(k) is str and len(k) <= 1024 for k in value), "JSON keys")
        children = value.values()
    else:
        children = value
    for v in children:
        validate_tree(v, depth + 1, budget)


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


def lf(raw):
    oa.require(type(raw) is bytes and len(raw) <= MAX_BYTES, "source byte cap")
    raw = raw.replace(b"\r\n", b"\n")
    text = raw.decode("utf-8")
    oa.require(
        all(ord(c) in (9, 10) or ord(c) >= 32 for c in text)
        and not any(127 <= ord(c) <= 159 for c in text),
        "source control byte",
    )
    return raw


def manifest():
    return {
        "schema": STEM + "-sources-v1",
        "authoring_base": BASE,
        "preregistration_commit": PREREG,
        "frozen_sources": BINDINGS,
        "runtime": oa.RUNTIME,
        "contract": CONTRACT,
        "documentation": bc.manifest()["documentation"],
    }


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
    historical = load_json(oa.read_source(BINDINGS[3]))
    oa.require(len(historical["frozen_sources"]) == 6, "FC closure shape")
    for binding in historical["frozen_sources"]:
        raw = oa.read_source(binding)
        blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        oa.require(
            blob == binding["git_blob"] and oa.digest(lf(raw)) == binding["sha256_lf"],
            "historical transitive source mismatch",
        )
        if binding["id"].startswith("BC"):
            oa.require(
                oa.digest(lf((ROOT / binding["path"]).read_bytes()))
                == binding["sha256_lf"],
                "executed BC parent mismatch",
            )


def frozen_fc_report():
    raw = oa.read_source(BINDINGS[2])
    oa.require(oa.digest(lf(raw)) == BINDINGS[2]["sha256_lf"], "FC fixture source")
    return load_json(raw)


def old_records():
    historical = frozen_fc_report()["roots"]
    oa.require(len(historical) == 14, "historical node coverage")
    records = []
    for old in historical:
        nums = [oa.unpair(v) * 2**180 for v in old["center"]]
        oa.require(all(v.denominator == 1 for v in nums), "historical dyadic centers")
        row, box, theta = root_record(old["box_center"], *(v.numerator for v in nums))
        oa.require(box is not None and theta is not None, "old-node fresh certificate")
        oa.require(
            row.pop("attempts") == [{"bits": 256, "status": "PASS"}], "old-node tier"
        )
        row.pop("weighted_alignment")
        lo, hi = map(oa.unpair, old["raw_corridor"])
        oa.require(
            abs(theta) > oa.qarb(lo) and abs(theta) < oa.qarb(hi), "old raw corridor"
        )
        row["raw_corridor"] = old["raw_corridor"]
        oa.require(
            canonical(row) == canonical(old), "literal historical node reconstruction"
        )
        records.append((row, box, theta))
    return records


def seal(value):
    oa.require(type(value) is dict and "payload_sha256" not in value, "seal input")
    return {**value, "payload_sha256": oa.digest(canonical(value))}


def build_report():
    authenticate()
    records = old_records()
    boxes = []
    scouts = []
    for window, expected in zip(WINDOWS, (8, 9, 9)):
        count = box_count(window)
        seed = scout(window)
        oa.require(
            seed["candidates"] == NEW_CENTERS[window], "fixed scouting reconstruction"
        )
        oa.require(
            count["count"] == expected == len(seed["candidates"]),
            "exhaustive heldout count",
        )
        for nx, ny in sorted(NEW_CENTERS[window]):
            record, box, theta = root_record(window, nx, ny)
            oa.require(
                box is not None and theta is not None, "unresolved root certificate"
            )
            records.append((record, box, theta))
        boxes.append(count)
        scouts.append(seed)
    oa.require(len(records) == 40, "exact finite node coverage")
    for j, (row, _, _) in enumerate(records):
        for old, _, _ in records[:j]:
            oa.require(
                abs(oa.unpair(row["center"][0]) - oa.unpair(old["center"][0]))
                > oa.unpair(row["radius"]) + oa.unpair(old["radius"]),
                "disjoint root discs",
            )
    summary = finite_summary(records)
    artifacts = {
        p.relative_to(ROOT).as_posix(): oa.digest(lf(p.read_bytes()))
        for p in (NOTE, Path(__file__), MANIFEST, TEST)
    }
    return seal(
        {
            "schema": STEM + "-v1",
            "contract": CONTRACT,
            "runtime": oa.RUNTIME,
            "frozen_sources": BINDINGS,
            "parameter_anchor": 64,
            "boundary_tiers": [list(v) for v in TIERS],
            "boxes": boxes,
            "scouts": scouts,
            "roots": [r for r, _, _ in records],
            "finite_data": summary,
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
            "PASS: fixedlambda64 heldout counts8/9/9,40nodes,finite Gram/weighted sums; no cofinal inference"
        )
        return
    print(json.dumps(value, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
