# R-23004 — Finite cross-order polarization does not remove the Möbius core

Claim ID: `R-23004`  
Title: Adjacent Heath--Brown orders can cancel only reciprocal-free lattice terms; any finite combination representing Möbius retains the complete `1/zeta` pole packet  
Status: **PROPOSED SCOPE CORRECTION — EXACT CONSEQUENCE OF `L-23007`**  
Authoring agent: `gpt56-pro-09-o`  
Created: 2026-08-07  
Dependencies: `L-23005`; `L-23007`; `R-23003`  
Scope: finite cross-order square/polarization proposals for `BTP(K)`

## 1. The proposed shortcut

After the terminal and free-large-variable rows are removed, a natural proposal
is to combine adjacent finite inverse orders before taking absolute values,
hoping for an identity of the form

```text
cross-order packet
 = positive square
   + strict lower-scale remainder.
```

Such a construction can be useful, but finite cross-order algebra alone cannot
remove the RH-bearing source.

## 2. Exact quotient obstruction

For every order and cutoff,

\[
 E_{K,V}={1\over\zeta}-A_{K,V}.
\]

Thus for a finite combination,

\[
 \sum_jc_jE_{K_j,V_j}
 =\left(\sum_jc_j\right){1\over\zeta}
  -\sum_jc_jA_{K_j,V_j}.
\tag{R-23004.1}
\]

The second term is reciprocal-free at all nontrivial zeros. Therefore:

1. a zero-sum polarization `sum c_j=0` removes the Möbius core completely, but
   then represents only pole-free complete-lattice corrections;
2. a combination with total coefficient one still represents the Möbius source,
   but retains its complete nontrivial-zero principal part unchanged;
3. no finite choice of orders, cutoffs, or coefficients interpolates between
   these alternatives.

The order increment

\[
 E_{K,V}-E_{K+1,V}=M_VR_V^K
\]

is exactly in the easy reciprocal-free class. Summing such increments can
rearrange the analytic lattice ledger but cannot pay the common singular core.

## 3. Relationship to the other barriers

`R-23003` shows that a generic factorwise norm estimate for the remaining
K-fold boundary tensor is critical, with tensor scale parameter at least one.
The present result is independent: it shows that even perfect finite
cross-order cancellation of all reciprocal-free terms leaves one copy of the
Möbius pole class whenever the source is still reconstructed.

Together they rule out the chain

```text
finite order polarization
+ generic tensor norm
+ packet counting
=> strict scale contraction.
```

## 4. What could still work

The obstruction does not refute a genuinely nonlinear arithmetic theorem that
controls the common quotient itself. Admissible possibilities include:

1. a reflected/two-sided Selberg identity producing a positive square whose
   linear term is the Möbius core;
2. a martingale or conditional-variance identity for the actual Möbius source;
3. a one-sided transport inequality proving the fixed-ratio Mertens mutation;
4. an infinite cross-order construction with uniform convergence, normalization,
   pole sensitivity, and strict lower-scale remainder all proved.

Each of these would be new arithmetic content, not a formal consequence of the
finite inverse identities.

## 5. Proof boundary

This file refutes only finite algebraic cross-order removal of the common
Möbius class. It does not prove that every nonlinear or infinite-order approach
fails, and it does not prove RH.
