# T-99980 — Dual closure assault: quadratic envelope and phase-Hasse cross-core symbol

Claim ID: `T-99980`  
Status: **UNCONDITIONAL STRUCTURAL ADVANCE; TWO FINAL PRODUCERS OPEN**  
Created: 2026-08-20  
Base: PR #668 at `15719b975115ecad1b23264c6a6303899b4c99dc`  
Sibling freeze: PR #670 at `f5d37a5f1880749dd33b103d98e2d85bac60ae28`  
RH status: **unproved**

## Route A — quadratic envelope

`L-99980` proves that eventual nonnegativity of

\[
\mathcal E_2(X)
=
16\frac{1-67^{-3/2}}{\zeta(3/2)}X-\mathfrak H_2(X)
\]

implies RH. `L-99981` proves every one-prime block, every two-prime block,
every fully coactive block, and the exact inactive-tail decomposition.

The complete remaining arithmetic statement is the finite activation gate

\[
\mathrm{FEAG99980}.
\]

It is a one-sided upper-envelope theorem for the already positive quadratic
SHARP transform, not the critical negative-mass estimate itself.

## Route B — phase-Hasse cross-core transport

`L-99990` constructs the exact permutation-invariant Hasse flow. `L-99991`
computes its complete phase symbol and proves that every potential boundary
annihilates the neutral cube residual through the factor

\[
1-p^{i\gamma}.
\]

The remaining arithmetic statement is

\[
\mathrm{PSCP99990},
\]

a subpower nonzero-phase packing estimate for the explicit Euler-product symbol
against the fixed zero-safe box transform.

## Conditional conclusions

\[
\boxed{\mathrm{FEAG99980}\Longrightarrow RH,}
\]

and, on the frozen normalized-box/Mellin consumer,

\[
\boxed{\mathrm{PSCP99990}\Longrightarrow RH.}
\]

The two routes are logically distinct:

- Route A is a future upper envelope for a globally positive quadratic
  transform and uses activities \(p^{-3/2}\).
- Route B is a critical native \(p^{-1}\) cross-core transport with exact
  zero-phase cancellation.

```text
quadratic envelope identities                 PROVED EXACT
one- and two-prime envelope positivity        PROVED EXACT
fully coactive envelope positivity            PROVED EXACT
FEAG99980 mixed activation theorem             OPEN / CONCLUSION-BEARING

symmetric random-order Hasse flow              PROVED EXACT
closed phase product symbol                    PROVED EXACT
neutral phase annihilation                     PROVED EXACT
PSCP99990 nonzero-phase packing                OPEN / CONCLUSION-BEARING

Riemann Hypothesis                             UNPROVED
```
