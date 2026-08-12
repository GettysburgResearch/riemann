# O-19854 — Three-front resolution portfolio after the vertical-defect audit

Claim ID: `O-19854`  
Status: **RESEARCH SYNTHESIS — NEW LEMMAS REMAIN SUBJECT TO INDEPENDENT REVIEW**  
Created: 2026-08-12  
RH status: **unproved**

## 1. Why three fronts

The positive residual/vertical-defect route on PR #202 has reduced its complete
conclusion to a source-bound derivative-intertwining estimate.  That estimate
is exact but remains RH-strength.  To avoid repeatedly optimizing the same
finite symmetrizer, this continuation pursued three structurally independent
mechanisms:

1. a fixed-scale completed Jordan/Suzuki first-chaos colligation;
2. a theta/Brownian positive-bulk Dirichlet-to-Neumann construction;
3. a finite factor-54 parity reset in the elementary endpoint/carry programme.

No route is declared proved through to RH.

## 2. Front A — fixed Suzuki colligation

On PR #400, `L-91301` identifies the exact model-space tangent leakage for the
safe inner family

\[
 \Theta_a(z)=\frac{\xi(1/2-a-iz)}{\xi(1/2+a-iz)}.
\]

If `P_a` projects onto `K_(Theta_a)`, then

\[
 -P_a\partial_{\log a}^2P_aP_a
 =2\mathcal B_a^*\mathcal B_a,
\]

with the canonical first-chaos feature

\[
 \mathcal J_a=\sqrt2\,M_{a\partial_a\Theta_a}^*P_a.
\]

`L-91305` proves a data-processing theorem.  If the whole safe inner family is
the compression of one fixed source colligation

\[
 M_{\Theta_a}=CV_a,
\]

where `C` is independent of `a` and `V_a` is isometric, then the output shape is
the contracted source-normal tangent and

\[
 (N_a^H)^*N_a^H\preceq(N_a^S)^*N_a^S.
\]

The source-minus-output defect has the explicit positive feature

\[
 f\longmapsto
 \binom{(I-C^*C)^{1/2}N_a^Sf}{Q_aCN_a^Sf}.
\]

Thus the exact remaining construction is one fixed first-chaos/Stinespring lift
of Suzuki's radial family whose source normal curvature is the Jordan plus
gamma/pole curvature.  Independent amplitude realizations at each scale do not
suffice.

## 3. Front B — theta/Brownian boundary system

On PR #401, `L-91302` proves

\[
 \Psi(v)=4B''(v)-\frac14B(v),
 \qquad
 B'(0)=-\frac18,
\]

and the one-port Green identity

\[
 2M(q)=\frac12+\left(q^2-\frac14\right)
       \int_0^\infty B(v)\cosh(qv/2)dv.
\]

The exact state is two-channel:

\[
 x_q(v)=\sqrt{2(1/4-q^2)B(v)}
 \binom{\cosh(qv/4)}{\sinh(qv/4)},
\]

and

\[
 \|x_q\|^2=1-4M(q).
\]

The BPY Gamma/Beta reservoir admits the hyperbolic coordinates

\[
 S=\frac12\log(A^2-D^2)+\log(\pi/2),
 \qquad
 \Delta=\operatorname{artanh}(D/A),
\]

and its complete local carré du champ acts only in the positive direction

\[
 \partial_\Delta-	anh\Delta\partial_S.
\]

`L-91304` analytically continues the two-channel state to the unit disk and
proves the strict Schur bound

\[
 \sup_{z\in D}\|\mathbf x(z)\|^2
 \le\frac{\pi e^{-\pi}}6<\frac1{32}.
\]

Nevertheless its prescribed symmetric scalar completion is exactly Xi:

\[
 1-[\mathbf x(z),\mathbf x(z)]=4M(z/2).
\]

Thus generic Schur completion is not enough.  The remaining theorem is an exact
Brownian/theta DtN identity realizing this **particular** Xi scalar port as the
boundary energy of the positive beta/theta bulk.

## 4. Front C — factor-54 reset

This is currently the most finite and operational front.

PR #399 already proves:

```text
positive equality and reserve states on 1 <= x <= 54.219...;
33-state squarefree parity shadows;
a 16-prime finite automaton;
positive martingale B-spline quantization;
a coefficientwise-positive quantization collar;
a conditional coefficient-one reset -> RH theorem.
```

`L-91303` sharpens the finite-versus-continuum transfer.  Uniformly for
`n>=X/55`,

\[
 b_X^\star(n)
 =\sqrt X\,\mathscr B^\star(n/X)
 +\frac1{2\sqrt X}\mathscr D(n/X)
 +O(X^{-3/2}),
\]

where

\[
 \mathscr D(\theta)
 =\theta^{-1/2}
  \sum_{k\le1/\theta}\frac{\mu(k)}{\sqrt k}
  \log\frac1{k\theta}.
\]

Consequently the finite reset splice obeys

\[
 K_X=c_0X+O(1),
\]

rather than requiring an `epsilon X` retreat.  The corrected seed remainder
causes only `O(X^-1)` relative interior carry loss.

The endpoint inverse of the first Euler correction is explicit:

\[
 \mathcal E\mathscr D(1/x)
 =\frac x2\sum_{k\le x}\frac{\mu(k)}{\sqrt k}
 [3\log(x/k)+5],
\]

with reciprocal-knot atoms `mu(N)/sqrt(N)`.  Every unsigned coefficient is
positive, so the correction lives in the same even/odd parity states as the
original reset.  Its total normalized mass is `O(1/X)` and is absorbed by the
fixed Hall margin `>0.11` for all sufficiently large `X`.

The remaining reset gate is now strictly finite:

> lift the robust 33-state parity transport and the bounded terminal quotient
> collars through the three-consecutive-integer divisor stencils, preserving
> endpoint nonnegativity and coefficient-one transfer of the `(L,R)` state.

All continuum error, splice drift, bulk quantization score and interior carry
loss are already paid.

## 5. Ranking

### First: factor-54 reset

This has the smallest remaining interface: a finite carry/capacity lift repeated
self-similarly.  It does not require analytic continuation through an unknown
zero set.

### Second: fixed Suzuki colligation

This has the cleanest operator target: construct one fixed first-chaos lifting
and invoke exact curvature data processing.  The missing lift must preserve the
whole radial family, not one scale at a time.

### Third: theta/Brownian DtN

This has the richest explicit positive bulk and probability structure.  It now
has a strict Schur state and one exact beta tangent direction, but the prescribed
Xi scalar port remains the conclusion-bearing boundary identification.

## 6. Exact status

```text
three independent attacks pursued                YES
new exact operator identities                    YES
new finite reset asymptotics                      YES
factor-54 finite collar lift                      OPEN
fixed first-chaos Suzuki lift                     OPEN
Brownian/theta Xi-port DtN identity               OPEN
Riemann Hypothesis                                UNPROVED
```
