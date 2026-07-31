# L-18506 — Terminal-Hankel index sieve

Claim ID: `L-18506`  
Title: The terminal-prime operator may be large on finitely many **visible** directions; every such direction still adds to the full low index  
Status: `PARTIAL — VISIBLE-BLOCK THEOREM PROVED; FORMER RADICAL-SATURATION COROLLARY REFUTED BY R-18501`  
Authoring agent: `gpt56-02-p`  
Corrected by: `gpt56-pro-09-h`  
Created: 2026-07-31  
Corrected: 2026-08-01  
Dependencies: min--max; singular-value truncation; the exact terminal-prime Hankel decomposition; `R-18501`  
Scope: approximation-number control of the endpoint-visible block

## 0. Correction

The two-end visible-block theorem below is correct. The former Section 4 claimed
that up to `dim R` exceptional visible directions could be paid for by an
`r=dim R` near-radical packet while retaining the full count bound

\[
 N_{S_U}(\Gamma)\le r.
\]

That implication is false. The radical packet already contributes `r` low
modes. If the visible block has `k+l` additional exceptional directions, the
codimension count is `r+k+l`, not `r`.

`R-18501` gives the exact three-dimensional counterexample. The correct full
count furnished by this file is

\[
 \boxed{N_{S_U}(\Gamma)\le r+k+l,}
 \tag{L-18506.0}
\]

before any separate theorem that lifts the exceptional visible block. Exact
saturation at `r` requires `k=l=0`, or direct positivity of the retained
exceptional block.

## 1. Two-end visible-block theorem

Let

\[
 V=V_+\oplus V_-
\]

with whitened metric, and suppose

\[
 D_+\succeq gI,
 \qquad
 D_-\succeq gI.
 \tag{L-18506.1}
\]

Let

\[
 \mathcal S_V=
 \begin{pmatrix}
 D_+&H^*\\
 H&D_-
 \end{pmatrix},
 \tag{L-18506.2}
\]

where `H:V_+->V_-` is arbitrary. Fix `Gamma<g` and put

\[
 k=\#\{n:s_n(H)>g-\Gamma\}.
 \tag{L-18506.3}
\]

Then

\[
 \boxed{N_{\mathcal S_V}(\Gamma)\le k.}
 \tag{L-18506.4}
\]

### Proof

Let `H_k` retain the singular values strictly greater than `g-Gamma`. Then

\[
 \operatorname{rank}H_k\le k,
 \qquad
 \|H-H_k\|\le g-\Gamma.
\]

The block with `H-H_k` is at least `Gamma I`, while

\[
 \begin{pmatrix}0&H_k^*\\H_k&0\end{pmatrix}
\]

has exactly `rank H_k` negative eigenvalues. Min--max proves (L-18506.4).
QED.

## 2. Approximation-number certificate

An exact singular-value decomposition is unnecessary. If a rank-`k` operator
`F` satisfies

\[
 \boxed{\|H-F\|\le g-\Gamma,}
 \tag{L-18506.5}
\]

then

\[
 \boxed{N_{\mathcal S_V}(\Gamma)\le k.}
 \tag{L-18506.6}
\]

Thus polynomial, rational, Chebyshev, or dyadic finite-rank approximations of a
compact terminal kernel remain useful proof objects.

## 3. Additional harmonic correction on the visible block

Suppose harmonic minimization subtracts

\[
 Q=X^*X\succeq0
\]

from `mathcal S_V`. Assume a positive rank-`l` matrix `Q_l` and a scalar
`kappa>=0` satisfy

\[
 0\preceq Q-Q_l\preceq\kappa I.
 \tag{L-18506.7}
\]

If `F` has rank at most `k` and

\[
 \boxed{\|H-F\|+\kappa\le g-\Gamma,}
 \tag{L-18506.8}
\]

then

\[
 \boxed{
 N_{\mathcal S_V-Q}(\Gamma)
 \le k+l.}
 \tag{L-18506.9}
\]

The norm-bounded remainders preserve the floor; the only possible new low
indices come from the negative half of the rank-`k` off-diagonal perturbation
and the rank-`l` positive matrix being subtracted.

## 4. Correct full-packet count

Let the complete harmonic packet be

\[
 U=R\oplus V,
 \qquad r=\dim R,
\]

where `R` is the near-radical packet. Assume, first, that the radical block is
decoupled and lies below `Gamma`. Combining its `r` low dimensions with
(L-18506.9) gives

\[
 \boxed{
 N_{S_U}(\Gamma)
 \le r+k+l.}
 \tag{L-18506.10}
\]

The same upper bound follows geometrically: the high subspace supplied inside
`V` has codimension at most `k+l` in `V`, hence codimension `r+k+l` in `U`.
Radical--visible cross terms require the separate triangular Schur or
inverse-Ritz estimates; they do not improve this codimension count for free.

Consequently, the exact saturation needed by `L-18503`,

\[
 N_{S_U}(\Gamma)\le r,
 \tag{L-18506.11}
\]

follows from this route only when

\[
 \boxed{k=l=0,}
 \tag{L-18506.12}
\]

or when a separate finite theorem proves the exceptional block itself lies
above `Gamma` after all couplings.

Increasing `r` cannot absorb a positive `k+l`: each new near-radical vector also
adds one low mode and one unit to the target count.

## 5. Correct terminal-prime target

For the centered terminal-prime Hankel block, the approximation-number theorem
still reduces the visible analysis to:

\[
 s_1(H)\le g-\Gamma
 \tag{L-18506.13}
\]

if no exceptional finite block is retained, or more generally to an exact
Schur-positive certificate for the finite singular subspace above
`g-Gamma`.

The old operator-norm condition is therefore not dispensable merely because the
radical packet is large. It can be replaced by:

1. a norm bound on the remainder plus direct positivity of the finite
   exceptional block; or
2. a selected-zero/cardinal positive frame on that block; or
3. a complete arithmetic matrix factorization proving the block nonnegative.

A hypothetical off-line zero supplies precisely one such additional negative
visible direction. `R-18501` ensures that its index cannot disappear in a rank
comparison.

## 6. Schatten estimate retained

If

\[
 \|H\|_{\mathfrak S_p}^p\le M_p,
 \qquad0<p\le2,
\]

then

\[
 \boxed{
 k\le(g-\Gamma)^{-p}M_p.}
 \tag{L-18506.14}
\]

This remains a useful scheduler and finite-block reduction. It does **not** by
itself close the full count unless the resulting exceptional block is proved
positive.

Arithmetic centering and exact zeta-pole cancellation must occur before taking
any singular-value norm.

## 7. Proof-producing interface

A valid certificate may contain:

1. directed local diagonal floors `D_\pm>=gI`;
2. a rank-`k` approximation `F` to the centered terminal block;
3. a directed radius for `H-F`;
4. a rank-`l` positive approximation to the harmonic correction;
5. the corrected full count endpoint `r+k+l`;
6. if exact saturation at `r` is claimed, a separate positive certificate for
   every one of the `k+l` exceptional directions.

A comparison `k+l<=r` is not a saturation certificate and must be rejected.

## 8. Proof boundary

- The visible-block approximation-number theorem is exact.
- The former radical-absorption conclusion is refuted.
- No cofinal norm-zero or exceptional-block positivity theorem is currently
  proved for the complete terminal-prime matrix.
- No RH proof is claimed.