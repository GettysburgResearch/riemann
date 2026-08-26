# The full odd-notch second-boundary zero density

Status: **exact fixed-`q` asymptotic from a standard prime-polynomial
progression theorem; zeros here are detector zeros, not zeros of an
individual `L`-function**

Exact replay:
[`quadratic_family_second_boundary_zero_density.py`](quadratic_family_second_boundary_zero_density.py).

## 0. Outcome

The finite-residue gate left by the preceding second-boundary reduction can
be closed exactly.

Let

\[
 n=2h+1,\qquad M=4h+1,\qquad h\longrightarrow\infty,
\]

with `q` a fixed odd prime power.  Count monic squarefree degree-`M`
conductors whose least factor degree is `h-1`, with no degree-`h` factor, and
whose exterior-cubic residual `D_3` vanishes.  Write this count as `Z^(2)_(q,h)`.

There is an explicit rational number `delta_q` such that

\[
 \boxed{
 Z^{(2)}_{q,h}
 =\delta_q{1+\log2\over3}{q^M\over h^2}
 +O_q\!\left({q^M\over h^3}\right).}
\tag{0.1}
\]

Since the number of squarefree monic degree-`M` polynomials is
`q^M-q^(M-1)`, the normalized density is

\[
 \boxed{
 {Z^{(2)}_{q,h}\over q^M-q^{M-1}}
 ={16\delta_q(1+\log2)\over
   3(1-q^{-1})M^2}
 +O_q(M^{-3}).}
\tag{0.2}
\]

The exceptional `(h-1,h,h,h+2)` branch is `O_q(M^-4)` and does not alter
(0.2).  Thus this packet determines the complete leading contribution from
the first accidental-zero layer outside the support-forced region.

The constant `delta_q` is not empirical.  It is the exact zero probability
of one finite Rademacher polynomial described below.  The replay evaluates
it with integer binomial sums and no residue-class enumeration.

## 1. The local residue law

Let

\[
 \mathcal R_{\le3}=\prod_{\deg R\le3}R.
\]

Every conductor in this layer is coprime to this fixed modulus.  If its
residue class is uniform in `(F_q[T]/R_(<=3))^times`, the local quadratic
symbols

\[
 \varepsilon_R=(Q/R),\qquad \deg R\le3,
\]

are independent uniform signs by the Chinese remainder theorem.  There are

\[
 N_1=q,\qquad N_2={q^2-q\over2},\qquad
 N_3={q^3-q\over3}
\tag{1.1}
\]

irreducibles in degrees one, two, and three.  Put

\[
 S_d=\sum_{\deg R=d}\varepsilon_R.
\]

The coefficient of degree one is `A_1=S_1`.  The coefficient of degree three
contains an irreducible cubic, a linear times a quadratic, or a complete
homogeneous cubic in the linear signs:

\[
 A_3=S_3+S_1S_2+h_3(\varepsilon_1,\ldots,\varepsilon_q).
\]

Because every linear sign squares to one,

\[
 h_3={S_1^3+(3q+2)S_1\over6}.
\]

Therefore

\[
 \boxed{
 D_3=A_3-qA_1
 =S_3+S_1S_2+{S_1^3+(2-3q)S_1\over6}.}
\tag{1.2}
\]

Polynomial quadratic reciprocity contributes a fixed minus sign to every
odd-degree coefficient when `q=3 mod 4`; it sends `D_3` to `-D_3` and hence
does not change its zero set.

It follows that

\[
 \boxed{\delta_q=\Pr\left(
 S_3+S_1S_2+{S_1^3+(2-3q)S_1\over6}=0
 \right),}
\tag{1.3}
\]

where the three sums contain respectively `N_1,N_2,N_3` independent
Rademacher variables.  Explicitly,

\[
 \delta_q=2^{-(N_1+N_2+N_3)}
 \sum_{s_1,s_2}
 {N_1\choose(N_1+s_1)/2}
 {N_2\choose(N_2+s_2)/2}
 {N_3\choose(N_3+s_3^*)/2},
\tag{1.4}
\]

where

\[
 s_3^*=-s_1s_2-{s_1^3+(2-3q)s_1\over6},
\]

and a binomial coefficient is zero unless its lower argument is integral and
in range.

## 2. Equidistribution of the rough profiles

For fixed modulus `R_(<=3)`, the standard prime-polynomial theorem in
arithmetic progressions gives, uniformly over invertible residue classes,

\[
 \pi_q(d;\mathcal R_{\le3},a)
 ={q^d\over d\varphi(\mathcal R_{\le3})}
 +O_q(q^{d/2}/d).
\tag{2.1}
\]

Character orthogonality applies (2.1) to products of two or three
irreducibles.  Every factor degree in the present layer is at least `h-1`,
so every nonprincipal character contribution is exponentially smaller than
`q^M/h^3`.  Repeated-degree diagonals and the squarefree exclusion are also
lower order.  Hence every leading factor-degree profile is equidistributed
among the invertible residue classes, and the fraction with `D_3=0` is
exactly (1.3).

This use of function-field RH is standard and source-faithful: the modulus is
fixed while the prime degrees grow.  It is not an inference from values at a
few `q`.

## 3. The factor-profile constant

The leading profiles contain exactly one degree-`h-1` factor.  Two such
factors contribute only `O(q^M/h^3)`.  With exactly one pinned factor and no
degree-`h` factor, there can be only one or two remaining factors, because

\[
 (h-1)+3(h+1)>4h+1.
\]

### Two factors

The profile is `(h-1,3h+2)`, with main weight

\[
 {1\over(h-1)(3h+2)}.
\]

After multiplication by `h^2`, this tends to `1/3`.

### Three factors

The profiles are

\[
 (h-1,d,3h+2-d),
 \qquad h+1\le d\le{3h+2\over2}.
\]

The repeated midpoint has half weight and is lower order.  The Riemann sum
gives

\[
 \begin{aligned}
 h^2\sum_d{1\over(h-1)d(3h+2-d)}
 &\longrightarrow
 \int_1^{3/2}{dx\over x(3-x)}\\
 &={\log2\over3}.
 \end{aligned}
\tag{3.1}
\]

Adding the two-factor contribution proves the profile constant
`(1+log(2))/3`.  Euler--Maclaurin at this smooth finite interval, together
with the lower profile layers, gives the stated `O_q(h^-3)` remainder.

## 4. A large-`q` cubic-chaos law

The exact constants suggest a second, independent limit.  As `q` grows,

\[
 {S_1\over\sqrt q}\Rightarrow X,\qquad
 {S_2\over q/\sqrt2}\Rightarrow Y,\qquad
 {S_3\over q^{3/2}/\sqrt3}\Rightarrow Z,
\]

for independent standard normals.  Dividing (1.2) by `q^(3/2)` and applying
the multivariate central limit theorem gives the exact weak limit

\[
 \boxed{
 {D_3\over q^{3/2}}
 \Rightarrow
 W={Z\over\sqrt3}+{XY\over\sqrt2}+{X^3-3X\over6}.}
\tag{4.1}
\]

The three summands are orthogonal Gaussian chaoses.  Direct Wick calculation
gives

\[
 \boxed{
 \mathbb E[W^2]=1,\qquad
 \mathbb E[W^4]=10,\qquad
 \mathbb E[W^6]=760.}
\tag{4.2}
\]

So the limiting law is emphatically non-Gaussian even though its variance is
one.  Conditional on `X=x`, it is normal with

\[
 \operatorname{mean}={x^3-3x\over6},\qquad
 \operatorname{variance}={1\over3}+{x^2\over2}.
\]

This supplies an explicit integral for its density at zero.  It is tempting
to conjecture the lattice local limit

\[
 q^{3/2}\delta_q\longrightarrow2f_W(0),
\tag{4.3}
\]

where the factor two is the lattice span.  The replay's exact rows are
consistent with this, but (4.3) is **not proved here**: weak convergence does
not imply a local limit for a cubic lattice polynomial.

## 5. Proof ledger

Proved exactly, conditional only on the standard theorem (2.1):

- the independent-sign formula (1.2)--(1.4);
- equidistribution of every leading rough profile modulo `R_(<=3)`;
- the count and density asymptotics (0.1)--(0.2);
- the weak cubic-chaos limit (4.1) and moments (4.2).

Still open:

- the local limit (4.3) as `q` grows;
- the next `M^-3` coefficient;
- any connection between these detector zeros and zeros of an individual
  `L`-function;
- RH or GRH over number fields.

No external novelty or priority claim is made without specialist review.

## 6. Bounded replay

Run:

```text
python -B research/l-families/atlas/function_field/quadratic_family_second_boundary_zero_density.py --check
python -B -O research/l-families/atlas/function_field/quadratic_family_second_boundary_zero_density.py --check
python -B -m unittest tests.test_quadratic_family_second_boundary_zero_density
python -B -O -m unittest tests.test_quadratic_family_second_boundary_zero_density
```

The replay enumerates no residue class, polynomial, curve, or point.  It
sums at most the two binomial coordinates for `q<=13`, checks profile Riemann
sums through `h=200`, and computes the three chaos moments by exact rational
polynomial arithmetic.
