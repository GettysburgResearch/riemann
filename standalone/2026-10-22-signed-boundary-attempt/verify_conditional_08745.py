"""Exact certificate for a conditional 0.8745 scalar target.

Standard library only. No numerical mesh, floating-point acceptance, or
assert statements. This checks scalar algebra and inequalities; it does
not prove the high-conductor inverse-moment hypothesis or upstream
analytic theorems.
"""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json


def require(condition, name):
    if not condition:
        raise ArithmeticError(name)


class P:
    """Polynomial in delta and y with exact rational coefficients."""
    def __init__(self, terms):
        self.terms = {e: F(v) for e, v in terms.items() if v}

    @staticmethod
    def of(v):
        return v if isinstance(v, P) else P({(0, 0): F(v)})

    def __add__(self, other):
        out = self.terms.copy()
        for e, v in P.of(other).terms.items():
            out[e] = out.get(e, F(0)) + v
        return P(out)

    __radd__ = __add__

    def __neg__(self):
        return P({e: -v for e, v in self.terms.items()})

    def __sub__(self, other):
        return self + -P.of(other)

    def __rsub__(self, other):
        return P.of(other) + -self

    def __mul__(self, other):
        out = {}
        for a, v in self.terms.items():
            for b, w in P.of(other).terms.items():
                e = (a[0] + b[0], a[1] + b[1])
                out[e] = out.get(e, F(0)) + v * w
        return P(out)

    __rmul__ = __mul__

    def __truediv__(self, scalar):
        return self * (1 / F(scalar))

    def __pow__(self, n):
        require(isinstance(n, int) and n >= 0, 'polynomial power')
        out = P.of(1)
        for _ in range(n):
            out = out * self
        return out

    def at(self, delta, y):
        return sum(v * delta**a * y**b
                   for (a, b), v in self.terms.items())

    def coefficient_delta(self, a):
        return P({(0, b): v for (i, b), v in self.terms.items() if i == a})

    def coefficients_y(self):
        require(all(a == 0 for a, _ in self.terms), 'univariate in y')
        degree = max((b for _, b in self.terms), default=0)
        return [self.terms.get((0, b), F(0)) for b in range(degree + 1)]

    def shift_delta(self, shift):
        delta, y = P({(1, 0): 1}), P({(0, 1): 1})
        out = P.of(0)
        for (a, b), v in self.terms.items():
            out = out + v * (delta + shift)**a * y**b
        return out


KAPPA = F(3, 4)
ELL = F(253, 1500)
B_MARK = F(7, 100)
ETA = F(1, 100)
NU = F(5, 6) * ETA
BOUNDARY = F(11, 12) - ELL / 4
C = 1 / (3 * KAPPA)
H = (1 + B_MARK + 3 * ELL) / 2
LY = (1 + B_MARK - ELL) / 2
LX = (1 - B_MARK - ELL) / 2
C0 = -F(1, 4) + B_MARK / 6 + 5 * ELL / 4
V = ELL + C * (H / 4 - LY / 2)


def primitive(nu):
    delta, y = P({(1, 0): 1}), P({(0, 1): 1})
    x = F(1, 2) - y
    d = 3 - (1 + 2 * C) * x
    p = (2 - 2 * C * x) * (1 - x)
    j = (F(5, 6) - delta - nu) * d + delta * p
    # Literal -2 J E, with R=1-delta+delta P(L-3nu)/(2J).
    numerator = (-2 * j * (C0 + F(1, 2) * delta + delta * x * V
                          - 3 * H * delta / 4)
                 - 3 * H * delta * p * (F(5, 6) - delta - 3 * nu) / 4)
    return d, p, j, numerator


def side_margins():
    asm = F(1, 2) + (ELL / 2) * (F(1, 2) + 2 * ELL / H) - H / 2
    return {
        'b_positive': B_MARK,
        'ell_above_sixth': ELL - F(1, 6),
        'ell_below_fifth': F(1, 5) - ELL,
        'kappa_above_source_lower': KAPPA - F(7497, 10000),
        'boundary_above_principal_floor': BOUNDARY - F(437, 500),
        'lx_above_ell': LX - ELL,
        'ly_minus_ell_above_11b6': LY - ELL - 11 * B_MARK / 6,
        'prime_capacity': 6 * KAPPA * ELL - F(3, 4),
        'ell_over_h_upper': 1 / (6 * KAPPA) - ELL / H,
        'ell_over_h_lower': ELL / H - F(21, 100),
        'ly_above_h_half': LY - H / 2,
        'ly_below_half': F(1, 2) - LY,
        'small_delta_zero': -F(1, 250) - C0,
        'small_delta_eighth': -F(1, 250) - C0 - asm / 8,
        'floor_endpoint': -F(1, 100) - C0 - (F(1, 2) + 3 * ELL / 2) / 50,
        'small_row': -F(1, 20) - 13 * H / 75 + LY / 2 - F(1, 50),
    }


def main():
    require(BOUNDARY == F(1749, 2000), 'rational boundary')
    require(NU == F(1, 120), 'exact inverse gain')
    require(KAPPA == F(3, 4), 'known 7/8 premise')
    d, p, j, fnew = primitive(NU)
    a, b, c = [fnew.coefficient_delta(i) for i in (2, 1, 0)]
    delta = P({(1, 0): 1})
    require(not (fnew - a * delta**2 - b * delta - c).terms,
            'quadratic identity from primitive endpoint')
    discr = 4 * a * c - b**2
    require(all(v > 0 for v in a.coefficients_y()), 'all A coefficients positive')
    require(all(v > 0 for v in discr.coefficients_y()),
            'all discriminant coefficients positive')
    require(a.at(0, F(1, 2)) == 1, 'A upper bound on y interval')
    j_upper = F(99, 40)
    require(j_upper == 3 * (F(5, 6) - NU), 'J upper bound')
    new_margin = discr.at(0, 0) / (8 * j_upper)
    require(new_margin > F(1, 25000), 'new endpoint uniform strict margin')

    # On the new range delta in [1/8,4/5], all terms below are positive.
    new_delta_upper = F(4, 5)
    require(F(5, 6) - new_delta_upper - 3 * NU == F(1, 120),
            't below three halves and R above floor')
    require(F(5, 6) - new_delta_upper - NU == F(1, 40),
            'positive intersection denominator and long slope')
    require((F(1, 2) - 3 * ETA / 2) == F(97, 200),
            't above row-scale cutoff identity coefficient')
    require(F(1, 6) + F(33, 40) * F(100, 99) == 1,
            'exact row-scale flat cutoff')
    require(new_delta_upper < F(5, 6), 'new R at least one-sixth')
    # q>0 follows from D>0,P>0; their exact endpoint lower bounds suffice.
    require(d.at(0, 0) == F(37, 18), 'D positive endpoint')
    require(p.at(0, 0) == F(7, 9), 'P positive endpoint')
    require(all(v > 0 for v in d.coefficients_y()), 'D positive coefficients')
    require(all(v > 0 for v in p.coefficients_y()), 'P positive coefficients')
    two_d_three_p = 2 * d - 3 * p
    x, y = F(1, 2) - P({(0, 1): 1}), P({(0, 1): 1})
    require(not (two_d_three_p - 2 * x * (2 + C - 3 * C * x)).terms,
            'old row upper bound identity')

    # The old formula is retained on [3/4,5/6]. Shift delta=3/4+z.
    _, _, jold, fold = primitive(F(0))
    old_shifted = fold.shift_delta(F(3, 4))
    require(all(v > 0 for v in old_shifted.terms.values()),
            'old high-delta shifted coefficients positive')
    old_margin = old_shifted.at(0, 0) / 5
    require(old_margin > F(1, 25000), 'old high-delta uniform margin')
    require(F(3, 4) < F(4, 5), 'open overlap of licensed ranges')
    # Old inputs alone do not certify this candidate.
    test_delta, test_y = F(47, 100), F(0)
    old_endpoint = -fold.at(test_delta, test_y) / (2 * jold.at(test_delta, test_y))
    require(old_endpoint > 0, 'negative control: old envelope fails at candidate')

    margins = side_margins()
    require(all(v > 0 for v in margins.values()), 'all inherited strict side conditions')
    require(F(749773294079928, 10**15) > 2 * BOUNDARY - 1,
            'target strictly below certified old limiting bracket')
    # An explicit allowable row-extension buffer for the closing argument.
    zeta = F(1, 10**7)
    require(2 * zeta < F(1, 50000), 'row-extension buffer inside half margin')
    require(ELL / (H + zeta) > F(21, 100), 'buffered prime supply')

    result = {
        'status': 'pass',
        'scope': 'Exact continuous scalar certificate conditional on the field-matched improved inverse moment and all inherited analytic interfaces. Matching analytic assembly is stated in separate packet notes and is not checked by this program. No high-conductor moment or new zero-free theorem is proved.',
        'source_commit': '64cb43c038d1828a478cb97cbc32e435e111d2d2',
        'source_formulas': 'Liu arXiv:2610.26835v1 (13.16), (14.3), (14.8), Remark 14.1, Proposition 14.6 and Lemma 14.7, with the stated conditional inverse replacement',
        'parameters': {k: str(v) for k, v in {
            'kappa': KAPPA, 'ell': ELL, 'b': B_MARK, 'eta': ETA, 'nu': NU,
            'B_conditional': BOUNDARY, 'lx': LX, 'ly': LY, 'h': H,
            'C0': C0, 'V': V, 'zeta': zeta}.items()},
        'new_range': ['1/8', '4/5'],
        'old_high_range': ['3/4', '5/6'],
        'flat_inverse_cutoff': '100/99',
        'A': [str(v) for v in a.coefficients_y()],
        'B': [str(v) for v in b.coefficients_y()],
        'C': [str(v) for v in c.coefficients_y()],
        'discriminant': [str(v) for v in discr.coefficients_y()],
        'old_shifted_coefficients': {f'z^{i}y^{j}': str(v)
                                     for (i, j), v in sorted(old_shifted.terms.items())},
        'strict_endpoint_margin': '1/25000',
        'new_proved_margin': str(new_margin),
        'old_high_proved_margin': str(old_margin),
        'side_margins': {k: str(v) for k, v in margins.items()},
        'negative_control_old_endpoint': str(old_endpoint),
        'checker_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
        'analytic_HC_proved': False,
        'achieved_zero_free_improvement': False,
        'arithmetic': 'fractions.Fraction; no floating-point acceptance or sample grid',
    }
    encoded = json.dumps(result, indent=2) + '\n'
    Path(__file__).with_name('CONDITIONAL_08745_CHECKS.json').write_text(
        encoded, encoding='utf-8', newline='\n')
    print(encoded, end='')


if __name__ == '__main__':
    main()
