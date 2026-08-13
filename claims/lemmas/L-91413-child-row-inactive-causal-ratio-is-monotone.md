# L-91413 — Before the child row activates, the causal row-per-score ratio is monotone

Claim ID: `L-91413`  
Status: **PROVED EXACT ANALYTIC MONOTONICITY THEOREM — FINITE ACTIVE-CHILD GATES REMAIN**  
Created: 2026-08-13  
Depends on: `L-91359` single-endpoint profile monotonicity  
RH status: **unproved**

## 1. Causal quotient below child-row activation

Fix a row `2<=j<=66`, a prime parameter `p>=67`, and put `r=p^-1/2`.  Let

\[
 S(Y)=5\sqrt Y-3,
 \qquad
 \phi_j(Y)=\frac{Q_Y(j)}{S(Y)}.
\]

For

\[
 1<=z<=j,
\]

the child row is causally zero:

\[
 Q_z(j)=0.
\]

The causal quotient therefore has the exact factorization

\[
 \boxed{
 q_{p,j}(z)
 =\frac{Q_{pz}(j)}{S(pz)-rS(z)}
 =\phi_j(pz)
  \frac{S(pz)}{S(pz)-rS(z)}.
 }
 \tag{L-91413.1}
\]

## 2. Both factors are increasing

The first factor `phi_j(pz)` is nondecreasing by `L-91359`.

For the second factor, put `u=sqrt(z)` and `a=sqrt(p)>1`.  Then

\[
 \frac{S(z)}{S(pz)}
 =\frac{5u-3}{5au-3}.
 \tag{L-91413.2}
\]

Direct differentiation gives

\[
 \frac d{du}
 \frac{5u-3}{5au-3}
 =\frac{15(a-1)}{(5au-3)^2}>0.
 \tag{L-91413.3}
\]

Hence

\[
 \frac{S(pz)}{S(pz)-rS(z)}
 =\left[1-r\frac{S(z)}{S(pz)}\right]^{-1}
 \tag{L-91413.4}
\]

is strictly increasing.  Both factors in (L-91413.1) are nonnegative, so

\[
 \boxed{
 z\longmapsto q_{p,j}(z)
 \text{ is nondecreasing on }[1,j].
 }
 \tag{L-91413.5}
\]

It is strict once the parent row has activated.

## 3. Discrete source consequence

For two child-active source indices `d_1<d_2<=y`, put

\[
 z_i=\frac y{d_i}.
\]

If

\[
 z_1,z_2<=j,
\]

then `z_1>=z_2` and (L-91413.5) gives

\[
 \boxed{
 \frac{K_R^{(j)}(d_1)}{K_S(d_1)}
 >=
 \frac{K_R^{(j)}(d_2)}{K_S(d_2)}.
 }
 \tag{L-91413.6}
\]

Thus every inner discrete-order comparison for which both child rows are inactive is closed analytically.

## 4. Size of the remaining inner family

An odd source can have an active child row only if

\[
 o<=\frac yj<=\frac{67}{j}.
 \tag{L-91413.7}
\]

Since the least odd source is `2`, no odd child-row-active comparison exists for

\[
 j>=34.
 \tag{L-91413.8}
\]

Therefore the continuous causal-ratio counterexample at row `66` cannot occur between two arithmetic parity nodes whose child rows are active.  All rows `34,...,66` are reduced to the inactive-child theorem plus finitely many activation-straddling pairs.  The genuinely active-child ordering problem is confined to rows `2,...,33` and the finite divisor set below `67/j`.

## 5. Boundary

```text
causal quotient factorization below activation      EXACT
single-endpoint factor increasing                    IMPORTED EXACT
score correction factor increasing                   EXACT
inactive-child causal ratio monotone                  EXACT
all inner comparisons at rows >=34                   REDUCED TO FINITE STRADDLES
active-child small-row comparisons                    OPEN / FINITE-DIRECTED
continuous all-z causal monotonicity                  NOT CLAIMED / FALSE
Riemann Hypothesis                                    UNPROVEN
```
