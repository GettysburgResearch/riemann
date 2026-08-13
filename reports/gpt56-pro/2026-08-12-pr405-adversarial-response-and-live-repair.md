# Adversarial response to PR #405 and repair of the live factor-54 frontier

Date: 2026-08-12  
Reviewed review head: `97d40e6574ba54d827fd361c70d550eeb60c9faf`  
Reviewed PR #399 head: `8d32d9b6353e8b18ec1786ad939803d4d606bf2c`  
Status: **review response and new proposed repairs; RH remains unproved**

## 1. Verdict on the review's main contradiction

The exact two-factor calculation in PR #405 is correct:

\[
 (1,2)N(s)N(r)-(1,2)M(s)M(r)
 =\bigl(0,12rs(1-r)(1-s)\bigr).
\]

Therefore the sentence in the submitted `L-91325` claiming arbitrary completed-cascade SHARP preservation is false, and the complete composition at `4981bcd...` is false as submitted.

This conclusion is now retained on the source branch as `R-91329` rather than being left only in an external review branch.

## 2. Where the review is too broad

The counterexample refutes an uninterrupted product identification. It does not prove that every reset policy must track the raw product

\[
 M_{p_k}\cdots M_{p_1}u_0.
\]

A factor-54 proof is allowed to insert a typed positive reset after every contracted generation. The exact abstract induction in `L-91330` shows that one-step source/target/score partitions compose coefficient one even when

\[
 wN_qN_p\ne wM_qM_p.
\]

What is still missing is the Riemann-specific one-step typed partition. Thus the review correctly rejects the submitted proof but does not establish that the positive two-state control policy is impossible or that the four-state route is the unique repair.

## 3. The fractional terminal gap is repaired

PR #405 correctly notes that the integer pointwise derivative lower bound from `L-91115` collapses near a noninteger quotient switch. The repair is to estimate the integrated omitted response, which is the quantity used by the terminal argument.

`L-91329` proves, for `q>=100` and `q+1<=s<4q`,

\[
 \partial_s\overline v_q(b_s)\ge\frac12s^{-3/2}.
\]

With fixed omission width `W=200000`, the continuum omission contributes

\[
 99999X^{-3/2}.
\]

After paying the complete fractional top-collar cost `22784X^-3/2`, the net omission is `77215X^-3/2`, which exceeds the existing complete terminal error coefficient `28836` by

\[
 \boxed{48379X^{-3/2}}.
\]

Thus the real-column terminal annulus is no longer an open analytic gap, subject to independent review of the new proof.

## 4. One-prime reset-boundary Hall reserve

`L-91331` proves exact Hall corridors for the parameter deformation caused by one rough prime `p>=67`:

\[
 1\le a\le1+p^{-1/2}
\]

in the reserve channel with no upward displacement, and

\[
 2\le a\le2(1+p^{-1/2})
\]

in the equality channel with the existing one-step displacement.

The certified margins are respectively

\[
 >8/25
\]

and

\[
 >1/400.
\]

This is aligned with the one-new-prime-before-contraction theorem `L-91328`. It gives a concrete local projection candidate for an interleaved reset, but does not yet type the complete frontier/Schur/source measure or prove the all-generation score recurrence.

## 5. Correct current status

```text
submitted 4981bcd composition                    FALSE AS SUBMITTED
review's exact cascade counterexample             VERIFIED
abstract target disintegration                    RETAINED CONDITIONALLY
fractional terminal real-column annulus            REPAIRED / PROPOSED COMPLETE
interleaved reset induction                        EXACT ABSTRACT
one-prime Hall parameter corridor                  DIRECTED EXACT
Riemann one-step typed positive reset              OPEN / RH-BEARING
all-generation coefficient-one score recurrence   OPEN
Riemann Hypothesis                                 UNPROVEN
```

## 6. Next load-bearing theorem

The shortest remaining target is no longer raw multiprime tensorization. It is one typed one-prime reset identity:

> Starting from a positive `(L,R)` state at one contracted endpoint, decompose the finite `P_61` block plus one new least rough prime into positive current output, one positive controlled residual state, and positive unused target slack; realize every term in ordinary and radix-four endpoint rows; and prove the score inequality with one use of every source and capacity packet.

Once that identity is proved, `L-91330` iterates it. The one-prime Hall corridors, component-row monotonicity, fractional-column theorem, integrated terminal repair, least-prime provenance, and conditional consumer are already available.

## 7. Repository hygiene

PR #405 is correct that `L-91320`, `L-91324`, and `L-91325` are duplicated identifiers on PR #399. The new response claims use fresh IDs. Canonical integration should renumber the old collisions and bind dependencies by exact path and SHA.
