# Full-problem attack: whole-matrix diagonal lower envelope

Agent: `gpt56-pro-09-n`  
Date: 2026-08-07  
PR: #202  
Classification: new global positive architecture and two analytic lemmas; **RH not claimed proved**

## Executive result

This pass deliberately stepped away from the latest one-scalar and one-soft-block
obstructions and compared the strongest global mechanisms in the repository.

The central conclusion is that the positive program has been imposing two
unnecessary requirements:

1. identify and control one finite ground eigenvector;
2. prove a complete infinite-complement floor at every fixed support.

A diagonal proof of Weil positivity needs neither.  It is enough to prove

\[
 A_j\succeq-\rho_jG_j,
 \qquad \rho_j\to0,
\]

for the **whole finite Weil matrix** on a rapidly densifying sequence of
expanding Fourier spaces.  Compact Gevrey tests are approximated so strongly
that the finite inequalities pass directly to the global Weil form.  Weil's
criterion then gives RH.

Three new files implement the attack:

```text
L-19818  rank-one Bessel support large sieve
L-19819  subexponential smooth Mellin-cardinal source frame
T-19807  whole-matrix diagonal lower-envelope theorem
```

## 1. The rank-one saving

The support-average work in `L-16226/L-15627` uses Hilbert--Schmidt operator
coefficients.  A zero contribution is not generic: it is rank one,

\[
 u_\gamma\otimes v_\gamma^*.
\]

Charging both factors by the same pointwise source envelope would square the
conditioning loss before the large sieve and can destroy the power budget.

`L-19818` proves a sharper theorem.  Control one profile factor pointwise and
sum the other through its positive line-centered Bessel Gram.  For a packet of
dimension `d_T`, vector envelope `M_T`, zero density `O(log T)` per unit bin,
and Bessel energy `E_T=O(T log T)`,

\[
 {1\over T}\int_T^{2T}\|Z_T(R)\|_{\rm op}^2dR
 \ll {d_TM_T^2(\log T)^3\over T}.
\]

The result pays `M_T^2`, not `M_T^4`.

For the regularized smooth source frame,

\[
 d_T=T^{o(1)},
 \qquad M_T=T^{3/8+o(1)},
\]

so the right side is

\[
 T^{-1/4+o(1)}.
\]

This restores a genuine power reserve for the complete frame.

## 2. The cutoff need not be quadratic-logarithmic

`L-15631` was written for `N=O(L^2)`.  The exact differential-cardinal algebra
works at any finite cutoff.  `L-19819` chooses

\[
 H_L=\exp(L^\theta),
 \qquad
 N_L\asymp L\exp(L^\theta),
 \qquad 0<\theta<1/2.
\]

The dimension is still `R^(o(1))` for `R=e^L`.

A measure deletion over the support length avoids the ordinates of every zeta
zero at all required grid points.  Riemann--von Mangoldt gives deleted measure
`o(1)`.  A local zeta product then gives

\[
 \max_k|\zeta(1/2+i\omega_k)|^{-1}
 +\max_k|\partial_L\zeta(1/2+i\omega_k)^{-1}|
 =R^{o(1)}.
\]

Consequently the exact smooth source inverse, including support derivatives,
has graph size

\[
 M_R=R^{1/4+o(1)}.
\]

The frame is large enough to approximate compact Gevrey tests with an error

\[
 \exp\{-c\exp(L^\theta/s)\},
\]

which dominates every support-side exponential constant in the explicit
formula.

## 3. Direct finite-to-global theorem

`T-19807` proves:

> If the exact whole finite matrices on these expanding spaces satisfy
> \(A_j\succeq-\rho_jG_j\) with \(\rho_j\to0\), then RH follows.

The proof approximates compact Gevrey functions by their finite Fourier series,
passes the lower bounds to the exact global Weil form, then uses density and
Weil's criterion.

This avoids:

```text
finite ground-state simplicity/parity;
finite-to-Xi Hurwitz convergence;
ambient complement coercivity at fixed support;
hard/soft packet splitting;
visible-block positivity as a separate theorem;
one finite eigenvalue being positive.
```

The matrices may remain slightly negative at every level.

## 4. One full-matrix LMI is enough

Let `D_R` be the positive line-centered profile Gram and

\[
 \widehat D_R=D_R+\tau_RG_R,
 \qquad
 \tau_R=R^{-1/4+o(1)}.
\]

If the line-centered and horizontal-displacement estimates give

\[
 A_R^0\succeq
 [\log R-C-\alpha_R]D_R-\alpha_R\tau_RG_R
\]

and

\[
 -\delta_R\widehat D_R
 \preceq A_R-A_R^0
 \preceq\delta_R\widehat D_R,
\]

with

\[
 \alpha_R+\delta_R=o(\log R),
 \qquad
 (\alpha_R+\delta_R)\tau_R\to0,
\]

then directly

\[
 A_R\succeq-\rho_RG_R,
 \qquad
 \rho_R=(\alpha_R+\delta_R)\tau_R\to0.
\]

The rank-one large sieve supplies a selected-support estimate

\[
 \delta_R=R^{-1/8+o(1)},
\]

so its contribution to the final floor is

\[
 \delta_R\tau_R=R^{-3/8+o(1)}.
\]

There is no need to export a soft projector or to solve a harmonic Schur problem
for the global implication.

## 5. Relationship to the existing repository routes

### PR #150

The independently reviewed finite-real-zero/Hurwitz implication remains valid,
but the new theorem does not require its simple-even ground-state gate or target
convergence.

### PR #152/#155/#159

Their block-Schur, symbol-complement, and certified-zero split results remain
useful finite diagnostics.  They are no longer logically mandatory for a full
proof if the whole-matrix LMI can be produced on a dense diagonal.

### PR #163

Its smooth Mellin source, regularized frame, and support-averaged profile ideas
are the closest producer machinery.  The new rank-one theorem supplies the
missing one-factor saving and the new cutoff supplies diagonal density.

### PR #164

Its endpoint/Poisson ledgers, radial normalization, local-Weyl estimates, and
support-phase separation are natural ingredients for the line-centered and
phase interfaces.  The new theorem uses them on the entire finite matrix rather
than only on a prescribed prolate ground sector.

## 6. Exact remaining interfaces

The route is not yet a proof of RH.  It has three source-specific gates.

1. **Finite matrix/source identity.**  Bind the periodized smooth source frame,
   restriction convention, endpoint terms, and zero-side profile matrix to the
   exact finite CCM/Weil matrix in one normalization.
2. **Line-centered Bessel local-Weyl estimate.**  Produce the positive main
   profile and Bessel upper bound on the complete `R^(o(1))` frame.
3. **Complete phase ledger.**  Put every actual-minus-line-centered term into a
   rank-one phase family, an Airy window, or an explicit endpoint/Poisson
   remainder.

These are concrete structural identities and estimates.  None asks for the sign
of the actual RH-sensitive matrix as an input.

## SERIOUS RESOLUTION PATH

**YES.**  The whole-matrix diagonal route is a serious proposal for a full
resolution.

A successful proof of the three interfaces above gives a cofinal finite lower
envelope, and `T-19807` then proves RH directly.  The route has a quantitative
power reserve and treats every finite direction simultaneously.

The status boundary remains explicit:

```text
rank-one large sieve:              PROPOSED, proved abstractly
subexponential smooth source:      PROPOSED, local zeta-product audit required
finite-to-global lower envelope:   PROPOSED, proved as an implication
source-specific CCM LMI:           NOT YET PROVED
RH:                                NOT YET CLAIMED
```
