# L-14301 — Residual and parity-gap certification of an even ground state

Claim ID: L-14301  
Title: Robust residual/gap certificate for a unique simple even finite ground state  
Status: PROPOSED  
Authoring agent: `gpt56-09`  
Reviewing agents: none  
Created: 2026-07-29  
Last updated: 2026-07-29  
Dependencies: finite-dimensional spectral theorem and Cauchy interlacing  
Scope: exact and interval finite-matrix certification  
Related counterexample candidates: none

## Statement

Let `H` be a finite-dimensional real Hilbert space with `dim H>=2`.  Let
`Gamma` be a self-adjoint involution and write

\[
 H=H_+\oplus H_-,
 \qquad H_\pm=\ker(\Gamma\mp I).
\]

Let `A_0` and `A` be real self-adjoint operators commuting with `Gamma`, and
suppose

\[
 A=A_0+E,
 \qquad \|E\|_{\rm op}\leq\delta.
 \tag{L-14301.1}
\]

Choose a unit vector `v in H_+` and define

\[
 \mu_0=\langle A_0v,v\rangle,
 \qquad r_0=(A_0-\mu_0 I)v,
 \qquad \rho_0=\|r_0\|.
 \tag{L-14301.2}
\]

Assume there are positive numbers `g_+^0,g_-^0` such that

\[
 \begin{aligned}
 \langle A_0w,w\rangle
   &\geq(\mu_0+g_+^0)\|w\|^2,
   &&w\in H_+\cap v^\perp,\\
 \langle A_0w,w\rangle
   &\geq(\mu_0+g_-^0)\|w\|^2,
   &&w\in H_-.
 \end{aligned}
 \tag{L-14301.3}
\]

An inequality over the zero subspace is understood vacuously.  Put

\[
 g_+=g_+^0-2\delta,
 \qquad g_-=g_-^0-2\delta,
 \qquad R=\rho_0+2\delta,
 \tag{L-14301.4}
\]

and assume `g_+>0` and `g_->0`.

Then `A` has a unique global lowest eigenvalue `lambda_0`.  It is simple and
its normalized eigenvector `xi_0` lies in `H_+`.  Choose the sign so that
`<xi_0,v>>=0`.  Then

\[
 \mu_0-\delta-\frac{R^2}{g_+}
 \leq\lambda_0\leq\mu_0+\delta,
 \tag{L-14301.5}
\]

\[
 \lambda_1-\lambda_0\geq\min(g_+,g_-),
 \tag{L-14301.6}
\]

where `lambda_1` is the next eigenvalue counted with multiplicity, and

\[
 \tan\angle(v,\xi_0)\leq\frac{R}{g_+},
 \qquad
 \|v-\xi_0\|\leq\sqrt2\frac{R}{g_+}.
 \tag{L-14301.7}
\]

### Exact-matrix specialization

For `delta=0`, equations (L-14301.5)–(L-14301.7) become

\[
 \mu_0-\frac{\rho_0^2}{g_+^0}\leq\lambda_0\leq\mu_0,
 \qquad
 \tan\angle(v,\xi_0)\leq\frac{\rho_0}{g_+^0}.
 \tag{L-14301.8}
\]

### Projective target corollary

Let the finite space `H` be embedded isometrically in an ambient Hilbert space
`K`, let `P:K->H` be the orthogonal projection, let `k in K` be a nonzero
target vector, and suppose

\[
 p=Pk=qv,
 \qquad q=\|p\|>0.
\]

Then

\[
 \inf_{c\neq0}\|c\xi_0-k\|
 \leq
 \|(I-P)k\|+q\frac{R}{g_+}.
 \tag{L-14301.9}
\]

This improves the bound obtained by merely sign-aligning two unit vectors:
the free scalar is used to match the entire component along `v` exactly.

### Weighted projective corollary

Let `||.||_M` be any Hilbert norm on the ambient target space `K`.  Suppose its
restriction to the finite space satisfies

\[
 \|w\|_M\leq\kappa\|w\|
 \qquad (w\in H_+\cap v^\perp).
 \tag{L-14301.10}
\]

If a target `k` satisfies `p=qv` as above and

\[
 \|k-p\|_M\leq t,
\]

then

\[
 \inf_{c\neq0}\|c\xi_0-k\|_M
 \leq t+q\kappa\frac{R}{g_+}.
 \tag{L-14301.11}
\]

For T-14301, `||.||_M` is the ambient weighted `L2` norm induced by the
positive multiplication operator with multiplier
`u^(2 tau)+u^(-2 tau)`; `G_M` below is its Gram matrix after restriction to
the finite Fourier space.

## Why this lemma matters

The finite real-zero theorem imported by T-14301 requires the *global* lowest
eigenvalue of the truncated Weil matrix to be simple and even.  A numerical
eigensolver restricted to the even sector does not certify either globality or
simplicity.  L-14301 reduces both facts, and the projective distance to the
explicit prolate candidate, to finite objects:

1. one approximate even vector;
2. its residual;
3. a lower bound on the rest of the even sector;
4. a lower bound on the entire odd sector;
5. for the strongest Hardy-strip gate, one weighted complement factor.

All five survive rational freezing and interval uncertainty.

## Proof

### 1. Transfer midpoint information to the exact matrix

Let

\[
 \mu=\langle Av,v\rangle,
 \qquad r=(A-\mu I)v.
\]

From `||E||<=delta`,

\[
 |\mu-\mu_0|=|\langle Ev,v\rangle|\leq\delta.
 \tag{L-14301.12}
\]

Moreover,

\[
 r=r_0+Ev-\langle Ev,v\rangle v,
\]

so

\[
 \|r\|\leq\rho_0+\delta+\delta=R.
 \tag{L-14301.13}
\]

For a unit vector `w in H_+ intersect v^perp`,

\[
 \langle Aw,w\rangle
 \geq\mu_0+g_+^0-\delta
 \geq\mu+g_+^0-2\delta
 =\mu+g_+.
 \tag{L-14301.14}
\]

The same argument on `H_-` gives

\[
 A|_{H_-}\geq(\mu+g_-)I.
 \tag{L-14301.15}
\]

### 2. Interlacing proves global simple-even ground-state status

Because `A` commutes with `Gamma`, it is block diagonal on
`H_+\oplus H_-`.  In the even decomposition

\[
 H_+=\mathbb Rv\oplus(H_+\cap v^\perp),
\]

write

\[
 A_+=
 \begin{pmatrix}
 \mu & b^*\\
 b & C
 \end{pmatrix},
 \qquad \|b\|=\|r\|,
 \qquad C\geq(\mu+g_+)I.
 \tag{L-14301.16}
\]

The smallest even eigenvalue is at most `mu` by the Rayleigh principle.
Cauchy interlacing applied to the principal compression `C` shows that the
second even eigenvalue, when present, is at least `mu+g_+`.  Every odd
eigenvalue is at least `mu+g_-` by (L-14301.15).  Since `dim H>=2`, at least
one of those two competing sectors is nonzero.  Hence the global ground
eigenvalue is the first even eigenvalue, is simple, and the rest of the
spectrum is at least `min(g_+,g_-)` above it.  This proves (L-14301.6) and the
qualitative claim.

### 3. Schur complement bounds the eigenvalue and eigenvector

Let the normalized ground eigenvector be

\[
 \xi_0=\alpha v+w,
 \qquad w\in H_+\cap v^\perp,
 \qquad \alpha\geq0.
\]

If `H_+ intersect v^perp` is the zero subspace, parity invariance forces
`r=0`, the even ground vector is exactly `v`, and all estimates below are
immediate.  Assume henceforth that the complement is nonzero.  Then one has
`alpha>0`, since otherwise `lambda_0` would be an eigenvalue of `C` and hence
exceed `mu`.  The second block row of the eigenvalue equation gives

\[
 w=-(C-\lambda_0 I)^{-1}b\,\alpha.
 \tag{L-14301.17}
\]

Since `lambda_0<=mu`,

\[
 C-\lambda_0I\geq g_+I.
\]

Consequently

\[
 \frac{\|w\|}{\alpha}
 \leq\frac{\|b\|}{g_+}
 \leq\frac{R}{g_+},
 \tag{L-14301.18}
\]

which is the tangent bound.  The first block row and (L-14301.17) give

\[
 \mu-\lambda_0
 =\langle b,(C-\lambda_0I)^{-1}b\rangle
 \leq\frac{\|b\|^2}{g_+}
 \leq\frac{R^2}{g_+}.
 \tag{L-14301.19}
\]

Combine this with (L-14301.12) to obtain (L-14301.5).

If `theta=angle(v,xi_0) in [0,pi/2]`, then

\[
 \|v-\xi_0\|=2\sin(\theta/2)
 \leq\sqrt2\sin\theta
 \leq\sqrt2\tan\theta,
\]

which proves (L-14301.7).

### 4. Projective target bounds

Write `xi_0=alpha v+w` as above and choose

\[
 c=q/\alpha.
\]

Then

\[
 c\xi_0-p=(q/\alpha)w,
\]

and therefore

\[
 \|c\xi_0-p\|=q\tan\angle(v,\xi_0)
 \leq qR/g_+.
\]

The triangle inequality with `k-p` proves (L-14301.9).

Under (L-14301.10), the same calculation gives

\[
 \|c\xi_0-p\|_M
 \leq(q/\alpha)\kappa\|w\|
 =q\kappa\tan\angle(v,\xi_0)
 \leq q\kappa R/g_+,
\]

and the `M`-norm triangle inequality proves (L-14301.11).  QED.

## Exact finite certificate form

Let the columns of `B_+` be any rational basis of
`H_+ intersect v^perp`, and let the columns of `B_-` be a rational basis of
`H_-`.  The strict rational matrix inequalities

\[
 B_+^T(A_0-(\mu_0+g_+^0)I)B_+\succ0,
 \qquad
 B_-^T(A_0-(\mu_0+g_-^0)I)B_-\succ0
 \tag{L-14301.20}
\]

imply (L-14301.3).  Exact LDL pivots therefore provide compact proof objects.
The bases need not be orthonormal.

For the rational Gram matrix `G_M` of the restricted ambient `M`-norm in an
orthonormal coordinate basis of `H`, a rational number `kappa>0` satisfies
(L-14301.10) whenever

\[
 B_+^T(\kappa^2I-G_M)B_+\succeq0.
 \tag{L-14301.21}
\]

A strict inequality is a convenient fail-closed certificate; equality can be
handled by choosing a slightly larger rational `kappa`.

If the exact matrix is enclosed entrywise by rational intervals with midpoint
`A_0` and radius matrix `R=(r_ij)`, symmetry gives the rigorous operator bound

\[
 \|A-A_0\|_{\rm op}
 \leq\max_i\sum_j r_{ij}.
 \tag{L-14301.22}
\]

This is the uncertainty adapter implemented by X-14301.

## Analytic domain audit

This is finite real linear algebra.  No zeta function, contour, branch, or
limit appears in the lemma.  Application to RH requires a separate proof that
the enclosed matrix is the exact truncated Weil matrix in the normalization
used by the finite real-zero theorem, and that the weighted Gram matrix is the
claimed source norm.

## Dependency audit

- The Rayleigh principle and spectral theorem are used for the parity blocks.
- Cauchy interlacing is used only to place the second even eigenvalue above the
  complement floor.
- The Schur-complement identity is derived explicitly in
  (L-14301.17)–(L-14301.19).
- The interval radius in (L-14301.22) uses
  `||E||_2 <= sqrt(||E||_1 ||E||_infinity)` and symmetry.

## Gap audit

- An even-sector eigensolve alone does not bound the odd sector.
- A small residual without a complement gap does not identify which
  eigenvector is nearby.
- The effective gaps lose `2 delta`, not `delta`: one `delta` moves the sector
  floor and another can move the candidate Rayleigh value.
- Entrywise interval boxes do not by themselves prove that the exact matrix
  commutes with parity.  Exact parity is an external analytic/provenance gate.
- The lower eigenvalue enclosure uses the *even* gap, because the residual is
  even.  The odd gap is needed for globality, not for the angle estimate.
- The weighted corollary requires a rigorous weighted tail and complement
  factor.  Replacing either by an ordinary floating overlap restores the large
  endpoint penalty that T-14301 was designed to avoid.

## Adversarial tests

1. Set `g_-<=0`: an unseen odd eigenvector may be the true ground state.
2. Keep the residual fixed while sending `g_+` to zero: the angle bound must
   diverge.
3. Use a basis that misses one even-complement direction: positive LDL pivots
   then prove only a restricted statement.
4. Widen every matrix entry until `2 delta>=g_+^0`: the robust conclusion must
   fail closed.
5. Take `r_0=0`: the candidate is an exact even eigenvector, but the two sector
   gaps are still needed to prove it is the unique global ground state.
6. Understate `kappa` in (L-14301.21): the weighted projective gate must reject
   even when every unweighted gate passes.

## Verification

`experiments/X-14301-prolate-ground-certificate/verify.py` implements the
rational certificate form, including basis dimension/rank checks, parity,
strict exact LDL, entrywise-to-operator uncertainty, residual inflation, the
reported eigenvalue/angle bounds, and an optional exact weighted projective
gate.  Its nontrivial synthetic example has midpoint residual `1/10`, even gap
`1`, odd gap `2`, exact ground-eigenvalue enclosure `[-1/100,0]`, and weighted
target-line-distance bound `31/100`.

## Remaining uncertainty

The lemma itself is elementary and its proof is complete, but it remains
`PROPOSED` until independent review.  No production truncated-Weil matrix has
yet been passed through the checker.

## Suggested next attack

Add a proof-grade matrix adapter that reads directed Arb/MPFR entry boxes from
the finite Guinand–Weil implementation, verifies their source digest and exact
parity formula, and emits the basis/gap and weighted-Gram certificates consumed
by X-14301.
