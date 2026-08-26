# The compact boundary field is an exact near-correlation RH criterion

Status: **exact prefix-energy, compact-ratio correlation, and RH-equivalence
theorem; no bound for the off-diagonal correlation and no proof of RH or
GRH**

Bounded exact replay:
[`ffps_boundary_field_near_correlation_criterion.py`](ffps_boundary_field_near_correlation_criterion.py).
Canonical summary:
[`ffps_boundary_field_near_correlation_criterion.json`](ffps_boundary_field_near_correlation_criterion.json).

Frozen source: the compact boundary-shell theorem at
`9e19e27614e473b3b7d06cfc3d51f92eb39ff009`.  Every imported Markdown,
producer, JSON, and test blob is pinned by the replay.

## 0. Outcome

Let

\[
 a_n={\beta(n)\over\sqrt n},
 \qquad
 \beta(n)=\mu(n)-1_{67\mid n}\mu(n/67),
\]

and let `K_bd` be the nonzero compact-BV primitive of the extra-notched
kernel.  It is supported in `[0,A]`, where

\[
 A=4\log2.
\]

For `X>=1`, define the finite prefix field

\[
 G_X(t)=\sum_{n\le X}a_nK_{\rm bd}(t-\log n)
\tag{0.1}
\]

and its complete energy

\[
 \mathcal E(X)=\int_{\mathbf R}|G_X(t)|^2\,dt.
\tag{0.2}
\]

Put

\[
 \mathcal R(u)=\int_{\mathbf R}
 K_{\rm bd}(v)K_{\rm bd}(v+u)\,dv.
\tag{0.3}
\]

Then finite Fubini gives the exact positive Gram identity

\[
 \boxed{
 \mathcal E(X)=
 \sum_{m,n\le X}{\beta(m)\beta(n)\over\sqrt{mn}}
 \mathcal R\!\left(\log{m\over n}\right).}
\tag{0.4}
\]

The autocorrelation `R` is even, continuous, positive definite, and
supported in `[-A,A]`.  Therefore every nonzero term in (0.4) satisfies

\[
 \boxed{{1\over16}\le {m\over n}\le16.}
\tag{0.5}
\]

The prefix energy is itself an exact RH criterion:

\[
 \boxed{
 \mathrm{RH}
 \Longleftrightarrow
 \mathcal E(X)=X^{o(1)}.}
\tag{0.6}
\]

No estimate in (0.6) is proved here.  The theorem converts the boundary-field
criterion into one compact-ratio two-point correlation target.

## 1. Exact Gram expansion

The sum in (0.1) is finite and `K_bd` is bounded and compactly supported, so
expanding (0.2) and interchanging the finite sum and integral is automatic.
For each pair,

\[
\begin{aligned}
 &\int_{\mathbf R}K_{\rm bd}(t-\log m)
 K_{\rm bd}(t-\log n)\,dt\\
 &\qquad=\int_{\mathbf R}K_{\rm bd}(v)
 K_{\rm bd}\!\left(v+\log{m\over n}\right)dv
 =\mathcal R\!\left(\log{m\over n}\right),
\end{aligned}
\]

which proves (0.4).  Autocorrelations of real `L^2` functions are even and
positive definite.  Translation is continuous in `L^2`, so `R` is
continuous.  Two translates of functions supported in `[0,A]` have disjoint
support when `|u|>A`; this proves (0.5).

The identity is a positive quadratic form even though individual
off-diagonal values of `R` and individual source products may have either
sign.  Taking absolute values before the assembled Gram sum would discard
the RH-bearing cancellation.

## 2. Why prefix energy is equivalent to RH

Let the complete causal boundary field be

\[
 G(t)=\sum_{n\ge1}a_nK_{\rm bd}(t-\log n).
\]

### RH implies the prefix bound

Under RH, the classical normalized beta partial sums satisfy, for every
`epsilon>0`,

\[
 A_\beta(x):=\sum_{n\le x}{\beta(n)\over\sqrt n}
 =O_\varepsilon(x^\varepsilon).
\tag{2.1}
\]

Stieltjes summation against one compact-BV translate of `K_bd`, with the
source truncated at `X`, gives the uniform bound

\[
 \sup_t|G_X(t)|=O_\varepsilon(X^\varepsilon).
\tag{2.2}
\]

The prefix field is supported in `[0,log X+A]`.  Hence

\[
 \mathcal E(X)
 \ll_\varepsilon(1+\log X)X^{2\varepsilon}=X^{o(1)}.
\tag{2.3}
\]

### The prefix bound implies RH

Put `X=e^T`.  Causality gives

\[
 G_X(t)=G(t)\qquad(0\le t\le T),
\tag{2.4}
\]

because a source index larger than `e^T` cannot reach an earlier logarithmic
time.  Therefore

\[
 \int_0^T|G(t)|^2dt\le\mathcal E(e^T)=e^{o(T)}.
\]

Cauchy--Schwarz gives

\[
 \int_0^T|G(t)|dt
 \le T^{1/2}\left(\int_0^T|G(t)|^2dt\right)^{1/2}
 =e^{o(T)}.
\]

The source-locked boundary-shell theorem says that this `L1` statement is
equivalent to RH.  This proves (0.6).

## 3. The diagonal is already harmless

Write

\[
 \mathcal E(X)=\mathcal D(X)+\mathcal O(X),
\]

where `D` is the diagonal `m=n` and `O` is the signed off-diagonal sum.  Since
`K_bd` is nonzero,

\[
 \mathcal R(0)=\|K_{\rm bd}\|_2^2>0,
\]

and

\[
 \mathcal D(X)=\mathcal R(0)
 \sum_{n\le X}{\beta(n)^2\over n}.
\tag{3.1}
\]

The square source has the exact Dirichlet series

\[
 \sum_{n\ge1}{\beta(n)^2\over n^s}
 ={\zeta(s)\over\zeta(2s)}
 {1+4\,67^{-s}+67^{-2s}\over1+67^{-s}}.
\tag{3.2}
\]

Indeed, away from `67` the local factor is `1+p^(-s)`, while the `67`-adic
coefficients are `(1,4,1,0,...)`.  Consequently

\[
 \sum_{n\le X}{\beta(n)^2\over n}
 ={2379\over2278\,\zeta(2)}\log X+O(1),
\tag{3.3}
\]

and the diagonal is only logarithmic.

It follows exactly that

\[
 \boxed{
 \mathrm{RH}
 \Longleftrightarrow
 |\mathcal O(X)|=X^{o(1)}.}
\tag{3.4}
\]

If the energy is subpower, subtracting the logarithmic diagonal gives the
off-diagonal bound.  Conversely, (3.1)--(3.3) plus an off-diagonal subpower
bound make the nonnegative energy subpower, and (0.6) applies.

Thus the smallest quadratic target exposed by this packet is

\[
 \boxed{
 \left|
 \sum_{\substack{m,n\le X\\m\ne n\\1/16\le m/n\le16}}
 {\beta(m)\beta(n)\over\sqrt{mn}}
 \mathcal R\!\left(\log{m\over n}\right)
 \right|=X^{o(1)}.}
\tag{3.5}
\]

This is a signed compact-ratio beta correlation.  It is not supplied by a
diagonal large sieve, an unsigned divisor bound, or the boundary telescope.

## 4. Research use

Equation (3.5) is better adapted to the family/amplifier programme than the
one-sided Jordan statement because it is already an assembled quadratic
form.  It suggests three concrete attacks:

1. decompose the ratio band into prime-factor incidence shells while keeping
   the signed Gram kernel intact;
2. express `beta=lambda*lambda` before opening the square and look for a
   relative/projector cancellation common to both copies;
3. compare the compact-ratio kernel with bilinear Möbius estimates, while
   remembering that any bound strong enough for (3.5) is RH-equivalent.

The result does not make the estimate routine.  Its value is localization:
the remaining direct-RH burden is one explicit off-diagonal correlation, not
an unspecified positivity phenomenon.

## 5. Proof and scope ledger

| statement | grade |
|---|---|
| prefix Gram identity and ratio-16 support | **PROVED EXACT** |
| RH equivalence of prefix `L2` energy | **PROVED EXACT FROM THE LOCKED BOUNDARY THEOREM** |
| beta-square Euler product and logarithmic diagonal | **PROVED EXACT / STANDARD PARTIAL SUMMATION** |
| off-diagonal criterion (3.4)--(3.5) | **PROVED EXACT EQUIVALENCE** |
| subpower off-diagonal estimate | **OPEN; EQUIVALENT TO RH** |
| family/sheaf realization of the correlation | **OPEN** |
| RH or GRH | **NOT PROVED** |

Equivalent criteria for RH are common, and no external novelty claim is made
without a dedicated literature comparison.  The project-specific content is
the source-locked compact-ratio Gram kernel and its interface with the
physical family-amplifier lane.

## 6. Bounded replay

```text
python -B research/l-families/atlas/function_field/ffps_boundary_field_near_correlation_criterion.py --check
python -B -O research/l-families/atlas/function_field/ffps_boundary_field_near_correlation_criterion.py --check
python -B -m unittest tests.test_ffps_boundary_field_near_correlation_criterion
python -B -O -m unittest tests.test_ffps_boundary_field_near_correlation_criterion
```

The replay checks every frozen source blob, the exact beta-square local
factors and first 512 coefficients, the exceptional Euler-factor ratio, a
finite exact Gram/autocorrelation identity, and all scope/resource guards.
It enumerates no zeta zero, finite field, curve, conductor family, or
`L`-function.
