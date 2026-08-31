#!/usr/bin/env python3
"""Small directed consumer of the original infinite physical Gram."""

from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
import json
from math import comb
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
GRAM_FILE = "physical_infinity_L96_p192.acquisition.json"
GRAM_SHA = "e828069e8898a464741553a44f53a13bb11d93c5c27ed5475130656a99749757"
GRAM_PRODUCER_SHA = "9eaad7aac963f0ad13d2d4a2656258bf172e61fc51fbb5af74a0aff7f1b13207"
SCOUT_FILE = "physical_infinity_L32.scout.json"
SCOUT_SHA = "61373d9ef78367814ff62e82689254f94c2965a130b409433daf819520f56778"
CENTER = (F("-0.08213318656215898"), F("1.1219897873534914"))
RADIUS = F(1, 100000000)
MARK = F(99, 100)
HEIGHT = F(1, 100)
PRECISION = 192
OUTPUT = HERE / "variational_certificate.verification.json"
PRIMITIVES = (
    ("ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc", "6810bcece309b0c54ae6c8fc84b314990004549c"),
    ("ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc", "d7330d114ebba1a7a16e22fa9ba6aa6b5eb7cdd6"),
    ("69b5322bc872b46d42d4f74e13dcbeb96c1421da", "2113ce2bef593e19ca647c12c4fbb3c0728572a2"),
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, "duplicate JSON key")
        result[key] = value
    return result


def typed_equal(left, right):
    """Exact JSON equality; Boolean and numeric aliases are not interchangeable."""
    if type(left) is not type(right):
        return False
    if type(left) is dict:
        return left.keys() == right.keys() and all(
            typed_equal(left[key], right[key]) for key in left)
    if type(left) is list:
        return len(left) == len(right) and all(
            typed_equal(a, b) for a, b in zip(left, right))
    return left == right


def read_authenticated(name, digest):
    raw = (HERE / name).read_bytes()
    require(len(raw) <= 2_000_000, "bounded source capture")
    require(sha256(raw).hexdigest() == digest, "input content hash: " + name)
    return json.loads(raw, object_pairs_hook=unique_object)


def rational(text):
    require(type(text) is str and len(text) <= 3000, "literal rational string")
    value = F(text)
    require(max(abs(value.numerator).bit_length(), value.denominator.bit_length()) <= 4096,
            "bounded rational input")
    return value


def fraction_of_arb_point(value):
    return F(str(value.fmpq()))


def bounds(value):
    require(value.is_finite(), "finite directed ball")
    return (fraction_of_arb_point(value.lower()), fraction_of_arb_point(value.upper()))


def encoded(value):
    lo, hi = bounds(value)
    return [str(lo), str(hi)]


def arb_fraction(value, arb):
    return arb(value.numerator) / value.denominator


def ball(lo, hi, arb):
    require(lo <= hi, "ordered exact endpoints")
    mid = arb_fraction((lo + hi) / 2, arb)
    radius = arb_fraction((hi - lo) / 2, arb)
    return mid + arb(0, radius.upper())


def from_pair(pair, arb):
    require(type(pair) is list and len(pair) == 2, "rational endpoint pair")
    return ball(rational(pair[0]), rational(pair[1]), arb)


def dot(left, right, arb):
    require(len(left) == len(right), "dot-product dimensions")
    return sum((x * y for x, y in zip(left, right)), arb(0))


def matvec(matrix, vector, arb):
    return [dot(row, vector, arb) for row in matrix]


def bilinear(left, matrix, right, arb):
    return dot(left, matvec(matrix, right, arb), arb)


def plane(arb):
    out = [[arb(0) for _ in range(4)] for _ in range(21)]
    for j in (0, 10, 12, 13, 14, 18, 20):
        out[j][0] = arb(1)
    out[1][1] = arb(1)
    out[10][2] = arb(-2)
    out[7][3] = arb(2)
    return out


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def small_gram(full, P, arb):
    columns = transpose(P)
    return [[bilinear(a, full, b, arb) for b in columns] for a in columns]


def profile(parameter, arb):
    lam, mu = parameter
    require(mu > 0, "positive slope in profile box")
    A = 1 + (lam - arb(1) / 2) / mu
    B = arb(1) / 2 - (lam * lam - lam + arb(1) / 3) / (2 * mu * mu)
    C2 = arb(1) / 2 + (lam / 2 - arb(1) / 3) / mu
    return [arb(1), A, B, C2]


def profile_derivatives(parameter, arb):
    lam, mu = parameter
    return [
        [arb(0), 1 / mu, -(2 * lam - 1) / (2 * mu**2), 1 / (2 * mu)],
        [arb(0), -(lam - arb(1) / 2) / mu**2,
         (lam * lam - lam + arb(1) / 3) / mu**3,
         -(lam / 2 - arb(1) / 3) / mu**2],
    ]


def equation(parameter, gram, arb):
    linear = matvec(gram, profile(parameter, arb), arb)[1:]
    return [linear[2] * parameter[0] + linear[0],
            linear[2] * parameter[1] + linear[1]]


def jacobian(parameter, gram, arb):
    linear = matvec(gram, profile(parameter, arb), arb)[1:]
    derivatives = [matvec(gram, v, arb)[1:]
                   for v in profile_derivatives(parameter, arb)]
    return [[derivatives[k][2] * parameter[i] + derivatives[k][i]
             + (linear[2] if i == k else arb(0)) for k in range(2)]
            for i in range(2)]


def inverse_midpoint(matrix):
    midpoint = [[sum(bounds(value), F(0)) / 2 for value in row] for row in matrix]
    a, b = midpoint[0]
    c, d = midpoint[1]
    determinant = a * d - b * c
    require(determinant != 0, "invertible rational root preconditioner")
    return [[d / determinant, -b / determinant],
            [-c / determinant, a / determinant]]


def certify_root(gram, arb):
    center = [arb_fraction(x, arb) for x in CENTER]
    box = [ball(x - RADIUS, x + RADIUS, arb) for x in CENTER]
    J = jacobian(box, gram, arb)
    pre = inverse_midpoint(jacobian(center, gram, arb))
    pre_ball = [[arb_fraction(x, arb) for x in row] for row in pre]
    residual = equation(center, gram, arb)
    error = [[arb(int(i == j)) - sum((pre_ball[i][k] * J[k][j]
              for k in range(2)), arb(0)) for j in range(2)] for i in range(2)]
    displacement = []
    for interval, origin in zip(box, CENTER):
        lo, hi = bounds(interval)
        displacement.append(ball(lo - origin, hi - origin, arb))
    K = [center[i] - dot(pre_ball[i], residual, arb)
         + dot(error[i], displacement, arb) for i in range(2)]
    contraction = max(sum((bounds(abs(x))[1] for x in row), F(0)) for row in error)
    require(contraction < 1, "strict root contraction")
    for original, image in zip(box, K):
        lo, hi = bounds(original)
        klo, khi = bounds(image)
        require(lo < klo and khi < hi, "strict inward Krawczyk image")
    lam, mu = box
    u0 = -lam / mu
    u1 = (1 - lam) / mu
    require(mu > 0 and lam < 0 and lam + mu > 1, "strict both-clipped regime")
    require(u0 > 0 and u1 < 1 and u1 - u0 > 0, "strict ordered clipping endpoints")
    return box, {
        "center": list(map(str, CENTER)), "nominal_radius": str(RADIUS),
        "actual_box": list(map(encoded, box)), "krawczyk_image": list(map(encoded, K)),
        "residual_at_center": list(map(encoded, residual)),
        "rational_preconditioner": [[str(x) for x in row] for row in pre],
        "contraction_upper": str(contraction),
        "lower_clip_endpoint": encoded(u0), "upper_clip_endpoint": encoded(u1),
    }


def quadratic_minimum(coefficients):
    C, B, A = coefficients
    candidates = [(C, F(0)), (A + B + C, F(1))]
    if A > 0 and -2 * A < B < 0:
        candidates.append((C - B * B / (4 * A), -B / (2 * A)))
    return min(candidates)


def cone_record(theta):
    records = []
    def c(j):
        return theta[j - 1]
    for sigma, tau in product((0, 1), repeat=2):
        pp = (c(2)-2*sigma*c(13)+tau*c(6), c(4)-2*sigma*c(20)+tau*c(15),
              c(17)-c(18)-2*sigma*c(14)+tau*c(8))
        qq = (c(3)-2*sigma*c(12)+tau*c(9), c(5)-2*sigma*c(18)+tau*c(16),
              c(19)-c(20)-2*sigma*c(14)+tau*c(11))
        for name, coefficients in (("p", pp), ("q", qq)):
            lower = quadratic_minimum([bounds(x)[0] for x in coefficients])
            upper = quadratic_minimum([bounds(x)[1] for x in coefficients])
            status = "PASS" if lower[0] >= 0 else "FAIL" if upper[0] < 0 else "UNKNOWN"
            records.append({"name": name+str(sigma)+str(tau), "status": status,
                            "coefficients": list(map(encoded, coefficients)),
                            "lower_envelope_minimum": list(map(str, lower)),
                            "upper_envelope_minimum": list(map(str, upper))})
    return records


def terminal_vectors(arb):
    length = 1 - MARK
    L = [F(0)] * 21
    Q = [F(0)] * 21
    for j in (2, 4, 17):
        L[j] += length
    L[18] -= length
    for j in (13, 14, 20):
        L[j] -= length * (1 + MARK)
    for j in (6, 8, 15):
        Q[j] += length
    return L, Q, [arb_fraction(x, arb) for x in L], [arb_fraction(x, arb) for x in Q]


MOMENT_FORMS = (
    ((0, 1, 0), 0), ((0, 0, 1), 0), ((0, 0, 1), 1),
    ((0, 1, 1), 0), ((1, 0, 1), 1), ((0, 0, 2), 0),
    ((0, 2, 0), 0), ((0, 2, 2), 0), ((0, 0, 2), 1),
    ((2, 0, 0), 1), ((2, 0, 2), 1), ((0, 2, 0), 2),
    ((2, 0, 0), 2), ((2, 2, 0), 2), ((0, 1, 2), 0),
    ((1, 0, 2), 1), ((0, 2, 1), 0), ((1, 2, 0), 2),
    ((2, 0, 1), 1), ((2, 1, 0), 2),
)


def monomial_segment(start, end, exponent, variable):
    """Integrate a literal monomial one-form on an affine segment over [0,1]."""
    polynomial = [F(1)]
    for origin, destination, power in zip(start, end, exponent):
        linear_power = [F(comb(power, k)) * origin**(power-k)
                        * (destination-origin)**k for k in range(power+1)]
        multiplied = [F(0)] * (len(polynomial)+len(linear_power)-1)
        for i, a in enumerate(polynomial):
            for j, b in enumerate(linear_power):
                multiplied[i+j] += a*b
        polynomial = multiplied
    return (end[variable]-start[variable]) * sum(
        (value/F(k+1) for k, value in enumerate(polynomial)), F(0))


def monomial_path(points, exponent, variable):
    return sum((monomial_segment(points[k], points[k+1], exponent, variable)
                for k in range(len(points)-1)), F(0))


def literal_current(points, a, b):
    total = F(0)
    for variable in range(3):
        if a[variable]:
            exponent = tuple(a[i]+b[i]-int(i == variable) for i in range(3))
            total += 2*monomial_path(points, exponent, variable)
    return total


def decoder_difference(a, b, delta):
    """Apply the endpoint-exact source identity to a zero-endpoint difference."""
    m = tuple(x+y for x, y in zip(a, b))
    signed = tuple(x-y for x, y in zip(a, b))
    singles = [i for i in range(3) if m[i] == 1]
    doubles = [i for i in range(3) if m[i] == 2]
    if not singles:
        return F(0)
    anchor = None if doubles else max(singles)
    value = F(0)
    for i in singles:
        if i == anchor:
            continue
        coefficient = signed[i] if anchor is None else signed[i]-signed[anchor]
        exponent = tuple(m[k]-int(i == k) for k in range(3))
        j = MOMENT_FORMS.index((exponent, i)) + 1
        value += coefficient*delta[j]
    return value


def literal_terminal_control(delta):
    old = [(MARK, F(1), F(0)), (F(1), F(1), F(0)), (F(1), F(1), F(1))]
    new = [(MARK, F(1), F(0)), (MARK, F(1), HEIGHT),
           (F(1), F(1), HEIGHT), (F(1), F(1), F(1))]
    measured = [F(0)] + [monomial_path(new, exponent, variable)
                        - monomial_path(old, exponent, variable)
                        for exponent, variable in MOMENT_FORMS]
    require(measured == delta, "all20 literal segment integrals versus terminal vectors")
    records = []
    for a, b in product(product((0, 1), repeat=3), repeat=2):
        direct = literal_current(new, a, b)-literal_current(old, a, b)
        require(direct == decoder_difference(a, b, measured),
                "all64 literal factor-two currents versus exact moment decoder")
        records.append({"a": list(a), "b": list(b), "current_difference": str(direct)})
    return {"old_terminal_points": [[str(x) for x in p] for p in old],
            "new_terminal_points": [[str(x) for x in p] for p in new],
            "direct_moment_difference21": list(map(str, measured)),
            "all64_current_differences": records}


def build():
    data = read_authenticated(GRAM_FILE, GRAM_SHA)
    scout = read_authenticated(SCOUT_FILE, SCOUT_SHA)
    require(data["producer_sha256"] == GRAM_PRODUCER_SHA, "Gram producer binding")
    require(data["status"] == "directed infinite physical Gram acquisition; independent replay pending",
            "directed acquisition status")
    require(type(data["L"]) is int and data["L"] == 96, "fixed product cutoff")
    require(type(data["precision_bits"]) is int and data["precision_bits"] == PRECISION,
            "fixed input precision")
    require(data["local_product_truncation"] is True, "local product truncation interface")
    require(data["source_norm"] == "Euclidean norm of twenty declared occupation coordinates",
            "source normalization")
    require(tuple((x["commit"], x["blob"]) for x in data["primitive_sources"]) == PRIMITIVES,
            "primitive manifest")
    require(tuple(F(str(x)) for x in scout["lambda_mu"]) == CENTER, "fixed scout center")
    sys.path.insert(0, str(Path.home() / ".cache/riemann-five-hour-deps"))
    from flint import arb, ctx
    ctx.prec = PRECISION
    entries = data["gram21_intervals"]
    require(type(entries) is list and len(entries) == 21 and
            all(type(row) is list and len(row) == 21 for row in entries), "full21 Gram shape")
    gram = [[from_pair(x, arb) for x in row] for row in entries]
    for i in range(21):
        for j in range(i):
            require(gram[i][j].overlaps(gram[j][i]), "inherited Gram symmetry")
    require(from_pair(data["frame_lower_interval"], arb) > 0, "inherited positive20 frame")
    P = plane(arb)
    small = small_gram(gram, P, arb)
    parameter, root = certify_root(small, arb)
    x = profile(parameter, arb)
    moments = matvec(P, x, arb)
    theta = matvec(gram, moments, arb)[1:]
    require(theta[6] > 0, "positive planar support coefficient C normalization")
    cone = cone_record(theta)
    s = arb_fraction(MARK, arb)
    epsilon = arb_fraction(HEIGHT, arb)
    require(s > (1 - parameter[0]) / parameter[1], "fixed mark lies on upper plateau")
    exactL, exactQ, L, Q = terminal_vectors(arb)
    literal_control = literal_terminal_control(
        [HEIGHT*l+HEIGHT**2*q for l, q in zip(exactL, exactQ)])
    a = bilinear(L, gram, moments, arb)
    b = bilinear(Q, gram, moments, arb)
    LL = bilinear(L, gram, L, arb)
    LQ = bilinear(L, gram, Q, arb)
    QQ = bilinear(Q, gram, Q, arb)
    require(a < 0, "actual negative first-order terminal variation")
    quartic = [2*a, 2*b+LL, 2*LQ, QQ]
    change = sum((coefficient * epsilon**power
                  for power, coefficient in enumerate(quartic, 1)), arb(0))
    delta = [epsilon*l + epsilon**2*q for l, q in zip(L, Q)]
    direct_change = 2*bilinear(moments, gram, delta, arb)+bilinear(delta, gram, delta, arb)
    require(change.overlaps(direct_change), "quartic versus complete-vector change")
    require(change < 0 and direct_change < 0, "strict original-energy descent at fixed height")
    old_energy = bilinear(moments, gram, moments, arb)
    new_moments = [x+y for x, y in zip(moments, delta)]
    new_energy = bilinear(new_moments, gram, new_moments, arb)
    return {
        "schema": "native-infinite-terminal-variation-v1",
        "status": "CERTIFIED_W_LAST_MINIMUM_AND_LEGAL_STRICT_DESCENT",
        "inputs": {GRAM_FILE: GRAM_SHA, SCOUT_FILE: SCOUT_SHA},
        "gram_producer_sha256": GRAM_PRODUCER_SHA,
        "precision_bits": PRECISION, "root": root,
        "profile_moments_1_A_B_Cover2": list(map(encoded, x)),
        "moment21": list(map(encoded, moments)), "gradient20": list(map(encoded, theta)),
        "positive_planar_coefficient": encoded(theta[6]), "full_path_cone": cone,
        "terminal_mark": str(MARK), "early_height": str(HEIGHT),
        "exact_terminal_L21": list(map(str, exactL)), "exact_terminal_Q21": list(map(str, exactQ)),
        "independent_literal_terminal_control": literal_control,
        "first_order_half_coefficient": encoded(a),
        "energy_quartic_coefficients": list(map(encoded, quartic)),
        "energy_change_quartic": encoded(change), "energy_change_direct": encoded(direct_change),
        "w_last_minimum_energy": encoded(old_energy), "improving_path_energy": encoded(new_energy),
        "improving_path_moment21": list(map(encoded, new_moments)),
        "certified_global_w_last_minimum": True,
        "certified_full_three_coordinate_minimum": False,
        "certified_legal_terminal_descent": True,
        "independent_Gram_replay_performed_here": False,
        "full_retained_gamma_identified": False,
    }


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write", action="store_true")
    group.add_argument("--check", action="store_true")
    args = parser.parse_args()
    try:
        result = build()
    except ValueError as exc:
        result = {"schema": "native-infinite-terminal-variation-v1", "status": "REFUSED",
                  "reason": str(exc), "inputs": {GRAM_FILE: GRAM_SHA, SCOUT_FILE: SCOUT_SHA}}
    result["producer_sha256"] = sha256(Path(__file__).read_bytes()).hexdigest()
    result["proof_note_sha256"] = sha256((HERE / "NATIVE_INFINITY_VARIATIONAL_THEORY.md").read_bytes()).hexdigest()
    result["preregistration_sha256"] = sha256((HERE / "variational_PREREGISTRATION.md").read_bytes()).hexdigest()
    if args.write:
        OUTPUT.write_text(json.dumps(result, indent=2, allow_nan=False) + "\n", encoding="utf8")
    else:
        require(typed_equal(json.loads(OUTPUT.read_text(encoding="utf8"),
                                       object_pairs_hook=unique_object), result),
                "complete exact replay")
    print(json.dumps({key: result[key] for key in
                     ("status", "first_order_half_coefficient", "energy_change_quartic")
                     if key in result}, indent=2))
    require(result["status"] != "REFUSED", result.get("reason", "refused"))


if __name__ == "__main__":
    main()
