# L-14308 — Block Temple–Schur lower floor from squared residuals

Claim ID: `L-14308`  
Title: A finite near-radical block gives a rigorous ambient spectral floor through a squared-residual Schur correction  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-09-b`  
Created: 2026-07-30  
Dependencies: elementary completion of squares; finite-dimensional Schur complements; audited `L-14302` for the prior distance-oriented interface  
Scope: self-adjoint lower bounds; finite or closed-form implementations of localized Weil operators  
Related counterexample candidates: none

## Statement

Let `H = S ⊕ E` be an orthogonal decomposition of a Hilbert space, with `S`
finite-dimensional.  Relative to this decomposition let a lower-bounded
self-adjoint operator, or its closed quadratic form, have block representation

\[
 A=\begin{pmatrix}B&R^*\\R&C\end{pmatrix}.
 \tag{L-14308.1}
\]

Let `M` be strictly positive on `E`.  Suppose there are real numbers
`gamma` and `h>0` such that, on the form domain in `E`,

\[
 C-\gamma I_E\succeq hM.
 \tag{L-14308.2}
\]

Assume the cross map is continuous into the `M`-dual, so that
`R^*M^{-1}R` is a finite operator on `S`.  Define

\[
 K:=B-h^{-1}R^*M^{-1}R.
 \tag{L-14308.3}
\]

Then

\[
 \boxed{
 \inf\sigma(A)\ge
 \min\bigl\{\gamma,\lambda_{\min}(K)\bigr\}.}
 \tag{L-14308.4}
\]

This is an ambient lower bound.  The subspace `S` need not contain an exact
eigenvector, and the lowest eigenvalue need not be simple or even.

### Directed midpoint adapter

Let `A_0` be a rigorously represented operator for which the hypotheses above
hold and suppose an independent analytic gate proves

\[
 \|A-A_0\|_{\mathrm{op}}\le\delta.
 \tag{L-14308.5}
\]

Then

\[
 \boxed{
 \inf\sigma(A)\ge
 \min\bigl\{\gamma,\lambda_{\min}(K_0)\bigr\}-\delta.}
 \tag{L-14308.6}
\]

The same conclusion holds for a form perturbation with a certified relative
bound translated into an absolute lower-floor loss.

## Proof

For `x∈S` and `y∈E`, (L-14308.2) gives

\[
\begin{aligned}
 \langle A(x+y),x+y\rangle
 &\ge \langle Bx,x\rangle
   +2\Re\langle Rx,y\rangle
   +\gamma\|y\|^2+h\langle My,y\rangle.
\end{aligned}
\]

Complete the square in the `M` geometry:

\[
\begin{aligned}
 h\langle My,y\rangle+2\Re\langle Rx,y\rangle
 ={}&h\left\|M^{1/2}y+h^{-1}M^{-1/2}Rx\right\|^2\\
 &-h^{-1}\langle R^*M^{-1}Rx,x\rangle.
\end{aligned}
\]

Hence

\[
 \langle A(x+y),x+y\rangle
 \ge \langle Kx,x\rangle+\gamma\|y\|^2.
 \tag{L-14308.7}
\]

The right side is at least

\[
 \min\{\gamma,\lambda_{\min}(K)\}
 (\|x\|^2+\|y\|^2),
\]

which proves (L-14308.4).  Equation (L-14308.6) follows from the elementary
operator perturbation inequality

\[
 \inf\sigma(A)\ge\inf\sigma(A_0)-\|A-A_0\|.
\]

QED.

## Scalar Temple corollary

Take `S=span{p}` and put

\[
 e=p/\|p\|,\qquad
 \rho=\langle Ae,e\rangle,\qquad
 z=(A-\rho)p.
\]

Then `z⊥p`, and if

\[
 C-\gamma I\succeq hM,
\]

one obtains

\[
 \boxed{
 \inf\sigma(A)\ge
 \min\left\{\gamma,
 \rho-\frac{\|z\|_{M^{-1}}^2}{h\|p\|^2}
 \right\}.}
 \tag{L-14308.8}
\]

When `gamma≥rho`, this is the familiar Temple-type form

\[
 \inf\sigma(A)\ge
 \rho-\frac{\|z\|_{M^{-1}}^2}{h\|p\|^2}.
 \tag{L-14308.9}
\]

The error is **quadratic** in the residual.

## Strict weakening of target-to-ground convergence

The distance-oriented estimate in audited `L-14302` naturally asks for

\[
 \frac{\|z\|_{M^{-1}}}{h\|p\|}\longrightarrow0.
 \tag{L-14308.10}
\]

The spectral-floor estimate asks only for

\[
 \frac{\|z\|_{M^{-1}}^2}{h\|p\|^2}\longrightarrow0.
 \tag{L-14308.11}
\]

These conditions are genuinely different.  If, along a sequence,

\[
 \|z\|_{M^{-1}}/\|p\|\asymp h\asymp\varepsilon\to0,
\]

then the projective distance ratio in (L-14308.10) stays of order one, while
the energy loss in (L-14308.11) is of order `epsilon` and vanishes.

Thus a proof of a lower spectral floor can succeed even when the proposed
prolate vector does not converge to an individual ground eigenvector.

## Why the block form matters for the CCM program

The localized Weil form exhibits several numerically tiny modes, not merely one.
A scalar Temple bound can become useless when the second eigenvalue is also
small.  L-14308 permits

\[
 S_\lambda=\operatorname{span}\{\text{all certified prolate near-radical modes}\},
\]

so that spectral crowding is handled exactly inside the small matrix `B`, while
only the genuinely high complement must satisfy (L-14308.2).  The corrected
low matrix

\[
 B-h^{-1}R^*M^{-1}R
\]

is then the complete finite object to certify.

This is a lower-bound interface, unlike ordinary Rayleigh–Ritz or conforming
finite-element eigenvalues, which supply upper bounds for the ambient lowest
eigenvalue.

## Proof-producing certificate

A finite exact certificate may contain:

1. rational Hermitian matrices `B`, `R`, `C`, and `M`;
2. rational `gamma`, `h>0`, and a proposed rational floor `F`;
3. exact positive `LDL*` pivots for `M`;
4. exact positive pivots for `C-gamma I-hM`;
5. an exact solve of `MX=R` and the matrix
   `K=B-h^{-1}R*X`;
6. exact positive pivots for `K-FI` and the comparison `gamma≥F`;
7. if the blocks are enclosures of an ambient operator, a separately proved
   operator/form radius `delta`, giving final floor `F-delta`.

`X-14304` implements this finite trust boundary with integers and
`fractions.Fraction` only.

## Gap audit

- A lower bound for a finite compression is **not** automatically a lower bound
  for the ambient operator.  The omitted Fourier/finite-element complement must
  be included in (L-14308.2) or charged through (L-14308.5).
- Positive Ritz values alone do not verify this lemma.
- The matrix `M` must be genuinely positive on the complete complement used in
  the certificate.
- An empirical estimate of `h` is not a proof of complement coercivity.
- For an unbounded operator, all vectors and cross functionals must lie in the
  declared form domains.
- This lemma is a sufficient lower-bound theorem, not a proof that the required
  CCM estimates hold.

## Adversarial checks

1. Omitting the Schur correction is false even in dimension two.
2. Replacing the squared residual by a signed midpoint residual is unsafe.
3. If a second near-zero mode is left in `E`, the certified `h` may collapse;
   putting all such modes in `S` repairs the interface.
4. A finite positive matrix can coexist with a negative omitted complement.
5. The scaling `residual≈h≈epsilon` separates the new energy condition from the
   old eigenvector-distance condition exactly.
