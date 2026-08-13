# L-92002 — Actual-Xi order-three positivity is equivalent to one reciprocal-curvature inequality

Claim ID: `L-92002`  
Status: **PROVED EXACT REDUCTION; SCALAR SIGN OPEN**  
Created: 2026-08-13  
Depends on: `L-92000/L-92001`; `L-91904/L-91905`  
RH status: **unproved**

Put

\[
 \Xi(x)=\xi\left(\frac12+x\right),\qquad
 F(x)=\frac{\Xi'(x)}{\Xi(x)},\qquad
 p(t)=\frac{F(\sqrt t)}{\sqrt t}.
\]

For safe nodes `x_i>1/2`, the infinitesimal Caratheodory matrix is

\[
 \mathcal H_{ij}=\frac{F(x_i)+F(x_j)}{x_i+x_j}.
\]

The parent theorem gives `p>0`, `p` decreasing and `tp` increasing. `L-92001`
gives strict concavity of `tp`. Therefore the determinant factorization of
`L-92000` shows that every three-node matrix is positive if and only if
`1/p` is concave.

Equivalently, the sole order-three condition is

\[
 \boxed{p(t)p''(t)-2p'(t)^2\ge0\qquad(t>1/4).}
 \tag{L-92002.1}
\]

Indeed,

\[
 \left(\frac1p\right)''=\frac{2p'^2-pp''}{p^3}.
\]

Using `t=x^2` gives

\[
 p'(t)=\frac{xF'(x)-F(x)}{2x^3},
\]

\[
 p''(t)=\frac{x^2F''(x)-3xF'(x)+3F(x)}{4x^5},
\]

and hence

\[
 \boxed{
 p p''-2p'^2=\frac{\mathfrak T_3(x)}{4x^6},
 }
\]

where

\[
 \boxed{
 \mathfrak T_3(x)=x^2FF''-2x^2(F')^2+xFF'+F^2.
 }
 \tag{L-92002.2}
\]

Thus actual-Xi three-node positivity is equivalent to

\[
 \boxed{\mathfrak T_3(x)\ge0\qquad(x>1/2).}
 \tag{L-92002.3}
\]

There is also an entire-function form. Define

\[
 \Phi(t)=\Xi(\sqrt t).
\]

Then `p=2 Phi'/Phi` and

\[
 \boxed{
 p p''-2p'^2
 =4\frac{\Phi\Phi'\Phi'''-2\Phi(\Phi'')^2+(\Phi')^2\Phi''}{\Phi^3}.
 }
 \tag{L-92002.4}
\]

All derivatives in (L-92002.2) are safely Eulerian. For
`s=1/2+x>1`,

\[
\begin{aligned}
 F={}&\frac1s+\frac1{s-1}-\frac12\log\pi
 +\frac12\psi(s/2)-\sum_{n\ge2}\Lambda(n)n^{-s},\\
 F'={}&-\frac1{s^2}-\frac1{(s-1)^2}+\frac14\psi_1(s/2)
 +\sum_{n\ge2}\Lambda(n)\log n\,n^{-s},\\
 F''={}&\frac2{s^3}+\frac2{(s-1)^3}+\frac18\psi_2(s/2)
 -\sum_{n\ge2}\Lambda(n)(\log n)^2n^{-s}.
\end{aligned}
\]

Every prime series converges absolutely. The remaining third-order theorem is
therefore a one-variable safe-axis sign, not a matrix search.

If (L-92002.3) holds, one-, two-, and three-node principal minors are all
nonnegative, so

\[
 \left(\frac{F(x_i)+F(x_j)}{x_i+x_j}\right)_{i,j=1}^3\succeq0.
\]

Conversely, positivity for every three-node packet implies (L-92002.3) by
coalescence because `(tp)''<0`.

## Exact boundary

```text
three-node matrices -> one scalar curvature       EXACT
one scalar curvature -> all three-node matrices   EXACT
safe prime/gamma formula                          EXACT
actual-Xi curvature sign                          OPEN
all-order positivity                              OPEN / RH-EQUIVALENT
Riemann Hypothesis                                UNPROVED
```
