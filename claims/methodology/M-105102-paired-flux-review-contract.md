# M-105102 — Hostile review contract for paired coherence flux

Claim ID: M-105102

Status: **REVIEW METHODOLOGY**

Created: 2026-08-23

RH status: **unproved**

Reject T-105102 if any item below fails.

## First-residue ledger

- \(P_F=F/F'\), with no \(F''\)-poles.
- A simple \(F'\)-zero contributes \(F/F''\).
- A common numerator zero is removable and contributes zero.
- The real moment has the sign
  \(\mathcal M_{1,F}=-\Phi_{1,F}+C_{1,F}\).
- \(\Phi_{1,F}\) is the uncorrected boundary charge, not the corrected carrier
  called \(A\) in draft PR #720 L-104522.
- \(C_{1,F}\) includes every nonreal in-window \(F'\)-zero and is not silently
  discarded.

## Boundary signs

- The counterclockwise traversal agrees with L-105101.
- Top and left parameters are reversed.
- Under definite parity, \(P_F\) is odd and opposite edges reinforce.
- The integrated \(p=z^2+1\) oracle must yield

      horizontal contribution = -1/pi + 1/4
      vertical contribution   =  1/pi + 1/4
      total first charge       = 1/2

- Either edge-sign mutation must fail.

## Paired quotient

- The second denominator is exactly \(B_F-C_{2,F}-D_{2,F}\).
- \(C_{2,F}\) uses algebraic squares at nonreal points, not moduli.
- The positive part is applied after the exact first-moment correction.
- A squared negative first moment is not called a transfer carrier; comparison
  with the literal RCMV104530 square requires a separately positive first
  moment.
- The zero-denominator case is not assigned a coherence value.
- Direct L-104522 transfer also checks common-zero freedom and
  \(F(-T)F(T)\ne0\).
- The \(x^5-x^3+x\) firewall must cancel the false boundary carrier through
  \(C_{1,F}=-2/25\).
- The thin-strip route may set \(C_{1,F}=C_{2,F}=0\) pointwise, but it must not
  be called an asymptotic boundary estimate.

## Scientific boundary

- PR #720 is draft post-freeze context, not an integrated dependency.
- The Xi specialization is conditional on local window hypotheses.
- Direct fixed-window identities do not transport the global root ledgers.
- No favorable sign, asymptotic estimate, strict coherence margin,
  RCMV104530, or RH conclusion follows formally.
