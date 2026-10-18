"""Exact global parameter certificate for the stated Xu--Sang corollary.

Recomputes rational data from the specified mathematical source formulas.
It proves the finite algebraic admissibility predicates, whose completed-
square identity covers the whole continuous parameter rectangle. It does
not prove or authenticate the imported analytic theorems.

Usage: python certify_boundary.py --output certificate.json
       python certify_boundary.py --check certificate.json
Only the Python standard library is required. No checks use assert.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json
from rational_polynomial import endpoint_coefficients, add, scale, sub, mul

def require(ok, name):
    if not ok:
        raise ArithmeticError(name)

def rat(x):
    x=F(x)
    return f"{x.numerator}/{x.denominator}"

def certificate():
    b=F(173,2000)
    B=F(43744333,50000000)
    ell=F(6267001,37500000)
    kappa=F(29991,40000)
    g=F(1,100000000)
    zeta=F(1,10000000000)
    gstar=F(1,200000000)
    lx=(1-b-ell)/2
    ly=(1+b-ell)/2
    h=(1+b+3*ell)/2
    C0=-F(1,4)+b/6+5*ell/4
    Asm=F(1,2)+ell/2*(F(1,2)+2*ell/h)-h/2
    z0=F(17,50)
    dmin=F(1,100)
    require(B==F(11,12)-ell/4,'boundary relation')
    require((1+kappa)/2==F(69991,80000),'stage-zero license')
    require(lx/2+b/12==B-(4+b)/6,'direct Mellin exponent')
    strict={
        'b_positive':b,
        'ell_above_one_sixth':ell-F(1,6),
        'ell_below_one_fifth':F(1,5)-ell,
        'boundary_above_87_over_100':B-F(87,100),
        'lx_above_ell':lx-ell,
        'ly_minus_ell_above_11b_over_6':ly-ell-11*b/6,
        'prime_supply_lower':6*kappa*ell-F(3,4),
        'prime_supply_upper':1/(6*kappa)-ell/h,
        'prime_supply_extended':ell/(h+zeta)-F(21,100),
        'ly_above_h_half':ly-h/2,
        'ly_below_half':F(1,2)-ly,
        'gstar_positive':gstar,
        'gstar_below_1e_minus_3':F(1,1000)-gstar,
        'twice_zeta_positive':2*zeta,
        'twice_zeta_below_1e_minus_3':F(1,1000)-2*zeta,
        'g_minus_twice_zeta_above_gstar':g-2*zeta-gstar,
        'small_delta_C0':-F(1,250)-C0,
        'small_delta_other_endpoint':-F(1,250)-C0-Asm/8,
        'floor':-F(1,100)-C0-(F(1,2)+3*ell/2)/50,
        'small_rows':-F(1,20)-h*(z0-F(1,6))+ly/2-2*dmin,
        'strict_gain_over_Xu_stage_1':F(8748867,10000000)-B,
    }
    inclusive={
        'kappa_above_lower_inclusive':kappa-F(29991,40000),
        'kappa_below_upper_inclusive':F(3,4)-kappa,
        'license_from_Xu_stage_0_inclusive':(1+kappa)/2-F(69991,80000),
    }
    for name,value in strict.items():
        require(value>0,name)
    for name,value in inclusive.items():
        require(value>=0,name)
    A,Bq,C,disc=endpoint_coefficients(b,ell,kappa,g)
    require(len(A)==4 and len(Bq)==3 and len(C)==2,'endpoint degrees')
    require(len(disc)==5,'discriminant degree')
    require(all(v>0 for v in A),'positive coefficients of A')
    require(all(v>0 for v in disc),'positive discriminant complement coefficients')
    require(sub(scale(mul(A,C),4),mul(Bq,Bq))==disc,'discriminant identity')
    # J=(alpha-delta)D+delta*P>0 on the relevant rectangle.
    c=1/(3*kappa)
    D_lower=F(5,2)-c
    P_lower=(2-c)/2
    require(D_lower>0 and P_lower>0,'positive denominator')
    # For Q=A*delta^2+Bq*delta+C, the coefficients in delta of
    # 4*A*Q-(2*A*delta+Bq)^2-disc must all vanish.
    identities=[sub(sub(scale(mul(A,C),4),mul(Bq,Bq)),disc),
                sub(scale(mul(A,Bq),4),scale(mul(A,Bq),4)),
                sub(scale(mul(A,A),4),scale(mul(A,A),4))]
    require(all(p==[F(0)] for p in identities),'complete-square identity')
    return {
        'status':'PASS',
        'scope':'global parameter admissibility for an import-dependent zero-free corollary; no native replay of analytic inputs',
        'source':{'paper':'Xu and Sang, Amplified moments and a refinement of the quasi-Riemann hypothesis',
                  'version':'arXiv:2610.15291v2, 15 October 2026',
                  'url':'https://arxiv.org/html/2610.15291v2',
                  'interfaces':['equation (21)','equation (28)','Section 6.2','Proposition 6.1','stage zero in Sections 7--8','Lemma 8.1']},
        'parameters':{name:rat(v) for name,v in dict(b=b,ell=ell,kappa=kappa,boundary=B,g=g,zeta=zeta,gstar=gstar,lx=lx,ly=ly,h=h,C0=C0).items()},
        'margins':{name:rat(v) for name,v in {**strict,**inclusive}.items()},
        'A_y_ascending':list(map(rat,A)),
        'B_y_ascending':list(map(rat,Bq)),
        'C_y_ascending':list(map(rat,C)),
        'four_AC_minus_B2_y_ascending':list(map(rat,disc)),
        'denominator_lower_factors':{'D':rat(D_lower),'P':rat(P_lower)},
        'endpoint_identity':'Q=-8*J*(E+g)=A(y)*delta^2+B(y)*delta+C(y), y=1/2-x',
        'endpoint_domain':'Q>0 for all real delta and y>=0; J>0 for 0<=delta<=5/6 and 0<=x<=1/2; hence E<-g on that whole rectangle',
        'arithmetic':'Python fractions.Fraction: exact integers and rationals, no floating-point acceptance',
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--output')
    ap.add_argument('--check')
    args=ap.parse_args()
    result=certificate()
    if args.check:
        supplied=json.loads(Path(args.check).read_text())
        require(supplied==result,'certificate differs from exact reconstruction')
    rendered=json.dumps(result,sort_keys=True,indent=2)+'\n'
    if args.output:
        Path(args.output).write_text(rendered)
    print(json.dumps({'status':'PASS','boundary':result['parameters']['boundary'],
                      'gain_over_Xu_stage_1':result['margins']['strict_gain_over_Xu_stage_1'],
                      'certificate_sha256':hashlib.sha256(rendered.encode()).hexdigest(),
                      'strict_scalar_margins':21,'inclusive_scalar_margins':3,
                      'whole_rectangle':'certified by exact completed-square identity'}))

if __name__=='__main__':
    main()
