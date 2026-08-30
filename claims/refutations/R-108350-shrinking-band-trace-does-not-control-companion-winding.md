# R-108350 — Shrinking physical-band trace does not control direct-companion winding

Claim ID: `R-108350`  
Status: **PROVED EXACT HARDY/BLASCHKE FIREWALL**  
Created: 2026-08-31  
Depends on: `T-108320`, `R-108330`; the all-inner finite-band theorem on PR #765  
RH status: **not assumed**

The actual-Xi theorem on PR #765 proves that a finite shallow companion packet has negligible mass in an accepted Fourier band whose absolute width is

\[
\Delta_X\asymp \frac{e^{-X}}X.
\]

That theorem is useful for a localized source trace. It cannot, even together with a geographic companion count of order \(R\log R\), control the winding in `T-108320`.

## 1. One exact Blaschke factor

For \(a\in\mathbb R\), \(y>0\), put

\[
b_{a,y}(z)=\frac{z-a-iy}{z-a+iy}.
\]

The one-dimensional model space \(K_{b_{a,y}}\) has the normalized Takenaka kernel

\[
\phi_{a,y}(x)=\sqrt{\frac y\pi}\frac1{x-a+iy}.
\]

In the unitary half-line Fourier convention its time-side modulus is

\[
\big|\widehat\phi_{a,y}(t)\big|^2
=2y e^{-2yt}\mathbf1_{t>0}.
\]

Hence for every band \(I=[X,X+\Delta]\),

\[
\boxed{
\int_I|\widehat\phi_{a,y}(t)|^2dt
=e^{-2yX}\bigl(1-e^{-2y\Delta}\bigr)
\le 2y\Delta e^{-2yX}.
}
\tag{R-108350.1}
\]

The bound is independent of the horizontal location \(a\). On the other hand,

\[
\boxed{\operatorname{wind} b_{a,y}=1}
\tag{R-108350.2}
\]

up to the fixed orientation convention.

Thus one exact winding unit may carry arbitrarily small mass in a shrinking or translated physical band.

## 2. Geographic packets at the actual-Xi count scale

Take distinct \(a_1,\ldots,a_n\in[-R,R]\), all at height \(y=1\), and let

\[
B_n=\prod_{j=1}^n b_{a_j,1}.
\]

The Takenaka decomposition and (R-108350.1) give

\[
\boxed{
\operatorname{tr}_{K_{B_n}}\Pi_{[X,X+\Delta]}
=n e^{-2X}(1-e^{-2\Delta})
\le 2n\Delta e^{-2X},
}
\tag{R-108350.3}
\]

while

\[
\boxed{\operatorname{wind}B_n=n.}
\tag{R-108350.4}
\]

Choose

\[
R=e^X,
\qquad
n=\lfloor R\log R\rfloor,
\qquad
\Delta=\frac C{R\log R}.
\]

Then the packet has precisely the geographic size allowed by an \(O(R\log R)\) zero-count theorem, but

\[
\operatorname{tr}_{K_{B_n}}\Pi_{[X,X+\Delta]}
=O_C(R^{-2}),
\qquad
\operatorname{wind}B_n\asymp R\log R.
\tag{R-108350.5}
\]

The ratio between winding and accepted-band trace is unbounded by more than any fixed power of the geographic scale.

## 3. Literal real entire companion realization

Let

\[
E_+(z)=\prod_{j=1}^n(z-a_j-iy_j),
\qquad
E_-(z)=\overline{E_+(\overline z)}.
\]

For any \(\varepsilon>0\), define

\[
G=\frac{E_++E_-}{2},
\qquad
F=\frac{E_+-E_-}{2i\varepsilon}.
\]

Both \(F\) and \(G\) are real polynomials on the real axis and

\[
\boxed{E_+=G+i\varepsilon F.}
\tag{R-108350.6}
\]

Therefore the counterexample belongs to the literal entire-companion class used by the direct endpoint programme; it is not merely an abstract inner-function example.

## 4. Binding consequence

No theorem of the following form can hold uniformly:

```text
geographic companion count O(R log R)
AND shallow companion heights
AND accepted absolute band width O(1/(R log R))
AND o(1) normalized all-inner/source band trace
    -> positive lower bound for direct-companion winding.
```

To use the PR #765 band theorem for `XI31WIND108320`, one would additionally need a **lower capture theorem** forcing every relevant winding unit to deposit definite mass in the accepted band. Equations (R-108350.3)--(R-108350.6) show that such a theorem is false in the entire-companion/inner class and would have to be a new, genuinely Xi-specific global arithmetic result.

## Scope

This firewall does not refute an argument-principle or Levinson theorem for the literal Xi companion. It proves that the newest narrow-band theorem and companion-count estimate do not pay that winding. The direct branch should no longer advertise source softness or shrinking bandwidth as a near-complete route to ninety percent.