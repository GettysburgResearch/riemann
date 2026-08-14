# L-91687 — The `P_5` first-order row is positive through the sixth quotient wall

Claim ID: `L-91687`  
Status: **PROVED DIRECTED / EXACT CELL REDUCTION**  
Created: 2026-08-14  
Depends on: exact activation-cell formula for `Q_Y(j)`; `L-91682`, `L-91685`, `L-91686`  
Replay: `X-91685-target-lorenz-vector-primal-dual/verify_quotient6.py`  
RH status: **unproved**

## 1. Directed row theorem

For

\[
 12\le j\le66,
 \qquad
 \max(67,5j)\le x\le6j,
\]

one has

\[
 \boxed{
 Q_x(j)
 -\frac1{\sqrt2}Q_{x/2}(j)
 -\frac1{\sqrt3}Q_{x/3}(j)
 -\frac1{\sqrt5}Q_{x/5}(j)>0.
 }
 \tag{L-91687.1}
\]

The endpoint replay uses outward rational square-root and logarithm enclosures.
No displayed decimal decides a sign.

## 2. Why integer endpoints are complete

On an activation cell

\[
 N\le Y<N+1,
\]

write

\[
 Q_Y(j)=C_{j,N}\log Y-D_{j,N}.
\]

For each `d in {1,2,3,5}`, the activation walls of `Q_{x/d}(j)` occur at

\[
 x=dn,
 \qquad n\in\mathbb Z.
\]

All such walls are integers. Between consecutive integers, every activation
index is fixed and the left side of (L-91687.1) has the form

\[
 A\log x+B.
\]

It is monotone on that open cell, so its minimum is attained at an endpoint.
The directed replay checks every integer endpoint in the stated domain. This
is an exact finite-cell reduction, not a grid approximation.

## 3. Target-Lorenz consequence for `5j<=x<6j`

Let `x=py` with `p>=67` and `1<=y<67`. If `x<6j`, then

\[
 y=\frac{x}{p}<\frac{6j}{67}<j,
\]

so all child rows are inactive. In the strip

\[
 5j\le x<6j,
\]

the row-active source atoms are exactly

```text
even: 1;
odd:  2,3,5.
```

There are two cases.

### `O_T<=T_1`

The Target-Lorenz removal uses `O_T/T_1` of atom `1`. Since the row-per-target
profile is nonincreasing,

\[
 \frac{O_T}{T_1}R_1
 \ge
 \sum_{d\in\{2,3,5\}}R_d.
 \tag{L-91687.2}
\]

Indeed the odd target total contains the target of every row-active odd atom.

### `O_T>T_1`

The Target-Lorenz removal uses all of atom `1`, and (L-91687.1) gives

\[
 R_1>R_2+R_3+R_5.
 \tag{L-91687.3}
\]

Thus in both cases

\[
 \boxed{
 R_j(U)-O_R^{(j)}>0
 \qquad(5j\le py<6j).
 }
 \tag{L-91687.4}
\]

Combining with `L-91686`, the exact Target-Lorenz row gate now holds throughout

\[
 \boxed{py<6j.}
 \tag{L-91687.5}
\]

## 4. Exact boundary

```text
cell reduction to integer endpoints          EXACT
all endpoint signs through quotient six      DIRECTED EXACT
Target-Lorenz row gate for py<6j             PROVED
first unresolved quotient sector             py>=6j
Riemann Hypothesis                            UNPROVEN
```
