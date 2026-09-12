"""Exact polynomial star moments and their box derivatives (no optimizer)."""
from fractions import Fraction as F
from math import comb
from ball_core import B, ZERO, ONE, Q, rad

COUNTS=(1,1,1,1,1,1,1,24,64)
ACTIVE=(9,0,7,1,8,2,5)
FIXED={3:F('0.21994570188028675'),4:F('0.19874795734917752'),6:F('0.17590620417053146')}


def sign_cumulant_polynomials(n):
    out=[[],[0,1]]
    for k in range(1,n):
        p=out[-1];d=[j*p[j] for j in range(1,len(p))]
        q=[0]*(len(d)+2)
        for j,v in enumerate(d):q[j]+=v;q[j+2]-=v
        while q and q[-1]==0:q.pop()
        out.append(q)
    return out

C=sign_cumulant_polynomials(16)

class D:
    """Forward derivative with seven exact outward ball components."""
    __slots__=('v','d')
    def __init__(self,v=0,d=None):
        self.v=v if isinstance(v,B) else B.real(v)
        self.d=tuple(ZERO for _ in ACTIVE) if d is None else tuple(d)
    def __add__(self,o):
        if not isinstance(o,D):o=D(o)
        return D(self.v+o.v,[a+b for a,b in zip(self.d,o.d)])
    __radd__=__add__
    def __neg__(self):return D(-self.v,[-a for a in self.d])
    def __sub__(self,o):return self+-o if isinstance(o,D) else self+-D(o)
    def __rsub__(self,o):return -self+o
    def __mul__(self,o):
        if not isinstance(o,D):
            return D(self.v*o,[a*o for a in self.d])
        return D(self.v*o.v,[a*o.v+self.v*b for a,b in zip(self.d,o.d)])
    __rmul__=__mul__
    def __truediv__(self,o):return self*(F(1)/F(o))


def poly(p,x):
    out=x*0
    for c in reversed(p):out=out*x+c
    return out


def graph(weights,K=16,tail=None,counts=COUNTS):
    """Return conditional moments, unconditional moments and cumulants."""
    zero=weights[0]*0;one=zero+1
    kk=[zero]*(K+1);kk[1]=weights[len(counts)]
    for count,a in zip(counts,weights[:-1]):
        power=one
        for k in range(1,K+1):
            power=power*a
            kk[k]=kk[k]+count*power*poly(C[k],a/100)
    if tail is not None:
        for k in range(1,K+1):kk[k]=kk[k]+tail[k]
    conditional=[one]
    for n in range(1,K+1):
        conditional.append(sum((comb(n-1,j-1)*kk[j]*conditional[n-j] for j in range(1,n+1)),zero))
    mu=[conditional[n] if n%2==0 else zero for n in range(K+1)]
    ku=[zero]*(K+1)
    for n in range(1,K+1):
        ku[n]=mu[n]-sum((comb(n-1,j-1)*ku[j]*mu[n-j] for j in range(1,n)),zero)
    return conditional,mu,ku


def inverse(a):
    """Fraction Gaussian elimination; also reconstructs both products."""
    n=len(a);aug=[[F(x) for x in row]+[F(int(i==j)) for j in range(n)] for i,row in enumerate(a)]
    for j in range(n):
        pivot=next((i for i in range(j,n) if aug[i][j]),None)
        if pivot is None:raise ArithmeticError('singular preconditioner')
        aug[j],aug[pivot]=aug[pivot],aug[j]
        s=aug[j][j];aug[j]=[v/s for v in aug[j]]
        for i in range(n):
            if i!=j:
                t=aug[i][j];aug[i]=[v-t*w for v,w in zip(aug[i],aug[j])]
    R=[row[n:] for row in aug]
    for x,y in ((a,R),(R,a)):
        for i in range(n):
            for j in range(n):
                if sum((x[i][k]*y[k][j] for k in range(n)),F(0))!=int(i==j):
                    raise ArithmeticError('inverse identity')
    return R


def root_certificate(centers,target_cumulants,target_moments,radius=F(1,10**24),tail=None):
    if len(centers)!=10:raise ValueError('ten weights required')
    for i,v in FIXED.items():
        if centers[i]!=v:raise ValueError('fixed coordinate changed')
    if any(a<=0 or a>=1 for a in centers):raise ValueError('positive subunit center required')
    def inputs(box):
        out=[]
        for j,c in enumerate(centers):
            deriv=[ZERO]*len(ACTIVE)
            if j in ACTIVE:deriv[ACTIVE.index(j)]=ONE
            value=B.real(c)
            if box and j in ACTIVE:value=value.grow(rad(radius))
            out.append(D(value,deriv))
        return out
    _,_,center_k=graph(inputs(False),14,tail)
    jac=[[F(center_k[k].d[j].a,Q) for j in range(7)] for k in range(2,15,2)]
    R=inverse(jac)
    f=[center_k[k].v-target_cumulants[k] for k in range(2,15,2)]
    delta=max(sum((R[i][j]*f[j] for j in range(7)),ZERO).norm() for i in range(7))
    _,box_mu,box_k=graph(inputs(True),16,tail)
    defects=[]
    for i in range(7):
        row=[]
        for j in range(7):
            val=int(i==j)-sum((R[i][l]*box_k[2*l+2].d[j] for l in range(7)),ZERO)
            row.append(val.norm())
        defects.append(row)
    contraction=max(sum(row) for row in defects)
    if contraction>=Q or F(delta,Q)+F(contraction,Q)*radius>=radius:
        raise ArithmeticError(f'root contraction failed delta={delta/Q:g}, q={contraction/Q:g}, r={float(radius):g}')
    bounds=[B.real(c).grow(rad(radius) if i in ACTIVE else 0) for i,c in enumerate(centers)]
    for a in bounds:
        if a.a-a.e<=0 or a.a+a.e>=Q:raise ArithmeticError('box leaves positive weights')
    difference=box_mu[16].v-target_moments[16]
    return {'delta_dyadic_upper':delta,'contraction_dyadic_upper':contraction,
            'radius':str(radius),'preconditioner_sha256':__import__('hashlib').sha256(__import__('json').dumps([[str(x) for x in row] for row in R],separators=(',',':')).encode()).hexdigest(),
            'preconditioner_norm_dyadic_upper':rad(max(sum(abs(x) for x in row) for row in R)),
            'exact_inverse_identities':98,
            'jacobian_defect_rows':defects,'weights':[[b.a,b.b,b.e] for b in bounds],
            'sixteenth_difference':[difference.a,difference.b,difference.e]},bounds,difference


def harmonic_tail(J=10**40):
    """Entire conditional cumulant tail, c=1/(2 sigma)<5/2.
    Each omitted harmonic leaf has a_j=c/j and m_j=a_j/100.
    The endpoints are uniform for every c in (0,5/2), not finite truncations.
    """
    out=[ZERO]*17; bounds=[F(0)]*17
    bounds[1]=F(1,100)*F(25,4)/F(J-1)
    for k in range(2,17):
        bounds[k]=sum(abs(v) for v in C[k])*F(5,2)**k/F((k-1)*(J-1)**(k-1))
    for k in range(1,17):out[k]=B(0,0,rad(bounds[k]))
    return out,bounds
