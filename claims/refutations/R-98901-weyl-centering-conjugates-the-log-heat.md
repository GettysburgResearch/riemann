# R-98901 — Weyl centering conjugates the log heat and does not remove the pole carrier

Claim ID: `R-98901`  
Status: **PROVED EXACT CCR COUNTERIDENTITY TO THE PUBLISHED PROOF STEP**  
Created: 2026-08-18  
RH status: **not assumed**

Let `h` be the one-particle logarithmic operator and let

\[
\mathsf A=d\Gamma(h)
\]

be its bosonic second quantization.  For every Weyl displacement `W(f)` in the
finite-cutoff Fock space, the CCR give

\[
\boxed{
W(f)^*\mathsf A W(f)
=\mathsf A+a^*(hf)+a(hf)+\langle f,hf\rangle.
}
\tag{R-98901.1}
\]

Therefore

\[
\boxed{
W(f)^*e^{-\mathsf A^2/(4T)}W(f)
=
\exp\!\left[-\frac{(
\mathsf A+a^*(hf)+a(hf)+\langle f,hf\rangle)^2}{4T}
\right],
}
\tag{R-98901.2}
\]

not `e^{-A^2/(4T)}`.

For the exact finite generalized-prime realization of the fractional packet,
one must take, up to the harmless finite dyadic normalization,

\[
f_q=\sqrt{\theta\lambda_\diamond(q)}\,q^{-1/4}.
\]

Indeed the unnormalised exponential vector `varepsilon(f)` satisfies

\[
\langle\varepsilon(f),
\Pi e^{-\mathsf A^2/(4T)}e^{-i\tau\mathsf A}
\varepsilon(f)\rangle
=
\sum_n\frac{b_\theta(n)}{\sqrt n}
 e^{-(\log n)^2/(4T)}e^{-i\tau\log n}.
\]

At cutoff `R`, `||f||^2=theta sum_(q<=R) lambda(q)/sqrt(q)` grows without
bound as the prime cutoff is removed.  The heat makes the final signed matrix
coefficient convergent for each fixed `T`, but the unheated coherent vectors do
not have a bounded-norm infinite-Fock limit.

Thus the `L-98703` step that removes the pole carrier by a Weyl translation and
then estimates with the original free heat omits the exact field terms in
(R-98901.2).  Together with `R-98900`, a correct centered formula must retain
both

```text
the compensated parity observable W(2f) Pi;
the conjugated heat containing a*(hf)+a(hf).
```

These terms contain the carrier that was claimed to have been removed.  No
bound of the form `L-98703.1` follows from unitarity or the unshifted Tao Gram.
This refutes the published proof mechanism, not the abstract possibility of a
different heat estimate.
