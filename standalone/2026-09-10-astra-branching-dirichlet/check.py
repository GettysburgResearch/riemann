"""Exact bounded Gamma--Dirichlet controls and one directed phase test.
No asserted RH result, all-depth zero preservation, or zero census.
"""
from fractions import Fraction as Q
from math import comb
from pathlib import Path
import argparse, hashlib, importlib.util, json, sys

HERE=Path(__file__).resolve().parent
PARENT=HERE.parent/'2026-09-10-astra-branching-order'/'certificate.py'
PARENT_SHA='f20b3528dfa626acf9a9d5f5c70bf0d8c147322bd0215045a7a469f3280070b2'
DEGREE=240

def load_core():
    if PARENT.is_symlink() or not PARENT.is_file(): raise ValueError('missing or linked parent')
    if hashlib.sha256(PARENT.read_bytes()).hexdigest()!=PARENT_SHA: raise ValueError('parent drift')
    spec=importlib.util.spec_from_file_location('bor_interval',PARENT)
    core=importlib.util.module_from_spec(spec);spec.loader.exec_module(core)
    return core

def rising(x,n):
    x=Q(x);r=Q(1)
    for j in range(n):r*=x+j
    return r

def beta_pair(m,a):
    """Moments of BZ+(1-B)Z', independent B~Beta(a,a)."""
    n=len(m)-1
    return [sum((comb(j,l)*rising(a,l)*rising(a,j-l)*m[l]*m[j-l]
                 for l in range(j+1)),Q())/rising(2*a,j) for j in range(n+1)]

def scale_moment(j):
    return Q(1) if j==0 else (1-Q(2)**(1-2*j))/(2*j-1)

def raw_orbit(nmax,jmax):
    m=[rising(Q(5,2),j)/Q(5,2)**j for j in range(jmax+1)]
    out=[m]
    for _ in range(nmax):
        m=[scale_moment(j)*sum((comb(j,l)*m[l]*m[j-l] for l in range(j+1)),Q()) for j in range(jmax+1)]
        out.append(m)
    return out

def gamma_dirichlet_controls():
    jmax=12;nmax=6;k=Q(5,2);raw=raw_orbit(nmax,jmax)
    z=[Q(1)]*(jmax+1);records=[]
    for n in range(nmax+1):
        a=k*2**n
        converted=[rising(a,j)*z[j]/k**j for j in range(jmax+1)]
        if converted!=raw[n]: raise ValueError('gamma source mismatch')
        if any(not Q(4)**(-n*j)<=z[j]<=1 for j in range(jmax+1)):
            raise ValueError('mixing support bounds')
        h=beta_pair(z,a)
        pair=[sum((comb(j,l)*raw[n][l]*raw[n][j-l] for l in range(j+1)),Q()) for j in range(jmax+1)]
        if [rising(2*a,j)*h[j]/k**j for j in range(jmax+1)]!=pair:
            raise ValueError('pair normalization')
        records.append({'n':n,'gamma_pair_shape':int(2*a),'lower_support':[1,4**n],
                        'left_first_pole':int(-4*a),'right_first_pole':int(1+4*a)})
        z=[scale_moment(j)*h[j] for j in range(jmax+1)]
    return records

def central_w(n):
    # Derived by integrating d[r^j/sqrt(1+r)] on [-3/5,3/5].
    r=[Q(1)];power=Q(1)
    for j in range(1,n+1):
        power*=Q(3,5)
        r.append(((Q(1,2)-(-1)**j)*power-j*r[-1])/Q(2*j-1,2))
    if any(abs(x)>Q(3,5)**j for j,x in enumerate(r)):raise ValueError('central W range')
    # Independent finite binomial reconstruction from exact uniform moments.
    for j in range(min(40,n)+1):
        q=sum((comb(j,l)*Q(8,5)**l*(-1)**(j-l)*scale_moment(l) for l in range(j+1)),Q())
        if q!=r[j]:raise ValueError('central W primitive')
    return r

def phase_certificate():
    core=load_core();I,C=core.I,core.C
    r=central_w(DEGREE)
    eta=[sum((Q(comb(j+4,4)*comb(n-j+4,4),comb(n+9,9))*r[j]*r[n-j]
              for j in range(n+1)),Q()) for n in range(DEGREE+1)]
    # Check first 25 mixing moments against the independent raw beta formula.
    raw=beta_pair([scale_moment(j) for j in range(25)],Q(5))
    for n in range(25):
        direct=sum((comb(n,j)*Q(8,5)**j*(-1)**(n-j)*raw[j] for j in range(n+1)),Q())
        if direct!=eta[n]:raise ValueError('wrong beta shape or gamma convention')
    if any(abs(x)>Q(3,5)**j for j,x in enumerate(eta)):raise ValueError('eta range')
    s=C(Q(1,2),23);p=s/2
    b=C(1);db=C();v=C(1);dv=C()
    for j in range(1,DEGREE+1):
        db,b=(db*(p-j+1)+b/2)/j,b*(p-j+1)/j
        v+=b*eta[j];dv+=db*eta[j]
    # On |s-s0|<=1 and |z|=4/5, |(1+z)^(s/2)|<10*3^24.
    # Cauchy in s also pays the derivative, so both full tails use this bound.
    err=40*3**24*Q(3,4)**(DEGREE+1)
    v=v.inflate(err);dv=dv.inflate(err)
    pi=core.pi_i();lc=core.log_i(pi/15)+core.log_i(Q(5,8))
    _,psi=core.loggamma_psi(10+p,pi)
    logder=C(lc/2)+psi/2+dv/v
    D=2*logder.re
    low,high=Q('-1.427840092064'),Q('-1.427840092063')
    if not (Q(D.lo,core.S)>low and Q(D.hi,core.S)<high):raise ValueError('phase bracket failure')
    den=v.re*v.re+v.im*v.im
    if den.lo<=0:raise ValueError('M nonzero not certified')
    return {'point_real':'1/2','point_imaginary':23,'depth':1,'initial_gamma_shape':'5/2',
            'beta_shape':5,'gamma_pair_shape':10,'degree':DEGREE,
            'D':D.rec(),'bracket':['-1.427840092064','-1.427840092063'],
            'mixing_series_square_modulus':den.rec(),'full_series_error':str(err),
            'meaning':'negative derivative of the modulus-ratio logarithm; NOT a zero certificate'}

def result():
    return {'schema':'BDR26-1','source_pr':853,'source_head':'e0b82da7ecdd4ed21e47e8b6adbb8c5182eac048',
            'orbit_zero_preservation_proved':False,'rh_proved':False,
            'gamma_dirichlet_controls':gamma_dirichlet_controls(),'phase':phase_certificate()}

def unique(pairs):
    d={}
    for k,v in pairs:
        if k in d:raise ValueError('duplicate JSON key')
        d[k]=v
    return d

def read_json(path):
    return json.loads(Path(path).read_text(),object_pairs_hook=unique,
        parse_float=lambda _: (_ for _ in ()).throw(ValueError('float JSON')),
        parse_constant=lambda _: (_ for _ in ()).throw(ValueError('nonfinite JSON')))

def canonical(x):return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=True)

def main():
    ap=argparse.ArgumentParser();g=ap.add_mutually_exclusive_group(required=True)
    g.add_argument('--write');g.add_argument('--check');args=ap.parse_args()
    actual=result()
    if args.write:
        Path(args.write).write_text(json.dumps(actual,sort_keys=True,indent=2)+'\n')
        print('PRODUCED_BDR26')
    else:
        if canonical(read_json(args.check))!=canonical(actual):raise ValueError('reconstruction mismatch')
        print('PASS_BDR26 '+hashlib.sha256(canonical(actual).encode()).hexdigest())

if __name__=='__main__':
    try:main()
    except (ValueError,TypeError,ZeroDivisionError,OSError) as e:
        print('REJECT_BDR26: '+str(e),file=sys.stderr);raise SystemExit(1)
