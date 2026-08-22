# T-105101 — Entire-window residue-flux frontier

Claim ID: T-105101

Status: **PROPOSED EXACT FIXED-WINDOW REDUCTION; ASYMPTOTIC CONTROL OPEN**

Created: 2026-08-23

Depends on: L-105101; PR #720 only as exact-head, post-freeze research context

RH status: **unproved**

## Result

Under the regular-rectangle hypotheses of L-105101, every real entire
function \(F\) with \(F''\not\equiv0\) satisfies

\[
\boxed{
M_{2,F}(T)
=B_F(T,\eta)-C_F(T,\eta)-D_F(T,\eta).
}
\tag{T-105101.1}
\]

Here \(B_F\) is the complete counterclockwise boundary charge of
\(F^2/(F'F'')\), \(C_F\) is the algebraic squared-residue sum over nonreal
\(F'\)-zeros in the rectangle, and \(D_F\) is the residue debt at its
\(F''\)-zeros. If \(F\) has definite parity, then

\[
B_F(T,\eta)
=\frac2\pi\left[
\int_0^\eta\Re Q_F(T+iy)\,dy
-\int_0^T\Im Q_F(x+i\eta)\,dx
\right].
\tag{T-105101.2}
\]

For \(F=\Xi^{(k-1)}\), \(k\ge1\), this is a direct fixed-window
representation of the second moment appearing in the draft PR #720
residue-coherence programme, conditional on the stated simplicity and
boundary hypotheses.

## What this closes

The direct entire-function route no longer needs a polynomial truncation in
order to represent \(M_{2,k}(T)\) at one regular \((T,\eta)\). It makes every
interior pole and all four oriented edges explicit.

It does **not** close LOC105100 or CPASS105100 on the separate root-ledger
route. That route aims to transport L-105100's explicit global
\(V_2,V_4\) expression; (T-105101.1) instead replaces it by the unevaluated
boundary charge \(B_F\).

## Correct continuation gates

    XIWIN105101
      Establish or correctly bifurcate the simple-zero and common-zero
      hypotheses needed for the intended Xi-derivative windows.

    UFLUX105101
      Control the horizontal and endpoint terms in (T-105101.2) along an
      admissible height/strip sequence, with a justified choice of eta(T).

    NCR2_105101
      Bound the nonreal Xi-derivative algebraic squared-residue correction.

    DCR2_105101
      Bound the adjacent-derivative residue debt.

These gates address only the second-moment input. The signed first moment,
strict coherence margin, common-zero branch, and antecedent derivative-line
proportion in PR #720 remain separate.

## Boundary

    fixed-window residue ledger              PROPOSED EXACT / REVIEW PENDING
    four-edge and parity reduction           PROPOSED EXACT / REVIEW PENDING
    direct fixed-window Xi specialization    CONDITIONAL / REVIEW PENDING
    LOC105100 root-ledger localization       OPEN
    CPASS105100                              OPEN
    XIWIN105101                              OPEN
    UFLUX105101                              OPEN
    NCR2_105101                              OPEN
    DCR2_105101                              OPEN
    RCMV104530                               OPEN
    Riemann Hypothesis                       UNPROVED
