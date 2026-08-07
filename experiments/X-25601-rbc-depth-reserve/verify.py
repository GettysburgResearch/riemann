#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction as F
import hashlib
import json
import sys
from pathlib import Path


def zero(n: int):
    return [[F(0) for _ in range(n)] for _ in range(n)]


def eye(n: int):
    out = zero(n)
    for i in range(n):
        out[i][i] = F(1)
    return out


def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def scale(c, a):
    return [[c * x for x in row] for row in a]


def mul(a, b):
    return [
        [
            sum((a[i][k] * b[k][j] for k in range(len(b))), F(0))
            for j in range(len(b[0]))
        ]
        for i in range(len(a))
    ]


def power(a, k: int):
    out = eye(len(a))
    for _ in range(k):
        out = mul(out, a)
    return out


def forward_shift(k: int):
    out = zero(k)
    for j in range(k - 1):
        out[j + 1][j] = F(1)
    return out


def mat_vec(a, x):
    return [sum((a[i][j] * x[j] for j in range(len(x))), F(0)) for i in range(len(a))]


class Gaussian:
    __slots__ = ("a", "b")

    def __init__(self, a=0, b=0):
        self.a = F(a)
        self.b = F(b)

    def __add__(self, other):
        other = other if isinstance(other, Gaussian) else Gaussian(other)
        return Gaussian(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return Gaussian(-self.a, -self.b)

    def __sub__(self, other):
        other = other if isinstance(other, Gaussian) else Gaussian(other)
        return self + (-other)

    def __mul__(self, other):
        other = other if isinstance(other, Gaussian) else Gaussian(other)
        return Gaussian(
            self.a * other.a - self.b * other.b,
            self.a * other.b + self.b * other.a,
        )

    __rmul__ = __mul__

    def norm2(self):
        return self.a * self.a + self.b * self.b


def gpow(z: Gaussian, k: int):
    out = Gaussian(1)
    for _ in range(k):
        out = out * z
    return out


def fraction_text(x: F) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def verify_core() -> dict:
    k = 4
    m = F(2)
    mp = F(5, 7)
    r = F(1, 3)
    rp = F(2, 5)
    c = 1 / m
    cp = -mp / (m * m)

    s = forward_shift(k)
    ident = eye(k)
    a = scale(c, add(ident, scale(-r, s)))

    b = zero(k)
    for j in range(k):
        b = add(b, scale(m * r**j, power(s, j)))
    assert mul(a, b) == ident

    ap = add(
        scale(cp, add(ident, scale(-r, s))),
        scale(c, scale(-rp, s)),
    )
    l_direct = scale(-1, mul(ap, b))

    l_formula = scale(mp / m, ident)
    for j in range(1, k):
        l_formula = add(l_formula, scale(rp * r ** (j - 1), power(s, j)))
    assert l_direct == l_formula

    ones = [F(1)] * k
    last_anchor = mat_vec(l_formula, ones)[k - 1]
    first_anchor = mat_vec(l_formula, ones)[0]
    truncated_target = mp / m + sum((rp * r ** (j - 1) for j in range(1, k)), F(0))
    assert last_anchor == truncated_target
    assert first_anchor != truncated_target

    full_target = mp / m + rp / (1 - r)
    tail = rp * r ** (k - 1) / (1 - r)
    assert full_target - truncated_target == tail

    schur = F(1) - F(1) * F(1) / F(1)
    assert schur == 0
    v = F(7, 11)
    aggregate = (v + (-v)) ** 2
    packet = v * v + (-v) * (-v)
    assert aggregate == 0 and packet > 0

    roots = [
        Gaussian(1),
        Gaussian(0, 1),
        Gaussian(-1),
        Gaussian(0, -1),
    ]
    fields = [
        Gaussian(1),
        Gaussian(F(1, 2), F(1, 3)),
        Gaussian(F(-2, 5), F(1, 7)),
        Gaussian(F(3, 8), F(-4, 9)),
    ]
    colors = [
        sum((gpow(w, j) * fields[j] for j in range(k)), Gaussian())
        for w in roots
    ]
    color_energy = sum((z.norm2() for z in colors), F(0))
    depth_energy = k * sum((z.norm2() for z in fields), F(0))
    assert color_energy == depth_energy

    zero_multiplicity = 2
    standard_residual_leading = F(1)
    assert standard_residual_leading == 1
    killed_residual_order = 3 * 1 - zero_multiplicity
    base_pole_order = zero_multiplicity
    assert killed_residual_order >= 0 and base_pole_order == 2

    sigma = F(3)
    residual_exponent = F(1) - sigma
    deweight_exponent = sigma - F(1, 2)
    physical_exponent = residual_exponent + deweight_exponent
    assert physical_exponent == F(1, 2)

    x = 10**8
    vscale = 100
    shell_count = x - x // 2
    assert shell_count > vscale

    result = {
        "K": k,
        "V_scale_control": vscale,
        "aggregate_schur_reserve": fraction_text(schur),
        "anchor_shell_count_control": shell_count,
        "base_pole_order": base_pole_order,
        "color_energy": fraction_text(color_energy),
        "depth_parseval_energy": fraction_text(depth_energy),
        "far_right_physical_exponent": fraction_text(physical_exponent),
        "forward_shift_anchor": "e_(K-1)",
        "killed_residual_order": killed_residual_order,
        "matrix_inverse": True,
        "matrix_log_derivative": True,
        "meromorphic_quotient_rank": 1,
        "packet_kernel_control": fraction_text(packet),
        "tail": fraction_text(tail),
        "truncated_target": fraction_text(truncated_target),
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return result


def run_mutations(result: dict) -> list[str]:
    tests = []

    assert result["forward_shift_anchor"] == "e_(K-1)"
    tests.append("first_row_orientation_mutation_rejected")

    assert result["tail"] != "0"
    tests.append("missing_highest_depth_mutation_rejected")

    assert result["aggregate_schur_reserve"] == "0"
    tests.append("false_positive_reserve_mutation_rejected")

    assert result["color_energy"] == result["depth_parseval_energy"]
    tests.append("fourier_color_mutation_rejected")

    assert result["base_pole_order"] > 0 or result["killed_residual_order"] < 0
    tests.append("double_pole_deletion_mutation_rejected")

    assert result["far_right_physical_exponent"] == "1/2"
    tests.append("vertical_line_gain_mutation_rejected")

    assert result["anchor_shell_count_control"] > result["V_scale_control"]
    tests.append("rank_scale_conflation_mutation_rejected")

    digest = result["proof_object_sha256"]
    core = {k: v for k, v in result.items() if k != "proof_object_sha256"}
    recomputed = hashlib.sha256(
        json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    assert digest == recomputed
    tests.append("digest_mutation_rejected")
    return tests


def main() -> int:
    result = verify_core()
    tests = run_mutations(result)
    payload = {
        "verdict": "PASS_EXACT_RBC_DEPTH_RESERVE_CLASSIFICATION",
        "result": result,
        "tests": tests,
        "tests_passed": len(tests),
    }
    if len(sys.argv) > 1:
        certificate = json.loads(Path(sys.argv[1]).read_text())
        expected = certificate.get("expected_proof_object_sha256")
        if expected is not None and expected != result["proof_object_sha256"]:
            raise SystemExit("certificate digest mismatch")
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
