"""Independent exact-rational replay of the narrow Liu tangent family.

All acceptance uses fractions, interval enclosures and explicit exceptions.
This verifies scalar formulas, not the analytic estimates which use them.
"""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json
from itertools import permutations


class I:
    def __init__(self, lo, hi=None):
        self.lo, self.hi = F(lo), F(lo if hi is None else hi)
        require(self.lo <= self.hi, 'ordered interval')
    @staticmethod
    def of(x):
        return x if isinstance(x, I) else I(x)
    def __add__(self, other):
        o = I.of(other)
        return I(self.lo+o.lo, self.hi+o.hi)
    __radd__ = __add__
    def __neg__(self):
        return I(-self.hi, -self.lo)
    def __sub__(self, o):
        return self+-I.of(o)
    def __rsub__(self, o):
        return I.of(o)+-self
    def __mul__(self, other):
        o = I.of(other)
        v = [self.lo*o.lo, self.lo*o.hi, self.hi*o.lo, self.hi*o.hi]
        return I(min(v), max(v))
    __rmul__ = __mul__
    def __truediv__(self, other):
        o = I.of(other)
        require(not o.lo <= 0 <= o.hi, 'nonzero denominator')
        return self*I(1/o.hi, 1/o.lo)
    def __rtruediv__(self, o):
        return I.of(o)/self
    def __pow__(self, n):
        require(isinstance(n, int) and n >= 0, 'integer power')
        ans=I(1)
        for _ in range(n):
            ans=ans*self
        return ans
    def receipt(self):
        return {'lower':str(self.lo), 'upper':str(self.hi)}


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


class P2:
    """Exact polynomials in delta and kappa, for primitive identities."""
    def __init__(self, terms):
        self.terms={e:F(v) for e,v in terms.items() if v}
    @staticmethod
    def of(v):
        return v if isinstance(v,P2) else P2({(0,0):F(v)})
    def __add__(self, other):
        o=P2.of(other)
        out=self.terms.copy()
        for e,v in o.terms.items(): out[e]=out.get(e,F(0))+v
        return P2(out)
    __radd__=__add__
    def __neg__(self):
        return P2({e:-v for e,v in self.terms.items()})
    def __sub__(self,o): return self+-P2.of(o)
    def __rsub__(self,o): return P2.of(o)+-self
    def __mul__(self,other):
        o=P2.of(other)
        out={}
        for a,x in self.terms.items():
            for b,y in o.terms.items():
                e=(a[0]+b[0],a[1]+b[1])
                out[e]=out.get(e,F(0))+x*y
        return P2(out)
    __rmul__=__mul__
    def derivative_d(self):
        return P2({(a-1,b):a*v for (a,b),v in self.terms.items() if a})
    def derivative_k(self):
        return P2({(a,b-1):b*v for (a,b),v in self.terms.items() if b})
    def __pow__(self,n):
        out=P2.of(1)
        for _ in range(n): out=out*self
        return out
    def at(self,d,k):
        value=I(0)
        for (a,b),v in self.terms.items(): value=value+v*d**a*k**b
        return value


def primitive_polynomials():
    d,k=P2({(1,0):1}),P2({(0,1):1})
    Db,Pb=15*k-2,6*k-1
    Jb=(F(5,6)-d)*Db+d*Pb
    Rb=2*(1-d)*Jb+(F(5,6)-d)*d*Pb
    den=96*k*Jb
    n0=(-F(1,4)+d*F(1,2))*den-2*d*Jb-18*k*(2*Jb-Rb)
    nl=(F(5,4)+d*F(1,2))*den+10*d*Jb-54*k*(2*Jb-Rb)
    nb=16*k*Jb-2*d*Jb-18*k*(2*Jb-Rb)
    critical=(3-324*k*k)*d*d+(756*k*k-54*k-5)*d+40*k-300*k*k
    require(not (3*nb+2*critical).terms,'primitive critical-class polynomial identity')
    bn=-(n0.derivative_d()*nl-n0*nl.derivative_d())
    bd=nl*nb.derivative_d()
    derivative_numerator=(n0.derivative_d()*nl-n0*nl.derivative_d())*nb.derivative_d()+bn*nb.derivative_d()
    require(not derivative_numerator.terms,'critical derivative cancellation')
    # Deliberately wrong source coefficient and wrong tangent orientation.
    require(bool((3*(nb+1)+2*critical).terms),'reject changed critical source coefficient')
    wrong=(n0.derivative_d()*nl-n0*nl.derivative_d())*nb.derivative_d()-bn*nb.derivative_d()
    require(bool(wrong.terms),'reject wrong tangent sign')
    # Primitive Sylvester determinant, reconstructed without a symbolic library.
    target=n0+(F(5,3)-2*k)*nl
    def dc(p,j):
        return P2({(0,b):v for (a,b),v in p.terms.items() if a==j})
    a,b,c=(dc(critical,j) for j in (2,1,0))
    u,v,w=(dc(target,j) for j in (2,1,0))
    zero=P2.of(0)
    matrix=[[a,b,c,zero],[zero,a,b,c],[u,v,w,zero],[zero,u,v,w]]
    determinant=P2.of(0)
    for perm in permutations(range(4)):
        sign=(-1)**sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
        term=P2.of(sign)
        for i,j in enumerate(perm): term=term*matrix[i][j]
        determinant=determinant+term
    quartic=16686*k**4-27405*k**3+9936*k*k+1290*k-275
    factor=-F(1600,3)*k*k*(6*k-1)**2*(15*k-2)*(42*k+5)*quartic
    require(not (determinant-factor).terms,'primitive critical resultant')
    return n0,nl,nb,bn,bd


def p_add(a,b):
    return [(a[i] if i<len(a) else I(0))+(b[i] if i<len(b) else I(0))
            for i in range(max(len(a),len(b)))]


def p_scale(a,c):
    return [x*c for x in a]


def p_mul(a,b):
    out=[I(0) for _ in range(len(a)+len(b)-1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]=out[i+j]+x*y
    return out


def cr(d,k):
    return (3-324*k*k)*d*d+(756*k*k-54*k-5)*d+40*k-300*k*k


def cr_d(d,k):
    return 2*(3-324*k*k)*d+756*k*k-54*k-5


def bracket_delta(k,steps=36):
    left,right=F(23,50),F(12,25)
    require(cr(I(left),k).hi<0 and cr(I(right),k).lo>0,'critical root endpoint signs')
    require(cr_d(I(left,right),k).lo>0,'critical root uniqueness')
    # Two independent bisections enclose the root for every k in the box.
    low_a,low_b=left,right
    high_a,high_b=left,right
    for _ in range(steps):
        m=(low_a+low_b)/2
        if cr(I(m),k).hi<0: low_a=m
        else: low_b=m
        m=(high_a+high_b)/2
        if cr(I(m),k).lo>0: high_b=m
        else: high_a=m
    require(cr(I(low_a),k).hi<0 and cr(I(high_b),k).lo>0,'closed critical root enclosure')
    return I(low_a,high_b)


def row_data(d,k,x):
    c=1/(3*k)
    D=3-(1+2*c)*x
    P=(2-2*c*x)*(1-x)
    J=(F(5,6)-d)*D+d*P
    R=1-d+(F(5,6)-d)*d*P/(2*J)
    Rd=-1+P*((F(5,6)-2*d)*J-(F(5,6)-d)*d*(P-D))/(2*J*J)
    return c,D,P,J,R,Rd


def endpoint(b,ell,k,d,x):
    c,D,P,J,R,Rd=row_data(d,k,x)
    h=(1+b+3*ell)/2
    ly=(1+b-ell)/2
    return -F(1,4)+b/6+5*ell/4+d/2+d*x*(ell+c*(h/4-ly/2))-3*h*(1-R)/4


def tangent(d,k):
    x=F(1,2)
    c,D,P,J,R,Rd=row_data(d,k,x)
    # E at b=ell=0 and its ell derivative, derived directly from (14.8).
    E00=-F(1,4)+d/2-d*c/16-F(3,8)*(1-R)
    El=F(5,4)+d*x*(1+5*c/8)-F(9,8)*(1-R)
    n0,nl,nb,bn,bd=PRIMITIVES
    ell=-n0.at(d,k)/nl.at(d,k)
    h0=(1+3*ell)/2
    ly0=(1-ell)/2
    Ed0=F(1,2)+x*(ell+c*(h0/4-ly0/2))+3*h0*Rd/4
    Edb=-x*c/8+3*Rd/8
    require(Edb.hi<0,'nonzero critical transversality')
    b=bn.at(d,k)/bd.at(d,k)
    return b,ell,El


def gap_derivative(d,k):
    n0,nl,nb,bn,bd=PRIMITIVES
    cd=cr_d(d,k)
    ck=-648*k*d*d+(1512*k-54)*d+40-600*k
    dd=-ck/cd
    n0p=n0.derivative_d().at(d,k)*dd+n0.derivative_k().at(d,k)
    nlp=nl.derivative_d().at(d,k)*dd+nl.derivative_k().at(d,k)
    ep=-(n0p*nl.at(d,k)-n0.at(d,k)*nlp)/(nl.at(d,k)**2)
    return F(1,2)+ep/4


def root_bracket():
    low,high=F(749773294079928,10**15),F(749773294079929,10**15)
    gaps=[]
    for k0 in (low,high):
        k=I(k0)
        d=bracket_delta(k,96)
        n0,nl,*_=PRIMITIVES
        ell=-n0.at(d,k)/nl.at(d,k)
        gaps.append((1+k)/2-F(11,12)+ell/4)
    require(gaps[0].hi<0 and gaps[1].lo>0,'strict self-consistent endpoint bracket')
    k=I(low,high)
    quartic_derivative=66744*k**3-82215*k*k+19872*k+1290
    require(quartic_derivative.lo>0 or quartic_derivative.hi<0,'unique quartic root on bracket')
    q=lambda k:16686*k**4-27405*k**3+9936*k*k+1290*k-275
    require(q(low)*q(high)<0,'quartic endpoint sign change')
    return {'kappa':[str(low),str(high)],'B':[str((1+low)/2),str((1+high)/2)]}


def abc(b,ell,k):
    c=1/(3*k)
    h=(1+b+3*ell)/2
    ly=(1+b-ell)/2
    C0=-F(1,4)+b/6+5*ell/4
    D=[F(5,2)-c,1+2*c]
    P=[1-c/2,I(2),2*c]
    V=ell+c*(h/4-ly/2)
    U=[F(1,2)+V/2,-V]
    PD=p_add(P,p_scale(D,-1))
    A=p_add(p_scale(p_mul(PD,U),-2),p_add(p_scale(P,9*h/4),p_scale(D,-3*h/2)))
    B=p_add(p_scale(PD,-2*C0),p_add(p_scale(p_mul(D,U),-F(5,3)),p_add(p_scale(D,5*h/4),p_scale(P,-5*h/8))))
    C=p_scale(D,-5*C0/3)
    return A,B,C


def side_margins(b,ell,k):
    h=(1+b+3*ell)/2
    ly=(1+b-ell)/2
    lx=(1-b-ell)/2
    B=F(11,12)-ell/4
    C0=-F(1,4)+b/6+5*ell/4
    Asm=F(1,2)+(ell/2)*(F(1,2)+2*ell/h)-h/2
    return {
        'b':b,'ell_above_sixth':ell-F(1,6),'ell_below_fifth':F(1,5)-ell,
        'B_floor':B-F(437,500),'lx_above_ell':lx-ell,
        'ly_minus_ell_above_11b6':ly-ell-11*b/6,
        'prime_capacity':6*k*ell-F(3,4),
        'ell_over_h_upper':1/(6*k)-ell/h,
        'ell_over_h_lower':ell/h-F(21,100),
        'ly_above_h_half':ly-h/2,'ly_below_half':F(1,2)-ly,
        'small_delta_0':-F(1,250)-C0,
        'small_delta_1':-F(1,250)-C0-Asm/8,
        'floor_endpoint':-F(1,100)-C0-(F(1,2)+3*ell/2)/50,
        'small_row':-F(1,20)-13*h/75+ly/2-F(1,50)
    }


def main():
    global PRIMITIVES
    PRIMITIVES=primitive_polynomials()
    lower,upper=F(7497732940799,10**13),F(3,4)
    count=64
    minima={}
    boxes=[]
    for j in range(count):
        a=lower+(upper-lower)*j/count
        z=lower+(upper-lower)*(j+1)/count
        k=I(a,z)
        d=bracket_delta(k)
        b,ell,El=tangent(d,k)
        A,B,C=abc(b,ell,k)
        discr=p_add(p_scale(p_mul(A,C),4),p_scale(p_mul(B,B),-1))
        margins=side_margins(b,ell,k)
        for n,x in enumerate(A): margins[f'A{n}']=x
        for n,x in enumerate(discr[1:],1): margins[f'discriminant_y{n}']=x
        margins['ell_derivative_minus_eighth']=El-F(1,8)
        margins['G_derivative']=gap_derivative(d,k)
        for name,x in margins.items():
            require(x.lo>0,f'positive {name} in box {j}: {x.receipt()}')
            minima[name]=min(minima.get(name,x.lo),x.lo)
        boxes.append({'kappa':[str(a),str(z)],'delta':d.receipt()})
    require(boxes[0]['kappa'][0]==str(lower) and boxes[-1]['kappa'][1]==str(upper),'endpoint coverage')
    require(all(boxes[i]['kappa'][1]==boxes[i+1]['kappa'][0] for i in range(count-1)),'contiguous coverage')
    output={
        'status':'pass',
        'scope':'Exact rational interval replay of tangent positivity and scalar side conditions. Critical double-root identities are documented algebraic derivations, not inferred from an interval containing zero. No analytic certification.',
        'source':'Liu arXiv:2610.26835v1 (14.3), (14.8), (14.10), Lemmas 14.8-14.10',
        'source_html_sha256':'5b128f3cedb4d6ecfe3a3d57b1290cb576cac03092cf0b807c6f8092abf864c6',
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
        'boxes':boxes,
        'strict_lower_bounds':{name:str(F(v.numerator*10**9//v.denominator,10**9)) for name,v in sorted(minima.items())},
        'rounding':'Each reported margin is rounded down to a rational multiple of 10^-9 using integer division. Acceptance uses the original exact positive interval bound.',
        'primitive_polynomial_identities':3,
        'negative_controls':2,
        'endpoint_bracket':root_bracket(),
        'not_replayed':['upstream analytic estimates','global critical family monotonicity outside the stated kappa interval']
    }
    print(json.dumps(output,indent=2))
    Path(__file__).with_name('TANGENT_CHECK.json').write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8',newline='\n')


if __name__=='__main__':
    main()
