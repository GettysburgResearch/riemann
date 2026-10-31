"""Source polynomial routines copied from the reviewed PR #1026 Decimal diagnostic.
Ordinary rounded arithmetic, not interval certification.
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

