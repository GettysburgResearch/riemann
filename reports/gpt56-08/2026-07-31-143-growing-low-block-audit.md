# Issue #143 continuation — the growing low block is an escaping-mode problem

Agent: `gpt56-08`  
Date: 2026-07-31  
Stack: PR #152 / `agent/gpt56-pro-09-b/143-squared-residual-floor`  
Classification: exact abstract closure theorem, exact scope refutation, no RH proof

## Executive conclusion

The remaining corrected low matrix

\[
 K_j=B_j-h_j^{-1}R_j^*M_j^{-1}R_j
\]

cannot be closed from decay of fixed radical rows and columns. The exact
counterexample

\[
 K_j=-e_je_j^*
\]

has every fixed entry eventually zero and converges strongly to zero, while its
minimum eigenvalue is `-1` at every level.

The final issue is therefore not matrix size or coefficient accumulation. It
is the exclusion of a **spectrally escaping mode**.

## New exact closure theorem

After embedding every changing low space in one common Hilbert space, strong
fixed-core decay plus the uniform tightness gate

\[
 \lim_{m\to\infty}\sup_j\|(I-P_m)K_j\|=0
\]

implies `||K_j||->0`. Quantitatively,

\[
 \|K_j\|\le
 \|P_mK_jP_m\|+2\|(I-P_m)K_j\|.
\]

This is the collectively compact route.

## Dimension-free radical route

A stronger application-specific route extends the entire low packet by exact
global radical vectors. If `V_j` is the joint discarded-tail synthesis map,
the radical identity gives

\[
 B_j=Q(V_j\cdot,V_j\cdot),
 \qquad
 R_j=-Q(V_j\cdot,E_j\cdot).
\]

Tail--tail and tail--complement continuity imply

\[
 K_j\succeq
 -\left(\alpha_j+\frac{\beta_j^2}{h_j}\right)I
\]

with no dimension factor. It suffices to prove

\[
 \alpha_j+\beta_j^2/h_j\to0.
\]

Under one form-controlling tail norm, this becomes a bound on the operator norm
of `V_j`, not on individual columns.

## Exact missing theorem

The repository does not currently prove either of the following for the full
support-dependent generalized-prolate packet:

1. common-frame collective compactness of the corrected blocks;
2. a form-norm spectral-synthesis theorem producing exact `E(S_0)` radical
   extensions with a shrinking joint tail-synthesis norm.

The finite Guinand--Weil dictionary maps finite source vectors to tests but is
not an inverse/density theorem for arbitrary low packets. The source paper's
prolate program likewise identifies convergence to the arithmetic target as a
remaining step. Therefore this packet-level statement cannot be inferred from
matching finite spectra or from fixed-column decay.

## Exact artifacts

- `R-14301`
- `L-14312`
- `L-14313`
- `X-14307`

The exact checker preserves:

```text
escaping mode minimum eigenvalue       -1 at every level
L-14312 synthetic norm upper            3/125
L-14313 synthetic floor loss            1/200
proof object SHA-256
a97c525a0efc578ece75038764be27dc59cd040763aabfbfae233e716b03965d
6/6 mutation tests PASS
```

## Strategic verdict

The new lemmas completely remove dimension from the estimate **conditional on
one uniform packet-level compactness or radical-tail bound**. They also prove
that fixed-row decay cannot substitute for that bound.

Obtaining the missing uniform spectral-synthesis theorem would close the low
matrix and, together with `T-14302`, prove RH. No such theorem is presently
proved here, so no RH proof is claimed.
