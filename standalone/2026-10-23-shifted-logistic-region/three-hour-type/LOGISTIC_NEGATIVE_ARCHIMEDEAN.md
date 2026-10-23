# A uniform negative archimedean correction for the logistic weight

2026-10-21. This strengthens the separate real-axis estimate without
changing the frozen baseline certificate. The idea and finite-sum
parameters were supplied by the parent agent; the sign/order of the
inequalities and exact rational constants were independently checked.

Under theta=1.1338, 0<eta<=.0075, .99<=sigma<=1, let a=2sigma-1 and
b=sigma+2. The earlier exact certificate gives w0>5.67 and
||w''||<350. The global Taylor estimate, valid for the compact extension,
is |w(eta u)-w0|<=175 eta^2 u^2. Thus

    [f0-f(u)]/eta
       <= -(w0/2)tanh(a u/2)+175 eta^2 u^2.

Insert this into the exact integral for E_f(sigma). Since a>=.98,
b<=3, and tanh is nonnegative and increasing, the magnitude of the
negative integral is at least

    (5.67/2) integral_0^infinity
       exp(-3u)tanh(.49u)/(1-exp(-2u))du.

Only after replacing the exponential in this nonnegative integrand
do we use tanh x>=x-x^3/3 for x>=0. Its proof is that the derivative
of tanh x-x+x^3/3 is x^2-tanh(x)^2>=0. This order matters: the cubic
polynomial itself becomes negative for large u.

The integral is therefore at least

    I=.49 sum_(n>=0)(3+2n)^-2
                 -2*.49^3 sum_(n>=0)(3+2n)^-4.

For a lower bound retain the first100 positive terms in the first
sum. For the second, retain the first100 terms and bound its tail by
the integral from99 to infinity, namely 1/[6*201^3]. The checker
`verify_logistic_negative_arch.py` gives exactly

    I > .1098466966,
    (5.67/2)I > .3114153849.

For the positive correction use

    1/(1-exp(-2u)) <= 1+1/(2u),   b>=2.99,

so it is at most

    175 eta^2 [2/b^3+1/(2b^2)] < .00128704636.

All comparisons are rational after the elementary analytic bounds.
Their difference is greater than .31. Consequently

    E_f(sigma) <= -.31 eta.

The checker also rejects .32 as unsupported by these particular
coarse constants. This is a uniform analytic improvement to one term
of the detector; it is not by itself a new zero-free theorem.
