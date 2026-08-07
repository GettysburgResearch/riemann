# R-15101 — Nonnegative graph weights are not a complete target-pinned completion test

Claim ID: `R-15101`  
Status: `PROVED FINITE SCOPE NARROWING`  
Authoring agent: `gpt56-04-f`  
Created: 2026-07-31  
Target audited: the graph-separator implementation of `T-15103`  
Scope: finite target-pinned scalar completions only  
Counterexample status: not related to an RH counterexample

## Finding

The edgewise graph condition in `T-15103` is a correct sufficient certificate,
but its failure must not be interpreted as failure of the target-pinned scalar
completion.

For

\[
 T_p(c)=A_p+cB_p
\]

and `x_i=p_i y_i`, one has

\[
 x^{\mathsf T}T_p(c)x
 =
 \sum_{i<j}
 w_{ij}(c)(y_i-y_j)^2,
\]

where

\[
 w_{ij}(c)=-(Q_{ij}-c\eta_i\eta_j)p_ip_j.
\]

If all weights are nonnegative and their positive support graph is connected,
then `T_p(c)` is positive semidefinite with kernel `Rp`. The converse is false:
a positive signed Laplacian may contain negative individual edge weights.

## Exact counterexample to necessity

Use

\[
 \eta=(1,1,1,1)^{\mathsf T},
 \qquad
 p=(1,1,-1/2,-1/2)^{\mathsf T},
\]

and

\[
 Q=
 \begin{pmatrix}
 50&39&15&163\\
 39&54&45&141\\
 15&45&54&66\\
 163&141&66&542
 \end{pmatrix}.
\]

One has

\[
 Q=R^{\mathsf T}R,
 \qquad
 R=
 \begin{pmatrix}
 -3&2&5&-7\\
 -5&-5&-2&-18\\
 -4&-5&-5&-13
 \end{pmatrix},
\]

and `Rp=0`. Since `R` has rank three, `Q` is positive semidefinite with kernel
exactly `Rp`. Also `Qp=0`, so

\[
 T_p(0)=Q.
\]

The exact complement LDL pivots are

\[
 26,\qquad \frac{6075}{104},\qquad48,
\]

which is a strict completion certificate.

Nevertheless the graph interval is empty. The same-sign off-diagonal maximum is

\[
 \max\{Q_{12},Q_{34}\}=66,
\]

while the opposite-sign minimum is

\[
 \min\{Q_{13},Q_{14},Q_{23},Q_{24}\}=15.
\]

The graph rule would require simultaneously

\[
 c\ge66,\qquad c\le15.
\]

At the actual passing scalar `c=0`, the edge `(1,2)` has negative weight `-39`.

## Correction

Use the graph interval only as a cheap sufficient screen. If it is empty, the
level remains open until one of the complete `L-15107` outcomes is produced:

1. a rational scalar with positive complement LDL;
2. a rational `B`-isotropic nonpositive direction;
3. a rational conflicting-threshold pair;
4. a proof of the full Finsler isotropic-cone condition.

## Impact

This correction enlarges the positive search space. It does not invalidate any
previous graph-positive certificate and does not prove that any actual Hermite
target level passes.

The exact regression is retained in

```text
experiments/X-15103-finsler-target-completion/
  certificates/feasible-graph-empty.json
```

and is checked without floating-point arithmetic.
