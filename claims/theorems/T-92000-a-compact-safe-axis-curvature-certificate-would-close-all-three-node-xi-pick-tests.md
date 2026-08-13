# T-92000 — A compact safe-axis curvature certificate would close all three-node Xi Pick tests

Claim ID: `T-92000`  
Status: **CONDITIONAL UNCONDITIONAL-ORDER-THREE PROPOSAL / COMPACT SIGN OPEN**  
Created: 2026-08-13  
Depends on: `L-92000`--`L-92003`; `L-91904/L-91905`  
RH status: **unproved**

## 1. Curvature target

Let

\[
 F(x)=\frac{\xi'}{\xi}\left(\frac12+x\right)
 \qquad(x>1/2)
\]

and define

\[
 \boxed{
 \mathfrak T_3(x)
 =x^2F F''-2x^2(F')^2+xFF'+F^2.
 }
 \tag{T-92000.1}
\]

`L-92002` proves that this is exactly the reciprocal-curvature numerator for
the order-three infinitesimal safe Pick kernel.

## 2. Compact Curvature Certificate (`CCC3`)

> Construct an effective `X_0>1/2` and a directed proof that
> 
> \[
> \boxed{
> \mathfrak T_3(x)\ge0
> \qquad(1/2<x\le X_0).
> }
> \tag{T-92000.2}
> \]
> 
> The evaluation must use the completed safe formula and rigorous enclosures
> for the prime-power and polygamma tails.  A floating-point mesh is not a
> proof.

`L-92003` supplies

\[
 \mathfrak T_3(x)>0
 \qquad(x\ge X_0)
\]

once the effective asymptotic threshold is chosen.  Hence `CCC3` implies

\[
 \mathfrak T_3(x)\ge0
 \qquad(x>1/2).
\]

## 3. Three-node conclusion

Under `CCC3`, put

\[
 p(t)=\frac{F(\sqrt t)}{\sqrt t}.
\]

Then:

1. `L-91905` gives `p>0`, `p` decreasing, and `tp` increasing;
2. `L-92001` gives strict concavity of `tp`;
3. `CCC3` and `L-92002` give concavity of `1/p`;
4. `L-92000` gives every principal minor through order three.

Therefore

\[
 \boxed{
 \left(
 \frac{F(x_i)+F(x_j)}{x_i+x_j}
 \right)_{i,j=1}^N
 \succeq0
 \qquad(N\le3,\ x_i>1/2).
 }
 \tag{T-92000.3}
\]

This would be an unconditional theorem about the actual Xi function.  It does
not imply RH, because `R-91902/R-92000` show that order three is only the first
RH-sensitive interpolation level, not the complete hierarchy.

## 4. Arithmetic form of the compact sign

For `s=1/2+x>1`, all inputs are absolutely convergent:

\[
\begin{aligned}
 F={}&\frac1s+\frac1{s-1}-\frac12\log\pi
 +\frac12\psi(s/2)-P_0(s),\\
 F'={}&-\frac1{s^2}-\frac1{(s-1)^2}
 +\frac14\psi_1(s/2)+P_1(s),\\
 F''={}&\frac2{s^3}+\frac2{(s-1)^3}
 +\frac18\psi_2(s/2)-P_2(s),
\end{aligned}
\]

where

\[
 P_k(s)=\sum_{n\ge2}\Lambda(n)(\log n)^k n^{-s}.
\]

A proof packet may use:

```text
near s=1:
    pole-cancelled eta or completed-xi Taylor coordinates;

intermediate compact interval:
    directed Euler--Maclaurin / interval arithmetic;

large s:
    L-92003 effective Stirling and prime-tail bounds.
```

## 5. After order three

Once `CCC3` is closed, the first open finite order becomes four.  The next
object should not be attacked by raw determinants.  The correct continuation
is to identify the general Cauchy--Loewner determinant with the continued
fraction / finite-string data of the scalar function `p(t)`.

At order three the entire matrix problem has already collapsed to one scalar
reciprocal curvature.  This is evidence that the all-order problem should be
organized by successive Stieltjes-string coefficients rather than by unrelated
finite matrices.

## 6. Exact boundary

```text
large safe-axis curvature tail             PROPOSED CLOSED
companion tp curvature                     PROPOSED CLOSED GLOBALLY
compact reciprocal-curvature sign          OPEN / DIRECTED ONE-DIMENSIONAL
all actual-Xi packets of size <=3           CONDITIONAL ON COMPACT SIGN
all finite packet sizes                     OPEN / RH-EQUIVALENT
Riemann Hypothesis                          UNPROVED
```
