#!/usr/bin/env python3
"""Exact finite algebra checks for pass2_signed_auxiliary.md.

The prime labels and Gauss values are formal algebraic data satisfying the
declared CRT/reciprocity interfaces. This is not evaluation of Eisenstein
Gauss sums and does not check Poisson summation or an analytic estimate.
"""

from fractions import Fraction
from itertools import product
import json


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


# Z[zeta_12] in basis 1,x,x^2,x^3, with x^4-x^2+1=0.
def mul_x(a):
    a0, a1, a2, a3 = a
    return (-a3, a0, a1+a3, a2)


ROOTS = [(1, 0, 0, 0)]
for _ in range(12):
    ROOTS.append(mul_x(ROOTS[-1]))
require(ROOTS[12] == ROOTS[0], "twelfth-root reduction")
ROOTS = ROOTS[:12]
ZERO = (0, 0, 0, 0)


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


def signed_root(sign, exponent):
    return tuple(sign*x for x in ROOTS[exponent % 12])


def mu(mask):
    return -1 if mask.bit_count() % 2 else 1


def bits(mask, n=3):
    return [i for i in range(n) if mask & (1 << i)]


def norm(mask, prime_norms=(7, 13, 19)):
    out = 1
    for i in bits(mask):
        out *= prime_norms[i]
    return out


def subsets(mask):
    s = mask
    while True:
        yield s
        if not s:
            return
        s = (s-1) & mask


def ray_bilinear(mask1, mask2, matrix):
    return sum(matrix[i][j] for i in bits(mask1) for j in bits(mask2)) % 2


def ray_g_exp(mask, matrix):
    ii = bits(mask)
    return (3*sum(matrix[i][i] for i in ii)
            + 6*sum(matrix[i][j] for i in ii for j in ii if i < j)) % 12


def gauss_data(matrix, cross):
    gamma2_prime = (1, 4, 7)
    xi_prime = (0, 2, 4)

    def alpha(mask):
        return sum(6+3*gamma2_prime[i] for i in bits(mask)) % 12

    def gamma2(mask):
        ii = bits(mask)
        return (sum(gamma2_prime[i] for i in ii)
                + 8*sum(cross[j][i] for i in ii for j in ii if i < j)) % 12

    def gamma1(mask):
        ii = bits(mask)
        return (sum(ray_g_exp(1 << i, matrix)+2*gamma2_prime[i] for i in ii)
                + 2*sum(cross[i][j]+cross[j][i]
                        for i in ii for j in ii if i < j)) % 12

    def gamma_minus1(mask):
        return (6*sum(matrix[i][i] for i in bits(mask))-gamma1(mask)) % 12

    def xi(mask):
        return sum(xi_prime[i] for i in bits(mask)) % 12

    def a(mask):
        return (-alpha(mask)+gamma2(mask)+xi(mask)) % 12

    return a, gamma1, gamma_minus1, xi


def check_gauss_scalar():
    count = 0
    wrong_conjugation = 0
    for bb in product(range(2), repeat=6):
        matrix = [[0]*3 for _ in range(3)]
        matrix[0][0], matrix[1][1], matrix[2][2] = bb[:3]
        for value, (i, j) in zip(bb[3:], [(0, 1), (0, 2), (1, 2)]):
            matrix[i][j] = matrix[j][i] = value
        for cc in product(range(3), repeat=3):
            cross = [[0]*3 for _ in range(3)]
            for value, (i, j) in zip(cc, [(0, 1), (0, 2), (1, 2)]):
                cross[i][j] = value
                cross[j][i] = (value+3*matrix[i][j]) % 6
            a, gamma1, gamma_minus1, xi = gauss_data(matrix, cross)
            for labels in product(range(3), repeat=3):
                z1 = sum(1 << i for i, x in enumerate(labels) if x == 1)
                z2 = sum(1 << i for i, x in enumerate(labels) if x == 2)
                if z1 == z2 == 0:
                    continue
                gamma_psi = (gamma1(z1)+gamma_minus1(z2)
                             + 6*ray_bilinear(z1, z2, matrix)) % 12
                lhs = (a(z1)-a(z2)+gamma_psi) % 12
                rhs = (6*(z1.bit_count()+z2.bit_count())
                       + xi(z1)-xi(z2)+ray_g_exp(z1 ^ z2, matrix)) % 12
                require(lhs == rhs, "native scalar identity")
                count += 1
                wrong = (a(z1)+a(z2)+gamma_psi) % 12
                wrong_conjugation += wrong != rhs
    require(wrong_conjugation > 0, "conjugation negative control")
    return {"formal_gauss_scalar_cases": count,
            "wrong_conjugation_rejected_cases": wrong_conjugation}


def check_auxiliary_reunion():
    matrix = [[1, 1, 0], [1, 0, 1], [0, 1, 1]]
    cross = [[0, 1, 2], [4, 0, 0], [2, 3, 0]]
    unit_weights = (3, 4, 1)  # parity agrees with diagonal reciprocity.
    a, _, _, _ = gauss_data(matrix, cross)

    def char_exp(mask, row, unit, extra_mask=0, extra_power=0):
        exponents = [row[i]+extra_power*bool(extra_mask & (1 << i)) for i in range(3)]
        if any(exponents[i] for i in bits(mask)):
            return None
        return (2*sum(unit*unit_weights[i]
                      + sum(cross[i][j]*exponents[j] for j in range(3))
                      for i in bits(mask))) % 12

    cases = 0
    strict_cases = 0
    norm_cases = 0
    negative = {"delete_common_row_zero": 0,
                "replace_mu_by_absolute": 0,
                "impose_coprime_h_w": 0,
                "use_h_w4_instead_of_h_w5": 0}
    first_witness = {}
    prime_norms = (7, 13, 19)
    for assignment in product(range(5), repeat=3):
        # 0 unused, 1 b, 2 w, 3 z1, 4 z2.
        masks = {j: sum(1 << i for i, x in enumerate(assignment) if x == j)
                 for j in range(1, 5)}
        b, w, z1, z2 = [masks[j] for j in range(1, 5)]
        if z1 == z2 == 0:
            continue
        for row in product(range(3), repeat=3):
            divisible = all(row[i] >= 1 for i in bits(w))
            for unit in range(6):
                lhs = ZERO
                unsigned = ZERO
                no_common_zero = ZERO
                for f in subsets(w):
                    d = w ^ f
                    m1, m2 = d | z1, d | z2
                    require((m1 != m2) == (z1 != z2), "strict pair reconstruction")
                    strict_cases += 1
                    x = char_exp(m1, row, unit, f, 4)
                    y = char_exp(m2, row, unit, f, 4)
                    if x is not None and y is not None:
                        exp = a(m1)-a(m2)+x-y
                        lhs = add(lhs, signed_root(mu(f), exp))
                        unsigned = add(unsigned, signed_root(1, exp))
                    xx = char_exp(z1, row, unit, w, 4)
                    yy = char_exp(z2, row, unit, w, 4)
                    if xx is not None and yy is not None:
                        no_common_zero = add(no_common_zero,
                                             signed_root(mu(f), a(z1)-a(z2)+xx-yy))
                rhs = ZERO
                wrong_coprime = ZERO
                wrong_power = ZERO
                if divisible:
                    h = tuple(row[i]-bool(w & (1 << i)) for i in range(3))
                    x = char_exp(z1, h, unit, w, 5)
                    y = char_exp(z2, h, unit, w, 5)
                    if x is not None and y is not None:
                        rhs = signed_root(mu(w), a(z1)-a(z2)+x-y)
                        if all(h[i] == 0 for i in bits(w)):
                            wrong_coprime = rhs
                    x4 = char_exp(z1, h, unit, w, 4)
                    y4 = char_exp(z2, h, unit, w, 4)
                    if x4 is not None and y4 is not None:
                        wrong_power = signed_root(mu(w), a(z1)-a(z2)+x4-y4)
                    nk = 1
                    nh = 1
                    for i, q in enumerate(prime_norms):
                        nk *= q**row[i]
                        nh *= q**h[i]
                    for height in (Fraction(1), Fraction(3, 2), Fraction(17)):
                        old_arg = height*nk/Fraction(norm(w)**2*norm(z1)*norm(z2))
                        new_arg = height*nh/Fraction(norm(w)*norm(z1)*norm(z2))
                        require(old_arg == new_arg, "reunited norm kernel")
                        norm_cases += 1
                require(lhs == rhs, "full signed auxiliary reunion")
                cases += 1
                for key, wrong in [("delete_common_row_zero", no_common_zero),
                                   ("replace_mu_by_absolute", unsigned),
                                   ("impose_coprime_h_w", wrong_coprime),
                                   ("use_h_w4_instead_of_h_w5", wrong_power)]:
                    if wrong != rhs:
                        negative[key] += 1
                        first_witness.setdefault(key, {"b": b, "w": w, "z1": z1, "z2": z2,
                                                       "row_valuations": row, "unit": unit,
                                                       "correct": rhs, "wrong": wrong})
    for key, n in negative.items():
        require(n > 0, "negative control failed: "+key)
    return {"reunion_cases": cases, "strict_condition_reconstructions": strict_cases,
            "rational_kernel_cases": norm_cases,
            "negative_control_rejections": negative,
            "first_negative_witnesses": first_witness}


def check_exponents():
    count = 0
    for beta in (Fraction(2, 3), Fraction(3, 4), Fraction(7, 8),
                 Fraction(139999, 160000), Fraction(1)):
        require(2*beta > 1, "coprimality convergence")
        for k in (1, 2, 3, 7):
            cutoff = k*(2*beta-1)/(2*beta)
            require(k*(2*beta-1)-2*beta*cutoff == 0, "sharp tail boundary")
            count += 1
    require(2*(2*Fraction(7, 8)-1)/(2*Fraction(7, 8)) == Fraction(6, 7), "7/8 cutoff")
    require(2*(2*Fraction(139999, 160000)-1)/(2*Fraction(139999, 160000))
            == Fraction(119998, 139999), "exact imported cutoff")
    return {"rational_tail_boundary_cases": count}


def main():
    report = {"status": "PASS",
              "scope": "Exact finite formal cyclotomic algebra and rational bookkeeping; no analytic certification.",
              "coefficient_contract": "Prime labels and Gauss monomials satisfy declared CRT and finite-ray interfaces; not primitive Eisenstein Gauss-sum evaluations."}
    report.update(check_auxiliary_reunion())
    report.update(check_gauss_scalar())
    report.update(check_exponents())
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
