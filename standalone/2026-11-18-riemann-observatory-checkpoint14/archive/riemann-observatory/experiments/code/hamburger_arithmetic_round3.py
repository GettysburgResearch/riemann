"""Exact rational checks for the elementary infinite-pole converse exception.

These checks support, rather than replace, the proof in
 audits/hamburger_converse_round3.md. No RH computation is performed.
Only Python standard-library arithmetic is used.
"""
from fractions import Fraction as F
import json
from pathlib import Path


def multiplier(q, x):
    return 1 / ((1 - F(q*q, 1) / x) * (1 - q*x))


def coefficients(q, limit):
    # M(s) = sum_{ell>=1} b_ell (q**ell)**(-s)
    b = {}
    ell = 1
    while q**ell <= limit:
        b[q**ell] = -sum((F(q)**(3*j-ell) for j in range(ell)), F(0))
        ell += 1
    return b


def main():
    checks=[]
    for q in (2,3,5):
        for x in (F(1,7), F(2,3), F(7,5), F(13,2)):
            if x in (F(q*q), F(1,q)):
                continue
            assert multiplier(q,x)==multiplier(q,F(q)/x)
            checks.append({'q':q,'x':str(x),'M':str(multiplier(q,x))})
    b=coefficients(2,32)
    # An independent recurrence follows from
    # (1-q^2 y)(1-q^(-1)y) M = -q^(-1)y, y=q^(-s).
    rec=[F(0)]*6
    rec[1]=-F(1,2)
    for ell in range(2,6):
        rec[ell]=(F(4)+F(1,2))*rec[ell-1]-2*rec[ell-2]
        assert rec[ell]==b[2**ell]
    ordinary={n:sum((v for d,v in b.items() if n%d==0),F(0)) for n in range(1,33)}
    assert ordinary[1]==0 and ordinary[2]==-F(1,2) and ordinary[4]==-F(11,4)
    result={
        'arithmetic':'exact rational; standard library only',
        'identity':'M(s)=M(1-s), x=q^s -> q/x',
        'reflection_checks':checks,
        'q2_multiplier_coefficients':{str(k):str(v) for k,v in b.items()},
        'q2_zeta_product_coefficients':{str(k):str(v) for k,v in ordinary.items()},
        'proof_scope':'Finite exact checks only. Global symmetry, convergence for Re(s)>2, and infinitely many poles are established analytically in the audit.',
        'novelty_claim':False,
    }
    dest=Path(__file__).resolve().parents[1]/'results'/'hamburger_arithmetic_round3.json'
    dest.write_text(json.dumps(result,indent=2)+'\n')
    print('12 exact reflection checks, 4 independent coefficient recurrence checks, and first coefficients passed.')

if __name__=='__main__':main()
