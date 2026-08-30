# L-0301 — Xi-zero symmetry orbits

Claim ID: L-0301  
Title: Nontrivial zeros occur in conjugate/reflection orbits  
Status: PROPOSED  
Authoring agent: `gpt56-03`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: D-0301  
Scope: multiplicity-preserving symmetry of the zero set  
Related counterexample candidates: any direct zero candidate

## Statement

Let `rho` be a zero of `xi` of multiplicity `m`.  Then
\[
 \overline{\rho},\qquad 1-\rho,\qquad 1-\overline{\rho}
\]
are also zeros of `xi`, each of multiplicity `m`.

Consequently an off-critical, nonreal zero normally belongs to the four-point
orbit
\[
 \{\rho,\overline{\rho},1-\rho,1-\overline{\rho}\},
\]
with orbit size reduced only when points coincide.  For a nonreal zero, a
coincidence between `rho` and `1-\overline{rho}` occurs exactly on the critical
line.

## Proof

Write the local factorization at `rho` as
\[
 \xi(s)=(s-\rho)^m u(s),
\]
where `u` is analytic near `rho` and `u(rho) != 0`.

From the reality relation in D-0301,
\[
 \xi(s)=\overline{\xi(\overline{s})}.
\]
For `s` near `\overline{rho}`,
\[
 \xi(s)
 =\overline{(\overline{s}-\rho)^m u(\overline{s})}
 =(s-\overline{\rho})^m\overline{u(\overline{s})}.
\]
The final factor is analytic near `\overline{rho}` and nonzero there, so
`\overline{rho}` has multiplicity `m`.

From the functional equation,
\[
 \xi(s)=\xi(1-s).
\]
For `s` near `1-rho`,
\[
 \xi(s)=((1-s)-\rho)^m u(1-s)
       =(-1)^m(s-(1-\rho))^m u(1-s).
\]
Again the remaining factor is analytic and nonzero at `1-rho`; hence the
multiplicity is `m`.  Applying conjugation to `1-rho` gives
`1-\overline{rho}` with the same multiplicity.

Finally,
\[
 \rho=1-\overline{\rho}
 \quad\Longleftrightarrow\quad
 2\operatorname{Re}\rho=1.
\]
This is precisely the critical-line condition.  ∎

## Motivation

A proposed off-line zero cannot be treated as an isolated asymmetric event.
Searches and zero counts must respect its reflected and conjugate companions.
The lemma also prevents accidental double counting.

## Analytic domain audit

Only the entire function `xi` is used.  No contour, pole, or branch occurs.

## Dependency audit

The proof uses exactly the two symmetries fixed in D-0301 and elementary local
factorization of an analytic function at a zero.

## Gap audit

- The lemma does not assert simplicity.
- A zero-count rectangle need not contain all members of an orbit.
- Symmetry of approximate decimal values is not a certificate that exact zeros
  exist.
- For a real zero, orbit sizes can differ; the direct-counterexample project
  normally searches nonreal zeros in the critical strip.

## Adversarial tests

Check the orbit degeneracies for:

1. `rho=1/2+i gamma` with `gamma!=0`;
2. a hypothetical real `rho` in `(0,1)`;
3. a hypothetical off-line nonreal `rho`.

## Remaining uncertainty

None beyond the imported functional equations in D-0301.  Independent proof
review is still required before status advancement.

## Suggested next attack

Use the orbit relation to design symmetry checks in Issue #7 certificates and
to reduce redundant reconnaissance rectangles without weakening proof.
