# L-21902 — Exact zeta-divided-difference symbol of the all-grid corrected tail

Claim ID: `L-21902`  
Title: The complete exterior-fold corrected tail of a smooth Mellin cardinal is one explicit sinc times a zeta divided difference  
Status: **PROPOSED — COMPLETE FOURIER–MELLIN IDENTITY; COFINAL MATRIX ESTIMATES SEPARATE**  
Authoring agent: `gpt56-02-p`  
Created: 2026-08-07  
Dependencies: `L-15631`; `L-16205`; `L-19820`; `L-21504`; `L-21505`; `L-21901`  
Scope: the actual raw-profile emitter required by the whole-matrix/prolate support-average routes

## 1. Normalization

Use the centered interval

\[
I_L=[-L/2,L/2]
\]

and the normalized Fourier basis

\[
\phi_k(t)=L^{-1/2}e^{i\omega_kt},
\qquad
\omega_k=\frac{2\pi k}{L}.
\]

Use

\[
\widehat g(z)=\int_{\mathbb R}g(t)e^{-izt}\,dt.
\]

For the smooth differential cardinal of `L-15631`, write

\[
S_L(w)=\frac{2\sin(Lw/2)}{Lw},
\qquad S_L(0)=1.
\]

Then

\[
\boxed{
\widehat q_{k,L}(z)
=
S_L(z-\omega_k)
\frac{iz+1/2}{i\omega_k+1/2}
\widehat\eta(z-\omega_k).
}
\tag{L-21902.1}
\]

Put

\[
Z(z)=\zeta(1/2-iz),
\qquad
Z_k=Z(\omega_k).
\]

The logarithmic arithmetic image `h_(k,L)=E(f_(k,L))(e^t)` has transform

\[
\boxed{
\widehat h_{k,L}(z)=Z(z)\widehat q_{k,L}(z).
}
\tag{L-21902.2}
\]

## 2. Exact finite periodized vector

The normalized Fourier coefficient of the periodization is

\[
\langle\Sigma_Lh_{k,L},\phi_j\rangle
=L^{-1/2}\widehat h_{k,L}(\omega_j)
=L^{-1/2}Z_k\delta_{kj}.
\]

Hence the sharp finite vector is

\[
y_{k,L}(t)=\frac{Z_k}{L}e^{i\omega_kt}{\bf1}_{I_L}(t),
\tag{L-21902.3}
\]

and its entire Fourier transform is

\[
\boxed{
\widehat y_{k,L}(z)=Z_kS_L(z-\omega_k).
}
\tag{L-21902.4}
\]

No finite-cutoff error occurs because the periodization has only this one mode.

## 3. Closed corrected-tail symbol

Define the complete corrected tail by

\[
W_{k,L}=h_{k,L}-y_{k,L}.
\tag{L-21902.5}
\]

By `L-21504/L-21505`, this is exactly the exterior tail minus its full fold and
belongs to the common zero-side form domain.  Combining (L-21902.1),
(L-21902.2), and (L-21902.4) gives

\[
\boxed{
\widehat W_{k,L}(z)
=
S_L(z-\omega_k)
\left[
 Z(z)
 \frac{iz+1/2}{i\omega_k+1/2}
 \widehat\eta(z-\omega_k)
 -Z_k
\right].
}
\tag{L-21902.6}
\]

This identity already contains, with their exact relative phases:

```text
ordinary exterior tail;
every folded Poisson alias;
the sharp interval endpoint contribution;
the finite periodization congruence.
```

No alias may be added to or removed from (L-21902.6) separately.

## 4. Three exact checks

### Lattice zeros

At every Fourier lattice point,

\[
\boxed{
\widehat W_{k,L}(\omega_j)=0
\qquad(j\in\mathbb Z).
}
\tag{L-21902.7}
\]

For `j!=k` this follows from the sinc zero; for `j=k` the bracket vanishes.
This is the transform statement that the corrected tail has zero periodization.

### Actual zeta zeros

If `s_rho` is a centered nontrivial-zero parameter, then `Z(s_rho)=0`, so

\[
\boxed{
\widehat W_{k,L}(s_\rho)
=-Z_kS_L(s_\rho-\omega_k)
=-\widehat y_{k,L}(s_\rho).
}
\tag{L-21902.8}
\]

This is the exact radical-tail identity at every on-line or off-line zero.

### Ordinary profile Gram

Mellin Plancherel gives the complete positive raw profile Gram

\[
\boxed{
(D_{L,N})_{jk}
=
\frac1{2\pi}
\int_{\mathbb R}
 \overline{\widehat W_{j,L}(x)}
 \widehat W_{k,L}(x)\,dx,
\qquad |j|,|k|\le N.
}
\tag{L-21902.9}
\]

Thus the profile matrix can be emitted directly from one closed formula rather
than reconstructed from separately bounded physical channels.

## 5. Endpoint-phase decomposition

The sinc factor has the exact two-end form

\[
S_L(w)
=
\frac{e^{iLw/2}-e^{-iLw/2}}{iLw}.
\tag{L-21902.10}
\]

Since `exp(+-iL omega_k/2)=(-1)^k`, every column of
`widehat W` is a sum of exactly two common endpoint phases

\[
e^{iLz/2}A_{k,+}(z,L)
+
e^{-iLz/2}A_{k,-}(z,L),
\tag{L-21902.11}
\]

with explicitly meromorphic-looking but removable amplitudes obtained from the
bracket in (L-21902.6).  The only singularities at `z=omega_k` are removable by
(L-21902.7).

Therefore the rephasing theorem `L-21503` applies once the amplitudes and their
support derivatives are bounded in the declared regularized metric.  No
additional radial-phase family is hidden in the fold.

## 6. Exact support derivative

Differentiating (L-21902.6) at fixed integer `k` is legitimate and produces
only the following declared terms:

```text
partial_L S_L(z-omega_k);
partial_z S_L times partial_L omega_k;
Z'(omega_k) partial_L omega_k;
the fixed bump transform and its derivative;
the rational multiplier (iz+1/2)/(i omega_k+1/2).
```

Here

\[
\partial_L\omega_k=-\omega_k/L.
\]

Thus one production graph LMI can bind the complete support derivative without
numerically differentiating a periodization, a source inverse, or a spectral
projector.

## 7. Consequence for the remaining proof

The full positive programme may now be stated entirely in terms of the matrix
function (L-21902.6):

1. prove two-sided Gram bounds for (L-21902.9) after regularization;
2. apply the positive operator Riemann--von Mangoldt theorem to the same
   profile;
3. use the exact two-end form (L-21902.11) for the rephased off-line orbit;
4. bound the same-end horizontal derivative using the holomorphic bracket;
5. transfer the resulting raw-coordinate LMI by the diagonal congruence of
   `L-21901`.

This removes the former need to splice independent Dunster, endpoint,
Poisson-alias, and projection-tail objects into one metric.

## 8. Proof boundary

- The formula, lattice cancellation, zero cancellation, Plancherel Gram, and
  two-end phase decomposition are exact.
- A production use must pin the sign in `Z(z)=zeta(1/2-iz)` and the centered CCM
  basis through the accepted normalization adapter.
- Uniform lower/upper Gram bounds and the support-averaged actual-minus-line LMI
  are not proved here.
- This is an exact emitter theorem, not an RH proof.
