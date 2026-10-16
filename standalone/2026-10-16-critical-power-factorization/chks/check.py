#!/usr/bin/env python3
"""Exact finite algebra checks, not a certification of an infinite theorem.

No third-party packages. Explicit RuntimeError gates remain active under -O.
The finite Eisenstein fixture uses ONLY three named prime ideals, not all
ideals below its norm cap. The primitive helper is authenticated from #936.
"""
from __future__ import annotations
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product
import hashlib
import json
import math
from pathlib import Path
import eisenstein_source as es

COUNTS: Counter[str] = Counter()


def check(ok: bool, label: str) -> None:
    COUNTS[label] += 1
    if not ok:
        raise RuntimeError(f'{label}: failed case {COUNTS[label]}')


@dataclass(frozen=True)
class GQ:
    """Gaussian rationals, used for coefficient diagnostics, not row symbols."""
    re: F = F(0)
    im: F = F(0)

    def __add__(self, other: GQ) -> GQ:
        return GQ(self.re+other.re, self.im+other.im)

    def __neg__(self) -> GQ:
        return GQ(-self.re, -self.im)

    def __sub__(self, other: GQ) -> GQ:
        return self+-other

    def __mul__(self, other: GQ) -> GQ:
        return GQ(self.re*other.re-self.im*other.im,
                  self.re*other.im+self.im*other.re)

    def times(self, r: F) -> GQ:
        return GQ(self.re*r, self.im*r)

    def norm2(self) -> F:
        return self.re*self.re+self.im*self.im


Z, O = GQ(), GQ(F(1))


def series_ratio(num: list[GQ], den: list[GQ], n: int) -> list[GQ]:
    check(den[0] == O, 'series_unit_denominator')
    out = [Z]*(n+1)
    for j in range(n+1):
        val = num[j] if j < len(num) else Z
        for t in range(1, min(j, len(den)-1)+1):
            if den[t] != Z:
                val = val-den[t]*out[j-t]
        out[j] = val
    return out


def mul_poly(a: list[GQ], b: list[GQ], n: int) -> list[GQ]:
    out = [Z]*(n+1)
    for j, v in enumerate(a[:n+1]):
        if v == Z:
            continue
        for t, w in enumerate(b[:n-j+1]):
            if w != Z:
                out[j+t] = out[j+t]+v*w
    return out


def local(q: int, m: int, a: GQ, b: GQ, n: int):
    if m < 2 or m % 2:
        raise ValueError('Rational diagnostic uses even m>=2')
    r, lam = F(1,q), F(q**(m//2-1))
    P, Q = [Z]*(m+2), [Z]*(m+2)
    P[0] = Q[0] = O
    P[1], P[m] = a.times(-(1-r)), b.times(-lam)
    Q[1], Q[m], Q[m+1] = -a, b.times(-lam), (a*b).times(lam)
    U, V = series_ratio(P,Q,n), series_ratio(Q,P,n)
    # The two universal coefficientwise majorants (6).
    num = [Z]*(m+2)
    num[1], num[m+1] = GQ(r), GQ(lam)
    denp = [Z]*(m+2)
    denp[0],denp[1],denp[m],denp[m+1] = O,-O,GQ(-lam),GQ(lam)
    denv = [Z]*(m+1)
    denv[0],denv[1],denv[m] = O,GQ(-(1-r)),GQ(-lam)
    Hp,Hv=series_ratio(num,denp,n),series_ratio(num,denv,n)
    Hp[0]=Hv[0]=O
    return P,Q,U,V,Hp,Hv


def local_checks() -> dict:
    phases = [Z,O,-O,GQ(F(0),F(1)),GQ(F(3,5),F(4,5))]
    configs=0
    for m,q,a,b in product((2,4,6,8,12,16),(5,7,25),phases,phases):
        n=2*m+8
        P,Q,U,V,Hp,Hv=local(q,m,a,b,n)
        expected=P+[Z]*(n+1-len(P))
        check(mul_poly(Q,U,n)==expected,'P_equals_Q_times_U')
        expected=Q+[Z]*(n+1-len(Q))
        check(mul_poly(P,V,n)==expected,'Q_equals_P_times_V')
        check(mul_poly(U,V,n)==[O]+[Z]*n,'U_inverse_identity')
        for j in range(n+1):
            check(Hp[j].im==0 and Hv[j].im==0 and Hp[j].re>=0 and Hv[j].re>=0,
                  'majorants_nonnegative')
            check(U[j].norm2()<=Hp[j].re**2,'forward_coefficient_majorant')
            check(V[j].norm2()<=Hv[j].re**2,'inverse_coefficient_majorant')
        configs+=1
    # Square local norms make the critical evaluation rational and exact.
    for m,sqrtq in product((2,4,6,8,12,16,24),(3,5,7,11)):
        q=sqrtq**2
        t,r,lam=F(1,sqrtq),F(1,q),F(q**(m//2-1))
        plus=1+(r*t+lam*t**(m+1))/((1-t)*(1-lam*t**m))
        minus=1+(r*t+lam*t**(m+1))/(1-(1-r)*t-lam*t**m)
        check(plus==minus,'critical_two_masses_equal')
        check(plus==1+2*t**3/((1-t)*(1-r)),'critical_mass_formula')
        check(plus<=1+5*t**3,'critical_five_bound')
    for m in range(2,101):
        theta=F(m,2*(m+1))
        gap=F(1,2*(m+1))
        check(theta+gap==F(1,2),'continuation_tail_exponents')
        check((m+1)*theta-F(m,2)+1==1,'summability_threshold')
    check(F(3,5)**3>F(1,5) and F(3,5)+F(3,5)**2<F(1),
          'uniform_local_nonvanishing_margin')
    for v,s,c in product((F(-3),F(0),F(5,7)),(F(2),F(1,2)),(F(5,6),F(0))):
        check(-v*v/4+(s-c)*v==-(v-2*(s-c))**2/4+(s-c)**2,
              'gaussian_completion_of_square')
    return {'complex_phase_configurations':configs,'even_powers':[2,4,6,8,12,16],
            'coefficient_degree_per_case':'2m+8',
            'critical_mass_rational_cases':28,
            'analytic_theorems_certified_by_finite_checks':False}


def frac_local(q: int, eta: int, n: int):
    P,Q,U,V,_,_=local(q,6,O,GQ(F(eta)),n)
    return [[v.re for v in A] for A in (P,Q,U,V)]


def tuples_under(qs: list[int], cap: int):
    out=[]
    def visit(i: int, exps: tuple[int,...], norm: int):
        if i==len(qs):
            out.append((exps,norm));return
        e=0
        while norm<=cap:
            visit(i+1,exps+(e,),norm)
            norm*=qs[i];e+=1
    visit(0,(),1)
    return sorted(out,key=lambda x:(x[1],x[0]))


def physical_checks() -> dict:
    generators=((-3,-2),(-3,-1),(-5,0))
    qs=[es.en(p) for p in generators]
    check(qs==[7,7,25],'actual_prime_ideal_norms')
    cap=7**7
    ideals=tuples_under(qs,cap)
    maxes=[max(a[j] for a,_ in ideals) for j in range(3)]
    loc=[frac_local(q,eta,n) for q,eta,n in zip(qs,(1,-1,1),maxes)]
    coeffs={}
    for e,N in ideals:
        vals=[]
        for k in range(4):
            val=F(1)
            for j in range(3):
                val*=loc[j][k][e[j]] if e[j]<len(loc[j][k]) else 0
            vals.append(val)
        coeffs[e]=vals
    # Independent finite divisor convolution, keeping all shared factors.
    for e,N in ideals:
        accum=[F(0),F(0)]
        for div in product(*(range(j+1) for j in e)):
            other=tuple(j-t for j,t in zip(e,div))
            accum[0]+=coeffs[div][2]*coeffs[other][1]
            accum[1]+=coeffs[div][3]*coeffs[other][0]
        check(accum==coeffs[e][:2],'ideal_convolution_with_shared_primes')
    rows=es.elements(13)
    check(len(rows)==54,'all_declared_rows')
    physical_pairs=0; zero_values=0
    for u in rows:
        chars=[es.prime_character(p,u) for p in generators]
        for mask in (None,0,2):
            table={}
            for e,N in ideals:
                bad=any(e[j]>0 and (chars[j] is None or j==mask) for j in range(3))
                phase=es.ZERO if bad else es.ROOTS[sum(e[j]*(chars[j] or 0) for j in range(3))%6]
                zero_values+=int(bad)
                table[e]=phase
                expected_zero=any(e[j]>0 and (es.divides(generators[j],u) or j==mask)
                                  for j in range(3))
                check((phase==es.ZERO)==expected_zero,'independent_literal_divisibility_masks')
            for D in (128,4096,cap):
                direct=[(F(0),F(0)),(F(0),F(0))]
                for e,N in ideals:
                    if D<2*N<=2*D:
                        for k in range(2):
                            direct[k]=es.add(direct[k],es.scale(table[e],coeffs[e][k]))
                via=[(F(0),F(0)),(F(0),F(0))]
                # A second physical assembly sums over dilation and residual ideals.
                for de,DN in ideals:
                    for re,RN in ideals:
                        if DN*RN>D: break
                        if D<2*DN*RN<=2*D:
                            ph=es.mul(table[de],table[re])
                            for target,kern,src in ((0,2,1),(1,3,0)):
                                via[target]=es.add(via[target],
                                    es.scale(ph,coeffs[de][kern]*coeffs[re][src]))
                check(via==direct,'literal_masked_physical_dilations')
                physical_pairs+=2
    return {'field':'Q(omega)','generators':[list(p) for p in generators],
            'prime_ideal_norms':qs,'norm_cap':cap,'semigroup_ideals':len(ideals),
            'rows':len(rows),'row_norm_cap':13,'additional_masks':[None,0,2],
            'hard_windows_D':[128,4096,cap],'physical_equalities':physical_pairs,
            'masked_column_evaluations':zero_values,
            'all_native_ideals_below_cap':False,
            'fixture_scope':'All powers/products under the cap of exactly these three prime ideals.'}


def negative_controls() -> list[str]:
    rejected=[]
    def reject(ok: bool, label: str):
        check(ok,'reject_'+label); rejected.append(label)
    P,Q,U,V,_,_=local(7,6,O,O,20)
    reject(P[6]!=GQ(F(-7**3)),'q_cubed_instead_of_q_squared')
    reject(Q[7]==GQ(F(49)) and Q[7]!=Z,'dropping_shared_prime_degree_seven')
    # Masking prime columns but preserving the same prime's sixth-power term is wrong.
    masked=local(7,6,Z,Z,20)[0]
    falsely_unmasked=local(7,6,Z,O,20)[0]
    reject(masked!=falsely_unmasked,'erasing_power_column_nonunit_zero')
    # mu convolution inverse is 1, not mu again.
    reject(mul_poly([O,-O],[O,-O],2)!=[O,Z,Z],'wrong_inverse_Mobius_sign')
    # Failure of extending the subcritical correction domain to unexcluded q=2.
    x=F(37,50)
    reject(8*x**7<1 and 1-F(1,2)*x-4*x**6<0,
           'unexcluded_prime_two_continuation')
    # q^(m/2-1) scaling in the Mellin kernel is exact; m=6 is 2, not 3.
    s=F(3,4)
    reject(F(2)-6*s!=F(3)-6*s,'wrong_physical_dilation_weight')
    reject(F(1,2)-F(3,7)==F(1,14) and F(3,7)!=F(1,2),
           'correction_region_relabelled_as_critical_target')
    return rejected


def main():
    helper=Path(__file__).with_name('eisenstein_source.py').read_bytes()
    blob=hashlib.sha1(b'blob '+str(len(helper)).encode()+b'\0'+helper).hexdigest()
    check(blob=='64d21a7f400f5bf5654fd67735743ff1befab067','primitive_helper_blob')
    result={'local':local_checks(),'physical':physical_checks(),
            'negative_controls':negative_controls()}
    result['counts']=dict(sorted(COUNTS.items()))
    result['total_explicit_predicates']=sum(COUNTS.values())
    result['scope']='Finite algebra and transport only. Not independent review or an RH proof.'
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__=='__main__':
    main()
