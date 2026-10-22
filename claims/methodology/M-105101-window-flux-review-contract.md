# M-105101 — Hostile review contract for the entire-window flux

Claim ID: M-105101

Status: **REVIEW METHODOLOGY**

Created: 2026-08-23

RH status: **unproved**

Reject T-105101 if any item below fails.

## Analytic hypotheses

- \(F''\not\equiv0\), and \(F(\bar z)=\overline{F(z)}\).
- Every in-window zero of \(F'\) and \(F''\) is simple.
- No denominator zero lies on an edge or corner of the closed rectangle.
- A common zero of \(F\) and \(F'\) is recorded as a removable zero-residue
  event; it is not silently promoted to the PR #720 transfer regime.
- Multiple derivative zeros require a separate confluent-residue ledger.

## Residues and coverage

- \(Q_F=F^2/(F'F'')\).
- An \(F'\)-zero contributes \((F/F'')^2\).
- An \(F''\)-zero contributes \(F^2/(F'F''')\), including the zero case.
- Every denominator zero is classified as inside, on the finite boundary
  segments, or outside. A supporting line beyond a segment is outside.
- The nonreal correction uses algebraic squares, not absolute squares.

## Orientation

- The traversal is
  \(-T-i\eta\to T-i\eta\to T+i\eta\to-T+i\eta\to-T-i\eta\).
- Top and left edges retain their reversed parameters.
- Schwarz reflection and oddness of \(Q_F\) under definite parity reinforce
  opposite edges; they do not cancel them.
- Reversing the contour reverses \(B_F\).
- \(B_F\) is a contour charge, not an argument-principle index. Pole-free
  edges need not integrate to zero.

## Continuation boundary

- PR #720 is open, draft, and post-freeze context, not an integrated
  dependency.
- The Xi specialization is conditional on the rectangle hypotheses.
- Xi-derivative simplicity and the downstream common-zero exclusion are not
  declared proved.
- The direct entire-function formula bypasses polynomial exhaustion only at
  fixed \((T,\eta)\); it does not transport L-105100's \(V_2,V_4\) ledger.
- No admissible asymptotic strip sequence, correction sign, RCMV104530, or RH
  conclusion follows from the exact identity.

## Executable minimum

The replay must reject incomplete and duplicate \(F'\)- and \(F''\)-root
manifests, denominator roots on finite boundary segments, reversed edge-sign
mutations, and the substitution of absolute squares for algebraic squares.
It must also accept both numerator-removable cases and independently match
the global polynomial residue sum to the L-105100 \(V_2,V_4\) ledger.
