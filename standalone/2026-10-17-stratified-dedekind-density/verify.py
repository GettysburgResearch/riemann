#!/usr/bin/env python3
"""Exact arithmetic and finite-coverage checks for the density-stratum proof.

Standard library only. Every all-parameter inequality is certified in a
Bernstein basis, not inferred from sampled values. No analytic input is
proved by this program. Conditions remain active under python -O.
"""
from __future__ import annotations
import argparse
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction as F
import itertools
import json
from math import comb
from pathlib import Path

COUNTS: Counter[str] = Counter()
MUTATION = 'none'
CAP = F(1, 10000)


def require(ok: bool, group: str) -> None:
    COUNTS[group] += 1
    if not ok:
        raise ArithmeticError(group)


@dataclass(frozen=True)
class P:
    """A rational polynomial in the positive slack parameter e."""
    c: tuple[F, ...]

    def __init__(self, *c):
        cc = [F(v) for v in c] or [F(0)]
        while len(cc) > 1 and cc[-1] == 0:
            cc.pop()
        object.__setattr__(self, 'c', tuple(cc))

    @staticmethod
    def coerce(x):
        return x if isinstance(x, P) else P(x)

    def __add__(self, other):
        other = P.coerce(other)
        return P(*(self.at(i) + other.at(i) for i in range(max(len(self.c), len(other.c)))))

    __radd__ = __add__

    def __neg__(self):
        return P(*(-v for v in self.c))

    def __sub__(self, other):
        return self + (-P.coerce(other))

    def __rsub__(self, other):
        return P.coerce(other) - self

    def __mul__(self, other):
        other = P.coerce(other)
        c = [F(0)] * (len(self.c) + len(other.c) - 1)
        for i, x in enumerate(self.c):
            for j, y in enumerate(other.c):
                c[i+j] += x*y
        return P(*c)

    __rmul__ = __mul__

    def __truediv__(self, q):
        q = F(q)
        if not q:
            raise ZeroDivisionError('polynomial scalar division by zero')
        return self * (1/q)

    def at(self, i: int) -> F:
        return self.c[i] if i < len(self.c) else F(0)

    def __call__(self, x) -> F:
        x = F(x)
        ans = F(0)
        for c in reversed(self.c):
            ans = ans*x + c
        return ans

    def bernstein(self, right=CAP) -> list[F]:
        # p(right*t)=sum_j b_j binom(n,j)t^j(1-t)^(n-j).
        n = len(self.c)-1
        return [sum((self.c[i]*right**i*F(comb(j,i), comb(n,i))
                     for i in range(j+1)), F(0)) for j in range(n+1)]

    def cert(self, strict=False, group='bernstein_nonnegative') -> list[str]:
        b = self.bernstein()
        require(all(x >= 0 for x in b), group)
        if strict:
            # The last basis function is t^n>0 for 0<t<=1; n=0 is constant.
            require(b[-1] > 0, group+'_strict_positive_e')
        return list(map(str,b))

    def record(self):
        return {'power_coefficients': list(map(str,self.c)),
                'at_e_cap':str(self(CAP))}


e = P(0,1)
ALPHA = F(5,9)
H = F(4,9)
BETA = P(H,1)
C = F(19,54)
B = F(35,54)
ZLINE = F(2,5)
SMALL = F(1,100)
UPPER = P(H,1)


def density(s: F):
    q = 2*s-1
    if s <= F(2,3):
        x, y = F(1,2), 2/(4-6*q)
        delta = q/(4-6*q)
    elif s <= F(11,12):
        den = 6*q*(10-6*q)-10
        x, y = (24*q-5)/den, (42*q-8)/den
        delta = q*(36*q-6*(6*s-2)+3)/(36*q*(3-2*s)-24*s+2)
    else:
        den = 1-6*(1-q)**2
        x, y = (6*q-4)/den, (8*q-5)/den
        delta = (8*s*s-10*s+3)/(1-24*(1-s)**2)
    return x, y, 1-delta, 1/(6-4*s), (1-s)/(3-2*s)


def density_checks():
    out=[]
    expected = [(F(2,3),F(5,6)), (F(3,4),F(8,11)),
                (F(17,20),F(191,359)), (F(19,20),F(11,47))]
    for s,g_expected in expected:
        x,y,g,z,ht = density(s)
        require(0 <= x <= y and z > 0, 'detector_cutoffs')
        require(g == g_expected, 'density_formula')
        # Pairs below are the N exponent and the coefficient of d in the
        # height exponent, AFTER removing the common outside factor T.
        inner = [x,F(1),x/3+F(5,6),5*x/6+F(1,3)]
        terms = [(F(1,2)+(F(1,2)-s)*y+v/2,
                  F(1,4)+(F(1,2)-s)*z) for v in inner]
        terms += [((2-2*s)*y,(2-2*s)*z), (1+(1-2*s)*x,F(0))]
        for c,dv in [(F(1,3),F(11,6)-2*s),(F(5,6),F(4,3)-2*s)]:
            terms += [(c+dv*x,F(0)),(c+dv*y,dv*z)]
        for nn,tt in terms:
            require(nn <= g, 'every_detector_N_term')
            require(tt <= ht, 'every_detector_height_term')
        require(max(nn for nn,_ in terms)==g, 'detector_bound_attained')
        out.append({'sigma':str(s),'A_N_exponent':str(x),'B_N_exponent':str(y),
                    'B_T_exponent_divided_by_degree':str(z),'density_N_exponent':str(g),
                    'density_T_exponent':'1 + degree*'+str(ht),
                    'all_N_terms':list(map(str,(v[0] for v in terms))),
                    'all_T_terms_divided_by_degree':list(map(str,(v[1] for v in terms)))})
    return out


def domain(x,y,z):
    x,y,z=map(P.coerce,(x,y,z))
    return {'x':x,'y':y,'z':z,'6z+y-1':6*z+y-1,'x+6z-1':x+6*z-1,
            'x+y-1':x+y-1,'x+y+6z-2':x+y+6*z-2,
            '6x+6z-5':6*x+6*z-5,'x-1/2':x-F(1,2),
            '3x-2':3*x-2,'3x+y-5/2':3*x+y-F(5,2)}


def exponent(x,y,z):
    return ALPHA/2 + x-1 + H*z + BETA*(y-1)


def positive_point(x,y,z,name):
    return {key:v.cert(strict=True, group='domain_'+name)
            for key,v in domain(x,y,z).items()}


def strata():
    rows=[('good',F(2,3),F(1,2),F(1),False),
          ('s_2_3_to_3_4',F(3,4),F(1,4),F(5,6),True),
          ('s_3_4_to_17_20',F(17,20),F(3,20),F(8,11),True),
          ('s_17_20_to_19_20',F(19,20),F(1,20),F(191,359),True),
          ('s_at_least_19_20',F(1),F(0),F(11,47),True)]
    if MUTATION == 'wrong-stratum-count':
        rows[1] = (rows[1][0], rows[1][1], rows[1][2], F(1), True)
    if MUTATION == 'omit-good-class':
        rows=rows[1:]
    return rows


def contour_checks():
    M=ALPHA+BETA
    (M-1).cert(strict=True, group='M_strictly_greater_one')
    (P(ALPHA)-BETA).cert(strict=True, group='beta_below_alpha')
    (UPPER-H).cert(strict=True, group='large_frequency_strict_gap')
    require(C==ALPHA/2+H/6 and B==1-C, 'principal_normalization')
    if MUTATION == 'wrong-principal-shift':
        require(B==F(13,20), 'incorrect_old_principal_normalization')
    if MUTATION == 'use_closed_endpoint':
        require((M-1)(0)>0, 'inadmissible_M_equals_one')
    rows = strata()
    require(len(rows)==5 and rows[0][0]=='good', 'complete_five_classes')
    expected=[P(F(2,27),-F(283,180),-F(1,2)),
              P(F(13,108),-F(69,40),-F(3,2)),
              P(F(533,5940),-F(18639,11880),-F(3,2)),
              P(F(19139,193860),-F(513225,387720),-F(3,2)),
              P(F(244,1269),-F(12699,12690),-F(3,2))]
    out=[]
    for row,want in zip(rows,expected):
        name,x0,y0,nu0,exceptional = row
        x,y=P(x0)+e,P(y0)+e
        nu=P(nu0)+(e if exceptional else 0)
        u=nu+(1-y)/2-ZLINE
        u.cert(strict=True, group='positive_intermediate_U_exponent')
        save=C-exponent(x,y,ZLINE)-UPPER*u
        require(save==want, 'exact_stratum_saving_polynomial')
        margin=(save-(F(2,27)-2*e)).cert(group='full_interval_saving')
        points=[]
        # Same intermediate rectangle: start at (x1,x1,2/5), move xi,
        # then w. Convexity covers each connecting segment.
        for point in [(1+e,1+e,ZLINE),(x,1+e,ZLINE),(x,y,ZLINE)]:
            points.append(positive_point(*point,name))
        out.append({'name':name,'xi_line':x.record(),'w_line':y.record(),
                    'row_count_exponent':nu.record(),'U_exponent':u.record(),
                    'saving':save.record(),'saving_minus_target_Bernstein':margin,
                    'domain_vertices_checked':len(points)})
    # Principal row: xi kept at 1+e; cross w=1, then z=1/6 in the residue.
    ps=[(1+e,1+e,F(1,6)+e),(1+e,P(F(1,2)),F(1,6)+e),
        (1+e,P(1),F(1,6)+e),(1+e,P(1),e)]
    principal_domains=[positive_point(*p,'principal') for p in ps]
    extras={
        'theta':C-(ALPHA+BETA/2-F(1,2)),
        'principal_w':C-exponent(1+e,P(F(1,2)),F(1,6)+e),
        'principal_z':C-exponent(1+e,P(1),e),
        'small_frequencies':C-exponent(1+e,F(1,2)+e,ZLINE)
               -SMALL*(1+(1-(F(1,2)+e))/2-ZLINE),
    }
    extra_expected={
        'theta':P(F(2,27),-F(1,2)),
        'principal_w':P(F(2,9),-F(17,18)),
        'principal_z':P(F(2,27),-F(13,9)),
        'small_frequencies':P(F(5941,54000),-F(50730,54000),-1),
    }
    for name,p in extras.items():
        require(p==extra_expected[name], 'extra_saving_identity')
        (p-(F(2,27)-2*e)).cert(group='extra_saving_full_interval')
    # L=ceil(10/e). In E(4,4,L)+(h+e)(1-L), the L dependence is -e*L.
    # e*L>=10. It is legitimate to fix L after choosing e, before Z varies.
    lower_large = C-ALPHA/2-3-3*BETA-H-e+10
    lower_large.cert(strict=True, group='large_frequency_saving')
    (lower_large-4).cert(strict=True, group='large_frequency_more_than_four')
    # The large vertex's domain is positive for every L>=1; L in use is >=100000.
    large_domain=positive_point(P(4),P(4),P(1),'large_at_L_one')
    for lin in domain(P(4),P(4),P(1)).values():
        require(lin(0)>0, 'large_domain_base')
    # All domain forms have nonnegative z coefficient.
    for key in domain(P(4),P(4),P(1)):
        require(domain(P(4),P(4),P(2))[key](0)>=domain(P(4),P(4),P(1))[key](0),
                'large_domain_z_monotonicity')
    require(B+C-F(2,27)==F(25,27), 'final_zero_free_boundary')
    require(C-F(2,27)==F(5,18), 'actual_detector_growth')
    return {'M':M.record(),'principal_residue_scale':str(C),'principal_shift':str(B),
            'strata':out,'principal_domain_vertices_checked':len(principal_domains),
            'other_savings':{k:v.record() for k,v in extras.items()},
            'large_saving_lower_polynomial':lower_large.record(),
            'large_domain_forms_checked_at_L_one':len(large_domain),
            'source_boundary':'25/27','not_claimed':'Source theorems and contour analytic estimates are not certified by these checks.'}


def finite_coverage_checks():
    # All four nested event sets generated by every subset of these possible
    # zero abscissae; boundaries are included exactly, not rounded away.
    cut=[F(2,3),F(3,4),F(17,20),F(19,20)]
    grid=[F(3,5),*cut,F(7,10),F(4,5),F(9,10),F(39,40)]
    cases=0
    for bits in itertools.product([False,True],repeat=len(grid)):
        zeros=[x for x,chosen in zip(grid,bits) if chosen]
        E=[any(x>=v for x in zeros) for v in cut]
        bins=[not E[0]]+[E[j] and not E[j+1] for j in range(3)]+[E[3]]
        require(sum(bins)==1,'partition_complete_and_disjoint')
        for j in range(4):
            if bins[j]:
                require(all(x<cut[j] for x in zeros),'reciprocal_class_has_no_upper_zero')
        for j in range(1,5):
            if bins[j]:
                require(E[j-1],'density_charged_at_lower_boundary')
        cases+=1
    # Norm of an nth-power-free ideal is not its radical. Two distinct primes,
    # all 36 possible exponent patterns through five are retained.
    for a,b in itertools.product(range(6),repeat=2):
        norm=7**a*13**b
        radical=(7 if a else 1)*(13 if b else 1)
        require(norm>=radical,'powerfree_norm_not_smaller_radical')
        if a>1 or b>1:
            require(norm>radical,'powerfree_norm_strict_for_repeated_prime')
    return {'all_synthetic_zero_subsets':cases,'powerfree_two_prime_cases':36,
            'scope':'Exact partition/indexing examples; these do not count zeros of actual L-functions.'}


def limiting_model_certificate():
    # Algebraic dual certificates for the restricted upper-estimate model.
    for h,beta in [(F(2,5),F(9,20)),(F(4,9),F(4,9)),(F(9,20),F(1,2))]:
        theta=2*h/3-beta/2
        floor=F(1,3)+beta/2-13*h/12
        require(F(2,27)-theta==(F(4,9)-h)/6+(beta-h)/2,
                'dual_low_h_identity')
        require(F(2,27)-(theta+floor)/2==F(5,24)*(h-F(4,9)),
                'dual_high_h_identity')
    # Symbolic slopes and their bounds, recorded rather than optimized numerically.
    require(F(1)-F(3,2)*F(4,9)==F(1,3), 'slope_threshold')
    return {'low_h_identity':'2/27-S_theta=(4/9-h)/6+(beta-h)/2',
            'high_h_identity':'2/27-(S_theta+S_floor)/2=(5/24)(h-4/9)',
            'scope':'Only the stated positive theta/good-row model, beta<=alpha, M>1; not an arithmetic lower bound or an RH no-go theorem.'}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path)
    parser.add_argument('--mutation',choices=['none','wrong-stratum-count','omit-good-class',
                        'wrong-principal-shift','use_closed_endpoint'], default='none')
    args=parser.parse_args()
    global MUTATION
    MUTATION=args.mutation
    out={'status':'PASS: exact finite algebra only','slack_interval':'0 < e <= 1/10000',
         'density':density_checks(),'contours':contour_checks(),
         'coverage':finite_coverage_checks(),'limited_model_certificate':limiting_model_certificate()}
    out['counts']=dict(sorted(COUNTS.items()))
    out['total_predicates']=sum(COUNTS.values())
    text=json.dumps(out,sort_keys=True,indent=2)+'\n'
    if args.output:
        args.output.write_text(text)
    else:
        print(text,end='')

if __name__=='__main__':
    main()
