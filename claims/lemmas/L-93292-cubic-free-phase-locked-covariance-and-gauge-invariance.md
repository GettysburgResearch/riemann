# L-93292 — The phase-locked covariance is cubic-free and invariant under safe-line preconditioning

Claim ID: `L-93292`  
Status: **EXACT UNCONDITIONAL TRANSFORM THEOREM**  
Created: 2026-08-18  
Depends on: `L-93280--L-93282` at PR #546  
RH status: **not assumed**

Use the Fourier convention

\[
 \widehat f(\xi)=\int_\mathbb R f(r)e^{-i\xi r}\,dr.
\tag{L-93292.1}
\]

PR #546 gives

\[
 \widehat{\mathcal G}_C(\xi,t)
 =\widehat W_C(1+i\xi)Z(\xi-t)
\tag{L-93292.2}
\]

and

\[
 \widehat B_{q,m}(\xi)
 =\frac{P(\xi+i/2)^{2m}\widehat h_q(\xi+i/2)}
 {\widehat W_C(1-i\xi)}.
\tag{L-93292.3}
\]

For the signed covariance

\[
 \mathfrak C_{q,m}(t)
 =\int_\mathbb R B_{q,m}(r)\mathcal G_C(r,t)\,dr,
\tag{L-93292.4}
\]

Parseval without conjugation gives

\[
 \mathfrak C_{q,m}(t)
 =\frac1{2\pi}\int_\mathbb R
 \widehat B_{q,m}(-\xi)
 \widehat{\mathcal G}_C(\xi,t)\,d\xi.
\tag{L-93292.5}
\]

The centered-cubic multiplier cancels exactly. Thus

\[
\boxed{
 \mathfrak C_{q,m}(t)
 =\frac1{2\pi}\int_\mathbb R
 K_{q,m}(\xi)Z(\xi-t)\,d\xi,
}
\tag{L-93292.6}
\]

where

\[
\boxed{
 K_{q,m}(\xi)
 =P(-\xi+i/2)^{2m}\widehat h_q(-\xi+i/2).
}
\tag{L-93292.7}
\]

The quotient poles in the synthesis and the safe-line zeros in the field have
fully disappeared. The actual arithmetic object is a phase-locked Gaussian
convolution of the pole-subtracted safe-line logarithmic derivative.

## Gauge invariance

More generally, let `M(xi)` be any fixed multiplier which is nonzero on the
safe line and for which both modified factors remain in the legal `L2` classes.
Replace

\[
 \widehat{\mathcal G}_C\mapsto
 M(\xi)\widehat{\mathcal G}_C,
\qquad
 \widehat B(-\xi)\mapsto
 \frac{\widehat B(-\xi)}{M(\xi)}.
\tag{L-93292.8}
\]

Then the covariance is unchanged pointwise:

\[
\boxed{
 \int B_M(r)\mathcal G_M(r,t)\,dr
 =\mathfrak C_{q,m}(t).
}
\tag{L-93292.9}
\]

Hence fixed zero-safe Peano banks, passive scale preconditioners, and invertible
safe-line smoothing kernels are coordinate choices for `SCID_PL`; they cannot
alter its signed scalar unless they change the arithmetic source or the
consumer itself.
