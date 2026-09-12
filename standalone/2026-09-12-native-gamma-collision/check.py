#!/usr/bin/env python3
"""Bounded exact checks, or --full fresh defining-integral fold replay.

The default run is NOT an integral replay. --full executes all three complete
point integrals and the contraction test before accepting result.json.
"""
from fractions import Fraction as Q
from math import factorial, comb
from pathlib import Path
import argparse, hashlib, importlib.util, json, sys
ROOT=Path(__file__).resolve().parent

def require(ok,message):
    if not ok: raise ValueError(message)
def strict(data):
    def pairs(items):
        ans={}
        for k,v in items:
            require(k not in ans,'duplicate JSON key');ans[k]=v
        return ans
    def bad(x):raise ValueError('nonintegral/nonfinite JSON number')
    return json.loads(data,object_pairs_hook=pairs,parse_float=bad,parse_constant=bad)
def canonical(x):return json.dumps(x,sort_keys=True,separators=(',',':'))
def authenticate(root=ROOT):
    manifest=root/'SHA256SUMS'
    require(manifest.is_file() and not manifest.is_symlink(),'manifest')
    entries={}
    for line in manifest.read_text().splitlines():
        h,name=line.split('  ',1)
        require(name and '/' not in name and '\\' not in name and name not in entries,'manifest path')
        require(len(h)==64,'hash length');entries[name]=h
    actual={p.name for p in root.iterdir()}
    require(actual==set(entries)|{'SHA256SUMS'},'complete inventory')
    for name,h in entries.items():
        p=root/name
        require(p.is_file() and not p.is_symlink(),'regular file only')
        require(hashlib.sha256(p.read_bytes()).hexdigest()==h,'source hash: '+name)
    return len(entries)

def density_rows(rates):
    out=[]
    for l in rates:
        b=l*l; c=Q(0)
        for r in rates:
            if r!=l:b*=r*r/(r-l)**2;c-=2/(r-l)
        out.append((l,b,c))
    return out

def compute():
    counts={}; details={}
    n=0
    for a in [Q(4),Q(9),Q(36)]:
        for u,v,w in [(Q(0),Q(1,3),Q(1)),(Q(1,7),Q(2,5),Q(3,4)),(Q(1,4),Q(1,2),Q(1))]:
            for s in [Q(0),Q(1,7),Q(1),Q(5,2)]:
                R=lambda x,y: ((1+x*s/a)/(1+y*s/a))**2
                p=1-u/v; inc=(1-p+p/(1+v*s/a))**2
                require(inc==R(u,v),'finite Markov transform')
                require(R(u,v)*R(v,w)==R(u,w),'Chapman-Kolmogorov')
                require(2*(p*2*(v/a)**2-(p*v/a)**2)==2*(v*v-u*u)/(a*a),'increment variance')
                n+=1
    counts['complete_transition_transform_instances']=n
    n=0
    for k in range(10):
        for u in [Q(1,5),Q(1,3),Q(3,4)]:
            for x in [Q(0),Q(1,2),Q(3)]:
                a=Q(36)
                raw= -2*k*x**(k-1)/a if k else Q(0)
                raw += 2/u*sum((comb(k,j)*x**(k-j)*factorial(j)*(u/a)**j for j in range(1,k+1)),Q(0))
                compensated=2/u*sum((comb(k,j)*x**(k-j)*factorial(j)*(u/a)**j for j in range(2,k+1)),Q(0))
                require(raw==compensated and compensated>=0,'complete convex polynomial generator')
                n+=1
    counts['generator_polynomial_instances']=n
    n=0
    for N in range(1,7):
        for u in [Q(1,4),Q(1,3),Q(1,2),Q(1)]:
            rates=[Q(k*k) for k in range(1,N+1)]+[Q((N+1)**2)/u]
            rr=density_rows(rates)
            for s in [Q(0),Q(1,3),Q(1),Q(7,2)]:
                lhs=sum((b/(l+s)**2+b*c/(l+s) for l,b,c in rr),Q(0))
                rhs=Q(1)
                for l in rates:rhs*=l*l/(l+s)**2
                require(lhs==rhs,'complete density Laplace transform');n+=1
            mean=sum((2*b/l**3+b*c/l**2 for l,b,c in rr),Q(0))
            require(mean==sum((2/l for l in rates),Q(0)),'density mean')
    counts['finite_density_transform_instances']=n
    # Gaussian-rational complex arithmetic, with no Python complex/float.
    cm=lambda z,w:(z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0])
    n=0
    for a in [Q(1),Q(3),Q(31)]:
        for b in [Q(1,7),Q(1,2),Q(2)]:
            for ar,bi in [(Q(1,3),Q(-2,5)),(Q(-7,3),Q(1)),(Q(0),Q(-1))]:
                r2=a*a+b*b
                direct=(-4*a*b*b*ar+2*b*(a*a-b*b)*bi)/r2**3
                via=2*b*cm(cm((a,-b),(a,-b)),(ar,bi))[1]/r2**3
                require(direct==via,'weighted defect chain rule');n+=1
    counts['defect_flux_instances']=n
    n=0
    for c in [Q(2),Q(5),Q(31)]:
        for k in [Q(-3),Q(-1,3),Q(1,3),Q(5)]:
            izz=8*c*c; iu=-4*k*c*c
            require(-2*iu/izz==k,'exact fold discriminant slope')
            for eps in [Q(1,100),Q(1,1000)]:
                D=k*eps
                defect=max(-D,Q(0))/(c*c-D)**2
                require((defect==0)==(D>=0),'fold birth/death contribution');n+=1
    counts['synthetic_fold_instances']=n
    # Independent rational guards for the real mixed derivative bound.
    cmax=Q(14400**2, factorial(11))*Q(225,2)**2
    require(cmax<90000,'simplex coefficient envelope')
    huu=300*(10**9*Q(3)**6+3*Q(3)**4)
    require(4*huu<10**18,'complete mixed derivative majorant')
    details['real_derivative_majorant']='1000000000000000000'
    details['simplex_coefficient_upper']=str(cmax)
    return {'status':'BOUNDED_EXACT_ALGEBRA_NOT_NATIVE_INTEGRAL_REPLAY',
            'counts':counts,'details':details,'rh_proved':False,'global_defect_decay_proved':False}

def load_certificate():
    sp=importlib.util.spec_from_file_location('_native_fold',ROOT/'certificate.py')
    m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m


def tube_report(result):
    c=load_certificate();I,S=c.I,c.S
    iv=lambda p:I(int(p[0]),int(p[1]),raw=True)
    qlo=lambda v:Q(v.lo,S)
    qhi=lambda v:Q(v.hi,S)
    aq=lambda v:Q(v.absmax(),S)
    jets=[[iv(p) for p in row['jets']] for row in result['source_cases']]
    J=[[iv(p) for p in row] for row in result['jacobian']]
    h=c.STEP;r=Q(1,10**15);M=c.HESSIAN;third=Q(8)
    f0,f1,f2=jets[0];fu=J[0][1];fxu=J[1][1]
    C0=aq(f0)+aq(fu)*h+M*h*h/2
    C1=aq(f1)+aq(fxu)*h+M*h*h/2
    curve=-qhi(f2)-M*h-third*r
    upward=qlo(fu)-M*h-aq(fxu)*r-M*r*r/2
    margin=(-qhi(f2))*r*r/2-C0-C1*r-M*h*r*r/2-third*r**3/6
    left_max=qhi(jets[1][0])+aq(jets[1][1])**2/(2*curve)
    right_center=qlo(jets[2][0])
    require(curve>0 and upward>0 and margin>0,'whole local tube guard')
    require(C1<curve*r,'unique critical point in tube')
    require(left_max<0 and right_center>0,'endpoint fold orientation')
    return {'status':'EXACT_LOCAL_TUBE_ARITHMETIC_FROM_COMPLETE_INTEGRALS',
       'x_center':str(c.XC),'x_radius':str(r),'u_center':str(c.UC),'u_halfwidth':str(h),
       'uniform_rouche_margin_lower':str(margin),'uniform_negative_curvature_lower':str(curve),
       'uniform_parameter_derivative_lower':str(upward),
       'left_real_maximum_upper':str(left_max),'right_center_value_lower':str(right_center),
       'zeros_in_complex_disk_for_every_parameter':2,
       'left_endpoint_two_nonreal_simple_zeros':True,'right_endpoint_two_real_simple_zeros':True,
       'unique_real_collision_in_tube':True,'same_as_parent_N5_pair_certified':False,
       'rh_proved':False,'unbounded_defect_decay_proved':False}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--full',action='store_true');ap.add_argument('--emit',type=Path)
    aa=ap.parse_args();authenticate()
    actual=load_certificate().reconstruct() if aa.full else compute()
    if aa.emit:
        aa.emit.write_text(json.dumps(actual,sort_keys=True,indent=2)+'\n')
        print('PRODUCED_NOT_ACCEPTED');return
    name='result.json' if aa.full else 'algebra.json'
    expected=strict((ROOT/name).read_text())
    require(canonical(actual)==canonical(expected),'reconstructed payload mismatch')
    if aa.full:
        require(canonical(tube_report(actual))==canonical(strict((ROOT/'tube.json').read_text())),'native tube arithmetic mismatch')
    authenticate()
    print('PASS_FULL_NATIVE_FOLD_REPLAY' if aa.full else 'PASS_BOUNDED_ALGEBRA_NOT_NATIVE_REPLAY')
if __name__=='__main__':
    try:main()
    except (ValueError,OSError,ArithmeticError) as e:
        print('REFUSE: '+str(e),file=sys.stderr);sys.exit(1)
