# T-0306 — Speiser criterion

Claim ID: T-0306  
Title: Speiser's derivative-zero criterion for RH  
Status: PROPOSED  
Authoring agent: `gpt56-03`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: external theorem of Speiser (1935)  
Scope: imported equivalence; local derivative-zero witness  
Related counterexample candidates: Issue #17

## Statement

The Riemann hypothesis is equivalent to the assertion that `zeta'(s)` has no
**nonreal** zero in the open half-strip
\[
 0<\operatorname{Re}s<\frac12.
\]

Consequently, a rigorously isolated zero of `zeta'` in any compact region
strictly contained in that half-strip and separated from the real axis is a
finite unconditional disproof of RH.

## Source

Andreas Speiser, *Geometrisches zur Riemannschen Zetafunktion*,
Mathematische Annalen 110 (1935), 514--521,
DOI 10.1007/BF01448042.

Inspection note: original publisher/EUDML metadata was located.  The exact
modern wording was checked in later primary research papers that explicitly
state Speiser's theorem, including Garunkštis--Tamošiūnas,
*Zeros of the Lerch zeta-function and of its derivative for equal parameters*,
arXiv:1902.03064.  The original German proof was not reconstructed.

## Motivation

This trades a direct zeta zero for a zero of its derivative.  The final proof
object can still be a compact rational rectangle and winding count, as
formalized in L-0330.

## Proof status

Imported theorem.  L-0330 proves only the final contrapositive once this
equivalence is accepted.

## Analytic/domain audit

- The word `nonreal` matters; derivative behavior at real points is not the
  witness used here.
- The half-strip is open and lies inside the critical strip.
- `zeta'` is analytic there because the pole of `zeta` is at `1`.
- A zero of `xi'` or a derivative of another completion is not automatically a
  zero of `zeta'`.

## Dependency audit

Issue #17 will depend on L-0302--L-0304 and a certified complex evaluator for
`zeta'`.  Speiser's theorem does not provide the numerical certificate.

## Gap audit

- A derivative zero on the critical line does not contradict the criterion.
- A rectangle touching `Re(s)=1/2` does not prove an off-left zero.
- A real zero inside `0<Re(s)<1/2` would not satisfy the stated nonreal witness.
- Multiple derivative conventions can introduce extra zeros.

## Remaining uncertainty

Independent review should inspect and translate the original theorem and check
whether any equivalent formulation includes or excludes specific real zeros.

## Suggested next attack

Claim Issue #17 and share the generic contour certificate verifier with Issue
#7 while keeping the analytic `zeta'` implementation independent.
