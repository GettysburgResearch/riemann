#!/usr/bin/env python3
"""Exact finite controls for the proposed compact Pick lemmas.

The mathematical theorem is in DENOMINATOR_FRAME.md. This executable checks
its strict rational sufficient inequalities, independent finite algebra,
and an exact synthetic counterexample. It does not prove the imported
all-height count or rerun the Platt--Trudgian height computation.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from fractions import Fraction as Q
from itertools import combinations
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve().parent
CERTIFICATE = HERE.parent / "certificates" / "hardy_z_certificate.json"
ANCHOR_PRODUCER = HERE.parent / "certificates" / "certify_hardy_z.py"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def digest_bytes(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def rational_receipt(value: Q) -> dict:
    raw = f"{value.numerator:x}/{value.denominator:x}".encode("ascii")
    return {"sha256_of_hex_fraction": digest_bytes(raw),
            "numerator_bits": abs(value.numerator).bit_length(),
            "denominator_bits": value.denominator.bit_length(),
            "sign": (value > 0) - (value < 0)}


def determinant(matrix: list[list[Q]]) -> Q:
    a = [row[:] for row in matrix]
    n = len(a)
    value = Q(1)
    for j in range(n):
        pivot = next((i for i in range(j, n) if a[i][j]), None)
        if pivot is None:
            return Q(0)
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            value = -value
        p = a[j][j]
        value *= p
        for i in range(j + 1, n):
            ratio = a[i][j] / p
            for k in range(j + 1, n):
                a[i][k] -= ratio * a[j][k]
    return value


def matmul(a: list[list[Q]], b: list[list[Q]]) -> list[list[Q]]:
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), Q(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a: list[list[Q]]) -> list[list[Q]]:
    return [list(row) for row in zip(*a)]


def poly_product(roots: list[Q]) -> list[Q]:
    """Ascending coefficients of prod(u^2+root)."""
    poly = [Q(1)]
    for r in roots:
        new = [Q(0)] * (len(poly) + 2)
        for i, value in enumerate(poly):
            new[i] += r * value
            new[i + 2] += value
        poly = new
    return poly


def polyval(poly: list[Q], x: Q) -> Q:
    return sum((value * x ** i for i, value in enumerate(poly)), Q(0))


def newton_matrix(nodes: list[Q]) -> list[list[Q]]:
    n = len(nodes)
    return [[Q(1, 1) / prod(nodes[k] - nodes[j]
                         for j in range(i + 1) if j != k)
             if k <= i else Q(0)
             for k in range(n)] for i in range(n)]


def prod(values) -> Q:
    result = Q(1)
    for value in values:
        result *= value
    return result


def critical_kernel(nodes: list[Q], squared: list[Q]) -> list[list[Q]]:
    return [[sum((2 * (x * y + r) / ((x*x + r)*(y*y + r))
                  for r in squared), Q(0)) for y in nodes] for x in nodes]


def check_anchor_algebra() -> list[dict]:
    receipts = []
    for squared, nodes, scale in [
        ([Q(200), Q(441)], [Q(1), Q(2), Q(5), Q(8)], Q(14)),
        ([Q(200), Q(441), Q(626)],
         [Q(1), Q(2), Q(3), Q(5), Q(8), Q(13)], Q(20)),
    ]:
        n, m = len(nodes), len(squared)
        gram = critical_kernel(nodes, squared)
        vandermonde = prod(y-x for x, y in combinations(nodes, 2))
        target = (2**n * prod(squared)
                  * prod((r2-r1)**4 for r1, r2 in combinations(squared, 2))
                  * vandermonde**2
                  / prod(prod(x*x+r for r in squared)**2 for x in nodes))
        require(determinant(gram) == target, "Anchor determinant identity")

        rs = [r / scale**2 for r in squared]
        us = [x / scale for x in nodes]
        coefficients = [[Q(0)] * n for _ in range(n)]
        metric = []
        for j, r in enumerate(rs):
            polynomial = poly_product(rs[:j] + rs[j+1:])
            for i, value in enumerate(polynomial):
                coefficients[i][2*j] = value
                coefficients[i+1][2*j+1] = value
            metric.extend([r, Q(1)])
        weighted = [[value * metric[j] for j, value in enumerate(row)]
                    for row in coefficients]
        b0 = matmul(weighted, transpose(coefficients))
        t = newton_matrix(us)
        v = [[u**k for k in range(n)] for u in us]
        w = matmul(t, v)
        expected = [[2 / scale**2 * value for value in row]
                    for row in matmul(matmul(w, b0), transpose(w))]
        denominators = [polyval(poly_product(rs), u) for u in us]
        weighted_t = [[value * denominators[j] for j, value in enumerate(row)]
                      for row in t]
        actual = matmul(matmul(weighted_t, gram), transpose(weighted_t))
        require(actual == expected, "Denominator-frame Gram identity")

        # Exact inverse trace from cofactors, independent of its closed formula.
        det_b0 = determinant(b0)
        inverse_trace = sum((determinant([
            [b0[i][j] for j in range(n) if j != k]
            for i in range(n) if i != k]) / det_b0
                             for k in range(n)), Q(0))
        formula = sum(((1+1/r) * sum((r**(2*k) for k in range(m)), Q(0))
                       / prod(rs[k]-r for k in range(m) if k != j)**2
                       for j, r in enumerate(rs)), Q(0))
        require(inverse_trace == formula, "Inverse Cauchy/Vandermonde trace")
        receipts.append({"order": n, "squared_anchors": list(map(str, squared)),
                         "nodes": list(map(str, nodes)),
                         "three_exact_identities": "PASS"})
    return receipts


def anchor_frame_data(anchors: list[tuple[Q, Q]], order: int, extent: Q,
                      scale: Q) -> tuple[Q, list[Q], Q]:
    require(order >= 2 and order % 2 == 0, "Even positive order required")
    require(len(anchors) >= order // 2, "Insufficient anchor intervals")
    require(extent > 0 and scale > 0, "Invalid compact parameters")
    selected = anchors[:order // 2]
    require(all(0 < left < right for left, right in selected),
            "Positive ordinate intervals required")
    require(all(selected[i][1] < selected[i+1][0]
                for i in range(len(selected)-1)), "Anchor intervals overlap")
    rs = [(left**2 / scale**2, right**2 / scale**2)
          for left, right in selected]
    tau = Q(0)
    m = len(rs)
    for j, (lower, upper) in enumerate(rs):
        sigma = prod((lower-hi if k < j else lo-upper)
                     for k, (lo, hi) in enumerate(rs) if k != j)
        require(sigma > 0, "Nonpositive anchor separation")
        tau += ((1+1/lower) * sum((upper**(2*k) for k in range(m)), Q(0))
                / sigma**2)
    u = extent / scale
    j_bound = sum((comb(i, k)**2 * u**(2*(i-k))
                   for i in range(order) for k in range(i+1)), Q(0))
    poly = poly_product([hi for lo, hi in rs])
    derivatives = [sum((poly[k] * comb(k, i) * u**(k-i)
                        for k in range(i, len(poly))), Q(0))
                   for i in range(order)]
    anchor_lower = 2 / (scale**2 * tau * j_bound)
    return anchor_lower, derivatives, u


def height_sums(height: Q) -> tuple[Q, Q, Q]:
    # At H=3e12: H<2^42 and log(2)<3/4, so log(H)<63/2.
    # The exact positive partial sum of exp(3/4) exceeds 2.
    require(height == 3 * 10**12, "This receipt fixes the imported height")
    require(height < 2**42, "Height logarithm enclosure")
    require(1 + Q(3,4) + Q(3,4)**2/2 + Q(3,4)**3/6 > 2,
            "Exact exp lower bound")
    return (Q(382, 9) / height**3, Q(951,25) / height**5,
            Q(1772,49) / height**7)


def frame_bound(anchors: list[tuple[Q, Q]], order: int, extent: Q,
                scale: Q, height: Q, width: Q, negative_features: bool = False,
                recompleted_features: bool = False) -> dict:
    require(height > width >= 0, "Invalid source parameters")
    anchor_lower, derivatives, u = anchor_frame_data(anchors, order, extent, scale)
    s4, s6, s8 = height_sums(height)
    beta = 2 * scale / height
    bs = [sum((derivatives[i-p] * beta**p for p in range(i+1)), Q(0))
          for i in range(order)]
    b_bound = sum((b*b for b in bs), Q(0))
    error_upper = 12 * width**2 * s4 * b_bound
    if negative_features:
        beta = scale / height
        first = [u*comb(k+3,3)*beta**k
                 + (comb(k+2,3)*beta**(k-1) if k >= 1 else Q(0))
                 for k in range(order)]
        second = [u*u*comb(k+3,3)*beta**k
                  + (2*u*comb(k+2,3)*beta**(k-1) if k >= 1 else Q(0))
                  + (comb(k+1,3)*beta**(k-2) if k >= 2 else Q(0))
                  for k in range(order)]
        v_bound = sum((sum((derivatives[i-k]*first[k] for k in range(i+1)), Q(0))**2
                       for i in range(order)), Q(0))
        w_bound = sum((sum((derivatives[i-k]*second[k] for k in range(i+1)), Q(0))**2
                       for i in range(order)), Q(0))
        error_upper = 16*width**2*(scale**2*v_bound*s6
                                  + scale**4*w_bound*s8/(1-width**2/height**2))
    if recompleted_features:
        require(1-6*width**2/height**2 > 0, "Recompleted odd square not positive")
        beta = scale / height
        feature_bounds = {}
        for degree in (2,3):
            coefficients = [sum((comb(degree,j)*u**(degree-j)*comb(k-j+3,3)*beta**(k-j)
                                 for j in range(min(degree,k)+1)), Q(0))
                            for k in range(order)]
            feature_bounds[degree] = sum((sum((derivatives[i-k]*coefficients[k]
                                              for k in range(i+1)), Q(0))**2
                                         for i in range(order)), Q(0))
        s10 = Q(2845,81)/height**9
        error_upper = 16*width**2*(scale**4*feature_bounds[2]*s8/(1-width**2/height**2)
                                 + scale**6*feature_bounds[3]*s10/(1-6*width**2/height**2))
    ratio = anchor_lower / error_upper if error_upper else None
    method = ("RECOMPLETED_NEGATIVE_FEATURES" if recompleted_features else
              "EXACT_NEGATIVE_FEATURES" if negative_features else "SIGNED_SHADOW")
    return {"method": method,
            "order": order, "extent": str(extent), "scale": str(scale),
            "height": str(height), "strip_width": str(width),
            "strict_sufficient_inequality": anchor_lower > error_upper,
            "margin_ratio_floor": ratio.numerator // ratio.denominator,
            "anchor_lower": rational_receipt(anchor_lower),
            "signed_error_upper": rational_receipt(error_upper),
            "exact_margin": rational_receipt(anchor_lower-error_upper)}


def check_negative_feature_identity() -> dict:
    a, b, m = Q(3,8), Q(1025), Q(256)
    c, h = b*b-a*a, 4*a*a*b*b
    denominator = lambda x: (x*x+c)**2+h
    p = lambda t: 4*m*(t+c)/((t+c)**2+h)
    nodes = [Q(1,10), Q(1), Q(14), Q(100)]
    for x in nodes:
        for y in nodes:
            fsx = [x**k/denominator(x) for k in range(4)]
            fsy = [y**k/denominator(y) for k in range(4)]
            split = 4*m*(c*(c*c+h)*(fsx[0]+fsx[2]/c)*(fsy[0]+fsy[2]/c)
                         +(fsx[3]+c*fsx[1])*(fsy[3]+c*fsy[1])
                         -h*fsx[1]*fsy[1]-h/c*fsx[2]*fsy[2])
            native = (x*p(x*x)+y*p(y*y))/(x+y)
            require(split == native, "Quartet positive/negative square identity")
            recompleted = 4*m*(c*(c*c+h)*(fsx[0]+fsx[2]/c)*(fsy[0]+fsy[2]/c)
                               +(c*c-h)*(fsx[1]+c*fsx[3]/(c*c-h))
                                 *(fsy[1]+c*fsy[3]/(c*c-h))
                               -h/c*fsx[2]*fsy[2]-h/(c*c-h)*fsx[3]*fsy[3])
            require(recompleted == native, "Quartet recompleted square identity")
    return {"status": "PASS_TWO_EXACT_QUARTET_SPLITS", "rational_entries": 2*len(nodes)**2,
            "parameters": {"a":str(a),"b":str(b),"m":str(m)}}


def check_single_reserve_counterexample() -> dict:
    r, e, a, b, m, h0 = Q(200), Q(1), Q(3,8), Q(1025), Q(256), Q(1024)
    c, h = b*b-a*a, 4*a*a*b*b
    p = lambda t: 2*e/(t+r) + 4*m*(t+c)/((t+c)**2+h)
    nodes = [Q(10250*i) for i in range(1,5)]
    kernel = [[(x*p(x*x)+y*p(y*y))/(x+y) for y in nodes] for x in nodes]
    positive_minors = 0
    for size in range(1,4):
        for indices in combinations(range(4), size):
            minor = [[kernel[i][j] for j in indices] for i in indices]
            require(determinant(minor) > 0, "Countermodel low principal minor")
            positive_minors += 1
    det4 = determinant(kernel)
    require(det4 < 0, "Countermodel fourth determinant")
    require(m/b**2 < 2/h0, "Countermodel complete off-line budget")
    require(1+2*m < h0 and h0 > 3, "Countermodel all-height count input")
    moments = [2*e+4*m, 2*e*r+4*m*c,
               2*e*r*r+4*m*(c*c-h),
               2*e*r**3+4*m*(c**3-3*c*h)]
    d0 = moments[0]*moments[2]-moments[1]**2
    d1 = moments[1]*moments[3]-moments[2]**2
    require(d0 == Q(4518253421430481, 2), "Countermodel D0")
    require(d1 == Q(-3346984876045740972698225, 16), "Countermodel D1")
    return {"status": "EXACT_SYNTHETIC_NEGATIVE_4_BY_4",
            "parameters": {"r": str(r), "a": str(a), "b": str(b), "m": str(m)},
            "nodes": list(map(str, nodes)),
            "positive_principal_minors_of_size_at_most_three": positive_minors,
            "fourth_determinant": rational_receipt(det4),
            "D0": str(d0), "D1": str(d1),
            "scope": "Finite polynomial model; no actual xi violation"}


def check_simple_cofinal_countermodel() -> dict:
    m, r, a = 256, Q(200), Q(3,8)
    shifts = [Q(j,2**20) for j in range(1,m+1)]
    mean = sum(shifts, Q(0)) / m
    variance = sum(((d-mean)**2 for d in shifts), Q(0)) / m
    require(variance == Q(m*m-1,12*2**40), "Simple-spectrum shift variance")
    coefficient = 8*m*(r-8*m*(a*a-variance))
    require(coefficient < 0, "Simple-spectrum cofinal leading coefficient")
    base = Q(3*10**12+1)
    bs = [base+d for d in shifts]
    moments = [Q(2+4*m),
               2*r+4*sum((b*b-a*a for b in bs), Q(0)),
               2*r*r+4*sum((b**4-6*a*a*b*b+a**4 for b in bs), Q(0)),
               2*r**3+4*sum((b**6-15*a*a*b**4+15*a**4*b*b-a**6 for b in bs), Q(0))]
    d0 = moments[0]*moments[2]-moments[1]**2
    d1 = moments[1]*moments[3]-moments[2]**2
    require(d0 > 0 and d1 < 0, "Simple-spectrum exact cofinal moment signs")
    require(Q(m)/base**2 < Q(2)/(3*10**12), "Simple-spectrum off-line budget")
    return {"status": "PASS_EXACT_SIMPLE_SPECTRUM_COUNTERMODEL",
            "quartet_count": m, "all_multiplicities": 1,
            "first_ordinate_base": str(base), "shift_step": "1/1048576",
            "variance": str(variance), "B6_coefficient": str(coefficient),
            "D0_at_base": rational_receipt(d0),
            "D1_at_base": rational_receipt(d1),
            "scope": "Cofinal polynomial source; no actual xi violation"}


def replay_anchors(path: Path, producer: Path, precision: int) -> tuple[list, dict]:
    stored = json.loads(path.read_text())
    spec = importlib.util.spec_from_file_location("wave_hardy_z_producer", producer)
    require(spec is not None and spec.loader is not None, "Anchor producer unavailable")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    replayed = module.certificate(precision)
    pairs = lambda result: [[str(Q(a)), str(Q(b))]
                            for a,b in result["critical_ordinate_intervals"]]
    require(pairs(stored) == pairs(replayed), "Anchor interval source mismatch")
    signs = lambda result: {str(Q(row["t"])): row["sign"]
                            for row in result["endpoints"]}
    require(signs(stored) == signs(replayed), "Anchor endpoint sign mismatch")
    anchors = [(Q(a), Q(b)) for a,b in replayed["critical_ordinate_intervals"]]
    receipt = {"status": "DIRECTED_LOW_ANCHORS_REGENERATED",
               "precision_bits": precision,
               "anchor_count": len(anchors),
               "certificate_sha256": digest_bytes(path.read_bytes()),
               "producer_sha256": digest_bytes(producer.read_bytes()),
               "scope": "Low critical pairs only; high-height theorem imported"}
    if "xi_half" in replayed:
        receipt["xi_one_half_lower_bound"] = replayed["xi_half"]["proved_strict_lower_bound"]
    elif "xi_one_half_lower_bound" in replayed:
        receipt["xi_one_half_lower_bound"] = replayed["xi_one_half_lower_bound"]
    return anchors, receipt


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--precision", type=int, default=128)
    args = parser.parse_args()
    anchors, primitive = replay_anchors(CERTIFICATE, ANCHOR_PRODUCER, args.precision)
    count_coefficient = Q(9,20480)+Q(4105,4096)*Q(49,40)
    require(count_coefficient == Q(201217,163840) and count_coefficient < Q(4,3),
            "Native Jensen all-height count numerical inequality")
    for width, orders in [(Q(1,2),45*10**11),(Q(3,8),6*10**12)]:
        require(2*orders*width/Q(3*10**12) == Q(3,2),
                "Finite derivative-sign elementary threshold")
    configurations = [(4,100,20), (8,100,20), (12,40,30),
                      (18,10,35), (24,5,40), (32,1,50)]
    bounds = []
    for n, x, scale in configurations:
        for width in [Q(3,8), Q(1,2)]:
            bound = frame_bound(anchors, n, Q(x), Q(scale), Q(3*10**12), width)
            require(bound["strict_sufficient_inequality"],
                    f"Declared finite theorem failed: n={n}, X={x}, A={width}")
            bounds.append(bound)
    improved = []
    for n, x, scale in [(8,500,20), (12,200,30), (18,100,35),
                        (24,40,40), (32,40,50)]:
        for width in [Q(3,8), Q(1,2)]:
            bound = frame_bound(anchors, n, Q(x), Q(scale), Q(3*10**12), width,
                                negative_features=True)
            require(bound["strict_sufficient_inequality"],
                    f"Improved finite theorem failed: n={n}, X={x}, A={width}")
            improved.append(bound)
    extended_path = HERE / "extended_anchor_certificate.json"
    extended_producer = HERE / "certify_extended_anchors.py"
    extended_anchors, extended_primitive = replay_anchors(extended_path, extended_producer,
                                                         args.precision)
    recompleted = []
    for n, x, scale in [(32,1,50), (64,1,80), (72,1,80),
                        (80,1,80), (88,1,100), (96,1,100)]:
        for width in [Q(3,8), Q(1,2)]:
            bound = frame_bound(extended_anchors, n, Q(x), Q(scale), Q(3*10**12), width,
                                recompleted_features=True)
            require(bound["strict_sufficient_inequality"],
                    f"Recompleted finite theorem failed: n={n}, X={x}, A={width}")
            recompleted.append(bound)
    extended_failed = frame_bound(extended_anchors,96,Q(100),Q(100),Q(3*10**12),Q(3,8),
                                  recompleted_features=True)
    require(not extended_failed["strict_sufficient_inequality"],
            "Extended out-of-range control unexpectedly passed")
    failed_control = frame_bound(anchors, 32, Q(100), Q(50), Q(3*10**12), Q(3,8))
    require(not failed_control["strict_sufficient_inequality"],
            "Deliberately out-of-range control unexpectedly passed")
    result = {"status": "PASS_EXACT_FINITE_CONTROLS",
              "primitive_low_anchor_replay": primitive,
              "native_count_coefficient":str(count_coefficient),
              "scalar_derivative_sign_orders":{"classical_strip":"0 through 4499999999999",
                                                "seven_eighths_strip":"0 through 5999999999999"},
              "anchor_algebra": check_anchor_algebra(),
              "negative_feature_identity": check_negative_feature_identity(),
              "uniform_compact_sufficient_bounds": bounds,
              "negative_feature_compact_bounds": improved,
              "extended_primitive_low_anchor_replay": extended_primitive,
              "recompleted_compact_bounds": recompleted,
              "extended_out_of_range_control": extended_failed,
              "out_of_range_control": failed_control,
              "single_reserve_counterexample": check_single_reserve_counterexample(),
              "simple_cofinal_countermodel": check_simple_cofinal_countermodel(),
              "checker_sha256": digest_bytes(Path(__file__).read_bytes()),
              "proof_scope": "Theorems remain proposed; no global RH or all-order conclusion"}
    rendered = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
