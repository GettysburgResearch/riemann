# R-106513 — Positive source and a real odd derivative do not transfer real zeros

Claim ID: `R-106513`  
Status: **PROVED EXACT SOURCE-FAITHFUL COUNTEREXAMPLE**  
Created: 2026-08-25  
RH status: **unproved**

Fix

\[
0<a<1
\]

and put

\[
F(t)=1+a\cos t.
\]

## 1. Every diagonal source hypothesis survives

`F` has the positive even Fourier measure

\[
\Phi=\delta_0+{a\over2}(\delta_{1}+\delta_{-1}).
\]

Thus all exterior-square and cross-current positivity statements of
`L-106500` apply after the standard finite-measure regularization.

For `K=5`,

\[
F'=-a\sin t,
\qquad
F^{(5)}=-a\sin t,
\qquad
F^{(6)}=-a\cos t.
\]

Hence

\[
\boxed{
\mathcal L_5
=F'F^{(5)}-FF^{(6)}
=a^2+a\cos t.
}
\tag{R-106513.1}

Its Fourier coefficients are

\[
a^2,
\qquad {a\over2},
\qquad {a\over2},
\]

and are all nonnegative, exactly as predicted by the odd-current hierarchy.
The all-order current completion is likewise positive.

## 2. The zero transfer fails maximally

Because `0<a<1`,

\[
F(t)>0
\]

for every real `t`.  Thus `F` has no real zero.

By contrast,

\[
F^{(5)}(t)=-a\sin t
\]

has only real simple zeros, two per period.  On a union of complete periods,

```text
base real-zero count:             0;
fifth-derivative real-zero count: maximal;
positive fifth Wronskian source:  exact;
positive cross-current hierarchy: exact.
```

The endpoint winding therefore records the complete failure of descent even
though every diagonal source sign is favorable.

Moreover (R-106513.1) is not pointwise positive when `cos t<-a`; a
nonnegative Fourier density is positive definite, not a pointwise Laguerre
inequality.

## 3. Binding consequence

No theorem may infer a real-zero percentage from the conjunction

```text
positive even Fourier source;
positive odd-endpoint exterior-square density;
positive all-order cross current;
high or complete real-root proportion for F^(5).
```

A noncommuting/oriented phase theorem is indispensable.  For Xi this is
precisely the open canonical-correlation, outer-covariant residue, or sharp
all-pass Hankel estimate isolated in `T-106530`.
