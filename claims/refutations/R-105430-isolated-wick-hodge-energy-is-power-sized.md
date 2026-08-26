# R-105430 — Isolating the Wick remainder before squaring leaves a power-sized Hodge carrier

Claim ID: `R-105430`

Status: **PROVED ASYMPTOTIC REFUTATION OF THE T-105420 ENERGY FRONTIER**

Frozen arithmetic input: PR #719 at
`b6cb90d3d5f06320ba2c4908930a5b85fa270240`.

Let the labelled prime Dirichlet coordinate be

\[
P_{67}(z)=\sum_p p^{-z}+67^{-z},
\]

where the final term is the second labelled occurrence of \(67\).  Put

\[
E(z)=\frac{1-67^{-z}}{\zeta(z)},
\qquad
S(z)=\frac{1-67^{-2z}}{\zeta(2z)}.
\]

The exact Wick identity on PR #719 is

\[
E=SRe^{-P_{67}},
\qquad
RS=Ee^{P_{67}}.
\]

The source remaining after the root/first-chaos packet is removed is

\[
D_{\ge2}(z)
=
E(z)-S(z)+R(z)S(z)P_{67}(z).
\tag{R-105430.1}
\]

## 1. The surviving real logarithmic carrier

Mertens' prime theorem gives

\[
P_{67}(z)
=
\log\frac1{z-1}+O(1)
\qquad(z\downarrow1).
\]

Moreover

\[
C_{67}
:=
\lim_{z\downarrow1}E(z)e^{P_{67}(z)}
=
\lim_{z\downarrow1}R(z)S(z)
\]

exists and is strictly positive: every local logarithm begins in prime degree
two and the corresponding Euler product converges absolutely at \(z=1\).
Consequently

\[
\boxed{
D_{\ge2}(z)
=
C_{67}\log\frac1{z-1}+O(1).
}
\tag{R-105430.2}
\]

The full source \(E-S\) has no such logarithmic singularity.  It is created by
separating \(RS\,P_{67}\) from its opposite contribution in \(D_{\ge2}\).

## 2. Transfer to the two F1 primitive coordinates

Use the centered filtered-disk coordinates

\[
B=G-A,
\qquad
L=4A-B,
\qquad
J=A+192B.
\]

PR #719 proves for their compact kernels that

\[
\widehat k_A(1/2)=0,
\qquad
\widehat k_B(1/2)=\kappa_0>0,
\]

with

\[
\kappa_0
=
4\log2\,(3-2\sqrt2).
\]

The standard Selberg--Delange/Mellin transfer for a logarithmic singularity
then gives

\[
B_{\ge2}(X)
=
C_{67}\kappa_0
\frac{\sqrt X}{\log X}
+
O\!\left(\frac{\sqrt X}{\log^2X}\right),
\tag{R-105430.3}
\]

while

\[
A_{\ge2}(X)
=
O\!\left(\frac{\sqrt X}{\log^2X}\right).
\]

Therefore

\[
L_{\ge2}(X)
=
-C_{67}\kappa_0
\frac{\sqrt X}{\log X}
+
O\!\left(\frac{\sqrt X}{\log^2X}\right),
\]

\[
J_{\ge2}(X)
=
192C_{67}\kappa_0
\frac{\sqrt X}{\log X}
+
O\!\left(\frac{\sqrt X}{\log^2X}\right).
\]

The isolated positive Hodge square obeys

\[
\boxed{
L_{\ge2}(X)^2+\frac{J_{\ge2}(X)^2}{48}
=
769C_{67}^2\kappa_0^2
\frac{X}{\log^2X}
\left(1+O\!\left(\frac1{\log X}\right)\right).
}
\tag{R-105430.4}
\]

It is power-sized on logarithmic blocks.

## 3. Correct disposition

The first-chaos packet has the opposite leading \((L,J)\) carrier.  Its
recombination with (R-105430.3) is load bearing.  The inequality

\[
(P+R)_-\le |R|
\]

is true but loses this power-scale cancellation and cannot be followed by a
subpower estimate for \(|R|^2\).

Thus the following checkpoint-three frontier is withdrawn:

```text
F1WNC105420:
  subpower positive Hodge energy of the isolated Wick remainder.
```

The finite Frobenius functor, toric Hodge index, three-ray primitive class and
Wick source identity are unaffected.  The corrected order is stated in
`L-105430` and `T-105430`.
