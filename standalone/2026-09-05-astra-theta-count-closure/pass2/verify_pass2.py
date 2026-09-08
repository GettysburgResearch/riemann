#!/usr/bin/env python3
"""Finite exact controls, NOT a machine proof of the analytic theorems.

Standard library only; all arithmetic in checks is rational or Q(i).
No floating-point zero evaluation, RH assumption, or finite-to-infinite test.
Explicit exceptions keep checks active under python -O.
"""
from __future__ import annotations
import argparse
from dataclasses import dataclass
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import json
import sys


@dataclass(frozen=True)
class QI:
    re: F = F(0)
    im: F = F(0)

    @staticmethod
    def cast(x: object) -> "QI":
        if isinstance(x, QI):
            return x
        if isinstance(x, (int, F)):
            return QI(F(x))
        raise TypeError(f"Not rational/Q(i): {type(x)}")

    def __add__(self, other: object) -> "QI":
        z = self.cast(other)
        return QI(self.re + z.re, self.im + z.im)
    __radd__ = __add__

    def __neg__(self) -> "QI":
        return QI(-self.re, -self.im)

    def __sub__(self, other: object) -> "QI":
        return self + (-self.cast(other))

    def __rsub__(self, other: object) -> "QI":
        return self.cast(other) - self

    def __mul__(self, other: object) -> "QI":
        z = self.cast(other)
        return QI(self.re*z.re - self.im*z.im,
                  self.re*z.im + self.im*z.re)
    __rmul__ = __mul__

    def __truediv__(self, other: object) -> "QI":
        z = self.cast(other)
        d = z.re*z.re + z.im*z.im
        if not d:
            raise ZeroDivisionError("zero Q(i) divisor")
        return QI((self.re*z.re + self.im*z.im)/d,
                  (self.im*z.re - self.re*z.im)/d)

    def __rtruediv__(self, other: object) -> "QI":
        return self.cast(other)/self

    def __pow__(self, n: int) -> "QI":
        if not isinstance(n, int):
            raise TypeError("integer powers only")
        if n < 0:
            return (1/self)**(-n)
        result, base = QI(F(1)), self
        while n:
            if n & 1:
                result = result*base
            base = base*base
            n //= 2
        return result

    def conj(self) -> "QI":
        return QI(self.re, -self.im)


COUNTS: dict[str, int] = {}

def require(group: str, condition: bool, detail: str) -> None:
    if not condition:
        raise ArithmeticError(f"{group}: {detail}")
    COUNTS[group] = COUNTS.get(group, 0) + 1


def H(atoms: list[QI], v: F, a: int, b: int) -> QI:
    return sum((v/(v+A))**(a+1)*(A/(v+A))**b for A in atoms)


def p(atoms: list[QI], v: F, n: int) -> QI:
    return sum((v/(v+A))**n for A in atoms)


def row(atoms: list[QI], v: F, n: int) -> list[F]:
    out: list[F] = []
    for k in range(n+1):
        z = comb(n,k)*H(atoms,v,k,n-k)
        if z.im:
            raise ArithmeticError("conjugate-complete row not real")
        out.append(z.re)
    return out


def polyval(coeffs: list[F], z: QI) -> QI:
    ans = QI()
    for c in reversed(coeffs):
        ans = ans*z+c
    return ans


def run() -> dict[str, object]:
    COUNTS.clear()
    # Elementary constants used in global analytic proofs.
    require("constants", sum(F(1,factorial(k)) for k in range(7))>F(19,7), "e lower 19/7")
    require("constants", sum(F(1,factorial(k)) for k in range(5))>F(8,3), "e lower 8/3")
    # e = sum through 4 + tail; tail <= (1/5!)/(1-1/6).
    require("constants", sum(F(1,factorial(k)) for k in range(5))+F(1,120)/(1-F(1,6))<F(11,4), "e upper")
    require("constants", F(11,4)**5<4**4, "exp(5/4)<4")
    require("constants", 1-F(11,10)**2/2>F(1,4), "core cosine")
    require("constants", F(10001,10000)**27<2, "complex amplitude factor")
    c27=40000*F(2500,49)**27*F(7,19)**120
    require("constants", c27<F(1,16), "27-layer tail")
    require("constants", F(27,100)+F(123,100)==F(3,2), "phase splitting")
    require("constants", F(56,100)<F(123,100), "small-time tail monotonicity")
    require("constants", F(123)>2*(27+1), "gamma-tail range")
    require("constants", F(123,100)*100-F(226*123,10000)>120, "exponent cutoff")
    ctail=64*F(3,8)**12/(1-F(9,8)*F(3,8)**5)
    require("constants", ctail<F(1,1024), "complete saddle tail")
    require("constants", F(1,512)-ctail>F(1,1024), "central reserve")
    require("constants", 1+F(15,10000)<F(11,10), "small j core phase")
    require("constants", F(15,10000)+F(2,3*10000**3)<F(11,10), "large j core phase")
    require("constants", F(10000,8*4)>60, "count-window reserve")
    require("constants", 10000>(4*4)**2, "logarithm range")
    # Positive coefficients certify the EM modulus polynomial for T=100+s.
    coeff=[22439048,678790,6844,23]
    require("constants", all(x>0 for x in coeff), "EM polynomial coefficients")
    for s in range(8):
        T=100+s
        require("em_polynomial", sum(coeff[k]*s**k for k in range(4))==23*T**3-56*T**2-10*T+48, "EM shifted identity")
    for k in range(5,41):
        require("tail_majorant", k*k//2>=12+5*(k-5), "Gaussian exponent")
        require("tail_majorant", F(k+3)<=8*F(9,8)**(k-5), "linear prefactor")
    for m in range(81):
        y=2*(m+1)
        q=sum(F(factorial(m+1),factorial(m+1-j)*y**j) for j in range(m+2))
        require("incomplete_gamma", 1<=q<2, "finite geometric majorant")

    # The quadrillion-depth corollary is an integer parameter comparison,
    # not a quadrillion tests and not a new zero verification.
    height=3*10**12; depth=10**15; tau=F(1,10**8)
    require("height_corollary", F(height**2+1,196)<height**2, "first logarithm numerator")
    require("height_corollary", F(8,3)**60>height**2, "first log bound")
    require("height_corollary", 2**100>32*height**2, "second log bound")
    require("height_corollary", 2*(depth+1)<tau*height**2, "weighted-tail overlap")
    require("height_corollary", 60*depth+100<tau*(height**2-226), "low-zero dominance overlap")

    # Independent finite versions of the mixed, Laguerre and heat algebra.
    atom_sets=[
        [QI(F(1)),QI(F(3)),QI(F(5))],
        [QI(F(1)),QI(F(2),F(1)),QI(F(2),F(-1))],
        [QI(F(7,2)),QI(F(7,2)),QI(F(11),F(2)),QI(F(11),F(-2))],
    ]
    scales=[F(1,3),F(1),F(4)]
    for atoms in atom_sets:
        for v in scales:
            for a in range(5):
                for b in range(7):
                    hd=sum((-1)**j*comb(b,j)*p(atoms,v,a+j+1) for j in range(b+1))
                    require("mixed_differences", hd==H(atoms,v,a,b), "difference vs spectral atom")
            for A in atoms:
                for a in range(3):
                    for b in range(5):
                        lag=sum(F((-1)**j*comb(a+b,b-j)*factorial(a+j),factorial(j))
                                /(1+A/v)**(a+j+1) for j in range(b+1))
                        lag=F(factorial(b),factorial(a+b))*lag
                        h=(v/(v+A))**(a+1)*(A/(v+A))**b
                        require("laguerre_integral", lag==h, "exact exponential integral")
                        require("heat_integral", v**(a+1)*A**b/(v+A)**(a+b+1)==h, "heat shift and factorials")
            old=None
            for n in range(19):
                rr=row(atoms,v,n)
                p1=p(atoms,v,1)
                require("bernstein_mass", sum(rr)==p1.re and not p1.im, "row mass")
                vv=sum(abs(c) for c in rr)
                ee=sum(max(F(0),-c) for c in rr)
                require("bernstein_mass", vv==p1.re+2*ee, "negative debt")
                squares=sum(c*c for c in rr)
                require("hardy_bounds", squares<=vv*vv<=(n+1)*squares, "Parseval norm bounds")
                if old is not None:
                    prev,prev_v=old
                    for k in range(n):
                        require("degree_elevation", prev[k]==F(n-k,n)*rr[k]+F(k+1,n)*rr[k+1], "refinement")
                    require("bernstein_variation", vv>=prev_v, "monotone total variation")
                old=(rr,vv)
                for z in [QI(F(0),F(1)),QI(F(3,5),F(4,5))]:
                    spectral=sum((v/(v+A))*(1-v/(v+A)+(v/(v+A))*z)**n for A in atoms)
                    require("row_polynomial", polyval(rr,z)==spectral, "all coefficients retained")
                    # Check a single atom of the generating-resolvent identity.
                    if n==0:
                        for A in atoms:
                            w=QI(F(1,7),F(1,11)); kap=v/(v+A)
                            left=kap/(1-w*(1-kap+kap*z))
                            right=v/(1-w)/(v*(1-w*z)/(1-w)+A)
                            require("resolvent", left==right, "Mobius normalization")

    counterfeit=atom_sets[1]
    bad=H(counterfeit,F(1),0,14)
    require("adversarial", bad==QI(-F(433316717939,10**15)), "Bernstein-log counterfeit")
    require("adversarial", sum(abs(c) for c in row(counterfeit,F(1),14))>p(counterfeit,F(1),1).re, "negative row is visible")
    for n in range(1,51):
        require("counterfeit_power_signs", p(counterfeit,F(1),n).re>0 and not p(counterfeit,F(1),n).im, "positive powers do not close mixed signs")
    # Refuse the false inference that all checked power signs imply all H.
    require("adversarial", bad.re<0, "rejected positivity shortcut")

    # The shift A=w^2+1/4 and finite binomial transport.
    for w in [QI(F(100),F(1,4)), QI(F(15)), QI(F(1000),-F(1,3))]:
        for m in range(12):
            require("invariant_shift", (w*w+F(1,4))**m==sum(comb(m,j)*F(1,4)**(m-j)*w**(2*j) for j in range(m+1)), "centered-to-invariant binomial")

    return {
        "status":"PASS_ASTRA_TC2_FINITE_EXACT_CONTROLS",
        "arithmetic":"EXACT_RATIONAL_AND_Q_I",
        "counts":dict(sorted(COUNTS.items())),
        "total_checks":sum(COUNTS.values()),
        "parameters":{"verified_height_import":height,"global_mixed_depth":depth,"small_time":"1/100000000"},
        "counterfeit_H_0_14":str(bad.re),
        "analytic_theorems_machine_proved":False,
        "external_zero_verification_rerun":False,
        "independent_review_completed":False,
        "rh_proved":False,
    }


def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check",type=Path,help="require equality to the committed JSON result")
    args=parser.parse_args()
    try:
        result=run()
        if args.check is not None:
            old=json.loads(args.check.read_text(encoding="utf-8"))
            if old!=result:
                raise ArithmeticError("retained result differs from fresh exact checks")
        print(json.dumps(result,indent=2,sort_keys=True))
        return 0
    except (ArithmeticError, OSError, ValueError, TypeError) as exc:
        print(f"FAIL_ASTRA_TC2: {exc}",file=sys.stderr)
        return 1


if __name__=="__main__":
    raise SystemExit(main())
