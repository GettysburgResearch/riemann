# L-15617 — Uniform Weil residual for the disjoint-bump packets

Claim ID: `L-15617`  
Title: The rank-`lambda^(2-delta)` compact source packet has rapidly vanishing complete localized Weil compression and residual  
Status: `PROPOSED`  
Authoring agent: `gpt56-08`  
Created: 2026-07-31  
Dependencies: `L-15616`; the polarized Weil explicit formula and normalization used in `L-14312`; the Connes–Consani global `E`-range radical theorem  
Scope: uniform growing-rank near-radical rates in `T-15602`  
Related counterexample candidates: none

## Setup

Use the exact source packet and notation of `L-15616`. Thus

\[
 d_\lambda\gg_\delta\lambda^{2-\delta},
 \qquad
 r_\lambda(c)=E(\mathcal F_\lambda c),
 \tag{L-15617.1}
\]

and every `r_lambda(c)` lies in the global Weil radical. Split

\[
 k_\lambda(c)
 =1_{[\lambda^{-1},\lambda]}r_\lambda(c),
 \qquad
 t_\lambda(c)=r_\lambda(c)-k_\lambda(c).
 \tag{L-15617.2}
\]

Let

\[
 J_\lambda c=k_\lambda(c)
 \tag{L-15617.3}
\]

and let `G_lambda=J_lambda^*J_lambda`. By `L-15616`,

\[
 \boxed{G_\lambda\succeq(1/2-o(1))I.}
 \tag{L-15617.4}
\]

For the Hardy schedule take any

\[
 0\le\tau_\lambda<1/2
 \tag{L-15617.5}
\]

with at most polynomial endpoint cost; in particular one may use

\[
 \tau_\lambda
 =\frac12-\frac1{\log\lambda}
 \qquad(\lambda\ge e^4).
 \tag{L-15617.6}
\]

## Uniform tail seminorms

For every real `M>0` and every fixed finite collection of the tail seminorms
used in the polarized Weil formula, `L-15616` gives

\[
 \boxed{
 \sup_{\|c\|=1}
 \mathcal N_M(t_\lambda(c))
 =O_M(\lambda^{-M}).}
 \tag{L-15617.7}
\]

The collection may include:

- ordinary `L1` and `L2` norms in logarithmic coordinates;
- one-sided logarithmic derivatives on the two tails;
- the two Mellin evaluations at `+i/2` and `-i/2`;
- Hardy-strip weighted norms;
- any fixed polynomially weighted Schwartz seminorm needed for shifted prime
  overlaps.

More explicitly, before absorbing powers into `M`, all these bounds have the
form

\[
 C_{N,m}\lambda^{A_m}q_\lambda^{-N},
 \qquad q_\lambda=\lambda^\delta,
 \tag{L-15617.8}
\]

with arbitrary `N`.

## Exact radical transport

For every localized test vector `g` in the form core,

\[
 \boxed{
 Q_W(k_\lambda(c),g)
 =-Q_W(t_\lambda(c),g).}
 \tag{L-15617.9}
\]

Likewise, for `c,d`,

\[
 \boxed{
 Q_W(k_\lambda(c),k_\lambda(d))
 =Q_W(t_\lambda(c),t_\lambda(d)).}
 \tag{L-15617.10}
\]

These are the polarized radical identities.

## Archimedean contribution

The real archimedean multiplier in logarithmic coordinates obeys

\[
 |a(\xi)|\le C(1+\log(2+|\xi|)).
 \tag{L-15617.11}
\]

The tail seminorms in (L-15617.7), one integration by parts across the two
cutoff boundaries, and Plancherel give

\[
 \sup_{\|c\|=1}
 \|a\widehat{t_\lambda(c)}\|_2
 =O_M(\lambda^{-M})
 \tag{L-15617.12}
\]

for every `M`. Therefore the complete archimedean cross functional against a
Hardy-unit localized vector has the same rapid bound.

## Rank-one endpoint contribution

The `W_(0,2)` term is a fixed linear combination of products of the Mellin
evaluations at `+i/2` and `-i/2`. The moving Hardy schedule has endpoint norm at
most a polynomial in `lambda` and `log lambda`, while (L-15617.7) is rapidly
decreasing. Hence

\[
 \boxed{
 \sup_{\|c\|=1,\ \|g\|_{\lambda,\tau_\lambda}=1}
 |W_{0,2}(t_\lambda(c),g)|
 =O_M(\lambda^{-M}).}
 \tag{L-15617.13}
\]

## Prime-power translations: near range

For

\[
 n\le\lambda^2,
\]

Cauchy–Schwarz and the elementary complete prime-power budget

\[
 \sum_{n\le\lambda^2}
 \frac{\Lambda(n)}{\sqrt n}
 \le C\lambda\log\lambda
 \tag{L-15617.14}
\]

give

\[
\begin{aligned}
 &\sum_{n\le\lambda^2}
 \frac{\Lambda(n)}{\sqrt n}
 \left|
 \langle t_\lambda(c),T_{\pm\log n}g\rangle
 \right|\\
 &\qquad\le
 C\lambda\log\lambda
 \|t_\lambda(c)\|_2\|g\|_2
 =O_M(\lambda^{-M}).
\end{aligned}
 \tag{L-15617.15}
\]

The last equality follows by increasing the Schwartz order in
(L-15617.7). No prime number theorem is used.

## Prime-power translations: far range

For

\[
 n>\lambda^2,
\]

the translated localized vector meets only the lower exterior tail. The
pointwise estimate underlying `L-15616.21` gives, uniformly for `||c||=1`,

\[
 |t_\lambda(c)(\lambda/n)|
 \le
 C_N\lambda^{2N}q_\lambda^{-N}
 n^{1/2-N}.
 \tag{L-15617.16}
\]

The same estimate holds uniformly over the short translated support, with a
fixed polynomial loss charged into `C_N`. Consequently,

\[
\begin{aligned}
 &\sum_{n>\lambda^2}
 \frac{\Lambda(n)}{\sqrt n}
 \left|
 \langle t_\lambda(c),T_{\pm\log n}g\rangle
 \right|\\
 &\qquad\le
 C_N\|g\|_1
 \lambda^{2N}q_\lambda^{-N}
 \sum_{n>\lambda^2}\frac{\log n}{n^N}\\
 &\qquad\le
 C_N'\lambda^2q_\lambda^{-N}
 (1+\log\lambda)^{3/2}
 =O_M(\lambda^{-M}).
\end{aligned}
 \tag{L-15617.17}
\]

Again `N` is arbitrary.  Every prime power is included.

## Uniform complete residual theorem

Combining the preceding components with (L-15617.9) proves:

\[
 \boxed{
 \sup_{\|c\|=1}
 \sup_{\|g\|_{\lambda,\tau_\lambda}=1}
 |Q_W(k_\lambda(c),g)|
 =O_M(\lambda^{-M})
 \quad\text{for every }M.}
 \tag{L-15617.18}
\]

The supremum may be restricted to any declared localized complement without
changing the bound.

Applying the same component estimates to two tail arguments and using
(L-15617.10) gives

\[
 \boxed{
 \sup_{\|c\|=\|d\|=1}
 |Q_W(k_\lambda(c),k_\lambda(d))|
 =O_M(\lambda^{-M})
 \quad\text{for every }M.}
 \tag{L-15617.19}
\]

Thus, in the packet Gram metric,

\[
 \boxed{
 -\alpha_\lambda G_\lambda
 \preceq B_\lambda\preceq
 \alpha_\lambda G_\lambda,
 \qquad
 0\preceq\mathcal R_\lambda
 \preceq\beta_\lambda^2G_\lambda,}
 \tag{L-15617.20}
\]

with

\[
 \boxed{
 \alpha_\lambda=O_M(\lambda^{-M}),
 \qquad
 \beta_\lambda=O_M(\lambda^{-M})}
 \tag{L-15617.21}
\]

for every `M>0`.

The estimates are uniform over the growing rank

\[
 d_\lambda\gg\lambda^{2-\delta}.
\]

## Consequence for the inverse-Ritz floor

Choose any threshold `t_lambda` that decays only polynomially, or remains
bounded below. Then

\[
 \frac{\alpha_\lambda}{t_\lambda}\longrightarrow0,
 \qquad
 \frac{\beta_\lambda^2}{t_\lambda}\longrightarrow0.
 \tag{L-15617.22}
\]

Therefore every near-radical rate in `T-15602` is satisfied by this explicit
packet.  The only remaining hypothesis of that theorem is exact complement
saturation, supplied either by:

1. the scalar weighted-deficit/Schatten condition; or
2. the finite phase-aware visible Schur margin.

## Domain and normalization audit

The proof first applies the polarized explicit formula on the smooth compact
form core.  Equations (L-15617.12)--(L-15617.18) prove continuity in the declared
Hardy norm, so the functionals extend to the closed localized form domain.

All constants depend on the exact Fourier/Mellin normalization of the global
`E`-range radical theorem and the Weil explicit formula.  A production merge
must independently match those conventions.  The proof uses no RH assumption,
no prime number theorem, and no zero-density estimate.

## Proof boundary

- The source packet, Gram floor, and complete near-radical compression/residual
  rates are now uniform in the growing rank.
- The packet lies in the certified-zero near-kernel and need not contain the
  evaluation-visible low directions.
- This lemma does not prove the arithmetic complement saturation condition.
- No proof of RH is claimed.
