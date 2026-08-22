# T-105104 — Multiplicity-aware transfer frontier

Claim ID: T-105104

Status: **PROPOSED EXACT TRANSFER BRANCH; XI JET ESTIMATES OPEN**

Created: 2026-08-23

Depends on: L-105103; L-105104; draft PR #720 only as exact-head,
post-freeze research context

RH status: **unproved**

## Result

L-105104 removes the real simplicity and common-zero exclusions from the
structural reverse--Rolle step. Its global jet-coherence form is

\[
N_{\mathbb R}^{\mathrm{mult}}(f;(a,b))
\ge
\mathfrak m_{\mathrm{com}}
+(2\mathfrak C_{\mathrm{jet}}-1)R_{\mathrm{jet}}-1.
\tag{T-105104.1}
\]

Here common derivative-order mass transfers directly, while
\(R_{\mathrm{jet}}\) counts distinct noncommon odd-order turns. The carrier
at a turn of order \(r\) is the leading principal coefficient
\(r!f(c)/f^{(r+1)}(c)\), not the ordinary Laurent residue.

The full derivative multiplicity splits exactly as

\[
N_{\mathbb R}^{\mathrm{mult}}(f')
=\mathfrak m_{\mathrm{com}}+R_{\mathrm{jet}}
+\Delta_{\mathrm{mult}}.
\tag{T-105104.2}
\]

Thus high multiplicity cannot silently inflate the line input: the neutral
defect \(\Delta_{\mathrm{mult}}\) must be controlled.

## Correct continuation gates

    XIJETMAN105104
      Produce the real common/odd-turn/even-stationary event manifest on
      cofinal Xi-derivative windows.

    JETMOM105104
      Estimate the first two leading-principal-part jet moments with a strict
      coherence margin.

    MULTDEF105104
      Control Delta_mult relative to the full derivative line-zero count.

    JETFLUX105104
      Construct a valid local-jet/global-observable bridge. Ordinary contour
      residues Phi_1 and B do not contain the required high-pole coefficients.

    XITRANS105104
      Combine effective turning/common proportions, total-count ratios, and
      the exact transfer inequality without changing support and multiplicity
      conventions.

## Boundary

    arbitrary-multiplicity interval identity      PROPOSED EXACT / REVIEW PENDING
    odd-turn jet sign dictionary                  PROPOSED EXACT / REVIEW PENDING
    multiplicity-aware jet-coherence transfer     PROPOSED EXACT / REVIEW PENDING
    ordinary-residue-only extension               REFUTED BY R-105104
    XIJETMAN105104                                 OPEN
    JETMOM105104                                   OPEN
    MULTDEF105104                                  OPEN
    JETFLUX105104                                  OPEN
    XITRANS105104                                  OPEN
    RCMV104530                                     OPEN
    Riemann Hypothesis                             UNPROVED
