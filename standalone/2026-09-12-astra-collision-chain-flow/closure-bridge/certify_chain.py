"""Full-source, full-tail Brouwer certificate. No floating acceptance arithmetic.

This add-only child uses the authenticated #875 interval/theta backend. It
proves existence, not uniqueness: the complete omitted cumulant tails are a
continuous perturbation, not differentiated by fiat. See PROOF.md.
"""
from __future__ import annotations
import argparse, hashlib, json, sys
from fractions import Fraction as Q
from pathlib import Path
from math import factorial

HERE=Path(__file__).resolve().parent
PARENT=HERE.parent
EXPECTED_PARENT={'exact_interval.py': '083ef417bc5249e189fb08f1c7b9009ff69a97a19073ba2778e02512515bf427', 'native_theta.py': '263271e3dac4f3316b20c0ac5d0e5e98ffef9ccd0573ed2aac3c9cd876f3d652', 'NUMERICS.md': '12e2dfe31b8470f5e0a326fe794238220f102f90970702442cb93a2416719324', 'ISING.md': 'aa8c8bafdc9c062fd1625616938f0266162def1f342297e1f14b003a414a38dd'}

def authenticate_parent():
    for name,wanted in EXPECTED_PARENT.items():
        raw=(PARENT/name).read_bytes()
        if hashlib.sha256(raw).hexdigest()!=wanted:
            raise ValueError('parent source identity mismatch: '+name)

authenticate_parent()
sys.path.insert(0,str(PARENT))
from exact_interval import I, SCALE, exp, log_q, pi
from native_theta import theta_moments, cumulants

ZERO=I.q(0);ONE=I.q(1)
TAN=(Q(1),Q(1,3),Q(2,15),Q(17,315),Q(62,2835))
LOGCOS=(Q(1,2),Q(1,12),Q(1,45),Q(17,2520),Q(31,14175))
K=5
N=8192

class D:
    __slots__=('v','d')
    def __init__(self,v,d):self.v=I.q(v);self.d=tuple(I.q(x) for x in d)
    def other(self,o):
        if isinstance(o,D):
            if len(o.d)!=len(self.d):raise ValueError('dual dimension')
            return o
        return D(o,(ZERO,)*len(self.d))
    def __add__(self,o):
        o=self.other(o);return D(self.v+o.v,tuple(a+b for a,b in zip(self.d,o.d)))
    __radd__=__add__
    def __neg__(self):return D(-self.v,tuple(-a for a in self.d))
    def __sub__(self,o):return self+-self.other(o)
    def __rsub__(self,o):return self.other(o)+-self
    def __mul__(self,o):
        o=self.other(o);return D(self.v*o.v,tuple(a*o.v+self.v*b for a,b in zip(self.d,o.d)))
    __rmul__=__mul__
    def inv(self):
        v=self.v.inv();return D(v,tuple(-a*v*v for a in self.d))
    def __truediv__(self,o):return self*self.other(o).inv()
    def __rtruediv__(self,o):return self.other(o)*self.inv()
    def __pow__(self,n):
        if type(n) is not int or n<0:raise ValueError('power')
        if n==0:return self.other(1)
        return D(self.v**n,tuple(n*(self.v**(n-1))*a for a in self.d))
    def sqrt(self):
        s=self.v.sqrt();return D(s,tuple(a/(2*s) for a in self.d))

def ilog(v):
    v=I.q(v)
    return I(log_q(Q(v.lo,SCALE)).lo,log_q(Q(v.hi,SCALE)).hi)

def dlog(v):return D(ilog(v.v),tuple(x/v.v for x in v.d))

def variable(v,j,dim):return D(v,tuple(ONE if i==j else ZERO for i in range(dim)))
def promote(x,dim=5):return D(x.v,(ZERO,)*(dim-1)+(x.d[0],))

def step(s,ell,a,q):
    """Exact formal Fourier recursion through degree ten, including all edges."""
    zero=a.other(0);one=a.other(1);a2=a*a
    powers=[one]
    for _ in range(K):powers.append(powers[-1]*a2)
    t=[a*powers[r]*TAN[r] for r in range(K)]
    u=[zero]+[q*sum((t[i]*s[r-1-i] for i in range(r)),zero) for r in range(1,K+1)]
    inv=[one]
    for r in range(1,K+1):inv.append(sum((u[j]*inv[r-j] for j in range(1,r+1)),zero))
    logs=[sum((u[j]*inv[r-j]*j for j in range(1,r+1)),zero)/r for r in range(1,K+1)]
    nums=[t[r]+q*s[r] for r in range(K)]
    ns=[sum((nums[i]*inv[r-i] for i in range(r+1)),zero) for r in range(K)]
    ne=[ell[r]+powers[r+1]*LOGCOS[r]+logs[r] for r in range(K)]
    return ns,ne

def neglog_one_minus(u,zero,one):
    inv=[one]
    for r in range(1,K+1):inv.append(sum((u[j]*inv[r-j] for j in range(1,r+1)),zero))
    return [sum((u[j]*inv[r-j]*j for j in range(1,r+1)),zero)/r for r in range(1,K+1)]

from functools import lru_cache
@lru_cache(maxsize=10000)
def sinh_q(u):
    z=exp(I.q(u));return (z-z.inv())/2

@lru_cache(maxsize=1)
def constants():
    p=pi();log2=log_q(Q(2));M=8192
    gamma=sum((I.q(Q(1,n)) for n in range(1,M+1)),ZERO)-log_q(Q(M))-Q(1,2*M)
    eg=I.q(Q(1,6*(M-1)**2))
    M=256;l=log_q(Q(M))
    f=(l)/(M*M);fp=(1-2*l)/(M**3);fppp=(26-24*l)/(M**5)
    S=sum((log_q(Q(n))/(n*n) for n in range(32,M)),ZERO)+(l+1)/M+f/2-fp/12+fppp/720
    es=-fppp/720
    return p,log2,gamma,eg,S,es,sum((I.q(Q(1,n)) for n in range(1,32)),ZERO)

def calibration(q):
    """Finite Simpson calibration and its complete error, as a function of q."""
    r=(1-q)/(1+q)
    def integ(u,first):
        if u==0:return 1/r
        s=sinh_q(u)
        m=(r*r+s*s).sqrt().__rtruediv__(s)
        return m/u if first else (m-1)/u
    def simp(a,b,n,first):
        total=q.other(0);h=Q(b-a,n)
        for j in range(n+1):
            u=Q(a)+j*h;w=1 if j in (0,n) else (4 if j%2 else 2)
            total=total+integ(u,first)*w
        return total*h/3
    C=-1+simp(0,1,512,True)+simp(1,8,4096,False)
    errC=I.q(Q(24576,180*512**4)+Q(24576*7**5,180*4096**4))+3*exp(-16)/16
    p,l2,gamma,eg,S,es,H=constants()
    d=7/(8*dlog((1+q)/2))
    A=-C/2-d*S-(1+ilog(2*p))/2+(l2-gamma)/2+H/2
    errA=(errC+eg)/2+abs_i(d.v)*es
    return A,d,errA

def abs_i(x):return I.q(Q(max(abs(x.lo),abs(x.hi)),SCALE))
def upper(x):return Q(x.hi,SCALE)

def finite_system(x,theta,scales):
    # Every tail entry depends only on q. Reversal keeps its near endpoint.
    q=variable(x[4],0,1)
    A,d,errA=calibration(q)
    zero=q.other(0);st=[zero]*K;lt=[zero]*K
    for n in range(N,31,-1):
        a=Q(1,2*n)+d*(log_q(Q(n))/(n*n))
        st,lt=step(st,lt,a,q)
    q5=variable(x[4],4,5);z5=q5.other(0);o5=q5.other(1)
    sh=[z5]*K;lh=[z5]*K
    for j,mult in enumerate((25,4,1,1)):
        a=variable(x[j],j,5)
        for _ in range(mult):sh,lh=step(sh,lh,a,q5)
    st=[promote(t) for t in st];lt=[promote(t) for t in lt]
    u=[z5]+[q5*sum((sh[i]*st[r-1-i] for i in range(r)),z5) for r in range(1,K+1)]
    extra=neglog_one_minus(u,z5,o5)
    vals=[(lh[r]+lt[r]+extra[r])*factorial(2*r+2) for r in range(K)]
    d5=promote(d);l=log_q(Q(N));kap=(1+q5)/(1-q5)
    integ=Q(1,4*N)+d5*(l+Q(1,2))/(2*N*N)+d5*d5*(l*l+2*l/3+Q(2,9))/(3*N**3)
    vals[0]=vals[0]+kap*integ
    eq=[sum((variable(x[j],j,5)*mult for j,mult in enumerate((25,4,1,1))),z5)-promote(A)]
    eq += [(vals[r]-theta[r])/scales[r] for r in range(4)]
    return eq,vals,errA,d.v

def tail_errors(q,errA,scales):
    """Uniform undifferentiated perturbation of the exact infinite equations."""
    qc=I.q(Q(1,32));kap=(1+qc)/(1-qc)
    evar=kap/(4*N*N)+qc/(4*(1-qc)**2*N*N)+2*qc/((1-qc)*N*(N+1))
    # Degree <=8 uses the tan(2u/n) majorant; degree 10 uses tan(3u/n).
    es=[errA,evar/scales[0]]
    for r,sg in ((2,2),(3,16),(4,272)):
        es.append(I.q(Q(sg*2**(2*r),(2*r-1)*N**(2*r-1)))/scales[r-1])
    return es,I.q(Q(7936*3**10,9*N**9))

def strict_pairs(items):
    out={}
    for key,value in items:
        if key in out:raise ValueError('duplicate JSON key')
        out[key]=value
    return out

def reject_number(_):raise ValueError('only exact string-valued numerical inputs')

def load_parameters():
    p=json.loads((HERE/'parameters.json').read_text(),object_pairs_hook=strict_pairs,
                 parse_float=reject_number,parse_constant=reject_number)
    if set(p)!={'center','radius','preconditioner','scales','status'}:raise ValueError('parameter schema')
    if p['status']!='exact rational certificate inputs':raise ValueError('parameter status')
    for key,n in (('center',5),('scales',4)):
        if type(p[key]) is not list or len(p[key])!=n or any(type(x) is not str for x in p[key]):
            raise ValueError('typed parameter vector')
    R=p['preconditioner']
    if type(R) is not list or len(R)!=5 or any(type(r) is not list or len(r)!=5 or
        any(type(v) is not str for v in r) for r in R):raise ValueError('typed preconditioner')
    if type(p['radius']) is not str or not 0<Q(p['radius'])<Q(1,100):raise ValueError('radius')
    if any(Q(x)<=0 for x in p['scales']):raise ValueError('positive scales')
    return p

def majorant_guard():
    # Independent exact-rational series, not the interval automatic differentiation.
    tcoeff=list(TAN);s=tcoeff[:];q=Q(1,32)
    for n in range(32,65):
        a=Q(1,2*n);t=[tcoeff[r]*a**(2*r+1) for r in range(K)]
        u=[Q(0)]+[q*sum(t[i]*s[r-1-i] for i in range(r)) for r in range(1,K+1)]
        inv=[Q(1)]
        for r in range(1,K+1):inv.append(sum(u[j]*inv[r-j] for j in range(1,r+1)))
        nums=[t[r]+q*s[r] for r in range(K)]
        s=[sum(nums[i]*inv[r-i] for i in range(r+1)) for r in range(K)]
    for c,k,alpha in ((2,4,Q(5,8)),(3,5,Q(3,4))):
        for j in range(k):
            if not s[j]<tcoeff[j]*Q(c,64)**(2*j+1):raise ArithmeticError('majorant base')
            if not q<=alpha**(2*j+1):raise ArithmeticError('coefficient dilation')
        if not Q(1,2)+alpha*c*Q(65,64)<c:raise ArithmeticError('majorant induction')
    return 9

def dec(q,up=False):
    q=Q(q);scale=10**30
    k=-((-q.numerator*scale)//q.denominator) if up else q.numerator*scale//q.denominator
    sign='-' if k<0 else '';k=abs(k)
    return sign+str(k//scale)+'.'+str(k%scale).zfill(30)

def bounds(x):return [dec(Q(x.lo,SCALE)),dec(Q(x.hi,SCALE),True)]

def reconstruct():
    guards=majorant_guard()
    pars=load_parameters()
    if pars.get('status')!='exact rational certificate inputs':raise ValueError('parameter status')
    c=[Q(v) for v in pars['center']];rad=Q(pars['radius'])
    R=[[Q(v) for v in row] for row in pars['preconditioner']]
    scales=[Q(v) for v in pars['scales']]
    if not len(c)==5 or not all(len(row)==5 for row in R):raise ValueError('dimension')
    box=[I.q(v)+I(-I.q(rad).hi,I.q(rad).hi) for v in c]
    if not all(x.lo>0 for x in box) or not upper(box[4])<Q(1,32):raise ValueError('positive parameter box')
    if not upper(sum((box[j]*m for j,m in enumerate((25,4,1,1))),ZERO))<1:raise ValueError('head mass guard')
    raw=theta_moments(5);mu=[v/raw[0] for v in raw];mu[0]=ONE
    signed=cumulants(mu);theta=[x if r%2==0 else -x for r,x in enumerate(signed)]
    fc,vc,ec,dc=finite_system([I.q(v) for v in c],theta,scales)
    fb,vb,eb,db=finite_system(box,theta,scales)
    if not upper(abs_i(db))<Q(13,10):raise ValueError('tail positivity/growth guard')
    jac=[[v.d[j] for j in range(5)] for v in fb]
    pre_res=[sum((fc[j].v*R[i][j] for j in range(5)),ZERO) for i in range(5)]
    beta=max(upper(abs_i(v)) for v in pre_res)
    defects=[[I.q(int(i==j))-sum((jac[k][j]*R[i][k] for k in range(5)),ZERO) for j in range(5)] for i in range(5)]
    L=max(sum(upper(abs_i(x)) for x in row) for row in defects)
    errors,e10=tail_errors(box[4],eb,scales)
    perturb=max(sum(abs(R[i][j])*upper(errors[j]) for j in range(5)) for i in range(5))
    bound=beta+L*rad+perturb
    if not L<1 or not bound<rad:raise ArithmeticError('Brouwer whole-box inclusion failed: '+str([dec(beta,True),dec(L,True),dec(perturb,True),dec(bound,True)]))
    tenth=(vb[4].v-theta[4]+I(0,e10.hi))/(mu[1]**5)
    # Invertibility follows already from ||I-RJ||<1; determinant is also exact.
    a=[row[:] for row in R];det=Q(1)
    for i in range(5):
        if not a[i][i]:
            k=next(k for k in range(i+1,5) if a[k][i]);a[i],a[k]=a[k],a[i];det=-det
        v=a[i][i];det*=v
        for k in range(i+1,5):
            q=a[k][i]/v
            for j in range(i+1,5):a[k][j]-=q*a[i][j]
    if not det:raise ArithmeticError('singular preconditioner')
    return {'status':'proposed computer-assisted existence; independent review required',
      'source':'complete native theta; inherited analytic source contract re-evaluated',
      'finite_chain_cutoff':N,'root_center':[str(x) for x in c],'root_box_radius':str(rad),
      'q_box':bounds(box[4]),'whole_tail_errors_scaled':[bounds(e) for e in errors],
      'center_displacement_upper':dec(beta,True),'derivative_defect_upper':dec(L,True),
      'continuous_tail_displacement_upper':dec(perturb,True),'box_image_radius_upper':dec(bound,True),
      'tenth_standardized_cumulant_difference_whole_box':bounds(tenth),
      'exact_even_moments_matched':[2,4,6,8],
      'growth_coefficients_matched':3,'existence_proved_with_brouwer':True,
      'uniqueness_proved':False,'rh_proved':False,'all_order_realization_proved':False,
      'native_variance':bounds(mu[1]),'majorant_base_checks':guards}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',type=Path);p.add_argument('--check',type=Path);a=p.parse_args()
    if bool(a.write)==bool(a.check):p.error('select exactly one of --write or --check')
    r=reconstruct();text=json.dumps(r,indent=2,sort_keys=True)+'\n'
    if a.write:a.write.write_text(text)
    else:
        if a.check.read_text()!=text:raise ValueError('receipt mismatch')
    print(hashlib.sha256(text.encode()).hexdigest())
