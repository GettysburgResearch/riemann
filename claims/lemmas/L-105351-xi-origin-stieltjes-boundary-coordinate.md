# L-105351 — In a symmetric Xi window the boundary gate is one origin Stieltjes moment sequence

Claim ID: `L-105351`  
Status: **PROVED EXACT FINITE-WINDOW REDUCTION — XI SIGN OPEN**  
Created: 2026-08-23  
Depends on: `L-105214`, `L-105217`, `L-105329`, `L-105350`; the classical Stieltjes moment theorem  
RH status: **not assumed**

## 1. Boundary Cauchy function and canonical anchor

Let `F` be entire, real on the real axis, and of definite parity. Let
`Omega` be a bounded regular domain invariant under conjugation and under
`z -> -z`, with a real interval `I` containing zero in its interior. Put

\[
H(z)=H_{F,\Omega}(z)
={1\over2\pi i}\int_{\partial\Omega}
 {F(\zeta)/F'(\zeta)\over\zeta-z}\,d\zeta.
\tag{L-105351.1}
\]

The quotient `F/F'` is odd. Symmetry of the contour therefore gives

\[
\boxed{H(-z)=-H(z).}
\tag{L-105351.2}
\]

Thus the source-owned analytic anchor in `L-105350` is canonically `x_*=0`.
Define

\[
\boxed{
\beta_n(F;\Omega)
={H^{(2n+1)}(0)\over(2n+1)!}
={1\over2\pi i}\int_{\partial\Omega}
 {F(\zeta)/F'(\zeta)\over\zeta^{2n+2}}\,d\zeta,
\qquad n\ge0.
}
\tag{L-105351.3}
\]

All intervening Hamburger moments vanish by oddness.

## 2. Parity block diagonalization

For `k>=1`, define the two Hankel matrices

\[
\boxed{
\mathsf E_k=[\beta_{r+s}]_{r,s=0}^{k-1},
\qquad
\mathsf O_k=[\beta_{r+s+1}]_{r,s=0}^{k-1}.
}
\tag{L-105351.4}
\]

The complete confluent Hamburger matrix of `L-105350` at zero has entries

\[
{H^{(r+s+1)}(0)\over(r+s+1)!}.
\]

After reordering the monomials by even and odd degree it is exactly

\[
\boxed{
\mathsf E_k\oplus\mathsf O_k
}
\tag{L-105351.5}
\]

at the corresponding truncation. Consequently,

\[
\boxed{
{H(x)-H(y)\over x-y}\succeq0
\text{ on every finite real packet in }I
\Longleftrightarrow
\mathsf E_k\succeq0\text{ and }\mathsf O_k\succeq0
\text{ for every }k.
}
\tag{L-105351.6}
\]

This is an exact equivalence, not a bounded-order approximation.

## 3. Stieltjes representation

By the classical Stieltjes moment theorem, (L-105351.6) is equivalent to the
existence of a finite positive compactly supported Borel measure `nu` on
`[0,infinity)` such that

\[
\boxed{
\beta_n=\int_0^\infty s^n\,d\nu(s),
\qquad n\ge0.
}
\tag{L-105351.7}
\]

Equivalently, throughout the connected upper neighborhood of the interval,

\[
\boxed{
H(z)=z\int_0^\infty {d\nu(s)\over1-sz^2}.
}
\tag{L-105351.8}
\]

The compact support follows from analyticity exactly as in `L-105350`: Cauchy
bounds on the origin derivatives bound the even moments exponentially and
exclude mass outside one finite interval.

Thus the complete boundary Loewner gate in a symmetric Xi window is one
literal Stieltjes moment problem at the origin.

## 4. Exact safe-axis scalar

For real `y` with `iy in Omega`, oddness gives

\[
\boxed{
{H(iy)\over iy}
={1\over2\pi i}\int_{\partial\Omega}
 {F(\zeta)/F'(\zeta)\over\zeta^2+y^2}\,d\zeta
=\int_0^\infty {d\nu(s)\over1+s y^2}.
}
\tag{L-105351.9}
\]

Therefore the exact source coordinate that a safe-axis, Laplace, continued
fraction, or complete-monotonicity argument must identify is the boundary
Cauchy scalar `H(iy)/(iy)`, with the interior critical-pole subtraction of
`L-105214` retained. Positivity of the raw quotient `F/F'` on the safe axis is
not silently identified with (L-105351.9).

## 5. Fixed-anchor contour-square cone

For real coefficient vectors `a=(a_0,...,a_{k-1})` and
`b=(b_0,...,b_{k-1})`, the two matrix conditions are exactly

\[
\boxed{
\begin{aligned}
a^T\mathsf E_k a
&={1\over2\pi i}\int_{\partial\Omega}
 {F(\zeta)\over F'(\zeta)}
 \left(\sum_{r=0}^{k-1}{a_r\over\zeta^{2r+1}}\right)^2d\zeta,\\
b^T\mathsf O_k b
&={1\over2\pi i}\int_{\partial\Omega}
 {F(\zeta)\over F'(\zeta)}
 \left(\sum_{r=0}^{k-1}{b_r\over\zeta^{2r+2}}\right)^2d\zeta.
\end{aligned}
}
\tag{L-105351.10}
\]

Thus arbitrary separated Cauchy packets may be replaced, without loss, by all
Laurent-polynomial squares at the single anchor zero.

## 6. Polynomial exterior-residue calibration

Let `p` be a centered real polynomial **of definite parity** and degree `n`.
Let a symmetric inner window contain some but not all simple critical points.
For every positive exterior critical point `c`, parity gives the paired point
`-c` with the same residue

\[
\rho_c={p(c)\over p''(c)}={p(-c)\over p''(-c)}.
\]

The exact nested-window decomposition gives

\[
H_{p,\Omega}(z)
={z\over n}
+\sum_{\substack{p'(c)=0\\c>0,\ c\notin\Omega}}
 \rho_c\left({1\over z-c}+{1\over z+c}\right),
\tag{L-105351.11}
\]

hence

\[
\boxed{
H_{p,\Omega}(z)
=z\left[
 {1\over n}
 +\sum_{\substack{p'(c)=0\\c>0,\ c\notin\Omega}}
 {-2\rho_c/c^2\over1-z^2/c^2}
 \right].
}
\tag{L-105351.12}
\]

The Stieltjes measure is exactly

\[
\boxed{
\nu={1\over n}\delta_0
+\sum_{\substack{p'(c)=0\\c>0,\ c\notin\Omega}}
 {-2\rho_c\over c^2}\,\delta_{1/c^2}.
}
\tag{L-105351.13}
\]

If every crossed exterior residue is nonpositive, this measure is positive and
the inner boundary Loewner kernel is PSD. This is the origin-moment form of the
nested-window transport theorem `L-105217`.

## 7. New boundary gate

Define:

```text
OASH105350:
  in every regular symmetric window of the exact Xi exhaustion, the two
  origin Hankel families E_k and O_k in (L-105351.4) are PSD for every k.
```

Then, window by window,

\[
\boxed{
\mathrm{OASH105350}
\Longleftrightarrow
\mathrm{BCVH105330}
\Longleftrightarrow
\text{the all-packet PSD component of BRP105220}.
}
\tag{L-105351.14}
\]

`OASH105350` is not proved for the last defective Xi derivative.

## 8. Scope

This theorem is an exact quantifier reduction. It does not estimate the
contour moments `beta_n`, produce the positive measure for Xi, exclude nonreal
critical points, validate the moving-saddle theorem, or prove RH. Every order
is load bearing: `R-105350` gives an exact rational odd function whose first
two confluent orders pass while the third fails.
