# L-15301 — Energy-gap transfer for a frozen finite ground line

Claim ID: `L-15301`  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-10-b`  
Created: 2026-07-31  
Dependencies: finite-dimensional spectral theorem; the coercivity setup of `L-14302`  
Scope: finite self-adjoint matrices; no Riemann-specific input

## Statement

Let `H` be a finite-dimensional real or complex Hilbert space, let

\[
A=A^*:H\to H,
\]

and let `v` be a unit vector. Write

\[
H=\mathbf C v\oplus W,
\qquad
A=
\begin{pmatrix}
\mu & b^*\\
b & C
\end{pmatrix}
\tag{L-15301.1}
\]

relative to this decomposition, where

\[
\mu=\langle Av,v\rangle,
\quad
b=P_WAv,
\quad
C=P_WA|_W.
\]

Let `M` be positive definite on `W`. Suppose that exact real numbers `U` and
`h` satisfy

\[
U\ge \mu,
\qquad
h>0,
\qquad
C-UI\succeq hM.
\tag{L-15301.2}
\]

Assume that the lowest eigenvalue `lambda_0` of `A` is simple and that its
normalized eigenvector has nonzero overlap with `v`. Choose its phase so that

\[
\xi_0=\alpha(v+y),
\qquad
\alpha>0,
\qquad
y\in W.
\tag{L-15301.3}
\]

Then

\[
\boxed{
\|y\|_M^2
\le
\frac{\mu-\lambda_0}{h}.}
\tag{L-15301.4}
\]

Consequently, every rigorous lower endpoint

\[
L\le\lambda_0
\tag{L-15301.5}
\]

gives the fully finite certificate

\[
\boxed{
\left\|
\frac{\xi_0}{\langle\xi_0,v\rangle}-v
\right\|_M
\le
\sqrt{\frac{\mu-L}{h}}.}
\tag{L-15301.6}
\]

In particular, if `A` is certified positive semidefinite, one may take `L=0`:

\[
\boxed{
\left\|
\frac{\xi_0}{\langle\xi_0,v\rangle}-v
\right\|_M
\le
\sqrt{\frac{\mu}{h}}.}
\tag{L-15301.7}
\]

### Unnormalized target form

Let `p=qv`, with `q>0`, and let `k` be an ambient target satisfying `Pk=p`,
where `P` is the ordinary projection onto `H`. Put

\[
t=\|k-p\|_M.
\]

Then the explicit scalar `c=q/alpha` obeys

\[
\boxed{
\|c\xi_0-k\|_M
\le
t+q\sqrt{\frac{\mu-L}{h}}.}
\tag{L-15301.8}
\]

## Proof

The `W` component of the eigenvalue equation is

\[
(C-\lambda_0 I)y=-b.
\tag{L-15301.9}
\]

The `v` component is

\[
\mu+\langle b,y\rangle=\lambda_0.
\tag{L-15301.10}
\]

Taking the inner product of (L-15301.9) with `y` and using
(L-15301.10) gives the exact energy identity

\[
\boxed{
\mu-\lambda_0
=
\langle(C-\lambda_0 I)y,y\rangle.}
\tag{L-15301.11}
\]

Since the Rayleigh principle gives `lambda_0<=mu<=U`,

\[
C-\lambda_0I
\succeq
C-UI
\succeq
hM.
\]

Combining this with (L-15301.11) proves (L-15301.4). Replacing
`lambda_0` by a rigorous lower endpoint `L` proves (L-15301.6).

For the target form, `c xi_0=p+qy`, hence

\[
c\xi_0-k=qy-(k-p).
\]

The triangle inequality and (L-15301.6) prove (L-15301.8). QED.

## Strict comparison with the residual certificate

The residual bound in `L-14302` is

\[
\|y\|_M
\le
\frac{\|b\|_{M^{-1}}}{h}.
\tag{L-15301.12}
\]

The energy-gap estimate is never worse when the exact ground value is used.
Indeed, put

\[
T=M^{-1/2}(C-\lambda_0I)M^{-1/2}\succeq hI,
\qquad
z=M^{1/2}y.
\]

Then

\[
\mu-\lambda_0=\langle Tz,z\rangle,
\qquad
\|b\|_{M^{-1}}^2=\langle T^2z,z\rangle.
\]

Since `T^2>=hT`,

\[
\boxed{
\frac{\mu-\lambda_0}{h}
\le
\frac{\|b\|_{M^{-1}}^2}{h^2}.}
\tag{L-15301.13}
\]

Thus the new theorem replaces a **linear residual/coercivity ratio** by a
**square-root Rayleigh-energy/coercivity ratio**.

## Why this matters for the positive RH route

The previous bottleneck was

\[
\frac{B_{\lambda,N,\tau}}{h_{\lambda,N,\tau}}\to0,
\qquad
B=\|b\|_{M^{-1}}.
\]

`L-15301` shows that this is sufficient but not necessary. A lower ground-state
bound permits the weaker condition

\[
\frac{\mu_{\lambda,N}-L_{\lambda,N}}
     {h_{\lambda,N,\tau}}
\to0.
\]

When the finite Weil matrix is positive semidefinite, this reduces to

\[
\frac{\mu_{\lambda,N}}{h_{\lambda,N,\tau}}	o0.
\]

This is the natural interface for a relative prolate comparison: the numerator
is a target **energy**, while the denominator is the first complementary
**energy scale**.

## Exact certificate interface

A proof object need contain only:

1. an exact target vector `p` and its ordinary squared norm;
2. a rational midpoint matrix plus a rigorous operator-radius enclosure for `A`;
3. an exact rational basis of the target-orthogonal complement;
4. a directed rational upper Hardy Gram on that complement;
5. exact LDL certificates for the complement coercivity and odd-sector gates;
6. a rigorous lower endpoint `L` for the global ground eigenvalue;
7. a rigorous upper endpoint for the target Rayleigh quotient.

No inverse Hardy Gram and no residual vector are required by the final bound.

## Gap audit

- A lower endpoint `L` is indispensable. A midpoint eigenvalue is not a lower
  spectral certificate.
- Positive semidefiniteness is enough for `L=0`; strict positivity is not
  required for the estimate.
- The complement gate must use the same Hardy normalization as the final target
  distance.
- The theorem does not itself prove the simple-even hypotheses. Those may be
  supplied by the full `L-14302` even/odd coercivity gates.
- This lemma is finite linear algebra. It does not compare the Weil and prolate
  operators and does not imply RH by itself.
