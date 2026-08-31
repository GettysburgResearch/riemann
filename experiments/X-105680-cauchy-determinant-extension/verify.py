#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path


@dataclass(frozen=True)
class C:
    re: F = F(0)
    im: F = F(0)

    @staticmethod
    def m(value: object) -> "C":
        return value if isinstance(value, C) else C(F(value), F(0))

    def __add__(self, other: object) -> "C":
        other = C.m(other)
        return C(self.re + other.re, self.im + other.im)

    __radd__ = __add__

    def __neg__(self) -> "C":
        return C(-self.re, -self.im)

    def __sub__(self, other: object) -> "C":
        return self + (-C.m(other))

    def __rsub__(self, other: object) -> "C":
        return C.m(other) - self

    def __mul__(self, other: object) -> "C":
        other = C.m(other)
        return C(
            self.re * other.re - self.im * other.im,
            self.re * other.im + self.im * other.re,
        )

    __rmul__ = __mul__

    def conj(self) -> "C":
        return C(self.re, -self.im)

    def __truediv__(self, other: object) -> "C":
        other = C.m(other)
        denominator = other.re * other.re + other.im * other.im
        return C(
            (self.re * other.re + self.im * other.im) / denominator,
            (self.im * other.re - self.re * other.im) / denominator,
        )

    def __pow__(self, exponent: int) -> "C":
        if exponent < 0:
            return C.m(1) / (self ** (-exponent))
        result = C.m(1)
        base = self
        while exponent:
            if exponent & 1:
                result = result * base
            base = base * base
            exponent //= 2
        return result

    def zero(self) -> bool:
        return self.re == 0 and self.im == 0


def eye(size: int) -> list[list[C]]:
    return [[C.m(i == j) for j in range(size)] for i in range(size)]


def mm(a: list[list[C]], b: list[list[C]]) -> list[list[C]]:
    return [
        [
            sum((a[i][k] * b[k][j] for k in range(len(b))), C())
            for j in range(len(b[0]))
        ]
        for i in range(len(a))
    ]


def mv(a: list[list[C]], vector: list[C]) -> list[C]:
    return [
        sum((a[i][j] * vector[j] for j in range(len(vector))), C())
        for i in range(len(a))
    ]


def inverse(a: list[list[C]]) -> list[list[C]]:
    size = len(a)
    augmented = [a[i][:] + eye(size)[i] for i in range(size)]
    for column in range(size):
        pivot = next(
            row for row in range(column, size) if not augmented[row][column].zero()
        )
        augmented[column], augmented[pivot] = (
            augmented[pivot],
            augmented[column],
        )
        value = augmented[column][column]
        augmented[column] = [entry / value for entry in augmented[column]]
        for row in range(size):
            if row == column:
                continue
            factor = augmented[row][column]
            if not factor.zero():
                augmented[row] = [
                    augmented[row][j] - factor * augmented[column][j]
                    for j in range(2 * size)
                ]
    return [row[size:] for row in augmented]


def trace(a: list[list[C]]) -> C:
    return sum((a[i][i] for i in range(len(a))), C())


def determinant(a: list[list[C]]) -> C:
    size = len(a)
    work = [row[:] for row in a]
    result = C.m(1)
    sign = 1
    for column in range(size):
        pivot = next(
            row for row in range(column, size) if not work[row][column].zero()
        )
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            sign = -sign
        value = work[column][column]
        result = result * value
        for row in range(column + 1, size):
            factor = work[row][column] / value
            for j in range(column + 1, size):
                work[row][j] = work[row][j] - factor * work[column][j]
    return C.m(sign) * result


def dot(vector: list[C], matrix: list[list[C]], other: list[C]) -> C:
    image = mv(matrix, other)
    return sum(
        (vector[i].conj() * image[i] for i in range(len(vector))), C()
    )


def gram(nodes: list[C], shift: F) -> list[list[C]]:
    return [
        [
            C.m(1) / (nodes[i].conj() + nodes[j] + shift)
            for j in range(len(nodes))
        ]
        for i in range(len(nodes))
    ]


def leading(matrix: list[list[C]], size: int) -> list[list[C]]:
    return [row[:size] for row in matrix[:size]]


def overlap_current(nodes: list[C], height: F) -> tuple[C, C]:
    g0, g1, g2, g4 = (
        gram(nodes, shift) for shift in (F(0), height, 2 * height, 4 * height)
    )
    overlap = trace(mm(mm(mm(inverse(g0), g2), inverse(g4)), g2))
    current = trace(mm(inverse(g0), g1))
    return overlap, current


def extension(nodes: list[C], height: F) -> tuple[C, C]:
    rank = len(nodes)
    old_rank = rank - 1
    g0, g1, g2, g4 = (
        gram(nodes, shift) for shift in (F(0), height, 2 * height, 4 * height)
    )
    if old_rank:
        a0 = leading(g0, old_rank)
        b0 = [g0[i][old_rank] for i in range(old_rank)]
        a4 = leading(g4, old_rank)
        b4 = [g4[i][old_rank] for i in range(old_rank)]
        u = [-entry for entry in mv(inverse(a0), b0)] + [C.m(1)]
        v = [-entry for entry in mv(inverse(a4), b4)] + [C.m(1)]
    else:
        u = v = [C.m(1)]

    norm_u = dot(u, g0, u)
    norm_v = dot(v, g4, v)

    if old_rank:
        cross_u = mv([row[:] for row in g2[:old_rank]], u)
        old_deep = dot(cross_u, inverse(leading(g4, old_rank)), cross_u) / norm_u
    else:
        old_deep = C()

    cross_v = mv(g2, v)
    new_shallow = dot(cross_v, inverse(g0), cross_v) / norm_v
    current_increment = dot(u, g1, u) / norm_u

    overlap, current = overlap_current(nodes, height)
    if old_rank:
        old_overlap, old_current = overlap_current(nodes[:old_rank], height)
    else:
        old_overlap = old_current = C()

    direct_increment = (overlap - old_overlap) - (current - old_current)
    projection_increment = old_deep + new_shallow - current_increment
    return direct_increment, projection_increment


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    checks = 0
    height = F(1)
    nodes = [C(F(1)), C(F(2), F(1)), C(F(3), F(-2))]
    g0, g1, g2, g4 = (
        gram(nodes, shift) for shift in (F(0), height, 2 * height, 4 * height)
    )
    ratio = determinant(g2) ** 2 / (determinant(g1) * determinant(g4))

    product = C.m(1)
    for node in nodes:
        x = 2 * node.re
        product *= C.m(
            (x + height)
            * (x + 4 * height)
            / (x + 2 * height) ** 2
        )
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            z = nodes[i].conj() + nodes[j]
            factor = (z + height) * (z + 4 * height) / (z + 2 * height) ** 2
            product *= factor.conj() * factor

    assert ratio == product
    assert ratio.im == 0 and ratio.re > 1
    checks += 3

    for x in range(1, 9):
        for y in range(0, 7):
            for h in range(1, 5):
                left = ((x + h) ** 2 + y * y) * ((x + 4 * h) ** 2 + y * y)
                left -= ((x + 2 * h) ** 2 + y * y) ** 2
                right = h * (
                    8 * h * h * x
                    + 9 * h * x * x
                    + 9 * h * y * y
                    + 2 * x**3
                    + 2 * x * y * y
                )
                assert left == right and right > 0
                checks += 1

    packets = [
        [C(F(1))],
        [C(F(1)), C(F(2), F(1))],
        [C(F(1)), C(F(2), F(1)), C(F(3), F(-2))],
        [C(F(1)), C(F(2), F(1)), C(F(3), F(-2)), C(F(4), F(3))],
    ]
    for packet in packets:
        direct, projection = extension(packet, F(1))
        assert direct == projection and direct.im == 0
        checks += 1

    result = {
        "claim": "T-105680",
        "verdict": "PASS_T105680_CAUCHY_DETERMINANT_AND_EXTENSION",
        "checks": checks,
        "determinant_strength_cti_exact": True,
        "rank_extension_identity_exact": True,
        "return_compensation_proved": False,
        "global_cti_proved": False,
        "rh_established": False,
        "scope": "exact rational Cauchy determinants, pair factors, and nested projection increments",
    }
    result["proof_object"] = hashlib.sha256(
        json.dumps(result, sort_keys=True).encode()
    ).hexdigest()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    print(result["verdict"])
    print(f"checks={checks}")
    print(result["proof_object"])


if __name__ == "__main__":
    main()
