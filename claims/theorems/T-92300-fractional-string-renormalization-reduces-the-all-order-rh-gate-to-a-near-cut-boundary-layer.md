# T-92300 — Fractional-string renormalization reduces the all-order RH gate to a near-cut boundary layer

Claim ID: `T-92300`  
Status: **FULL CONDITIONAL RESEARCH PROPOSAL / NEAR-CUT COMPLETION OPEN**  
Created: 2026-08-14  
Depends on: `L-92100`, `L-92204`, `L-92300`--`L-92302`, `R-92300`  
RH status: **unproved**

## 1. Universal high-axis object

The renormalised safe Xi impedance is

\[
 \widehat Z_x(u)
 =\frac{\ell_x}{2x}Z(x^2u),
 \qquad
 \ell_x=\log\frac{x}{2\pi}.
\]

`L-92300` gives

\[
 \widehat Z_x(u)
 =u^{\alpha_x}
  \left[1+O_K(\ell_x^{-2})+O_K((x\ell_x)^{-1})\right],
 \qquad
 \alpha_x=\frac12-\frac1{2\ell_x},
\]

locally uniformly off the negative-real cut.

The model `u^(alpha_x)` is the Dirichlet-to-Neumann impedance of an explicit
positive homogeneous Krein string.

## 2. Growing finite-order passivity

`L-92302` proposes an effective `c>0` such that

\[
 Z\text{ is matrix monotone of order }n
 \text{ on }[x^2,\infty)
\]

whenever

\[
 n\le c\sqrt{\frac{\log x}{\log\log x}}.
\]

Thus the number of certified Loewner levels tends to infinity unconditionally
on the high safe axis.

## 3. Where a possible off-line pair goes

Let

\[
 \rho=\frac12+a+ib,
 \qquad 0<|a|<\frac12.
\]

In the squared-pole plane, the corresponding pole is

\[
 -s=-(b^2-a^2)-2iab.
\]

At the natural scaling `x=b`,

\[
 -\frac{s}{b^2}
 =-1+O(b^{-2})-2i\frac{a}{b}.
\]

Hence the pole is not seen on compact subsets of the slit plane: it lies in a
boundary layer of angular width `asymp |a|/b` around the negative cut.

The complete-Bernstein/RH problem is therefore exactly the question whether
the positive fractional string can be completed uniformly through this
shrinking near-cut layer.

## 4. Near-Cut Fractional-String Completion (`NCFSC`)

Construct, directly from the prime Clark, paired-eta, compact bridge and gamma
source channels, a positive-string representation

\[
 \boxed{
 \widehat Z_x(u)
 =a_x+b_xu
  +\int_0^\infty\frac{u}{u+s}\,d\nu_x(s),
 \qquad
 \nu_x\ge0,
 }
 \tag{T-92300.1}
\]

with control uniform not merely on compact subsets of the slit plane, but down
to imaginary distance `O(1/x)` from its negative-real cut.

Equivalently, prove the Pick sign

\[
 \Im\widehat Z_x(u)\ge0
 \qquad(\Im u>0)
\]

in the near-cut scaling regime

\[
 u=-r+i\eta,
 \qquad
 r\asymp1,
 \qquad
 0<\eta\lesssim x^{-1}.
\]

The ordinary safe asymptotic and every fixed Loewner order already control the
complement of this layer.

## 5. Consequence

If `NCFSC` holds for all sufficiently large `x`, then no centered Xi zero can
have nonzero real part at a sufficiently large ordinate.  The externally
verified finite range removes the remaining ordinates, and RH follows.

A cofinal version also suffices: for every hypothetical depth-height pair
`(a,b)`, one needs the near-cut Pick sign at `x=b` and imaginary resolution
smaller than `2|a|/b`.

## 6. Why finite-order escalation is not enough

`R-92300` proves that a finite squared-pole system can pass arbitrarily many
Hankel/Loewner orders and fail at the next one.  The same geometric mechanism
places a high shallow off-line pair in a very thin boundary layer.

Therefore the next proof should not merely increase the confluent derivative
order.  It should attack the boundary layer directly, by one of:

```text
pair-adapted nonconfluent safe interpolation;
a source-ordered Krein-string Schur complement;
a near-cut Herglotz estimate with the prime and gamma channels coupled;
a rational microscope whose poles remain in the safe negative half-axis.
```

## 7. Relation to Claude's theorem

Claude's Gabor theorem proves a major unconditional proportion using only two
trace moments and explicitly identifies sparse off-line zeros as invisible to
that bandwidth-one certificate.  The fractional-string limit gives the
all-order safe-axis analogue: every prescribed finite interpolation complexity
converges to a passive universal background, while a sparse off-line pair lives
in a shrinking layer that only a complexity growing with its height can
resolve.

## 8. Exact boundary

```text
universal fractional-string scaling              PROPOSED COMPLETE
fixed and growing finite-order tail positivity    PROPOSED UNCONDITIONAL
arbitrarily delayed finite-order failure          EXACT CONTROL
near-cut positive-string completion               OPEN / RH-EQUIVALENT
Riemann Hypothesis                                UNPROVED
```
