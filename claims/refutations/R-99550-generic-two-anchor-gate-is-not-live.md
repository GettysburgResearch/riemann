# R-99550 — The generic two-anchor gate is not a live obstruction for the canonical equality frame

Claim ID: `R-99550`  
Status: **PROVED SOURCE-SPECIFIC FIREWALL**  
Created: 2026-08-19  
Depends on: `L-99230`, `L-99231`, `L-99550`, `L-99551`  
RH status: **unproved**

PR #638 correctly proves that an arbitrary profile with the same smooth
Volterra density may differ by

\[
c\sqrt\theta+d\theta
\]

and may carry derivative-jump atoms at activation knots.  That theorem must not
be discarded.

For the actual canonical equality seed, however, every activated colour is
clamped by

\[
F(1)=F'(1)=0,
\]

and the total frame satisfies

\[
\mathscr B^\star(1)=(\mathscr B^\star)'(1)=0.
\]

Adding `c sqrt(theta)+d theta` preserves these two endpoint data only if

\[
c+d=0,
\qquad
\frac c2+d=0,
\]

which forces

\[
\boxed{c=d=0.}
\]

Likewise every activation jump is zero colour by colour.  Therefore importing
a nonzero two-anchor debt into the canonical frame is an over-generalization
of the PR #638 audit, not an additional theorem obligation.

This refutation is narrow.  It does not prove the compact Hall theorem, the
common-parent source identity, finite/native equality, literal score, or RH.
