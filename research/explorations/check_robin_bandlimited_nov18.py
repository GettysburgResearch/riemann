"""Verify the bandlimited tangent budget. Requires python-flint 0.9.0."""
from flint import arb, ctx


def main():
    ctx.prec = 144
    one = arb(1)
    H = arb(3)*10**12
    pi = arb.pi()
    a = arb("0.0001")
    first = arb(10)**38
    last = arb("1.5")*10**48
    L = first.log()
    scale = L/(L-a)
    slope = one + 1/(L-a)
    b = pi/H
    assert a > 2*b
    tau = 16/(H*a)**3
    first_tail = 23/(H**3*a**2)
    variance = b*b/(1-tau)
    epsilon = (tau+2*first_tail+2*(2*a).exp()*b*b)/(1-tau)
    assert epsilon < arb("3e-24")

    curvature = last.sqrt()*variance*a.exp()*scale*slope/2
    low = arb("0.047")*(a/2).exp()*scale*slope
    high = arb("3.1e-12")*(last.sqrt()*epsilon*(1+1/L)
                            +(2*a).exp()*scale*(2+1/(L-a))/first.sqrt())
    arch = (2*pi).log()*a.exp()*scale/first.sqrt()
    lower_v = first*(-a).exp()
    eta = arb("0.000001")
    assert lower_v.sqrt().log() > 30
    assert arb("0.0244") / lower_v.sqrt().log()**3 < eta
    powers = 1+eta+2*lower_v**(-one/6)+2*lower_v.log()*lower_v**(-one/4)/arb(2).log()
    prime = 2*powers*scale*slope*(a/2).exp()
    total = curvature+low+high+arch+prime

    ell = L-a
    cutoff_ratio = 10000
    assert cutoff_ratio*(2*lower_v).sqrt() < lower_v/2
    qlog = (ell+arb(2).log())/2
    cost = (-a/2).exp()*L/(L+a)*arb(2).sqrt()/(1+arb(2).log()/ell)
    cost *= (1-eta)+(1-eta)*(1-1/qlog-one/cutoff_ratio)-2*eta
    print("band leakage",epsilon,"variance",variance)
    print("total upper cost",total,"lower exponent budget",cost)
    assert total < cost


if __name__ == "__main__":
    main()
