"""Additional reflected-phase counterexamples in nonidentity square classes."""
from flint import acb, arb, arb_series, ctx, dirichlet_char


def logarithmic_derivatives(s, a):
    q = 11
    jet = arb_series([s,1], prec=2)
    values = [jet.zeta(arb(r)/q, deflate=True) for r in range(1,q)]
    total = acb(0)
    for j in range(2,q):
        chi = dirichlet_char(q,j)
        v = sum(chi(r)*h[0] for r,h in enumerate(values,1))
        d = sum(chi(r)*h[1] for r,h in enumerate(values,1))
        total += chi(a).conjugate()*(arb(q).log()-d/v).conjugate()
    if s==2:
        z = jet.zeta()
        total -= z[1]/z[0]
    assert total.imag.contains(0)
    return total.real


def test(a,x):
    q = 11
    answer = (arb(x).log()+1-arb.const_euler()-1/(2*arb(x))
              + logarithmic_derivatives(1,a) - x*logarithmic_derivatives(2,a))
    sieve = bytearray([1])*(x+1)
    for p in range(2,x+1):
        if not sieve[p]:
            continue
        for n in range(p*p,x+1,p):
            sieve[n] = 0
        n = p
        while n<=x:
            factor = 1 if p==q else (q-1)*int(n*a % q == 1)
            if factor:
                answer += arb(p).log()*(factor*(x-n))/n**2
            n *= p
    margin = arb(x).sqrt()*answer-arb(4)/3
    assert margin > 0
    return margin


if __name__=='__main__':
    ctx.prec=96
    for a,x in ((3,3079),(9,27701)):
        print(a,x,test(a,x))
