# L-15614 — Phase-aware terminal-prime matrix error band

Claim ID: `L-15614`  
Title: A finite critical-zero phase matrix plus a scalar zero-tail moat encloses the complete centered terminal-prime Hankel block under RH  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-09-f`  
Created: 2026-07-31  
Dependencies: `L-15610`, `L-15613`; the polarized smoothed explicit formula  
Scope: phase-complete endpoint-visible packet bound for `T-15603`  
Related counterexample candidates: none

## 1. Real profile packet

Let

\[
 \boldsymbol\phi=(\phi_1,\ldots,\phi_m)^T,
 \qquad
 \phi_j\in C_c^\infty(0,R;\mathbb R),
\]

and let `G_V>0` be a real packet metric. Define the Laplace profile vector

\[
 \boldsymbol\Phi(z)
 =\int_0^R e^{-zr}\boldsymbol\phi(r)\,dr.
 \tag{1}
\]

Let `E_a` be the centered terminal-prime matrix of `L-15610`, at support
parameter `a>2R`.

For a positive critical-line ordinate `gamma`, put

\[
 p(\gamma)=\boldsymbol\Phi(i\gamma).
 \tag{2}
\]

The positive/negative ordinate pair contributes the real symmetric matrix

\[
 \boxed{
 Z_{a,\gamma}
 =-4m_\gamma
 \operatorname{Re}\left[
  e^{2ia\gamma}p(\gamma)p(\gamma)^T
 \right].}
 \tag{3}
\]

For every real coefficient vector `c`,

\[
 c^TZ_{a,\gamma}c
 =-4m_\gamma
 \operatorname{Re}\left[
  e^{2ia\gamma}(c^Tp(\gamma))^2
 \right].
 \tag{4}
\]

Equation (3) is the polarized form of `L-15610.15` and `T-15402.9`.

## 2. One-zero Loewner bound

Define the leverage response

\[
 h(\gamma)
 =p(\gamma)^*G_V^{-1}p(\gamma).
 \tag{5}
\]

Cauchy--Schwarz gives

\[
 |c^Tp(\gamma)|^2
 \le(c^TG_Vc)h(\gamma).
\]

Therefore

\[
 \boxed{
 -4m_\gamma h(\gamma)G_V
 \preceq Z_{a,\gamma}
 \preceq4m_\gamma h(\gamma)G_V.}
 \tag{6}
\]

This estimate is independent of the phase `2a gamma`; selected phases should be
retained exactly rather than charged through (6).

## 3. Selected phase matrix and finite shells

For a proof-grade finite zero set `mathcal Z`, define

\[
 Z_{a,\mathcal Z}
 =\sum_{\gamma\in\mathcal Z}Z_{a,\gamma}.
 \tag{7}
\]

Use the same finite ordinate shells as in `L-15613`. Let:

- `M_k` be a rigorous upper total multiplicity in shell `I_k`;
- `r_k` be the selected multiplicity in that shell;
- `H_k` satisfy
  \[
   h(t)\le H_k\qquad(t\in I_k).
  \tag{8}
  \]

Under RH, the complete unselected contribution through height `T` obeys

\[
 \boxed{
 -\Theta_{\rm shell}G_V
 \preceq E_{a,\rm shell}^{\rm rem}
 \preceq\Theta_{\rm shell}G_V,}
 \tag{9}
\]

where

\[
 \Theta_{\rm shell}
 =4\sum_k(M_k-r_k)H_k.
 \tag{10}
\]

## 4. Dimension-free high-zero tail

For integer `p>=1`, define

\[
 \mathcal A_p
 =\int_0^R
 \sqrt{
  \boldsymbol\phi^{(p)}(r)^T
  G_V^{-1}
  \boldsymbol\phi^{(p)}(r)
 }\,dr.
 \tag{11}
\]

For every real `c`, integration by parts and packet-metric Cauchy--Schwarz give

\[
 |c^T\boldsymbol\Phi(it)|
 \le|t|^{-p}\mathcal A_p\sqrt{c^TG_Vc}.
\]

Hence

\[
 \boxed{h(t)\le\mathcal A_p^2|t|^{-2p}.}
 \tag{12}
\]

With the zero-moment tail `mathfrak Z_(2p)(T)` of `L-15613`, the complete
high-zero matrix tail satisfies

\[
 \boxed{
 -\Theta_{>T}G_V
 \preceq E_{a,>T}
 \preceq\Theta_{>T}G_V,
 \qquad
 \Theta_{>T}=4\mathcal A_p^2\mathfrak Z_{2p}(T).}
 \tag{13}
\]

The constant is independent of packet dimension except through the explicit
metric integral (11).

## 5. Trivial-zero matrix tail

Define

\[
 \mathcal A_0
 =\int_0^R
 \sqrt{
  \boldsymbol\phi(r)^T G_V^{-1}\boldsymbol\phi(r)
 }\,dr.
 \tag{14}
\]

Retain the first `M` trivial-zero matrices exactly. For

\[
 d=a-R>0,
\]

the remaining matrix tail obeys

\[
 \boxed{
 -\Theta_{\rm triv}^{>M}G_V
 \preceq E_{a,\rm triv}^{>M}\preceq0,}
 \tag{15}
\]

with

\[
 \boxed{
 \Theta_{\rm triv}^{>M}
 \le
 2\mathcal A_0^2
 \frac{
  e^{-2(2M+5/2)d}
 }{
  1-e^{-4d}
 }.}
 \tag{16}
\]

The sign in (15) is available because every trivial-zero matrix is negative
semidefinite. For a symmetric norm enclosure one may use its absolute radius.

## 6. Final matrix band

Let `E_(a,triv,M)` be the exactly retained first `M` trivial-zero matrices and
put

\[
 \Theta_a
 =\Theta_{\rm shell}
  +\Theta_{>T}
  +\Theta_{\rm triv}^{>M}.
 \tag{17}
\]

Then RH implies

\[
 \boxed{
 -\Theta_aG_V
 \preceq
 E_a-Z_{a,\mathcal Z}-E_{a,\rm triv,M}
 \preceq
 \Theta_aG_V.}
 \tag{18}
\]

Equivalently,

\[
 \left\|
 G_V^{-1/2}
 (E_a-Z_{a,\mathcal Z}-E_{a,\rm triv,M})
 G_V^{-1/2}
 \right\|_{op}
 \le\Theta_a.
 \tag{19}
\]

For any rational frozen vector `c`, a directed violation

\[
 \boxed{
 |c^T(E_a-Z_{a,\mathcal Z}-E_{a,\rm triv,M})c|
 >\Theta_a c^TG_Vc}
 \tag{20}
\]

is an unconditional disproof of RH after the explicit-formula and arithmetic
inputs are independently reviewed.

## 7. Relation to the visible margin

The theorem is principally a **disproof band**. It is conditional on RH and
therefore cannot be inserted circularly as the positive estimate required to
prove RH.

It nevertheless gives the sharpest finite audit of `theta_a`:

1. compute `E_a` from the complete terminal prime powers;
2. compute the selected critical-line phase matrix;
3. compare their difference with the rigorous tail radius `Theta_a`;
4. if the band passes, preserve the observed norm as positive-path
   reconnaissance;
5. if it fails, freeze the violating vector and promote it through (20).

A phase-blind direct norm bound on the raw terminal prime matrix would erase the
pole cancellation and is not an acceptable substitute.

## 8. Five-notch universal packet

For a scalar universal notched profile, the leverage is simply

\[
 h(t)=\frac{|\Phi(it)|^2}{G_V}.
\]

For a phase-complete two-profile packet, every entry and the complete selected
phase matrix are evaluated directly, while (10)--(13) control the omitted zero
spectrum. The notch factors remain zero-free at every shifted off-line zero, so
false RH forces eventual violation of (18).

## Gap audit

- The packet profiles are required to be real for the simple matrix formula
  (3). Complex packets can be handled by realification.
- A floating selected-zero matrix is not a proof object.
- The high-zero bound requires either exact cumulative count data or a proved
  count majorant.
- The theorem does not supply a cofinal positive bound for `theta_a`; doing so
  would already prove the RH-sensitive terminal estimate.
- No RH proof is claimed.
