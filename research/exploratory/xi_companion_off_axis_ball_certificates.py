"""Source-bound ball certificates for nine actual Xi off-axis companion zeros."""

from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import math
import platform
import subprocess
from contextlib import contextmanager
from fractions import Fraction as Q
from pathlib import Path

import flint
from flint import acb, acb_series, arb, ctx, fmpq

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
STEM = "xi_companion_off_axis_ball_certificates"
NOTE = HERE / "XI_COMPANION_OFF_AXIS_BALL_CERTIFICATES.md"
MANIFEST = HERE / (STEM + ".sources.json")
FIXTURE = HERE / (STEM + ".json")
TEST = ROOT / "tests" / ("test_" + STEM + ".py")
BASE = "ac7fa9af27c3fbcb3314f3ed58c8eed35b318052"
PRECISION, CENTER_BITS, RADIUS_BITS = 256, 180, 120
MAX_BYTES, MAX_NODES, MAX_DEPTH, MAX_BITS = 3_000_000, 100_000, 24, 4096
BINDINGS = [
    {
        "commit": "d38961c15fc76d671cef4fddfc92d3c866af4fd5",
        "git_blob": "9688e30825fcc3d2b13570539bf03299407eae87",
        "id": "NA",
        "path": "research/exploratory/XI_COMPANION_IMAGINARY_AXIS_SAMPLING.md",
        "role": "AX1-2 moments and companion; AX7 no common axis zero; AX21 Wronskian",
        "sha256_lf": "a9d6b51b3b2f1ccb388fb8d74e115023c622115b169d3214f071ef9005034081",
    },
    {
        "commit": "9da33e7ea2b15a4badb3cb436e38e54762ad5e1d",
        "git_blob": "e592a4c031876f56f07d28b7e18a8a7cf6e826f4",
        "id": "GH",
        "path": "research/exploratory/XI_COMPANION_GLOBAL_HEIGHT_BOUNDARY.md",
        "role": "GH1-4 native ratio and inner premise; GH3/16 pure component infinite height",
        "sha256_lf": "5bf33ffd58c3fe277f4bfb0408f0805eae1b2f34aab49bb71e4c714afb80dc6d",
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
        "id": "GC",
        "commit": "d76a1a8eb8ec40b19a351af95439b9a6514bee87",
        "path": "research/exploratory/XI_COMPANION_GENERIC_PARAMETER_COPRIMALITY.md",
        "git_blob": "797f7b581580ad5a441c7702015c64a53eca6f4d",
        "sha256_lf": "55aa96745c3f269ac464ea7c0b8227e14e7d8ceb33f8bec2fc13f9642b33d44d",
        "role": "Cancellation-safe local zeros, exact W identity, countable parameter exception limitation",
    },
    {
        "id": "L106610",
        "commit": "81d52e569cc8bb566e54043fd692fd6157406aab",
        "path": "claims/lemmas/L-106610-riemann-siegel-gauge-factorization.md",
        "git_blob": "16ab64a193e59608c9e2c9fd9762addc58809c3f",
        "sha256_lf": "11c87fd9b50c309249b76f39fd87c3d20953779355a39a0338ef281d3cb57c87",
        "role": "Exact Riemann-Siegel phase and digamma derivative of the native freezing scale",
    },
]
RUNTIME = {
    "python_flint": "0.9.0",
    "flint": "3.6.0",
    "python": "3.12.10",
    "system": "Windows",
    "machine": "AMD64",
    "native_files": 44,
    "native_files_sha256": "36c07323af58dec0eb6fd82a99bf871924eb69f1833d9af626fc09437ae5b0cc",
}
REFERENCES = [
    {
        "url": "https://python-flint.readthedocs.io/en/latest/general.html",
        "role": "Ball enclosure, certified comparisons, exact rational inputs, series cap",
    },
    {
        "url": "https://python-flint.readthedocs.io/en/latest/acb_series.html",
        "role": "Taylor-series gamma, exp, zeta; no numerical finite differences",
    },
    {
        "url": "https://github.com/flintlib/flint/blob/v3.6.0/doc/source/acb_poly.rst",
        "role": "Pinned library-version series API documentation",
    },
]
CONTRACT = {
    "arithmetic": "FLINT directed complex balls plus exact rational acceptance",
    "primitive": "unrescaled xi(1/2+i*z), exact zeta-gamma product",
    "lambda": "fixed inverse exact Riemann-Siegel phase derivative at anchor",
    "coverage": "nine declared disks only; exactly one simple R5 zero per disk",
    "orientation": "R5 zeros in C+; conjugate C5 zeros in C-",
    "local_noncommon": "C5, R0, C0, f6, W and R5prime exclude zero on each enclosing rectangle",
    "native_quotient": "nine genuine simple poles of R0*C5/(C0*R5), with residue enclosures",
    "inner_premise": "only needed for reduced-inner and global projection interpretation",
    "physical_capture": "no band, high-T, outer-metric or Hilbert-Schmidt conclusion",
    "parameter_exception": "no global exception membership decision at any anchor",
    "proof_trust": "pinned FLINT ball implementation; not a verified implementation of FLINT",
    "RH": "not assumed for local certificates and not concluded",
}
# Scout output is frozen as exact dyadic input; no root finder runs in acceptance.
# Each tuple is (anchor, center-real numerator, center-imag numerator, raw modulus floor /1000).
DISKS = (
    (
        32,
        42034761155286392844123443947936327561204929779360569793,
        1038236505928023023728100327203357217058930427182845279,
        672,
    ),
    (
        32,
        48646761901958011383536958777890710313735072380295558254,
        989149726131168252735411717995278477853215802889087250,
        439,
    ),
    (
        32,
        54927659577449707367303836698233492702742368264140128176,
        864477057460305574443524809281004635524078383579847140,
        722,
    ),
    (
        64,
        93688840983717009192007008556789253600532658229139916088,
        789890996978386783775176156476608619467778670259796651,
        250,
    ),
    (
        64,
        97834042478154200157427569346996071157579646438211961770,
        814867591442383920243490953466341973880501705807673759,
        692,
    ),
    (
        64,
        106281446229931038075008844817687771873282305361521423738,
        741171149737919808331805235542187750006345795707261412,
        451,
    ),
    (
        128,
        191509096009174577046364866943026800845500950959312757904,
        709846627006410942577675275542289692609195710769974424,
        265,
    ),
    (
        128,
        197902795034345061471835965284700334840500589148063009239,
        731344597039956210924763084574469315548503303505219882,
        493,
    ),
    (
        128,
        204316402898964686882481395026318050319508080967420941858,
        700900597613860164803966873403864836257852540086696679,
        438,
    ),
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def integer(value, lower, upper):
    require(type(value) is int and lower <= value <= upper, "strict integer/cap")
    return value


def rational(value):
    require(type(value) in (int, Q), "strict rational type")
    result = Q(value)
    require(
        max(abs(result.numerator).bit_length(), result.denominator.bit_length())
        <= MAX_BITS,
        "rational bit cap",
    )
    return result


def pair(value):
    value = rational(value)
    return [value.numerator, value.denominator]


def unpair(value):
    require(type(value) is list and len(value) == 2, "rational pair")
    n, d = value
    require(type(n) is int and type(d) is int and d > 0, "strict rational components")
    require(max(abs(n).bit_length(), d.bit_length()) <= MAX_BITS, "rational input cap")
    result = rational(Q(n, d))
    require(pair(result) == value, "canonical rational pair")
    return result


def endpoint(value):
    require(
        type(value) is arb and value.is_finite() and value.is_exact(),
        "finite exact arb endpoint",
    )
    frac = value.fmpq()
    return rational(Q(int(frac.numerator), int(frac.denominator)))


def rbounds(value):
    require(type(value) is arb and value.is_finite(), "finite real ball")
    return [pair(endpoint(value.lower())), pair(endpoint(value.upper()))]


def cbounds(value):
    require(type(value) is acb and value.is_finite(), "finite complex ball")
    return {"real": rbounds(value.real), "imag": rbounds(value.imag)}


def qarb(value):
    value = rational(value)
    return arb(fmpq(value.numerator, value.denominator))


def lf(raw):
    require(type(raw) is bytes and len(raw) <= MAX_BYTES, "byte cap")
    normalized = raw.replace(b"\r\n", b"\n")
    text = normalized.decode("utf-8")
    require(
        all(ord(c) in (9, 10) or ord(c) >= 32 for c in text)
        and not any(127 <= ord(c) <= 159 for c in text),
        "source control byte",
    )
    return normalized


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def validate_tree(value, depth=0, budget=None):
    budget = [0] if budget is None else budget
    budget[0] += 1
    require(depth <= MAX_DEPTH and budget[0] <= MAX_NODES, "JSON tree cap")
    if value is None or type(value) is bool:
        return
    if type(value) is str:
        require(len(value) <= MAX_BYTES, "JSON string cap")
        return
    if type(value) is int:
        require(value.bit_length() <= MAX_BITS, "JSON integer cap")
        return
    require(type(value) in (list, dict) and len(value) <= MAX_NODES, "JSON type/cap")
    if type(value) is dict:
        require(all(type(k) is str and len(k) <= 1024 for k in value), "JSON keys")
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
    require(len(raw) <= MAX_BYTES, "canonical byte cap")
    return raw


def pairs_unique(items):
    result = {}
    for key, value in items:
        require(key not in result, "duplicate JSON key")
        result[key] = value
    return result


def load_json(raw):
    require(type(raw) is bytes and len(raw) <= MAX_BYTES, "JSON byte cap")

    def reject(_):
        raise ValueError("noninteger JSON number")

    result = json.loads(
        raw, object_pairs_hook=pairs_unique, parse_float=reject, parse_constant=reject
    )
    validate_tree(result)
    return result


def manifest():
    return {
        "schema": STEM + "-sources-v1",
        "authoring_base": BASE,
        "contract": CONTRACT,
        "frozen_sources": BINDINGS,
        "runtime": RUNTIME,
        "external_documentation": REFERENCES,
    }


def read_source(binding):
    return subprocess.check_output(
        ["git", "show", binding["commit"] + ":" + binding["path"]], cwd=ROOT
    )


def runtime():
    dist = importlib.metadata.distribution("python-flint")
    native = {}
    for path in dist.files:
        if str(path).endswith((".pyd", ".dll")):
            source = Path(dist.locate_file(path))
            require(
                source.is_file() and source.stat().st_size <= 100_000_000,
                "native runtime file cap/missing",
            )
            native[str(path)] = digest(source.read_bytes())
    return {
        "python_flint": flint.__version__,
        "flint": flint.__FLINT_VERSION__,
        "python": platform.python_version(),
        "system": platform.system(),
        "machine": platform.machine(),
        "native_files": len(native),
        "native_files_sha256": digest(canonical(native)),
    }


def authenticate():
    require(
        canonical(load_json(MANIFEST.read_bytes())) == canonical(manifest()),
        "manifest mismatch",
    )
    require(canonical(runtime()) == canonical(RUNTIME), "pinned runtime mismatch")
    for binding in BINDINGS:
        raw = read_source(binding)
        normalized = lf(raw)
        blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        require(blob == binding["git_blob"], "source Git blob mismatch")
        require(digest(normalized) == binding["sha256_lf"], "source LF hash mismatch")
    return BINDINGS


@contextmanager
def precision(bits=PRECISION):
    integer(bits, 192, 512)
    previous = ctx.prec, ctx.cap
    ctx.prec, ctx.cap = bits, 9
    try:
        yield
    finally:
        ctx.prec, ctx.cap = previous


def xi_jet(z, *, reflected=False):
    require(type(z) is acb and z.is_finite(), "finite acb input")
    require(type(reflected) is bool, "strict route flag")
    require(ctx.prec >= 192 and ctx.prec <= 512 and ctx.cap == 9, "arithmetic context")
    # A small compact domain keeps public calls away from removable product poles.
    require(
        z.real > 20 and z.real < 150 and z.imag > 0 and z.imag < 1,
        "declared evaluation domain",
    )
    s = acb(qarb(Q(1, 2))) + acb(0, 1) * acb_series([z, 1])
    if reflected:
        s = 1 - s
    value = s * (s - 1) / 2 * (-(s / 2) * arb.pi().log()).exp()
    value = value * (s / 2).gamma() * s.zeta()
    result = [value[j] * math.factorial(j) for j in range(9)]
    require(all(v.is_finite() for v in result), "nonfinite Xi jet")
    return result


def frozen_lambda(anchor):
    integer(anchor, 32, 128)
    require(anchor in (32, 64, 128), "declared freezing anchor")
    require(192 <= ctx.prec <= 512, "lambda precision")
    omega = (acb(qarb(Q(1, 4)), qarb(Q(anchor, 2))).digamma().real - arb.pi().log()) / 2
    require(omega > 0, "certified positive phase derivative")
    return 1 / omega


def rouche_bounds(residual_upper, derivative_lower, second_upper, radius):
    a, d, m, r = map(rational, (residual_upper, derivative_lower, second_upper, radius))
    require(a >= 0 and d > 0 and m >= 0 and r > 0, "Rouche bound signs")
    left, right = a + m * r * r / 2, d * r
    require(left < right, "strict Rouche inequality failed")
    return pair(left), pair(right)


def disk_inputs(index):
    integer(index, 0, len(DISKS) - 1)
    anchor, nx, ny, coarse = DISKS[index]
    r = Q(1, 2**RADIUS_BITS)
    x, y = Q(nx, 2**CENTER_BITS), Q(ny, 2**CENTER_BITS)
    require(Q(anchor - 6) < x - r and x + r < Q(anchor + 6), "declared real window")
    require(0 < y - r and y + r < 1, "strict off-axis disk")
    c = acb(qarb(x), qarb(y))
    box = acb(arb(c.real, qarb(r)), arb(c.imag, qarb(r)))
    return anchor, x, y, r, coarse, c, box


def companions(jet, lam):
    require(
        type(jet) is list
        and len(jet) == 9
        and all(type(v) is acb and v.is_finite() for v in jet),
        "jet shape",
    )
    require(type(lam) is arb and lam > 0, "positive lambda ball")
    ilam = acb(0, 1) * lam
    return {
        "R0": jet[0] - ilam * jet[1],
        "C0": jet[0] + ilam * jet[1],
        "R5": jet[5] - ilam * jet[6],
        "C5": jet[5] + ilam * jet[6],
        "R5prime": jet[6] - ilam * jet[7],
        "R5second": jet[7] - ilam * jet[8],
        "f6": jet[6],
        "W": jet[0] * jet[6] - jet[1] * jet[5],
    }


def theta_jets(jet, lam):
    ilam = acb(0, 1) * lam
    r = [jet[k] - ilam * jet[k + 1] for k in range(3)]
    c = [jet[k] + ilam * jet[k + 1] for k in range(3)]
    require(c[0].abs_lower() > 0, "Theta denominator excludes zero")
    t0 = r[0] / c[0]
    t1 = (r[1] - t0 * c[1]) / c[0]
    t2 = (r[2] - t0 * c[2] - 2 * t1 * c[1]) / c[0]
    return [t0, t1, t2]


def record(index, bits=PRECISION):
    with precision(bits):
        anchor, x, y, radius, coarse, center, box = disk_inputs(index)
        lam = frozen_lambda(anchor)
        point = xi_jet(center)
        region = xi_jet(box)
        reflected_point = xi_jet(center, reflected=True)
        reflected_region = xi_jet(box, reflected=True)
        require(
            all(a.overlaps(b) for a, b in zip(point, reflected_point)),
            "functional equation point disagreement",
        )
        require(
            all(a.overlaps(b) for a, b in zip(region, reflected_region)),
            "functional equation rectangle disagreement",
        )
        p, q = companions(point, lam), companions(region, lam)
        residual = endpoint(p["R5"].abs_upper())
        derivative = endpoint(p["R5prime"].abs_lower())
        second = endpoint(q["R5second"].abs_upper())
        left, right = rouche_bounds(residual, derivative, second, radius)
        require(unpair(left) * 2**50 < unpair(right), "declared Rouche slack")
        nonzero = {}
        for key in ("C5", "R0", "C0", "f6", "W", "R5prime"):
            lower = endpoint(q[key].abs_lower())
            require(lower > 0, "local nonzero guard: " + key)
            nonzero[key] = pair(lower)
        theta = theta_jets(region, lam)
        theta_abs = abs(theta[0])
        require(
            theta_abs > qarb(Q(coarse, 1000)) and theta_abs < qarb(Q(coarse + 1, 1000)),
            "raw modulus corridor",
        )
        require(theta_abs > qarb(Q(1, 4)), "raw modulus >1/4")
        # This identity is checked on the actual input, not a synthetic coefficient model.
        identity = q["R0"] * q["C5"] - q["C0"] * q["R5"] - 2 * acb(0, 1) * lam * q["W"]
        require(identity.contains(0), "companion W identity")
        return {
            "id": index,
            "anchor": anchor,
            "center": [pair(x), pair(y)],
            "radius": pair(radius),
            "rectangle": {
                "real": [pair(x - radius), pair(x + radius)],
                "imag": [pair(y - radius), pair(y + radius)],
            },
            "lambda": rbounds(lam),
            "precision_bits": bits,
            "point_Xi_derivatives_0_to_8": [cbounds(v) for v in point],
            "rectangle_Xi_derivatives_0_to_8": [cbounds(v) for v in region],
            "reflected_point_Xi_derivatives_0_to_8": [
                cbounds(v) for v in reflected_point
            ],
            "reflected_rectangle_Xi_derivatives_0_to_8": [
                cbounds(v) for v in reflected_region
            ],
            "rectangle_companions": {k: cbounds(v) for k, v in q.items()},
            "rouche": {
                "residual_upper": pair(residual),
                "derivative_lower": pair(derivative),
                "second_upper": pair(second),
                "left": left,
                "right": right,
                "zeros_counted_with_multiplicity": 1,
            },
            "positive_modulus_lower": nonzero,
            "rectangle_raw_Theta0_derivatives_0_to_2": [cbounds(v) for v in theta],
            "raw_Theta0_modulus": rbounds(theta_abs),
            "native_quotient_residue_at_root": cbounds(
                q["R0"] * q["C5"] / (q["C0"] * q["R5prime"])
            ),
            "raw_Theta0_coarse_strict_bounds": [
                pair(Q(coarse, 1000)),
                pair(Q(coarse + 1, 1000)),
            ],
        }


def seal(report):
    require(type(report) is dict and "payload_sha256" not in report, "seal input")
    return {**report, "payload_sha256": digest(canonical(report))}


def build_report():
    authenticate()
    rows = [record(j) for j in range(len(DISKS))]
    # Exact disjointness within each parameter; there is deliberately no region census.
    for j, row in enumerate(rows):
        for other in rows[:j]:
            if row["anchor"] == other["anchor"]:
                require(
                    abs(unpair(row["center"][0]) - unpair(other["center"][0]))
                    > unpair(row["radius"]) + unpair(other["radius"]),
                    "disk disjointness",
                )
    artifacts = {
        p.relative_to(ROOT).as_posix(): digest(lf(p.read_bytes()))
        for p in (NOTE, Path(__file__), MANIFEST, TEST)
    }
    return seal(
        {
            "schema": STEM + "-v1",
            "contract": CONTRACT,
            "frozen_sources": BINDINGS,
            "runtime": RUNTIME,
            "precision_bits": PRECISION,
            "disks": rows,
            "artifacts": artifacts,
        }
    )


def check_report(report):
    validate_tree(report)
    require(type(report) is dict and "payload_sha256" in report, "report shape")
    unsigned = {k: v for k, v in report.items() if k != "payload_sha256"}
    require(report["payload_sha256"] == digest(canonical(unsigned)), "payload seal")
    require(
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
        output = manifest()
    elif args.emit:
        output = build_report()
    else:
        check_report(load_json(FIXTURE.read_bytes()))
        print(
            "PASS: nine actual-Xi off-axis simple-zero disks; six source pins; no census/RH"
        )
        return
    print(json.dumps(output, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
