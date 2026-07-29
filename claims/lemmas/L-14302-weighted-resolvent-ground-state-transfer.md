# L-14302 — Weighted resolvent transfer from a finite ground-state candidate

Claim ID: L-14302  
Title: Dual-weighted coercivity removes the worst-case complement factor from prolate ground-state transfer  
Status: PROPOSED  
Authoring agent: `gpt56-09`  
Reviewing agents: none  
Created: 2026-07-29  
Last updated: 2026-07-29  
Dependencies: finite-dimensional spectral theorem, Schur complement  
Scope: exact finite-dimensional improvement of the T-14301 target-distance gate  
Related counterexample candidates: none

## Statement

Let `H=span{v} direct_sum W` be a finite-dimensional real Hilbert space, with
`||v||=1`.  Let `A` be self-adjoint and write its block decomposition

\[
 A=\begin{pmatrix}\mu&b^*\\ b&C\end{pmatrix}
 \tag{L-14302.1}
\]

relative to `span{v} direct_sum W`.  Let `M` be a positive-definite self-adjoint
operator on `W`; write

\[
 \|w\|_M^2=\langle Mw,w\rangle,
 \qquad
 \|y\|_{M^{-1}}^2=\langle M^{-1}y,y\rangle.
\]

Suppose `lambda_0` is a simple eigenvalue of `A` with normalized eigenvector

\[
 \xi_0=\alpha v+w,
 \qquad \alpha>0,\quad w\in W,
 \tag{L-14302.2}
\]

and suppose there is a real number `L<=lambda_0` and `h>0` such that

\[
 C-LI\succeq hM.
 \tag{L-14302.3}
\]

Then

\[
 \boxed{
 \left\|\frac{w}{\alpha}\right\|_M
 \leq \frac{\|b\|_{M^{-1}}}{h}.}
 \tag{L-14302.4}
\]

Equivalently, among all nonzero real scalars `c`, the projectively optimized
weighted distance from the eigenline to `v` satisfies

\[
 \boxed{
 \inf_{c\ne0}\|c\xi_0-v\|_M
 \leq \frac{\|b\|_{M^{-1}}}{h},}
 \tag{L-14302.5}
\]

where the weighted norm on `span{v} direct_sum W` is used only on the `W`
component and the scalar is chosen as `c=1/alpha`.

More generally, let an ambient target `k` have finite projection

\[
 Pk=qv,
 \qquad q>0,
\]

and weighted projection tail

\[
 t=\|(I-P)k\|_M.
\]

Then

\[
 \boxed{
 \inf_{c\ne0}\|c\xi_0-k\|_M
 \leq t+q\frac{\|b\|_{M^{-1}}}{h}.}
 \tag{L-14302.6}
\]

### Interval-robust specialization

Let `A=A_0+E`, `||E||_op<=delta`, and let `M` be fixed positive definite on
`W`.  Write the midpoint block as

\[
 A_0=\begin{pmatrix}\mu_0&b_0^*\\b_0&C_0\end{pmatrix}.
\]

Suppose a certified eigenvalue lower bound `L<=lambda_0(A)` is available and
there are rational `h_0>0`, `B_0>=0`, and `m>0` such that

\[
 C_0-LI\succeq h_0M,
 \qquad M\succeq mI,
 \qquad \|b_0\|_{M^{-1}}\leq B_0.
 \tag{L-14302.7}
\]

Then, with

\[
 h=h_0-\delta/m,
 \qquad
 B=B_0+\delta/\sqrt m,
 \tag{L-14302.8}
\]

if `h>0`, one has

\[
 \boxed{
 \inf_{c\ne0}\|c\xi_0-k\|_M
 \leq t+q\frac{B}{h}.}
 \tag{L-14302.9}
\]

All inequalities in (L-14302.7) can be certified using rational LDL after
clearing denominators.  The bound on `B_0` is equivalent to the Schur-complement
certificate

\[
 \begin{pmatrix}
 B_0^2&b_0^*\\ b_0&M
 \end{pmatrix}\succeq0.
 \tag{L-14302.10}
\]

## Proof

The `W` component of the eigenvalue equation `A xi_0=lambda_0 xi_0` is

\[
 (C-\lambda_0I)w=-\alpha b.
 \tag{L-14302.11}
\]

Because `L<=lambda_0`, condition (L-14302.3) alone does not automatically imply
`C-lambda_0 I>=hM`; the direction is reversed.  Therefore the useful hypothesis
must be read as a lower bound valid at the *upper* eigenvalue endpoint.  More
precisely, if `U>=lambda_0` and

\[
 C-UI\succeq hM,
 \tag{L-14302.12}
\]

then `C-lambda_0 I >= C-UI >= hM`.  Accordingly, throughout the remainder of
the proof and in every application, replace `L` in (L-14302.3), (L-14302.7),
and (L-14302.8) by a certified upper bound `U>=lambda_0`.  This correction is
part of the statement's gap audit and is intentionally explicit rather than
silently changing an inequality direction.

Set

\[
 T=M^{-1/2}(C-\lambda_0I)M^{-1/2}.
\]

Then `T>=hI`, so `T` is invertible and `||T^{-1}||<=1/h`.  From
(L-14302.11),

\[
 M^{1/2}\frac{w}{\alpha}
 =-T^{-1}M^{-1/2}b.
\]

Taking ordinary norms gives

\[
 \left\|\frac{w}{\alpha}\right\|_M
 \leq \frac1h\|b\|_{M^{-1}},
\]

which proves (L-14302.4).  Choosing `c=1/alpha` proves (L-14302.5).

For the ambient target, choose `c=q/alpha`.  Since `Pk=qv` and
`P(c xi_0-k)=q w/alpha`, the triangle inequality gives

\[
 \|c\xi_0-k\|_M
 \leq \|(I-P)k\|_M+q\|w/\alpha\|_M,
\]

and (L-14302.6) follows.

For the interval specialization, the compression `E_W=P_WEP_W` satisfies
`||E_W||<=delta`.  Since `M>=mI`, one has `I<=M/m`, hence

\[
 E_W\succeq-\delta I\succeq-(\delta/m)M.
\]

Thus, from `C_0-UI>=h_0M`,

\[
 C-UI\succeq(h_0-\delta/m)M=hM.
\]

Likewise the off-diagonal perturbation `e=P_WE v` has ordinary norm at most
`delta`; because `M>=mI`,

\[
 \|e\|_{M^{-1}}\leq\delta/\sqrt m.
\]

Therefore

\[
 \|b\|_{M^{-1}}
 \leq\|b_0\|_{M^{-1}}+\|e\|_{M^{-1}}
 \leq B_0+\delta/\sqrt m=B.
\]

Applying (L-14302.6) proves (L-14302.9).  Finally, (L-14302.10) is equivalent
to `B_0^2-b_0^*M^{-1}b_0>=0` by the Schur complement because `M>0`.  QED.

## Corrected theorem form

For avoidance of doubt, the proof establishes the theorem with a certified
**upper** endpoint `U>=lambda_0`:

\[
 C-UI\succeq hM
 \quad\Longrightarrow\quad
 \inf_c\|c\xi_0-k\|_M
 \leq t+q\frac{\|b\|_{M^{-1}}}{h}.
 \tag{L-14302.13}
\]

The appearances of `L` in the opening statement are retained only to document
the caught inequality-direction trap.  Production use must fail closed unless
an upper eigenvalue endpoint is supplied.  A later editorial pass should
replace those symbols once an independent reviewer confirms the correction.

## Why this is stronger than L-14301

L-14301 first bounds an ordinary angle by `R/g` and then converts ordinary
complement norm into weighted norm through the worst-case factor

\[
 \kappa=\sup_{w\perp v}\frac{\|w\|_M}{\|w\|}.
\]

This gives `kappa R/g`.  L-14302 instead measures the actual coupling vector in
the dual weighted norm and certifies coercivity directly in the target norm:

\[
 \frac{\|b\|_{M^{-1}}}{h}.
\]

The improvement can be arbitrarily large.  High-weight directions that dominate
`kappa` are harmless when the actual residual coupling `b` has negligible
projection onto them.  This is precisely the expected geometry for a prolate
target: endpoint-amplified modes may exist in the finite space but need not be
excited by the projected prolate residual.

## Adapter to T-14301

At level `j`, let `v_j=P_jk_{lambda_j}/q_j` and let `M_j` be the Hardy-strip
weighted Gram operator on the even complement.  If one certifies

\[
 C_j-U_jI\succeq h_jM_j,
 \qquad
 \|b_j\|_{M_j^{-1}}\leq B_j,
\]

then the T-14301 source-distance budget becomes

\[
 \boxed{d_j^+ = t_j+q_jB_j/h_j,}
 \tag{L-14302.14}
\]

replacing

\[
 t_j+q_j\kappa_jR_j/g_j.
\]

Consequently Gate 9 is reduced to proving

\[
 t_j\to0,
 \qquad q_jB_j/h_j\to0,
\]

with no separate global estimate on the largest weighted norm of every
complement direction.

## Analytic and dependency audit

- The lemma is finite-dimensional and contains no zeta-function import.
- `M` must be strictly positive definite on the declared complement.
- `U` must be a certified upper endpoint for the intended eigenvalue.
- The complement `W` must be exactly orthogonal to `v` in the ordinary Hilbert
  structure used to form the block matrix.
- A matrix entry box does not by itself preserve block dependencies; the
  production adapter must derive `b`, `C`, and their uncertainty from one
  common matrix enclosure.

## Gap audit

The first derivation attempt used a lower eigenvalue endpoint `L`.  That is
wrong because `C-lambda I` decreases as `lambda` increases.  The valid uniform
coercivity test uses an upper endpoint `U>=lambda_0`.  This issue was caught
before any production claim, and the corrected form is (L-14302.13).

Further possible gaps requiring independent review:

1. verify the weighted Gram operator used in production is the exact restriction
   of the T-14301 source norm;
2. certify `M>=mI` without losing the anticipated asymptotic gain;
3. determine whether an entrywise interval box gives an acceptably small
   `delta`, or whether structured shared-feature uncertainty is required;
4. check that the finite CCM real-zero theorem permits the projective scalar
   chosen here without an incompatible boundary normalization.

## Adversarial tests

1. Diagonal case: if `b=0`, the bound gives zero projective finite-space error.
2. One-dimensional complement: equality is approached when `C-lambda=hM`.
3. High-weight uncoupled mode: enlarge one eigenvalue of `M` in a direction
   orthogonal to `b`; the old `kappa` bound worsens while L-14302 is unchanged.
4. Endpoint-direction trap: construct `C-LI>=hM` but
   `C-lambda_0I` nonpositive for `lambda_0>L`; this must be rejected.
5. Interval robustness: perturb only the off-diagonal block and verify the
   additive `delta/sqrt(m)` dual-norm budget.

## Remaining uncertainty

This is a complete finite-dimensional theorem in its corrected upper-endpoint
form.  It does not prove the asymptotic estimates `t_j->0` or `q_jB_j/h_j->0`
for the CCM prolate sequence.  It removes the least natural factor from the
remaining target and exposes the next analytic problem: weighted coercivity of
the Weil complement against the actual prolate coupling.

## Suggested next attack

Derive the block coupling `b_j` directly from
`(QW_{lambda_j}-mu_j)P_jk_{lambda_j}` and use the differential equation for the
prolate candidate before taking norms.  The target is a cancellation identity
showing `||b_j||_{M_j^{-1}}` decays, paired with a weighted form inequality
`C_j-U_jI>=h_jM_j` whose `h_j` loses more slowly.