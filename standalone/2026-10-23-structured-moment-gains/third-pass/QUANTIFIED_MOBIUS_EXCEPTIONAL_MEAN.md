# An explicit saving in the Möbius exceptional cubic means

24 October 2026. Proposed source-dependent quantitative refinement.
This note supplies a finite exponent argument for the adapter in
[MOBIUS_EXCEPTIONAL_CUBIC_MEAN.md](MOBIUS_EXCEPTIONAL_CUBIC_MEAN.md). It imports the
ordinary and unrestricted-inner cubic large sieves, the full smooth
Hecke functional equation, and the off-diagonal Gram estimate from its
exact source. It does not assert a new global zero-free boundary.

The source is `openai/math` at
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`,
`preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/build/sections/dual.tex`.
The exact source file has SHA256
`1209fd17cee79f4a21b71d66d3d8b60b210216fa783ec555959d2ebff2fba483`.
The fixed-angular full-sum variant is also supplied by the pinned
source's `sections/angular.tex`, subsection “Smooth duality and the
exceptional moments” (exact source SHA256
`f14a7c1c4f0b19b70d6705c8a2adcb658bfbc77814edb61cd57edb2465f38510`).
Its constants are allowed to depend on the fixed angular order.

## 1. Claim and numerical margins

The Möbius exceptional-mean adapter is valid with the explicit choices

\[
 \boxed{\delta=10^{-9},\qquad \eta=10^{-6}.}             \tag{1}
\]

Thus, with the source's good primary-ideal conventions, a fixed smooth
annular test `W`, and one fixed finite-ray and angular Hecke character
`nu`, put

\[
 A(p,q)=\sum_{(b,e)=1}\mu(b)\nu(b)W(Nb/Y)(Nb)^{iu}
                  \chi_b(vpq^2).
\]

For `Nv,Ne<=Y^delta`, `1+|u|<=Y^.36`, and coprime squarefree `p,q`
whose norm exponents are in the stated `delta` neighborhoods of
`(1,0)` or `(1/3,1/3)`, one has

\[
 \sum_{p,q}|A(p,q)|^2\ll Y^{7/3-\eta}.                 \tag{2}
\]

The constant depends on the fixed tests and character data. This is a
fixed-angular assertion, not uniformity in an unbounded angular order.

The proof uses a deliberately generous intermediate error budget

\[
 \kappa=10^{-4}.
\]

Each exponent inequality below has **at most `kappa` total error**.
This is legitimate for all sufficiently large `Y` because:

1. The original neighborhood widths contribute at most `20 delta` to
   any displayed length or conductor exponent. To see this in the only
   conductor-sensitive step, the conductor is at most `N(vpq)` times a
   fixed constant, and missing Euler factors divide a fixed multiple of
   `ve`. Fixing their local parts changes lengths by at most
   `Y^(2delta+o(1))`; fixing the first-configuration `q` costs at most
   `Y^(delta+o(1))`.
2. Dyadic endpoint ratios are fixed. Their logarithms divided by
   `log Y`, as well as the discrepancy between the product of dyadic
   scales and `Y`, can be made smaller than `delta`. We use the product
   of scales as the exponent base, so `sum a_i=1` exactly. In this base
   the two Möbius-factor exponents are at most `1/2+2delta`.
3. There are three factors and at most 29 repetitions. Every coefficient
   is bounded by a fixed divisor power. All sieve and divisor estimates
   permit an arbitrarily small prescribed power loss. Choose their
   total contribution, including large-value bins, dyadic sums and the
   common Mellin majorant, to be at most `10^-6`. This is a finite
   choice, independent of the variable lengths or characters.
4. The putative failure of (2) costs `eta=10^-6`. All these losses,
   together with `20 delta`, are strictly smaller than `kappa`.

There is no effective claim for the threshold from which the fixed
endpoint ratios and logarithmic factors fit this budget. The theorem's
implied constant absorbs the bounded initial range.

## 2. Exact reduction to three factors

Let `Y0` exceed every norm in the support by a fixed factor, and put
`m=mu 1_(N<=sqrt(Y0))`. On `Nn<=Y0`,

\[
 \mu=2m-m*m*1.
\]

This follows because `delta1-m*1` is zero up to `sqrt(Y0)`, its
convolution square is zero up to `Y0`, and convolution with `mu`
expands to the displayed identity. For sufficiently large `Y`, the
`2m` term is absent on the annulus.

After smooth dyadic separation and Mellin inversion of the one product
weight, each piece is a product of three character polynomials. Write
their length exponents as `a1,a2,a3`, with

\[
 a_1,a_2\le\tfrac12+2\delta,\qquad
 a_1+a_2+a_3=1,\qquad a_i\ge0.                         \tag{3}
\]

The third polynomial is a full smooth ideal sum. Its norm height is at
most `Y^.37`, after truncating the common Mellin shifts. The first two
retain their hard Möbius cutoffs; all subsequent sieves allow these
arbitrary divisor-bounded coefficients.

If (2) failed, Minkowski and large-value pigeonholing would produce one
such product, and a set of rows of size `Y^r`, on which the factors have
sizes at least `Y^(v_i)`, satisfying

\[
 r+2v\ge\tfrac73-\kappa,
 \qquad v=v_1+v_2+v_3.                                \tag{4}
\]

Using dyadic upper endpoints for the sizes changes (4) only within the
budget. Values below a fixed large negative power may be discarded by
the trivial bounds on the other factors and the number of rows.

## 3. A full factor of exponent at least 9/10

Suppose `a3>=9/10`. The other factors have total trivial size
`Y^(1-a3+o(1))`. Remove missing Euler factors, fix their local parts as in
the source, and apply the full-sum functional equation.

At the first endpoint, its dual polynomial length has exponent at most
`1.74-a3`, before the error budget. The amplitude `sqrt(Z/J)` and the
unrestricted-inner cubic sieve give a total second-moment exponent at
most

\[
 2-a_3+\max\{1,1.74-a_3,\tfrac23(2.74-a_3)\}+\kappa
 \le \frac{349}{150}+\kappa.
\]

Here `349/150=7/3-1/150`. The conductor and root-number dependence stays
outside each polynomial, exactly as in the source's full-sum lemma.
The fixed small parts and the `q` average are included in the budget.

At the second endpoint, the trivial dual estimate gives full-factor
size at most `Y^(1/3+.37+o(1))`. Including the remaining factors and
`Y^(2/3+o(1))` rows gives exponent at most

\[
 \frac23+2(\tfrac13+.37)+2(1-a_3)+\kappa
 \le\frac{341}{150}+\kappa
 =\frac73-\frac3{50}+\kappa.
\]

Both contradict (4), since `2 kappa < 1/150`. We may henceforth assume
`a3<9/10`. By (3), one of the two short Möbius factors has exponent

\[
 \frac1{20}<a\le\frac12+2\delta.                      \tag{5}
\]

## 4. First endpoint: a bounded number of copies

Fix the subpower `q` variable; its count has already been charged to
(4). Put

\[
 d_i=v_i-\frac56a_i,\qquad D=d_1+d_2+d_3.
\]

For any of the products used below whose total length exponent `z` is
in `[1/2-2delta,2]`, the unrestricted-inner cubic sieve implies

\[
 r\le\frac23-2\sum_i k_i d_i+\kappa.                  \tag{6}
\]

For `z>=1/2` this is the exact identity
`z+max(1,z,2(1+z)/3)=(2+5z)/3`. The short interval below `1/2` changes
the right side by at most `4delta/3`, already included in the budget.

Repeating each factor once, so that `k=(1,1,1)+e_i`, is allowed since
`1+a_i<1.9` apart from negligible endpoint errors. Compare (6) with
the lower bound `r>=2/3-2D-kappa` from (4). This yields

\[
 d_i\le\kappa\quad(i=1,2,3),
 \qquad r\ge\frac23-7\kappa.                         \tag{7}
\]

Omitting the short factor in (5) is also allowed: its remaining length
is at least `1/2-2delta`. The same comparison gives
`d>=-kappa` for that factor.

Write `v_*` for the selected short factor's value exponent, and take
`k=ceil((7/5)/a)`. Then `k<=28`, hence certainly `k<=29`, and

\[
 1.4\le z=ka<1.900001,
 \qquad w=kv_*\ge\frac56z-29\kappa.                 \tag{8}
\]

The polynomial consisting of these copies has fixed divisor bounds
and a fixed support ratio. Apply the source's off-diagonal Gram estimate
and the Bombieri--Halász--Montgomery row bound to the same set of rows.
In exponent form this gives

\[
 2w-z\le
 \max\left\{z-r,
 \frac{z+\max(1,2-2z/3)-r}{2}\right\}+\kappa.          \tag{9}
\]

At `r=2/3` the two terms on the right of (9) are smaller than `2z/3`
by the respective gaps

\[
 \frac{2-z}{3},\qquad
 \begin{cases}(3z-4)/6,&z\le3/2,\\(z-1)/6,&z\ge3/2.
 \end{cases}
\]

Throughout (8), both gaps exceed `3/100`. Equations (7)--(9) would
therefore imply

\[
 \frac3{100}\le 66\kappa=0.0066,
\]

which is false. (The budget uses 58 `kappa` for the two-sided value
loss in (8), seven for the row count, and one for (9).)

## 5. Second endpoint: repeat each of the three factors once

The row count gives `r<=2/3+kappa`, so (4) implies

\[
 v\ge\frac56-\kappa.                                 \tag{10}
\]

For each `i`, apply the ordinary character large sieve to the full
product with factor `i` repeated once. Its length exponent is `1+a_i`
and the square of the conductor range has exponent `4/3`, before the
error budget. Comparing with (4) yields

\[
 v_i\le
 \begin{cases}
 a_i/2+\kappa,&a_i\le1/3,\\
 a_i-1/6+\kappa,&a_i\ge1/3.
 \end{cases}                                         \tag{11}
\]

Since `sum a_i=1` and every `a_i<=9/10`, the sum of the three
non-error terms in (11) is at most `47/60`. Indeed it equals
`1/2+(1/2)sum_i(a_i-1/3)_+`; with one exponent above `1/3` the positive
sum is at most `9/10-1/3=17/30`, while with two such exponents it is at
most `1/3`. Therefore

\[
 v\le\frac{47}{60}+3\kappa,
\]

contradicting (10), because `1/20>4 kappa`. This proves (2).

## 6. What is and is not quantified

The explicit saving in (1) concerns the exceptional ordinary cubic
character means with Möbius coefficients. It uses no zero-free input.
The fixed-angular extension uses only the Hecke functional equation.

A full Möbius-weighted cubic Gauss-sum moment also needs the generic
frequency ranges, common-divisor tails, and small-conductor estimates.
Those may use a source-qualified zero-free input. This note does not
assign them the same `eta` or supply a new inverse or global zero-free
consumer.
