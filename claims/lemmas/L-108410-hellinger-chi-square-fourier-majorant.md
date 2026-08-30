# L-108410 — Occupancy Hellinger debt has an exact nonprincipal Fourier majorant

Claim ID: `L-108410`  
Status: **PROVED EXACT FINITE HARMONIC-ANALYSIS THEOREM**  
Created: 2026-08-31  
Depends on: `L-108400` only for the later positive-trace application  
RH/GRH status: **not assumed**

Let `X` be a finite abelian group of cardinality `m`. Let

\[
n:X\to[0,\infty),
\qquad
N=\sum_{x\in X}n(x)>0,
\qquad
\bar n={N\over m}.
\]

Define the unnormalized Fourier transform

\[
\widehat n(\chi)
=
\sum_{x\in X}n(x)\overline{\chi(x)}
\]

and the square-root occupancy debt

\[
H_X(n)^2
=
\sum_{x\in X}
\left(\sqrt{n(x)}-\sqrt{\bar n}\right)^2.
\tag{L-108410.1}
\]

## 1. Chi-square and Fourier bounds

Pointwise,

\[
\left(\sqrt a-\sqrt b\right)^2
=
{(a-b)^2\over(\sqrt a+\sqrt b)^2}
\le
{(a-b)^2\over b}
\qquad (b>0).
\]

Therefore

\[
H_X(n)^2
\le
{m\over N}
\sum_x|n(x)-\bar n|^2.
\tag{L-108410.2}
\]

Parseval in the declared unnormalized convention gives

\[
\sum_x|n(x)-\bar n|^2
=
{1\over m}
\sum_{\chi\ne1}|\widehat n(\chi)|^2.
\]

Consequently

\[
\boxed{
H_X(n)^2
\le
{1\over N}
\sum_{\chi\ne1}|\widehat n(\chi)|^2.
}
\tag{L-108410.3}
\]

In normalized form,

\[
\boxed{
\eta_X(n)
:={H_X(n)^2\over N}
\le
{1\over N^2}
\sum_{\chi\ne1}|\widehat n(\chi)|^2.
}
\tag{L-108410.4}
\]

Thus the live Hellinger problem is a literal nonprincipal character-energy
problem rather than a nonlinear occupancy mystery.

## 2. Total-variation boundary transfer

For arbitrary nonnegative occupancies `n,e` on the same finite set,

\[
\boxed{
\sum_x(\sqrt{n(x)}-\sqrt{e(x)})^2
\le
\sum_x|n(x)-e(x)|.
}
\tag{L-108410.5}
\]

If they have equal total mass `N`, `L-108400` therefore gives

\[
\boxed{
\left|\operatorname{tr}Q(n)_+
-
\operatorname{tr}Q(e)_+\right|
\le
2\sqrt{N}
\,\|n-e\|_1^{1/2}.
}
\tag{L-108410.6}
\]

In particular a live-mask completion with relative missing mass `delta`
contributes at most `2N sqrt(delta)` to the positive trace. The square-root
loss is explicit and may not be suppressed.

## 3. Orbitwise version

The same proof applies on every orbit of a finite partial-Frobenius action.
Writing `bar n` for the orbitwise average, one obtains the direct sum of
(L-108410.3). Thus only Fourier modes nontrivial on the declared orbits enter
the Hellinger debt.

## Scope

The theorem is exact finite harmonic analysis. It does not estimate the live
number-field character energy or the explicit quadratic resonance rows.
