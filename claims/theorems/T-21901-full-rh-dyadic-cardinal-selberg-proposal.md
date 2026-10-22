# T-21901 — Full RH proposal from dyadic cardinal completion and Selberg–Hankel duality

Claim ID: `T-21901`  
Title: One positive operator-valued Selberg adjoint certificate gives a vanishing whole-matrix lower envelope and RH  
Status: **FULL PROOF PROPOSAL — DEDUCTION COMPLETE; ONE COFINAL SELBERG–HANKEL CERTIFICATE PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-02-p`  
Created: 2026-08-07  
Dependencies: Weil's criterion; the whole-matrix diagonal theorem `T-19807`; `L-21504`--`L-21506`; `L-21901`, `L-21902`, `L-21904`, `L-21905`; the exact centered prime/pole explicit formula  
Scope: proposed complete positive proof of the Riemann hypothesis

## 1. Strategic statement

Let

\[
 I_L=[-L/2,L/2]
 \]

and let `V_L` be the complete finite Fourier space with bandwidth

\[
 H_L=\exp(L^\theta),
 \qquad 0<\theta<1/2.
 \tag{T-21901.1}
\]

Every vector is extended by zero outside `I_L`.  Let `A_L` be the exact
localized Weil matrix and `G_L` its `L2` Gram.

The whole-matrix diagonal theorem says that

\[
 \boxed{
 A_{L_j}\succeq-\rho_jG_{L_j},
 \qquad
 \rho_j\to0,
 \qquad
 L_j\to\infty
 }
 \tag{T-21901.2}
\]

on a Gevrey-dense diagonal implies the Riemann hypothesis.

The present proposal supplies a complete exact source and metric architecture
for (T-21901.2) and reduces its arithmetic content to one operator-valued
Selberg–Hankel certificate stated in Section 6.

## 2. Exact complete source frame

Use the twice-period all-grid differential cardinals of `L-21904`.  Before zeta
inversion, every source is smooth, compactly supported, satisfies both
Connes--Consani cancellations, and has periodized arithmetic image

\[
 \Sigma_LE(f_{k,L})
 =Z_k(L)e_k,
 \qquad
 Z_k(L)=\zeta(1/2-i\omega_k).
 \tag{T-21901.3}
\]

Support averaging is performed in these raw coordinates.  Delete the
`o(1)`-measure zeta-unsafe set of `L-21506`, select a remaining support, and only
then apply the diagonal inverse `Z_L^{-1}`.  Every relative Loewner inequality
is transported by exact congruence.

The corrected tail of each column is a genuine function in a common
zero-side form domain.  It has the closed sinc--zeta divided-difference symbol
of `L-21902`; no separate projection, endpoint, or Poisson term is omitted.

Thus the complete finite Fourier packet is represented exactly by one source
matrix, one corrected-tail synthesis, and one Weil matrix.

## 3. Uniform ordinary-tail metric

The twice-period source vanishes on the complete antiperiodic half-grid.
`L-21904` gives the exact identity

\[
 \mathcal A_LW_c=-y_c
 \tag{T-21901.4}
\]

and the quantitative floor

\[
 \boxed{
 D_L:=W_L^*W_L
 \succeq[1/2-o(1)]G_L.
 }
 \tag{T-21901.5}
\]

This removes the last algebraic and conditioning ambiguity from the complete
source frame.  There is no soft finite sector hidden by a vanishing ordinary
profile denominator.

Put

\[
 \widehat D_L=D_L+\tau_LG_L,
 \qquad
 \tau_L=e^{-L/4+o(L)}.
 \tag{T-21901.6}
\]

The raw source graph and its support derivative have size `e^(L/4+o(L))`, so
regularization yields a sub-square-root profile envelope exactly as in the
whole-matrix source theorem.  The product of every deterministic graph loss
with `tau_L` tends to zero.

## 4. Prime-side centered matrix

For a finite coefficient vector `c`, write the complete explicit formula as

\[
 \langle c,A_Lc\rangle
 =\mathcal A_L^{\rm arch}(c)
  +\langle dP,\mathcal K_{L,c}\rangle,
 \tag{T-21901.7}
\]

where

\[
 dP(y)=\sum_{n\ge2}{\Lambda(n)\over\sqrt n}
       \delta_{\log n}(dy)
 \tag{T-21901.8}
\]

and `mathcal K_(L,c)` is the exact compact-support correlation kernel generated
by the finite vector.  Put

\[
 dP_0(y)=e^{y/2}dy,
 \qquad
 d\nu=dP-dP_0.
 \tag{T-21901.9}
\]

The pole contribution of `dP_0` is combined with the archimedean matrix before
any estimate.  Thus

\[
 \langle c,A_Lc\rangle
 =\mathcal B_L(c)
  +\langle\nu,\mathcal K_{L,c}\rangle,
 \tag{T-21901.10}
\]

where `mathcal B_L` is completely explicit and includes the pole, gamma,
trivial-zero, and endpoint terms in the repository's fixed convention.

The constant coordinate of (T-21901.10) is the square-screw/prime-polygon
criterion.  Therefore any proof of the matrix lower bound necessarily proves
the scalar RH-sensitive channel; no packet construction bypasses it.

## 5. Exact nonlinear Selberg identity

The centered prime measure satisfies

\[
 \boxed{
 \mathscr L\nu+\nu*\nu=R,
 }
 \tag{T-21901.11}
\]

with

\[
 (\mathscr L^*f)(y)
 =yf(y)+2\int_0^\infty f(x+y)e^{x/2}dx.
 \tag{T-21901.12}
\]

For every `s>1/2`, `L-21905` constructs the explicit completely monotone
adjoint

\[
 f_s(y)=\int_s^\infty
 \left({s-1/2\over u-1/2}\right)^2e^{-uy}du,
 \qquad
 \mathscr L^*f_s=e^{-sy}.
 \tag{T-21901.13}
\]

Its Hankel kernel is a literal Gram kernel.  Positive matrix-valued mixtures of
the `f_s` therefore convert the quadratic prime channel in (T-21901.11) into a
nonnegative square rather than an exponentially large absolute-value error.

## 6. Sole arithmetic review hinge: `SH(L)`

For each sufficiently large safe support `L`, let `mathcal K_L(y)` denote the
Hermitian matrix kernel satisfying

\[
 c^*\mathcal K_L(y)c=\mathcal K_{L,c}(y).
 \tag{T-21901.14}
\]

The proposed Selberg--Hankel certificate `SH(L)` consists of:

1. a finite positive matrix measure `Lambda_L` on `(1/2,infinity)`;
2. a Hermitian matrix function `g_L` whose Hankel kernel
   \[
   (x,y)\longmapsto g_L(x+y)
   \]
   is positive semidefinite;
3. a residual matrix kernel `e_L`;

such that

\[
 \boxed{
 -\mathcal K_L
 =\mathscr L^*
  \left[
   \int f_s\,d\Lambda_L(s)+g_L
  \right]
  +e_L.
 }
 \tag{T-21901.15}
\]

Put

\[
 F_L=\int f_s\,d\Lambda_L(s)+g_L.
 \tag{T-21901.16}
\]

The required directed inequalities are

\[
 \boxed{
 \mathcal B_L-\langle R,F_L\rangle
 \succeq-\alpha_LG_L,
 }
 \tag{T-21901.17}
\]

and

\[
 \boxed{
 -\beta_LG_L
 \preceq\langle\nu,e_L\rangle
 \preceq\beta_LG_L,
 }
 \tag{T-21901.18}
\]

with

\[
 \boxed{
 \rho_L:=\alpha_L+\beta_L\longrightarrow0.
 }
 \tag{T-21901.19}
\]

Every object is finite at fixed `L`: the prime kernel has finitely many spline
cells, `Lambda_L` may be finitely supported, and all transcendental inputs admit
directed enclosures.  The certificate is therefore independently checkable by
matrix additions, exact Selberg residual contractions, and LDL pivots.

### Proposed construction of `SH(L)`

The construction is the joint form of the three strongest arithmetic
coordinates already present in the repository.

- The prime-polygon transport recurrence supplies the one-sided reserve.
- The curvature-corrected Haar/dilation identity supplies the centered mass
  square.
- The exponential adjoints (T-21901.13) supply the positive resolvent cone.

On each prime-knot cell, solve the finite adjoint interpolation problem in the
span of the exponential adjoints and the curvature square, preserving the
shared endpoint values.  Adjacent cells are joined by the exact translation
recurrence of the prime-spline programme.  Selberg's coefficient identity
places the quadratic channel in the positive Hankel term; the remaining
endpoint rows form `e_L`.

The claim that this construction satisfies (T-21901.17)--(T-21901.19) is the
**only new load-bearing line not proved elsewhere in this proposal**.  It is the
line an independent reviewer must verify or reject.  It must be checked before
any entrywise absolute value is taken.

## 7. Deduction of the whole-matrix lower envelope

Assume `SH(L)`.  Pair (T-21901.11) with the matrix function `F_L`.  Since both
parts of its Hankel kernel are positive semidefinite,

\[
 \iint F_L(x+y)\,d\nu(x)d\nu(y)\succeq0.
 \tag{T-21901.20}
\]

Using (T-21901.15),

\[
 -\langle\nu,\mathcal K_L\rangle
 \preceq
 \langle R,F_L\rangle+\langle\nu,e_L\rangle.
 \tag{T-21901.21}
\]

Substitution into (T-21901.10), followed by (T-21901.17)--(T-21901.18), gives

\[
 \boxed{
 A_L\succeq-\rho_LG_L,
 \qquad
 \rho_L\to0.
 }
 \tag{T-21901.22}
\]

No ground-state identification, complete ambient-complement theorem,
selected-zero frame, or fixed-height zero census is used.

## 8. Finite-to-global passage

Choose an unbounded sequence of safe supports on which `SH(L)` holds.  The
bandwidth (T-21901.1) is sufficient to approximate every compact Gevrey test
function superexponentially in the support length.  The elementary
support-dependent explicit-formula continuity bound is only exponential.
Therefore the finite Fourier projections form a diagonal core for the global
Weil distribution.

For a compact Gevrey test function `f`, let `P_Lf in V_L` be its finite Fourier
projection.  Then

\[
 Q_W(P_Lf)\to Q_W(f),
 \qquad
 \|P_Lf\|_2\to\|f\|_2.
 \tag{T-21901.23}
\]

Equation (T-21901.22) gives

\[
 Q_W(P_Lf)\ge-\rho_L\|P_Lf\|_2^2.
 \]

Taking the limit yields

\[
 Q_W(f)\ge0.
 \tag{T-21901.24}
\]

Density and continuity extend this to the complete Weil test space.  Weil's
criterion then gives

\[
 \boxed{\mathrm{RH}.}
 \tag{T-21901.25}
\]

Thus `SH(L)` on an unbounded safe sequence completes the proof.

## 9. Relationship to the hybrid prolate target

The fixed repaired prolate/Xi packet remains useful as a low-dimensional
calibration and an independent Hurwitz route.  `L-21904` proves that its
cardinal quotient has a uniform ordinary-tail Schur floor after a finite
orthogonal enlargement.  If `SH(L)` is certified only on that quotient, the
fixed `d_4/d_8` hierarchy and the existing Rayleigh-floor theorem give the same
RH conclusion.

The whole-matrix route is preferred in this proposal because it avoids the
additional target/gap bookkeeping once (T-21901.22) is available.

## 10. Status boundary

The proposal has reached a full implication chain, not an independently
verified proof.

Closed or reduced to exact finite identities:

- complete finite source surjectivity;
- absence of a high-Fourier projection tail;
- fold and zero-side domain convergence;
- zeta-safe support selection;
- a uniform ordinary-tail metric floor;
- explicit positive-Hankel exponential adjoints;
- finite-to-global diagonal passage;
- the deduction `SH(L) => RH`.

Open and load bearing:

\[
 \boxed{\text{the cofinal Selberg--Hankel certificate }SH(L).}
 \]

A finite certificate or a finite positive ladder does not prove its cofinal
rate.  Until (T-21901.15)--(T-21901.19) are independently established, RH is
not claimed proved.
