# T-100611 — Audited interval-region implication hypermatrix

Claim ID: `T-100611`  
Status: **PROVED EXACT HYPEREDGES; LONG-INTERVAL ESTIMATES OPEN; RENEWAL REGION WITHDRAWN**  
Created: 2026-08-20  
Depends on: `L-100605`, `L-100610--L-100615`, `T-100610`  
RH status: **unproved**

The exact interval entry is

\[
A_{ij}(X)=
\sqrt{r_ir_j}
(I-U_i)(I-U_j)E_{i+1:j-1}\Psi(X),
\qquad i<j.
\]

The following implication hyperedges survive hostile reconstruction.

## H1 — opposite owner decompositions combine

The first-owner and largest-owner identities are the row and column marginals of one two-ended interval tensor.  This follows coefficientwise from `L-100605` and in positive hazard form from `L-100610`.

## H2 — source tensor and cubic geometry combine

Global monotonicity and convexity of `Psi` make every root, singleton, and zero-interior double-ended term nonnegative (`L-100612`).  All possible negativity therefore lies in nonempty interior prime intervals.

## H3 — endpoint geometry and prime spacing combine

`L-100613` proves every actual interval with `p_j/p_i<=8` nonnegative.  `L-100615` enlarges this asymptotically to

\[
p_j\le p_i^A
\qquad(A<e^{3/4}).
\]

## H4 — opposite collar energies combine

The exact Schur theorem `T-100610` gives

\[
\mathrm{FOCR100610}\wedge\mathrm{LOCR100610}
\Longrightarrow
\text{subpower cubic negative mass}
\Longrightarrow RH.
\]

## Correct regional matrix

| region | exact status | valid tool | remaining obligation |
|---|---|---|---|
| root/singleton/adjacent | positive | cubic monotonicity/convexity | none |
| `p_j/p_i<=8` | positive | exact interval Harnack | none |
| `p_j<=p_i^A`, `A<e^(3/4)` | eventually positive | Mertens interval mass | finite low-prime audit only |
| fully active long entry | centered residual zero | exact carrier subtraction | none |
| long partial-activation collar | signed | double-owner coboundary; balanced completion coordinate | FOCR and LOCR |

## Audit correction

The former table contained a “divisor-exposed positive-renewal” region and identified `HDRB100603` / `ODSB100604` as established projections.  That was incorrect: completion/future monomials are dilations, whereas PR #671 concerns divisor restrictions.  Those rows and semantic identifications are withdrawn.

Finite squaring remains an exact **forward** coordinate inside a long interval, but completed and transition terms must stay in one oriented ledger; no positive desquaring or positive-renewal shortcut has been proved.

```text
coefficient double-owner tensor             proved exact
positive two-ended hazard tensor            proved exact
cubic endpoint and short-interval signs     proved
power-width interval corridor               proved
renewal/desquaring regional arrow           withdrawn
FOCR100610                                  open
LOCR100610                                  open
Riemann Hypothesis                          unproved
```
