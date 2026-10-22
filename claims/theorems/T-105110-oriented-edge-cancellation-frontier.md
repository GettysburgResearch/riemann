# T-105110 — Oriented-edge cancellation frontier

Claim ID: T-105110

Status: **PROPOSED EXACT FINITE-EDGE LEDGER; XI CANCELLATION OPEN**

Created: 2026-08-23

Depends on: L-105103; L-105107; L-105109; L-105110; R-105110

RH status: **unproved**

## Result

The phase-sensitive branch left open by T-105109 splits into two independent
debts.  If a weighted quotient continues meromorphically across a straight
edge and is decomposed as

\[
Wh=R+\sum_j\frac{r_j}{z-p_j},
\tag{T-105110.1}
\]

then exterior simple poles whose normal projections stay away from the
corners contribute at most

\[
\left(\pi+\log\frac\ell\kappa\right)\sum_j|r_j|
\tag{T-105110.2}
\]

to the oriented edge, uniformly as their normal collar distances vanish.
The pole-subtracted remainder contributes at most its edge \(L^1\) norm.

This is a genuine escape from the absolute quotient-margin gate: the exact
simultaneous derivative-quotient family

\[
F_\delta(z)=e^{z^2/2-\delta z}
\tag{T-105110.3}
\]

has, on every fixed \(E_a\) with \(0<a\le1/2\), divergent first and second
boundary suprema and absolute edge integrals, while both centered oriented
edge integrals converge to \(-i\pi\).

The escape is conditional, not automatic.  R-105110 gives a real-even
zero-free entire family with one globally fixed simple critical target,
residue one, no exterior critical point, and optimal selector norm one, yet
one individual oriented edge grows faster than \(N^2/30\).  Its
pole-subtracted holomorphic remainder carries the entire failure.

## Programme split

    PPKERNEL105110
      Straight-edge exterior simple-pole cancellation and exact corner
      failure.  Closed finitely by L-105110.

    PPRESIDUE105110
      Weighted residue ell-one and corner-separation certificate.
      Closed as a conditional finite-edge implication by L-105110.

    PPREMAINDER105110
      Bound the pole-subtracted weighted edge remainder.  Structurally
      independent and refuted as automatic by R-105110; open for Xi.

    XICONTINUE105110
      Continue the Xi weighted quotients meromorphically across each open
      rectangle edge and authenticate all exterior principal parts.  Open.

    XICORNER105110
      Prove corner separation or a paired two-edge corner cancellation
      ledger.  Open.

    XICANCEL105110
      Combine weighted exterior-residue sums with a cofinal remainder
      estimate on authenticated Xi windows.  Open.

    XICOFINAL105110
      Combine oriented edges with Green-Gram selector costs, correction
      terms, multiplicity defect, and strict jet coherence.  Open.

## Boundary

    exterior simple-pole kernel cancellation       PROPOSED EXACT / REVIEW PENDING
    corner separation is dispensable               REFUTED
    quotient supremum decay is necessary            REFUTED BY FINITE FIXTURE
    manifest/parity/selector force edge cancellation REFUTED
    Xi weighted meromorphic continuation             OPEN
    Xi exterior principal-part residue ledger        OPEN
    Xi pole-subtracted remainder estimate             OPEN
    Xi paired-corner cancellation                      OPEN
    cofinal strict jet coherence                       OPEN
    RCMV104530                                         OPEN
    Riemann Hypothesis                                 UNPROVED

No Xi edge estimate, cofinal cancellation theorem, RCMV104530, or RH
conclusion follows.
