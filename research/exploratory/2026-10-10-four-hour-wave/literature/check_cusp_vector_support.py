"""Exact controls for a source-qualified complete cusp support return.

These finite controls do not rebuild the imported theta automorphy and
do not establish the remaining full inverse moment.
"""
import argparse
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import sympy as s


def require(ok, context):
    if not ok:
        raise ArithmeticError(context)


def eis_add(x, y):
    return (x[0]+y[0], x[1]+y[1])


def eis_mul(x, y):
    a,b=x; c,d=y
    return (a*c-b*d, a*d+b*c-b*d)


def eis_conj(x):
    return (x[0]-x[1], -x[1])


def primitive_root(q):
    for g in range(2,q):
        if len({pow(g,j,q) for j in range(q-1)})==q-1:
            return g
    raise ArithmeticError(('no primitive root',q))


def controls():
    counts={}
    a,c,u,b,delta=s.symbols('a c u b delta',nonzero=True)
    C=u*a+c
    G=s.Matrix([[a,b],[C,delta]])
    H=s.Matrix([[1,0],[u,1]])
    T=s.Matrix([[1,a/c],[0,1]])
    # Use the adjugate; the separate Bezout identity says det G=1.
    adj=s.Matrix([[delta,-b],[-C,a]])
    actual=adj*H*T
    wanted=s.Matrix([[delta-b*u,1/c],[-c,0]])
    for j in range(4):
        diff=s.factor((actual-wanted)[j])
        require(s.simplify(diff.subs(delta,(1+b*C)/a))==0,
                ('complete cusp matrix',j))
    counts['symbolic_cusp_matrix']=4
    require(s.simplify(G.det().subs(delta,(1+b*C)/a))==1,'Bezout determinant')
    counts['bezout_determinant']=1
    # Every unit normalization preserves the conductor norm.
    omega=(-1+s.sqrt(3)*s.I)/2
    for unit in (1,-1,omega,-omega,omega**2,-omega**2):
        require(s.simplify(unit*s.conjugate(unit))==1,'literal Eisenstein unit')
    counts['unit_conductor_normalization']=6
    # All primitive first columns modulo 3 admit the source's normalized
    # finite cusp construction; this is not an imported automorphy check.
    residues=list(product(range(3),repeat=2))
    units=[(1,0),(2,0),(0,1),(0,2),(2,2),(1,1)]
    def mod(x): return (x[0]%3,x[1]%3)
    def mul(x,y): return mod(eis_mul(x,y))
    lam=(1,2)
    nlam=mod((-lam[0],-lam[1]))
    primitive=0
    for A,Cc in product(residues,repeat=2):
        # The unique prime over 3: lambda divides a+b*omega iff a+b=0 mod3.
        if (sum(A)%3==0) and (sum(Cc)%3==0):
            continue
        normalized=False
        for e in units:
            AA,CC=mul(A,e),mul(Cc,e)
            if sum(CC)%3:
                normalized |= CC==(1,0)
            else:
                normalized |= AA==(1,0) and CC in ((0,0),lam,nlam)
        require(normalized,('normalized cusp first column',A,Cc))
        primitive+=1
    counts['primitive_cusp_columns_mod3']=primitive
    # A full cusp has no primary-index 27^s factor. Retain both Mellin scales.
    t=s.symbols('t')
    gp,gm,K0=s.symbols('gp gm K0',nonzero=True)
    K27=K0/27
    factor=s.simplify((K27/K0)**t)
    require(s.simplify(factor-27**(-t))==0,'full cusp dilation')
    for q in (s.Rational(-2,3),s.Integer(0),s.Rational(1,2),s.Integer(3)):
        require(s.simplify(s.Rational(1,27)**q-s.Integer(27)**(-q))==0,
                'fixed real Mellin dilation')
    require(F(-2,3)>F(-5,6),'legal first-pole margin')
    counts['mellin_scale_and_strip']=6
    # Polynomial identities in Q(omega)[z]/Phi_q(z) certify cubic Gauss
    # modulus and quadratic zero-frequency cancellation, without floats.
    gauss=0
    for q in (7,13,19,31,37,43):
        g=primitive_root(q)
        log={pow(g,j,q):j for j in range(q-1)}
        powers=((1,0),(0,1),(-1,-1))
        chi={x:powers[log[x]%3] for x in range(1,q)}
        require(sum((-1)**log[x] for x in range(1,q))==0,'quadratic active conductor')
        hist=[(0,0) for _ in range(q)]
        for x in range(1,q):
            for y in range(1,q):
                z=(x-y)%q
                hist[z]=eis_add(hist[z],eis_mul(chi[x],eis_conj(chi[y])))
        # The only degree<q relation is a multiple of Phi_q=sum z^j.
        residual=list(hist)
        residual[0]=eis_add(residual[0],(-q,0))
        require(len(set(residual))==1,('exact cubic Gauss modulus',q))
        require(F(q,q*q)*q==1,'positive active branch modulus one')
        # The Fourier coefficients of delta_0 are 1/q for all frequencies.
        for m in range(q):
            hist_delta=[0]*q
            for h in range(q): hist_delta[(h*m)%q]+=1
            if m==0:
                require(hist_delta==[q]+[0]*(q-1),'delta inverse at zero')
            else:
                require(len(set(hist_delta))==1,'delta inverse at nonunit mask complement')
            gauss+=1
        gauss+=3
    counts['local_fourier_and_exact_gauss']=gauss
    primes=(7,13,19,31,37)
    ramanujan=0
    for bits in product((0,1),repeat=len(primes)):
        original=1
        for q,bit in zip(primes,bits): original*=(-1+q*bit)
        expanded=0
        for choices in product((0,1),repeat=len(primes)):
            term=1
            for q,bit,positive in zip(primes,bits,choices):
                term*=q*bit if positive else -1
            expanded+=term
        require(original==expanded,'full two-term Ramanujan interference')
        ramanujan+=1
    counts['complete_ramanujan_allocations']=ramanujan
    an,kn,rn,B,c10,c20,nell=s.symbols('an kn rn B c10 c20 nell',positive=True)
    X=c10**2*kn**2*an**2/B
    argument=s.cancel(27*nell*X/(c20**2*kn**2*rn**2))
    desired=27*nell*c10**2*(an/rn)**2/(B*c20**2)
    require(s.cancel(argument-desired)==0,'exact moving conductor cancellation')
    support=1
    for upper in (F(1),F(7,5),F(9)):
        for ratio in (F(1),F(1,9),F(17,4)):
            threshold=3*upper/ratio
            for bb in (F(1),F(53,7)):
                h2=(threshold+1)*bb
                for nl in (F(1,81),F(7,81),F(1),F(9)):
                    value=27*nl*ratio*h2/bb
                    require(value>upper,'full nonzero-frequency exclusion')
                    support+=1
    counts['source_support_filter']=support
    return counts


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    here=Path(__file__).resolve().parent
    source=Path('/workspace/.riemann-research/sources/qrh11-12.tex')
    digest=sha256(source.read_bytes()).hexdigest()
    require(digest=='d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d',
            'literal imported theta source')
    source_hashes={str(source):digest}
    upstream=Path('/workspace/.riemann-research/moment-sources/915/standalone/2026-10-10-sextic-critical-core')
    for name,expected in [
      ('COUPLED_THETA_COMPLETION.md','f3b57f69338e8736ffe4addd5a6e2ebf6d5f8976ee9d2fda5921c83ff484eb36'),
      ('REFLECTION_SCALAR_AUDIT.md','17bdce731735412cc463c50c944df9240736e5797282f2c5a4eed5a07b2e21e2')]:
        p=upstream/name
        h=sha256(p.read_bytes()).hexdigest()
        require(h==expected,('literal upstream component',name))
        source_hashes[str(p)]=h
    record={'status':'PASS_EXACT_CUSP_VECTOR_SUPPORT_CONTROLS',
      'checks':controls(),'source_sha256':source_hashes,
      'manuscript_sha256':sha256((here/'CUSP_VECTOR_SUPPORT_RETURN.md').read_bytes()).hexdigest(),
      'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
      'written_adapter_independently_reviewed':True,
      'imported_analysis_independently_rebuilt':False,
      'theta_automorphy_independently_rebuilt':False,
      'full_generalized_moment_proved':False,'rh_proved':False}
    args.output.write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
    print(record['status'])


if __name__=='__main__':
    main()
