"""High precision Decimal exploration, NOT directed/certified arithmetic.

Energy variable x=E/a^2 improves polynomial scaling. All coefficient weights
are reconstructed from the literal theta source. J-fraction sign extraction
avoids polynomial root finding but is still precision-sensitive.
"""
from decimal import Decimal as D, localcontext
from math import factorial
from pathlib import Path
import json,sys

def pi_value():
    # Machin series evaluated with ordinary Decimal rounding.
    def arct(q):
        term=D(1)/q; s=term; k=0
        while True:
            k+=1; term=-term/(q*q); z=term/(2*k+1)
            old=s;s+=z
            if s==old:return s
    return 16*arct(D(5))-4*arct(D(239))

def trim(x):
    while len(x)>1 and not x[-1]:x.pop()
    return x

def add(x,y):
    z=[D(0)]*max(len(x),len(y))
    for j,v in enumerate(x):z[j]+=v
    for j,v in enumerate(y):z[j]+=v
    return trim(z)

def scale(x,c):return trim([v*c for v in x])

def mul_linear(x,c0,c1):return add(scale(x,c0),[D(0)]+scale(x,c1))

def divmod_poly(num,den):
    r=num[:]; q=[D(0)]*max(1,len(r)-len(den)+1)
    for j in range(len(r)-len(den),-1,-1):
        q[j]=r[j+len(den)-1]/den[-1]
        for k,v in enumerate(den[:-1]):r[j+k]-=q[j]*v
        r[j+len(den)-1]=D(0)
    return trim(q),trim(r)

def phi_from_x(x,pi):
    y=abs(x)+(1+x*x).sqrt(); y4=y.sqrt().sqrt(); total=D(0)
    for k in range(1,50):
        kk=D(k*k);term=(4*pi*pi*kk*kk*y*y-6*pi*kk*y)*y4*(-pi*kk*y).exp()
        old=total;total+=term
        if total==old:return total
    return total

def bessel_i(n,a):
    term=(a/2)**n/D(factorial(n));total=term;k=0
    while True:
        k+=1;term*=a*a/(4*k*(n+k));old=total;total+=term
        if total==old:return total

def polynomials(a,M,pi):
    c=[bessel_i(n,a)*phi_from_x(D(n)/a,pi) for n in range(M+1)]
    base=c[0];c=[v/base for v in c]
    pp,qq=[D(1)],[D(0)];p,q=[D(0),D(1)],[-1/a]
    A=[D(1)];B=[D(0)]
    for n in range(1,M+1):
        ae=[2*v*(-1)**j for j,v in enumerate(p[::2])]
        be=[2*v*(-1)**j for j,v in enumerate(q[::2])]
        A=add(A,scale(ae,c[n]));B=add(B,scale(be,c[n]))
        pn=add(pp,mul_linear(p,2*D(n)/a,D(2)))
        qn=add(qq,mul_linear(q,2*D(n)/a,D(2)))
        pp,p=p,pn;qq,q=q,qn
    return trim(A),trim(B)

def inspect(a,M,precision):
    with localcontext() as ctx:
        ctx.prec=precision;pi=pi_value();A,B=polynomials(a,M,pi)
        quo,P=divmod_poly(scale(A,-1),B);Q=B
        row={'a':str(a),'M':M,'precision':precision,'r0':str(-A[0]/B[0]),'polynomial_part':[str(v) for v in quo]}
        row['polynomial_gate']=len(quo)<=2 and (len(quo)<2 or quo[1]<=0)
        stages=[];prevbeta=D(0);prevpivot=None;failure=None
        if not row['polynomial_gate']:failure='positive linear polynomial part'
        if P==[D(0)]:row.update({'stages':[],'failure':failure,'gate':failure is None});return row
        for j in range(M//2+2):
            if len(Q)!=len(P)+1:
                failure=f'nonproper degree at stage {j}';break
            gamma=P[-1]/Q[-1]
            if gamma<=0:
                failure=f'nonpositive residue mass at stage {j}';stages.append({'stage':j,'gamma':str(gamma)});break
            quot,R=divmod_poly(scale(Q,gamma),P)
            if len(quot)!=2:failure=f'Jacobi quotient degree at stage {j}';break
            alpha=-quot[0]/quot[1]
            pivot=alpha if prevpivot is None else alpha-prevbeta/prevpivot
            stages.append({'stage':j,'gamma':str(gamma),'alpha':str(alpha),'LDL_pivot':str(pivot),'slope':str(quot[1])})
            if pivot<=0 and failure is None:failure=f'nonpositive pole LDL pivot at stage {j}'
            if R==[D(0)]:break
            # next F = -R/P = beta^2*m_next
            nextP=scale(R,-1);nextQ=P
            prevbeta=nextP[-1]/nextQ[-1] if len(nextQ)==len(nextP)+1 else D(0)
            prevpivot=pivot;P,Q=nextP,nextQ
        row.update({'stages':stages,'failure':failure,'gate':failure is None})
        return row

if __name__=='__main__':
    precision=int(sys.argv[1]) if len(sys.argv)>1 else 180
    pairs=[(1,3),(5,3),(10,3),(20,3),(1,8),(5,8),(20,20),(50,20),(10,30),(10,50),(20,60),(20,100),(50,150),(50,250)]
    rows=[]
    for a,M in pairs:
        row=inspect(D(a),M,precision);rows.append(row)
        print(a,M,'gate',row['gate'],'failure',row['failure'],'stages',len(row['stages']),flush=True)
    Path(__file__).with_name('BESSEL_JACOBI_'+str(precision)+'.json').write_text(json.dumps({'scope':'ordinary Decimal arithmetic, no directed certification','rows':rows},indent=2)+'\n')
