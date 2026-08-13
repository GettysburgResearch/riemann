# L-91334 — The common rough Hilbert innovation embeds into one bounded native endpoint port

Claim ID: `L-91334`  
Status: **PROVED EXACT MATRIX-PORT EMBEDDING / BOUNDED-COST THEOREM**  
Created: 2026-08-12  
Depends on: `L-91316`, `L-91320`, `L-91324`, `L-91333`  
RH status: **unproved**

## 1. The two fixed matrices

Retain the common rough Hilbert metric

\[
 H=\begin{pmatrix}2&-3\\-3&5\end{pmatrix}>0.
\tag{L-91334.1}
\]

Its trace is seven and its determinant is one. Hence

\[
 \boxed{
 H\prec7I_2.
 }
\tag{L-91334.2
 }

For the finite Boolean block through `61`, retain the native endpoint Schur port

\[
 \mathcal P_{61}(x)
 =\begin{pmatrix}
  \mathcal V_{61}(x)&\mathcal B_{61}(x)\\
  \mathcal B_{61}(x)&\mathcal V_{61}(x)
 \end{pmatrix}.
\tag{L-91334.3}

`L-91316/L-91320` prove pointwise

\[
 \boxed{
 \mathcal P_{61}(x)
 \succeq\frac19\mathcal V_{61}(x)I_2.
 }
\tag{L-91334.4
 }

## 2. Pointwise embedding

Multiplying (L-91334.2) by `mathcal V_61(x)/2` and using
(L-91334.4) gives

\[
\boxed{
 \frac12\mathcal V_{61}(x)H
 \preceq\frac72\mathcal V_{61}(x)I_2
 \preceq\frac{63}{2}\mathcal P_{61}(x).
}
\tag{L-91334.5
 }

Thus one fixed multiple of one native endpoint port dominates the complete
common Hilbert budget.

No dependence on the number, size or order of the rough primes appears.

## 3. Multiprime correction budget

For an ordered rough cascade, `L-91333` proves

\[
 \sum_j C_j^*C_j\preceq\frac12H,
\tag{L-91334.6}

where `C_j` is the minimal rank-one projective correction at stage `j`, already
transported to the common initial state coordinate.

Tensoring with the positive endpoint density `mathcal V_61(x)` and using
(L-91334.5),

\[
\boxed{
 \mathcal V_{61}(x)
 \sum_j C_j^*C_j
 \preceq\frac{63}{2}\mathcal P_{61}(x).
}
\tag{L-91334.7
 }

This is the desired nonduplicating endpoint-port allocation: every rough prime
uses one innovation slice of a common budget, and the total fits into one
bounded positive port.

## 4. Positive functoriality and color erasure

Every operation used in the reset is positive and linear at the matrix-valued
measure level:

```text
least-prime branch restriction;
affine parent-coordinate pushforward;
physical-column evaluation;
summation over colors;
martingale B-spline quantization.
```

By `L-91324`, applying any composition of these functors to
(L-91334.7) preserves the positive-semidefinite order. Therefore branch colors
may be forgotten after all innovations are assembled, without creating one
fresh endpoint port per color.

The finite mismatch and terminal repairs are then applied once to the total
positive endpoint measure, as required by `L-91329`.

## 5. Bounded endpoint-score mass

The normalized endpoint mass of `mathcal V_61` is

\[
 \prod_{p\le61}\left(1+\frac1p\right)<\frac{14}{3}.
\tag{L-91334.8}

Consequently the crude total normalized mass of the port on the right side of
(L-91334.7) is bounded by

\[
 \boxed{
 \frac{63}{2}\frac{14}{3}=147.
 }
\tag{L-91334.9
 }

This constant is deliberately unoptimized. It is independent of the parent
endpoint and of the rough-prime cascade. Positive endpoint quantization and the
finite collar machinery therefore charge only `O(1)` score per factor-54 reset.

The port cost is additive boundary debt, not an inherited score-loss
coefficient.

## 6. What remains

The global projective correction and physical color-erasure costs are now paid
by one bounded native endpoint port. What is not supplied by this matrix theorem
is the exact positive **source partition** determining which child state is
fed into which innovation slice.

That remaining partition must be constructed before the Hilbert telescope is
applied. `R-91305` forbids feeding the full parent source independently into
every prime branch.

```text
ordered Hilbert innovation telescope               EXACT
all projective corrections share one budget         EXACT
common budget -> one endpoint Schur port             EXACT
physical color erasure of total port                 EXACT
bounded total endpoint-score cost                    EXACT
least-prime disjoint positive source partition       OPEN
all-generation reset                                 OPEN / RH-BEARING
Riemann Hypothesis                                   UNPROVEN
```
