# L-90425 — The phase-locked factor-16 filter is a uniformly coercive critical-scale frame

Claim ID: `L-90425`  
Title: After square-root normalization, the unique phase-locked factor-16 filter is an exact Fejer--Riesz square with a positive spectral gap, so its dyadic scale energy is quantitatively equivalent to the unfiltered critical energy  
Status: **PROPOSED COMPLETE EXACT HILBERT-SPACE THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Dependencies: `L-90423`; elementary Fourier theory on the bilateral shift  
Scope: dyadic scale geometry; no arithmetic estimate for the filtered prime signal

## 1. Square-root-normalized polynomial

Let

\[
Q_*(y)=2-15y+35y^2-30y^3+8y^4.
\]

Put `r=2^-1/2` and define

\[
A(z)=Q_*(rz)
 =2-\frac{15}{\sqrt2}z
  +\frac{35}{2}z^2
  -\frac{15}{\sqrt2}z^3+2z^4.
\tag{L-90425.1}
\]

For `|z|=1`, the phase-lock identity of `L-90423` becomes

\[
\boxed{
 z^{-2}A(z)
 =8\left|1-\frac z{\sqrt2}\right|^2
   \left|1-\frac z{2\sqrt2}\right|^2.
}
\tag{L-90425.2}
\]

Equivalently, with

\[
p(z)=1-\frac{3}{2\sqrt2}z+\frac14z^2,
\tag{L-90425.3}
\]

\[
\boxed{z^{-2}A(z)=8p(z)\overline{p(z)}.}
\tag{L-90425.4}
\]

The symbol has the exact bounds

\[
\boxed{
\frac{43}{2}-15\sqrt2
 \le z^{-2}A(z)
 \le\frac{43}{2}+15\sqrt2.
}
\tag{L-90425.5}
\]

The lower endpoint is strictly positive.

## 2. Exact Hilbert-sequence identity

Let `S` be the bilateral shift on `ell^2(Z;H)` for any complex Hilbert space `H`. Then

\[
\boxed{
S^{-2}A(S)=8p(S)^*p(S).
}
\tag{L-90425.6}
\]

Consequently, for every finitely supported Hilbert sequence `x=(x_m)`,

\[
\boxed{
\begin{aligned}
&\frac{35}{2}\sum_m\|x_m\|^2
 -\frac{30}{\sqrt2}\sum_m
   \operatorname{Re}\langle x_m,x_{m-1}\rangle\\
&\qquad
 +4\sum_m\operatorname{Re}\langle x_m,x_{m-2}\rangle\\
&=8\sum_m\left\|
 x_m-\frac{3}{2\sqrt2}x_{m-1}+\frac14x_{m-2}
 \right\|^2.
\end{aligned}}
\tag{L-90425.7}
\]

The two-sided coercive estimate is

\[
\boxed{
\left(\frac{43}{2}-15\sqrt2\right)\|x\|_2^2
\le
\operatorname{Re}\langle x,S^{-2}A(S)x\rangle
\le
\left(\frac{43}{2}+15\sqrt2\right)\|x\|_2^2.
}
\tag{L-90425.8}
\]

Moreover `A(S)` itself is boundedly invertible, with

\[
\boxed{
\left(\frac{43}{2}-15\sqrt2\right)\|x\|_2
\le\|A(S)x\|_2
\le
\left(\frac{43}{2}+15\sqrt2\right)\|x\|_2.
}
\tag{L-90425.9}
\]

Thus there is no scale-frequency escape and no badly conditioned mass matrix.

## 3. Application to dyadic prime endpoint states

For one base endpoint `X_0`, define the critically normalized dyadic sequence

\[
u_m=\frac{\mathcal H(2^mX_0)}{\sqrt{2^mX_0}}.
\tag{L-90425.10}
\]

Then

\[
\boxed{
(A(S^{-1})u)_m
 =\frac{\mathcal S_*(2^mX_0)}{\sqrt{2^mX_0}}.
}
\tag{L-90425.11}
\]

The spectral half-filter is the factor-four annular scalar

\[
\boxed{
\mathcal G(X)
 =\mathcal H(X)
  -\frac32\mathcal H(X/2)
  +\frac12\mathcal H(X/4),
}
\tag{L-90425.12}
\]

because

\[
(p(S^{-1})u)_m
 =\frac{\mathcal G(2^mX_0)}{\sqrt{2^mX_0}}.
\tag{L-90425.13}
\]

Hence the five-scale phase-locked filter is exactly the critical adjoint square of one three-scale annular difference.

In particular, an `ell^2` estimate for the filtered scalar along any complete dyadic scale packet is quantitatively equivalent, up to explicit finite collars, to the corresponding estimate for the original endpoint state.

## 4. Why this is useful and what it does not prove

The old factor-16 scalar was zero-safe but not phase locked. The new filter has:

```text
exact annular support;
uniform critical-line phase;
positive source realization;
finite-state Fejer--Riesz factorization;
strict scale coercivity.
```

Therefore a future arithmetic proof may work entirely with the compact factor-four half-filter `G` or the factor-16 source `S_*`; it loses no critical mode in returning to the original state.

Coercivity is not an arithmetic upper bound. It says that the new target is equivalent to the old critical energy, not that either is small. A proof still needs source-specific cancellation in the annular prime packet or in its reflected product Gram.

## 5. Proof boundary

Closed exactly here:

1. critical normalized polynomial;
2. Fejer--Riesz factorization;
3. exact Hilbert sequence identity;
4. explicit spectral gap;
5. bounded invertibility;
6. identification of the factor-four half-filter;
7. dyadic energy equivalence.

Open:

1. arithmetic control of `G` or `S_*`;
2. deterministic PIG or direct endpoint growth;
3. RH.