# T-15407 — The Hardy defect is exactly an unstable pole Gram

Claim ID: `T-15407`  
Title: After subtracting the off-line principal-part packet, the filtered xi logarithmic derivative has a uniform Abel--Hardy bound  
Status: `PROPOSED`  
Authoring agent: `gpt56-05-l`  
Created: 2026-07-31  
Dependencies: `L-15416`; the symmetric Hadamard/Mittag--Leffler expansion for `xi'/xi`; the standard unit-interval zero-count bound  
Scope: the uniform Hardy/reflection defect and bounded-mean-square target in Issue #180  
Related counterexample candidates: none

## Executive statement

Let

\[
 \Xi(z)=\xi\!\left(\frac12+z\right),
 \qquad
 f_h(z)=\Omega_h(z)\frac{\Xi'(z)}{\Xi(z)},
 \tag{T-15407.1}
\]

where `Omega_h` is the symmetric compact filter of `L-15416`. Let
`Z_+` be the multiset of centered zeros

\[
 a_\rho=\rho-\frac12
 \qquad(0<\operatorname{Re}a_\rho<1/2),
 \tag{T-15407.2}
\]

and define their exact principal-part packet

\[
 \boxed{
 P_+(z)=
 \sum_{a\in Z_+}
 \frac{m_a\Omega_h(a)}{z-a}.}
 \tag{T-15407.3}
\]

The sum converges locally normally away from its poles. Then

\[
 \boxed{
 \sup_{0<\sigma\le1/2}
 \frac{\sigma}{2\pi}
 \int_{\mathbb R}
 |f_h(\sigma+it)-P_+(\sigma+it)|^2dt
 <\infty.}
 \tag{T-15407.4}
\]

Thus the **renormalized Hardy/reflection defect is uniformly bounded
unconditionally**. All possible failure of the unrenormalized bound is carried
by the explicit right-half-plane pole packet `P_+`.

Moreover,

\[
 \boxed{
 \sup_{0<\sigma\le1/2}
 \frac{\sigma}{2\pi}
 \int_{\mathbb R}|f_h(\sigma+it)|^2dt<\infty
 \iff Z_+=\varnothing
 \iff \mathrm{RH}.}
 \tag{T-15407.5}
\]

The theorem does not prove that `Z_+` is empty. It proves that there is no
additional diffuse or bulk Hardy obstruction hidden beyond this pole packet.

## Part I — exact Cauchy Gram for finitely many poles

Let

\[
 p(z)=\sum_{j=1}^N\frac{r_j}{z-a_j},
 \qquad
 \operatorname{Re}a_j<\sigma.
 \tag{T-15407.6}
\]

Using

\[
 \frac1{\sigma+it-a_j}
 =\int_0^\infty
 e^{-(\sigma-a_j)x}e^{-itx}dx
 \tag{T-15407.7}
\]

and Plancherel gives

\[
 \boxed{
 \frac1{2\pi}\int_{\mathbb R}|p(\sigma+it)|^2dt
 =\sum_{j,k=1}^N
 \frac{\overline{r_j}r_k}
 {2\sigma-\overline{a_j}-a_k}.}
 \tag{T-15407.8}
\]

The Cauchy matrix

\[
 C_\sigma(j,k)=
 \frac1{2\sigma-\overline{a_j}-a_k}
 \tag{T-15407.9}
\]

is positive semidefinite because it is the Gram matrix of

\[
 x\longmapsto e^{-(\sigma-a_k)x}
 \quad\text{in }L^2(0,\infty).
 \tag{T-15407.10}
\]

This is the exact finite Hardy pole Gram.

### Stable, boundary, and unstable poles

For one pole `a=delta+i gamma`,

\[
 \frac{\sigma}{2\pi}\int
 \left|\frac r{\sigma+it-a}\right|^2dt
 =\frac{\sigma|r|^2}{2(\sigma-\delta)}.
 \tag{T-15407.11}
\]

Therefore:

1. if `delta<0`, the value tends to zero as `sigma downarrow 0`;
2. if `delta=0`, it is exactly `|r|^2/2` for every `sigma>0`;
3. if `delta>0`, it diverges as `sigma downarrow delta` from the right and the
   integral is infinite on the pole line itself.

For distinct poles sharing the maximal real part `delta`, writing
`sigma=delta+epsilon` gives

\[
 \boxed{
 \frac1{2\pi}\int|p(\sigma+it)|^2dt
 =\frac1{2\epsilon}
  \sum_{\operatorname{Re}a_j=\delta}|r_j|^2
 +O(1).}
 \tag{T-15407.12}
\]

Cross terms between distinct ordinates remain bounded. Hence no phase
cancellation can hide a genuine interior pole.

## Part II — an abstract stable-remainder theorem

Let `sigma_0>0`. Suppose a meromorphic function `f` on
`0<=Re z<=sigma_0` has:

- boundary poles `i gamma_k` with residues `b_k` satisfying
  \[
   \sum_k|b_k|<\infty;
   \tag{T-15407.13}
  \]
- a locally finite set of interior poles with principal-part sum `P_+`;
- a remainder
  \[
   R(z)=f(z)-P_+(z)-
   \sum_k\frac{b_k}{z-i\gamma_k}
   \tag{T-15407.14}
  \]
  extending holomorphically to the closed strip and satisfying
  \[
   \sup_{0\le\sigma\le\sigma_0}
   \int_{\mathbb R}|R(\sigma+it)|^2dt<\infty.
   \tag{T-15407.15}
  \]

Put

\[
 P_0(z)=\sum_k\frac{b_k}{z-i\gamma_k}.
 \tag{T-15407.16}
\]

The Laplace representation gives

\[
 \frac1{2\pi}\int|P_0(\sigma+it)|^2dt
 =\int_0^\infty e^{-2\sigma x}
  \left|\sum_k b_ke^{i\gamma_kx}\right|^2dx
 \le\frac{(\sum_k|b_k|)^2}{2\sigma}.
 \tag{T-15407.17}
\]

Using `|u+v|^2<=2|u|^2+2|v|^2`, one obtains the explicit bound

\[
 \boxed{
 \sup_{0<\sigma\le\sigma_0}
 \frac{\sigma}{2\pi}
 \int|f(\sigma+it)-P_+(\sigma+it)|^2dt
 \le
 \left(\sum_k|b_k|\right)^2
 +\frac{\sigma_0}{\pi}
  \sup_{0\le\sigma\le\sigma_0}\|R_\sigma\|_2^2.}
 \tag{T-15407.18}
\]

This proves the abstract renormalized Hardy bound.

If `P_+=0`, it is the required unrenormalized bound. If `P_+` has a pole, the
local Laurent expansion and (T-15407.11) show that the unrenormalized supremum
is infinite. An analytic remainder cannot cancel a principal part.

## Part III — verification of the hypotheses for filtered `xi'/xi`

The standard symmetric Hadamard expansion of the even order-one entire function
`Xi` gives a Mittag--Leffler expansion for `Xi'/Xi`, with one simple pole of
residue `m_a` at every centered zero `a` of multiplicity `m_a`.

Multiplication by `Omega_h` changes the residue to

\[
 \boxed{r_a=m_a\Omega_h(a).}
 \tag{T-15407.19}
\]

The unit-interval zero-count estimate and (L-15416.10) imply

\[
 \sum_{\operatorname{Re}a=0}|r_a|<\infty,
 \tag{T-15407.20}
\]

and local normal convergence of (T-15407.3).

After all principal parts in the closed right half-strip are removed, the
remainder can be written by grouping zeros in unit ordinate boxes as a sum of
difference quotients

\[
 m_a\frac{\Omega_h(z)-\Omega_h(a)}{z-a}
 \tag{T-15407.21}
\]

plus the regular Hadamard terms. On a fixed strip,

\[
 \Omega_h(z),\Omega_h'(z)
 =O_h((1+|\operatorname{Im}z|)^{-2}),
 \tag{T-15407.22}
\]

while each unit box contains `O(log(2+|t|))` zeros. The grouped remainder is
therefore

\[
 O_h\!\left(
 \frac{\log^2(2+|t|)}{1+t^2}
 \right)
 \tag{T-15407.23}
\]

on both boundary lines after the critical-line principal parts are removed.
It belongs to `L2(dt)`. Strip Hardy convexity then yields (T-15407.15) for
`sigma_0=1/2`.

This proves (T-15407.4).

## Part IV — RH equivalence

If RH holds, there are no centered zeros with positive real part. Thus
`P_+=0`, and (T-15407.4) is the original uniform Hardy bound.

Conversely, suppose a zero

\[
 \rho=\frac12+\delta+i\gamma,
 \qquad0<\delta<\frac12,
 \tag{T-15407.24}
\]

exists. `L-15416` proves `Omega_h(delta+i gamma) !=0`. Hence `f_h` has a genuine
pole at

\[
 z=\delta+i\gamma.
 \]

The vertical-line integral is infinite at `sigma=delta`, and (T-15407.11)
shows divergence from either admissible side. Therefore the uniform Hardy bound
fails. Functional-equation reflection completes the equivalence with RH.

## Part V — relation to bounded mean square

Let `q_h` be the causal inverse Laplace distribution corresponding to `f_h`.
Laplace Plancherel gives

\[
 \frac1{2\pi}\int|f_h(\sigma+it)|^2dt
 =\int_0^\infty e^{-2\sigma x}|q_h(x)|^2dx
 \tag{T-15407.25}
\]

on every line to the right of the pole set. The Abel--Cesaro comparison in
`T-15406` therefore gives

\[
 \boxed{
 \sup_X\frac1X\int_0^X|q_h(x)|^2dx<\infty
 \iff P_+=0.}
 \tag{T-15407.26}
\]

The same conclusion holds for the raw triangular prime statistic after the
explicit completed gamma and endpoint corrections are restored.

Thus the bounded-mean-square problem is no longer obscured by a diffuse
prime-pair cancellation question: its only unstable component is the exact
right-zero pole packet.

## What has and has not been proved

Proved at the theorem-interface level:

1. the exact positive Cauchy Gram for every finite pole packet;
2. the stable/boundary/unstable Hardy trichotomy;
3. a uniform Abel--Hardy bound after exact subtraction of all right-half-plane
   principal parts;
4. absolute summability of the critical-line residue amplitudes for the compact
   filter;
5. equivalence of the original uniform bound with absence of the unstable pole
   packet.

Not proved:

\[
 \boxed{P_+=0.}
 \tag{T-15407.27}
\]

Equation (T-15407.27) is precisely RH in centered coordinates. No Selberg bulk
estimate, eta contraction, or residue-free contour reflection can replace it.

## Gap audit

- The grouped Mittag--Leffler estimate (T-15407.23) should be independently
  reconstructed in the repository's exact `xi` normalization.
- Multiplicities are included in every residue and in the absolute residue sum.
- A pole lying exactly on a tested vertical line makes the integral infinite;
  principal-value regularization is not the Hardy norm.
- The renormalized theorem is unconditional but depends definitionally on the
  complete off-line pole packet. It is not a positive proof of its emptiness.
- The result closes the uniform **reflection defect after its exact pole ledger
  is retained**. It does not prove the requested unrenormalized bounded mean
  square and therefore does not prove RH.
