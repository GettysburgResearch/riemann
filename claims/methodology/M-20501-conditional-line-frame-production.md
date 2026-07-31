# M-20501 — Production protocol for conditional line frames

Claim ID: `M-20501`  
Status: `PROPOSED METHODOLOGY`  
Authoring agent: `gpt56-03-q`  
Created: 2026-08-01

## Objective

Certify the final selected-real-zero kernel without demanding absolute smallness
of its exact Möbius tail.

## Required objects

At each finite support retain one common metric and basis for:

1. the inherited packet \(R\);
2. its complete complement \(W\);
3. the first simple-line frame \(Z\);
4. the graph kernel \(K_Z\);
5. the second simple-line frame \(Y\);
6. the complete signed residual after subtracting \(Y\);
7. the positive ambient complement and kernel cross.

## Construction order

### 1. First frame

Build directed evaluation matrices

```text
A = V_Z|R
B = V_Z|W
```

and certify `B` invertible.

Form exactly

```text
J = [I; -B^-1 A]
G_K = J* G_U J.
```

### 2. Second frame

Build

```text
C = V_Y|R
D = V_Y|W
S = C-D B^-1 A.
```

Do not replace `S` by `C`.

Require an exact or directed positive LMI

```text
S* M_Y S >= sigma^2 G_K.
```

### 3. One-sided residual

Subtract the selected positive \(Y\)-zero form exactly once. Produce one complete
signed residual matrix and certify only

```text
R_Y|K >= -omega G_K.
```

No upper bound is required.

### 4. Schur cross

With the same graph basis and complement metric, certify

```text
J* Z_K* C^-1 Z_K J <= chi G_K.
```

### 5. Verdict

The exact kernel margin is

```text
margin = sigma^2-omega-chi.
```

Accept strict positivity if `margin>0`; accept a cofinal lower-envelope level if
`margin>=-epsilon`.

## Frame selection

The finite simple-line uniqueness theorem guarantees termination of an
algorithmic row search at each fixed level:

1. enumerate proof-grade simple critical-line zero intervals;
2. append directed evaluation rows;
3. pivot the first block until `B` has a certified inverse;
4. condition the remaining rows through `S=C-D B^-1 A`;
5. pivot until `S` has a certified inverse;
6. optimize the lower frame endpoint against the one-sided residual cost.

Greedy max-volume or QR may nominate rows, but the proof object stores only
directed matrices and exact inequalities.

## Möbius producer

Use PR #204 as an independent residual producer:

- physical divisor coefficients;
- Mellin multiplier;
- optional free Dirichlet coefficients.

The selected residual Weil matrix is invariant under these choices. Optimization
may be used only for analytic norm and Schur-cross reduction.

## Prohibited inferences

Do not infer a proof from:

- finite frame existence without a quantitative moat;
- a small absolute tail on a few vectors;
- dimension equality;
- a floating singular value;
- positive selected mass without the complete residual;
- optimizing Möbius coefficients and observing a better Hardy norm;
- subtracting the same selected zero from both frame and residual.

## Independent reproduction

A promoted production result should have:

- two directed special-function backends for evaluation rows;
- an exact rational matrix consumer;
- independent residual assembly;
- immutable zero-census and source provenance;
- mutation tests for row deletion, row duplication, frame singularity,
  residual sign, and Schur-cross inflation.
