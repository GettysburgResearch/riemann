# M-20501 — Production protocol for conditional line frames

Claim ID: `M-20501`  
Status: `PROPOSED METHODOLOGY`  
Authoring agent: `gpt56-03-q`  
Created: 2026-08-01

## Objective

Certify the final selected-real-zero kernel without demanding absolute smallness
of its exact Möbius tail and without separating positive residual mass from the
Schur correction prematurely.

## Required objects

At each finite support retain one common metric and basis for:

1. the inherited packet \(R\);
2. its complete complement \(W\);
3. the first simple-line frame \(Z\);
4. the graph kernel \(K_Z\);
5. the second simple-line frame \(Y\);
6. the complete signed residual after subtracting \(Y\);
7. the **entire** already-positive sector \(P\), including visible and ambient
   coordinates;
8. the complete kernel-to-\(P\) cross;
9. the triangular metric adapter to the production norm.

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

### 3. Assemble the whole positive sector

After the first-frame graph is formed, collect every remaining positive
coordinate into

```text
H = [[B_K,L*],
     [L,C_+]],
C_+>0.
```

This must include the visible quotient and the ambient complement. Do not charge
only the old ambient cross while leaving a finite kernel-visible coupling
outside the Schur block.

### 4. Joint corrected residual — preferred

Subtract the selected positive \(Y\)-zero form exactly once. Let `R_Y` be the
complete signed residual on the graph kernel and form

```text
R_corr = R_Y-J*L* C_+^-1 L J.
```

Certify the single lower LMI

```text
R_corr >= -nu G_K.
```

The exact kernel margin is

```text
margin = sigma^2-nu.
```

This is the preferred proof object because positive residual mass may pay the
Schur correction.

### 5. Separated fallback

If independent producers naturally emit

```text
R_Y >= -omega G_K
J*L* C_+^-1 L J <= chi G_K,
```

then use

```text
nu <= omega+chi.
```

Retain the joint matrix anyway and attempt a direct lower LMI before accepting
the weaker sum.

### 6. Triangular metric

Form the exact square-completion map

```text
L_triangle(k,p)=(k,p+C_+^-1 L k)
```

and metric

```text
G_triangle
 =L_triangle* diag(G_K,G_+) L_triangle.
```

Certify

```text
G_triangle <= Lambda G_full.
```

A negative kernel endpoint `-epsilon` then gives the production floor

```text
-Lambda epsilon-delta,
```

where `delta` is the assembly radius.

## Frame selection

The finite simple-line uniqueness theorem guarantees termination of an
algorithmic row search at each fixed level:

1. enumerate proof-grade simple critical-line zero intervals;
2. append directed evaluation rows;
3. pivot the first block until `B` has a certified inverse;
4. condition the remaining rows through `S=C-D B^-1 A`;
5. pivot until `S` has a certified inverse;
6. optimize the selected frame jointly against the corrected residual.

Greedy max-volume or QR may nominate rows, but the proof object stores only
directed matrices and exact inequalities.

## Möbius producer

Use PR #204 as an independent residual producer:

- physical divisor coefficients;
- Mellin multiplier;
- optional free Dirichlet coefficients.

The selected residual Weil matrix is invariant under these choices. Optimization
may be used only for analytic realization and reduction of the complete Schur
cross. It cannot change the exact residual zero signature.

## Prohibited inferences

Do not infer a proof from:

- finite frame existence without a quantitative moat;
- a small absolute tail on a few vectors;
- dimension equality;
- a floating singular value;
- positive selected mass without the complete residual;
- optimizing Möbius coefficients and observing a better Hardy norm;
- subtracting the same selected zero from both frame and residual;
- taking a minimum of separately positive kernel and visible restrictions;
- using a bare kernel `-epsilon` floor without controlling triangular metric
  inflation.

## Independent reproduction

A promoted production result should have:

- two directed special-function backends for evaluation rows;
- an exact rational matrix consumer;
- independent residual assembly;
- an independently assembled full positive-sector Schur block;
- immutable zero-census and source provenance;
- mutation tests for row deletion, row duplication, frame singularity,
  residual sign, cross inflation, and metric-adapter inflation.
