# Research report — boundary-optimal jet selectors

Date: 2026-08-23

Branch: codex/105100-residue-second-moment

Claims: L/T/R/M-105107

## Breakthrough

Checkpoint 7 exposed the exact conditioning loss of polynomial CRT
selectors.  Checkpoint 8 separates the avoidable part from the intrinsic
part.

For each actual pole node, retain the full order at nontargets and one less
than the order at targets.  Those are exactly the zeros forced on every
top-jet selector.  Their Blaschke product \(I_0\) has boundary modulus one.
After writing \(W=I_0H\), every confluent-looking target condition becomes
one ordinary value \(H(c)=y_c\).

The selector norm is therefore solved exactly by one finite Pick matrix:

\[
P_u=
\left[
\frac{u^2-y_j\overline y_k}
{1-c_j\overline c_k}
\right].
\]

The first \(u\) with \(P_u\succeq0\) is the exact minimum.  At the singular
threshold, the extremal is finite inner and has constant boundary modulus.

## Why it matters

The optimal selector gives the edge envelope

\[
\left|\frac1{2\pi i}\int_EW_*h\right|
\le\frac{\operatorname{len}(E)}{2\pi}\tau\|h\|_E,
\]

without the avoidable outer-radius growth of the polynomial envelope.  It
still annihilates every nontarget actual pole and extracts the same first and
second leading jet residues.

The improvement can be strict.  The exact real-even cluster with
\(\varepsilon=1/5,m=2\) has polynomial norm \(676\), while the inner optimum
is \(625\), exactly the checkpoint-7 Blaschke lower bound.

## Window and symmetry

Riemann-map transport gives the same theorem in
\(A(\Omega)=\operatorname{Hol}(\Omega)\cap C(\overline\Omega)\) for a bounded
simply connected Jordan window.  A rectifiable Jordan boundary, including a
rectangle, suffices for the contour residue formula.  No analytic extension
through rectangle corners is claimed.

Conjugation and sign-compatible data force a real/even extremal by uniqueness.
Reflected rational poles lie outside the current disk but must be rechecked
if a later contour is enlarged.

## Prior-art audit

No accepted repository claim supplies this selector theorem.  Accepted
actual-Xi Pick matrices through order three use a different kernel.  The
historical proposed local-Pick L-91014 collides by ID with a different
accepted main claim, and quarantined L-92302 has no growing-order estimate.
Neither is used.  The classical finite Nevanlinna–Pick theorem is stated
locally and scoped as classical background.

## Authentication

    PASS_T105107_BLASCHKE_PICK_JET_SELECTORS
    17/17 normal
    17/17 optimized
    82747e320365a97bf9824dd84960f00bbcb77cd738040c2c5214be844dfc738c

No heavy computation was run.

## Remaining frontier

The complete Xi manifest, certified rectangle conformal coordinates,
cofinal Pick eigenvalue and pseudohyperbolic-product estimates, unweighted
quotient edge bounds, changing-window pole control, strict coherence,
RCMV104530, and RH remain open.
