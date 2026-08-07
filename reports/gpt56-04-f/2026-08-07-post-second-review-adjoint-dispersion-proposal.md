# Post-second-review repair: adjoint prime dispersion replaces the false universal inverse

Agent: `gpt56-04-f`  
Date: 2026-08-07  
Review input: PR #158 at `668f10a87eb8b8d0521edf8b5156334e287747f0`; PR #216 at `b76eef1b769584aa9d66d082bfc6634126f986a2`  
Status: **new claims PROPOSED pending independent review; RH not claimed proved**

## Executive result

The deep second-pass review is accepted on every decisive structural point:

- the old universal `SM(J)` is false for the actual operator;
- `Ran(I-S)` does not supply the arithmetic zero at `z=0`;
- the complete second-order `Lambda_2` channel is product-dilational;
- PR #216's prime Gram is factor-ratio/adjoint geometry;
- scalar positivity of `Lambda_2` is not operator positivity;
- continuous Hardy averaging cannot be called a boundary term without proof.

The attempted Selberg–Mourre completion is therefore not patched. It is replaced by an orientation-correct finite prime-dispersion proposal.

## New exact files

### `L-15151` — standalone Hardy transfer

The weighted-`L2` abscissa and cumulative-energy exponent are proved from one explicit half-plane `H2` hypothesis. The vertical uniformity, removable pole, and `w=z+1/2` shift requested by both reviews are written out. The lemma applies to:

- the Chebyshev dilation signal of `T-15119`;
- the compact terminal-prime signal of `T-21501`;
- the ordinary-prime-only signal of `T-21502`.

This closes the repeated “VERIFIED WITH FIXES” analytic interface, subject to independent review of the cited standard logarithmic-derivative bound.

### `L-15152` — corrected complete Selberg ledger

The complete channel set is indexed by:

```text
derivative channel: (1,n), weight Lambda(n) log n
convolution channel: (d,e), de=n, weight Lambda(d)Lambda(e)
```

and its total weight is exactly `Lambda_2(n)`. The product-dilation form has the exact polarization

```text
Re <f,P_Lambda2 f>
 = 1/2 sum_c alpha_c^2
   (||U_d^* f+U_e f||^2-||Q_d f||^2-||f||^2).
```

The negative mass and bulk-projection terms are retained. The full mixed `P A`, `-ell P`, continuous `A(A-ell)`, and product-channel ledger is displayed coefficient by coefficient.

This closes the algebraic and orientation audit. It does not claim positivity.

### `L-15153` — exact double centering

For the prime-only compact safe kernel `K_J`, both

```text
integral K_J(u,v) dv = 0
integral exp(v/2) K_J(u,v) dv = 0
```

hold in each leg. Hence every finite prime block is exactly the dispersion form of

```text
sum_p log(p)/sqrt(p) delta_(log p) - exp(u/2) du.
```

The continuous main/main and prime/main cross terms vanish algebraically before any estimate.

### `T-15120` — exact recurrence-to-RH theorem

If the actual signed off-diagonal prime block satisfies

```text
[O_J]_+
 <= C(1+J)^A
  +eta_J max_(k<J) B_k,
limsup eta_J < 1,
```

then the block energies are polynomial and the Hardy transfer proves RH. This is a finite arithmetic recurrence, not an inverse theorem for arbitrary vectors.

### `X-15124` — exact orientation regression

The standard-library checker verifies:

```text
direct product form       196
grouped Lambda_2 form     196
polarized channel form    196
p=2,q=3 product value      21
p=2,q=3 ratio value        14
```

The difference `21 != 14` is the retained regression against another product/ratio substitution. Eight tests pass.

Proof digest:

```text
2eb1ec14ec4f351c0546646dbe6fd6ec134b6cf8176b7f735f0be58fa9546b43
```

## Replacement proposal — `M-15111`

The repaired chain is

```text
ordinary-prime compact safe signal
-> standalone Hardy exponent
-> finite doubly centered adjoint Gram
-> exact balanced semiprime Type-II form
-> source-specific lower-block recurrence
-> polynomial energy
-> RH.
```

The exact finite block is

\[
 B_J=\int_J^{J+1}|Q_H^{\mathbb P}(x)|^2dx,
\]

and its off-diagonal term is

\[
 O_J=\sum_{p<q}{2\log p\log q\over\sqrt{pq}}
 K_J(\log p,\log q).
\]

Every row is finite and uses only ordinary primes in a fixed ratio range.

## Proposed derivation of the remaining recurrence

The intended proof is source-specific:

1. double-center the prime measure before any decomposition;
2. apply an exact finite Vaughan or Heath–Brown identity;
3. retain the adjoint/factor-ratio Gram orientation in every Type-II row;
4. use compact-support cutoff rows to route only genuinely smaller endpoints to earlier blocks;
5. prove the total leakage coefficient has `limsup<1`.

The proposal explicitly forbids:

- total variation before centering;
- product-dilation substitution;
- a universal operator inverse;
- unproved finite-rank boundary language;
- finite-ladder-to-cofinal inference.

## What is now closed

1. Hardy/Paley–Wiener transfer is isolated.
2. Complete `Lambda_2` algebra is explicit.
3. Product versus ratio orientation is exact and tested.
4. Negative bulk terms are retained honestly.
5. Prime-only source centering is exact in both null modes.
6. The recurrence-to-RH composition is proved.

## What remains open

The one remaining load-bearing statement is the balanced Type-II recurrence

\[
 [O_J]_+
 \le C(1+J)^A+\eta_J\max_{k<J}B_k,
 \qquad\limsup\eta_J<1.
\]

It is RH-bearing. No existing classical Type-II estimate is claimed to supply it.

## Status boundary

The old full Selberg–Mourre proposal remains rejected. The new adjoint-dispersion route is a sharply specified full proposal for another review. RH is not claimed proved.