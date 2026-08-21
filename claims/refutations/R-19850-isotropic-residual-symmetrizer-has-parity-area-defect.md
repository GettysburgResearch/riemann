# R-19850 — An isotropic residual complement has an exact parity-area defect

Claim ID: `R-19850`  
Status: **PROVED SCOPE FIREWALL**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-12  
Dependencies: companion commutator formula of `L-19869`  
Scope: rules out treating an asymptotically isotropic positive complement as an automatic CCM symmetrizer  
Nonclaim: no lower bound is asserted for every anisotropic source-bound residual Gram

## 1. Statement

Let `V` be a finite-dimensional real Hilbert space.  Let `xi` be a unit vector,
let `eta` satisfy

\[
 \langle\eta,\xi\rangle=1,
 \tag{R-19850.1}
\]

and let `Lambda` be real symmetric.  Put

\[
 P=I-|\xi\rangle\langle\xi|,
 \qquad
 \alpha=P\Lambda\xi,
 \qquad
 \delta=P\eta.
 \tag{R-19850.2}
\]

Use the positive semidefinite form `Q=P`, whose kernel is exactly
`R xi`.  Its CCM commutator defect is

\[
 \mathcal E
 =P\Lambda-\Lambda P
  -|\alpha\rangle\langle\eta|
  +|\eta\rangle\langle\alpha|.
 \tag{R-19850.3}
\]

Then exactly

\[
 \boxed{
 \mathcal E
 =|\delta\rangle\langle\alpha|
  -|\alpha\rangle\langle\delta|.
 }
 \tag{R-19850.4}
\]

On the quotient `xi^perp`, where `Q=I`, one has

\[
 \boxed{
 \frac12\|\mathcal E\|_{\rm op}
 =\frac12
 \sqrt{\|\alpha\|^2\|\delta\|^2
       -\langle\alpha,\delta\rangle^2}.
 }
 \tag{R-19850.5}
\]

Thus complement positivity and an exact isolated kernel do not make the
commutator defect small.  The defect is the Euclidean area of the two vectors
`P Lambda xi` and `P eta`.

## 2. Exact algebra

Write

\[
 \mu=\langle\xi,\Lambda\xi\rangle,
 \qquad
 \Lambda\xi=\alpha+\mu\xi.
 \tag{R-19850.6}
\]

Then

\[
\begin{aligned}
 P\Lambda-\Lambda P
 &=\Lambda|\xi\rangle\langle\xi|
   -|\xi\rangle\langle\xi|\Lambda\\
 &=|\alpha\rangle\langle\xi|
   -|\xi\rangle\langle\alpha|.
\end{aligned}
 \tag{R-19850.7}
\]

Since (R-19850.1) gives

\[
 \eta=\xi+\delta,
 \tag{R-19850.8}
\]

substitution into (R-19850.3) yields

\[
\begin{aligned}
\mathcal E
&=|\alpha\rangle\langle\xi|
  -|\xi\rangle\langle\alpha|
  -|\alpha\rangle\langle\xi+\delta|
  +|\xi+\delta\rangle\langle\alpha|\\
&=|\delta\rangle\langle\alpha|
  -|\alpha\rangle\langle\delta|,
\end{aligned}
 \tag{R-19850.9}
\]

which proves (R-19850.4).

## 3. Norm of the rank-two skew form

The operator in (R-19850.4) vanishes on the orthogonal complement of
`span{alpha,delta}`.  On that two-dimensional plane its two nonzero singular
values are both

\[
 \sqrt{\|\alpha\|^2\|\delta\|^2
       -\langle\alpha,\delta\rangle^2}.
 \tag{R-19850.10}
\]

This proves (R-19850.5).

## 4. Parity specialization

Suppose an orthogonal involution `R` satisfies

\[
 R\xi=\xi,
 \qquad R\eta=\eta,
 \qquad R\Lambda R=-\Lambda.
 \tag{R-19850.11}
\]

Then `delta` is even and `alpha=P Lambda xi` is odd.  Hence

\[
 \langle\alpha,\delta\rangle=0
 \tag{R-19850.12}
\]

and

\[
 \boxed{
 \frac12\|\mathcal E\|_{\rm op}
 =\frac12\|P\Lambda\xi\|\,\|P\eta\|.
 }
 \tag{R-19850.13}
\]

This is the exact CCM parity geometry: the evaluation vector is even, the
scaling derivative of an even target is odd, and an isotropic positive
complement leaves their full area unpaid.

## 5. Consequence for the exterior-residual programme

`L-19867` proves that, after whitening by its own positive residual metric, the
finite pencil has one isolated target line and an identity complement.  That
spectral statement alone does **not** imply the approximate divided-difference
commutator required by `L-19869`.

If the whitened arithmetic metric approached the isotropic model in a topology
that also controlled the transformed scaling and evaluation vectors, then
(R-19850.13) would be the leading defect.  A successful proof must therefore
use a genuinely anisotropic source-bound complement which cancels this parity
area.  Merely improving the target/complement eigenvalue ratio cannot do so.

## 6. Exact proof boundary

- The finite formula is unconditional and exact.
- It applies directly to the isotropic projector model.
- It does not prove that the actual exterior-cardinal residual metric is
  asymptotically isotropic in the commutator topology.
- It identifies the missing obligation as a source-specific anisotropic
  commutator cancellation, not another spectral-gap estimate.
