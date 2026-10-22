# Log-derivative edge margins and the exterior-critical obstruction

Date: 2026-08-23

Checkpoint base: `e223f98823bdb7b11736a05993ac12b75d5263b3`

## Outcome

The optimal selector norm \(\tau\) is only one factor in the absolute edge
estimate.  The other factor is an exact lower-margin problem.  Writing

\[
\mathscr L=F'/F,
\qquad
\mathscr A=\mathscr L^2+\mathscr L'=F''/F,
\]

gives

\[
\|W_{1,*}F/F'\|_E=\tau_1/\inf_E|\mathscr L|,
\qquad
\|W_{2,*}F^2/(F'F'')\|_E
=\tau_2/\inf_E|\mathscr L\mathscr A|.
\]

These are equalities because the optimal selectors have constant boundary
modulus.

## Orthogonal two-factor firewall

L/R-105106 already supplied a clustered quartic family where selector
conditioning diverges.  L/R-105109 supplies the orthogonal failure:

\[
F_s(z)=\exp(z^2/2-z^4/(4s)).
\]

For \(s\downarrow1\), the first selector norm stays one and the second tends
to \((3+\sqrt5)/2\), while the two raw and optimally weighted boundary
suprema diverge.  The first interior manifest is fixed; the second has a
stable target/nontarget topology and bounded separation/conditioning.  Its
nontarget locations move with \(s\), and no identical-support claim is made.

The full weighted contour integrals remain exactly one.  This is an
absolute-envelope obstruction, not a refutation of phase-sensitive edge
cancellation.

## Finite-jet firewall

A polynomial exponential gauge can vanish to arbitrary assigned orders at a
finite interior set while prescribing the first or second logarithmic
denominator at a boundary point.  It preserves the zeros and selected jets
of \(F\), but not necessarily its derivative-event manifest.  Thus local
jet information cannot stand in for a global boundary collar certificate.

## Prior-art audit

No `L/T/R/M/X-105109` collision exists across the fetched refs or shared
worktrees.  The closest direct antecedents are L/R-105106: their quartic
fixture loads selector conditioning, and their abstract
\(h_C=1/z+C\) remainder is not a simultaneous derivative-quotient
realization.  PR #720 L-104519 controls a different companion
log-derivative difference under a fixed-ladder far-right exhaustion;
L-104521 controls argument variation, not boundary suprema.  Accepted
Vinogradov–Korobov safe-disc and low-order actual-Xi Pick claims use different
objects/regions and provide no reciprocal boundary lower margin.  PR #719's
arithmetic source “gauge” and PR #720's Hermite–Biehler construction are
unrelated.

The elementary exponential mechanism is classical; novelty is claimed only
for this exact programme-specific two-factor realization.  The family is
zero-free of order four and is not an Xi-class model.

## Exact authentication

    PASS_T105109_LOG_DERIVATIVE_EDGE_OBSTRUCTION
    17/17 focused tests in normal and optimized Python
    54829e77cb2aa90192aabdd61f86ff045a04ba3549f82c75384bc9a4e08f2890

The verifier uses exact rational coefficient, sign, and isolating-interval
certificates.  No numerical root finding or heavy computation is used.

## Remaining gate

A cofinal Xi application needs either a two-sided collar with quantitative
lower bounds for both logarithmic denominators or an oriented-edge
cancellation theorem that bypasses the absolute envelope.  It must then be
combined with the Green–Gram selector cost, correction terms, multiplicity
defect, and a strict coherence margin.  RCMV104530 and RH remain open.
