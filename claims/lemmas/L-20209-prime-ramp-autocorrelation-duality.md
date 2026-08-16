# L-20209 — Prime-ramp/autocorrelation duality for every positive screw filter

Claim ID: `L-20209`  
Title: A nonnegative finite screw filter has an exact cosine-ramp transform, and its prime weights are linear interpolation of one aperiodic autocorrelation sequence  
Status: **PROPOSED — COMPLETE FINITE ALGEBRAIC PROOF**  
Authoring agent: `gpt56-pro-09-n`  
Created: 2026-08-07  
Dependencies: Fejer--Riesz factorization; `L-20208`  
Scope: arbitrary finite real even RH-positive FIR filters

## 1. Filter and ramp

Let

\[
 P(x)=\sum_{k=1}^{N}\lambda_k(1-\cos kx)
\]

be a nonzero real trigonometric polynomial satisfying

\[
 P(x)\ge0\qquad(x\in\mathbb R).
\]

Define the compact piecewise-linear ramp

\[
\boxed{
 L_P(s)=\sum_{k=1}^{N}\lambda_k(k-s)_+,
 \qquad s\ge0.}
\]

Then the exact cosine-transform identity is

\[
\boxed{
 P(x)=x^2\int_0^N L_P(s)\cos(xs)\,ds.
}
\]

Indeed, term by term,

\[
 x^2\int_0^k(k-s)\cos(xs)\,ds=1-\cos(kx).
\]

At `x=0` the identity is interpreted by continuity, and in particular

\[
\boxed{
 \int_0^N L_P(s)\,ds
 ={1\over2}\sum_{k=1}^N k^2\lambda_k
 ={1\over2}P''(0)\ge0.}
\]

Consequently, if `L_P(s)<=0` throughout `[0,N]`, then `L_P=0` and hence
`P=0`. A nonzero RH-positive finite filter necessarily carries a positive ramp
region, and therefore an adverse prime-weight region after the explicit-formula
sign is inserted.

## 2. Fejer factor and autocorrelations

Choose a Fejer--Riesz factor

\[
 P(x)=|A(e^{ix})|^2,
 \qquad
 A(z)=(1-z)Q(z),
 \qquad
 Q(z)=\sum_{j=0}^{N-1}q_jz^j.
\]

Set

\[
 d_m=\operatorname{Re}
 \sum_{j=0}^{N-m-1}q_{j+m}\overline{q_j}
 \qquad(0\le m<N),
 \qquad d_N=0.
\]

Then at every integer knot,

\[
\boxed{
 L_P(m)=2d_m
 \qquad(0\le m\le N).}
\]

### Proof

Let `c_m` be the Fourier autocorrelation coefficient of `A`, so

\[
 P(x)=c_0+2\sum_{m=1}^Nc_m\cos(mx),
 \qquad
 \lambda_m=-2c_m.
\]

Writing `A=(1-z)Q` gives the discrete second-difference identity

\[
 c_m=2d_m-d_{m-1}-d_{m+1},
\]

with the natural endpoint conventions. The sequence

\[
 R_m=\sum_{k>m}\lambda_k(k-m)=L_P(m)
\]

obeys

\[
 R_{m-1}-2R_m+R_{m+1}=\lambda_m,
 \qquad R_N=0,
 \qquad R_0=2d_0.
\]

The sequence `2d_m` obeys the same recurrence and endpoints, proving the
identity.

Since `L_P` is affine between successive integer knots, for

\[
 s=m+\theta,
 \qquad m\in\{0,\ldots,N-1\},
 \qquad0\le\theta\le1,
\]

one has the full interpolation formula

\[
\boxed{
 L_P(s)=2\bigl[(1-\theta)d_m+\theta d_{m+1}\bigr].}
\]

Thus the complete continuous prime-ramp geometry is nothing more than linear
interpolation of one finite aperiodic autocorrelation sequence.

## 3. Exact prime contraction

For the filtered screw statistic

\[
 \mathcal S_P(t)=\sum_{k=1}^N\lambda_k\Psi(kt),
\]

a prime power `q` with

\[
 s_q={\log q\over t}=m_q+\theta_q
\]

has coefficient

\[
\boxed{
 -2t\,{\Lambda(q)\over\sqrt q}
 \bigl[(1-\theta_q)d_{m_q}+\theta_qd_{m_q+1}\bigr].}
\]

Only `q<=e^(Nt)` occurs. Grouping all prime powers gives

\[
\boxed{
 \mathcal P_P(t)
 =-2t\sum_{m=0}^{N}W_m(t)d_m,}
\]

where every deposition weight `W_m(t)` is nonnegative and is obtained by
linearly depositing each mass `Lambda(q)/sqrt(q)` on the two adjacent normalized
logarithmic knots.

This is the exact bridge between:

- positive trigonometric/screw filters;
- low-autocorrelation sequence design;
- the repository's Toeplitz carrier contractions;
- the prime-power convex polygon and Chebyshev--Riesz formulations.

No phase or prime term is discarded.

## 4. Strengthened first-cell barrier

For `0<=s<=1`, the ramp has the exact form

\[
 L_P(s)=2\|q\|_2^2-s\|Dq\|_2^2,
\]

where `Dq=(q_0,q_1-q_0,\ldots,q_{N-1}-q_{N-2},-q_{N-1})`. The largest
eigenvalue of `D^*D` is

\[
 4\cos^2\!\left({\pi\over2(N+1)}\right).
\]

Hence

\[
\boxed{
 {L_P(s)\over L_P(0)}
 \ge
 1-2s\cos^2\!\left({\pi\over2(N+1)}\right)
 \qquad(0\le s\le1).}
\]

At `s=1/2` this recovers the sharp theorem of `L-20208`:

\[
 {L_P(1/2)\over L_P(0)}
 \ge
 \sin^2\!\left({\pi\over2(N+1)}\right).
\]

The first possible zero of the ramp therefore lies no earlier than

\[
\boxed{
 s_N^*={1\over2\cos^2(\pi/[2(N+1)])}
 =\frac12+{\pi^2\over8N^2}+O(N^{-3}).}
\]

The alternating-sine factor from `L-20208` attains equality throughout this
first cell. It is the canonical endpoint-concentrated filter.

## 5. Full-problem consequence

There is now a sharp dichotomy.

- A finite positive screw filter cannot eliminate the adverse low-prime prefix.
- Increasing the degree can push the first ramp crossing down to `1/2`, but only
  at the exact quadratic rate `O(N^-2)`.
- Beyond the first cell, every prime coefficient is controlled by the signed
  aperiodic autocorrelations `d_m`.

Thus the remaining positive theorem is a quantitative **bulk transport versus
autocorrelation debt** statement. One must construct a growing sequence `q^(N)`
and scales `t_N` for which the positive deposited prime mass, archimedean terms,
and pole cancellation dominate

\[
 2t_N\sum_m W_m(t_N)(d_m^{(N)})_+
\]

while preserving the pole-descent completeness of the filtered family.

Equivalently, one may prove the same domination in the prime-polygon or
Chebyshev--Riesz coordinate. The lemma turns that global arithmetic target into
an explicit low-autocorrelation design problem; it does not prove the target.
