# ORACLES — Epstein–Eisenstein moduli lab (E1)

Arithmetic class: **NON_DIRECTED_HIGH_PRECISION** (stated truncation bounds,
non-directed floating rounding). dps = 40 (45 where noted). RH is **not** established
and nothing here claims it; "zero" always means "numerically located to the stated
precision". All oracles must pass before any experiment output is trusted.

Convention validated here (see `lab.py` docstring for the derivation):
`Lambda_z(s) = -1/s - 1/(1-s) + sum_{(m,n)!=0} [(pi Q)^{-s} Gamma(s, pi Q) + (pi Q)^{s-1} Gamma(1-s, pi Q)]`,
sum over **all** nonzero (m,n), **no** extra factor 1/2; `Lambda_z(s) = pi^{-s} Gamma(s) Z_z(s)`.

| oracle | statement | measured | threshold | pass |
|---|---|---|---|---|
| O0a | enumerator count Q<=10 at z=i vs brute-force double loop | 36 = 36 | exact | PASS |
| O0b | theta_z(1/t) = t theta_z(t) at t=0.7, 1.3 (z=i and 0.13+1.07i) | max diff 1.75e-46 | < 1e-30 | PASS |
| O0c | incomplete-gamma engine vs independent Fourier/Bessel engine (3 pts) | rel 1.53e-37 | < 1e-28 | PASS |
| O1 | direct lattice sum at z=i, s=2+0.5i, radius 2000 + tail estimate | 17.7 digits | >= 15 digits | PASS |
| O2 | Z_i(s) = 4 zeta(s) beta(s) at s=0.7+3i, 0.5+14i | 45.3, 39.4 digits | >= 20 digits | PASS |
| O3 | \|Lambda_z(s) - Lambda_z(1-s)\| at 10 fixed points, z=i and generic | incgamma: exact 0 (manifest); fourier engine: max 5.61e-45 | < 1e-25 | PASS |
| O4 | \|Im Lambda_z(1/2+it)\| at t=5, 13.7, 22.3, generic z | incgamma: exact 0 (manifest); fourier engine: max 6.27e-49 | < 1e-25 | PASS |
| O5 | Lambda_i zeros include the first beta zero and first zeta zero | beta 8.88e-16, zeta 0.00e+00 | < 1e-6 | PASS |

O3/O4 note: in the incomplete-gamma representation the functional equation and the
reality on the line are MANIFEST (the two summands of each lattice term swap under
s -> 1-s, and conjugate cancellation is bitwise), so those diffs are exact zeros by
construction; the quoted Fourier-engine numbers are the non-trivial checks, routed
through a genuinely independent computation (divisor-sum identity + K_nu = K_-nu).

O1 tail scheme: r2 divisor sieve to N=R^2=4e6; head n<=5e4 in mpmath dps 35; mid part in exactly-rounded double sums (math.fsum); tail s*pi*N^{1-s}/(s-1) - (A(N)+1)*N^{-s} with EXACT A(N) (the +1 removes the mean -1 of P = E_gauss - 1 from the excluded origin), triangular(Cesaro)-averaged over 257 truncation points N-256000..N step 1000; empirical averaging spread 5.05e-15.
O2 also cross-checks beta(s) = 4^(-s)(zeta(s,1/4) - zeta(s,3/4)) against the alternating
series (Richardson/Shanks): 46.1 digits.
O5 independent references: first zero of the completed Dirichlet beta located by bisection
at t = 6.020948904698; first zeta zero from mpmath.zetazero(1)
at t = 14.134725141735.

Note (spec discrepancy, resolved by the spec's own oracle): the inline table
"r(n)=4,4,0,4,8,0,0,4,4,4 for n=1..10" contains a typo at n=10; r2(10)=8
(10 = 1+9 has representations (+-1,+-3),(+-3,+-1)). The brute-force double loop —
the designated oracle — gives 36 for the count at X=10, and the divisor sieve agrees.

Context: that Epstein zeta functions of non-arithmetic / class-number > 1 forms have
off-critical-line zeros is classical (Davenport–Heilbronn; Potter–Titchmarsh; real zeros:
Bateman–Grosswald, Stark), and the zero-collision/departure phenomenon in one-parameter
Epstein families is published (Arenstorf–Brewer 1993; Travenec–Samaj arXiv:1909.07112;
Betermin–Samaj–Travenec arXiv:2110.09368). These oracles only certify this lab's
implementation against arithmetic ground truth; they claim no new mathematics.
