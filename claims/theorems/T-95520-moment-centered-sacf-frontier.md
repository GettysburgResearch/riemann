# T-95520 — Moment-centered SACF is the sharpened Q4 frontier

Claim ID: `T-95520`  
Status: **UNCONDITIONAL STRUCTURAL ADVANCE; SACF REMAINS OPEN**  
Created: 2026-08-18  
Depends on: PR #580; `L-95520/L-95521`; `R-95520`  
RH status: **unproved**

For every fixed `M>=1`, apply `(I-S)^M` to the annular Q4 packet and to its
balanced separated coprime correlation. Call the resulting exact gate
`SACF^[M]`.

Then

\[
 \boxed{
 \mathrm{SACF}^{[M]}
 \Longleftrightarrow\mathrm{SACF}
 \Longrightarrow\mathrm{FOCC}
 \Longrightarrow\mathrm{OCHD}
 \Longrightarrow\mathrm{RH},
 }
\tag{T-95520.1}
\]

where the first equivalence allows a fixed change of logarithmic exponent.
The transformed kernels have `M` arbitrary vanishing moments at `z=0`, while
retaining the intrinsic order-two/order-one cancellation at `z=1/2`.

The Type-I prime channel is exactly centered against `d(theta-t)`. However,
`R-95520` proves that no further finite scale filter with only polylogarithmic
inverse cost can increase the order of the `z=1/2` zero. Therefore the
remaining balanced coprime Type-II correlation cannot be closed by another
safe annular/filter layer alone; its proof must exploit the Möbius signs,
coprimality, future-prime structure, or a genuinely new arithmetic input.

```text
arbitrary boundary zero moments             PROVED EXACT
polylog inverse equivalence                  PROVED EXACT
continuous prime mode in J0,J1              CANCELLED EXACTLY
first log prime mode in J0                   CANCELLED EXACTLY
additional safe-line zero by stable filter  IMPOSSIBLE
centered balanced coprime Type-II SACF       OPEN / RH-BEARING
Riemann Hypothesis                           UNPROVEN
```
