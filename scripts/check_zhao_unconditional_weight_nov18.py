"""An unconditional 16-prime exclusion test for the completed real-axis weight."""
from functools import cache
from math import comb, factorial
from flint import arb, ctx

DECIMALS = ('.882','-.764','-.336','.345','.802','.023','-1.64','1.1011')


@cache
def signature_term(r1, r2, prec):
    if ctx.prec != prec:
        raise ArithmeticError('Precision changed')
    s = arb(5)/2
    w = list(map(arb,DECIMALS))
    v = w[0]*(1/s+1/(s-1)-((r1+2*r2)/2)*arb.pi().log())
    for k in range(1,len(w)):
        v -= w[k]*(s**(-k-1)+(s-1)**(-k-1))
    for a,count in [(0,r1+r2),(1,r2)]:
        u = (s+a)/2
        v += count*w[0]*u.digamma()/2
        for k in range(1,len(w)):
            v += count*w[k]*arb(k+1).zeta(u)/2**(k+1)
    return v


def field_term(disc,r1,r2):
    return signature_term(r1,r2,ctx.prec) + (arb(DECIMALS[0])/2)*arb(abs(disc)).log()


@cache
def _euler(p, f, limit, prec):
    if ctx.prec != prec:
        raise ArithmeticError('Precision changed')
    if limit < 55:
        raise ValueError('Must include all prime powers through 55')
    q = p**f
    logq = arb(q).log()
    w = list(map(arb,DECIMALS))
    result=arb(0)
    power=q
    j=1
    while power<=limit:
        y=j*logq
        value=-w[0]+sum(w[k]*y**k/factorial(k) for k in range(1,len(w)))
        result+=logq*value/(arb(power)**2*arb(power).sqrt())
        power*=q
        j+=1
    return result


def prime_term(p,f,limit=55):
    """Contribution for one prime ideal of residue degree f above p."""
    return _euler(p,f,limit,ctx.prec)


def certify():
    from sympy import Poly, Rational as Q, oo, symbols
    w=list(map(Q,DECIMALS))
    t=symbols('t')
    s=Q(5,2)
    def check_edge(beta,x,lo,hi):
        a=beta*(1-beta)
        p,q=s-beta,s-1+beta
        m=len(w)
        ep,eq=p*p+x,q*q+x
        h=0
        for v,b in [(p,q),(q,p)]:
            for k,c in enumerate(w):
                re=sum(comb(k+1,2*j)*v**(k+1-2*j)*(-x)**j for j in range((k+1)//2+1))
                h+=(1 if k==0 else -1)*c*re*(v*v+x)**(m-k-1)*(b*b+x)**m/2
        num=Poly(Q('1.0005')*(x+a)*ep**m*eq**m-((a-x)**2+x)*h,t)
        assert num.eval(lo)>0 and num.count_roots(lo,hi)==0
    check_edge(0,t,Q(3,4),oo)
    check_edge(t,Q(3,4),0,Q(1,2))
    euler=Poly(-w[0]+sum(w[k]*t**k/factorial(k) for k in range(1,len(w))),t)
    assert euler.eval(4)>0 and euler.count_roots(4,oo)==0
    print('Both zero-strip edges and the complete Euler tail pass exact rational checks.')


if __name__=='__main__':
    certify()
