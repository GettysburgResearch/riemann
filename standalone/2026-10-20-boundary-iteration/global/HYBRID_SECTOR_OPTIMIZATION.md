# Exact all-ratio optimization of the hybrid smooth sectors

20 October 2026. **Proposed source-dependent consequence.** This is an
algebraic optimization of the independently reviewed
[hybrid angular mean](../type_i/HYBRID_ANGULAR_MEAN.md), SHA256
`dcf9f71ae9d828f71741ae255be7d41323b9ea3ca7ab184b1c9fbeb31de82ae8`.
It uses no additional analytic theorem and no common zero-free premise.
The theta and large-sieve inputs of that note remain dependencies.

## Statement and scope

Use exactly the free-column cubic Gauss form, fixed radial weights,
common bounded outer coefficients, and periodized smooth angular bump
of that note. Put `A=X^a`, `B=X^(1-a)`, with a fixed `0<a<=1`.
The zero-angular mode is subtracted with its exact Fourier coefficient.
Define

\[
g(a)=
\begin{cases}
\displaystyle\frac{5a-3+\sqrt{9+42a-47a^2}}{24},
                                      &0<a\le5/9,\\[2mm]
3a/10,                                &5/9\le a\le5/7,\\[1mm]
(1+a)/8,                              &5/7\le a\le1.
\end{cases}
\tag{G1}
\]

For each fixed `0<eta<g(a)`, at all widths
`Delta>=X^(-g(a)+eta)`, the smooth discrepancy is smaller than
`X Delta` by a fixed power of `X`. The displacement and all subpower
allowances are chosen in terms of `a,eta`; no uniform constant as
`a` tends to zero is claimed. There is no positive shrinking-width
claim at `a=0`.

This is the optimum of the three displayed fixed-displacement
constraints below, not an assertion of optimality among other
analytic methods. The inner variable remains a free smooth column.
This does not give a prime asymptotic, a sharp-sector estimate, a
smaller zero-free boundary, or RH.

## The three constraints

Write `d` for the positive contour displacement, with `0<d<1/4`.
The first and third error terms in H7 and H18 give respectively

\[
 f_1(a,d)=a(1/2-d),\qquad
 f_3(a,d)=\frac{3a+3d(1-3a)}{10-12d}.
\tag{G2}
\]

The middle term gives

\[
 f_2(a,d)=
 \begin{cases}
 \displaystyle\frac{1+a+2d(1-3a)}{8(1-d)},&0<d\le1/6,\\[2mm]
 \displaystyle\frac{1-2d}{4(1-d)},&1/6\le d<1/4.
 \end{cases}
\tag{G3}
\]

The two expressions agree at `d=1/6`, where `f_2=1/5`.
The transition uses the enlarged row normalization H16, including
its essential positive row subpower in Abel summation. It does not
extend H1 past its proved range without that change.

For a width exponent strictly below `min(f_1,f_2,f_3)`, comparison
of each Fourier-summed error to `X Delta` gives a power saving.
The remaining argument computes its supremum over `0<d<1/4`.

## The first branch and the normalization transition

For `0<a<=5/9`, the first constraint decreases with `d` and the
third is nondecreasing, because

\[
 \frac{\partial f_3}{\partial d}
                      =\frac{30-54a}{(10-12d)^2}\ge0.
\tag{G4}
\]

At zero their difference is `a/5>0`; at `d=1/5` it is nonpositive.
They therefore cross at the smaller root of

\[
 12ad^2-(7a+3)d+2a=0,
\qquad
 d(a)=\frac{7a+3-\sqrt{9+42a-47a^2}}{24a}.
\tag{G5}
\]

This root lies in `(0,1/5]`. It is at or below `1/6` exactly when
`a<=3/7`. Thus the first branch genuinely passes through both
normalizations; its validity is not inferred from the enlarged
one at small `a`.

The middle constraint stays above the crossing. In the enlarged
range `d>=1/6`,

\[
 \frac{f_2}{f_1}=\frac{1}{2a(1-d)}>1
                  \quad(0<a\le5/9).
\tag{G6}
\]

In the original range, the equality `f_1=f_3` gives
`a=3d/(2-7d+12d^2)`. Substituting this into the numerator
`8(1-d)(f_2-f_1)` gives

\[
 \frac{2(1-2d)(1-4d)}{2-7d+12d^2}>0
                        \quad(0<d\le1/6).
\tag{G7}
\]

The denominator is positive on this interval. Hence the crossing
attains the upper bound obtained by discarding the middle constraint.
Its value `a(1/2-d(a))` is precisely the first branch of G1.
For `a=5/9`, the third constraint is constant; the displayed crossing
at `d=1/5` remains a valid maximizing choice.

## The two remaining branches

For `5/9<=a<=5/7`, the third constraint is nonincreasing in `d`.
It is therefore at most its zero-displacement value `3a/10`.
At zero the other two constraints are no smaller:
`a/2>=3a/10` and `(1+a)/8>=3a/10`. A sufficiently small fixed
positive displacement attains any exponent below `3a/10`.

For `5/7<=a<=1`, the middle constraint decreases throughout both
displacement ranges. In the first range its derivative has the
sign of `3-5a`, which is negative here; in the second range its
derivative is negative. The two branches meet continuously.
Thus it is at most `(1+a)/8`, its zero-displacement value. At zero
the first and third constraints are no smaller. Again every
strictly smaller exponent follows from a fixed positive displacement.
These are limits of proved positive-displacement inequalities,
not a claim of a bound directly on the half-line.

## Checks and comparison

The branches agree at their endpoints:

\[
g(1/2)=\frac{\sqrt{73}-1}{48},\quad
g(5/9)=\frac16,\quad g(5/7)=\frac3{14},\quad g(1)=\frac14.
\tag{G8}
\]

As `a` tends to zero, `d(a)` is asymptotic to `2a/3` and
`g(a)=a/2-2a^2/3+O(a^3)`. These expansions are consistency checks,
not uniform endpoint theorems. G1 strengthens the simple all-ratio
bound H10 for `0<a<5/9`, and agrees with it thereafter. In particular
it includes the frozen balanced optimum without changing that proof.
