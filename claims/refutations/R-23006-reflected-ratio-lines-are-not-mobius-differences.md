# R-23006 — Reflected ratio lines are not Möbius-difference lines

Claim ID: `R-23006`  
Title: The reflected Hermitian packet has same-sign factor reallocations, so its balanced ratio cones do not carry the difference factors required by the Brion line-annihilation proposal  
Status: **PROPOSED EXACT REFUTATION OF `L-23602` AS A GENERAL THEOREM**  
Authoring agent: `gpt56-pro-09-o`  
Created: 2026-08-07  
Frozen target: PR #242 at `1d5c9226db03022a11f92b2f84395da4eec4cb68`  
Dependencies: the reflected coefficient identity of PR #226 `L-9516`; the local two-frequency correction of PR #241 `L-9518`; elementary Dirichlet convolution  
Scope: the claimed universal BLINE/line-cone vanishing mechanism; no assertion that every possible Brion repair fails

## 1. The claimed cancellation

`L-23602` asserts that every positive-dimensional balanced tangent cone contains
one source-complete line whose cone denominator

\[
1-e^{-\langle z,v\rangle}
\tag{R-23006.1}
\]

is canceled by an actual Möbius difference factor

\[
I-e^{-\langle z,v\rangle}.
\tag{R-23006.2}
\]

In particular, Section 6 treats directions tangent to fixed total product as
zero-mass reflected Möbius lines.  This is false for the basic reflected
factor-reallocation direction.

## 2. Exact double-inverse coefficient

For real `t`, the inverse of the product

\[
\zeta(s+it)\zeta(s-it)
\]

has coefficient

\[
B_\times(n,t)
=
\sum_{de=n}\mu(d)\mu(e)(d/e)^{-it}.
\tag{R-23006.3}

If `n` is squarefree with prime set `P(n)`, every prime is assigned to exactly
one of `d,e`, and the coefficient factors as

\[
\boxed{
B_\times(n,t)
=(-1)^{\omega(n)}
\prod_{p\mid n}
\left(p^{-it}+p^{it}\right).}
\tag{R-23006.4}

The two assignments of one prime have the **same** Möbius sign.  The source
factor is a sum, not a difference.

For one prime,

\[
B_\times(p,t)=-(p^{-it}+p^{it}).
\tag{R-23006.5}

For two distinct primes,

\[
\begin{aligned}
B_\times(pq,t)
&=(p^{-it}+p^{it})(q^{-it}+q^{it})\\
&=(pq)^{-it}+(p/q)^{-it}+(q/p)^{-it}+(pq)^{it}.
\end{aligned}
\tag{R-23006.6}

The two balanced allocations `(d,e)=(p,q)` and `(q,p)` occur with the same
positive sign.

## 3. Reflected Selberg cross term has the same obstruction

The exact Hermitian subtraction of `L-9516` produces

\[
2\Lambda_t*\Lambda_{-t}.
\]

At `n=pq`, `p\ne q`, its balanced part is

\[
\boxed{
2\log p\log q
\left[(p/q)^{-it}+(q/p)^{-it}\right]
=4\log p\log q\cos(t\log(p/q)).}
\tag{R-23006.7}

Again the factor-reassignment directions have the same sign.  The reflected
Hermitian square reinforces rather than annihilates this ratio pair.

## 4. Exact Laurent-polynomial divisibility failure

Let `X` encode motion in the factor-ratio direction.  The two balanced
orientations give the Laurent numerator

\[
N(X)=X+X^{-1}.
\tag{R-23006.8}

A geometric cone in that exchange direction has denominator, up to a monomial,

\[
1-X^2.
\tag{R-23006.9}

Multiplying (R-23006.8) by `X` gives

\[
X N(X)=X^2+1.
\]

This polynomial is not divisible by `1-X^2`; evaluating at `X=1` gives

\[
XN(X)|_{X=1}=2\ne0.
\tag{R-23006.10}

Equivalently, the source contains no factor `1-X^2` or `1-X` along the reflected
ratio line.

High-order null moments act in the total-product/pole-model coordinate.  They do
not manufacture a missing ratio-difference factor in (R-23006.8).

## 5. Two-slot Möbius control

The same obstruction is visible before introducing phases.  Assign one prime
`p` to one of two Möbius slots:

```text
(p,1)  coefficient mu(p)mu(1) = -1,
(1,p)  coefficient mu(1)mu(p) = -1.
```

Both points have the same total product.  On a test depending only on that
product their signed valuation is

\[
-2F(p),
\]

not zero.  The exchange direction changes two slot coordinates and preserves
Möbius parity.  It is not a one-coordinate toggle.

This is precisely the balanced prime-replacement geometry already isolated in
PR #234: replacing one prime by another preserves parity, whereas a single
prime insertion/removal exits a narrow shell.

## 6. Consequence for `L-23602/L-23603`

The proposed clause

```text
positive-dimensional face tangent to fixed total product
    -> zero reflected Möbius valuation
```

is not an algebraic consequence of the reflected packet.  The fundamental
factor-ratio line (R-23006.7) is a source-complete same-sign pair and has no
matching difference numerator.

Therefore:

1. `L-23602.9` is false as a universal line-cone theorem;
2. the assertion that every nonvertex cone vanishes in `L-23603.6` is not
   established;
3. the reduction to at most ten vertex denominators does not follow;
4. `BLINE` fails unless an additional source identity cancels every reflected
   same-sign ratio line.

The high-order Euler theorem remains valid for complete one-variable lattice
rows.  It gives a small remainder, not exact vanishing of the balanced ratio
source.

## 7. Independent localization defect

The frozen `L-23602.2` also uses the one-frequency global vertical identity of
`L-9516` as though it were a physical block indexed by `J`.  Its left side has
no `J`.  PR #241 `L-9518` proves that a unit block requires two independent
frequencies and the local kernel

\[
\Phi_{J,\alpha}(t-s)
=\int_J^{J+1}e^{2\alpha x}e^{i(t-s)x}dx.
\]

Thus even a repaired Brion programme must first be rebuilt in the two-frequency
normal orientation.  Aggregate one-frequency positivity cannot be assigned to
individual packet cones.

## 8. Lattice-coordinate warning

The variables `y_i=log n_i` do not form a finite affine lattice.  Already
`log2/log3` is irrational, since a rational relation would imply
`2^a=3^b`.  Hence the actual log-integer source is not directly a rational
lattice polytope with primitive edge denominators as in `L-23603.7`.

One may lift to the full prime-exponent lattice, but then the dimension and
threshold-face family grow with the prime set.  The bounds `BRANK<=10`, at most
ten unmatched denominators, and `BSHORT` must be reproved in that lifted source;
they do not follow from the cumulative real-log prefix change.

## 9. Correct status of PR #242

```text
L-23601 threshold-polytope schema         GAP/BLOCKED
L-23602 universal line-cone annihilation  REJECTED
L-23603 vertex-only balanced contraction  REJECTED AS DERIVED
L-23604 conditional Mertens composition   CONDITIONAL ONLY
T-23601 full RH proof                     GAP/BLOCKED
RH                                        UNPROVED
```

A viable repair must retain the same-sign ratio pairs in a coupled
(two-frequency) reflected packet and prove a source-specific inequality for
them.  They cannot be deleted by calling them Möbius toggle lines.

The exact dyadic/`2/3` scalar export of `L-23008/T-23003` remains available to
any corrected source-specific proof.
