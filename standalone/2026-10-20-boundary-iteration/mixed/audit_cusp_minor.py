"""Independent exact audit of the three cusp extraction minor.

Source: Dunn--Radziwill 2109.07463v3, (5.13), (5.16), Appendix A.
Arithmetic is in Z[rho]/(rho**6+rho**3+1), rho=exp(2*pi*i/9).
This verifies a finite coefficient calculation, not automorphic analysis.
"""
import json
from pathlib import Path


def reduce_poly(a):
    a = list(a) + [0] * max(0, 6 - len(a))
    for n in range(len(a) - 1, 5, -1):
        v = a[n]
        a[n - 3] -= v
        a[n - 6] -= v
    return tuple(a[:6])


ZERO = (0,) * 6
ONE = (1, 0, 0, 0, 0, 0)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def mul(a, b):
    out = [0] * 11
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return reduce_poly(out)


def root(n):
    n %= 9
    return reduce_poly([0] * n + [1])


def conj(a):
    out = ZERO
    for i, x in enumerate(a):
        out = add(out, tuple(x * y for y in root(-i)))
    return out


def cusp_row(cusp, ell, r_alpha2):
    # d_j(x)=scalar*tau_1(omega**u*x)*check_e(delta*x).
    # delta is either zero or a signed Eisenstein unit omega**v.
    data = {
        20: (6, 1, 0, 0),
        22: (6, 0, 1, 1),
        26: (0, 0, 0, 0),
        27: (0, 0, 1, 0),
    }
    scalar_exp, u, delta_sign, delta_power = data[cusp]
    # Conjugates of the three coefficients in DR (5.13), divided by 9.
    bbar = [root(6), root(4), root(-1)]
    row = [ZERO] * 3
    m = ell - r_alpha2
    for t in range(3):
        # -omega**u*mu=omega**t*lambda**(-4)*c*d**3.
        exponent = (t - u + delta_power) % 3
        tr = delta_sign * (2 if exponent == 0 else -1)
        # check_e(delta*mu) has scalar rho**(-tr) and profile kappa_(tr,0).
        profile = (-t + tr) % 3
        term = mul(bbar[t], root(-scalar_exp + 3 * (t - u) * m - tr))
        if ell % 2:
            term = tuple(-x for x in term)
        row[profile] = add(row[profile], term)
    return row


def inner(a, b):
    out = ZERO
    for x, y in zip(a, b):
        out = add(out, mul(x, conj(y)))
    return out


def determinant(a):
    out = ZERO
    for p, sign in [((0, 1, 2), 1), ((1, 2, 0), 1), ((2, 0, 1), 1),
                    ((0, 2, 1), -1), ((2, 1, 0), -1), ((1, 0, 2), -1)]:
        term = mul(mul(a[0][p[0]], a[1][p[1]]), a[2][p[2]])
        out = add(out, tuple(sign * x for x in term))
    return out


def main():
    checks = 0
    rejected_singular = 0
    for ell in range(-6, 7):
        for a2 in range(3):
            mat = [cusp_row(j, ell, a2) for j in (22, 26, 27)]
            for i in range(3):
                for j in range(3):
                    expected = (3, 0, 0, 0, 0, 0) if i == j else ZERO
                    if inner(mat[i], mat[j]) != expected:
                        raise AssertionError((ell, a2, i, j, mat))
                    checks += 1
            det = determinant(mat)
            if mul(det, conj(det)) != (27, 0, 0, 0, 0, 0):
                raise AssertionError((ell, a2, det))
            checks += 1
            bad = [cusp_row(j, ell, a2) for j in (20, 22, 26)]
            if determinant(bad) != ZERO:
                raise AssertionError("The rejected cusp choice must be singular")
            rejected_singular += 1
    result = {
        "status": "pass",
        "arithmetic": "exact Z[rho]/(rho^6+rho^3+1)",
        "source": "https://arxiv.org/html/2109.07463v3",
        "valid_cusps": [22, 26, 27],
        "identity": "M M*=3 I, |det M|^2=27",
        "ell_values": list(range(-6, 7)),
        "row_unit_classes": [0, 1, 2],
        "exact_checks": checks,
        "rejected_minor": [20, 22, 26],
        "rejected_singular_checks": rejected_singular,
        "scope": "Finite local algebra only; not an infinite mean-value proof.",
    }
    out = Path(__file__).with_name("CUSP_MINOR_AUDIT.json")
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
