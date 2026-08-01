# L-15140 — Central-jet persistence and the quartic body dichotomy

Claim ID: `L-15140`  
Status: **PROVED NECESSARY GATE FROM THE ACTUAL CENTRAL KERNEL; REALIZED-JET DECAY OPEN**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-01  
Dependencies: `L-15135`, `L-15136`, `L-15139`  
Scope: test whether the full finite-jet body can decay as the window grows

## 1. The local source jet does not move to high readout frequency

The actual central kernel is

\[
 h_w(u)=\frac{e^{wu}-1}{u}
 =\sum_{m\ge1}\frac{w^m}{m!}u^{m-1}.
\]

At determinant order `ell`, the source finite jet is

\[
 j_{\ell,M}^{\rm src}
 =\frac1{(\ell-1)!}
 C_M^{\rm src}(\chi_Mu^{\ell-2}),
\tag{L-15140.1}
\]

where `C_M^src=iota_M^cen P_M^cen J_M^cen` is the manuscript's
finite-jet source map.

Assume the windows are nested and `chi_M=1` on one fixed neighborhood of
`u=0` for every sufficiently large `M`, and assume `J_M^cen` depends only on a
fixed finite jet at `u=0` with compatible coordinate normalization.  Then

\[
 \boxed{
 J_M^{\rm cen}(\chi_Mu^q)
 =J_\infty^{\rm cen}(u^q)
 }
\tag{L-15140.2}
\]

for every fixed `q` and every sufficiently large `M`.

In particular, the quartic input

\[
 \boxed{
 \frac16J_M^{\rm cen}(\chi_Mu^2)
 }
\tag{L-15140.3}
\]

is eventually constant.  It is a retained **local body**, not a readout tail.

## 2. The realized quartic jet

Let

\[
 \mathcal B_M
 =\mathfrak J_R\,
  \mathcal R_{\partial,R,M}^{\rm fp}\,
  \epsilon_M^{\rm fp}\,
  \iota_M^{\rm cen}P_M^{\rm cen}
\tag{L-15140.4}
\]

be the full singular-seam comparison chain of `L-15136`.  Define the realized
quartic jet vector

\[
 \boxed{
 c_{4,M}
 =\frac16\mathcal B_MJ_M^{\rm cen}(\chi_Mu^2).}
\tag{L-15140.5}
\]

This is the first actual object that can decide whether the central finite-jet
body is Schatten-small.

If `v_(4,M)` is a unit source/readout coordinate representing the quartic jet,
then

\[
 \boxed{
 \|C_M\|_4\ge\|C_Mv_{4,M}\|
 =\|c_{4,M}\|.}
\tag{L-15140.6}
\]

Consequently

\[
 \boxed{
 \liminf_{M\to\infty}\|c_{4,M}\|>0
 \Longrightarrow
 \liminf_{M\to\infty}\|C_M\|_4>0.}
\tag{L-15140.7}
\]

By `L-15139`, no coupled choice of `N(M)` can then make
`||C_(M,N(M))||_4` tend to zero.

Conversely, the proposed Schatten-smallness theorem necessarily implies

\[
 \boxed{\|c_{4,M}\|\to0.}
\tag{L-15140.8}
\]

Thus an all-operator proof must first pass this one-vector quartic body gate.

## 3. Stability under a limiting comparison map

Suppose the compatible jet coordinate is fixed and

\[
 \mathcal B_M\to\mathcal B_\infty
\]

in operator norm on the finite jet space.  Then

\[
 c_{4,M}\to
 c_{4,\infty}
 :=\frac16\mathcal B_\infty J_\infty^{\rm cen}(u^2).
\tag{L-15140.9}
\]

Therefore exactly one of the following occurs:

1. **annihilating body:** `c_(4,infinity)=0`, so quartic jet decay remains
   possible and higher jets must be checked;
2. **persistent body:** `c_(4,infinity)!=0`, so the proposed
   `||C_(M,N(M))||_4->0` route is impossible.

The manuscript's regular area-trace cancellation does not decide this dichotomy,
because `mathcal B_M` uses the retained singular seam coordinate.

## 4. Directed production gate

A proof-facing quartic record must therefore contain a directed enclosure of

\[
 \boxed{
 \|c_{4,M}\|
 =\frac16\left\|
  \mathfrak J_R\mathcal R_{\partial,R,M}^{\rm fp}
  \epsilon_M^{\rm fp}
  \iota_M^{\rm cen}P_M^{\rm cen}J_M^{\rm cen}(\chi_Mu^2)
 \right\|.}
\tag{L-15140.10}
\]

It must be reported separately from the readout-tail bound
`||C_M-C_(M,N)||_4`.

A lower interval endpoint bounded away from zero certifies failure of the
Schatten-small finite-jet strategy.  An upper endpoint tending to zero permits,
but does not by itself prove, the full `S_4` statement.

## 5. Proof boundary

The local source jet is shown to stabilize under the manuscript's stated
finite-jet architecture.  The theorem does not assign a value to its image under
the complete singular-seam comparison chain.  That image is precisely what the
next directed ladder must compute.
