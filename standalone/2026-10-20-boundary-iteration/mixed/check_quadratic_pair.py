"""Finite and rational checks for QUADRATIC_PAIR_ABSORPTION.md.

This is not a proof of the analytic mean.  It checks the finite Fourier
orientation, its zero mask and conductor modulus, and the exact exponent
arithmetic used after the analytic reflection.  Explicit checks remain
active under python -O.
"""

from fractions import Fraction as F
from pathlib import Path
import hashlib
import json


ROOT = Path(__file__).resolve().parent
checks = 0
rejected_wrong_variants = 0


def require(ok, message):
    global checks
    if not ok:
        raise ArithmeticError(message)
    checks += 1


def primitive_root(p):
    for g in range(2, p):
        if len({pow(g, a, p) for a in range(p - 1)}) == p - 1:
            return g
    raise ArithmeticError("No primitive root")


SIXTH = ((1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1))


def product6(x, y):
    # zeta_6^2 = zeta_6 - 1.
    a, b = x
    c, d = y
    return (a*c-b*d, a*d+b*c+b*d)


class Cyclotomic:
    """Exact Z[zeta_6,zeta_p] in its 2(p-1)-element integral basis."""

    def __init__(self, p, coefficients):
        self.p = p
        c = list(coefficients)
        c += [(0, 0)] * (p-len(c))
        baseline = c[p-1]
        self.c = tuple((a-baseline[0], b-baseline[1]) for a, b in c[:p-1])

    def __eq__(self, other):
        return self.p == other.p and self.c == other.c

    def unit(self, digit):
        return Cyclotomic(self.p, [product6(x, SIXTH[digit % 6]) for x in self.c])

    def conjugate(self):
        c = [(0, 0)] * self.p
        for i, (a, b) in enumerate(self.c):
            c[(-i) % self.p] = (a+b, -b)
        return Cyclotomic(self.p, c)

    def __mul__(self, other):
        require(self.p == other.p, "Cyclotomic fields differ")
        c = [[0, 0] for _ in range(self.p)]
        for i, x in enumerate(self.c):
            if x == (0, 0):
                continue
            for j, y in enumerate(other.c):
                a, b = product6(x, y)
                c[(i+j) % self.p][0] += a
                c[(i+j) % self.p][1] += b
        return Cyclotomic(self.p, c)


for p in (7, 13, 19, 31, 37, 43, 61, 67, 73, 97):
    g = primitive_root(p)
    logs = {pow(g, a, p): a for a in range(p - 1)}
    def gauss(digit, frequency=1):
        c = [[0, 0] for _ in range(p)]
        for x in range(1, p):
            a, b = SIXTH[(digit * logs[x]) % 6]
            c[(frequency*x) % p][0] += a
            c[(frequency*x) % p][1] += b
        return Cyclotomic(p, c)

    def integer(n):
        return Cyclotomic(p, [(n, 0)])

    for j in (0, 2):
        digit = (3 + 2 * j) % 6
        new_j = (-j - 1) % 3
        new_digit = (3 + 2 * new_j) % 6
        require((j, new_j) in ((0, 2), (2, 0)), "Pair does not close")
        require(new_digit == (-digit - 2) % 6, "Wrong sextic reflection digit")
        tau1 = gauss(digit)
        tau2 = gauss(digit+2)
        require(tau1*tau1.conjugate() == integer(p), "First primitive Gauss norm")
        require(tau2*tau2.conjugate() == integer(p), "Second primitive Gauss norm")
        tau12 = tau1*tau2
        require(tau12*tau12.conjugate() == integer(p*p), "Product conductor norm")
        require(tau12*tau12.conjugate() != integer(p), "Wrong square-root conductor was accepted")
        rejected_wrong_variants += 1
        require((3*digit*logs[g]) % 6 != 0, "Cube completion was incorrectly made untwisted")
        rejected_wrong_variants += 1
        require(tau2.unit(new_digit*logs[g]) != tau2.unit(digit*logs[g]),
                "Wrong self-pair reflection was accepted")
        rejected_wrong_variants += 1
        for d in range(p):
            expected = integer(0) if d == 0 else tau1.unit(-digit*logs[d])
            require(gauss(digit, d) == expected, "First transform and zero mask")
        for a in range(1, p):
            require((-digit*logs[pow(a, -1, p)]) % 6 == (digit*logs[a]) % 6,
                    "Inverse variable phase")
        for u in range(p):
            expected = integer(0) if u == 0 else tau2.unit(new_digit*logs[u])
            require(gauss(digit+2, u) == expected, "Second transform and zero mask")

for denominator in range(7, 55):
    delta = F(1, denominator)
    p = F(1, 2) - delta
    # F_delta has three R powers.  Partial summation is legitimate
    # because each is strictly larger than the divisor weight 2 delta.
    right = [(F(1), F(0)), (F(1, 2)-delta, 1-2*delta),
             (1-delta, F(2, 3)-2*delta)]
    require(all(a > 2*delta for a, _ in right), "Partial-summation endpoint")
    reflected = [(a+2*delta, b+4*delta) for a, b in right]
    expected = [(2-2*p, 2-4*p), (1-p, 2-2*p),
                (F(3, 2)-p, F(5, 3)-2*p)]
    require(reflected == expected, "Q5 reflection exponents")
    bilinear = [(F(1, 2)+a/2, b/2) for a, b in reflected]
    require(bilinear == [(F(3, 2)-p, 1-2*p), (1-p/2, 1-p),
                         (F(5, 4)-p/2, F(5, 6)-p)], "Q13 bilinear exponents")
    # At U=KL, add (2p-1) to both K and L exponents.
    terminal = [(2*p-1+2*a-1, 2*p-1+1+2*b) for a, b in bilinear]
    require(terminal == [(F(1), 2-2*p), (p, F(2)),
                         (p+F(1, 2), F(5, 3))], "Q15 terminal exponents")

require(F(1, 2)-F(1, 6) == 2*F(1, 6), "Strict delta endpoint was lost")
require(F(5, 6)+F(3, 5)/3 == F(31, 30), "Sextic counterexample power")
require(F(16, 11) < F(5, 3) < 2, "Sextic counterexample range")

receipt = {
    "status": "PASS",
    "checks": checks,
    "rejected_wrong_variants": rejected_wrong_variants,
    "arithmetic": "Exact integer arithmetic in Z[zeta_6,zeta_p] and rational exponents; no floating point.",
    "finite_fields": [7, 13, 19, 31, 37, 43, 61, 67, 73, 97],
    "proof_sha256": hashlib.sha256((ROOT / "QUADRATIC_PAIR_ABSORPTION.md").read_bytes()).hexdigest(),
    "scope": "Finite orientation/masks and rational exponent identities only; not an analytic proof.",
}
(ROOT / "QUADRATIC_PAIR_CHECK.json").write_text(json.dumps(receipt, indent=2)+"\n", encoding="utf-8")
print(json.dumps(receipt, indent=2))
