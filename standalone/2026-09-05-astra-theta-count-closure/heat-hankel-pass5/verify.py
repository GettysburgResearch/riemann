#!/usr/bin/env python3
"""Recompute bounded EXACT_RATIONAL controls, not infinite RH assertions.

Standard library only. All arithmetic decisions use Fraction, including
Gaussian rational numbers. Saved result records are compared with strict JSON
types; assertions are not used for acceptance (the checker works under -O).
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path
from typing import Any

@dataclass(frozen=True)
class Q:
    re: F = F(0)
    im: F = F(0)
    def __post_init__(self):
        object.__setattr__(self, 're', F(self.re))
        object.__setattr__(self, 'im', F(self.im))
    @staticmethod
    def of(z):
        return z if isinstance(z, Q) else Q(F(z))
    def __add__(self, z):
        z=Q.of(z); return Q(self.re+z.re,self.im+z.im)
    __radd__=__add__
    def __neg__(self): return Q(-self.re,-self.im)
    def __sub__(self,z): return self+-Q.of(z)
    def __rsub__(self,z): return Q.of(z)+-self
    def __mul__(self,z):
        z=Q.of(z); return Q(self.re*z.re-self.im*z.im,self.re*z.im+self.im*z.re)
    __rmul__=__mul__
    def __truediv__(self,z):
        z=Q.of(z); d=z.abs2()
        if not d: raise ZeroDivisionError('zero Gaussian denominator')
        return self*z.conj()*F(1,d)
    def __rtruediv__(self,z): return Q.of(z)/self
    def __pow__(self,n):
        if type(n) is not int: raise TypeError('integer exponent required')
        if n<0: return (1/self)**(-n)
        a=self; r=Q(1)
        while n:
            if n&1:r=r*a
            a=a*a; n//=2
        return r
    def conj(self): return Q(self.re,-self.im)
    def abs2(self): return self.re*self.re+self.im*self.im
    def real(self):
        if self.im: raise ValueError('expected exactly real number')
        return self.re

COUNTS=Counter()

def check(name, condition):
    if condition is not True: raise ArithmeticError('failed: '+name)
    COUNTS[name]+=1

def matrix_inverse(a):
    n=len(a); b=[[Q.of(v) for v in a[i]]+[Q(int(i==j)) for j in range(n)] for i in range(n)]
    for j in range(n):
        pivot=next((i for i in range(j,n) if b[i][j].abs2()),None)
        if pivot is None: raise ValueError('singular matrix')
        b[j],b[pivot]=b[pivot],b[j]
        t=b[j][j]; b[j]=[x/t for x in b[j]]
        for i in range(n):
            if i!=j:
                t=b[i][j]; b[i]=[x-t*y for x,y in zip(b[i],b[j])]
    return [r[n:] for r in b]

def bilinear(v,a,w,conjugate=False):
    return sum((v[i].conj() if conjugate else v[i])*a[i][j]*w[j]
               for i in range(len(v)) for j in range(len(w)))

def determinant(a):
    b=[[Q.of(v) for v in row] for row in a]; n=len(b); d=Q(1)
    for j in range(n):
        pivot=next((i for i in range(j,n) if b[i][j].abs2()),None)
        if pivot is None: return Q(0)
        if pivot!=j: b[j],b[pivot]=b[pivot],b[j];d=-d
        t=b[j][j];d=d*t
        for i in range(j+1,n):
            z=b[i][j]/t
            for k in range(j+1,n): b[i][k]-=z*b[j][k]
    return d

def inertia(a):
    """Exact symmetric congruence elimination, with 2x2 zero-pivot blocks."""
    a=[[F(Q.of(x).real()) for x in row] for row in a]; pos=neg=zero=0
    while a:
        n=len(a); i=next((i for i in range(n) if a[i][i]),None)
        if i is not None:
            perm=[i]+[j for j in range(n) if j!=i]
            a=[[a[i][j] for j in perm] for i in perm]; p=a[0][0]
            pos+=int(p>0);neg+=int(p<0)
            a=[[a[i][j]-a[i][0]*a[0][j]/p for j in range(1,n)] for i in range(1,n)]
        else:
            pair=next(((i,j) for i in range(n) for j in range(i+1,n) if a[i][j]),None)
            if pair is None: zero+=n;break
            i,j=pair; perm=[i,j]+[l for l in range(n) if l not in pair]
            a=[[a[i][j] for j in perm] for i in perm];p=a[0][1]
            pos+=1;neg+=1
            a=[[a[i][j]-(a[i][0]*a[1][j]+a[i][1]*a[0][j])/p
                for j in range(2,n)] for i in range(2,n)]
    return [pos,neg,zero]

def gram(basis):
    return [[Q(F(math.factorial(r+s),(p+q)**(r+s+1))) for q,s in basis] for p,r in basis]

def values(basis,A):
    return [math.factorial(r)/(A+p)**(r+1) for p,r in basis]

def blaschke(A,basis):
    return math.prod(((A-p)/(A+p) for p,r in basis),start=Q(1))

def h(atoms,p): return sum((w/(A+p) for A,w in atoms),Q(0))

def poly_mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c

def poly_eval(a,z):
    y=Q(0)
    for x in reversed(a):y=y*z+x
    return y

def partial_fractions(num, poles):
    """Proper rational numerator / product(z+b)^d: exact pole coefficients."""
    out={}
    for b,d in poles.items():
        series=[sum(num[j]*math.comb(j,k)*(-b)**(j-k) for j in range(k,len(num))) for k in range(d)]
        for c,e in poles.items():
            if c==b:continue
            factor=[F((-1)**k*math.comb(e+k-1,k),(c-b)**(e+k)) for k in range(d)]
            series=poly_mul(series,factor)[:d]
        for k,x in enumerate(series):
            if x:out[(b,d-k)]=x
    return out

def partial_eval(parts,z):return sum((c/(z+b)**r for (b,r),c in parts.items()),Q(0))

def inv_laplace_inner(p,q):
    return sum(c*d*F(math.factorial(r+s-2),math.factorial(r-1)*math.factorial(s-1)*(b+a)**(r+s-1))
               for (b,r),c in p.items() for (a,s),d in q.items())

def tm_functions(poles):
    num=[F(1)];den=Counter();out=[]
    for b in poles:
        den[b]+=1
        norm=math.isqrt(2*b)
        if norm*norm!=2*b:raise ValueError('fixture needs rational normalization')
        p=[norm*x for x in num]
        out.append((p,dict(den),partial_fractions(p,den)))
        num=poly_mul(num,[-b,1])
    return out

def strict_equal(a:Any,b:Any)->bool:
    if type(a) is not type(b):return False
    if isinstance(a,dict):return a.keys()==b.keys() and all(strict_equal(a[k],b[k]) for k in a)
    if isinstance(a,list):return len(a)==len(b) and all(strict_equal(x,y) for x,y in zip(a,b))
    return a==b

def run():
    COUNTS.clear()
    root=Path(__file__).resolve().parent
    lock=json.loads((root/'SOURCE_LOCK.json').read_text())
    if lock['own_parent']!='634d9a8ec4b0819442e601686a109ff7015b7b0b':
        raise ValueError('wrong parent source lock')
    if lock['read_sources'][0]['commit']!='f22b67db113d1aa4f986fe35a2fc0321fdff7d47' or lock['read_sources'][1]['commit']!='875e8dd47186e924445533513a1ad405af09d7a7':
        raise ValueError('wrong cross-branch source lock')
    atoms=[(Q(7),Q(1)),(Q(12,2),Q(1)),(Q(12,-2),Q(1)),(Q(40,3),Q(1)),(Q(40,-3),Q(1))]
    H=h(atoms,0).real();C=H/(1-H);x0=1/H-1
    check('finite_source_budget',0<H<F(1,2))
    check('finite_source_budget',sum(w.real()/A.re for A,w in atoms)<=C)
    for A,w in atoms:
        check('finite_source_budget', A.re>=x0)
    for p in range(1,9):
        for q in range(1,9):
            direct=sum(w/((A+p)*(A+q)) for A,w in atoms)
            source=(h(atoms,p)-h(atoms,q))/(q-p) if p!=q else sum(w/(A+p)**2 for A,w in atoms)
            check('source_divided_difference',direct==source)
    for k,J in [(1,0),(1,1),(1,2),(2,0),(2,1),(2,2),(3,0)]:
        basis=[(2**j,r) for j in range(J+1) for r in range(2*k)]
        G=gram(basis);Ginv=matrix_inverse(G)
        for A in [Q(3,1),Q(6,2),Q(20,-3),Q(100,5)]:
            v=values(basis,A)
            residual=F(1,2*A.re)-bilinear(v,Ginv,v,True).real()
            claimed=blaschke(A,basis).abs2()*F(1,2*A.re)
            check('confluent_projection_identity',residual==claimed)
            check('confluent_projection_identity',residual>=0)
        Qmat=[[sum(w*v[i]*v[j] for A,w in atoms for v in [values(basis,A)])
               for j in range(len(basis))] for i in range(len(basis))]
        for i,(p,r) in enumerate(basis):
            for j,(q,s) in enumerate(basis):
                parts=partial_fractions([F(math.factorial(r)*math.factorial(s))],Counter({p:r+1})+Counter({q:s+1}))
                observed=sum(coef*sum(w/(A+b)**d for A,w in atoms) for (b,d),coef in parts.items())
                check('safe_source_confluent_matrix',observed==Qmat[i][j])
    for b in [1,2,4,8,16,32]:
        for rr in [F(i,8) for i in range(8,17)]:
            x=b*rr
            for y in [F(j,2) for j in range(-12,13) if F(j,2)**2<=x]:
                A=Q(x,y)
                check('dyadic_strip_ratio',((A-b)/(A+b)).abs2()<=F(1,3))
                check('dyadic_strip_polynomial',x*x-4*b*x+b*b+y*y<=0)
    for R in [1,2,4,16,128]:
        for x in [R+F(1,4),2*R,5*R]:
            for y in [F(0),F(1,2),F(1)]:
                check('safe_tail_resolvent',(1/(Q(x,y)+R)).re>=F(1,5*x))
    params=[]
    for tau in [F(1,100),F(1,10),F(1),F(2),F(10)]:
        prev=-1
        for k in [1,2,4,8,16]:
            J=0
            while tau*2**J<2*k:J+=1
            check('thermal_rank_choice',tau*2**J>=2*k)
            check('thermal_rank_choice',J==0 or tau*2**(J-1)<2*k)
            check('thermal_rank_choice',J>=prev);prev=J
            params.append({'tau':str(tau),'k':k,'J':J,'dimension':2*k*(J+1),'error_upper':str(F(1,3**k))})
    last=None
    for k in range(1,33):
        epsilon=F(1,3**k)+(10+F(5*k,2))*F(1,4**k)
        if last is not None:check('zero_shift_error_decreases',epsilon<last)
        last=epsilon
    # Exact normalization and the source-derivative compiler in an orthonormal frame.
    tm=tm_functions([2,2,8,8,2,32])
    for i,(num,poles,parts) in enumerate(tm):
        for z in [Q(0),Q(3,1),Q(8,-2)]:
            den=math.prod(((z+b)**d for b,d in poles.items()),start=Q(1))
            check('tm_partial_fraction',partial_eval(parts,z)==poly_eval(num,z)/den)
        for j,(num2,poles2,parts2) in enumerate(tm):
            check('tm_metric',inv_laplace_inner(parts,parts2)==int(i==j))
            prod=partial_fractions(poly_mul(num,num2),Counter(poles)+Counter(poles2))
            for z in [Q(1,1),Q(7),Q(15,-3)]:
                check('tm_source_compiler',partial_eval(prod,z)==partial_eval(parts,z)*partial_eval(parts2,z))
            source=sum(c*sum(w/(A+b)**d for A,w in atoms) for (b,d),c in prod.items())
            direct=sum(w*partial_eval(parts,A)*partial_eval(parts2,A) for A,w in atoms)
            check('tm_source_compiler',source==direct)
    # Inertia survives finite background and positive multiplicity changes.
    records=[]
    for q in range(4):
        for mult in [1,2,5]:
            aa=[(Q(3),Q(mult))]
            for j in range(q):
                A=Q(7+4*j,1+j);w=Q(mult+j,j)
                aa.extend([(A,w),(A.conj(),w.conj())])
            n=len(aa);basis=[(2+i,0) for i in range(n)]
            mat=[[sum(w/((A+b)*(A+c)) for A,w in aa) for c,r in basis] for b,s in basis]
            got=inertia(mat);expected=[q+1,q,0]
            check('finite_pair_inertia',got==expected)
            records.append({'pairs':q,'weight':mult,'inertia':got})
    # Generic positive heat does not imply a positive Hankel matrix.
    fake=[Q(1),Q(2,1),Q(2,-1)]
    coeff=[22,-114,70]
    def R(z):return sum(c*math.factorial(j)/(z+1)**(j+1) for j,c in enumerate(coeff))
    check('counterfeit',R(fake[0])==Q(0))
    check('counterfeit',R(fake[1])==Q(0,1))
    check('counterfeit',R(fake[2])==Q(0,-1))
    qvalue=sum(R(A)**2 for A in fake).real()
    norm=sum(F(c*d*math.factorial(i+j),2**(i+j+1)) for i,c in enumerate(coeff) for j,d in enumerate(coeff))
    check('counterfeit',qvalue==F(-2))
    check('counterfeit',norm==697)
    M=[[sum(2*(A-1)**(i+j)/(A+1)**(i+j+2) for A in fake).real() for j in range(3)] for i in range(3)]
    expected=[[F(41,50),F(22,125),F(48,625)],[F(22,125),F(48,625),F(82,3125)],[F(48,625),F(82,3125),F(88,15625)]]
    for row,erow in zip(M,expected):
        for x,y in zip(row,erow):check('counterfeit_matrix',x==y and x>0)
    check('counterfeit_matrix',determinant(M).real()==F(-2,15625))
    check('counterfeit_matrix',inertia(M)==[2,1,0])
    for c in range(5,16):
        Hc=F(1,c)+F(4*c,4*c*c+1)
        upper=(F(1,c)-Hc/2)/2
        check('small_negative_mass_family',Hc<F(1,2))
        check('small_negative_mass_family',upper==F(1,4*c*(4*c*c+1)) and upper<F(1,16*c**3))
        aa=[Q(c),Q(2*c,1),Q(2*c,-1)]
        mat=[[sum(1/((A+b)*(A+d)) for A in aa) for d in [1,2,3]] for b in [1,2,3]]
        check('small_negative_mass_family',inertia(mat)==[2,1,0])
    # Endpoint of the rational explicit-formula test, and metric warning.
    for num,poles,parts in tm:
        endpoint=partial_eval(parts,Q(0)).real()**2
        direct=(poly_eval(num,Q(0))/math.prod((Q(b)**d for b,d in poles.items()),start=Q(1))).real()**2
        check('explicit_formula_endpoint',endpoint==direct)
    check('raw_metric_warning',gram([(1,0)])[0][0]==Q(F(1,2)))
    source_hashes={name:hashlib.sha256((root/name).read_bytes()).hexdigest()
                   for name in ['PROOF.md','CROSS_REVIEW.md','SOURCE_LOCK.json','verify.py']}
    output={'source_hashes':source_hashes,'status':'PASS_HEAT_HANKEL_FINITE_CONTROLS','arithmetic':'EXACT_RATIONAL_AND_GAUSSIAN_RATIONAL',
            'checks':sum(COUNTS.values()),'groups':dict(sorted(COUNTS.items())),
            'thermal_parameters':params,'inertia_fixtures':records,
            'counterfeit':{'quadratic_value':'-2','norm_squared':'697','rayleigh':'-2/697','determinant':'-2/15625'},
            'rh_proved':False,'infinite_analytic_proof_machine_checked':False,'actual_xi_matrix_evaluated':False}
    return output

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',type=Path)
    args=parser.parse_args()
    result=run()
    if args.check:
        saved=json.loads(args.check.read_text())
        if not strict_equal(saved,result):raise SystemExit('REFUSED: saved record does not match strict recomputation')
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__=='__main__':main()
