#!/usr/bin/env python3
"""Exact finite checks for the proposed hereditary-numerator composition.

No analytic theorem is proved by this program. The finite parameter choices
are inputs; every density monomial, selected moment and contour cost is derived.
Use --details for the complete derived class report. Mutations are finite-model
negative controls, not perturbations of a formalized analytic proof.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
from typing import Any
import model as M

ROOT = Path(__file__).resolve().parent
COUNTS: Counter[str] = Counter()


def check(condition: bool, group: str, message: str) -> None:
    COUNTS[group] += 1
    if not condition:
        raise ValueError(f'{group}: {message}')


def frac(s: str) -> F:
    if '/' in s:
        a, b = s.split('/')
        return F(int(a), int(b))
    return F(int(s))


def strings(obj: Any) -> Any:
    if isinstance(obj, F):
        return str(obj)
    if isinstance(obj, float):
        raise TypeError('Floating point is forbidden in the certificate')
    if isinstance(obj, dict):
        return {str(k): strings(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [strings(v) for v in obj]
    return obj


def read_rows() -> list[dict[str, Any]]:
    rows = []
    for line in (ROOT/'strata.tsv').read_text().splitlines():
        if not line or line.startswith('#'):
            continue
        s, method, t, a, b, r, y = line.split()
        rows.append(dict(sigma=frac(s), method=method, theta=frac(t),
                         A=frac(a), B=frac(b), r=int(r), y=frac(y)))
    return rows


# A polynomial is given by its coefficients in e, degree at most two.
def bernstein(p: tuple[F, F, F]) -> tuple[F, F, F]:
    a, b, c = p
    E = M.EMAX
    return a, a+b*E/2, a+b*E+c*E*E


def budget(p: tuple[F, F, F], name: str) -> None:
    gap = (M.A_SCALE/2-p[0], F(3)-p[1], -p[2])
    for value in bernstein(gap):
        check(value >= 0, 'whole_interval_budgets', name)


def domain_line(x: tuple[F, F], y: tuple[F, F], z: tuple[F, F], name: str) -> None:
    g0 = M.domain(x[0], y[0], z[0])
    gE = M.domain(x[0]+x[1]*M.EMAX, y[0]+y[1]*M.EMAX,
                  z[0]+z[1]*M.EMAX)
    for left, right in zip(g0, gE):
        check(left >= 0 and right > 0, 'strict_contour_domains', name)


def independent_density(theta: F, sigma: F, a: F, b: F) -> list[F]:
    # Build the eight pre-elimination Holder monomials (U power, R power).
    S = (2-2*theta, 2*theta-1)
    L = (F(13,6)-2*theta, F(0))
    moll = [S, ((2-2*theta)*a,F(0)),
            (F(5,6)+(F(4,3)-2*theta)*a,F(0)),
            (F(1,3)+(F(11,6)-2*theta)*a,F(0))]
    pairs=[]
    for num, mol in [(S,moll[0]),(L,moll[0])]+[
            pair for mol in moll[1:] for pair in ((S,mol),(L,mol))]:
        u=(theta-sigma)*b+num[0]/4+mol[0]/2
        r=F(1,4)+num[1]/4+mol[1]/2
        check(0 <= r < 1, 'holder_elimination', 'R exponent')
        pairs.append(u/(1-r))
    return pairs+M.tail(sigma,a,b)+[F(1,2)]


def finite_moment_checks() -> None:
    nus=[F(0),F(1,10),F(1,6),F(1,4),F(1,2),F(2,3),F(3,4),F(9,10),F(1)]
    ys=[F(0),F(1,4),F(1,3),F(1,2),F(7,12),F(3,4),F(1)]
    for nu in nus:
        v0=M.vzero(nu)
        check(M.k(v0)-v0==nu,'crossing_formula','k(v0)-v0')
        for r in (1,2,3,4):
            L=F(r,2)
            for y in ys:
                # Exact finite diagnostics; the written convexity proof supplies
                # the unsampled continuum statement.
                candidates={F(0),L}|{v for v in (F(1,2),F(1),F(2),v0) if 0<=v<=L}
                brute=max(min(nu+(2-2*y)*v,M.k(v)+(1-2*y)*v) for v in candidates)
                check(M.phi(nu,y,L)==brute,'crossing_formula','endpoint maximum')
                for j in range(5):
                    v=L*j/4
                    check(min(nu+(2-2*y)*v,M.k(v)+(1-2*y)*v)<=brute,
                          'finite_block_diagnostics','interior dyad')
                if y>=F(1,2):
                    for q in (F(0),F(1,3),F(1)):
                        for t in (F(0),F(1,2),F(1)):
                            v=F(r,2)*q*t
                            dual=r*q*(1-2*y)+min(nu+2*y*v,M.k(v)+(2*y-1)*v)
                            target=min(nu+(2-2*y)*v,M.k(v)+(1-2*y)*v)
                            check(dual<=target,'actual_conductor','dual Q power')
    for nu in nus[:-1]:
        delta=min(F(1,1000),1-nu)
        for r in (1,2,3,4):
            for y in ys[1:-1]:
                inc=M.mean(r,nu+delta,y)-M.mean(r,nu,y)
                check(0<=inc<=delta,'finite_lipschitz_diagnostics','same subset count loss')
    check(M.selected_kappa(3,F(2,3),F(3,4))==F(5,6),'new_specializations','upper sixth')
    check(M.selected_kappa(3,F(2,3),F(1,4))==F(7,3),'new_specializations','lower sixth')
    check(M.mean(3,F(2,3),F(1,4))==F(17,18),'new_specializations','selected first mean')
    check(F(23,24)-F(17,18)==F(1,72),'new_specializations','previous sufficient envelope')


def masks(mutation: str | None) -> None:
    from math import gcd
    # Abstract rational residue fixtures; NOT a number-field or L-value census.
    primes=[7,13]
    roots={7:3,13:2}
    logs={p:{pow(roots[p],j,p):j%6 for j in range(p-1)} for p in primes}
    def char(n: int, support: tuple[int,...]):
        if any(n%p==0 for p in support):
            return None  # Literal character zero.
        return sum(logs[p][n%p] for p in support)%6
    for support in ((7,),(13,),(7,13)):
        modulus=1
        for p in support: modulus*=p
        for c in (1,2,7,13,14,49,91):
            for d in (1,2,7,13,14,49,91):
                left=char(c*d**6,support)
                right=char(c,support) if gcd(d,modulus)==1 else None
                if mutation=='erased_mask': right=char(c,support)
                check(left==right,'sixth_power_masks','complete column identity')
    check(char(7*7**6,(13,))==char(7,(13,)),
          'sixth_power_masks','shared prime between c and d is allowed')


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--details',action='store_true')
    parser.add_argument('--mutation',choices=['full_family','lost_dual','upper_count',
        'omit_class','old_shift','wrong_block_weight','full_mollifier','zero_tail_gap','erased_mask'])
    args=parser.parse_args()
    mutation=args.mutation
    finite_moment_checks()
    masks(mutation)
    # These controls change an actual decisive finite-model input.
    if mutation=='lost_dual':
        r,q,y,v=3,F(1,3),F(3,4),F(1,2)
        nu=F(2,3)
        false=min(nu+2*y*v,M.k(v)+(2*y-1)*v)  # Dropped Q factor.
        true=min(nu+(2-2*y)*v,M.k(v)+(1-2*y)*v)
        check(false<=true,'mutation_gate','dual prefactor is indispensable')
    if mutation=='wrong_block_weight':
        v,y=F(1),F(3,4)
        wrong=M.k(v)  # Dropped V^(1-2y).
        check(wrong==M.k(v)+(1-2*y)*v,'mutation_gate','coefficient square weight')

    t,s,a,b=F(7,12),F(3,4),F(5,7),F(8,7)
    dt=M.density_terms('H',s,t,a,b)
    check(all(isinstance(x,F) for x in dt),'rational_contract','no floats in density')
    check(dt==independent_density(t,s,a,b),'holder_elimination','two independent reconstructions')
    check(max(dt)==F(5,7),'new_specializations','three-quarters density')
    check(F(43,60)-max(dt)==F(1,420),'new_specializations','gain over #966')
    check(F(395,552)-max(dt)==F(5,3864),'new_specializations','gain over #971')
    check(F(8,11)-max(dt)==F(1,77),'new_specializations','gain over DF')
    if mutation=='full_mollifier':
        # Retain hereditary numerator but replace its mollifier by full-family
        # U. At theta=7/12 the L0 term forces the weaker exponent 47/63.
        wrong=(t-s)*b+F(1,4)+F(1,2)
        check(wrong/F(3,4)<=F(5,7),'mutation_gate','full mollifier loses new density')

    rows=read_rows()
    check(len(rows)==112,'coverage','112 thresholds')
    check(rows[0]['sigma']==3*M.A_SCALE/2,'normalization','good threshold')
    check(rows[-1]['sigma']==F(19,20),'coverage','terminal threshold')
    for j,row in enumerate(rows):
        s,t,a,b=(row[k] for k in ('sigma','theta','A','B'))
        check(F(1,2)<=t<s<1 and 0<a<=b,'density_domains',f'threshold {j}')
        if j:check(rows[j-1]['sigma']<s,'coverage','strictly nested thresholds')
        terms=M.density_terms(row['method'],s,t,a,b)
        check(all(isinstance(x,F) for x in terms),'rational_contract',f'density {j}')
        check(len(terms)==(15 if row['method']=='H' else 10),'coverage','all detector monomials')
        if row['method']=='H':
            check(terms==independent_density(t,s,a,b),'holder_elimination',f'H reconstruction {j}')
        row['g']=max(terms)
        check(0<row['g']<1-M.EMAX,'density_domains','usable count exponent')
        for term in terms:
            check(term<=row['g'],'all_density_monomials',f'threshold {j}')

    one=(F(1),F(1)); half=(F(1,2),F(0)); z0=(M.ZLINE,F(0))
    domain_line((F(5),F(0)),(F(5),F(0)),(F(2),F(0)),'initial strict lines')
    domain_line(one,one,z0,'intermediate start')
    a,h,z=M.A_SCALE,1-M.A_SCALE,M.ZLINE
    budget((a/2,F(8,5),F(0)),'good')
    domain_line((rows[0]['sigma'],F(1)),one,z0,'good xi edge')
    domain_line((rows[0]['sigma'],F(1)),half,z0,'good central')
    details=[]; margins=[]; powers=[]
    indices=list(range(len(rows)-1))
    if mutation=='omit_class': indices.pop(42)
    for j in indices:
        row=rows[j]; x=rows[j+1]['sigma']; nu=row['g']; y=row['y']; r=row['r']
        if mutation=='upper_count': nu=rows[j+1]['g']
        check(nu==row['g'],'lower_count_upper_contour',f'class {j}')
        check(r in (2,3,4) and 0<y<1,'moment_domains',f'class {j}')
        m=M.mean(r,nu,y)
        if mutation=='full_family':
            # Revert the selected moment to its full-family version before Holder.
            m=(1-F(1,2*r))*nu+M.selected_kappa(r,F(1),y)/(2*r)
        c=x-1-a/2+a*y+h*m
        coeff=1+m-z+h
        check(isinstance(m,F) and isinstance(c,F),'rational_contract','moment arithmetic')
        check(m-z>0,'top_dyad_signs',f'class {j}')
        check(c<a/2,'constant_margins',f'class {j}')
        budget((c,coeff,F(1)),f'middle {j}')
        domain_line((x,F(1)),one,z0,f'class {j} xi edge')
        domain_line((x,F(1)),(y,F(0)),z0,f'class {j} w edge')
        margins.append(a/2-c);powers.append(m-z)
        details.append(dict(j=j,lower=row['sigma'],upper=x,g=nu,r=r,y=y,m=m,
                            constant=c,e_coefficient=coeff,e_squared=F(1),
                            margin=a/2-c))
    check(len(details)+2==113,'coverage','all middle classes plus good and terminal')
    check({d['j'] for d in details}==set(range(111)),'coverage','no omitted class')
    g=rows[-1]['g']
    check(g==F(11,47),'terminal_class','last density')
    m=g+F(1,2)
    last=(-a/2+h*m,1+a+(m-z)+h/2,F(1,2))
    check(last[0]==F(3433,16450),'terminal_class','last leading exponent')
    check(m-z>0,'top_dyad_signs','last class')
    budget(last,'last class')
    domain_line(one,(F(0),F(1)),z0,'last class')

    # Principal residues retain all connecting vertices.
    for yy,zz,name in [(one,(F(1,6),F(1)),'principal start'),
                      (half,(F(1,6),F(1)),'w remainder'),
                      ((F(1),F(0)),(F(1,6),F(1)),'w residue'),
                      ((F(1),F(0)),(F(0),F(1)),'z remainder')]:
        domain_line(one,yy,zz,name)
    budget((h/6,1+h,F(0)),'principal w')
    budget((a/2,1+h,F(0)),'principal z')
    small=h/3+F(11,1200)
    check(small<a/2,'small_frequency','separate z=1/3 needed')
    domain_line(one,half,(F(1,3),F(0)),'small frequency')
    budget((small,F(1),F(0)),'small frequency')

    for row in rows:
        s=row['sigma'];e=M.EMAX
        R,ro,rt,ri=2-s-e/4,2-s-e/2,2-s-e,1-e/4
        check(R>ro>rt>ri>0,'reciprocal_disks','strict radii')
        check(2-R>s and 2-ri>1,'reciprocal_disks','outer free, inner Euler')
    check(h+M.EMAX<F(3,5),'height_tails','upper U exponent')
    check(2+2*F(3,5)-F(600,100)<-1,'height_tails','coarse full-tail saving')
    gap=F(0) if mutation=='zero_tail_gap' else M.EMAX
    check(gap>0,'large_tail','strict positive cutoff gap')
    L=10/M.EMAX+2
    large=a/2+4+h*L+4*a+(h+M.EMAX)*(1-L)
    check(large==-5+7*a/2-M.EMAX,'large_tail','initial absolute lines x=y=5')
    check(large==F(-2457,700)-M.EMAX and large<-3,'large_tail','negative exponent')
    check(0<2*a<1,'normalization','subcritical physical support with diagonal')
    shift=F(121,175) if mutation!='old_shift' else F(103,150)
    check(shift==1-(a/2+h/6),'normalization','actual Mellin shift')
    check(shift+a/2==M.BOUND==F(633,700),'normalization','new half-plane')
    check(F(68,75)-M.BOUND==F(1,420),'normalization','gain over recovered packet')

    result=dict(status='finite exact checks only; analytic composition remains proposed',
                predicates=sum(COUNTS.values()),groups=dict(sorted(COUNTS.items())),
                thresholds=len(rows),classes=len(details)+2,
                density_methods=dict(sorted(Counter(x['method'] for x in rows).items())),
                middle_moment_orders=dict(sorted(Counter(x['r'] for x in details).items())),
                first_threshold=rows[0]['sigma'],terminal_threshold=rows[-1]['sigma'],
                minimum_middle_margin=min(margins),minimum_middle_row_power=min(powers),
                e_interval=['0 excluded',M.EMAX],boundary=M.BOUND,mellin_shift=shift,
                theta_exponent=a/2,density_at_three_quarters=F(5,7),
                strata_sha256=hashlib.sha256((ROOT/'strata.tsv').read_bytes()).hexdigest(),
                uses_floating_point=False,actual_L_values_computed=False,
                independent_analytic_review=False)
    if args.details:
        result['derived_classes']=details
        result['derived_density_choices']=rows
    print(json.dumps(strings(result),sort_keys=True,indent=2))


if __name__=='__main__':
    main()
