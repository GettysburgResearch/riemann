"""Exact finite controls for the endpoint forward-correction adapter.

These controls do not certify an asymptotic moment, joint continuation or RH.
All acceptance predicates use require and remain active under Python -O.
"""
from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations, product
from math import comb
from pathlib import Path
import argparse
import json


def require(condition, context):
    if not condition:
        raise ArithmeticError(context)


def coefficient(e, masked):
    return 1 if masked else 1 - sum(x != 0 for x in e)


def controls():
    counts = {"local_convolution": 0, "critical_pair": 0,
              "absolute_local_sum": 0, "residual_sign": 0,
              "source_masks": 0, "incidence": 0}
    # Multiply the independently enumerated product polynomial by the
    # proposed correction coefficients, at every multidegree tested.
    for k in range(2, 7):
        for e in product(range(3), repeat=k):
            positive = [i for i, x in enumerate(e) if x]
            for masked in (False, True):
                got = 0
                for size in range(len(positive) + 1):
                    for chosen in combinations(positive, size):
                        child = list(e)
                        for i in chosen:
                            child[i] -= 1
                        got += (-1) ** size * coefficient(child, masked)
                wanted = (int(sum(e) == 0) if masked else
                          int(sum(e) == 0) - int(sum(e) == 1))
                require(got == wanted, ("local convolution", k, e, masked))
                counts["local_convolution"] += 1
        for i, j in combinations(range(k), 2):
            e = [0] * k
            e[i] = e[j] = 1
            require(coefficient(e, False) == -1, ("critical pair", k, i, j))
            counts["critical_pair"] += 1
        for s in (2*k+1, 2*k+3, 4*k+1):
            t = F(1, s)
            direct = 1 + sum((m-1)*comb(k,m)*(t/(1-t))**m
                             for m in range(2,k+1))
            closed = 2 + (k*t-1)/(1-t)**k
            require(direct == closed and direct >= 1,
                    ("absolute local sum", k, t))
            # The genuine degree-two coefficient is one per pair;
            # omitted higher-support terms remain positive.
            require(direct >= 1 + comb(k,2)*t*t,
                    ("critical positive leading term", k, t))
            counts["absolute_local_sum"] += 1
    for k in range(1, 11):
        patterns = 0
        for r in range(k+1):
            for s in range(k+1):
                if r+s == 0:
                    continue
                multiplicity = comb(k,r)*comb(k,s)
                patterns += multiplicity
                residue = (r-s) % 6
                require((-1)**(r+s) == (-1)**residue,
                        ("literal Mobius sign",k,r,s))
                require(residue != 0 or r+s >= 2,
                        ("principal singleton forbidden",k,r,s))
                require(r+s != 1 or residue in (1,5),
                        ("singleton conductor",k,r,s))
                if r+s == 2 and residue != 0:
                    require(residue in (2,4) and (r==0 or s==0),
                            ("nonprincipal double",k,r,s))
                counts["residual_sign"] += multiplicity
        require(patterns == 2**(2*k)-1, ("complete pattern count",k))
    # Zero-extension guard: a residual-zero prime is still masked.
    # The local polynomial at eta=0 is one on either side of G3.
    require(0**6 == 0 and 0**0 == 1, "literal nonunit conventions")
    for k in range(2,9):
        require(sum((-1)**len(I) for size in range(1,k+1)
                    for I in combinations(range(k),size)) == -1,
                ("nonunit nonconstant terms vanish",k))
        counts["source_masks"] += 1
    # A feasible three-axis configuration: c13=c23=D^(1/2),
    # all other shared factors one. This is outside the old ranges.
    axis = [F(1),F(1),F(1)]
    common = F(0)
    for I, power in [((0,2),F(1,2)),((1,2),F(1,2))]:
        for i in I:
            axis[i] -= power
    require(axis == [F(1,2),F(1,2),F(0)], "feasible native incidence")
    p = sum(axis)
    q1 = p - max(axis)
    q2 = sum(sorted(axis)[:1])
    require(p == 1 and q1 == F(1,2) and q2 == 0 and common == 0,
            "r-axis range bookkeeping")
    for h in (F(101,100),F(11,10)):
        require(p > h/2, "outside previous short product")
        require(common < (5-(h-1))/9, "outside growing common gcd")
        counts["incidence"] += 1
    return counts


def source_hashes():
    base = Path('/workspace/.riemann-research/moment-sources')
    rows = [
      ('913/standalone/2026-10-10-sextic-moment-descent/GENERAL_MOMENT_ATTACK.md',
       'a4ca15c0d731ef6000b19507b39b64a4786a7f8af9939864b3176221bf02b499'),
      ('914/standalone/2026-10-10-sextic-moment-conductor-core/CONDUCTOR_SECTORS.md',
       'c160bbb1b1d7c6bcc5514d496ad41f15fd17ea3d36206b0d05cfa0d7d6503983'),
      ('914/standalone/2026-10-10-sextic-moment-conductor-core/A2_COMPLETION.md',
       'd99eade56807077b07e5ec1325001f1592115db216e1e10e6a3906a3e01f0aad'),
      ('915/standalone/2026-10-10-sextic-critical-core/ANISOTROPIC_SINGLETON_CORES.md',
       '4854a01c2767a1dc4d7c67c490e5502bcad8935bce3089ba5f37adb1e6d02ea8'),
      ('915/standalone/2026-10-10-sextic-critical-core/COUPLED_THETA_COMPLETION.md',
       'f3b57f69338e8736ffe4addd5a6e2ebf6d5f8976ee9d2fda5921c83ff484eb36'),
      ('915/standalone/2026-10-10-sextic-critical-core/REUNITED_RAMANUJAN_EULER_PRODUCT.md',
       '6d1f0e01d8645972de0c38897e37633d8bfc70d193f6e279dcf8f33b0e992433'),
      ('915/standalone/2026-10-10-sextic-critical-core/PRIMARY_SOURCE_MATCH.md',
       'c4162dc668980d44c115e67868393fc43230d78a0fdacf73ff05abcc8a200258')]
    out = {}
    for rel, expected in rows:
        got = sha256((base/rel).read_bytes()).hexdigest()
        require(got == expected, ('frozen source',rel))
        out[rel] = got
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    here = Path(__file__).resolve().parent
    record = {
      'status':'PASS_EXACT_FINITE_ENDPOINT_CONTROLS',
      'checks':controls(), 'source_sha256':source_hashes(),
      'manuscript_sha256':sha256((here/'GENERALIZED_MOMENT_ATTACK.md').read_bytes()).hexdigest(),
      'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
      'asymptotic_moment_proved':False,
      'additional_mixed_fourth_moment_paid':False,
      'signed_remainder_bound_proved':False,
      'joint_reflected_continuation_proved':False,
      'rh_proved':False}
    args.output.write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
    print(record['status'])


if __name__ == '__main__':
    main()
