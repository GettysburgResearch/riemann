# Global wrapper for the degree-12 logistic detector

Status: proposed source-dependent classical logarithmic zero-free
region with R=4.815. This is a new component; the R=4.84 and R=4.82
files remain separate. It neither proves RH nor lowers the distinct
fixed-width Hecke boundary. Human mathematical review is outstanding.

The full analytic and global argument is in LOGISTIC_GLOBAL_WRAPPER.md,
SHA256 acb4b29ef72c031eb78ec27f41c8f4169e648f554a35badc559472077a8b36cb.
Its explicit formula, finite verification to H=3*10^12, published
Littlewood coefficient 21.233, minimum-zero construction, multiplicities
and distant-zero estimates are retained, with the changes checked below.

## 1. Changed detector and scalar obligation

Use the exact degree-12 sum-of-two-squares polynomial in
../three-hour-type/LOGISTIC_POLY12_AND_CURVATURE.md,
SHA256 da4e104b4f4b9b861a4a174c3119c14a91b18583a25fab7102735a648665ca7c.
It has a0=1, every ak>0, a1>1, and aP=sum_(k=1)^12 ak<4.
That note independently proves Carch<-3.003196. Use the weaker
rational upper bound Carch=-3.00317. Its kernel curvature bound and
../three-hour-boundary/LOGISTIC_CURVATURE_51.md give the global estimate
|w(v)-w0|<=(51/2)v^2, including beyond the compact support.

Put K=12, Astar=200/963=1/4.815, Lstar=exp(21.233*Astar),

    c(l)=log(12+10^10 exp(-l)), mu=l/(l+c(l)),
    eta=A/l, sigma=1-A/(l+c(l)), alpha=2sigma-1.

The kernel, exact logistic f, and F are otherwise unchanged. Define
S=a1[F(sigma-1+eta)+F(sigma-eta)]-F(sigma-1).
The sufficient scalar inequality is

    S-eta*w0/2*(aP*l/2-3.00317)-10^(-7)
                         +1.57eta-90eta^3 > 0.          (D-M)

The four-prime lower bound 1.26eta-90eta^3 is proved in
../three-hour-boundary/LOGISTIC_DEGREE12_PRIME_GAIN.md,
SHA256 bccdc8825518319ca252995a9ccab657e18d9ffd468978d9a636f5c19b56054f.
The separate negative real-axis correction E_f(sigma)<=-.31eta is
proved in ../three-hour-type/LOGISTIC_NEGATIVE_ARCHIMEDEAN.md,
SHA256 88d8dba1316e61aa3cd67e2bb81a2c04d1ac114985593ecde9082aeae766182f.
The two favorable linear terms concern different summands of the
explicit formula; their sum is 1.57eta. The cubic remainder is adverse.

The root's certify_logistic_degree12.py, SHA256
350b5dc73787cb6f9925833e19ebaaa9256ed273c44da27e5bb35192be4a83f6,
proves a sufficient lower bound for (D-M) on the closed rectangle

    0<=A<=200/963, 28<=l<=823/10.

Its three-transform Taylor error uses 51 rather than 1000, justified
by the global curvature bound. Its LOGISTIC_DEGREE12_CERTIFICATE.json,
SHA256 667f839a258512acdcba4121d9c0aec7f1c52193c296f349eb6037f33690921f,
has 39 closed boxes and minimum lower bound greater than .00000702.
The independent exact Fraction replay and its binding review are
separate finite-certificate obligations. The A=0 face is only the
continuous scalar extension; the physical detector uses A>0.

## 2. The changed cutoff preserves the analytic budget

The rectangle gives eta<.0075, sigma>.99, alpha>.98 and A<.21;
Lstar<82.3 and log H>28. Thus the adapter's pointwise estimates,
real-axis correction and prime Taylor inequalities all apply.
The coefficient sum aP<4 gives the same weighted bounds for high-
frequency gamma errors, E errors and the isolated pole errors as in
the baseline. The new Carch was evaluated with these exact new ak.
There is no use of the old degree-16 constant or coefficients.

For the distant zeros put T=12t+T0, T0=10^10, q=kt, 1<=k<=12.
Then T>=q+T0 and log(q+T0)<=log T<l+3 for t>=H. The direct
Lehman integration in the baseline therefore again gives

    sum_(gamma>T) [(gamma-q)^(-2)+(gamma+q)^(-2)]
                                         <10^(-9)(l+4).

The pair loss is at most 10eta times this expression, less than
2.4*10^(-9), since eta*l=A<.21 and l>=28. The zero-frequency loss
is unchanged and is below 4*10^(-10). Multiplication by all ak,
including a0=1, costs less than five times the relaxed 10^(-8)
bound. The other errors still total less than the remaining half
of 10^(-7). Retaining the original full 10^(-7) allowance is safe.

## 3. Global consequence

Assume a violating zero for

    Re s > 1-1/(4.815 log|Im s|), |Im s|>=3.            (D-G)

The finite-height input and Littlewood region confine it to
H<|Im s|<exp(Lstar). Choose B=(1-beta)log|gamma| minimal among
zeros in this finite range. Then 0<B<Astar and all zeros above H
have b(rho)>=B, including those outside the finite range.
Use eta=B/log t and sigma=1-B/log(12t+T0).

All zeros with |gamma|<=12t+T0 lie in the paired positivity strip
1-sigma<=beta<=sigma; the verified low zeros do as well. Isolate
the chosen pair at k=1, count multiplicities, and bound the remaining
zeros by Section 2. The explicit formula with the new polynomial and
prime lower bound then gives the reverse of (D-M) at A=B,l=log t.
The certified strict positivity contradicts it. Heights 3 through H
follow from the finite verification, and negative heights by conjugation.

This is the same finite-minimum global argument as the baseline,
with its actual changed cutoff checked. The finite scalar program
certifies only (D-M)'s explicit sufficient lower bound. The conclusion
(D-G) also depends on the separately reviewed analytic and imported
source theorems; it is not an infinite theorem certified solely by code.
