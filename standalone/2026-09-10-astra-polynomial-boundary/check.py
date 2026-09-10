#!/usr/bin/env python3
"""Bounded exact controls for AC29, NOT a proof of Q-AC28 or of RH."""
from __future__ import annotations
import argparse, copy, hashlib, json, math
from fractions import Fraction as F
from pathlib import Path

SCHEMA='AC29-origin-boundary/v1'
PARENT='b9ccd03a681a73e91fb7bbfb7a3b97766fe8285e'
BITS=160

def need(ok, msg):
    if not ok: raise ValueError(msg)

class I:
    def __init__(self, a=0,b=None):
        self.a=F(a); self.b=F(a if b is None else b)
        need(self.a<=self.b, 'reversed interval')
    @staticmethod
    def cast(x): return x if isinstance(x,I) else I(x)
    def __add__(self,o):
        o=self.cast(o); return I(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return I(-self.b,-self.a)
    def __sub__(self,o): return self+-self.cast(o)
    def __rsub__(self,o): return self.cast(o)+-self
    def __mul__(self,o):
        o=self.cast(o); v=[x*y for x in (self.a,self.b) for y in (o.a,o.b)]
        return I(min(v),max(v))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=self.cast(o); need(not o.a<=0<=o.b, 'division through zero')
        return self*I(1/o.b,1/o.a)
    def __pow__(self,n):
        need(type(n) is int and n>=0,'power'); out=I(1)
        for _ in range(n): out=out*self
        return out
    def absmax(self): return max(abs(self.a),abs(self.b))
    def encode(self):
        # Outward rounded dyadic record; all comparisons happen BEFORE rounding.
        D=1<<40
        lo=(self.a*D).__floor__(); hi=(self.b*D).__ceil__()
        return [str(lo),str(hi),40]

def qp(x,ex):
    """Exact directed rational enclosure of positive x**ex; 4*ex is integral."""
    x=F(x); ex=F(ex); j=4*ex
    need(x>0 and j.denominator==1,'quarter-power domain')
    y=x**int(j); D=1<<BITS; M=(y.numerator*D**4)//y.denominator
    k=math.isqrt(math.isqrt(M))
    need(k**4*y.denominator<=y.numerator*D**4<(k+1)**4*y.denominator,'root certificate')
    return I(F(k,D),F(k+1,D))

def chi(v):
    v=F(v)
    if v<=1:return F(0)
    if v>=2:return F(1)
    return 3*(v-1)**2-2*(v-1)**3

def dc(v):
    v=F(v)
    return 6*(v-1)*(2-v) if 1<v<2 else F(0)

def Zstrip(s,M):
    need(M>=2 and M%2==0,'even Euler boundary')
    partial=sum((qp(n,-s) for n in range(1,M,2)),I())
    center=partial-qp(M,1-s)/(2*(1-s))
    radius=qp(M,-s).b/2
    return center+I(-radius,radius)

def cs(s):
    out=qp(2,s-1)/(1-s)
    for j,c in enumerate([5,-12,9,-2]):
        out+=c*(qp(2,s+j-1)-1)/(s+j-1)
    return out/2

def smooth(s,v):
    out=I(); deriv=I()
    for n in range(1,math.floor(v)+2,2):
        out+=qp(n,-s)*chi(v/n)
        deriv+=qp(n,-s)*(v/n)*dc(v/n)
    return out,deriv

def bernoullis(n):
    B=[F(1)]
    for m in range(1,n+1):
        B.append(-sum(F(math.comb(m+1,k))*B[k] for k in range(m))/(m+1))
    return B

def atan_inv(q,N):
    s=sum((F((-1)**j,(2*j+1)*q**(2*j+1)) for j in range(N)),F())
    term=F((-1)**N,(2*N+1)*q**(2*N+1))
    return I(min(s,s+term),max(s,s+term))

def Zeven(k):
    # Classical even-zeta formula and Machin identity; explicit alternating tails.
    pi=16*atan_inv(5,96)-4*atan_inv(239,32)
    b=abs(bernoullis(2*k)[2*k])
    return (1-F(1,2**(2*k)))*b*(2*pi)**(2*k)/(2*math.factorial(2*k))

def mul_poly(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for j,x in enumerate(a):
        for k,y in enumerate(b): out[j+k]+=x*y
    return out

def bernstein_power(m,N):
    out=[F(0)]*(N+1)
    for j in range(N+1):
        fac=F(j,N)**m*math.comb(N,j)
        for k in range(N-j+1): out[j+k]+=fac*(-1)**k*math.comb(N-j,k)
    return out

def integral_sq(p,lo,hi):
    out=I()
    for a,c in p.items():
        for b,d in p.items():out+=c*d*F(hi**(a+b+1)-lo**(a+b+1),a+b+1)
    return out

def transformed(p):
    a={};e={0:I()}
    for k,c in p.items():
        need(k%2==1,'odd polynomial'); z=Zeven((k+1)//2)
        a[k]=k*c*z; e[0]+=c*z; e[k]=-c*(z-1)
    return a,e

def build():
    need(F(1)+F(1,9)+F(1,25)+F(1,49)+F(1,14)<F(5,4),'Z2 ceiling')
    cutoff=[]
    for j in range(65):
        v=F(j,16)
        need(0<=chi(v)<=1 and abs(dc(v))<=F(3,2),'cutoff bounds')
        if 1<=v<=2:need(chi(v)==-2*v**3+9*v*v-12*v+5,'cutoff expansion')
        cutoff.append([str(v),str(chi(v)),str(dc(v))])
    rows=[];graph=[];Zrows=[]
    for s in (F(1,4),F(1,2),F(3,4)):
        z1,z2=Zstrip(s,128),Zstrip(s,256)
        need(max(z1.a,z2.a)<=min(z1.b,z2.b),'independent cutoff overlap')
        Zrows.append([str(s),z1.encode(),z2.encode()])
        c=cs(s);k0=qp(2,s-1)*(s+3)/s;k1=qp(2,s-1)*(3*(s+1)+24)/s
        K=(1-s)*k0+k1
        for v in (F(1,2),F(1),F(3,2),F(2),F(3),F(4),F(8),F(16),F(32)):
            sm,ds=smooth(s,v)
            R=sm-c*qp(v,1-s)-z2
            Rd=ds-(1-s)*c*qp(v,1-s)
            bd0=k0*qp(v,-s);bd1=k1*qp(v,-s)
            need(R.absmax()<bd0.a and Rd.absmax()<bd1.a,'complete cutoff bound')
            rows.append([str(s),str(v),R.encode(),Rd.encode(),bd0.encode(),bd1.encode()])
        for eps in (F(1,8),F(1,16)):
            for v in (F(1),F(2),F(4),F(8)):
                t=eps*v
                # Literal derivative of the finite dilation sum, not R identity.
                literal=I()
                for n in range(1,math.floor(v)+2,2):
                    u=t/n
                    fp=qp(u,s-2)*((s-1)*chi(u/eps)+(u/eps)*dc(u/eps))
                    literal+=t*fp/(n*n)
                sm,ds=smooth(s,v)
                alt=qp(t,s-1)*((s-1)*sm+ds)
                need(max(literal.a,alt.a)<=min(literal.b,alt.b),'two derivative paths')
                diff=literal-(s-1)*z2*qp(t,s-1)
                bd=K*qp(eps,s)/t
                need(diff.absmax()<bd.a,'graph error envelope')
                graph.append([str(s),str(eps),str(t),literal.encode(),bd.encode()])
    poly=[]
    for m in (2,3,4):
        for N in (m,m+2,8,12):
            h=bernstein_power(m,N)
            # p_N-f: integrate h_N(t^2)-t^(2m).
            h[m]-=1
            p={2*j+1:c/F(2*j+1) for j,c in enumerate(h) if c}
            d=F(m*(m-1),8*N)
            pnorm=integral_sq({k:I(v) for k,v in p.items()},0,1)
            aa,ee=transformed(p)
            anorm,enorm=integral_sq(aa,0,1),integral_sq(ee,1,3)
            need(pnorm.b<=d*d/3,'primitive approximation bound')
            need(anorm.b<25*d*d/48 and enorm.b<8*d*d,'full native continuity bounds')
            # Two evaluations of Bernstein polynomial at every rational grid node.
            for x in [F(j,16) for j in range(17)]:
                coeff=sum(c*x**j for j,c in enumerate(h))+x**m
                basis=sum(F(j,N)**m*math.comb(N,j)*x**j*(1-x)**(N-j) for j in range(N+1))
                need(coeff==basis,'Bernstein representations')
                need(abs(coeff-x**m)<=d,'Bernstein Taylor bound')
            poly.append([m,N,pnorm.encode(),anorm.encode(),enorm.encode(),str(d)])
    return {'schema':SCHEMA,'parent':PARENT,
            'scope':{'full_positive_eta_inequality_proved':False,'rh_proved':False,
                     'zeta_zeros_evaluated':0,'strip_tests_are_not_zeros':True},
            'cutoff_controls':cutoff,'strip_source_enclosures':Zrows,
            'complete_remainder_controls':rows,'literal_derivative_controls':graph,
            'bernstein_native_controls':poly,
            'counts':{'cutoff_values':len(cutoff),'strip_sources':len(Zrows),
                      'complete_remainders':len(rows),'derivative_paths':len(graph),
                      'bernstein_polynomials':len(poly),'bernstein_points':17*len(poly)}}

def raw(x):return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def seal(p):return {'payload':p,'sha256':hashlib.sha256(raw(p)).hexdigest()}
def pairs(xs):
    out={}
    for k,v in xs:
        need(k not in out,'duplicate JSON key');out[k]=v
    return out

def accept(obj,expected):
    need(type(obj) is dict and set(obj)=={'payload','sha256'},'envelope')
    need(type(obj['sha256']) is str and obj['sha256']==hashlib.sha256(raw(obj['payload'])).hexdigest(),'digest')
    need(raw(obj)==raw(expected),'primitive regeneration mismatch')

def tests(expected):
    variants=[]
    for field,value in [('rh_proved',True),('full_positive_eta_inequality_proved',True),('zeta_zeros_evaluated',1),('strip_tests_are_not_zeros',False)]:
        p=copy.deepcopy(expected['payload']);p['scope'][field]=value;variants.append(seal(p))
    for field in ['complete_remainders','derivative_paths','bernstein_points']:
        p=copy.deepcopy(expected['payload']);p['counts'][field]-=1;variants.append(seal(p))
    p=copy.deepcopy(expected['payload']);p['complete_remainder_controls'][0][2][0]='0';variants.append(seal(p))
    p=copy.deepcopy(expected['payload']);p['bernstein_native_controls'].pop();variants.append(seal(p))
    p=copy.deepcopy(expected['payload']);p['parent']='0'*40;variants.append(seal(p))
    for v in variants:
        need(v!=expected,'mutation must change report')
        try:accept(v,expected)
        except ValueError:pass
        else:raise ValueError('corruption accepted')
    return len(variants)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--write',type=Path);ap.add_argument('--check',type=Path);ap.add_argument('--self-test',action='store_true')
    args=ap.parse_args();expected=seal(build())
    if args.write:args.write.write_bytes(raw(expected)+b'\n')
    if args.check:
        obj=json.loads(args.check.read_text(),object_pairs_hook=pairs,parse_float=lambda s:(_ for _ in ()).throw(ValueError('float rejected')))
        accept(obj,expected)
    n=tests(expected) if args.self_test else 0
    print('PASS_AC29_BOUNDED_CONTROLS',expected['sha256'],'rejections='+str(n))
    print(json.dumps(expected['payload']['counts'],sort_keys=True))
if __name__=='__main__':main()
