# L-91410 — The causal row/score secant separates the child-active and frontier sectors

Claim ID: `L-91410`  
Status: **PROVED EXACT ANALYTIC SEPARATION THEOREM — LORENZ DETERMINANT SEPARATE**  
Created: 2026-08-13  
Depends on: `L-91359` single-endpoint score-normalized component monotonicity; causal component and score kernels  
Repairs the usable scope after: `R-91311` continuous causal-ratio counterexample  
RH status: **unproved**

## 1. Single-endpoint profile

Fix a row `2<=j<=66`.  Put

\[
 S(Y)=5\sqrt Y-3
\]

and extend the component row causally by `Q_Y(j)=0` for `Y<j`.  Define

\[
 \phi_j(Y)=\frac{Q_Y(j)}{S(Y)}
 \qquad(Y>=1).
 \tag{L-91410.1}
\]

`L-91359` proves that `phi_j` is nondecreasing on the complete half-line and strictly increasing after activation.

## 2. Causal one-prime secant

Let

\[
 p>=67,\qquad r=p^{-1/2},\qquad z>=1.
\]

The child-active causal row-per-score ratio is

\[
 \boxed{
 q_{p,j}^{\rm in}(z)
 =\frac{Q_{pz}(j)-rQ_z(j)}
        {S(pz)-rS(z)}.
 }
 \tag{L-91410.2}
\]

The denominator is strictly positive.  Writing `Q=phi S` and subtracting the right-endpoint profile gives the exact identity

\[
 \boxed{
 q_{p,j}^{\rm in}(z)-\phi_j(pz)
 =
 \frac{rS(z)[\phi_j(pz)-\phi_j(z)]}
      {S(pz)-rS(z)}
 >=0.
 }
 \tag{L-91410.3}
\]

Therefore

\[
 \boxed{
 q_{p,j}^{\rm in}(z)
 >=\phi_j(pz)
 >=\phi_j(p).
 }
 \tag{L-91410.4}
\]

This is an upper-secant phenomenon: the negative child term pushes the quotient above the larger-endpoint profile rather than between the two endpoint values.

## 3. Frontier sector

For a source node `d>y` in the causal packet at `x=py`, the child term is inactive and

\[
 q_{p,j}^{\rm out}(d)
 =\frac{K_R^{(j)}(d)}{K_S(d)}
 =\phi_j\!\left(\frac{py}{d}\right).
 \tag{L-91410.5}
\]

Since `d>y`,

\[
 \frac{py}{d}<p,
\]

and hence

\[
 \boxed{
 q_{p,j}^{\rm out}(d)
 <=\phi_j(p).
 }
 \tag{L-91410.6}
\]

Combining (L-91410.4) and (L-91410.6),

\[
 \boxed{
 \text{every child-active source ratio is at least every frontier-source ratio.}
 }
 \tag{L-91410.7}
\]

The ordering is uniform in `p`, `y`, the source node and the row.

## 4. Ordering on the actual Lorenz residual

`L-91359` on the review branch proves that the score-Lorenz cutoff `c` satisfies

\[
 c>y.
 \tag{L-91410.8}
\]

Consequently the complete Lorenz residual is child-inactive.  On its support `d>=c`,

\[
 q_{p,j}(d)=\phi_j(py/d)
\]

is nonincreasing in `d`.  Moreover every removed child-active even source has ratio at least the cutoff ratio:

\[
 d<=y<c
 \Longrightarrow
 q_{p,j}(d)>=\phi_j(p)>=q_{p,j}(c).
 \tag{L-91410.9}
\]

Thus the continuous counterexample in `R-91311`, which lies inside the child-active secant family, cannot create an ordering reversal across the actual Lorenz cutoff.

## 5. What this does and does not prove

The theorem closes the interface ordering and proves monotonicity on the residual support.  It does not by itself compare the row average of the removed even score mass with the odd row average.  That remaining comparison is one scalar cutoff determinant, isolated in `L-91411`.

```text
single-endpoint profile monotonicity                 IMPORTED / L-91359
causal secant identity                               EXACT
child-active ratio >= phi_j(p)                       EXACT
frontier ratio <= phi_j(p)                           EXACT
inner/outer global separation                        EXACT
ordering on actual Lorenz residual                   EXACT USING c>y
continuous causal monotonicity                       NOT USED / FALSE
cutoff determinant                                   SEPARATE OPEN SIGN
Riemann Hypothesis                                   UNPROVEN
```
