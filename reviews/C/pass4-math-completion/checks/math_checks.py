#!/usr/bin/env python3
"""Independent bounded exact controls for C4; no upstream producer is imported.

Requires SymPy. Infinite analytic arguments and actual source completeness are
NOT proved by this executable. Acceptance never uses Python assertions.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import itertools
import json
from pathlib import Path
import sys
import sympy as sp

SCHEMA = 'riemann.review.C4.math-controls.v1'
SCOPE = {
    'arithmetic': 'EXACT_RATIONAL_AND_SYMBOLIC',
    'actual_zero_census': False,
    'lean_compiled': False,
    'rh_proved': False,
    'infinite_analytic_proofs_machine_checked': False,
}


def require(value: bool, message: str) -> None:
    if not value:
        raise ValueError(message)


def pairs_no_duplicates(pairs):
    d = {}
    for k, v in pairs:
        if k in d:
            raise ValueError('duplicate JSON key: ' + k)
        d[k] = v
    return d


def canonical(obj) -> str:
    return json.dumps(obj, sort_keys=True, separators=(',', ':'), ensure_ascii=False)


def read_result(path: Path):
    d = json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=pairs_no_duplicates)
    require(type(d) is dict and set(d) == {'schema', 'scope', 'groups', 'constants'}, 'result schema')
    require(d['schema'] == SCHEMA, 'schema identifier')
    require(canonical(d['scope']) == canonical(SCOPE), 'exact scope mismatch')
    require(type(d['groups']) is dict and len(d['groups']) == 8, 'group inventory')
    for k, v in d['groups'].items():
        require(type(k) is str and type(v) is int and v > 0, 'count type/value')
    require(type(d['constants']) is dict, 'constants type')
    return d


def log_interval(x: F, n: int = 24):
    require(type(n) is int and n > 0 and x >= 1, 'log interval domain')
    z = (x - 1) / (x + 1)
    lo = 2 * sum((z ** (2*k+1) / (2*k+1) for k in range(n)), F(0))
    tail = 2 * z ** (2*n+1) / ((2*n+1) * (1-z*z))
    return lo, lo+tail


def atan_interval(x: F, n: int):
    require(0 < x < 1 and type(n) is int and n > 0, 'atan interval domain')
    val = sum(((-1)**k*x**(2*k+1)/F(2*k+1) for k in range(n)), F(0))
    nxt = val + (-1)**n*x**(2*n+1)/F(2*n+1)
    return min(val, nxt), max(val, nxt)


def energy(j):
    return j[0]*j[2]-2*j[1]*j[1]


def plus(*jets):
    return tuple(sum((j[k] for j in jets), F(0)) for k in range(3))


def scale(a, j):
    return tuple(a*x for x in j)


def critical(t, gamma, m=1):
    v = t+gamma*gamma
    return (2*m/v, -2*m/v**2, 4*m/v**3)


def off(t, a, b, m=1):
    u=t+b*b-a*a; B=2*a*b; den=u*u+B*B
    return (4*m*u/den, 4*m*(B*B-u*u)/den**2,
            8*m*u*(u*u-3*B*B)/den**3)


def det3(A):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
            - A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
            + A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))


def symbolic_controls():
    n=0
    def zero(expr, label):
        nonlocal n
        require(sp.cancel(expr) == 0, label); n += 1
    z,L=sp.symbols('z L')
    zero(z*(z-1)*(L-1/z-1/(1-z))/2 - (sp.Rational(1,2)+z*(z-1)*L/2), 'entire xi normalization')
    zero((1-z)*((1-z)-1)-z*(z-1), 'functional-equation coefficient')
    t,c,B,m,V=sp.symbols('t c B m V')
    U=t+c; q=4*m*U/(U*U+B*B); r=2/(t+V)
    zero(q*sp.diff(q,t,2)-2*sp.diff(q,t)**2+32*m*m*B*B/(U*U+B*B)**3, 'off-line energy')
    zero(r*sp.diff(r,t,2)-2*sp.diff(r,t)**2, 'critical energy')
    zero(sp.diff(t*q,t)-4*m*(c*U**2+(2*t+c)*B**2)/(U*U+B*B)**2, 'tp first')
    zero(sp.diff(t*q,t,2)+8*m*(c*U**3+3*t*U*B**2-B**4)/(U*U+B*B)**3, 'tp second')
    u,s,k=sp.symbols('u s k')
    bb=k*s*s*u*u; den=u*u+bb; v=u*(1-s)
    qj=(4*m*u/den, 4*m*(bb-u*u)/den**2, 8*m*u*(u*u-3*bb)/den**3)
    rj=(2/v,-2/v**2,4/v**3)
    cross=qj[0]*rj[2]+rj[0]*qj[2]-4*qj[1]*rj[1]
    Q=1-k+3*k*s*(2-s)+k*k*s*s*(3-2*s)
    zero(cross-16*m*s*s*Q/(u**4*(1+k*s*s)**3*(1-s)**3), 'one-orbit cross')
    a,b,d,e,f,g=sp.symbols('a b d e f g')
    cross=a*g+e*d-4*b*f
    zero(a*e*cross-a*a*(e*g-2*f*f)-e*e*(a*d-2*b*b)-2*(e*b-a*f)**2, 'cross-square certificate')
    vals=sp.symbols('v0:3'); ds=sp.symbols('d0:3'); es=sp.symbols('e0:3')
    A=sum(vals)
    rhs=A*sum((vals[i]*es[i]-2*ds[i]**2)/vals[i] for i in range(3))
    rhs += 2*sum(vals[i]*vals[j]*(ds[i]/vals[i]-ds[j]/vals[j])**2 for i in range(3) for j in range(i+1,3))
    zero(A*sum(es)-2*sum(ds)**2-rhs, 'n-term energy decomposition')
    x,y,z,p,q,r=sp.symbols('x y z p q r')
    l12=x+y; l13=x+z; l23=y+z
    n12=x*p+y*q; n13=x*p+z*r; n23=y*q+z*r
    zero(p*q-n12*n12/l12**2-(p-q)*(y*y*q-x*x*p)/l12**2, 'Pick two')
    D=l12**2*l13**2*l23**2
    detD=p*q*r*D+2*n12*n13*n23*l12*l13*l23-p*n23**2*l12**2*l13**2-q*n13**2*l12**2*l23**2-r*n12**2*l13**2*l23**2
    ta=x*x; tb=y*y; tc=z*z
    AA=p*q*(ta-tb)-p*r*(ta-tc)+q*r*(tb-tc)
    BB=ta*p*(tb-tc)+tb*q*(tc-ta)+tc*r*(ta-tb)
    require(sp.Poly(sp.expand(detD-AA*BB),x,y,z,p,q,r).is_zero, 'Pick three polynomial'); n += 1
    x,C=sp.symbols('x C')
    zero(((x+sp.Rational(1,4))**2-C*(x+sp.Rational(1,4)))/(x+sp.Rational(9,4))-(x-C-sp.Rational(7,4)+(4+2*C)/(x+sp.Rational(9,4))), 'frequency division')
    # Local affine factorization for arbitrary finite multiplicities.
    w,rho,a=sp.symbols('w rho a')
    for mult in range(1,6):
        s0=rho-sp.Rational(1,2)
        f=(w+sp.Rational(1,2)-rho)**mult*(2+w+sp.Rational(1,2)-rho)
        zero(f-(w-s0)**mult*(2+w-s0), 'shifted pole factor')
    return n


def interval_controls():
    ln2=log_interval(F(2)); ln3=log_interval(F(3))
    at5=atan_interval(F(1,5),24); at239=atan_interval(F(1,239),8)
    pi=(16*at5[0]-4*at239[1],16*at5[1]-4*at239[0])
    q3=ln2[1]/F(707,500)+ln3[1]/F(433,250)
    h32=sum((F(1,k) for k in range(1,33)),F(0))
    gamma_hi=h32-5*ln2[0]
    s92=sum((F(4,4*k+1) for k in range(93)),F(0))
    s152=sum((F(4,4*k+1) for k in range(153)),F(0))
    vals=[pi[0]>3,pi[1]<F(22,7),ln2[0]>F(2,3),ln2[1]<F(7,10),
          ln3[1]<F(11,10),log_interval(F(22,7))[1]<F(6,5),
          F(707,500)**2<2,F(433,250)**2<3,q3<F(9,8),gamma_hi<F(3,5),
          s92>F(35,4),s152>F(37,4),9*102**2>2*46665+F(7,2),
          F(3,2)*(1-F(17205*4+7,4*93636))>=F(6,5),
          F(9,4)/F(6,5)==F(15,8),F(18,32)+F(18,1024)==F(297,512),
          F(297,512)<1, F(1,6)+ln2[1]/3<F(2,5)]
    for v in vals: require(v,'rational source constant')
    return len(vals), {'q3_upper':str(q3),'gamma_upper':str(gamma_hi),
                       'S92':str(s92),'S152':str(s152),'reserve_budget_upper':'297/512',
                       'remaining_reserve_lower':'215/512','schur_constant_general':'3',
                       'schur_constant_L1':'15/8'}


def orbit_controls():
    count=0; H=F(1024)
    for a,b,gamma,m,t in itertools.product([F(1,10),F(1,4),F(49,100)],
            [F(1025),F(2048)], [F(1),F(32),F(512)], [1,2,7],
            [F(0),F(1,100),F(1,4),F(1),F(100)]):
        c=b*b-a*a; B=2*a*b; d=c-gamma*gamma; kap=B*B/d**2
        eps=2*m*kap/(1-kap); q=off(t,a,b,m); r=critical(t,gamma)
        require(d>=F(2,3)*b*b and 0<=kap<F(1,2), 'orbit geometry')
        require(eps<=9*m/b**2 and eps>=0,'share bound')
        require(energy(plus(q,scale(eps,r)))>=0,'paid orbit')
        require(q[1]<0 and q[0]+t*q[1]>0 and 2*q[1]+t*q[2]<0,'companion signs')
        count+=1
    return count


def prefix_pick_controls():
    count=0
    off_data=[(F(1,4),F(1025),1),(F(1,10),F(2048),2)]
    for t in [F(0),F(1,100),F(1,4),F(1),F(9)]:
        R=critical(t,F(1)); selected=scale(3,R)
        for n in range(3):
            shares=[]; qs=[]
            for a,b,m in off_data[:n]:
                d=b*b-a*a-1; kap=(2*a*b)**2/d**2
                shares.append(2*m*kap/(1-kap)); qs.append(off(t,a,b,m))
            raw=plus(selected,critical(t,F(2),2),*qs)
            paid=plus(scale(1-sum(shares,F(0)),R),scale(2,R),critical(t,F(2),2),
                      *(plus(q,scale(e,R)) for q,e in zip(qs,shares)))
            require(raw==paid and energy(raw)>=0 and raw[0]>0,'exact prefix')
            count+=1
    nodes=[F(1,10),F(1,2),F(1),F(2),F(4)]
    # Three distinct source models: empty, one, and two off-line atoms.
    for n in range(3):
        def p(x):
            return plus(critical(x*x,F(1)),*(off(x*x,a,b,m) for a,b,m in off_data[:n]))[0]
        for xs in itertools.product(nodes,repeat=3):
            ps=[p(x) for x in xs]
            K=[[(xs[i]*ps[i]+xs[j]*ps[j])/(xs[i]+xs[j]) for j in range(3)] for i in range(3)]
            require(all(K[i][i]>0 for i in range(3)),'Pick diagonals')
            require(all(K[i][i]*K[j][j]-K[i][j]**2>=0 for i in range(3) for j in range(i+1,3)),'Pick pairs')
            require(det3(K)>=0,'Pick triple')
            if len(set(xs))<3: require(det3(K)==0,'duplicate-node pullback')
            count+=1
    return count


def spectral_validate(expected, observed, selected):
    require(type(expected) is dict and type(observed) is list,'spectral schema')
    require(selected in expected and expected[selected][0]=='critical','selected orbit')
    found={}
    for o in observed:
        if o is None: continue
        require(type(o) is dict and set(o)=={'key','kind','multiplicity','selected'},'atom fields')
        key=o['key']; require(type(key) is str and key in expected,'actual completeness target')
        require(key not in found,'duplicate location')
        require(type(o['multiplicity']) is int and o['multiplicity']>=1,'multiplicity type')
        require(type(o['selected']) is bool,'selected type')
        require((o['kind'],o['multiplicity'])==expected[key],'multiplicity correspondence')
        require(o['selected']==(key==selected),'selected disjointness')
        found[key]=True
    require(set(found)==set(expected),'missing actual atom')


def enumeration_controls():
    count=0
    expected={'g1':('critical',1),'o1':('off_line',2)}
    good=[{'key':'g1','kind':'critical','multiplicity':1,'selected':True},None,
          {'key':'o1','kind':'off_line','multiplicity':2,'selected':False}]
    spectral_validate(expected,good,'g1'); count+=1
    spectral_validate({'g1':('critical',1)},[good[0],None,None],'g1'); count+=1
    import copy
    cases=[]
    cases.append(good[:-1]); cases.append(good+[good[0]])
    a=copy.deepcopy(good); a[-1]['multiplicity']=1; cases.append(a)
    a=copy.deepcopy(good); a[-1]['selected']=True; cases.append(a)
    a=copy.deepcopy(good); a[0]['multiplicity']=True; cases.append(a)
    a=copy.deepcopy(good); a[-1]['key']='invented'; cases.append(a)
    a=copy.deepcopy(good); a[0]['extra']=0; cases.append(a)
    cases.append([None,None]); cases.append([])
    for case in cases:
        try: spectral_validate(expected,case,'g1')
        except ValueError: count+=1
        else: raise ValueError('bad spectral contract accepted')
    return count


def mellin_controls():
    count=0
    for q in [F(1,4),F(1,2),F(2,3)]:
        totals=[1/(1-q),1/(1-q)**2,(1+q)/(1-q)**3]
        for j in range(3):
            for N in range(21):
                part=sum((F(k+1)**j*q**k for k in range(N+1)),F(0))
                require(part<totals[j],'positive domination series')
                count+=1
    # A finite Taylor test never replaces Tonelli: these are only indexing controls.
    for n in range(12):
        for y in [F(0),F(1,4),F(1),F(2)]:
            term=y**n/F(__import__('math').factorial(n))
            require(term>=0,'Landau Taylor sign'); count+=1
    return count


def schur_controls():
    count=0
    for M in range(1,31):
        mass=sum((F(1,4**j) for j in range(1,M+1)),F(0))
        require(mass==(1-F(1,4**M))/3,'compact model sum')
        for C in [F(1,4),F(1,3),F(1,2)]:
            SM=C-mass; S=C-F(1,3)
            require(SM-S==F(1,3*4**M),'Galerkin upper gap')
            count+=1
        require(F(1,2)-M<0,'unbounded energy coupling witness'); count+=1
    for n in range(1,9):
        A=sp.diag(1,2,4)
        B=sp.Matrix([[sp.Rational(n,3),sp.I/2],[1,sp.Rational(n,7)],[sp.I,1]])
        C=sp.Matrix([[2,sp.I/3],[-sp.I/3,3]])
        V=sp.Matrix([[sp.Rational(n,11),0],[sp.I/5,sp.Rational(1,7)],[0,sp.Rational(n,13)]])
        S=C-B.conjugate().T*A.inv()*B
        U=C-B.conjugate().T*V-V.conjugate().T*B+V.conjugate().T*A*V
        R=B-A*V
        err=R.conjugate().T*A.inv()*R
        require(all(sp.simplify(x)==0 for x in U-S-err),'Schur residual matrix identity')
        bound=R.conjugate().T*R-err
        require(sp.simplify(bound[0,0])>=0 and sp.simplify(bound[1,1])>=0 and sp.simplify(bound.det())>=0,'full Hermitian residual bound')
        count+=1
    return count


def source_contract_controls():
    # Exact zero/fixed-point and additive vs multiplicative source controls.
    count=0
    for x in [F(-3),F(0),F(1,4),F(1,2),F(1),F(3)]:
        require((1-x)*(-x)==x*(x-1),'reflection polynomial'); count+=1
    for q in [F(0),F(1,2),F(7)]:
        require(F(1,2)+F(0)*q==F(1,2),'removable endpoint'); count+=1
    for n in range(12):
        tail=sum((F(1,1024**2*4**(j+1)) for j in range(n)),F(0))
        require(tail==(1-F(1,4**n))/F(3*1024**2),'infinite model finite prefixes'); count+=1
    return count


def compute():
    c, constants=interval_controls()
    groups={'symbolic_identities':symbolic_controls(),'rational_constant_certificates':c,
            'one_orbit_parameter_fixtures':orbit_controls(),
            'prefix_and_pick_packets':prefix_pick_controls(),
            'spectrum_contract_fixtures':enumeration_controls(),
            'mellin_domination_fixtures':mellin_controls(),
            'schur_and_energy_fixtures':schur_controls(),
            'source_normalization_fixtures':source_contract_controls()}
    return {'schema':SCHEMA,'scope':SCOPE,'groups':groups,'constants':constants}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--write',type=Path)
    parser.add_argument('--check',type=Path)
    args=parser.parse_args()
    old=read_result(args.check) if args.check else None
    result=compute()
    if old is not None:
        require(canonical(old)==canonical(result),'reconstructed result mismatch')
    if args.write: args.write.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n',encoding='utf-8')
    print(canonical({'status':'PASS_C4_BOUNDED_MATH_CONTROLS','groups':result['groups'],
                     'total_fixtures':sum(result['groups'].values()),'rh_proved':False}))

if __name__=='__main__':
    try: main()
    except (ValueError, OSError, json.JSONDecodeError) as e:
        print('REJECT: '+str(e),file=sys.stderr); sys.exit(2)
