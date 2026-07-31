# L-15612 — A low packet automatically captures weighted deficit trace

Claim ID: `L-15612`  
Title: Low compression for the same operator converts packet dimension into a rigorous leverage trace-tail bound  
Status: `PROPOSED`  
Authoring agent: `gpt56-08`  
Created: 2026-07-31  
Dependencies: trace cyclicity; positivity; `L-15607/L-15608`; `L-15610`  
Scope: scalar closure of the weighted-deficit complement in Issue #156  
Related counterexample candidates: none

## Purpose

`R-15601` shows that an arbitrary packet of the correct dimension need not
capture the weighted-deficit eigenspace.  `L-15610` repairs this at the level of
spectral counts by adding the load-bearing low-Rayleigh hypothesis for the same
operator.

The present lemma is stronger and quantitative: the low-Rayleigh hypothesis
itself forces the packet to capture at least `G-alpha` units of weighted deficit
per orthonormal direction.  Summing those inequalities gives the exact leverage
trace-tail needed by `L-15607`, with no principal angle and no threshold-index
matching.

## Abstract theorem

Let `A` be lower-bounded self-adjoint on a Hilbert space `H`.  Let `D` be a
positive trace-class operator and suppose

\[
 \boxed{A\succeq GI-D}
 \tag{L-15612.1}
\]

for a real number `G`.

Let `L subset H` be a `d`-dimensional subspace with orthogonal projection `P`,
and suppose

\[
 \boxed{A|_L\preceq\alpha I_L.}
 \tag{L-15612.2}
\]

Then

\[
 \boxed{PDP|_L\succeq(G-\alpha)I_L,}
 \tag{L-15612.3}
\]

and therefore

\[
 \boxed{
 \operatorname{Tr}(PDP)
 \ge d(G-\alpha).}
 \tag{L-15612.4}
\]

Consequently the uncaptured positive deficit satisfies

\[
 \boxed{
 \operatorname{Tr}((I-P)D(I-P))
 \le
 \operatorname{Tr}D-d(G-\alpha).}
 \tag{L-15612.5}
\]

Finally,

\[
 \boxed{
 A|_{L^\perp}
 \succeq
 \left[G-\operatorname{Tr}D+d(G-\alpha)\right]I.}
 \tag{L-15612.6}
\]

### Proof

Compress (L-15612.1) to `L`:

\[
 A|_L\succeq GI_L-PDP|_L.
\]

Together with (L-15612.2), this gives

\[
 PDP|_L\succeq(G-\alpha)I_L,
\]

proving (L-15612.3).  Taking the finite-dimensional trace proves
(L-15612.4).

Since `D` is trace class and `P` is finite rank, cyclicity gives

\[
 \operatorname{Tr}((I-P)D(I-P))
 =\operatorname{Tr}D-\operatorname{Tr}(PDP),
\]

which proves (L-15612.5).

For `w in L^perp`,

\[
 \langle Dw,w\rangle
 =\langle(I-P)D(I-P)w,w\rangle.
\]

The compression is positive, so its operator norm is at most its trace.  Insert
(L-15612.5) into (L-15612.1) to obtain (L-15612.6). QED.

## Exact scalar saturation criterion

Fix `t<Gamma`.  If

\[
 A|_L\prec tI
 \tag{L-15612.7}
\]

and

\[
 \boxed{
 \operatorname{Tr}D-d(G-\alpha)
 \le G-\Gamma,}
 \tag{L-15612.8}
\]

then

\[
 \boxed{A|_{L^\perp}\succeq\Gamma I.}
 \tag{L-15612.9}
\]

Therefore

\[
 \boxed{N_A(t)=N_A(\Gamma)=d.}
 \tag{L-15612.10}
\]

This is a scalar exact capacity-saturation certificate.  Unlike a bare
dimension comparison, every quantity in (L-15612.8) is bound to the same
operator inequality.

## Relation to packet leverage

For the weighted-deficit multiplier

\[
 D=P_I\mathcal F^{-1}(G-s)_+\mathcal FP_I,
 \tag{L-15612.11}
\]

one has the exact identity from `L-15608`

\[
 \operatorname{Tr}((I-P)D(I-P))
 =\int c_L(\xi)(G-s(\xi))_+d\xi.
 \tag{L-15612.12}
\]

Thus (L-15612.5) proves automatically that

\[
 \boxed{
 \int c_L(G-s)_+
 \le\operatorname{Tr}D-d(G-\alpha).}
 \tag{L-15612.13}
\]

The packet's low compression supplies a global lower bound on its integrated
frequency leverage.  No cellwise Fourier transform of the packet is required
for this coarse certificate.

A direct cellwise leverage calculation may still be sharper than
(L-15612.13), but it is no longer logically necessary when the trace budget has
a moat.

## Why the `R-15601` packet fails the hypothesis

In the exact counterexample

\[
 D=\operatorname{diag}(1,0),
 \qquad
 G=1,
 \qquad
 L=\operatorname{span}\{e_2\},
\]

the packet captures no deficit.  Equation (L-15612.3) says that a packet with
`A|_L<=alpha I` would need

\[
 0=\langle De_2,e_2\rangle\ge1-\alpha.
\]

Hence `alpha>=1`.  It cannot simultaneously be a low packet below
`t<Gamma=1/2`.  The trace theorem therefore pinpoints exactly which missing
hypothesis invalidates the dimension-only shortcut.

## Directed Gram/compression adapter

Let `J:C^d->H` be an injective basis map and define

\[
 H_L=J^*J,
 \qquad
 B_L=J^*AJ.
 \tag{L-15612.14}
\]

A proof packet certifies

\[
 \boxed{B_L\preceq\alpha H_L}
 \tag{L-15612.15}
\]

by exact or interval `LDL*`.  The dimension `d` is the exact rank of `J`.
Every operator/form assembly radius must be charged in the safe direction in
both (L-15612.1) and (L-15612.15).

The trace of `D` may be evaluated directly from the symbol:

\[
 \boxed{
 \operatorname{Tr}D
 =\frac{|I|}{2\pi}
 \int_{\mathbb R}(G-s(\xi))_+d\xi.}
 \tag{L-15612.16}
\]

Thus the complete complement gate reduces to one integrated symbol deficit,
one packet dimension, and one packet compression endpoint.

## Cofinal phase-space margin

At level `j`, put

\[
 \Theta_j
 =\operatorname{Tr}D_j-d_j(G_j-\alpha_j).
 \tag{L-15612.17}
\]

If

\[
 \boxed{
 \Theta_j\le G_j-\Gamma_j}
 \tag{L-15612.18}
\]

and the near-radical packet residual/rate conditions of `T-15602` hold, then the
count saturates and the cofinal lower floor tends to zero.

A useful strict asymptotic form is

\[
 \boxed{
 \frac{\operatorname{Tr}D_j}{d_jG_j}
 \le1-\delta,
 \qquad
 \frac{\alpha_j}{G_j}=o(1),}
 \tag{L-15612.19}
\]

with a fixed `delta>0` and thresholds chosen inside the resulting moat.  This is
the corrected phase-space comparison: it uses packet dimension only after its
actual low compression has converted that dimension into guaranteed deficit
capture.

## Interaction with external source repair

`L-15611` may preserve the complete dimension of a source concentration packet.
To use that rank in (L-15612.19), one must still certify the repaired localized
compression

\[
 B_L\preceq\alpha H_L.
\]

The dimension-preserving repair and the low-compression trace capture are
separate but composable gates.

## Proof boundary

- The theorem is exact elementary operator/trace algebra.
- `D` must be positive trace class and the lower comparison must concern the
  same exact operator `A` as the packet compression.
- A negative or inconclusive trace moat does not disprove RH.
- No current artifact proves the cofinal arithmetic deficit margin
  (L-15612.18) for Suzuki's exact symbol.
- No proof of RH is claimed.
