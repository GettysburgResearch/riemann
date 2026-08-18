# T-97700 — Threshold-flexible causality reduces to critical-saddle history transport

Claim ID: `T-97700`  
Status: **UNCONDITIONAL DECISION AND SHARP OPEN FRONTIER**  
Created: 2026-08-18  
Depends on: `L-97700`--`L-97702`, `R-97700`--`R-97701`; PR #587  
RH status: **unproved**

The threshold-flexible causal method is now decided at its stated scope.

1. Every native rough occurrence has one exact first-owner ledger and retains
   its coefficient `p^(-1/2)`.
2. Every threshold contraction must absorb the full `(R-A)F` residual; the
   one-prime `r-2r^2` correction is compulsory when two `r^2` copies have
   already been charged.
3. The root observation is the native annular scalar, not the finite `P_61`
   base.
4. Raw signed exposure is invariant under thresholding.
5. Every even stopping depth with
   `L log L=o(log log X)` has an eventually negative exact current.
6. In particular the `LAPBR67` residual of PR #578 is eventually negative.
7. States with least prime at least `Y^theta`, `theta>e^(-1)`, are positive.

Thus ownership, scale descent, and a contracted `<1/8` recursive budget do not
prove positivity. The stopping line must reach the rough harmonic saddle

\[
L\asymp\sum_{p\le X}{1\over p}\asymp\log\log X.
\]

## Critical-Saddle History Transport (`CSHT67`)

Put

\[
T_k(X)=
\sum_{\substack{m\in\mathcal R_{67}^{\rm sf}\\\omega(m)=k}}
 {1\over\sqrt m}b(X/m).
\]

Then

\[
\mathcal A_X=\sum_{k\ge0}(-1)^kT_k(X).
\tag{T-97700.1}
\]

The next producer is the following source-complete theorem.

> **CSHT67.** For every sufficiently large real `X`, after removing the
> high-least-prime sector of `L-97702`, construct a nonnegative one-use flow
> from odd-depth native occurrences to even-depth native occurrences. Every
> edge must preserve the complete source coefficient, activation, first owner,
> parity, target and scalar coordinates. The flow must cover all odd demand
> and may use each even occurrence at most once.

Equivalently, emit the exact finite Hall/Lorenz primal on the active
critical-depth history DAG, or an exact separating dual. A local terminal
margin, a depth count, or a contracted child norm is not a substitute.

If `CSHT67` holds, (T-97700.1) is nonnegative. The fixed `5:3` annular
Mellin-Landau consumer then gives RH. `CSHT67` is not proved here and carries
the remaining zero-free-strip strength.

```text
native first-owner ledger                  PROVED EXACT
r-2r^2 / (R-A)F residual                  PROVED EXACT
root equals native annular scalar          PROVED EXACT
raw-exposure conservation                  PROVED EXACT
subcritical threshold-depth positivity     FALSE
LAPBR67                                    FALSE
high-least-prime sector                    PROVED POSITIVE
CSHT67 critical-saddle transport           OPEN / RH-BEARING
Riemann Hypothesis                         UNPROVEN
```
