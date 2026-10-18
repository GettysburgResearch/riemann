"""Independent rational enclosure of the complete divisibility-ray constant.

Logarithms use composite midpoint/trapezoid integration of 1/x. Exponentials
use a positive Taylor series and a geometric tail, followed by reciprocation.
No source checker, transcendental library call, or stored numerical constant
is used. This checks the constant, not the asymptotic arithmetic theorem.
"""
from fractions import Fraction as F
from math import isqrt
import json
import argparse

BITS=100
S=1<<BITS
PANELS=512
TERMS=160

def down(a,b):return a//b
def up(a,b):return -((-a)//b)
def mul(a,b):return (down(a[0]*b[0],S),up(a[1]*b[1],S))
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def scalar(a,b):
    b=F(b)
    if b<0:return (down(a[1]*b.numerator,b.denominator),up(a[0]*b.numerator,b.denominator))
    return (down(a[0]*b.numerator,b.denominator),up(a[1]*b.numerator,b.denominator))

def log_between_one_two(n,d):
    """Bounds log(n/d), 1<=n/d<=2, by convex quadrature."""
    if not d<=n<=2*d:raise ValueError('quadrature interval')
    if n==d:return (0,0)
    # h=(n-d)/(d*PANELS); each h*f is evaluated as one exact rational.
    mid=0
    for j in range(PANELS):
        mid+=down(2*S*(n-d),2*d*PANELS+(2*j+1)*(n-d))
    trap=up(S*(n-d),2*d*PANELS)+up(S*(n-d),2*n*PANELS)
    for j in range(1,PANELS):
        trap+=up(S*(n-d),d*PANELS+j*(n-d))
    return (mid,trap)

LOG2=log_between_one_two(2,1)
def log_integer(n):
    k=n.bit_length()-1;lo,hi=log_between_one_two(n,1<<k)
    return (lo+k*LOG2[0],hi+k*LOG2[1])

def exp_positive(x):
    """Return exp(x) for 0<=x<160, with complete positive-series tail."""
    if x[0]<0 or x[1]>=TERMS*S:raise ValueError('exponential range')
    term=(S,S);total=term
    for j in range(1,TERMS+1):
        term=scalar(mul(term,x),F(1,j));total=add(total,term)
    nxt=scalar(mul(term,x),F(1,TERMS+1))
    # For all remaining terms, the next ratio is at most x_hi/(TERMS+2).
    tail=up(nxt[1]*(TERMS+2)*S,(TERMS+2)*S-x[1])
    return(total[0],total[1]+tail)

def exp_negative(x):
    a=exp_positive(x)
    return (down(S*S,a[1]),up(S*S,a[0]))

def beta_by_trial_division(n):
    value=F(1);p=2
    while p*p<=n:
        if n%p==0:
            power=1
            while n%p==0:n//=p;power*=p
            value*=-F(p*p-1,power*(p+2))
        p+=1
    if n>1:value*=-F(n*n-1,n*(n+2))
    return value

def main(limit):
    total=(S,S)
    for n in range(2,limit+1):
        logn=log_integer(n)
        exponent=add(scalar(logn,F(1,2)),scalar(mul(logn,logn),F(1,8)))
        weight=exp_negative(exponent)
        total=add(total,scalar(weight,2*beta_by_trial_division(n)))
    # Exact full absolute tail: 8 exp(1/2-(log N-2)^2/8)/(log N-2).
    l=log_integer(limit);q=(l[0]-2*S,l[1]-2*S)
    exponent=scalar(mul(q,q),F(1,8))
    exponent=(exponent[0]-S//2,exponent[1]-S//2)
    exp=exp_negative(exponent)
    tail=up(8*exp[1]*S,q[0])
    interval=(total[0]-tail,total[1]+tail)
    if not -F(9,5)*S<interval[0]<interval[1]<-F(17,10)*S:
        raise ValueError('full independent sign gate failed')
    return {'status':'PASS','scope':'infinite L_div constant only; not the energy asymptotic',
      'bits':BITS,'panels':PANELS,'exponential_terms':TERMS,'cutoff':limit,
      'finite_interval_integer':list(total),'tail_upper_integer':tail,
      'full_interval_integer':list(interval),'denominator':S,
      'full_interval_decimal_display':[float(F(x,S))for x in interval],
      'acceptance':'-9/5 < L_div < -17/10',
      'log_method':'convex midpoint/trapezoid rational integrals',
      'exp_method':'positive Taylor sum, full geometric tail, reciprocal'}

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--limit',type=int,default=4096)
    args=parser.parse_args();print(json.dumps(main(args.limit),sort_keys=True,indent=2))
