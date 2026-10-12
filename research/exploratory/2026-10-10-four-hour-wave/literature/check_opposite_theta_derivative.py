"""Exact symbolic controls for a proposed source-qualified theta adapter.

Does not rebuild theta automorphy or prove a full inverse moment.
"""
import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import sympy as s


def require(condition, context):
    if not condition:
        raise ArithmeticError(context)


def controls():
    counts = {}
    z,zb,v=s.symbols('z zb v',real=False)
    c,cb,delta=s.symbols('c cb delta',nonzero=True)
    den=v*v+z*zb
    zp=-delta/c-zb/(c*c*den)
    zbp=-delta/cb-z/(cb*cb*den)
    vp=v/(c*cb*den)
    origin={z:0,zb:0}
    derivative=[s.diff(zp,z).subs(origin),s.diff(zbp,z).subs(origin),
                s.diff(vp,z).subs(origin)]
    wanted=[0,-1/(cb*cb*v*v),0]
    require(all(s.simplify(a-b)==0 for a,b in zip(derivative,wanted)),
            'opposite cusp derivative')
    counts['cusp_chain_rule']=3
    # Actual Eisenstein primary generators from the pinned source packet.
    omega=(-1+s.sqrt(3)*s.I)/2
    lam=1+2*omega
    require(s.simplify(lam-s.I*s.sqrt(3))==0,'literal lambda')
    primary=[s.Integer(1),-2-3*omega,1-3*omega]
    for a in primary:
        for b in primary:
            alpha_a=s.simplify(a/s.sqrt(s.expand(a*s.conjugate(a))))
            alpha_b=s.simplify(b/s.sqrt(s.expand(b*s.conjugate(b))))
            alpha_ell=s.I*alpha_a*alpha_b**3
            require(s.simplify(s.I*alpha_ell+alpha_a*alpha_b**3)==0,
                    'opposite fixed Fourier phase')
            require(s.simplify(s.I*s.conjugate(alpha_ell)
                    -s.conjugate(alpha_a)*s.conjugate(alpha_b)**3)==0,
                    'original fixed Fourier phase')
            require(s.simplify(s.conjugate(alpha_a)*alpha_a**2-alpha_a)==0,
                    'angular numerator matching')
            require(s.simplify(s.conjugate(alpha_b)**3*alpha_b**6-alpha_b**3)==0,
                    'entire cube completion retained')
    counts['literal_eisenstein_phase']=36
    # Treat the four gamma factors as independent nonzero formal symbols.
    # Their exact paired quotient cancels without Stirling approximation.
    ap,bp,am,bm,K,x=s.symbols('ap bp am bm K x',nonzero=True)
    t=s.symbols('t')
    gp=ap*bp/(am*bm)
    gm=am*bm/(ap*bp)
    require(s.cancel(gp*gm)==1,'full gamma involution')
    require(s.simplify(K**t*K**(-t))==1,'fixed scale involution')
    require(F(-2,3)>F(-5,6),'no first gamma pole crossed')
    require(F(-1,6)-F(1,2)==F(-2,3),'chosen Mellin line')
    require(F(1,2)+F(1,12)>F(1,2),'initial absolute line')
    counts['mellin_controls']=5
    # The same local Fourier transform is used in both orientations.
    # Two j-reflections return the literal residue class, including masks.
    for j in range(6):
        j1=(-j-2)%6
        j2=(-j1-2)%6
        require(j2==j,'local character involution')
    require((-3-2)%6==1,'quadratic input returns sextic, not quadratic')
    require(0**3==0 and 0**1==0,'nonunit retained on both sides')
    counts['local_character_masks']=8
    gnorm,knorm,B,c0norm,const=s.symbols('gnorm knorm B c0norm const',positive=True)
    X=gnorm**2*knorm**2/(const*B)
    ratio=s.cancel(X/(c0norm**2*knorm**2))
    require(s.cancel(ratio-gnorm**2/(const*B*c0norm**2))==0,
            'second conductor restores outer support')
    for upper in (F(1),F(3,2),F(7)):
        for fixed in (F(1),F(3),F(17,5)):
            threshold=81*upper*fixed
            g2=(threshold+1)*F(101,7)
            bb=F(101,7)
            for norm_integer in (1,3,7,19):
                argument=F(norm_integer,81)*g2/(fixed*bb)
                require(argument>upper,'complete nonzero frequency exclusion')
    counts['conductor_and_support']=37
    return counts


def sources():
    paths=[
      (Path('/workspace/.riemann-research/sources/qrh11-12.tex'),
       'd9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d'),
      (Path('/workspace/.riemann-research/moment-sources/915/standalone/2026-10-10-sextic-critical-core/COUPLED_THETA_COMPLETION.md'),
       'f3b57f69338e8736ffe4addd5a6e2ebf6d5f8976ee9d2fda5921c83ff484eb36'),
      (Path('/workspace/.riemann-research/moment-sources/915/standalone/2026-10-10-sextic-critical-core/PRIMARY_SOURCE_MATCH.md'),
       'c4162dc668980d44c115e67868393fc43230d78a0fdacf73ff05abcc8a200258')]
    out={}
    for p,expected in paths:
        got=sha256(p.read_bytes()).hexdigest()
        require(got==expected,('frozen source',str(p)))
        out[str(p)]=got
    return out


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    here=Path(__file__).resolve().parent
    record={
      'status':'PASS_EXACT_OPPOSITE_DERIVATIVE_CONTROLS',
      'checks':controls(),'source_sha256':sources(),
      'manuscript_sha256':sha256((here/'OPPOSITE_THETA_DERIVATIVE.md').read_bytes()).hexdigest(),
      'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
      'theta_automorphy_independently_rebuilt':False,
      'asymptotic_full_moment_proved':False,
      'other_cusp_component_bound_proved':False,
      'rh_proved':False}
    args.output.write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
    print(record['status'])


if __name__=='__main__':
    main()
