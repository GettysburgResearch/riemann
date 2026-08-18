# M-98600 — Proof program for the zero-marginal critical completion block

Claim ID: `M-98600`  
Status: **PROPOSED METHODOLOGY — PENDING INDEPENDENT REVIEW**  
Created: 2026-08-18  
Authoring agent: `gpt56-pro`

## Objective

Prove `ZMCSCBI67` from `T-98600` without introducing a renamed root sign. The
producer must be an explicit cross-scale Gram or contraction built from the
exact four-profile quotient state of PR #610.

## 1. Freeze the exact state

At every quotient coordinate retain exactly

```text
A_P(x)       restricted Mobius reciprocal sum;
N_P(x)       semigroup count;
H_P(x)       semigroup harmonic sum;
N_(P^c)(x)   complementary-semigroup count.
```

Do not compress to one root value. PRs #582, #591 and #611 independently prove
that the actual quotient profile is Markov-minimal for their respective
observables.

## 2. Work in parity channels

Diagonalize each local completion matrix

\[
J_v=\begin{pmatrix}\Gamma_v&U_v\\U_v&\Gamma_v\end{pmatrix}
\]

into the positive channel energies

\[
E_v^+=\Gamma_v+U_v,
\qquad E_v^-=\Gamma_v-U_v.
\]

The target is an explicit Douglas factorization of the antisymmetric feature
through the symmetric feature. A proof based only on the local inequalities
`|U_v|<=Gamma_v` is insufficient; PR #610 supplies an explicit finite
overshoot after the Abel lift.

## 3. Construct cross blocks before integration

The cross-state kernel must be produced at the multiplicative-semigroup level,
using restricted Möbius inversion and common quotient coordinates. Only after
that common kernel is established should it be integrated against the positive
Stieltjes measure `dh_0`.

Independent pointwise square roots of the local `2 x 2` matrices are forbidden:
they do not respect prime updates and cannot survive the half-order Abel lift.

A successful construction should provide a block identity of the form

\[
G_v^+-G_v^-
=C_v+\sum_{w\succ v}\mathcal L_{vw}(G_w^+-G_w^-),
\tag{M-98600.1}
\]

where each current defect `C_v` is positive semidefinite and every
`mathcal L_(v,w)` is a source-computable positive map. Finite backward induction
would then prove channel order.

## 4. Use the hereditary corridor as boundary data

Choose the terminal frontier using PR #608 or the equivalent signed transfer of
PR #609. Do not continue the Dickman model through fixed primes: PR #610 proves
that the fixed-prime homogeneous margin is eventually negative.

The terminal theorem should enter only as boundary channel order. The low-prime
critical block is then finite at every endpoint and is handled by the exact
completion recurrence.

## 5. Exploit the zero-marginal collapse

Do not rebuild all Lorenz hinge parameters. PR #601 proves that, eventually,
nonzero hinge thresholds carry no independent obstruction. The completion
producer should target only the trace-free scalar channel at `lambda=0`.

This is the principal state reduction relative to PR #591.

## 6. Separate the constant and transverse modes

PR #604's four-band kernel has nonzero zeroth and first dyadic moments and
cumulative signs `-,+,+,-`. Therefore a residual curvature estimate must first
extract its constant and linear modes explicitly. The constants already
available are:

```text
a_*  = limiting P61 source mass;
J_*  = first logarithmic Stieltjes moment;
```

from PR #607. After those two modes are removed, test whether the residual
kernel admits a positive second-difference or a two-switch variation bound.
No free moment cancellation may be asserted.

## 7. Use the two-row lane as a hostile audit

PR #611 decomposes the literal row-two and sharp-row-three states into one common
Dickman component plus a compact three-band transverse correction. A proposed
completion should be tested on this transverse channel. Passing the scalar
channel but failing CPQR23 means the construction has not yet supplied a
physical two-row lift, although the scalar RH consumer may still remain valid.

## 8. Hazard budget only after typing

The exact nonduplicating hazard identity and its `<1/8` child mass are valuable
only after the aggregate current has been placed in a positive physical packet
class. Raw-exposure conservation prevents using the coefficient budget as a
substitute for the cross-scale sign theorem.

## 9. Proof and computation deliverables

A proof-grade producer should emit:

1. an explicit formula for every cross-state Gram block;
2. a proof of positivity before Stieltjes integration;
3. exact covariance under the four prime-update recurrences;
4. the symmetric-to-antisymmetric contraction or positive-map identity;
5. a finite fail-closed checker for quotient-DAG algebra;
6. hostile fixtures reproducing the overshoot at `P={3,5,7,11,13}`, `N=26`;
7. terminal-frontier compatibility with PR #608;
8. a clear statement that no floating finite sweep proves the all-scale theorem.

## 10. Fallback analytic formulation

If a direct Gram is unavailable, the equivalent analytic target is a
source-faithful maximum principle for the completion correlation

\[
\vartheta_v=\frac{U_v}{\Gamma_v}\in[-1,1]
\]

on the exact four-profile quotient DAG. Unlike the scalar ratio in PR #608,
this denominator is always positive. The maximum principle must be derived from
the four-profile recurrences and the positive Stieltjes source; assuming
`vartheta>=0` at interior states is circular.

## Boundary

```text
local unit Schur ports                 proved
positive Stieltjes source              proved
four-profile recurrences               proved
terminal boundary order                proved in mesoscopic corridor
cross-state Gram / positive maps       open
zero-marginal contraction              open / RH-bearing
RH                                     unproved
```
