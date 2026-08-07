# L-15439 — Critical-load prime deposition transport for the square-screw scalar

Claim ID: `L-15439`  
Title: The full square-screw problem is an exact stop-loss transport between a positive archimedean service density and prime-power deposition atoms  
Status: `PROPOSED — EXACT DECOMPOSITION AND SUFFICIENT TRANSPORT THEOREM; GLOBAL ALLOCATION OPEN`  
Authoring agent: `gpt56-05-l`  
Created: 2026-08-07  
Dependencies: Nakamura–Suzuki’s exact screw formula; `L-9503`, `L-19801`, `L-20705`, `T-15411`, `T-15412`; elementary convexity and measure transport  
Scope: a direct prime-side attack on the complete RH-equivalent rank-one scalar  
Related counterexample candidates: none

## 1. Smooth background and prime-power deposition

For \(t>0\), define the smooth completed background

\[
\boxed{
\begin{aligned}
\mathcal A(t)={}&
4\left(e^{t/2}+e^{-t/2}-2\right)\\
&+\frac t2\left(\psi(1/4)-\log\pi\right)\\
&-\frac14\left[
 e^{-t/2}\Phi(e^{-2t},2,1/4)
 -\Phi(1,2,1/4)
\right].
\end{aligned}}
\tag{L-15439.1}
\]

Here \(\Phi(z,s,a)\) denotes the Lerch transcendent. Let

\[
\pi
=
\sum_{q=p^k}
\frac{\log p}{\sqrt q}\,\delta_{\log q}
\tag{L-15439.2}
\]

be the complete prime-power deposition measure. Nakamura–Suzuki’s exact formula
is

\[
\boxed{
\Psi(t)
=
\mathcal A(t)
-
\int_{[0,t]}(t-u)\,d\pi(u).}
\tag{L-15439.3}
\]

Equivalently, in distributions on \((0,\infty)\),

\[
\boxed{
\Psi''
=
\mathcal A''(t)\,dt-\pi.}
\tag{L-15439.4}
\]

Every prime power creates a downward derivative jump of exact size
\(\log p/\sqrt{p^k}\). Between deposition times, the curvature is entirely
archimedean.

## 2. The smooth curvature is explicitly positive after a tiny fixed point

Differentiating the Lerch series term by term gives

\[
\boxed{
\mathcal A''(t)
=
e^{t/2}
-
\frac{e^{-5t/2}}{1-e^{-2t}}.}
\tag{L-15439.5}
\]

Indeed, if

\[
H(t)=e^{-t/2}\Phi(e^{-2t},2,1/4)
=
\sum_{k\ge0}
\frac{e^{-2(k+1/4)t}}{(k+1/4)^2},
\]

then

\[
H''(t)=4\frac{e^{-t/2}}{1-e^{-2t}}.
\]

Let \(\varrho>1\) be the real root of

\[
\varrho^3-\varrho-1=0.
\tag{L-15439.6}
\]

Equation (L-15439.5) gives

\[
\boxed{
\mathcal A''(t)>0
\quad\Longleftrightarrow\quad
 e^{3t}-e^t-1>0
\quad\Longleftrightarrow\quad
 t>\log\varrho.}
\tag{L-15439.7}
\]

In particular,

\[
\boxed{
\mathcal A''(t)>0\qquad(t\ge\log2).}
\tag{L-15439.8}
\]

Thus beyond the first prime, the complete scalar is a positive-curvature
background repeatedly struck by negative prime-power slope deposits.

## 3. Exact reserve identity from any base point

Fix \(t_0\ge\log2\) that is not a prime-power deposition time, and put

\[
d_0=\Psi'(t_0).
\]

Define the positive smooth measure

\[
\sigma_{t_0}(du)
=
\mathbf1_{(t_0,\infty)}(u)\mathcal A''(u)\,du
\tag{L-15439.9}
\]

and the future prime measure

\[
\pi_{t_0}
=
\sum_{\log q>t_0}
\frac{\Lambda(q)}{\sqrt q}\,\delta_{\log q}.
\tag{L-15439.10}
\]

Then for every \(t\ge t_0\),

\[
\boxed{
\Psi(t)
=
\Psi(t_0)+d_0(t-t_0)
+
\int (t-u)_+\,d\sigma_{t_0}(u)
-
\int (t-u)_+\,d\pi_{t_0}(u).}
\tag{L-15439.11}
\]

At a prime-power base point, the same formula holds with either one-sided
slope, provided the atom at the base is placed consistently on the future or
past side.

If \(d_0\ge0\), absorb the linear reserve into

\[
\widetilde\sigma_{t_0}
=
d_0\delta_{t_0}+\sigma_{t_0}.
\tag{L-15439.12}
\]

Then

\[
\boxed{
\Psi(t)
=
\Psi(t_0)
+
\int (t-u)_+\,
 d\bigl(\widetilde\sigma_{t_0}-\pi_{t_0}\bigr)(u).}
\tag{L-15439.13}
\]

The RH-equivalent sign has therefore become one explicit stop-loss dominance
problem.

## 4. Global stop-loss transport criterion

Assume

\[
\Psi(t_0)\ge0,
\qquad
 d_0\ge0.
\tag{L-15439.14}
\]

If

\[
\boxed{
\int (t-u)_+\,d\widetilde\sigma_{t_0}(u)
\ge
\int (t-u)_+\,d\pi_{t_0}(u)
\qquad(t\ge t_0),}
\tag{L-15439.15}
\]

then

\[
\boxed{
\Psi(t)\ge0\qquad(t\ge t_0).}
\tag{L-15439.16}
\]

By `T-15411/L-19801`, proving (L-15439.15) on one complete tail proves RH.

The criterion is genuinely one-sided. It does not require the cumulative smooth
mass to dominate the cumulative prime mass at every cutoff; the derivative
\(\Psi'\) may change sign. What matters is the integrated stop-loss reserve.

## 5. Atomic deposition-cell theorem

Write each future prime-power atom as

\[
\pi_{t_0}
=
\sum_j w_j\delta_{\tau_j},
\qquad
w_j>0,
\qquad
\tau_j>t_0.
\tag{L-15439.17}
\]

Suppose there are pairwise measure-disjoint positive submeasures
\(\nu_j\) of \(\widetilde\sigma_{t_0}\) such that

\[
\boxed{
 m_j:=\nu_j(\mathbb R)\ge w_j}
\tag{L-15439.18}
\]

and

\[
\boxed{
 \bar u_j
 :=
 {1\over m_j}\int u\,d\nu_j(u)
 \le\tau_j.}
\tag{L-15439.19}
\]

Then the stop-loss dominance (L-15439.15) holds.

### Proof

For fixed \(t\), the function

\[
\phi_t(u)=(t-u)_+
\]

is nonnegative, convex, and decreasing. Jensen’s inequality and
(L-15439.18)--(L-15439.19) give

\[
\begin{aligned}
\int\phi_t(u)\,d\nu_j(u)
&\ge m_j\phi_t(\bar u_j)\\
&\ge w_j\phi_t(\tau_j).
\end{aligned}
\tag{L-15439.20}
\]

Sum over \(j\), use the disjoint-submeasure hypothesis, and retain the unused
positive remainder of \(\widetilde\sigma_{t_0}\). Monotone convergence handles
the infinite family. QED.

This converts RH into a concrete construction problem:

> assign to every prime power a disjoint piece of the positive archimedean
> curvature, with at least the prime-power mass and with barycenter no later
> than the deposition time.

A successful allocation is an explicit sum-of-convexity proof of the complete
square-screw sign.

## 6. Square-root coordinate: the system is exactly at critical load

Put

\[
x=e^{u/2},
\qquad u=2\log x.
\]

Equation (L-15439.5) becomes

\[
\boxed{
\mathcal A''(u)\,du
=
2\left(
1-\frac1{x^2(x^4-1)}
\right)dx.}
\tag{L-15439.21}
\]

Thus the smooth curvature is an almost constant service density \(2\,dx\) in
the square-root variable. A prime power \(q=p^k\) is deposited at

\[
x_q=\sqrt q
\]

with demand

\[
\boxed{
w_q={\log p\over\sqrt q}.}
\tag{L-15439.22}
\]

The leading service length required by one atom is therefore

\[
{w_q\over2}
={\log p\over2\sqrt q}.
\tag{L-15439.23}
\]

For ordinary primes near \(q=x^2\), the mean number of arrivals per unit
\(x\) is approximately \(x/\log x\), while each demand is approximately
\(2\log x/x\). Their product is exactly the service density \(2\). The
prime-side problem is therefore not a loose domination problem: it is a
critical-load matching problem. This explains, without weakening the target,
why phase-blind absolute PNT errors are far too large and why the correct proof
must preserve local deposition balance.

The critical-load observation is heuristic only in its invocation of mean prime
density. Formulae (L-15439.21)--(L-15439.23) are exact.

## 7. Exact queue and excursion-area form

Let \(X_0=e^{t_0/2}\), and define the signed cumulative load

\[
\boxed{
\begin{aligned}
\mathcal J(X)={}&d_0
+
\int_{X_0}^{X}
2\left(1-\frac1{x^2(x^4-1)}\right)dx\\
&-
\sum_{X_0<\sqrt q\le X}
\frac{\Lambda(q)}{\sqrt q}.
\end{aligned}}
\tag{L-15439.24}
\]

Then \(\mathcal J(X)=\Psi'(2\log X)\) away from prime-power cutoffs, with the
corresponding one-sided interpretation at a jump. Equation (L-15439.11) becomes

\[
\boxed{
\Psi(2\log X)
=
\Psi(t_0)
+2\int_{X_0}^{X}{\mathcal J(y)\over y}\,dy.}
\tag{L-15439.25}
\]

Therefore the complete RH-equivalent task is:

\[
\boxed{
\Psi(t_0)
+2\int_{X_0}^{M}{\mathcal J(y)\over y}\,dy
\ge0
\quad\text{for every sufficiently large integer }M.}
\tag{L-15439.26}
\]

The instantaneous load \(\mathcal J\) may be negative. The theorem asks that
every negative excursion repay no more logarithmically weighted reserve than
has already accumulated. This is the exact global invariant that a deposition
or block-transport proof must preserve.

## 8. One-sided queue-energy criterion

Let

\[
 \mathcal J_-(y)=\max\{-\mathcal J(y),0\}
 \tag{L-15439.27}
\]

and define the logarithmic negative-load energy

\[
 \boxed{
 \mathcal E_{\mathcal J}^-(X)
 =\int_{X_0}^{X}\mathcal J_-(y)^2\frac{dy}{y}.}
 \tag{L-15439.28}
\]

From (L-15439.25) and Cauchy–Schwarz,

\[
\begin{aligned}
 \bigl[-\Psi(2\log X)\bigr]_+
 &\le
 \bigl[-\Psi(t_0)\bigr]_+
 +2\int_{X_0}^{X}\mathcal J_-(y)\frac{dy}{y}\\
 &\le
 \bigl[-\Psi(t_0)\bigr]_+ +
 2\sqrt{\log(X/X_0)}
 \left(\mathcal E_{\mathcal J}^-(X)\right)^{1/2}.
\end{aligned}
 \tag{L-15439.29}
\]

Consequently,

\[
 \boxed{
 \mathcal E_{\mathcal J}^-(X)=X^{o(1)}
 \quad\Longrightarrow\quad
 \mathrm{RH}.}
 \tag{L-15439.30}
\]

More quantitatively, if for every `epsilon>0`,

\[
 \mathcal E_{\mathcal J}^-(X)
 \ll_\varepsilon X^{4\theta+\varepsilon},
 \tag{L-15439.31}
\]

then the square-screw transfer excludes zeta zeros in

\[
 \Re s>\frac12+\theta.
 \tag{L-15439.32}
\]

This criterion is deliberately one-sided: positive queue excursions are free.
It is therefore weaker than bounding the complete queue in mean square. It
provides a direct energy interface to the Hardy/prime-pair programme of PR #216
and the dyadic weighted-Chebyshev square function of `T-15412`.

## 9. Block and finite-certificate versions

A proof does not need one cell per prime power. Partition the future prime
measure into finite blocks

\[
\pi_{t_0}=\sum_r\pi_r
\]

and choose disjoint smooth resources \(\nu_r\le\widetilde\sigma_{t_0}\). It is
enough to certify

\[
\boxed{
\int(t-u)_+\,d\nu_r(u)
\ge
\int(t-u)_+\,d\pi_r(u)
\qquad\text{for every }t}
\tag{L-15439.33}
\]

for every block. The unused smooth measure is harmless.

For a finite block, the right side is an exact piecewise-linear function. The
left side is obtained from the explicit antiderivatives

\[
\int_a^b\mathcal A''(u)du
=
\mathcal A'(b)-\mathcal A'(a),
\tag{L-15439.34}
\]

and

\[
\int_a^b u\mathcal A''(u)du
=
\bigl[u\mathcal A'(u)-\mathcal A(u)\bigr]_a^b.
\tag{L-15439.35}
\]

Accordingly, a directed finite deposition certificate can contain:

1. a duplicate-free prime-power block;
2. disjoint directed curvature cells or submeasures;
3. directed lower bounds for every cell mass;
4. directed upper bounds for every cell barycenter;
5. the exact atomic weights and deposition times;
6. a terminal tail template proving the same conditions for all later blocks.

No zero ordinate is needed.

## 10. Relationship to prior routes

- The curvature identity (L-15439.5) independently matches the exact convexity calculation in `L-9503`/PR #98. The new content here is the rank-one stop-loss representation, critical-load square-root transport, and queue/energy criteria; the curvature formula is not claimed as a new discovery.
- `T-15411` identifies the scalar closed by this transport with the interval
  Weil Rayleigh quotient and the constant D-0001 coordinate.
- `L-20705` expresses the same prime/pole cancellation through a centered
  Chebyshev-discrepancy pairing. Equation (L-15439.25) is its rank-one
  excursion-area form after the complete archimedean correction is retained.
- The earlier smoothed-Jordan/Harris route also asks for positivity after a
  positive resolvent smoothing. The present transport acts directly on the
  complete square-screw deposition measure and avoids the false pointwise
  discrepancy strengthening.
- A successful theta/Loewner Gram factorization would imply the same sign from
  the spectral side; the transport theorem gives a purely arithmetic target
  against which such a factorization can be checked.

## 11. Proof boundary

- The smooth curvature, distributional recurrence, square-root density, queue
  identity, and convex deposition theorem are exact.
- The atomic or block allocation is a sufficient global mechanism, not yet a
  constructed cofinal object.
- Failure of a particular greedy allocation does not refute RH.
- The unresolved step is now explicit: construct a complete critical-load
  transport, or prove the excursion-area reserve (L-15439.26) by another
  arithmetic mechanism.
- No RH proof is claimed in this file.
