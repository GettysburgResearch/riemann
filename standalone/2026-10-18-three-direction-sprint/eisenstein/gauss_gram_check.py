"""Exact finite Eisenstein Gram conventions; no asymptotic spectral bound is inferred."""
from fractions import Fraction as F
from pathlib import Path
from math import gcd,isqrt
import json,hashlib
from gauss_phase_check import add,mul,norm,conjugate,prime,field_data,UNITS,ZERO
from angular_check import smallest_primes,ideal_squarefree

def req(v,msg):
    if not v:raise ArithmeticError(msg)

def primaries(cap):
    bnd=isqrt(2*cap)
    return [(a,b) for b in range(-bnd,bnd+1) if b%3==0
            for a in range(-bnd,bnd+1) if (a-1)%3==0
            and 0<a*a-a*b+b*b<=cap and gcd(a*a-a*b+b*b,6)==1]

def divides(p,u):
    t=mul(u,conjugate(p));q=norm(p)
    return t[0]%q==0 and t[1]%q==0

def power(a,k):
    out=(1,0)
    for _ in range(k):out=mul(out,a)
    return out

class E:
    __slots__=('a','b')
    def __init__(self,a=0,b=0):self.a,self.b=F(a),F(b)
    @staticmethod
    def of(v):return v if isinstance(v,E) else E(v)
    def __add__(self,o):o=E.of(o);return E(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self):return E(-self.a,-self.b)
    def __sub__(self,o):return self+-E.of(o)
    def __mul__(self,o):
        o=E.of(o);return E(self.a*o.a-self.b*o.b,self.a*o.b+self.b*o.a-self.b*o.b)
    __rmul__=__mul__
    def inv(self):
        n=self.a*self.a-self.a*self.b+self.b*self.b
        req(n!=0,'zero field inverse');return E((self.a-self.b)/n,-self.b/n)
    def __truediv__(self,o):return self*E.of(o).inv()
    def eq(self,o):o=E.of(o);return self.a==o.a and self.b==o.b
    def dump(self):return [str(self.a),str(self.b)]

def det(mat):
    a=[[E(x.a,x.b) for x in row] for row in mat];ans=E(1)
    for k in range(len(a)):
        pivot=next((j for j in range(k,len(a)) if not a[j][k].eq(0)),None)
        req(pivot is not None,'singular Gram minor')
        if pivot!=k:a[k],a[pivot]=a[pivot],a[k];ans=-ans
        z=a[k][k];ans=ans*z
        for j in range(k+1,len(a)):
            q=a[j][k]/z
            for l in range(k,len(a)):a[j][l]=a[j][l]-q*a[k][l]
    return ans

def main():
    cap=1024;spf=smallest_primes(cap);allrows=primaries(cap)
    prows=[]
    for p in allrows:
        q=norm(p);r=isqrt(q)
        if prime(q):prows.append((p,q,False))
        elif r*r==q and prime(r) and r%3==2:prows.append((p,r,True))
    prows.sort(key=lambda t:(norm(t[0]),t[0]))
    data={p:field_data(p,r,inert) for p,r,inert in prows}
    rows=[u for u in allrows if 128<=norm(u)<256 and ideal_squarefree(*u,norm(u),spf)]
    req(len(rows)>10,'nonempty full squarefree row annulus')
    p7=next(p for p,r,i in prows if norm(p)==7)
    p13=next(p for p,r,i in prows if norm(p)==13)
    labels=[(1,0),p7,conjugate(p7),p13,power(p7,2),power(p7,3),power(p7,5)]
    factors={};factorchecks=0
    for u in rows:
        fs=[p for p,r,i in prows if divides(p,u)]
        prod=(1,0)
        for p in fs:prod=mul(prod,p)
        req(prod==u,'complete primary ideal factorization');factors[u]=fs;factorchecks+=1
    chars=[];zeros=0
    for u in rows:
        row=[]
        for R in labels+[power(p7,6)]:
            z=(1,0)
            for p in factors[u]:
                q=norm(p);r=isqrt(q);inert=(r*r==q)
                _,_,ch,_,_=data[p]
                if inert:v=(R[0]%r,R[1]%r)
                else:
                    root=(-p[0]*pow(p[1],-1,q))%q;v=(R[0]+R[1]*root)%q
                z=mul(z,ch(v,1))
            if z==ZERO:zeros+=1
            else:req(z in UNITS,'sextic character not a sixth root')
            row.append(z)
        req(row[-1]==(ZERO if divides(p7,u) else (1,0)), 'sixth power retains its zero mask')
        chars.append(row[:-1])
    G=[]
    for i in range(len(labels)):
        gr=[]
        for j in range(len(labels)):
            z=ZERO
            for row in chars:z=add(z,mul(conjugate(row[i]),row[j]))
            gr.append(E(*z))
        G.append(gr)
    for i in range(len(labels)):
        req(G[i][i].b==0 and G[i][i].a>0,'diagonal positive real count')
        for j in range(len(labels)):
            req(G[j][i].eq(E(G[i][j].a-G[i][j].b,-G[i][j].b)),'Hermitian Gram')
    minors=[]
    for k in range(1,len(labels)+1):
        d=det([row[:k] for row in G[:k]])
        req(d.b==0 and d.a>0,'exact finite Gram positive definite');minors.append(str(d.a))
    req(zeros>0 and G[0][0].a>G[1][1].a,'nonunit-zero mutation control')
    payload=[[v.dump() for v in row] for row in G]
    out={'status':'PASS','scope':'Finite exact Gram/zero conventions only; no asymptotic conditioning inferred.',
         'row_annulus':[128,256],'complete_squarefree_rows':len(rows),'factorizations_checked':factorchecks,
         'sixth_power_free_labels':labels,'nonunit_zero_cases':zeros,
         'diagonal_counts':[str(G[i][i].a) for i in range(len(G))],
         'positive_leading_Gram_determinants':minors,
         'exact_Gram_sha256':hashlib.sha256(json.dumps(payload,separators=(',',':')).encode()).hexdigest()}
    Path(__file__).with_name('GAUSS_GRAM_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
