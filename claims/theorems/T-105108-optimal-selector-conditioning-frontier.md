# T-105108 — Optimal-selector conditioning frontier

Claim ID: T-105108

Status: **PROPOSED EXACT FINITE-WINDOW LEDGER; COFINAL CONTROL OPEN**

Created: 2026-08-23

Depends on: L-105107; L-105108; R-105108

RH status: **unproved**

## Result

Assume \(\mathcal T\ne\varnothing\).  If \(\mathcal T=\varnothing\),
L-105107 gives \(W_*=0\) and \(\tau=0\), and all target-indexed ledgers
below are vacuous.

The L-105107 optimal selector norm now splits into two authenticated finite
loads.  The full-event Green normalization is

\[
|y_c|
=|\gamma_c|r_\Omega(c)^{d_c-1}
\exp\!\left(\sum_{a\ne c}n_ag_\Omega(c,a)\right),
\qquad
g_\Omega=-\log\rho_\Omega,
\tag{T-105108.1}
\]

while target interaction is the exact normalized-Gram operator

\[
\boxed{
\tau=\|G^{-1/2}D_yG^{1/2}\|_2.
}
\tag{T-105108.2}
\]

Writing \(Y=\max|y_c|\), one has

\[
Y\le\tau\le Y\sqrt{\kappa_2(G)}.
\tag{T-105108.3}
\]

Finite Blaschke target cardinals give the unconditional potential envelope

\[
\boxed{
\tau\le
\sum_{c\in\mathcal T}
|\gamma_c|r_\Omega(c)^{d_c-1}
\exp\!\left(\sum_{a\ne c}d_ag_\Omega(c,a)\right).
}
\tag{T-105108.4}
\]

The theorem also supplies exact two-target thresholds, product-separation
and diagonal-dominance bounds, fixed-data domain monotonicity, and
conformal-map-free Euclidean collision bounds.  For one target, the Green
formula is an equality.  For several targets, phases and the complete Pick
matrix remain essential.

On a rectifiable window edge, (T-105108.4) multiplies the unweighted quotient
norm in the L-105107 residue estimate.  Neither factor is estimated
cofinally here.

## Programme split

    GREENLOAD105108
      Exact conformal-radius/positive-Green formula for every forced Pick
      value and the one-target optimum.  Closed finitely by L-105108.

    GRAMOP105108
      Exact normalized-Gram operator, phase-sensitive condition envelope,
      and trace ledger.  Closed finitely by L-105108.

    CARDSEP105108
      Target-cardinal potential upper bound, inverse-Gram/product identity,
      and finite separation criteria.  Closed finitely by L-105108.

    COLLECTIVE105108
      Two-target exact thresholds and a three-target refutation of pairwise
      sufficiency.  Closed finitely by L/R-105108.

    DOMAIN105108
      Fixed-manifest domain monotonicity and one-target Euclidean collision
      bounds.  Closed at the stated finite scope by L-105108.

    XIGREENGRAM105108
      Authenticate Xi manifests, rectangle conformal data, Green loads,
      product separation, phases, and joint Gram operators cofinally.  Open.

    XIQUOTEDGE105108
      Prove quotient-edge decay strong enough after multiplication by the
      selector envelope.  Open.

## Boundary

    positive-Green local normalization              PROPOSED EXACT / REVIEW PENDING
    normalized-Gram exact optimum                   PROPOSED EXACT / REVIEW PENDING
    target-cardinal potential envelope              PROPOSED EXACT / REVIEW PENDING
    product/Gram conditioning identities            PROPOSED EXACT / REVIEW PENDING
    pair restrictions replace full Pick PSD         REFUTED
    local magnitudes determine multipoint optimum    REFUTED
    fixed smooth geometry removes collision debt     REFUTED
    Xi event and conformal manifest                  OPEN
    cofinal Xi Green–Gram bound                      OPEN
    Xi quotient edge estimates                      OPEN
    cofinal strict jet coherence                    OPEN
    RCMV104530                                      OPEN
    Riemann Hypothesis                              UNPROVED

Historical Green claims with a factor-two convention and accepted actual-Xi
Pick claims with a different kernel are not dependencies.  No RCMV104530 or
RH conclusion follows.
