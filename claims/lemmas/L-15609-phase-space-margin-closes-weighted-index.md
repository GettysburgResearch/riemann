# L-15609 — A strict phase-space margin closes the weighted index by pre-plunge capacity

Claim ID: `L-15609`  
Title: Integrated arithmetic deficit below the source Shannon capacity gives a full-rank small-tail radical packet  
Status: `PROPOSED`  
Authoring agent: `gpt56-08`  
Created: 2026-07-31  
Dependencies: `L-15607/L-15608`; min--max; pre-plunge localization estimates  
Scope: scalar sufficient condition for the comparison in `T-15603`  
Related counterexample candidates: none

## Purpose

`T-15603` asks whether the weighted-deficit index can be supplied by an exact
repaired source packet with uniformly small tails.  This lemma gives a simple
strict-margin criterion.  It separates the arithmetic burden into one
integrated deficit and the source burden into one concentration/Shannon count.

The two phase spaces need not be identified.  Their exact normalization and the
source-to-localized-vector map must be supplied independently.

## Weighted-index upper bound

Use the notation of `L-15608`.  Put

\[
 \kappa=G-\Gamma>0,
 \qquad
 D=D_G.
 \tag{L-15609.1}
\]

Then

\[
 p_G(\Gamma)=\#\{n:\nu_n(D)>\kappa\}
 \le\frac{\operatorname{Tr}D}{\kappa}.
 \tag{L-15609.2}
\]

Since

\[
 \operatorname{Tr}D
 =\frac{L}{2\pi}\int_{\mathbb R}(G-s(\xi))_+d\xi,
 \tag{L-15609.3}
\]

one may use the exact integer cap

\[
 \boxed{
 p_G(\Gamma)
 \le
 P_{\rm def}
 :=\left\lfloor
 \frac{L}{2\pi\kappa}
 \int (G-s)_+
 \right\rfloor.}
 \tag{L-15609.4}
\]

If the quotient is an integer, a strict/equality endpoint convention must be
handled by a directed spectral or rational moat; a production packet may safely
use the ceiling instead.

## Source concentration capacity

Let `S_src` be a positive compact contraction on a source Hilbert space, with
concentration eigenvalues

\[
 1\ge\chi_1\ge\chi_2\ge\cdots\ge0.
 \tag{L-15609.5}
\]

For `0<epsilon<1`, put

\[
 N_{\rm src}(\epsilon)
 =\#\{n:\chi_n\ge1-\epsilon\}.
 \tag{L-15609.6}
\]

Assume its high-concentration eigenspace has an orthogonal local/tail split
whose unnormalized tail norm is at most `sqrt(epsilon)`.  Apply the external
source repair of `L-15607`.  Let

\[
 d_{\rm rep}
 =\sqrt\epsilon+q_T\Lambda,
 \tag{L-15609.7}
\]

and let `g_rep` be the directed local Gram lower singular value after repair.
The repaired exact source packet has dimension

\[
 \boxed{N_{\rm src}(\epsilon)}
 \tag{L-15609.8}
\]

with normalized tail-synthesis norm at most

\[
 \boxed{
 \varepsilon_{\rm tail}^{1/2}
 \le d_{\rm rep}/g_{\rm rep}.}
 \tag{L-15609.9}
\]

## Finite capacity dominance theorem

If

\[
 \boxed{
 N_{\rm src}(\epsilon)
 \ge p_G(\Gamma),}
 \tag{L-15609.10}
\]

then an exact repaired packet of dimension `p_G(Gamma)` may be selected from
the source packet without worsening the operator tail bound.  Hence the
weighted-deficit index is no larger than the repaired radical capacity,
provided the form/residual tolerances induced by (L-15609.9) fit the declared
`alpha,beta` budget.

A sufficient purely scalar condition is

\[
 \boxed{
 N_{\rm src}(\epsilon)
 \ge
 \left\lceil\frac{\operatorname{Tr}D}{\kappa}\right\rceil.}
 \tag{L-15609.11}
\]

Together with the rate conditions of `T-15603`, this proves RH.

## Cofinal strict-margin criterion

Let

\[
 c_j=\operatorname{Tr}S_{{\rm src},j}
 \tag{L-15609.12}
\]

be the source Shannon number.  Suppose there is a fixed `delta>0` such that

\[
 \boxed{
 \frac{\operatorname{Tr}D_j}
      {(G_j-\Gamma_j)c_j}
 \le1-\delta}
 \tag{L-15609.13}
\]

for all sufficiently large `j`.

Suppose one can choose `epsilon_j downarrow0` such that

\[
 \boxed{
 N_{{\rm src},j}(\epsilon_j)
 \ge(1-\delta/2)c_j}
 \tag{L-15609.14}
\]

and the external-repair/form rates satisfy

\[
 \frac{d_{{\rm rep},j}^2}{g_{{\rm rep},j}^2}
 C_{tt,j}=o(t_j),
 \qquad
 \frac{d_{{\rm rep},j}^2}{g_{{\rm rep},j}^2}
 C_{te,j}^2=o(t_j).
 \tag{L-15609.15}
\]

Then, apart from finite integer rounding absorbed by the strict margin,

\[
 p_{j,G}(\Gamma_j)
 \le(1-\delta)c_j
 <(1-\delta/2)c_j
 \le N_{{\rm src},j}(\epsilon_j).
\]

Thus `T-15603` applies and RH follows.

## Input from the 2026 pre-plunge theorem

For one-dimensional interval localization with phase-space parameter `c`, the
sharp pre-plunge result gives, uniformly before the plunge,

\[
 -\log(1-\chi_n(c))
 \asymp
 \frac{c-n}{\log(2c/(c-n))}.
 \tag{L-15609.16}
\]

Consequently, for any fixed `delta>0`, every rank

\[
 n\le(1-\delta/2)c
\]

has exponentially small leakage.  This supplies choices of `epsilon_j` in
(L-15609.14) that decay faster than any inverse power of `c_j`, subject to the
exact geometry and normalization hypotheses of that theorem.

Therefore the difficult part of (L-15609.13)--(L-15609.15) is not the finite
source constraints or the pre-plunge eigenvalues.  It is:

1. a proof-grade integrated bound for the complete arithmetic deficit;
2. a source/localization adapter identifying the correct Shannon number;
3. control of the Weil form-continuity constants on the repaired growing
   packet.

## Stronger Schatten-margin version

For any `q>0`, (L-15608.14) gives

\[
 p_G(\Gamma)
 \le\kappa^{-q}\|D\|_{S_q}^q.
 \tag{L-15609.17
 }
\]

Thus the trace ratio in (L-15609.13) may be replaced by

\[
 \boxed{
 \frac{\|D_j\|_{S_{q_j}}^{q_j}}
      {(G_j-\Gamma_j)^{q_j}c_j}
 \le1-\delta.}
 \tag{L-15609.18}
\]

This is often sharper for a deficit with a narrow deep core and a broad shallow
halo.  The dyadic layer-cake/Rotfel'd interface of `L-15608` is designed to
produce exactly this quantity from the modern plunge estimates.

## Why the source phase space cannot be enlarged formally

The source concentration operator, its local/tail split, and the arithmetic
map must be fixed by the construction.  One cannot enlarge an auxiliary
frequency set merely to increase `c_j`: doing so need not produce more exact
radical vectors with controlled Weil tails.

This gate prevents a vacuous dimension proof.  The scalar comparison is useful
only after the source Shannon number has been derived from the actual
source-to-localization operator.

## Directed proof interface

A proof packet should contain:

1. a rational upper enclosure for `Tr D_j` or `||D_j||_(S_q)^q`;
2. a directed lower enclosure for `kappa_j=G_j-Gamma_j`;
3. the exact source concentration packet and a certified high-eigenvalue count;
4. the external corrector map and repaired Gram floor;
5. tail/form radii yielding `alpha_j,beta_j`;
6. the final strict integer comparison.

## Proof boundary

- The finite and cofinal implications are exact.
- No current artifact proves the arithmetic phase-space margin
  (L-15609.13) or (L-15609.18).
- The pre-plunge estimate applies only after its interval/finite-union geometry
  and Fourier normalization are matched exactly.
- This theorem does not identify the source concentration operator for the
  zeta `E`-map.
- No proof of RH is claimed.
