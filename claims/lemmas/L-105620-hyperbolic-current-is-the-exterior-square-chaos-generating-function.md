# L-105620 — The hyperbolic Xi current is the complete exterior-square chaos generating function

Claim ID: `L-105620`  
Status: **PROVED EXACT UNCONDITIONAL POSITIVE-SOURCE THEOREM**  
Created: 2026-08-25  
Depends on: the positive even Xi Fourier kernel; `L-105613/L-106401` for the quadratic exterior square  
RH status: **not assumed**

## 1. Positive Fourier source

Let

\[
F(z)=\int_{\mathbb R}\Phi(u)e^{izu}\,du,
\qquad
\Phi(-u)=\Phi(u)\ge0,
\]

where `Phi` has the decay needed for every differentiation and convolution
below. The standard Xi kernel satisfies these hypotheses.

For `h>0`, put

\[
F_h(a)=F(a+ih)
\]

and define the hyperbolic denominator current

\[
\boxed{
J_h(a)=\operatorname{Im}\bigl(F_h(a)\overline{F_h'(a)}\bigr)
={1\over2}\partial_h|F_h(a)|^2.
}
\tag{L-105620.1}
\]

Use the Fourier convention of `L-106401`, so that `widehat F=Phi`.
For real `xi`, set

\[
P_\xi(x)
=\Phi\!\left(x+{\xi\over2}\right)
 \Phi\!\left(x-{\xi\over2}\right).
\tag{L-105620.2}
\]

Because `Phi` is even, `P_xi` is even in `x` and nonnegative.

The Fourier transform of the positive square is

\[
\widehat{|F_h|^2}(\xi)
=\int_{\mathbb R}e^{-2hx}P_\xi(x)\,dx.
\tag{L-105620.3}
\]

Differentiating and pairing `x` with `-x` gives

\[
\boxed{
\widehat J_h(\xi)
=2\int_0^\infty
x\sinh(2hx)P_\xi(x)\,dx
\ge0.
}
\tag{L-105620.4}
\]

Thus `J_h` is positive definite for every physical height, without assuming
that it is pointwise positive.

## 2. The complete even exterior-square hierarchy

For every integer `m>=1`, define

\[
\boxed{
\Lambda_{2m}(\xi)
={1\over2}\int_{\mathbb R}
(2u-\xi)^{2m}\Phi(u)\Phi(\xi-u)\,du.
}
\tag{L-105620.5}
\]

Every `Lambda_(2m)` is nonnegative. Substituting
`u=x+xi/2` gives

\[
\Lambda_{2m}(\xi)
=2^{2m}\int_0^\infty x^{2m}P_\xi(x)\,dx.
\tag{L-105620.6}
\]

The first member is precisely the actual Laguerre--Turan source:

\[
\Lambda_2
=\widehat{F'^2-FF''}.
\tag{L-105620.7}
\]

Expanding the hyperbolic sine in (L-105620.4), with monotone convergence,
proves the exact all-order identity

\[
\boxed{
\widehat J_h(\xi)
=
\sum_{k=0}^\infty
{h^{2k+1}\over(2k+1)!}
\Lambda_{2k+2}(\xi).
}
\tag{L-105620.8}
\]

The denominator current is therefore not a separate source which must be
reconstructed or whitened against the Turan numerator. It is the odd
exponential generating function of the complete positive exterior-square
chaos hierarchy, and the actual Turan source is its first coefficient.

## 3. Exact reserve beyond the Turan source

Every term in (L-105620.8) is nonnegative, so

\[
\boxed{
\widehat J_h(\xi)
\ge h\Lambda_2(\xi)
+{h^3\over6}\Lambda_4(\xi)
\ge h\Lambda_2(\xi).
}
\tag{L-105620.9}
\]

For the Xi kernel the reserve is strict wherever `Lambda_4` is nonzero.
No cutoff, saddle approximation, Euler freeze or zero-location input occurs.

More generally, truncating after any order leaves a nonnegative remainder:

\[
\widehat J_h
-
\sum_{k=0}^{M}
{h^{2k+1}\over(2k+1)!}\Lambda_{2k+2}
\ge0.
\tag{L-105620.10}
\]

## 4. One-sided analytic Turan channels

Let

\[
\mathcal T_F(z)=F'(z)^2-F(z)F''(z).
\]

Analytic translation gives

\[
\boxed{
\widehat{\mathcal T_F(\cdot+ih)}(\xi)
=e^{-h\xi}\Lambda_2(\xi).
}
\tag{L-105620.11}
\]

Hence on the decaying positive-frequency channel,

\[
\boxed{
0\le
h e^{-h\xi}\Lambda_2(\xi)
\le h\Lambda_2(\xi)
\le\widehat J_h(\xi)
\qquad(\xi\ge0).
}
\tag{L-105620.12}
\]

By reflection, on the decaying negative-frequency channel,

\[
\boxed{
0\le
h e^{h\xi}\Lambda_2(\xi)
\le\widehat J_h(\xi)
\qquad(\xi\le0).
}
\tag{L-105620.13}
\]

Thus both causal orientations of the **actual translated Xi Turan source** are
coefficientwise dominated by the actual denominator current, with the explicit
higher-chaos reserve (L-105620.9).

The amplified opposite-frequency halves are not discarded. They are precisely
the reflected/Toeplitz channels which must remain paired in the physical
polarization.

## 5. Meaning for the current programmes

The following source-side interfaces are now exact:

```text
actual denominator current                positive Fourier source;
actual Turan numerator                    first exterior-square chaos;
all higher current reserve                positive exterior-square chaoses;
positive-frequency upper channel          dominated coefficientwise;
negative-frequency reflected channel      dominated coefficientwise.
```

The unresolved theorem is no longer a magnitude comparison between unrelated
sources. It is whether this diagonal Fourier domination survives the
source-to-physical identification and the variable all-pass phase
`conjugate(Xi')/Xi'`.

## 6. Scope

Positive Fourier density is not pointwise positivity. Equations
(L-105620.9)--(L-105620.13) do not imply

\[
h|\mathcal T_\Xi(a+ih)|\le J_\Xi(a,h)
\]

or its phase-oriented version. The countermodel in `R-105610` remains binding.
The theorem removes source reconstruction and source-level denominator
whitening; it does not prove the physical phase-collision estimate or RH.
