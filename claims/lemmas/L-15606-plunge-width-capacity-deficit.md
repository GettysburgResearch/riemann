# L-15606 — Plunge-width bound for the capacity deficit

Claim ID: `L-15606`  
Title: When the count and source capacity use one concentration operator, every unmatched mode lies in the plunge region or the finite source codimension  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-09-d`  
Created: 2026-07-31  
Dependencies: elementary eigenvalue counting; `L-15605`; sharp plunge estimates of Kulikov--Dam Larsen and Azimifard for quantitative applications  
Scope: size of the finite visible Schur block

## Abstract counting theorem

Let `K` be a positive compact contraction with eigenvalues

\[
 1\ge\chi_1\ge\chi_2\ge\cdots\ge0.
 \tag{L-15606.1}
\]

Fix

\[
 0<\eta<1-\varepsilon<1.
 \tag{L-15606.2}
\]

Define

\[
 D_\eta=\#\{n:\chi_n>\eta\},
 \tag{L-15606.3}
\]

\[
 P_\varepsilon=\#\{n:\chi_n\ge1-\varepsilon\},
 \tag{L-15606.4}
\]

and the intervening plunge count

\[
 \Pi_{\eta,\varepsilon}
 =\#\{n:\eta<\chi_n<1-\varepsilon\}.
 \tag{L-15606.5}
\]

Then exactly

\[
 \boxed{D_\eta-P_\varepsilon\le\Pi_{\eta,\varepsilon}.}
 \tag{L-15606.6}
\]

The inequality is an equality except for eigenvalues equal to the endpoint
`1-epsilon`, whose inclusion in `P_epsilon` can only improve the bound.

## Capacity consequence

Suppose:

1. a complete symbol theorem uses the concentration packet
   \[
   U_\eta=\operatorname{Ran}1_{(\eta,1]}(K)
   \]
   and therefore gives a preliminary count cap
   \[
   D\le D_\eta;
   \]
2. the highly concentrated packet
   \[
   P_\varepsilon=\operatorname{Ran}1_{[1-\varepsilon,1]}(K)
   \]
   has one uniform source-to-form tail estimate;
3. imposing the exact source conditions costs at most `r` dimensions.

Then `L-15605` gives a radical capacity

\[
 C\ge P_\varepsilon-r,
 \tag{L-15606.7}
\]

and hence

\[
 \boxed{
 D-C\le\Pi_{\eta,\varepsilon}+r.}
 \tag{L-15606.8}
\]

Thus every possible count-capacity mismatch lies in a plunge packet plus the
finite source-repair loss.

### Proof

The modes counted by `D_eta` but not by `P_epsilon` have eigenvalues in the
interval `(eta,1-epsilon)`, apart from endpoint conventions.  This proves
(L-15606.6).  Combining `D<=D_eta` and (L-15606.7) gives (L-15606.8).  QED.

## Same-operator requirement

The theorem is useful only when the count packet and capacity packet are built
from the same concentration operator, with identical time window, frequency set,
Fourier normalization, and eigenvalue convention.

Comparing a one-band prolate count to an unrelated Hermite truncation by their
leading dimensions does not satisfy the theorem.  A production implementation
should either:

- construct the exact source packet inside the same multiband concentration
  eigenspace used by the symbol cover; or
- provide a separate directed subspace-transfer theorem.

## Quantitative literature input

For one-dimensional time--frequency localization on interval or finite-union
geometries, the newest plunge-region results bound

\[
 \Pi_{\eta,\varepsilon}
\]

by an explicit logarithmic or near-logarithmic function of the phase-space size
and

\[
 \log\frac1{\eta(1-\eta)},
 \qquad
 \log\frac1{\varepsilon(1-\varepsilon)}.
\]

Accordingly, even when `D` and `C` are both of bulk phase-space order, the
unmatched finite visible block may be only logarithmic in support.

The constants and endpoint conventions must be imported from the cited theorem
in the exact interval/multiband geometry; no asymptotic `O` notation is a proof
certificate by itself.

## Revised finite saturation architecture

Take

\[
 L=\text{codimension-repaired high-concentration packet}.
\]

The mismatch space in `L-15604` may then be chosen with dimension at most

\[
 \Pi_{\eta,\varepsilon}+r,
 \tag{L-15606.9}
\]

before further certified-zero evaluation splitting.  Only this plunge-sized
matrix requires the direct visible Schur lower bound.

This is a major reduction from treating the entire bulk symbol packet as the
unresolved finite block.

## What would close the scalar inequality

Equation (L-15606.8) does not by itself prove `D<=C`.  It proves that the only
possible surplus is finite and plunge-sized.  The exact inequality follows once
all those surplus directions are either:

1. repaired and adjoined to `L`; or
2. certified above `Gamma` by the finite Schur complement of `L-15604`.

The remaining theorem is therefore a direct estimate on a logarithmic-sized
plunge/visible block, not a bulk capacity comparison.

## Proof boundary

- The counting identity is exact elementary algebra.
- Uniform source-to-form control on the whole high-concentration packet is an
  external hypothesis.
- The latest plunge estimates do not prove the arithmetic visible-block floor.
- This lemma does not prove `D<=C` or RH by itself.
