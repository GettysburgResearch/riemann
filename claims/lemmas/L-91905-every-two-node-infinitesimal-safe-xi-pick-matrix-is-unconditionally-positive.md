# L-91905 — Every two-node infinitesimal safe Xi Pick matrix is unconditionally positive

Claim ID: `L-91905`  
Status: **PROPOSED COMPLETE UNCONDITIONAL ORDER-TWO THEOREM — REVIEW REQUIRED**  
Created: 2026-08-13  
Depends on: the centered Hadamard product for Xi; the rigorously known fact that every nontrivial zeta zero has `|Im rho|>1`  
RH status: **unproved**

## 1. Centered notation

Put

\[
 \Xi(z)=\xi\left(\frac12+z\right),
 \qquad
 F(x)=\frac{\Xi'(x)}{\Xi(x)}
 \qquad(x>1/2).
 \tag{L-91905.1}

`L-91904` asks for positivity of the kernel

\[
 \mathscr H(x,y)=\frac{F(x)+F(y)}{x+y}
 \tag{L-91905.2}

on every finite safe-real packet.  This note closes all packets of size at
most two unconditionally.

## 2. Orbitwise Hadamard expansion

The centered Xi function is even, real entire and of order one.  Grouping its
zeros by the symmetries

\[
 \lambda,\ -\lambda,\ \overline\lambda,\ -\overline\lambda
\]

removes the genus-one exponentials and gives a locally normally convergent
expansion for `F(x)/x`.

### Critical-line orbit

For a zero `lambda=i b`, `b>1`, of multiplicity `m`, the orbit contributes

\[
 \boxed{
 G_{0,b}(x)=\frac{2m}{x^2+b^2}
 }
 \tag{L-91905.3}

to `F(x)/x`.

### Off-line orbit

Choose one representative

\[
 \lambda=a+ib,
 \qquad
 0<a<1/2,
 \qquad
 b>1.
\]

Put

\[
 t=x^2,
 \qquad
 A=a^2-b^2<0,
 \qquad
 B=2ab,
 \qquad
 U=t-A=t-a^2+b^2.
\]

The complete quadruple contributes

\[
\boxed{
\begin{aligned}
 G_{a,b}(x)
 &:=2m\left[
  \frac1{x^2-\lambda^2}
  +\frac1{x^2-\overline\lambda^2}
 \right]\\
 &=\frac{4mU}{U^2+B^2}>0
\end{aligned}}
 \tag{L-91905.4
}

again to `F(x)/x`.

## 3. Two opposite monotonicities

For the critical-line contribution,

\[
 G_{0,b}(x)
 \quad\text{is strictly decreasing,}
\]

while

\[
 x^2G_{0,b}(x)
 \quad\text{is strictly increasing.}
\]

For an off-line orbit, differentiation with respect to `t=x^2` gives

\[
 \boxed{
 \frac d{dt}G_{a,b}
 =\frac{4m(B^2-U^2)}{(U^2+B^2)^2}<0.
 }
 \tag{L-91905.5}

Indeed

\[
 U>b^2>b>|B|
\]

because `x>|a|`, `b>1` and `2|a|<1`.

Likewise

\[
 \boxed{
 \frac d{dt}\bigl[tG_{a,b}\bigr]
 =\frac{4m\left[-AU^2+B^2(2t-A)\right]}
       {(U^2+B^2)^2}>0,
 }
 \tag{L-91905.6}

since `A<0` and `2t-A>0`.

The grouped series and its first derivative converge normally on every
`x>=x_0>1/2`, because the zero count gives summable `|lambda|^(-2)` tails.
Summing the orbit inequalities yields

\[
 \boxed{
 \frac{F(x)}x>0
 \text{ and is strictly decreasing on }(1/2,\infty),
 }
 \tag{L-91905.7}

and

\[
 \boxed{
 xF(x)>0
 \text{ and is strictly increasing on }(1/2,\infty).
 }
 \tag{L-91905.8}

No RH assumption was used: off-line quadruples satisfy the same two
monotonicities because their ordinates are larger than one.

## 4. Exact two-point determinant

Take

\[
 1/2<x<y,
 \qquad
 r=\frac{F(y)}{F(x)},
 \qquad
 \tau=\frac yx>1.
\]

Equations (L-91905.7)--(L-91905.8) give

\[
 \boxed{
 \tau^{-1}<r<\tau.
 }
 \tag{L-91905.9}

The two-node Carathéodory matrix is

\[
 H_{x,y}
 =\begin{pmatrix}
  F(x)/x&(F(x)+F(y))/(x+y)\\
  (F(x)+F(y))/(x+y)&F(y)/y
 \end{pmatrix}.
 \tag{L-91905.10}

Its determinant is nonnegative exactly when

\[
 \tau+\tau^{-1}
 \ge r+r^{-1}.
 \tag{L-91905.11}

Since the convex function `z+z^(-1)` has the same value at the two endpoints
of `[tau^(-1),tau]`, (L-91905.9) gives strict inequality.  Therefore

\[
 \boxed{
 H_{x,y}\succ0
 \qquad(x\ne y).
 }
 \tag{L-91905.12}

The one-node diagonal is positive by (L-91905.7).

## 5. Consequence for finite RH witnesses

For the infinitesimal safe criterion of `L-91904`,

\[
 \boxed{
 \mathcal H[\mathbf q]\succeq0
 \qquad\text{whenever }|\mathbf q|\le2.
 }
 \tag{L-91905.13}

Thus any negative safe-real witness to false RH in the **linearized** criterion
must use at least three distinct interpolation nodes.

This is compatible with the possibility of off-line zeros: a high-ordinate
quadruple has the correct order-two variation but can still violate higher
Carathéodory positivity.

## 6. Relation to Claude's rank--trace geometry

Claude's theorem obtains a proportion from first and second global spectral
moments.  The present result is another exact order-two firewall: one- and
two-node safe infinitesimal tests cannot see an off-line zeta zero at its
actual large ordinate.  The first genuinely RH-sensitive interpolation
complexity is at least order three.

## 7. Review joints

Independent review should check:

1. the grouped centered Hadamard product and absence of an exponential term;
2. normal convergence after differentiating the orbit series;
3. the use of the external verified zero-height bound only through `|b|>1`;
4. multiplicity and the `a=0` orbit convention;
5. the determinant equivalence (L-91905.11).

## 8. Exact boundary

```text
orbitwise positivity                              PROPOSED COMPLETE
F(x)/x strictly decreasing                        PROPOSED COMPLETE
xF(x) strictly increasing                         PROPOSED COMPLETE
all one- and two-node infinitesimal Pick matrices POSITIVE UNCONDITIONALLY
first possible negative witness size              AT LEAST THREE
all N-node positivity                             OPEN / RH-EQUIVALENT
Riemann Hypothesis                                UNPROVED
```
