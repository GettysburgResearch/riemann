# L-106710 — Carrier-adapted odd-endpoint antiphase density is source-soft

Claim ID: `L-106710`  
Status: **PROVED EXACT FOURIER ALGEBRA; XI ASYMPTOTIC INHERITS THE REVIEW BOUNDARY OF L-106502**  
Created: 2026-08-27  
Depends on: `L-106500--L-106502`; the positive even Xi Fourier kernel  
RH status: **not assumed**

Let

\[
F(t)=\int_{\mathbb R}\Phi(u)e^{itu}\,du,
\qquad \Phi(-u)=\Phi(u)\ge0,
\]

with enough decay for the operations below, and let `K=2m+1` be odd. Retain

\[
\mathcal L_K=(-1)^m(F'F^{(K)}-FF^{(K+1)})
\]

from `L-106500`, whose Fourier density is

\[
L_K(\xi)
=\frac12\int_{\mathbb R}
(v-u)(v^K-u^K)\Phi(u)\Phi(v)\,du\ge0,
\qquad v=\xi-u.
\tag{L-106710.1}
\]

For a constant companion scale `lambda>0`, define the antiphase numerator

\[
A_{K,\lambda}
=FF^{(K)}+\lambda^2F'F^{(K+1)}.
\tag{L-106710.2}
\]

This is the exact endpoint sum in `L-106501`:

\[
N+D=2A_{K,\lambda},
\qquad
D=A_{K,\lambda}+i\lambda(-1)^m\mathcal L_K.
\tag{L-106710.3}
\]

## 1. Exact antiphase Fourier density

Put

\[
a_{K,\lambda}(\xi)
=(-1)^m(-i)\widehat{A_{K,\lambda}}(\xi).
\]

Symmetrizing `u` and `v` gives

\[
\boxed{
a_{K,\lambda}(\xi)
=\frac12\int
(u^K+v^K)(1-\lambda^2uv)
\Phi(u)\Phi(v)\,du.
}
\tag{L-106710.4}
\]

For `xi>0`, write

\[
s=\frac\xi2,
\qquad
\delta=\frac{v-u}{2},
\qquad
u=s-\delta,
\quad v=s+\delta.
\]

Then

\[
\boxed{
1-\lambda^2uv
=1-\lambda^2s^2+\lambda^2\delta^2.
}
\tag{L-106710.5}
\]

Consequently

\[
a_{K,\lambda}(\xi)
=\left(1-\frac{\lambda^2\xi^2}{4}\right)a_{K,0}(\xi)
+\lambda^2 b_K(\xi),
\tag{L-106710.6}
\]

where, for `xi>0`, both

\[
a_{K,0}(\xi)
=\frac12\int[(s-\delta)^K+(s+\delta)^K]\Phi(s-\delta)\Phi(s+\delta)d\delta
\]

and

\[
b_K(\xi)
=\frac12\int\delta^2[(s-\delta)^K+(s+\delta)^K]
\Phi(s-\delta)\Phi(s+\delta)d\delta
\]

are nonnegative. Equation (L-106710.6) isolates the diagonal carrier mismatch
from the positive spread term.

## 2. Frequency-adapted source softening

For each `xi>0`, choose the Fourier-adapted scale

\[
\lambda_\xi=\frac2\xi=\frac1s.
\tag{L-106710.7}
\]

Then the mismatch term vanishes and

\[
1-\lambda_\xi^2uv=\frac{\delta^2}{s^2}.
\]

For every odd `K` and every real `x`,

\[
\boxed{
x\bigl[(1+x)^K+(1-x)^K\bigr]
\le
K\bigl[(1+x)^K-(1-x)^K\bigr]
\quad(x\ge0).
}
\tag{L-106710.8}
\]

Indeed the coefficient of `x^(2j+1)` in the difference is

\[
2\left[K{K\choose 2j+1}-{K\choose 2j}\right]\ge0.
\]

Applying (L-106710.8) pointwise in `delta` gives

\[
\boxed{
0\le a_{K,\lambda_\xi}(\xi)
\le\frac K\xi L_K(\xi),
\qquad \xi>0.
}
\tag{L-106710.9}
\]

Equivalently,

\[
0\le b_K(\xi)\le\frac{K\xi}{4}L_K(\xi).
\tag{L-106710.10}
\]

Thus the carrier-adapted antiphase density is one inverse source frequency
softer than the positive odd-current source.

## 3. Sharp fifth-order formula

For `K=5`, the pointwise gap before integration is exactly

\[
\boxed{
\frac5\xi(v-u)(v^5-u^5)
-(u^5+v^5)\left(1-\frac{4uv}{\xi^2}\right)
=16\delta^2s(5\delta^2+3s^2)\ge0.
}
\tag{L-106710.11}
\]

The common half-convolution factor is omitted from both sides. Hence no
constant is hidden in (L-106710.9).

## 4. Xi conditional carrier law

Use the conditional source probability measure `mu_(K,xi)` from `L-106502`.
For `K=5`, put `x=d/xi`, where `d=v-u`. Then

\[
\boxed{
\frac{a_{5,2/\xi}(\xi)}{L_5(\xi)}
=\frac1\xi
\int
\frac{1+10x^2+5x^4}{5+10x^2+x^4}
\,d\mu_{5,\xi}(d).
}
\tag{L-106710.12}
\]

Since

\[
5\frac{1+10x^2+5x^4}{5+10x^2+x^4}-1
=
\frac{8x^2(5+3x^2)}{5+10x^2+x^4},
\tag{L-106710.13}
\]

and `L-106502` proves

\[
\int |d|^{2q}d\mu_{5,\xi}(d)=O(e^{-q\xi}),
\]

one obtains

\[
\boxed{
\frac{a_{5,2/\xi}(\xi)}{L_5(\xi)}
=\frac1{5\xi}
\left(1+O\left(\frac{e^{-\xi}}{\xi^2}\right)\right).
}
\tag{L-106710.14}
\]

Since `lambda_xi=2/xi`, the dimensionless antiphase/source ratio is

\[
\boxed{
\frac{a_{5,\lambda_\xi}(\xi)}
     {\lambda_\xi L_5(\xi)}
=\frac1{10}
+O\left(\frac{e^{-\xi}}{\xi^2}\right).
}
\tag{L-106710.15}
\]

The constant `1/10` is the exact high-frequency fifth-endpoint diagonal phase,
not a fitted numerical parameter.

## 5. Scope

The scale in (L-106710.7) is a Fourier multiplier depending on `xi`. The
physical companion in `T-106620` uses one constant `lambda_j` on each real
mesoscopic window. Replacing that physical scale by `2/xi` is a nonlocal
operation and does not preserve the endpoint index theorem. Moreover the
full free energy has the forced topological factor isolated in `L-106674` and
`T-106700`.

```text
odd-endpoint antiphase density                         PROVED EXACT
carrier mismatch/spread decomposition                 PROVED EXACT
frequency-adapted source-soft inequality               PROVED EXACT
Xi fifth-order high-frequency ratio 1/10              PROVED GIVEN L-106502
physical constant-scale transfer                       OPEN
full Xi source-Pick free-energy bound                  OPEN
ninety percent / RH                                    UNPROVEN
```
