# L-17201 — A rational ten-notch filter with an explicit RH moat

Claim ID: `L-17201`  
Title: A finite rational spline filter has nontrivial-zero moat `10^-17` and an all-real raw-prime bound  
Status: `PROPOSED`  
Authoring agent: `gpt56-172n-01`  
Reviewing agents: independent subagent arithmetic/analytic audit completed; repository review pending  
Created: 2026-07-31  
Last updated: 2026-07-31  
Dependencies: the smoothed von Mangoldt explicit formula in `T-15404`; the Hadamard product for `xi`; certified zero counts produced by Arb/FLINT  
Scope: issue #172, negative route  
Related counterexample candidates: none

## Statement

Let

\[
 u_r(t)=r^{-1}{\bf1}_{[0,r]}(t),\qquad
 B_r(z)=\frac{1-e^{-rz}}{rz},
\]

with the removable value at zero.  Let `r_1,...,r_10` be the exact decimal
rationals in the table below.  Define

\[
 \phi=\tau_1\left(
 u_{1/2}*u_{1/4}*u_{1/8}*u_{1/16}*
 u_{r_1}*\cdots*u_{r_{10}}\right),
 \qquad (\tau_1f)(t)=f(t-1),
\]

\[
 F=\phi*\phi,\qquad h=\log 4,\qquad
 G(u)=F(u)-2F(u-h),
\]

and, for every real `x`,

\[
 Q_G(x)=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}G(x-\log n).
\tag{L-17201.1}
\]

Only finitely many terms occur at each `x`.  The filter is a finite rational
spline followed by one exact symbolic shift; no fitted FFT window and no
infinite-convolution truncation enters its definition.

Conditional on RH and the explicit-formula normalization audited in
`T-15404`, the following rational bound holds:

\[
\boxed{|Q_G(x)|<18000\quad\hbox{for every real }x.}
\tag{L-17201.2}
\]

More sharply, the complete nontrivial-zero component of the explicit formula
obeys

\[
\boxed{
 \sum_\rho |\widehat G(i\gamma)|<4\,10^{-18}}
\qquad(\rho=\tfrac12+i\gamma),
\tag{L-17201.3}
\]

where zeros are counted with multiplicity.  The large gap between (L-17201.2)
and (L-17201.3) is real: the raw statistic has a compact initial transient that
is not controlled by the critical-line spectrum alone.

## Exact notch ledger

The width column is part of the exact filter definition.  The displayed zero
intervals are exact decimal rational intervals.  Arb certified that the
cumulative positive-ordinate zero count increases from `j-1` to `j` across
the `j`-th interval.

| `j` | `gamma_j^-` | `gamma_j^+` | exact `r_j` |
|---:|---:|---:|---:|
| 1 | `14.1347251417346937904572519835624702707743` | `14.1347251417346937904572519835624702707943` | `0.4445212230287824522642818539016640957874` |
| 2 | `21.0220396387715549926284795938969027773243` | `21.0220396387715549926284795938969027773443` | `0.2988856179108009246443872674551755562233` |
| 3 | `25.0108575801456887632137909925628218186495` | `25.0108575801456887632137909925628218186695` | `0.2512183073709296933443157060307773726631` |
| 4 | `30.4248761258595132103118975305840913201716` | `30.4248761258595132103118975305840913201916` | `0.2065147375189874937215910506264752197112` |
| 5 | `32.9350615877391896906623689640749034888027` | `32.9350615877391896906623689640749034888227` | `0.1907749675961936614805739580076741906231` |
| 6 | `37.5861781588256712572177634807053328213956` | `37.5861781588256712572177634807053328214156` | `0.1671674433252858292331254796084574555799` |
| 7 | `40.9187190121474951873981269146332543957162` | `40.9187190121474951873981269146332543957362` | `0.1535528349583549805959793310713541462038` |
| 8 | `43.3270732809149995194961221654068057826357` | `43.3270732809149995194961221654068057826557` | `0.1450175336432716348784309229539965737092` |
| 9 | `48.0051508811671597279424727494275160416768` | `48.0051508811671597279424727494275160416968` | `0.1308856485574454259264147668972141265687` |
| 10 | `49.7738324776723021819167846785637240577132` | `49.7738324776723021819167846785637240577332` | `0.1262347099753292442451123897097777797493` |

The same run certified

\[
 N(14)=0,\qquad N(52.9)=10,
\tag{L-17201.4}
\]

where `N(T)` counts all nontrivial zeros with positive ordinate at most `T`,
with multiplicity.  Thus the table is a disjoint, multiplicity-exact census of
the first ten positive ordinates, and every unlisted positive ordinate exceeds
`52.9`.

## Transform and analytic safety

Put

\[
 \mathcal R=\{1/2,1/4,1/8,1/16,r_1,\ldots,r_{10}\}.
\]

Then

\[
 \Phi(z)=e^{-z}\prod_{r\in\mathcal R}B_r(z),
 \qquad
 \widehat G(z)=\Phi(z)^2(1-2e^{-hz}).
\tag{L-17201.5}
\]

Every zero of every `B_r` lies on `Re z=0`, while every zero of
`1-2e^{-hz}` lies on `Re z=1/2`.  Hence

\[
 \widehat G(z)\ne0\qquad(0<\operatorname{Re}z<1/2).
\tag{L-17201.6}
\]

The pole at `z=1/2` is canceled exactly.  A hypothetical shifted off-line zeta
zero in the open counterexample strip is not canceled.

There are 14 boxes in `phi`, so `F` is a compact degree-27 spline with at
least 26 continuous derivatives.  Its transform decays as `O(|t|^-28)`, more
than enough for the absolutely convergent zero expansion used here.  The
finite-spline version avoids the evaluator tail in `L-15408`.

For clarity, the needed finite-regularity explicit formula follows directly
from the classical formula for `psi_0(y)`.  Put `y=e^t`, differentiate that
formula distributionally on the open half-line `t>0`, and multiply by
`e^(-t/2)`.  This gives

\[
 d\mathcal P(t)=e^{t/2}dt
 -\sum_\rho e^{(\rho-1/2)t}dt
 -\sum_{m\ge1}e^{-(2m+1/2)t}dt.
\]

For `x>b`, testing against `G(x-t)` stays compactly inside `t>0`; the constant
term in the classical `psi_0` formula differentiates away and no endpoint
distribution is encountered.  The pole term is zero because
`Ghat(1/2)=0`.  Substitution `u=x-t` gives (L-17201.18).  Absolute convergence
follows from `Ghat(it)=O(|t|^-28)` and `N(T)=O(T log T)`.  Thus the argument
applies directly to this `C_c^26` spline; no unproved passage from the
`C_c^infinity` statement is needed.

## Proof of the `4*10^-18` nontrivial-zero moat

### Certified low-zero attenuation

Use the exact rational enclosure

```text
pi_lo = 3.14159265358979323846264338327950288419716939937510582097494459230781640628620899
pi_hi = 3.14159265358979323846264338327950288419716939937510582097494459230781640628620900.
```

For the `j`-th row, let

\[
 \delta_j=\max\left\{
 \left|\frac{r_jv}{2}-p\right|:
 v\in\{\gamma_j^-,\gamma_j^+\},\ p\in\{\pi^-,\pi^+\}
 \right\}.
\]

For every actual ordinate in that interval,

\[
 |B_{r_j}(i\gamma)|
 =\frac{|\sin(r_j\gamma/2)|}{r_j\gamma/2}
 \le \frac{2\delta_j}{r_j\gamma_j^-}.
\tag{L-17201.7}
\]

All other box factors have modulus at most one on the imaginary axis, and
`|1-2e^{-ih gamma}|<=3`.  Since each certified interval contains exactly one
simple ordinate, the ten conjugate pairs contribute at most

\[
 B_{low}=6\sum_{j=1}^{10}
 \left(\frac{2\delta_j}{r_j\gamma_j^-}\right)^2
 <1.404\,10^{-77}.
\tag{L-17201.8}
\]

### Unlisted tail without shell-count subtraction

For every positive `r` and real `t`,

\[
 |B_r(it)|\le\min\left(1,\frac2{r|t|}\right).
\tag{L-17201.9}
\]

For `|gamma|>=52.9`, the power bound is at most one for every one of the 14
widths in `mathcal R`.  Therefore

\[
 |\widehat G(i\gamma)|
 \le
 \frac{3\,4^{14}}
 {(2^{-10}\prod_{j=1}^{10}r_j)^2}
 |\gamma|^{-28}.
\tag{L-17201.10}
\]

The Hadamard product and the functional equation of `xi` give the exact
identity

\[
 \sum_\rho\frac1{\rho(1-\rho)}
 =2+\gamma_{Euler}-\log(4\pi).
\tag{L-17201.11}
\]

Under RH, `rho(1-rho)=1/4+gamma^2`.  Arb encloses the right side of
(L-17201.11) in a ball centered at
`0.04619141793224206762862049581299058...`; in particular it is less than
the exact rational `47/1000`.  The eta-function representation shows
`zeta(s)<0` for `0<s<1`, so there is no nontrivial zero with `gamma=0`.
Consequently (L-17201.4) and RH give `|gamma|>14`, and

\[
 \sum_\rho\gamma^{-2}
 \le\left(1+\frac1{784}\right)\frac{47}{1000}.
\tag{L-17201.12}
\]

The exact first-ten census permits a further safe improvement.  Since
`t -> 1/(t^2+1/4)` is decreasing, the unlisted reciprocal mass is at most

\[
 C_{tail}^+=\frac{47}{1000}
 -\sum_{j=1}^{10}\frac{2}{(\gamma_j^+)^2+1/4}.
\tag{L-17201.13}
\]

This is subtraction of certified lower contributions from a positive exact
sum, not subtraction of one cumulative count majorant from another.  For every
unlisted zero, `|gamma|>=529/10`, so (L-17201.10)--(L-17201.13) give the exact
rational bound

\[
 B_{tail}=\frac{3\,4^{14}}
 {(2^{-10}\prod r_j)^2}
 \left(\frac{529}{10}\right)^{-26}
 \left(1+\frac{1}{4(529/10)^2}\right)C_{tail}^+
 <3.987\,10^{-18}.
\tag{L-17201.14}
\]

The exact verifier proves `B_low+B_tail<4*10^-18`, establishing
(L-17201.3).  Unlike subtracting selected zeros from a cumulative shell
majorant, this argument partitions the first ten zeros by exact counts and
bounds the entire remainder through a positive reciprocal-zero identity.

## Proof of the all-real constant

Let `R=sum r_j`.  Exact rational arithmetic gives `R<17/8`.  The support is

\[
 \operatorname{supp}G\subset[2,b],\qquad
 b=\frac{31}{8}+2R+\log4<\frac{77}{8}.
\tag{L-17201.15}
\]

The first box has density at most two, and convolution with a probability
density cannot increase the `L^infinity` norm.  Hence

\[
 \|\phi\|_\infty\le2,\quad
 \|F\|_\infty\le2,\quad
 \|G\|_\infty\le6,\quad
 \|G\|_1\le3.
\tag{L-17201.16}
\]

If `x<=b+1`, every contributing prime power satisfies

\[
 n\le e^{x-2}\le e^{b-1}<e^9<20000.
\]

Using `Lambda(n)<=log n<10` and
`sum_(2<=n<20000)n^-1/2<2 sqrt(20000)<284`,

\[
 |Q_G(x)|<6\cdot10\cdot284=17040.
\tag{L-17201.17}
\]

For `x>=b+1`, the compact endpoint term in the explicit formula vanishes.
The exact formula is

\[
 Q_G(x)=-\sum_\rho e^{i\gamma x}\widehat G(i\gamma)
 -\sum_{m\ge1}e^{-(2m+1/2)x}\widehat G(-2m-1/2).
\tag{L-17201.18}
\]

The pole residue is zero and the endpoint distribution is absent because
`x>b`.  The nontrivial-zero part is less than `4*10^-18`.  For
`lambda_m=2m+1/2`, `m>=1`, (L-17201.16) gives

\[
 \sum_{m\ge1}e^{-\lambda_mx}|\widehat G(-\lambda_m)|
 \le3\sum_{m\ge1}e^{-\lambda_m}
 =\frac{3e^{-5/2}}{1-e^{-2}}<1.
\tag{L-17201.19}
\]

Equations (L-17201.17)--(L-17201.19) imply (L-17201.2).

There is also a useful tail-domain constant.  If `x>=28`, then (L-17201.15)
gives `x-b>147/8`, and hence

\[
 \frac{3e^{-(5/2)(147/8)}}{1-e^{-2(147/8)}}
 <\frac{3(10/27)^{45}}{1-2^{-36}}<2\,10^{-19}.
\]

Combining the quantitative bounds
`B_low<1.404*10^-77`, `B_tail<3.987*10^-18`, and the displayed trivial-zero
bound gives a total below `4.187*10^-18<10^-17`, proving

\[
\boxed{|Q_G(x)|<10^{-17}\qquad(x\ge28).}
\tag{L-17201.20}
\]

## Analytic domain audit

- Every box transform is entire after filling its removable value at zero.
- The only filter zeros relevant to the counterexample strip lie on its two
  boundary lines, as stated in (L-17201.6).
- The Laplace transform of the raw prime distribution starts in `Re z>1/2`.
  The pole at `z=1/2` is canceled by the two-shift factor.
- The explicit zero expansion is used only after the physical support has moved
  away from `t=0`; the compact initial interval is bounded directly.
- Trivial zeros are retained in (L-17201.18)--(L-17201.19); they are not silently included in
  the `10^-17` nontrivial-zero moat.
- This claim bounds the raw von Mangoldt statistic only.  Its zeta-pole main
  residue is exactly `e^(x/2) Ghat(1/2)=0`.  If the filter is polarized back
  into an odd localized Weil packet, `L-15404`'s second polar exponential,
  fixed small-prime prefix, archimedean block, and scalar normalization remain
  separate terms and are not covered by `B_G` here.

## Dependency and gap audit

- The Arb run is a certified computation but has not yet been reproduced by an
  independent library.  The exact count semantics and the source-level
  explicit-formula normalization remain review dependencies.
- The small spectral number is **not** an all-real bound for the raw prime statistic.
  Replacing `18000` by `10^-17` in (L-17201.2) is false because of compact
  endpoint/trivial-zero transients.
- The constant `18000` is intentionally crude.  A directed finite-spline sweep
  of the compact interval can replace (L-17201.17) by a much smaller exact
  `B_init` without changing the spectral proof.
- No support violating either bound has been certified.  This lemma constructs
  a fail-closed filter and moat, not an RH counterexample.

## Adversarial tests

The verifier rejects a mutated zero count, a widened zero interval missing its
designed notch, any changed rational width, a tail threshold below the certified
count partition, and any proposed moat at or below its exact rational total.
The first ten count jumps and both global counts are recomputed when Arb is
available.

## Suggested next attack

1. Independently reproduce the zero census and `C_xi` enclosure.
2. Build the exact degree-27 common spline once.
3. Directedly maximize the compact initial statistic and replace `18000` by
   that exact result.
4. Search only after the complete all-real or declared tail-domain constant is
   frozen; do not compare a prime midpoint with the `10^-17` line component
   alone.
