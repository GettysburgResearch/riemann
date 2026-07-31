# L-15110 — Relative diagonal residual and complement coercivity imply target completion

Claim ID: `L-15110`  
Status: **PROVED FINITE-DIMENSIONAL LEMMA; COFINAL ARITHMETIC ESTIMATES OPEN**  
Authoring agent: `gpt56-04-f`  
Created: 2026-07-31  
Dependencies: `L-15107`; elementary Loewner order  
Scope: a quantitative sufficient condition for the cofinal Finsler inequality  
Related counterexample candidates: none

## 1. Purpose

The exact Finsler criterion says that the target-pinned pencil succeeds if and
only if `A_p` is positive on the nonzero `B_p`-isotropic cone. That criterion is
complete but does not yet expose a directly estimable arithmetic numerator and
denominator.

This lemma gives a stronger, quantitative sufficient condition. It separates:

1. coercivity of a scalar/rank-one shifted background on the complete target
   complement;
2. the coordinate-relative failure of the prescribed target to solve the
   corresponding boundary equation.

It is adapted to the exact radical-tail program because the second quantity can
be bounded from the discarded tail. It also exposes the additional denominator
and small-coordinate obligations that cannot be replaced by ordinary norm
convergence.

## 2. Setup

Let

\[
 Q=Q^{\mathsf T}\in\mathbb R^{n\times n},
 \qquad
 p,\eta\in\mathbb R^n,
\]

with every coordinate `p_i!=0` and

\[
 \eta^{\mathsf T}p=1.
 \tag{L-15110.1}
\]

The target-pinned pencil is

\[
 T_p(c)
 =Q+
 \operatorname{diag}\!\left(
  \frac{c\eta_i-(Qp)_i}{p_i}
 \right)
 -c\eta\eta^{\mathsf T}.
 \tag{L-15110.2}
\]

Choose arbitrary real scalars `mu,c` and define the boundary-equation residual

\[
 \boxed{
 r=Qp-\mu p-c\eta.}
 \tag{L-15110.3}
\]

Then

\[
 \boxed{
 T_p(c)
 =Q-\mu I-c\eta\eta^{\mathsf T}
  -\operatorname{diag}\!\left(\frac{r_i}{p_i}\right).}
 \tag{L-15110.4}
\]

Let

\[
 M=\operatorname{diag}(m_1,\ldots,m_n),
 \qquad m_i>0,
 \tag{L-15110.5}
\]

be any positive diagonal comparison metric.

## 3. Main finite theorem

Assume that for every `x perpendicular p`,

\[
 \boxed{
 x^{\mathsf T}
 (Q-\mu I-c\eta\eta^{\mathsf T})x
 \ge g\,x^{\mathsf T}Mx}
 \tag{L-15110.6}
\]

for one `g>0`, and that the residual satisfies the coordinate-relative bounds

\[
 \boxed{
 |r_i|\le\rho\,|p_i|m_i
 \qquad(1\le i\le n)}
 \tag{L-15110.7}
\]

for one `0<=rho<g`.

Then

\[
 \boxed{
 x^{\mathsf T}T_p(c)x
 \ge(g-\rho)x^{\mathsf T}Mx
 \qquad(x\perp p).}
 \tag{L-15110.8}
\]

Consequently

\[
 \boxed{
 T_p(c)\succeq0,
 \qquad
 \ker T_p(c)=\mathbb Rp.}
 \tag{L-15110.9}
\]

In particular the exact Finsler isotropic-cone inequality holds.

### Proof

Equation (L-15110.4) is obtained by substituting

\[
 Qp=\mu p+c\eta+r
\]

into (L-15110.2). For every real vector `x`, (L-15110.7) gives

\[
 \left|
  \sum_i\frac{r_i}{p_i}x_i^2
 \right|
 \le\rho\sum_i m_ix_i^2
 =\rho x^{\mathsf T}Mx.
 \tag{L-15110.10}
\]

Combining (L-15110.4), (L-15110.6), and (L-15110.10) proves
(L-15110.8). Since `M` is positive definite, the right side is strictly
positive for every nonzero `x perpendicular p`.

The target-pinning identity gives `T_p(c)p=0`. Decomposing every vector as a
multiple of `p` plus a vector in `p^perp` now proves positive semidefiniteness
and the one-dimensional kernel. QED.

## 4. Useful metric choices

### Ordinary metric

Taking `M=I` reduces the conditions to

\[
 Q-\mu I-c\eta\eta^{\mathsf T}\succeq gI
 \quad\text{on }p^\perp,
 \tag{L-15110.11}
\]

and

\[
 \max_i\left|\frac{r_i}{p_i}\right|<g.
 \tag{L-15110.12}
\]

This is the simplest gate but can be badly conditioned when some target
coefficient is small.

### Absolute-residual metric

Taking

\[
 m_i=|p_i|^{-1}
 \tag{L-15110.13}
\]

makes (L-15110.7) the absolute bound

\[
 |r_i|\le\rho.
 \tag{L-15110.14}
\]

The price is that the complement floor must be proved in the weighted metric

\[
 M=\operatorname{diag}(|p_i|^{-1}).
\]

This choice is natural when the radical-tail producer gives uniform coordinate
residuals but the Fourier target coefficients vary over many scales.

### General balancing

The optimal diagonal metric can be selected after directed bounds for `p_i` and
`r_i` are available. The proof consumer trusts only the final positive rational
`m_i`, the complete complement coercivity certificate, and the exact residual
intervals.

## 5. Cofinal corollary

For a sequence `(Q_j,p_j,eta_j)`, choose real or rational `mu_j,c_j`, positive
diagonal metrics `M_j`, and numbers `g_j,rho_j` satisfying

\[
 Q_j-\mu_jI-c_j\eta_j\eta_j^{\mathsf T}
 \succeq g_jM_j
 \quad\text{on }p_j^\perp,
 \tag{L-15110.15}
\]

and

\[
 |(Q_jp_j-\mu_jp_j-c_j\eta_j)_i|
 \le\rho_j|(p_j)_i|(M_j)_{ii}.
 \tag{L-15110.16}
\]

If

\[
 \boxed{
 \limsup_{j\to\infty}\frac{\rho_j}{g_j}<1,}
 \tag{L-15110.17}
\]

then the target-pinned completion passes cofinally. In particular, the stronger
asymptotic condition

\[
 \rho_j/g_j\longrightarrow0
 \tag{L-15110.18}
\]

is sufficient.

Combined with the target-transform convergence and finite real-zero theorem of
`T-15104`, this package would prove RH.

## 6. Relation to radical leakage and mode-8 scales

For an exact global radical split into a localized target and an exterior tail,
the form residual `Qp-mu p-c eta` is generated entirely by the discarded tail,
subject to the common-domain and normalization gates. The Hermite source gives a
super-Gaussian tail estimate.

The pure positive-prolate calculation in `T-15102` supplies a model complement
scale

\[
 g_{\rm model}\asymp d_8(\lambda),
\]

with a target excess on the smaller `d_4` scale and

\[
 d_4/d_8=\Theta(\lambda^{-8}).
\]

Therefore a possible closing package would be

\[
 g_j\ge c_0a_jd_8(\lambda_j),
 \tag{L-15110.19}
\]

and

\[
 \rho_j=o(a_jd_8(\lambda_j)).
 \tag{L-15110.20}
\]

The exact mode-8 theorem proves these scales only for the pure prolate defect
model. The repository does not presently prove the actual localized-Weil
coercivity (L-15110.19), nor does it prove the coordinate-relative residual
(L-15110.20) uniformly over a growing finite band.

The cardinal obstruction `R-15102` explains why these missing statements cannot
be replaced by local-uniform transform convergence.

## 7. Finite proof objects

A production certificate may contain:

1. exact/directed `Q,p,eta`;
2. rational `mu,c`;
3. positive rational diagonal entries `m_i`;
4. a rational complement basis `U` with `U^T p=0`;
5. exact LDL pivots proving
   \[
   U^{\mathsf T}
   (Q-\mu I-c\eta\eta^{\mathsf T}-gM)U\succeq0;
   \]
6. directed residual intervals proving (L-15110.7);
7. the strict rational comparison `rho<g`.

No eigensolver, root finder, or floating condition number enters the final
consumer.

## 8. Gap audit

- The lemma is sufficient, not necessary. A Finsler completion may exist even
  when no convenient diagonal metric gives (L-15110.6)--(L-15110.7).
- Ordinary small residual norm does not imply the coordinate-relative bound when
  target coefficients are tiny.
- A pure-prolate complement gap is not automatically an actual Weil complement
  gap.
- The rank-one boundary scalar `c` must be included in both the complement form
  and residual; optimizing only `mu` can miss a valid completion.
- No cofinal production sequence satisfying (L-15110.17) is claimed here.