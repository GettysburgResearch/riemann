# Scalarize before composing: a factor-67 SHARP Harnack reduction

## Status

This document proves an exact reduction and an exact finite theorem. It does
not prove the unbounded tail and does not establish the Riemann Hypothesis.

## 1. Where the live proof graph stands

The latest repository work makes three corrections unavoidable.

First, the same physical row cannot carry the old `4sqrt(X)-O(1)` score while
remaining near-native in every response coordinate. Second, the old
second-order Volterra inverse has a two-dimensional homogeneous nullspace and
activation-knot atoms. Third, PR #642 supplies a cleaner object: every fixed
component row is an exact positive convolution of the single SHARP target

\[
T(y)=(4\sqrt y-3)\mathbf1_{y\ge1}.
\]

For each `j>=2`, there is an explicit strictly positive kernel `kappa_j` with

\[
Q_Y(j)=\int_1^YT(Y/t)\kappa_j(t)\frac{dt}{t}.
\tag{1.1}
\]

Consequently the full Möbius row is

\[
c_X(j)=\int_1^X\Psi(X/t)\kappa_j(t)\frac{dt}{t},
\tag{1.2}
\]

where

\[
\Psi(x)=\sum_{n\le x}\frac{\mu(n)}{\sqrt n}T(x/n).
\tag{1.3}
\]

Thus `Psi`, not an equality endpoint frame, is the common primitive of every
row.

## 2. Exact source repair inside the kernel

Define

\[
dM_Y^{(j)}(t)=\mathbf1_{t\le Y}T(Y/t)\kappa_j(t)\frac{dt}{t}.
\]

For `Z<=Y`, the child is not the raw cutoff of this measure. It is

\[
dM_Z^{(j)}(t)
=
\mathbf1_{t\le Z}
\frac{T(Z/t)}{T(Y/t)}dM_Y^{(j)}(t).
\tag{2.1}
\]

The ratio lies in `[0,1]`. Hence every child is a literal submeasure of one
parent.

The same formula proves the normalized Hall profile. For fixed `t`,

\[
\frac{\partial}{\partial Y}
\frac{T(Y/t)}{T(Y)}
=
\frac{6(1-t^{-1/2})}
{\sqrt Y(4\sqrt Y-3)^2}\ge0.
\tag{2.2}
\]

Therefore the normalized source measures `M_Y/T(Y)` increase with endpoint.
Every matched compact Hall edge is a positive difference of two such measures.
Every residual source is positive. For child coefficients `alpha_i` with total
below `1/8`, the widths

\[
\alpha_i\mathbf1_{t\le Z_i}\frac{T(Z_i/t)}{T(Y/t)}
\]

fit disjointly into one random-key coordinate. This reconstructs the Hall
profile and child-ownership interfaces exactly.

The raw-cutoff negative control is concrete. At `Y=16`, `Z=4`, `t=4`, the raw
parent density is `5 kappa_j(4)` while the child density is `kappa_j(4)`. The
factor `1/5` in (2.1) is load-bearing.

## 3. The scalar factor-67 move

Once (1.2) is known, carrying every row through the global recursion is
unnecessary. Put

\[
\mathfrak H_{67}(x)
=\Psi(x)-67^{-1/2}\Psi(x/67).
\tag{3.1}
\]

If `mathfrak H_67(x)>=0`, then

\[
\Psi(x)\ge67^{-1/2}\Psi(x/67).
\]

The compact SHARP Hall certificate gives `Psi>=0` on `[1,67)`. Repeated
division therefore proves `Psi>=0` globally. Equation (1.2) then makes every
component row nonnegative.

More importantly, the scalar has its own direct analytic consumer, so no row
index is needed at all.

## 4. Exact local square

Finite reindexing gives

\[
\mathfrak H_{67}(x)
=
\sum_{n\le x}\frac{\beta_{67}(n)}{\sqrt n}T(x/n),
\qquad
\beta_{67}(n)=\mu(n)-\mathbf1_{67\mid n}\mu(n/67).
\tag{4.1}
\]

Writing `n=67^f m`, `(m,67)=1`, gives

\[
\beta_{67}(n)=c_{67}(f)\mu(m),
\qquad c_{67}(0,1,2)=(1,-2,1),
\tag{4.2}
\]

and zero thereafter. The chosen dilation exactly squares the local Euler
factor at 67.

On `[N,N+1)`,

\[
\mathfrak H_{67}(x)
=4\sqrt x\sum_{n\le N}\frac{\beta_{67}(n)}n
-3\sum_{n\le N}\frac{\beta_{67}(n)}{\sqrt n}.
\tag{4.3}
\]

Hence the function is monotone on each cell and its minimum is at one of the
two cell boundaries.

## 5. Exact finite certificate

The retained segmented producer uses denominator `2^50` for the two prefix
sums and denominator `2^100` after multiplying by the directed square-root
interval. Every candidate comparison is signed integer arithmetic. The scan
covers the left endpoint and pre-activation right limit of every cell through
`10^8`.

It proves

\[
\mathfrak H_{67}(x)>0
\qquad(67\le x<100000001).
\]

The minimum enclosure occurs at `x=201^-`:

\[
\frac{1626923303441334483980962730376}{2^{100}}
\le\min\mathfrak H_{67}
\le
\frac{1626923303449543135335825015140}{2^{100}}.
\]

The lower endpoint is greater than `1.28341618987788997`. The sign decision is
therefore separated from zero by a macroscopic margin.

The fast verifier independently reconstructs the compact Hall base, the wrong
`2sqrt(y)-1` target failure, the Radon–Nikodym ratios, the local-square
coefficient dictionary, the Mellin symbol, and the exact minimizer interval.
Full replay rescans all cells and requires byte-identical output.

## 6. Direct Mellin–Landau closure

For `Re(s)>1/2`,

\[
\int_1^\infty\mathfrak H_{67}(x)x^{-s-1}dx
=
\frac{(1-67^{-(s+1/2)})(s+3/2)}
{s(s-1/2)\zeta(s+1/2)}.
\tag{6.1}
\]

The continuation is analytic on every positive real `s`. If
`mathfrak H_67>=0` globally, Landau's theorem forces the defining transform to
be holomorphic in `Re(s)>0`. A zero `rho` with `Re(rho)>1/2` produces a pole at
`s=rho-1/2`. It cannot be canceled by the factor at 67 because

\[
|67^{-\rho}|<1.
\]

This contradiction excludes all zeros to the right. Functional-equation
symmetry excludes zeros to the left.

## 7. The exact last line

The entire conclusion-facing route has therefore been reduced to

\[
\boxed{
\mathfrak H_{67}(x)\ge0
\qquad(x\ge100000001).
}
\]

Proving that tail would complete the argument. This packet does not prove it.

All of the following are absent from the conclusion-facing path:

```text
score calibration;
ordinary or radix-four capacity;
second-order Volterra boundary modes;
finite/continuum endpoint equality;
row-specific noncancellation;
common-parent recursion;
terminal and prime-square ports.
```
