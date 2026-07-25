#!/usr/bin/env python3
"""Exact Gaussian-rational algebra for cross-height matched-pole Pick packets."""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
from typing import Any, Iterable, Sequence


def parse_int(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise ValueError(f"{name} must be an integer, not bool")
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        return int(value, 10)
    raise ValueError(f"{name} must be an integer or decimal string")


def parse_fraction(value: Any, name: str) -> Fraction:
    if not isinstance(value, dict):
        raise ValueError(f"{name} must be an object")
    numerator = parse_int(value.get("numerator"), f"{name}.numerator")
    denominator = parse_int(value.get("denominator"), f"{name}.denominator")
    if denominator <= 0:
        raise ValueError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


def fraction_json(value: Fraction) -> dict[str, str]:
    value = Fraction(value)
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


@dataclass(frozen=True)
class Gaussian:
    real: Fraction
    imag: Fraction = Fraction(0)

    def __post_init__(self) -> None:
        object.__setattr__(self, "real", Fraction(self.real))
        object.__setattr__(self, "imag", Fraction(self.imag))

    @classmethod
    def parse(cls, value: Any, name: str) -> "Gaussian":
        if not isinstance(value, dict):
            raise ValueError(f"{name} must be an object")
        return cls(
            parse_fraction(value.get("real"), f"{name}.real"),
            parse_fraction(value.get("imag"), f"{name}.imag"),
        )

    def to_json(self) -> dict[str, dict[str, str]]:
        return {"real": fraction_json(self.real), "imag": fraction_json(self.imag)}

    def __add__(self, other: Any) -> "Gaussian":
        other = as_gaussian(other)
        return Gaussian(self.real + other.real, self.imag + other.imag)

    __radd__ = __add__

    def __neg__(self) -> "Gaussian":
        return Gaussian(-self.real, -self.imag)

    def __sub__(self, other: Any) -> "Gaussian":
        return self + (-as_gaussian(other))

    def __rsub__(self, other: Any) -> "Gaussian":
        return as_gaussian(other) - self

    def __mul__(self, other: Any) -> "Gaussian":
        other = as_gaussian(other)
        return Gaussian(
            self.real * other.real - self.imag * other.imag,
            self.real * other.imag + self.imag * other.real,
        )

    __rmul__ = __mul__

    def conjugate(self) -> "Gaussian":
        return Gaussian(self.real, -self.imag)

    def norm_squared(self) -> Fraction:
        return self.real * self.real + self.imag * self.imag

    def reciprocal(self) -> "Gaussian":
        denominator = self.norm_squared()
        if denominator == 0:
            raise ZeroDivisionError("zero Gaussian rational")
        return Gaussian(self.real / denominator, -self.imag / denominator)

    def __truediv__(self, other: Any) -> "Gaussian":
        return self * as_gaussian(other).reciprocal()

    def __rtruediv__(self, other: Any) -> "Gaussian":
        return as_gaussian(other) / self

    def __pow__(self, exponent: int) -> "Gaussian":
        if not isinstance(exponent, int):
            raise TypeError("Gaussian power must be an integer")
        if exponent < 0:
            return self.reciprocal() ** (-exponent)
        result = Gaussian(Fraction(1))
        base = self
        power = exponent
        while power:
            if power & 1:
                result *= base
            base *= base
            power >>= 1
        return result


def as_gaussian(value: Any) -> Gaussian:
    return value if isinstance(value, Gaussian) else Gaussian(Fraction(value))


def barycentric_weights(nodes: Sequence[Gaussian]) -> list[Gaussian]:
    if len(nodes) < 2 or len(set(nodes)) != len(nodes):
        raise ValueError("at least two distinct Gaussian nodes are required")
    result: list[Gaussian] = []
    for index, node in enumerate(nodes):
        product = Gaussian(Fraction(1))
        for other_index, other in enumerate(nodes):
            if other_index != index:
                product *= node - other
        result.append(1 / product)
    return result


def matched_pole_vector(nodes: Sequence[Gaussian], model_d: Fraction) -> list[Gaussian]:
    """Return c with conjugate(c) satisfying alpha overlap 0 and beta overlap -1."""
    d = Fraction(model_d)
    if d <= 0:
        raise ValueError("model_d must be positive")
    if any(node * node == d for node in nodes):
        raise ValueError("a node square meets the modeled pole")
    weights = barycentric_weights(nodes)
    alpha = [node / (node * node - d) for node in nodes]
    s0 = sum((weight * value for weight, value in zip(weights, alpha)), Gaussian(0))
    s1 = sum(
        (weight * node * value for weight, node, value in zip(weights, nodes, alpha)),
        Gaussian(0),
    )
    product = Gaussian(1)
    for node in nodes:
        product *= node * node - d
    lambdas = [
        product * weight * (s1 - s0 * node)
        for weight, node in zip(weights, nodes)
    ]
    return [value.conjugate() for value in lambdas]


def matched_identities(
    nodes: Sequence[Gaussian], vector: Sequence[Gaussian], model_d: Fraction
) -> dict[str, Any]:
    if len(nodes) != len(vector):
        raise ValueError("node/vector length mismatch")
    d = Fraction(model_d)
    lambdas = [value.conjugate() for value in vector]
    moments = [
        sum(
            (coefficient * (node ** power) for coefficient, node in zip(lambdas, nodes)),
            Gaussian(0),
        )
        for power in range(max(0, len(nodes) - 2))
    ]
    alpha = sum(
        (
            coefficient * node / (node * node - d)
            for coefficient, node in zip(lambdas, nodes)
        ),
        Gaussian(0),
    )
    beta = sum(
        (coefficient / (node * node - d) for coefficient, node in zip(lambdas, nodes)),
        Gaussian(0),
    )
    norm_squared = sum((value.norm_squared() for value in vector), Fraction(0))
    return {
        "moments": moments,
        "alpha": alpha,
        "beta": beta,
        "norm_squared": norm_squared,
        "modeled_pair_value": -2 * d,
    }


def pick_contraction_coefficients(
    x_values: Sequence[Fraction],
    t_values: Sequence[Fraction],
    vector: Sequence[Gaussian],
) -> list[Gaussian]:
    """Return q_j such that v*Kv = Re sum_j q_j F(s_j)."""
    if not (len(x_values) == len(t_values) == len(vector)) or not vector:
        raise ValueError("point/vector arrays must have the same positive length")
    coefficients: list[Gaussian] = []
    for j, (xj, tj) in enumerate(zip(x_values, t_values)):
        inner = Gaussian(0)
        for k, (xk, tk) in enumerate(zip(x_values, t_values)):
            denominator = Gaussian(Fraction(xj) + Fraction(xk), Fraction(tj) - Fraction(tk))
            inner += vector[k] / denominator
        coefficients.append(2 * vector[j].conjugate() * inner)
    return coefficients


def vector_norm_squared(vector: Iterable[Gaussian]) -> Fraction:
    return sum((value.norm_squared() for value in vector), Fraction(0))


def coefficient_l1(coefficients: Iterable[Gaussian]) -> Fraction:
    return sum((abs(value.real) + abs(value.imag) for value in coefficients), Fraction(0))
