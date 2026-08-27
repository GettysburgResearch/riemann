# L-105613 — The actual Turán exterior square is the numerator of the hyperbolic phase barycenter

Claim ID: `L-105613`  
Status: **PROVED EXACT FACTORIZATION; XI FOURIER SOURCE UNCONDITIONAL**  
Created: 2026-08-24  
Depends on: `L-105600`; sibling PR #731 at head `50cf8ef3419b88c33b11de4b538192c5ad6a36e9`  
RH status: **not assumed**

## 1. Algebraic factorization

Let `F` be holomorphic and put

\[
D=F',
\qquad
\mathcal T_F=D^2-FD'.
\tag{L-105613.1}
\]

At

\[
z=a+ih,
\qquad h>0,
\]
assume `D(z)!=0` and define

\[
J_F(z)=\operatorname{Im}\bigl(F(z)\overline{D(z)}\bigr).
\tag{L-105613.2}
\]

For

\[
m={F\over F'},
\qquad
v=\operatorname{Im}m(z),
\]
one has exactly

\[
\boxed{
v={J_F\over|D|^2},
\qquad
m'={\mathcal T_F\over D^2}.
}
\tag{L-105613.3}
\]

Whenever `J_F>0`, the normalized hyperbolic derivative from `L-105600` is

\[
\boxed{
\mathfrak d_m(z)
={h m'(z)\over\operatorname{Im}m(z)}
={h\mathcal T_F(z)\over J_F(z)}
 {\overline{D(z)}\over D(z)}.
}
\tag{L-105613.4}
\]

Thus:

```text
magnitude source:       h |T_F| / J_F;
only unit phase:        conjugate(D)/D;
```

and

\[
\boxed{
|\mathfrak d_m(z)|
={h|\mathcal T_F(z)|\over J_F(z)}.
}
\tag{L-105613.5}
\]

The complete Schwarz--Pick defect is therefore

\[
\boxed{
1-|\mathfrak d_m(z)|^2
={J_F(z)^2-h^2|\mathcal T_F(z)|^2\over J_F(z)^2}.
}
\tag{L-105613.6}
\]

The directional microscope is

\[
\boxed{
2\mathcal C_F(a,h)
={h\over|D|^2}
\Re\left(
\mathcal T_F{\overline D\over D}
\right)
-{J_F\over|D|^2}.
}
\tag{L-105613.7}
\]

Hence the differential/Newton phase reserve is a normalized, denominator-
rotated Turán field.

## 2. Positive Xi exterior-square source

Use the positive Fourier representation

\[
\Xi(z)=\int_{\mathbb R}\Phi(u)e^{izu}\,du,
\qquad \Phi(u)\ge0.
\tag{L-105613.8}
\]

A direct double-integral calculation gives

\[
\boxed{
\mathcal T_\Xi(z)
=\Xi'(z)^2-\Xi(z)\Xi''(z)
={1\over2}
\iint_{\mathbb R^2}
(u-v)^2\Phi(u)\Phi(v)e^{iz(u+v)}\,du\,dv.
}
\tag{L-105613.9}
\]

With the Fourier normalization used on sibling PR #731,

\[
\boxed{
\widehat{\mathcal T_\Xi}(\xi)
={1\over4\pi}
\int_{\mathbb R}
(2u-\xi)^2\Phi(u)\Phi(\xi-u)\,du
\ge0.
}
\tag{L-105613.10}
\]

Thus the actual Xi Turán numerator is already a positive exterior-square theta
source. No frozen numerator or arithmetic surrogate is required.

At positive height, analytic translation multiplies this density by the
positive weight `exp(-h xi)` in the oriented Fourier convention. Positivity of
the source density is retained; only the all-pass denominator phase in
(L-105613.4) remains signed.

## 3. Cross-program identification

Sibling PR #731 uses precisely the source `T_Xi` as the actual theta-Hankel
leakage in its robust frame. Equations (L-105613.4)--(L-105613.7) prove that
the same source is the numerator of the pointwise phase-barycenter and
zero-height microscope on this PR.

Therefore the two current programmes share the exact physical pair

```text
denominator/current:   J_Xi and the Xi-prime all-pass phase;
positive numerator:    T_Xi = Xi'^2-Xi Xi''.
```

The averaged `ROBUSTFRAME106310` theorem and the pointwise
`DMPXFER105603` theorem are not independent source constructions. They are two
norms of the same actual denominator-whitened Turán source.

## 4. A pointwise scalar normal form

In any region where `J_Xi>0`, the full Schwarz--Pick contraction is the single
actual inequality

\[
\boxed{
h|\mathcal T_\Xi(z)|\le J_\Xi(z).
}
\tag{L-105613.11}
\]

The directional microscope needs only the phase-oriented version

\[
\boxed{
h\Re\left(
\mathcal T_\Xi(z){\overline{\Xi'(z)}\over\Xi'(z)}
\right)
\le J_\Xi(z).
}
\tag{L-105613.12}
\]

These are exact actual-Xi scalar coordinates. They are not asserted here.

## 5. Scope

A positive Fourier density need not be pointwise positive after analytic
translation and multiplication by an arbitrary all-pass denominator. The
factorization removes the frozen-to-actual numerator interface; it does not
prove the denominator-whitened inequality. The remaining work is physical
restriction/conditioning, not source reconstruction.