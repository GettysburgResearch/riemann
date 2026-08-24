# R-105610 — A positive Fourier source does not remove the physical all-pass phase

Claim ID: `R-105610`  
Status: **PROVED EXACT COUNTERMODEL / BINDING FIREWALL**  
Created: 2026-08-24  
Depends on: `L-105613`  
RH status: **not assumed**

## 1. Countermodel

Take the positive finite Fourier source

\[
F(z)=1+{1\over2}\cos z.
\tag{R-105610.1}
\]

Its Fourier coefficients are nonnegative. Consequently the exterior-square
identity of `L-105613` gives a nonnegative Fourier density for

\[
\mathcal T_F=F'^2-FF''.
\]

Nevertheless `F` has nonreal zeros. At

\[
z=\pi+i\log2,
\]
one has

\[
\cosh(\log2)={5\over4},
\qquad
\sinh(\log2)={3\over4},
\]

and therefore

\[
F(z)={3\over8},
\qquad
F'(z)={3i\over8},
\qquad
{F(z)\over F'(z)}=-i.
\tag{R-105610.2}
\]

Moreover

\[
F''(z)={5\over8},
\qquad
\mathcal T_F(z)=-{3\over8},
\qquad
m'(z)={8\over3}.
\tag{R-105610.3}
\]

Thus the differential microscope is

\[
\boxed{
\mathcal C_F(\pi,\log2)
={1\over2}
\left({8\log2\over3}+1\right)>0.
}
\tag{R-105610.4}
\]

The desired sign fails despite the positive Fourier source.

## 2. Meaning

The failure occurs through the physical factor

\[
{\overline{F'(z)}\over F'(z)}
\]

in the exact factorization `L-105613.4`. Positive source density does not fix
its orientation after analytic translation.

Likewise, the exact positive Laplace coefficients of `L-105610` do not imply a
pointwise sign after all translation phases have been collapsed. They supply a
one-sided operator reserve, not a source-blind scalar positivity theorem.

## 3. Binding consequence

The following shortcuts are invalid:

```text
positive reciprocal coefficients -> pointwise microscope sign;
positive Turan Fourier density    -> pointwise microscope sign;
finite positive Fourier model     -> Xi base descent;
```

A valid proof must retain either:

```text
one-sided source ownership and its strict phase gap;
denominator-whitened actual-frame control;
or topology-safe H^(1/2) shell energy.
```

The countermodel does not refute those source-sensitive routes.