"""Independent finite selector, spectral-pressure and tilted-source controls.
These are synthetic algebra tests, not a cofinal Xi theorem or kernel build.
"""
import json, sys
from fractions import Fraction as Q
import sympy as sp

def need(ok, msg):
    if not ok: raise RuntimeError(msg)

def run():
    x=sp.symbols('x'); n=0
    f=1+x**4/4; p=sp.diff(f,x); q=sp.diff(p,x)
    r1=sp.residue(x**2*f/p,x,0)
    r2=sp.residue(3*x**4*f**2/(p*q),x,0)
    wrong=sp.residue(x**4*f**2/(p*q),x,0)
    need(r1==r2==1 and wrong==sp.Rational(1,3),'flat-turn selector');n+=3
    f=x**4/4-x**2/2+1;p=sp.diff(f,x);q=sp.diff(p,x)
    w2=sp.Rational(9,2)*x**4-sp.Rational(9,2)*x**2+1
    need(sp.rem(w2-1,p,x)==0,'critical congruence');n+=1
    need(sp.rem(w2,q,x)==0,'second-denominator cancellation');n+=1
    rho=[sp.cancel(f/q).subs(x,c) for c in [-1,0,1]]
    total=sum(sp.residue(w2*f**2/(p*q),x,c) for c in [-1,0,1])
    need(sum(rho)==-sp.Rational(1,4) and total==sum(v*v for v in rho)==sp.Rational(41,32),'second residue sum');n+=2
    # One-spike spectra attain the displayed sharp envelope when E<2.
    spectral=[]
    for m,a in [(4,Q(11,10)),(10,Q(6,5)),(280,Q(51,50))]:
        e=a*a+Q(a*a,m-1); delta=2*a-1+Q(a*a,m-1)
        need(e<2 and delta==e-(a-1)**2,'one-spike identity')
        need((Q(m-1,m)*e)==a*a,'sharp Cauchy equality');n+=2
        spectral.append({'m':m,'spike':str(a),'E':str(e),'Delta':str(delta)})
    # Reflected tilt majorants: arbitrary finite positive source, all sampled
    # e^{-y u} replaced by exact r**u in [0,1]. This is a finite control only.
    atoms=[1,2,4];weights=[Q(1,5),Q(1,2),Q(3,10)]
    mu=sum(w*u for u,w in zip(atoms,weights));var=sum(w*(u-mu)**2 for u,w in zip(atoms,weights))
    for r in [Q(1),Q(3,4),Q(1,2),Q(1,10)]:
        neg=sum(w*abs(1-Q(u,1)/mu)*r**u for u,w in zip(atoms,weights))
        deriv=sum(w*u*abs(1-Q(u,1)/mu)*r**u for u,w in zip(atoms,weights))
        need(neg*neg<=var/(mu*mu),'uniform reflected Cauchy bound')
        need(deriv*deriv<=var*(mu*mu+var)/(mu*mu),'reflected derivative bound');n+=2
    # Frozen lambda is essential; adjacent mean is strictly different.
    mu_next=sum(w*u*u for u,w in zip(atoms,weights))/mu
    need(mu_next-mu==var/mu and mu_next>mu,'tilted mean monotonicity');n+=2
    return {'verdict':'PASS_SELECTOR_AND_SPECTRAL_CONTROLS','exact_checks':n,
      'flat_turn_residues':[str(r1),str(r2)],'wrong_square_residue':str(wrong),
      'simple_second_moment':str(total),'spectral_fixtures':spectral,
      'cofinal_xi_bound_proved_by_checks':False,'rh_proved':False}
if __name__=='__main__':
    result=run();open(sys.argv[1],'w').write(json.dumps(result,indent=2,sort_keys=True)+'\n');print(result['verdict'],result['exact_checks'])
