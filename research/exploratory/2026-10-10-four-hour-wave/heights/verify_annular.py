#!/usr/bin/env python3
"""Exact finite checks for ANNULAR_GLOBAL_PICK.md; no external theorem replay."""
from __future__ import annotations
import argparse
import hashlib
import json
from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import combinations
from math import factorial
from pathlib import Path

HERE = Path(__file__).resolve().parent
H = 3 * 10**12
BANDS = [
    (Q(1035,1024), Q(1043,1024)),
    (Q(81,64), Q(163,128)),
    (Q(1513,1024), Q(1521,1024)),
    (Q(851,512), Q(855,512)),
    (Q(117,64), Q(235,128)),
    (Q(2029,1024), Q(2037,1024)),
]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def prod(values):
    result = Q(1)
    for value in values:
        result *= value
    return result


def determinant(matrix):
    matrix = [row[:] for row in matrix]
    value = Q(1)
    for k in range(len(matrix)):
        row = next((j for j in range(k, len(matrix)) if matrix[j][k]), None)
        if row is None:
            return Q(0)
        if row != k:
            matrix[row], matrix[k] = matrix[k], matrix[row]
            value = -value
        pivot = matrix[k][k]
        value *= pivot
        for j in range(k + 1, len(matrix)):
            ratio = matrix[j][k] / pivot
            for l in range(k + 1, len(matrix)):
                matrix[j][l] -= ratio * matrix[k][l]
    return value


def matmul(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), Q(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a):
    return [list(row) for row in zip(*a)]


@dataclass(frozen=True)
class CQ:
    re: Q = Q(0)
    im: Q = Q(0)

    @staticmethod
    def coerce(value):
        return value if isinstance(value, CQ) else CQ(Q(value))

    def __add__(self, other):
        other = self.coerce(other)
        return CQ(self.re + other.re, self.im + other.im)

    __radd__ = __add__

    def __neg__(self):
        return CQ(-self.re, -self.im)

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __mul__(self, other):
        other = self.coerce(other)
        return CQ(self.re*other.re-self.im*other.im,
                  self.re*other.im+self.im*other.re)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self.coerce(other)
        norm = other.re*other.re+other.im*other.im
        require(bool(norm), "zero complex denominator")
        return CQ((self.re*other.re+self.im*other.im)/norm,
                  (self.im*other.re-self.re*other.im)/norm)

    def __pow__(self, power):
        require(power >= 0, "nonnegative power required")
        result = CQ(Q(1))
        for _ in range(power):
            result *= self
        return result

    def real(self):
        require(self.im == 0, "conjugate sum was not real")
        return self.re


def cprod(values):
    result = CQ(Q(1))
    for value in values:
        result *= value
    return result


def linear_product(roots):
    coefficients = [Q(1)]
    for root in roots:
        updated = [Q(0)] * (len(coefficients)+1)
        for k, value in enumerate(coefficients):
            updated[k] += root * value
            updated[k+1] += value
        coefficients = updated
    return coefficients


def moment_congruence(nodes, source):
    n = len(nodes)
    values = [sum((CQ(w)/(s+x*x) for w,s in source), CQ()).real()
              for x in nodes]
    kernel = [[(x*values[i]+y*values[j])/(x+y)
               for j,y in enumerate(nodes)] for i,x in enumerate(nodes)]
    moments = [sum((w*s**j/cprod(s+x*x for x in nodes)
                    for w,s in source), CQ()).real() for j in range(n)]
    a, b = (n+1)//2, n//2
    block = [[Q(0)]*n for _ in nodes]
    for i in range(a):
        for j in range(a):
            block[i][j] = moments[i+j]
    for i in range(b):
        for j in range(b):
            block[a+i][a+j] = moments[i+j+1]
    transform = []
    for i in range(n):
        coefficients = linear_product(nodes[:i]+nodes[i+1:])
        transform.append([coefficients[2*k]*(-1)**k for k in range(a)]
                         + [coefficients[2*k+1]*(-1)**k for k in range(b)])
    target = matmul(matmul(transform, block), transpose(transform))
    require(kernel == target, f"full moment congruence at n={n}")
    delta = prod(y-x for x,y in combinations(nodes, 2))
    require(determinant(transform)**2 == delta**2,
            f"transformation Vandermonde at n={n}")
    if n <= 8:
        require(determinant(kernel) == delta**2*determinant(block),
                f"moment determinant product at n={n}")
    return {"packet_size": n, "source_locations": len(source),
            "entry_checks": n*n, "transform_determinant_checked": True,
            "full_determinant_checked": n <= 8}


def pfaffian(matrix):
    n = len(matrix)
    if n == 0:
        return Q(1)
    require(n % 2 == 0, "even skew order required")
    result = Q(0)
    for j in range(1,n):
        remainder = [i for i in range(n) if i not in (0,j)]
        minor = [[matrix[i][k] for k in remainder] for i in remainder]
        result += (-1)**(j+1)*matrix[0][j]*pfaffian(minor)
    return result


def check_pfaffians():
    receipts = []
    for n in (2,4,6,8):
        nodes = [Q(2*i+1, i+1) for i in range(n)]
        values = [Q((i+2)**2, 3*i+1) for i in range(n)]
        kernel = [[(x*values[i]+y*values[j])/(x+y)
                   for j,y in enumerate(nodes)] for i,x in enumerate(nodes)]
        skew_a = [[(values[i]-values[j])/(x+y)
                   for j,y in enumerate(nodes)] for i,x in enumerate(nodes)]
        skew_b = [[(x*x*values[i]-y*y*values[j])/(x+y)
                   for j,y in enumerate(nodes)] for i,x in enumerate(nodes)]
        require(determinant(kernel) == (-1)**(n//2)*pfaffian(skew_a)*pfaffian(skew_b),
                f"generic Pfaffian determinant at n={n}")
        receipts.append({"packet_size": n, "generic_values": True})
    return receipts


def check_constants():
    require(all(Q(1)<lo<hi<Q(2) and hi-lo == Q(1,128)
                for lo,hi in BANDS), "six width-1/128 interior bands")
    intervals = [(lo*lo/4-Q(1,2**22), hi*hi/4) for lo,hi in BANDS]
    require(all(intervals[j][1] < intervals[j+1][0] for j in range(5)),
            "projected band separation")
    require(Q(1,4*1024**2)/4 < Q(1,2**22), "projection correction")
    gamma = sum((prod((1+intervals[k][1])**2 for k in range(6) if k != j)
                 /prod((intervals[j][0]-intervals[k][1])**2 if k<j
                       else (intervals[k][0]-intervals[j][1])**2
                       for k in range(6) if k != j) for j in range(6)), Q(0))
    require(Q(611192582) < gamma < Q(611192583), "rational frame bracket")
    require(Q(256,255)**12 < Q(17,16), "normalized phi bound")
    require((1+Q(1,510**2))**6 < Q(17,16), "vertical numerator bound")
    require(Q(256,255)**2 < Q(17,16), "vertical inverse-square bound")
    require(Q(17,16)**3 < Q(5,4), "second derivative constant")
    n = 12
    threshold = 8000*6*10*n*n*gamma*4**n*Q(1024,255)
    ratio = threshold/Q(H*H)
    require(ratio < Q(1,3), "strict global annular sufficient inequality")
    require(H*(Q(25,28672)-Q(1,2000)) > 1, "uniform lower band constant")
    require(Q(112,1000)+Q(278,1000)/8+Q(2510,1000)/28+Q(1,1000)
            < Q(1,4), "source-qualified count error coefficient")
    require(Q(11,4)**28 < H, "log H > 28 using e < 11/4")
    require(sum((Q(7,2)**k/Q(factorial(k)) for k in range(10)),Q(0)) > 28,
            "log 28 < 7/2 by positive exponential partial sum")
    return {"H": H, "packet_size": n,
            "frame_gamma_exact": str(gamma),
            "sufficient_ratio_exact": str(ratio),
            "sufficient_ratio_upper": "1/3",
            "margin_floor": (1/ratio).numerator//(1/ratio).denominator,
            "bands": [[str(lo),str(hi)] for lo,hi in BANDS],
            "projected_intervals": [[str(lo),str(hi)] for lo,hi in intervals],
            "normalization": "u=s/(4L^2), phi=D/prod(rho+s/L^2)",
            "published_inputs_replayed": False}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    source = [(Q(2),CQ(Q(r))) for r in (200,441,626,900,1100,1500)]
    for a,b,w in ((Q(3,8),Q(1025),Q(2)),(Q(1,4),Q(2050),Q(4))):
        c,d = b*b-a*a, 2*a*b
        source.extend([(w,CQ(c,d)),(w,CQ(c,-d))])
    base_nodes = [Q(1,100),Q(1,10),Q(1),Q(2),Q(5),Q(13),
                  Q(100),Q(1000),Q(1001),Q(10**6),Q(10**8),Q(10**12)]
    checks = [moment_congruence(base_nodes[:n],source) for n in range(1,13)]
    output = {"status": "PASS_EXACT_ANNULAR_GLOBAL_PICK_CONTROLS",
              "constants": check_constants(),
              "congruence_checks": checks, "pfaffian_checks": check_pfaffians(),
              "proof_sha256": hashlib.sha256((HERE/"ANNULAR_GLOBAL_PICK.md").read_bytes()).hexdigest(),
              "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "limitations": ["finite controls do not prove the analytic annular theorem",
                              "published S bound and verified height are imported",
                              "RH remains unproved"]}
    content = json.dumps(output,indent=2,sort_keys=True)+"\n"
    if args.output:
        args.output.write_text(content)
    else:
        print(content,end="")

if __name__ == "__main__":
    main()
