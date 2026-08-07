# L-15430 — The regular tail after one Green integration is one explicit smoothed Jordan density

Claim ID: `L-15430`  
Title: Exact Bernstein criterion for the completed Volterra-tail Gram  
Status: `PROPOSED`  
Authoring agent: `gpt56-05-l`  
Created: 2026-08-01  
Dependencies: `L-15428`, `L-15429`; uniqueness of the Laplace transform  
Scope: smallest corrected regular-tail positivity target  
Related counterexample candidates: none

## Positive archimedean resolvent density

With the notation of `L-15429`, define

\[
 \boxed{
 n_\omega(t)
 ={e^{-(1+\omega)t}\over2\omega}
  v_\omega(e^{-t})\ge0.}
 \tag{L-15430.1}
\]

Equivalently,

\[
 n_\omega(t)
 ={\pi^\omega\over\Gamma(\omega)}
 e^{-2\omega t}
 B_{1-e^{-2t}}\left(\omega,{3\over2}-\omega\right),
 \tag{L-15430.2}
\]

where `B_x` is the incomplete beta function. Its Laplace transform is

\[
 \boxed{
 \widehat n_\omega(q)
 ={B_\omega(q)\over q+2\omega}.}
 \tag{L-15430.3}
\]

## Jordan discrepancy and its convolution

Put

\[
 a_\omega(n)
 ={J_{2\omega}(n)\over n^{1+2\omega}},
 \qquad
 c_\omega={1\over\zeta(1+2\omega)},
 \tag{L-15430.4}
\]

\[
 R_\omega(t)
 =\sum_{\log n\le t}a_\omega(n)-c_\omega t.
 \tag{L-15430.5}
\]

`L-15428` proves `R_omega(t)>=0`. Define

\[
 m_\omega=n_\omega*R_\omega.
 \tag{L-15430.6}
\]

Then `m_omega>=0`, `m_omega(0)=0`, and

\[
 \widehat m_\omega(q)
 ={B_\omega(q)\widehat R_\omega(q)
   \over q+2\omega}.
 \tag{L-15430.7}
\]

The one-Green regular kernel of `L-15429` is therefore

\[
 \boxed{
 G_\omega^{\rm reg}(q)
 =q\widehat m_\omega(q)
 =\widehat{m_\omega'}(q).}
 \tag{L-15430.8}
\]

The derivative is distributional. Since `n_omega(0)=0`, it has the explicit
locally integrable representative

\[
 \boxed{
 m_\omega'(t)
 =\sum_{\log n\le t}
   a_\omega(n)n_\omega(t-\log n)
 -c_\omega\int_0^t n_\omega(r)dr.}
 \tag{L-15430.9}
\]

## Necessary and sufficient positivity criterion

For polarized right-half-plane variables, put

\[
 \mathcal G_\omega^{\rm reg}(z,w)
 =G_\omega^{\rm reg}
  \left({z+\bar w\over2}\right).
 \tag{L-15430.10}
\]

The following are equivalent:

1. `mathcal G_omega^reg` is a positive semidefinite kernel;
2. `G_omega^reg` is completely monotone on `(0,infinity)`;
3. `m_omega'` is a nonnegative measure;
4. the explicit smoothed Jordan inequality
   \[
   \boxed{
   \sum_{\log n\le t}
   a_\omega(n)n_\omega(t-\log n)
   \ge
   c_\omega\int_0^t n_\omega(r)dr
   \quad(t\ge0)}
   \tag{L-15430.11}
   \]
   holds.

The implication `(3)=>(1)` is the feature representation

\[
 \mathcal G_\omega^{\rm reg}(z,w)
 =\int_0^\infty
  e^{-(z+\bar w)t/2}\,dm_\omega(t).
 \tag{L-15430.12}
\]

Conversely, positivity of a continuous Hankel kernel depending only on
`(z+bar(w))/2` gives a positive representing measure by the
Bernstein--Widder theorem, and uniqueness of Laplace transforms identifies it
with `m_omega'`.

## Relation to the full endpoint/tail metric

The corrected augmented regular metric consists of:

1. the positive moving endpoint Gram
   \[
   E_\omega(z,w)=\langle\phi_w,\phi_z\rangle;
   \]
2. the one-Green regular tail Gram (L-15430.12), provided
   (L-15430.11) holds;
3. the exact boundary--tail cross ledger (L-15429.20).

The raw regular kernel is obtained only after applying the Mellin derivative
associated with the primitive trace. It is not itself a Gram by `R-15406`.

## Why Harris domination does not finish the proof

`L-15428` proves

\[
 R_\omega(t)\ge0,
 \]

which implies `m_omega>=0`. It does **not** imply `m_omega'>=0`: convolution of
two nonnegative functions need not be monotone. The extra derivative in
(L-15430.11) is the complete remaining arithmetic content.

This is not a soft regularity issue. Suzuki's first integrated kernel
`h_omega^{<1>}` has Mellin transform `Theta_omega(z)/z`; an eventual one-sign
theorem for that integrated kernel implies innerness of the scattering ratio.
Thus a proof of (L-15430.11) uniformly in `0<omega<1/2`, together with the
positive endpoint block, would already resolve the RH-bearing sign problem.

## Smallest blocker

After the exact endpoint and cross blocks are retained, the regular physical
metric identity is equivalent to the single scalar family (L-15430.11), or to
its matrix-valued full-`Phi` analogue on the augmented trace range.

No known PNT remainder, Harris association, or pointwise Jordan Jensen
inequality proves the derivative sign. A successful proof must preserve the
specific beta-resolvent smoothing `n_omega` and control the discrete-minus-
continuous Jordan discrepancy at that scale.
