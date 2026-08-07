# Chosen-route continuation: from Hermite interpolation to the exact hybrid endgame

Date: 2026-08-07  
Agent: `gpt56-02-p`  
Branch: `agent/gpt56-02-p/215-prime-polygon-rh-attack`  
Status: **research continuation; every new strengthening remains PROPOSED pending independent review; RH is not claimed proved**

## Executive result

I chose the positive source-frame route over the prime-power polygon route.
The polygon route has a cleaner scalar statement, but its last inequality is
already the complete RH sign with no apparent quantitative reserve.  The
source-frame route has more analytic machinery, but it offers a possible
separation between:

```text
a fixed Xi/prolate target hierarchy,
and
a separately completed finite complement.
```

The continuation produced three substantive results.

1. The dilation-Hermite polynomial ladder gives an exact finite Vandermonde
   source frame, but `R-21901` proves that it leaves a high-Fourier corrected
   tail exponentially larger than the prolate `d4` scale.  It cannot be used as
   the target-preserving complete frame.
2. The all-grid differential cardinal of `L-15631` is therefore forced: its
   periodization has exactly one Fourier mode and no projection remainder.
   `L-21901` assembles the full exact source/periodization/form bridge.
3. `L-21902` resums the entire exterior tail, every folded alias, and the sharp
   finite endpoint into one closed Fourier--Mellin formula: a sinc factor times
   a zeta divided difference.  This is the first single-formula emitter for the
   actual raw corrected-tail profile.

The remaining theorem is expressed by the hybrid Schur invariant of
`M-21901`.  It is not another source-existence problem.

## 1. Why the prime polygon was not selected

The exact polygon margin is

\[
M_j=B_j-F^*(A_j).
\]

Its recurrence and finite negative semidecision are useful, but proving
`M_j>=0` cofinally is exactly equivalent to RH.  Standard PNT, generic convexity,
and finite-Euler log-convexity miss an order-one archimedean threshold.  No
intermediate positive operator with a visible reserve emerged from that
formulation.

The positive route instead has an explicit small parameter

\[
d_4/d_8\to0
\]

inside the repaired prolate target.  The research question is whether exact
source completion can preserve that ratio on the complete finite space.

## 2. Exact Hermite ladder and its failure

Let

\[
\mathcal D=x\partial_x+1/2,
\qquad
h_m=(-\mathcal D^2)^m h.
\]

The arithmetic images satisfy

\[
\widehat{E(h_m)}(z)=z^{2m}\Xi(z).
\]

This gives a literal polynomial/Vandermonde interpolation map on any finite
CCM grid.  The idea initially appeared to replace all generic source
surjectivity.

The fatal scale mismatch is the exact discarded Fourier norm

\[
\frac1{2\ell}
\sum_{|k|>N}
|\Xi(\pi k/\ell)|^2|P((\pi k/\ell)^2)|^2.
\]

For the target `P=1` and `N~c ell^2`, a zero-safe first omitted sample is only
`exp(-C ell)`, while the fixed prolate defects are
`exp(-c exp(2ell))`.  The finite polynomial frame therefore destroys the
prolate target hierarchy before any zero-side estimate is attempted.

This is a useful negative result: exact finite interpolation is not the same as
an exact periodized source frame.

## 3. All-grid cardinal completion

The smooth differential cardinal satisfies

\[
\widehat q_{k,L}(\omega_j)=\delta_{kj}
\quad\text{for every integer }j.
\]

After the arithmetic multiplier,

\[
\Sigma_LE(f_{k,L})
=
\zeta(1/2-i\omega_k)e_k.
\]

Thus the finite projection is exact and the omitted high-Fourier term is zero.
The global arithmetic image is logarithmically Schwartz; every fold converges;
the sharp finite vector is compact BV; and all zero-side pairings converge
absolutely.  The zeta inverse is delayed until after support selection and then
enters only through an exact diagonal congruence.

This closes the complete source interface at the algebraic and form-domain
levels.

## 4. Closed corrected-tail symbol

For

\[
S_L(w)=\frac{2\sin(Lw/2)}{Lw},
\qquad
Z(z)=\zeta(1/2-iz),
\]

the complete corrected-tail column is

\[
\widehat W_{k,L}(z)
=
S_L(z-\omega_k)
\left[
Z(z)
\frac{iz+1/2}{i\omega_k+1/2}
\widehat\eta(z-\omega_k)
-Z(\omega_k)
\right].
\]

It has four decisive properties:

```text
zero at every Fourier lattice point;
minus the finite vector at every actual zeta zero;
exact Plancherel ordinary-tail Gram;
exact two-end support-phase decomposition.
```

This formula replaces separate Dunster, alias, endpoint, fold, and projection
objects for the raw cardinal completion.  All future estimates can be tested in
one metric against one immutable analytic function.

## 5. Exact remaining invariant

Retain a fixed low prolate packet `R_L` containing the repaired Xi target, and
let `C_L` be the all-grid cardinal completion.  In the complete corrected-tail
Gram, short the low packet:

\[
\mathfrak D_L
=D_{CC}-D_{CR}D_{RR}^{-1}D_{RC}.
\]

The target-preserving completion is equivalent to the cofinal lower bound

\[
\lambda_{min}(\mathfrak D_L,G_C)
\ge c d_8(L).
\]

Alternatively, bypass the ordinary-tail comparison and prove the joint Weil
short directly:

\[
\mathfrak A_L
=A_{CC}-A_{CR}A_{RR}^{-1}A_{RC}
\succeq-o(1)G_C.
\]

These are the smallest exact positive-route obligations found in the session.
Every earlier packet/capture/source ambiguity has been absorbed into their
matrices.

## 6. What would finish RH

A proof of either joint estimate on an unbounded sequence, together with the
existing fixed target hierarchy and Hardy projection convergence, yields

\[
\frac{\mu_L-L_L}{g_L}	o0.
\]

The finite simple-real-zero theorem and Hurwitz then give RH.

The most plausible next analytic attack is on the direct joint matrix using the
closed symbol above:

1. apply the positive operator Riemann--von Mangoldt formula to its line-centered
   profile;
2. rephase the cross-end horizontal terms as in `L-21503`;
3. bound the same-end horizontal divided difference directly from the bracket;
4. keep the low/cardinal cross inside the final Schur matrix;
5. do not replace it by separate norm budgets.

## 7. Honest status

The continuation does not complete RH.  It does complete an exact source
emitter and rules out a seductive but scale-incompatible Hermite completion.
The remaining object is one joint finite matrix sequence, not a list of
independent qualitative assumptions.
