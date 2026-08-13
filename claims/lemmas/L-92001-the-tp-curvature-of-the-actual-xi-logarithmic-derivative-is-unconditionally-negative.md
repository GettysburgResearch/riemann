# L-92001 — The `t p(t)` curvature of the actual Xi logarithmic derivative is unconditionally negative

Claim ID: `L-92001`  
Status: **PROPOSED COMPLETE UNCONDITIONAL ORBITWISE THEOREM — REVIEW REQUIRED**  
Created: 2026-08-13  
Depends on: `L-91905`; the rigorous source lock that every nontrivial zeta zero has ordinate larger than one in modulus  
RH status: **unproved**

## 1. Setup

Put

\[
 \Xi(z)=\xi\left(\frac12+z\right),
 \qquad
 F(x)=\frac{\Xi'(x)}{\Xi(x)},
 \qquad
 p(t)=\frac{F(\sqrt t)}{\sqrt t}.
 \tag{L-92001.1}
\]

We work on

\[
 t>\frac14,
\]

which corresponds to the safe half-plane `Re(s)>1`.

The centered zero multiset is invariant under

\[
 \lambda\mapsto-\lambda,
 \qquad
 \lambda\mapsto\overline\lambda.
\]

Group the logarithmic derivative by these orbits.

## 2. Critical-line orbit

A critical-line orbit `lambda=ib`, of multiplicity `m`, contributes

\[
 p_{0,b}(t)=\frac{2m}{t+b^2}.
 \tag{L-92001.2}
\]

Therefore

\[
 \boxed{
 \frac{d^2}{dt^2}\bigl[t p_{0,b}(t)\bigr]
 =-\frac{4mb^2}{(t+b^2)^3}<0.
 }
 \tag{L-92001.3}
\]

## 3. Off-line orbit

Take one representative

\[
 \lambda=a+ib,
 \qquad
 0<|a|<\frac12.
\]

Put

\[
 c=b^2-a^2,
 \qquad
 B=2ab,
 \qquad
 U=t+c.
 \tag{L-92001.4}
\]

The complete quadruple contributes

\[
 \boxed{
 p_{a,b}(t)
 =\frac{4mU}{U^2+B^2}.
 }
 \tag{L-92001.5}
\]

Direct differentiation gives

\[
\boxed{
\begin{aligned}
 \frac{d^2}{dt^2}\bigl[t p_{a,b}(t)\bigr]
 =-8m\frac{
 cU^3+3B^2U^2-3cB^2U-B^4
 }{(U^2+B^2)^3}.
\end{aligned}
}
\tag{L-92001.6}
\]

Introduce

\[
 q=\frac cU\in(0,1),
 \qquad
 r^2=\frac{B^2}{U^2}.
\]

The numerator divided by `U^4` is

\[
 \boxed{
 q(1-3r^2)+r^2(3-r^2).
 }
 \tag{L-92001.7}
\]

Because `t>1/4` and `a^2<1/4`,

\[
 U=t+b^2-a^2>b^2.
\]

Hence

\[
 |r|<\frac{2|a|}{|b|}<\frac1{|b|}.
 \tag{L-92001.8}
\]

For `|b|>sqrt(3)`, one has `r^2<1/3`, so both terms in
(L-92001.7) are strictly positive.  Therefore every off-line orbit with
ordinate larger than `sqrt(3)` has strictly negative `tp` curvature.

All nontrivial zeta zeros have ordinates far larger than this threshold.  The
external verified-height input used on the parent branch supplies the much
stronger statement `|b|>14`.

## 4. Summation over all zero orbits

On every compact interval `t>=t_0>1/4`, the orbit series and its first two
`t`-derivatives converge normally.  Indeed a critical orbit contributes
`O(m b^{-2})` to `p`, `O(m b^{-4})` to `p'`, and `O(m b^{-6})` to `p''`;
the off-line formula has the same bounds uniformly for `|a|<1/2`, and the
Riemann--von Mangoldt count makes the differentiated tails summable.

We may therefore sum (L-92001.3) and (L-92001.6) term by term.  Every summand
is strictly negative, giving

\[
 \boxed{
 \frac{d^2}{dt^2}
 \left[t\frac{F(\sqrt t)}{\sqrt t}\right]<0
 \qquad(t>1/4).
 }
 \tag{L-92001.9}

Thus `t p(t)` is strictly concave on the entire safe axis, without assuming
RH.

## 5. Equivalent `x`-derivative form

Since `t=x^2`,

\[
 \boxed{
 (tp)''(t)
 =\frac{x^2F''(x)+xF'(x)-F(x)}{4x^3}.
 }
 \tag{L-92001.10}

Consequently

\[
 \boxed{
 x^2F''(x)+xF'(x)-F(x)<0
 \qquad(x>1/2).
 }
 \tag{L-92001.11}

## 6. Significance

`L-92000` shows that a three-node infinitesimal Pick determinant is the product
of the second divided differences of `1/p` and `tp`.  The present theorem fixes
the sign of the second factor once and for all.  Therefore the entire actual-Xi
order-three problem is equivalent to only one scalar inequality:

\[
 \left(\frac1p\right)''\le0.
\]

The first two interpolation orders used two monotonicities.  The third order
uses one additional curvature, and no matrix search remains.

## 7. Review joints

1. the grouped Hadamard expansion and multiplicity convention;
2. the algebra in (L-92001.6)--(L-92001.7);
3. the implication `U>b^2`;
4. the differentiated normal convergence;
5. the external zero-height source lock.

## 8. Exact boundary

```text
critical-orbit tp curvature                 STRICTLY NEGATIVE
high off-line-orbit tp curvature            STRICTLY NEGATIVE
actual-Xi tp concavity                      PROPOSED UNCONDITIONAL
reciprocal curvature                        OPEN / ORDER-THREE GATE
three-node infinitesimal Xi positivity      REDUCED TO ONE SCALAR SIGN
Riemann Hypothesis                          UNPROVED
```
