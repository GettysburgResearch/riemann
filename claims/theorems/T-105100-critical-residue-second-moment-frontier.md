# T-105100 — Critical-residue second-moment descent frontier

Claim ID: T-105100

Status: **PROPOSED EXACT FINITE REDUCTION; XI LIMIT AND ESTIMATES OPEN**

Created: 2026-08-23

Depends on: L-105100; PR #720 only as post-freeze research context

RH status: **unproved**

## Result

L-105100 converts the finite-polynomial second moment of derivative-ratio
residues into one complete-root fourth-moment ledger and two explicit
corrections:

\[
M_{2,\mathbb R}(p)
=
\mathcal K_4(p)-\mathcal C_2(p)-\mathcal D_2(p),
\tag{T-105100.1}
\]

where

\[
\mathcal C_2(p)
=\sum_{\substack{p'(c)=0\\c\notin\mathbb R}}
\left(\frac{p(c)}{p''(c)}\right)^2,
\]

and

\[
\mathcal D_2(p)
=\sum_{p''(d)=0}
\frac{p(d)^2}{p'(d)p'''(d)}.
\]

This continues the local contour observable in PR #720 L-104523.3 and is the
second-moment analogue of that branch's centered-variance first-residue
ledger. It advances the open mean-value problem by computing the global
infinity term and naming the exact debts that any root-moment argument must
pay.

## Correct continuation gates

The finite identity reaches the Xi residue-coherence input only after all
four gates below are supplied.

    LOC105100
      Localize the global finite-polynomial identity to a height window,
      retaining exterior residues, contour-side terms and endpoint effects.

    CPASS105100
      Pass the localized quartic root ledger and residue sums through a
      symmetric canonical-product exhaustion, with a justified order for the
      polynomial-truncation and height limits.

    NCR2_105100
      Bound the off-real Xi-derivative squared-residue correction at the
      required scale.

    DCR2_105100
      Bound the Xi second-derivative cross-residue debt at the required scale.

Even these gates address only the second-moment half of RCMV104530. The signed
first moment, a strict coherence margin, and the antecedent derivative-line
proportion remain separate inputs.

## Boundary

    finite second-residue balance             PROPOSED EXACT / REVIEW PENDING
    exact real/nonreal/debt decomposition      PROPOSED EXACT / REVIEW PENDING
    LOC105100                                  OPEN
    CPASS105100                                OPEN
    NCR2_105100                                OPEN
    DCR2_105100                                OPEN
    RCMV104530                                 OPEN
    Riemann Hypothesis                         UNPROVED
