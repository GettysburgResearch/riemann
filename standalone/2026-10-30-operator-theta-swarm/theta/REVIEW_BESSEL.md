# Independent review of the Bessel boundary packet

Reviewer: arithmetic/operator lane, 30 October 2026.

**Verdict:** the exact recurrence, the self-adjoint realization and its sharp
zero-energy threshold, the local zero theorem, the complete nonnegative
`M<=2` theorem, and the eight exact actual-source `M=3` certificates check at
their stated scopes. The higher-degree numerical material remains exploratory.
There is no proof of the required cofinal boundary sign control, RH, or a new
zero-free region. No worldwide novelty determination is part of this review.

## Frozen scope and hashes

The two proof notes and the two exact-checker source files were read in full.
The exact M3 checker was rerun independently in ordinary and optimized isolated
Python. The diagnostic scripts were inspected, and their report summaries were
compared with the note; those costly exploratory runs were not rerun.

| File | SHA-256 |
|---|---|
| `work_theta/BESSEL_BOUNDARY.md` | `c2e2d3a9db19238d7e802b9f1288546e115d0f6430eb05358ccf4ea92b44498a` |
| `work_spectral/BESSEL_SELFADJOINT_GATE.md` | `f6692c936a5448d47fd5853475c537556cfc20f7a8899a379d9540e2bc3e50f6` |
| `work_theta/verify_bessel_m3.py` | `2623eb5e893cbc7cf764f0855eb72faf494868f6e91afa126bc9ed0166db81a8` |
| `work_theta/verify_polya_obstruction.py` | `cb4f9cb91d4595295974aae955e7782ac9aa8d1fa83c9a4f80f39ae1e7e30989` |
| `work_theta/BESSEL_M3_CERTIFICATE.json` | `d336bb929a85518794306e1a9a8ea52917ebdc0214d9abc17333a54b6e1469a2` |
| `work_theta/BESSEL_M3_CERTIFICATE_OPT.json` | `d336bb929a85518794306e1a9a8ea52917ebdc0214d9abc17333a54b6e1469a2` |
| `work_theta/bessel_jacobi_diagnostic.py` | `7b32d31d23741930877202083e92333e20162fd34dea87b1ef41c745ec861c47` |
| `work_theta/bessel_low_poles_diagnostic.py` | `de65d8984e818b886b62e73f4a66ce6a270d3fcae120adc83c2526a3cff8d555` |
| `work_theta/BESSEL_JACOBI_180.json` | `1c1591f218d9a62c3895a1c23f9a85d6bf25ecebb5e67bb1a73020275f109066` |
| `work_theta/BESSEL_JACOBI_360.json` | `508b1e1ec4ceaccbea2a45540ee34385629697999872a5b3dd3b65272932660e` |
| `work_theta/BESSEL_LOW_POLES_DIAGNOSTIC.json` | `b2fd8b52984c8542c7c6449ca08756ac100f3e9e7c539f1fb67b9792aab99cb1` |

The reviewer outputs `theta_m3_replay.json` and
`theta_m3_replay_optimized.json` have the same `d336bb...` digest as the exact
author certificate. This review supplements the separately frozen
`REVIEW_THETA.md`, which concerns the preceding approximation proof.

## 1. Independent normalization and recurrence check

For the usual argument derivative of K, the order identities give

\[
\begin{aligned}
K_{\nu+1}+K_{\nu-1}&=-2K_\nu',\\
K_{\nu+2}+K_{\nu-2}
 &=(2+4\nu^2/a^2)K_\nu-(4/a)K_\nu',\\
K_{\nu+3}+K_{\nu-3}
 &=(8/a+24\nu^2/a^3)K_\nu
   -(2+16/a^2+8\nu^2/a^2)K_\nu'.
\end{aligned}
\]

These follow by two direct substitutions into
`K_(nu+1)=K_(nu-1)+(2nu/a)K_nu`; the first identity also follows by
differentiating the integral representation. They agree with the note's
polynomial recurrence. The standard identities and the defining Bessel
equation were checked against [DLMF 10.29](https://dlmf.nist.gov/10.29),
[DLMF 10.25](https://dlmf.nist.gov/10.25), and the integral representation
[DLMF 10.32.9](https://dlmf.nist.gov/10.32.E9).

The substitution `y(u)=K_nu(a exp(u))`, `nu^2=-E`, gives
`-y''+a^2 exp(2u)y=Ey` and, crucially, `y'(0)=a K_nu'(a)`.
Thus the note's `M=3` coefficients D0,D1 multiply the argument derivative,
and the radial impedance is exactly

\[
r(E)=a\frac{A_0-A_1E}{D_0-D_1E},\qquad
r'(E)=\frac{a\Delta}{(D_0-D_1E)^2},\qquad
\gamma=-\frac{a\Delta}{D_1^2}.
\]

Both the factor a and the residue sign are correct. The exact checker only
tests Delta, so that harmless positive scale cannot affect its signs.

## 2. Self-adjoint and local arguments

The proposed form has the correct positive boundary mass. Integration by
parts gives

\[
y'(0)=h y(0)+\sum_j\sqrt{\gamma_j}x_j-bE y(0),
\]

while oscillator variation gives
`x_j=sqrt(gamma_j)y(0)/(E-lambda_j)`. In particular the sign preceding bE
must be negative. The domain with the trace coordinate is dense; narrow
functions of prescribed trace approximate independent boundary coordinates
in the ambient norm. The trace estimate makes the finite couplings
infinitesimally form bounded. The confining potential and finite additional
coordinates give the asserted compact resolvent.

The zero/eigenvalue correspondence handles genuine poles correctly:
coprimality forces the numerator to be nonzero at a denominator zero,
and a transform zero there is precisely a Dirichlet bulk eigenvalue. The
corresponding oscillator coordinate supplies the boundary derivative. Distinct
poles rule out oscillator-only eigenvectors. Common polynomial factors are
kept separately, as they must be for statements about every transform zero.

The zero-energy ground-state identity has the sign

\[
\int(|y'|^2+a^2e^{2u}|y|^2)
 =\int w^2|(y/w)'|^2-m_a(0)|y(0)|^2,
\qquad w=K_0(ae^u).
\]

Completing the oscillator squares therefore proves the exact threshold
`r(0)>=m_a(0)`. If that inequality fails, the stated test vector has negative
form value and compact resolvent supplies a negative-energy eigenvalue.
Strict inequality, equality, a genuine pole at zero, pure Dirichlet, and pure
Neumann cases are all treated consistently. The necessity claim applies
within the displayed rational anti-Herglotz class, not to all possible
rational impedances.

The local theorem also checks. The Lagrange identity has the positive sign
`Im(m_a(E))/Im(E)=integral |y_E|^2/|y_E(0)|^2`; hence an anti-Herglotz
boundary function cannot meet it at a nonreal regular point. A pole of the
boundary function cannot create a missed nonreal zero because of coprimality
and the real Dirichlet spectrum. At negative real energy the Bessel value is
strictly positive, so the separate negative-energy condition is sufficient.
The monotonic replacement using `r(0)>=m_a(0)` is valid when the stipulated
pole-free negative interval exists. The local uniform convergence and
expanding-disk Rouché argument do not need global real-rootedness of any
single approximant.

## 3. Exact finite-order conclusions

For `M<=2`, the affine impedance has `h>=0`, `b>=0`; since `m_a(0)<0`,
its entire reduced spectrum is positive. The note correctly includes pure
c1 as Neumann, pure c0 as Dirichlet, and excludes the zero tuple. Thus this
is a complete all-zero statement for every nonzero nonnegative coefficient
tuple at those orders.

For the actual positive `M=3` coefficients, the strict negative Delta signs
at `a=1/4,1/2,1,2,5,10` imply a single positive pole with positive residue
and `r(0)>0`. Strictness also excludes a numerator/denominator cancellation.
These six finite actual-source transforms therefore have only real zeros.
The positive signs at 20 and 50 show failure of this sufficient realization,
and imply no nonreal transform zero.

The fixed-order limit follows already from `c_n/c_0->1`: the leading two
terms of `a^2 Delta` are 24 and -16, giving the stated limit 8. This says
nothing about the required moving regime `M/a->infinity`.

There is a useful independent control for the distinction between gate
failure and root failure. For equal weights c0=c1=c2=c3=1, define the radial
determinant `D=-Delta/a`. Direct algebra gives

\[
D=\frac{-8a^3+48a^2+160a+384}{a^6},\qquad
D(10)=-\frac{1216}{1000000}<0.
\]

The corresponding multiplier polynomial is `1+q+...+q^6`, with every root
on the unit circle; the universal-factor argument in the earlier reviewed
proof still makes its Bessel transform real-rooted. Thus the scalar
anti-Herglotz condition is demonstrably sufficient rather than necessary.

## 4. Certificate contract and numerical boundary

The root-enclosure routine floors exact rational multiples of `10^70` before
applying integer square roots; applying `isqrt` twice gives the correct
fourth-root floor. The upper endpoint is enlarged by one grid unit. Its
inputs in this checker are positive.

For x=n/a>=0, `Y=x+sqrt(1+x*x)>=1` and

\[
\Phi(\tfrac12\operatorname{arsinh}x)
 =\sum_{k\ge1}(4\pi^2k^4Y^2-6\pi k^2Y)Y^{1/4}e^{-\pi k^2Y}.
\]

All terms are positive. For k>=5, each is at most
`40 k^4 Y^(9/4) exp(-3 k^2 Y)`, and consecutive upper bounds have ratio
below one half. Therefore the complete tail bound used by the checker is
valid. Using the lower Y endpoint in the exponential and upper endpoints in
the positive power only enlarges that bound.

The modified-Bessel I series is retained through series index 180. The next
term is followed by a decreasing positive term ratio, and the explicit
geometric bound includes its entire remainder. Division by the strictly
positive c0 interval preserves enclosure. The imported rational interval,
Machin-pi, and exponential primitives were already independently reviewed in
`REVIEW_THETA.md` and were read again here. No float enters a sign decision.

Both isolated executions reproduced all eight strict signs and the exact
rational endpoints byte for byte. This replay shares the author's interval
implementation; it is not advertised as a second transcendental arithmetic
library or a proof-assistant formalization.

The higher-degree table matches the stored reports. All 14 reported pairs
agree between 180 and 360 digits on gate result and first reported failure.
The four low-pole reports contain respectively 6,8,8,8 located real poles,
all with the recorded positive residue signs; the first-pole values in the
note match those reports. The scaled-energy residue conversion in that
script correctly multiplies by a squared.

These comparisons are only integrity checks on exploratory reports. Decimal
rounding is not directed, polynomial division does not certify a gcd, and
searching sign changes cannot count complex poles or multiple real roots.
The note preserves these limitations and does not promote its minute
residues, its sampled signs, or agreement at two precisions into a complete
complex-domain sign proof. The required unbounded local gate remains open.
