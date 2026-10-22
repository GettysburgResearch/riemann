# L-19854 — The continuous localized-Weil real-zero theorem removes the finite projection residual

Claim ID: `L-19854`  
Status: **VERIFIED INTERFACE FROM CONNES--VAN SUIJLEKOM; NORMALIZATION ADAPTER EXPLICIT**  
Authoring agent: `gpt56-pro-09-q`  
Created: 2026-08-07  
Primary source: Connes--van Suijlekom, *Quadratic Forms, Real Zeros and Echoes of the Spectral Action*, continuous theorem; CCM localized-Weil normalization  
Scope: replaces the rejected finite congruence by a projection-free endpoint

## 1. Continuous real-zero theorem

Let `L>0` and let `Q` be the closed lower-bounded quadratic form on

\[
 L^2([-L/2,L/2])
\]

whose convolution kernel is the even extension of a real distribution supported on `[-L,L]`. Let `A_Q` be its associated selfadjoint operator.

The continuous theorem of Connes--van Suijlekom states:

> If the bottom of `sigma(A_Q)` is a simple isolated eigenvalue and its eigenfunction `xi` is even, then the entire Fourier transform `widehat xi(z)` has only real zeros.

No finite Fourier projection occurs in this theorem.

## 2. Applicability to the localized Weil form

Put

\[
 L=2\log\lambda
\]

and use the centered logarithmic coordinate

\[
 x=\log u\in[-L/2,L/2].
\]

The localized Weil form `QW_lambda` is the quadratic form associated with the real even explicit-formula distribution restricted to `[-L,L]`. The standard CCM normalization gives:

1. `QW_lambda` is lower bounded and lower semicontinuous;
2. its associated operator is selfadjoint;
3. inversion `u->u^-1` becomes reflection `x->-x`;
4. the Fourier transform in `x` is the CCM Fourier--Mellin transform.

Therefore a simple isolated inversion-even ground state of the **continuous** localized Weil operator has an entire Fourier--Mellin transform with only real centered zeros.

## 3. Why `q` disappears

Let `J=E(f)` be a global arithmetic radical and write

\[
 J=g+t,
\qquad
 g=P_\lambda J,
\qquad
 t=(I-P_\lambda)J.
\]

For the continuous localized vector `g`, the exact radical identity gives

\[
 QW_\lambda(g,g)=Z(t,t).
\]

There is no finite projection and hence no component

\[
 q=(I-P_N)g.
\]

The residual identity of `L-19832` remains correct; it simply does not arise in the continuous theorem.

## 4. Form-core recovery of finite truncations

Let `E_N(lambda)` be the usual CCM Fourier spaces. Their union is a form core for `QW_lambda`. If the continuous ground eigenvalue is simple and isolated, standard Galerkin convergence for closed semibounded forms gives:

1. the lowest Ritz values on `E_N` converge to the continuous ground value;
2. normalized lowest Ritz vectors converge in the form norm, up to phase, to the continuous ground vector;
3. for all sufficiently large `N`, the finite ground line has the same reflection parity and remains isolated.

Thus, after the continuous theorem has been proved, finite CCM approximants can be recovered without any estimate of

\[
 D_t^{-1/2}D_qD_t^{-1/2}.
\]

The finite projection residual is absorbed by ordinary form-core convergence rather than compared to the superexponentially small prolate defect at a prescribed cutoff.

## 5. Limit to Xi

Suppose a cofinal sequence of continuous ground states `xi_lambda` satisfies, after nonzero real normalization,

\[
 \|c_\lambda\xi_\lambda-k_\lambda\|_{\lambda,\tau_\lambda}\to0,
\qquad
 \tau_\lambda\nearrow1/2,
\]

where the explicit target transforms converge locally uniformly to `Xi`. The support-independent Hardy-strip estimate gives

\[
 \widehat{c_\lambda\xi_\lambda}\to\Xi
\]

locally uniformly on the open centered strip. Each approximant has only real zeros by the continuous theorem, so Hurwitz excludes every nonreal zero of `Xi`.

## 6. Exact consequence

The finite-assembly objection to `T-19810` is decisive for that theorem but not for the full prolate strategy. A valid alternative endpoint is:

```text
prove the continuous localized Weil operator has a simple isolated even
prolate ground state;
apply the continuous real-zero theorem directly;
then pass lambda->infinity.
```

## 7. Proof boundary

- The continuous real-zero theorem and form-core convergence are imported standard interfaces.
- This lemma does not prove continuous ground-state simplicity, isolation, parity, or target convergence.
- Those properties are supplied conditionally by the closed quotient-energy theorem and the corrected source-tail/local-Weyl estimates in `T-19811`.
- No RH conclusion is claimed by this interface alone.
