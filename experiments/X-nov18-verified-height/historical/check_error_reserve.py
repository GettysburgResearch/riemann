"""Independent directed error budget for the original parameters at the new heights.

Equations and the allocation of the real DC-bin reserve are in error-reserve.md.
"""
from math import factorial
from flint import arb, ctx


def main():
    ctx.prec = 192
    lo, hi = arb(3 * 10**12), arb(3_000_200_000_000)
    pi = arb.pi()
    two = arb(2)
    B, h = arb(5376), arb(116)
    A = arb(512) / 21
    H = arb(13) / 64
    M, K = arb(768000), 23
    tiny = arb("1e-1500")

    def c(sigma, width, k=0):
        m = (sigma - 1) // 2
        a = arb(sigma) + arb(1)/2
        tilt = m/(lo+sigma) + k/a
        return (4*pi*width * (2*pi*a)**k * ((hi+sigma)/2)**m
                * (width**2 * tilt**2 / 2).exp())

    def passed(name, value, limit):
        # Feed the actual binary64 number used by the historical C compiler.
        if not value < arb(float(limit)):
            raise ArithmeticError(f"{name} is too large: {value}, ceiling {limit}")
        print(f"{name} <= {value}", flush=True)

    k = K
    taylor = ((2*M.sqrt()-1) * two**(arb(k+5)/2)*pi**(k+arb(1)/2)
              * h**(k+1) * (arb("0.500021")/B)**k / (arb(k+2)/2).gamma())
    passed("Taylor remainder", taylor, "6.73e-33")
    sigma=1431
    b1=(c(sigma,h)*((two*sigma-1)**2/(8*h*h)).exp()
        * pi**(arb(1-2*sigma)/4) * M**(1-sigma)/(sigma-1)) + tiny
    passed("Dirichlet tail", b1, "2.1e-33")

    v = B**2/(8*h**2)
    g_errors=[]
    for k in range(K):
        x=8*(pi*B)**k/factorial(k)
        g_errors.append(x*((-v).exp()+two**(arb(3*k-1)/2)*(h/B)**(k+1)
                             *v.gamma_upper(arb(k+1)/2)))
    passed("Finite g lattice", max(g_errors), "1.83e-44")

    # Lemmas 5.5.2 and 5.5.3: this covers both frequency aliasing and
    # the hard zeroing of G^(k)/k! past its positive Nyquist endpoint.
    sigma=511
    a=A/4
    s2=2*sigma-1
    exponent=(arb(2*sigma+1)**2/(8*h**2) - a*pi*s2/2).exp()
    alias=max((2*(1+1/(a*pi*s2))*c(sigma,h,k)*exponent+tiny)/factorial(k)
              for k in range(K))
    passed("G frequency alias and omitted G bins", alias, "1e-307")

    sigma=201
    s2=2*sigma-1
    coeff=arb(sigma).zeta()*pi**(arb(1-2*sigma)/4)*c(sigma,h)
    fhead=(coeff*(arb(s2)**2/(8*h**2)-pi*s2*A/8).exp())+tiny
    passed("Padded F frequency tail", fhead, "3.93e-245")
    falias=2*coeff*(arb(s2)**2/(8*h**2)-pi*s2*A/2).exp()*(1+1/(A*pi*s2))+tiny
    passed("F frequency alias", falias, "1e-307")

    # Uniform global growth of the scaled critical-line completed zeta.
    def growth(y):
        return 10**6 + 32*(1+y)**(arb(1)/3)

    # The factor 4 includes both signs and the first-term geometric tail.
    time_alias=4*growth(hi+2*B)*(-B**2/(8*h*h)).exp()
    passed("Time alias", time_alias, "1e-108")

    sigma=3
    s2=2*sigma-1
    band=(4*arb(sigma).zeta()/s2*pi**(arb(-3-2*sigma)/4)*c(sigma,H)
          *(arb(s2)**2/(8*H**2)-pi*A*s2/2).exp())+tiny
    ns=69  # floor allows the old mag-based nearest-node conversion
    truncated=(4*growth(hi+(ns+1)/A)/(pi*ns)
               *(-arb(ns)**2/(2*A**2*H**2)).exp())
    passed("Complete interpolation error", band+truncated, "4e-38")

    # Even permitting 2*M.sqrt()*K missing G bins individually at the
    # (much weaker) bound 1e-307 leaves this reserve in the real DC input.
    dc=arb(float("3.26e-33"))-b1-K*2*M.sqrt()*arb("1e-307")
    node=dc/B-time_alias
    nearest=(2/pi)*(-1/(8*A**2*H**2)).exp()
    if not (dc>arb("1e-33") and node>arb("1.8e-37") and nearest>arb("0.6")
            and node*nearest>band+truncated):
        raise ArithmeticError("Combined DC reserve failed")
    print(f"DC excess {dc}; time-node excess {node}; interpolation coverage {node*nearest}")


if __name__ == "__main__":
    main()
