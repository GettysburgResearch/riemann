# L-15102 — Radical localization and exact tail-leakage residual

Claim ID: `L-15102`  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-10`  
Created: 2026-07-30  
Last updated: 2026-07-30  
Dependencies: elementary Hermitian-form algebra, min--max principle, and the weighted Schur--Ritz argument of audited `L-14302`  
Scope: convert the positive route's ambient residual into a boundary-tail functional  
Related counterexample candidates: none

## 1. Abstract radical decomposition identity

Let `K` be a real or complex Hilbert space and let `q` be a Hermitian
sesquilinear form on a linear domain `D`. Let

\[
 r\in\operatorname{Rad}(q),
 \qquad
 q(r,f)=0\quad(f\in D).
 \tag{L-15102.1}
\]

Take **any** exact decomposition

\[
 \boxed{r=p+t,\qquad p,t\in D.}
 \tag{L-15102.2}
\]

No orthogonal-projection hypothesis is required. Then, for every `w in D`,

\[
 \boxed{q(p,w)=-q(t,w).}
 \tag{L-15102.3}
\]

Moreover,

\[
 \boxed{
 q(p,p)=q(t,t)=-q(p,t)=-q(t,p).}
 \tag{L-15102.4}
\]

The equality is exact and does not assume positivity of `q`.

### Proof

Since `r=p+t` is in the radical,

\[
 0=q(r,w)=q(p,w)+q(t,w),
\]

which gives (L-15102.3). Taking `w=p` and `w=t` gives

\[
 q(t,p)=-q(p,p),
 \qquad
 q(p,t)=-q(t,t).
\]

Hermitian symmetry and the reality of diagonal form values imply
`q(p,p)=q(t,t)`, proving (L-15102.4). QED.

This stronger formulation is important in production: a smooth compact
localization `p=chi r` is generally not an orthogonal projection of `r`, but it
is still an exact decomposition with `t=(1-chi)r`.

## 2. The constrained localized residual is pure leakage

Let `K_loc` be a closed local subspace containing `p`, and assume the restriction
of `q` to a local form domain

\[
 D_{loc}\subset D\cap K_{loc}
\]

is closed and lower bounded, with self-adjoint representative `A_loc`. Suppose
`p` belongs to the local operator domain and put

\[
 \mu_p=\frac{q(p,p)}{\|p\|^2}.
 \tag{L-15102.5}
\]

Then, for every local `w in D_loc` with `w perpendicular p`,

\[
 \boxed{
 \langle(A_{loc}-\mu_pI)p,w\rangle
 =q(p,w)
 =-q(t,w).}
 \tag{L-15102.6}
\]

Thus the component of the localized eigen-residual transverse to the target
line is not an unexplained interior defect. It is exactly the form interaction
with the discarded global-radical tail.

When `p` is only in the form domain, (L-15102.6) remains valid as a form-dual
identity and should be used in that form rather than asserting an operator
residual.

## 3. Weighted leakage norm

Let `Gamma` be a self-adjoint involution commuting with the local form and let
`p` be even. Let `W_+` be the even local form domain orthogonal to `p`, and let
`||.||_M` be any Hilbert norm on `W_+`.

Define the exact leakage dual norm

\[
 \boxed{
 \mathcal L_{q,M}(t;p)
 :=\sup_{0\ne w\in W_+}
   \frac{|q(t,w)|}{\|w\|_M}.}
 \tag{L-15102.7}
\]

By (L-15102.3), this is also the dual norm of the transverse localized residual
of `p`.

## 4. Continuum Schur--Ritz transfer

Assume the local operator has compact resolvent. Let

\[
 U\ge\mu_p,
 \qquad h>0,
 \qquad g_->0,
 \tag{L-15102.8}
\]

and suppose

\[
 q(w,w)-U\|w\|^2\ge h\|w\|_M^2
 \quad(w\in W_+),
 \tag{L-15102.9}
\]

while every odd form-domain vector obeys

\[
 q(w,w)-U\|w\|^2\ge g_-\|w\|^2.
 \tag{L-15102.10}
\]

Then the global local ground eigenvalue is simple, its eigenvector is even, and
for a suitable nonzero real scalar `c`,

\[
 \boxed{
 \|c\xi_0-p\|_M
 \le\frac{\mathcal L_{q,M}(t;p)}{h}.}
 \tag{L-15102.11}
\]

### Proof

The compression to `p^perp` lies strictly above `U`, while the Rayleigh value of
`p` is at most `U`. The min--max principle gives a unique ground line, and the
odd lower bound forces that line to be even.

Put `v=p/||p||` and write the normalized ground vector as

\[
 \xi_0=\alpha v+w,
 \qquad
 \alpha>0,
 \qquad
 w\in W_+.
\]

The complement component of the eigenvalue equation is

\[
 (C_+-\lambda_0I)w=-\alpha b,
\]

where the complement functional is

\[
 b(z)=q(v,z)=-\frac{q(t,z)}{\|p\|}.
\]

Since `lambda_0<=U`, (L-15102.9) gives the same weighted inverse bound as
`L-14302`:

\[
 \left\|\frac w\alpha\right\|_M
 \le\frac{\|b\|_{M^*}}h
 =\frac{\mathcal L_{q,M}(t;p)}{h\|p\|}.
\]

Taking `c=||p||/alpha` proves (L-15102.11). QED.

## 5. Application to the exact Hermite target

Let `k=E(h)` be the exact radical target of `L-15101`. Let `chi_lambda` be a
smooth inversion-even multiplier supported in `[lambda^-1,lambda]`, and put

\[
 p_\lambda=\chi_\lambda k,
 \qquad
 t_\lambda=(1-\chi_\lambda)k.
 \tag{L-15102.12}
\]

Whenever the semilocal Weil form is the exact restriction of the global form on
the declared common domain, the complete positive-route numerator is

\[
 \boxed{
 \mathcal L_{QW,M}(t_\lambda;p_\lambda),}
 \tag{L-15102.13}
\]

not the ambient prolate eigen-defect appearing in `L-14307`.

The target tail itself is super-Gaussian by `L-15101`. Therefore any proved
continuity estimate

\[
 |QW(t_\lambda,w)|
 \le C_\lambda\|t_\lambda\|_{X_\lambda}\|w\|_M
 \tag{L-15102.14}
\]

reduces the spectral approximation problem to

\[
 \boxed{
 \frac{C_\lambda\|t_\lambda\|_{X_\lambda}}{h_\lambda}
 \longrightarrow0.}
 \tag{L-15102.15}
\]

This is the exact place where an arithmetic trace-form estimate and a continuum
ground-gap estimate must enter.

## Why this is a real narrowing

`L-14307` correctly proves that Fourier-cutoff refinement cannot remove a
nonzero ambient prolate defect. `L-15102` avoids that obstruction by starting
from a vector in the exact **global** radical. Its localized residual is forced
to be a boundary effect.

This still does not prove that the boundary effect is small relative to the
localized spectral gap. It identifies the missing estimate without conflating
it with finite-section error.

## Gap audit

- The identity requires the global radical vector, its localized part, and its
  tail to belong to the common form domain. A production proof must verify
  smooth-cutoff stability in the exact Connes/Suzuki normalization.
- A small diagonal value `q(p,p)=q(t,t)` is not enough: the full dual leakage
  norm controls the angle to the ground line.
- The coercivity `h` is a complement bound relative to the selected weighted
  norm, not merely the ordinary first spectral gap.
- If several localized near-radical directions coexist, `h` may collapse. That
  possibility is the remaining structural obstruction, not a numerical error.
