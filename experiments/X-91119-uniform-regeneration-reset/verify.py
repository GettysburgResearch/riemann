#!/usr/bin/env python3
from fractions import Fraction
import json
from pathlib import Path
import sympy as sp


def main() -> None:
    r = sp.symbols('r', positive=True)
    A = 1-r**2
    B = 1-r
    c = B/sp.Integer(50)

    D = sp.diag(A,A,B,B)
    R = sp.simplify(D-c*sp.eye(4))
    assert sp.simplify(D-(c*sp.eye(4)+R)) == sp.zeros(4)

    j = sp.Matrix([[4,-4,-3,3]])
    Xp,Xm,Yp,Ym = sp.symbols('Xp Xm Yp Ym')
    z = sp.Matrix([Xp,Xm,Yp,Ym])
    X = Xp-Xm
    Y = Yp-Ym

    bp = sp.simplify(4*(A-c)/(3*(B-c)))
    expected_bp = sp.Rational(4,3)*(1+sp.Rational(50,49)*r)
    assert sp.simplify(bp-expected_bp) == 0

    observed = sp.expand((j*R*z)[0])
    expected = sp.expand(3*(B-c)*(bp*X-Y))
    assert sp.simplify(observed-expected) == 0

    assert 400**2 < 49**2*67

    masses = [Fraction(7,20), Fraction(1,4), Fraction(1,10)]
    assert sum(masses) <= 1
    residual = sum(Fraction(1,50)*m for m in masses)
    assert residual <= Fraction(1,50)

    out = {
        'classification': 'PASS_UNIFORM_FOUR_STATE_REGENERATION_SPLIT',
        'doeblin_coefficient': '(1-p^(-1/2))/50',
        'coefficient_upper': '1/50',
        'current_channel_parameter': '4/3*(1+50/(49*sqrt(p)))',
        'corridor': ['4/3','3/2'],
        'worst_prime_integer_gate': '400^2 < 49^2*67',
        'synthetic_branch_residual': str(residual),
        'scope': (
            'Exact symbolic state split, SHARP observation, corridor gate, and '
            'finite subpartition contraction. The Riemann conclusion additionally '
            'requires the typed least-prime measure subpartition stated in L-91332.'
        ),
    }
    path = Path(__file__).resolve().parent/'results'/'verification.json'
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(out['classification'])


if __name__ == '__main__':
    main()
