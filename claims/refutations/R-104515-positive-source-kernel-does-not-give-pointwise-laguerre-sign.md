# R-104515 — A nonnegative source kernel does not imply pointwise Laguerre positivity

Claim ID: `R-104515`  
Status: **EXACT MECHANISM FIREWALL**  
Created: 2026-08-23  
RH status: **unproved**

`L-104528` proves that the target Laguerre expression is the Fourier transform
of a nonnegative kernel.  That fact alone cannot establish its pointwise sign.

Take the positive even measure

\[
d\mu={1\over2}(\delta_{-1}+\delta_{1}).
\]

Its Fourier transform is

\[
\widehat\mu(t)=\cos t,
\]

which is negative on every interval

\[
\frac\pi2+2\pi j<t<\frac{3\pi}2+2\pi j.
\]

Equivalently, a Fourier transform of a positive measure is positive definite,
but positive-definite functions need not be pointwise nonnegative.
Smooth positive even approximations to `mu` retain negative Fourier values, so
the obstruction is not an artifact of atoms.

Therefore none of the following is sufficient for `LAG2XI104550`:

```text
mathcal K_2(x)>=0;
positive definiteness of mathcal L_2;
positive Gaussian averages of mathcal L_2;
a finite collection of positive Laguerre samples.
```

The needed theorem is positive definiteness of `mathcal K_2` itself, or an
independent proof that its Fourier transform is nonnegative.
