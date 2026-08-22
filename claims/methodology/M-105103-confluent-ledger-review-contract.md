# M-105103 — Hostile review contract for the confluent ledger

Claim ID: M-105103

Status: **REVIEW METHODOLOGY**

Created: 2026-08-23

RH status: **unproved**

Reject T-105103 if any item below fails.

## Local algebra

- Orders `m,r,s` are taken before canceling either quotient.
- Taylor coefficients are `F^(j)(a)/j!`; derivative factors in `V,W` are
  retained.
- `Res P` uses coefficient index `r-m-1`.
- `Res Q` uses coefficient index `r+s-2m-1`.
- A negative index gives zero, but the denominator event remains in the
  manifest.
- The derivative constraints `r>=1 => s=r-1` and
  `m in {0,r+1}` are checked.
- The complete principal coefficients for `1+x^3+x^4` at zero begin

      P: x^-2/3 - 4 x^-1/9
      Q: x^-3/18 - 5 x^-2/27 + 38 x^-1/81

## Unique merged support

- `S1`, `S2`, and `G` are disjoint and cover every distinct zero of `F'F''`
  in the window.
- A multiple `F'` zero, hence a common `F'/F''` zero, is processed once in
  `G`, not once per denominator factor.
- A simple common `F,F'` zero belongs to `G`, even though both Laurent
  residues vanish.
- The simple noncommon real critical count is `R_F^snc`, not the denominator-event
  count and not a multiplicity-weighted count.
- Algebraic squares, never modulus squares, are used at nonreal simple
  critical points.

## Exact reconstruction

- The signs are

      M1^snc = -Phi1 + C1^s + Lambda1^mrg
      M2^snc =  B_F  - C2^s - D2^s - Lambda2^mrg.

- For `1+x^3+x^4`, the local unique-support sum agrees with the independently
  reversed residue-at-infinity series: `Phi1=-3/64`, `B_F=169/4096`.
- The same fixture reconstructs `M1^snc=-229/576` and
  `M2^snc=52441/331776`.
- Dropping either merged Laurent correction fails an exact mutation check.
- `x^3` remains in the event manifest although both quotient residues vanish.
- `x^5-5x+5` and `x^5-5x` have Q pole orders three and one at zero but the
  same residue `-1/4`; residue alone is not an order classifier.
- Normal and optimized Python runs return the same exact artifact.

## Transfer and scientific boundary

- Removing simplicity from the contour identity is not called a proof of
  Xi-derivative simplicity.
- Transfer is withheld if a real `F'` event is multiple or common with `F`.
  Nonreal merged events and `F''`-only merged events may remain corrected.
- Even when the real obstruction set is empty, endpoint nonvanishing,
  positivity, and strict coherence remain separate prerequisites.
- No sign is assigned to either merged Laurent correction without proof.
- No boundary asymptotic, strict coherence margin, RCMV104530, or RH
  conclusion follows formally.
