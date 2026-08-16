# L-91781 — The proportional Target-Lorenz determinant is positive on the complete compact domain `py<166000`

Claim ID: `L-91781`  
Status: **PROVED DIRECTED FINITE/REAL CELL THEOREM**  
Created: 2026-08-15  
Depends on: `L-91780`; exact component row from `L-91112.25--26`  
Replay: `X-91780-target-lorenz-compact-avlt`  
RH status: **unproved**

## 1. Statement

Let

\[
 p\ge67,\qquad 1\le y<67,\qquad x=py<166000,
 \qquad 2\le j\le66.
\]

For the actual causal `P_61` atoms define

\[
 K_T(d)=d^{-1/2}\bigl[T(x/d)-p^{-1/2}T(y/d)\bigr],
 \qquad T(z)=4\sqrt z-3
\]

with causal zero extension, and

\[
 K_R^{(j)}(d)=d^{-1/2}
 \bigl[Q_{x/d}(j)-p^{-1/2}Q_{y/d}(j)\bigr].
\]

Let `E_T,O_T,E_R^(j),O_R^(j)` be the positive even/odd parity totals. Then

\[
 \boxed{
 \Theta_j(p,y)=O_TE_R^{(j)}-E_TO_R^{(j)}>0.
 }
\tag{L-91781.1}
\]

Consequently `L-91780` gives

\[
 \boxed{\mathfrak L_j(p,y)>0}
\tag{L-91781.2}
\]

on the complete compact domain.

## 2. Exact activation-cell form

Put

\[
 N=\lfloor x\rfloor,\qquad k=\lfloor y\rfloor,
 \qquad t=\sqrt x,\qquad q=p^{-1/2}=\sqrt{y/x},
 \qquad L=\log x.
\]

On one parent/child activation cell, the parity row totals have the exact form

\[
 j(j-1)R_\sigma
 =(a_{\sigma,N}-q a_{\sigma,k})L
 -b_{\sigma,N}+q b_{\sigma,k}
 -2q a_{\sigma,k}\log q.
\tag{L-91781.3}
\]

The integer coefficient recurrence used to construct `a,b` is

```text
for n=d m with d|P61:
  +2                    on rows 2,...,m-2;
  -m(m-3)               on row m-1;
  +m(m+1)               on row m;
```

with the parity of `d`. This is exactly the finite Euler transform of the
three-sector formula for `Q`.

The target totals are

\[
 T_\sigma=4t(A_{\sigma,N}-q^2A_{\sigma,k})
 -3(B_{\sigma,N}-qB_{\sigma,k}).
\tag{L-91781.4}
\]

Expanding (L-91781.1) gives a polynomial in

\[
 t,\ L,\ q,\ q^2,\ q^3,
 \ q\log q,\ q^2\log q,\ q^3\log q
\]

whose coefficients are fixed on the cell. No cancellation is evaluated by
subtracting two already-rounded determinants.

## 3. Complete real-cell enclosure

For every

```text
67 <= N < 166000;
1 <= k <= min(66,floor(N/67));
2 <= j <= 66,
```

the checker encloses the full real rectangle satisfying

\[
 N\le x<N+1,\qquad k\le y<k+1,\qquad p=x/y\ge67.
\]

It uses exact fixed-point outward enclosures for inverse square roots and
logarithms, monotonic endpoint enclosures for `q^r log q`, and the expanded
formula above. The total census contains

\[
 \boxed{702511095}
\]

row-cell inequalities.

Exactly `702511091` cells are closed directly by the coarse rectangle. The
smallest raw directed lower endpoint among them is

\[
 0.0012010574018749666\ldots
\]

at `(N,k,j)=(125,1,62)`. A separate primitive and floating-operation audit is
rowwise; after its conservative deduction every directly closed cell retains
margin greater than

\[
 \boxed{10^{-3}}.
\tag{L-91781.5}
\]

## 4. Four dependency exceptions

The only coarse rectangles whose independent `t,q` enclosure crosses zero are

```text
(127,1,63), (129,1,64), (131,1,65), (133,1,66).
```

Here `N=2j+1` and `1<=y<2`. Only the child target atom `d=1` is active, while
all child component rows vanish. The child correction to `E_T` equals

\[
 \frac{4y-3\sqrt y}{\sqrt x},
\]

which is increasing in `y`. Since the odd row is nonnegative, the determinant
is minimized at `y=1`. Restoring the exact correlation `q=1/sqrt(x)` leaves a
one-variable interval on `2j+1<=x<2j+2`. Directed evaluation gives respective
lower bounds

```text
j=63: 0.329048733868...
j=64: 0.324125573978...
j=65: 0.320026347386...
j=66: 0.315372789821...
```

all above `3/10`.

## 5. Boundary

```text
compact real activation cells py<166000     PROVED DIRECTED
Target-Lorenz compact row margins            PROVED BY L-91780
unbounded domain py>=166000                  OPEN / L-91782 RESERVE ONLY
live native root source/channel allocation   OPEN
Riemann Hypothesis                           UNPROVEN
```
