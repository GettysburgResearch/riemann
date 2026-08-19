# T-99130 — Reciprocal-Julia single-profile envelope frontier

Claim ID: `T-99130`  
Status: **UNCONDITIONAL EXACT REDUCTION; ENVELOPE OPEN**  
Created: 2026-08-19  
Frozen base: PR #611 at `9d0b0521e5ace8c96df63a85a68f60a789b09923`  
RH status: **unproved**

For every critical quotient state `(Y,z)` of PR #611, define `B_z,R_z,K_2,K_3`
as in `L-99130/L-99131`. Define the reciprocal-Julia common-envelope theorem
`RJCE23` by

\[
\boxed{
(K_2B_z)(Y)\le R_z(Y),
\qquad
(K_3B_z)(Y)\le R_z(Y).
}
\tag{T-99130.1}
\]

By `L-99131`, this is pointwise equivalent to

\[
A_{2,z}(Y)\ge0,
\qquad
A_{3,z}^\sharp(Y)\ge0.
\tag{T-99130.2}
\]

PR #611 already proves positivity outside its critical corridor and supplies
the exact descending-prime quotient recurrence. Hence finite backward induction
gives

\[
\boxed{
\mathrm{RJCE23}
\Longrightarrow
\mathrm{CPQR23}
\Longrightarrow
\mathrm{FPCB23}
\Longrightarrow
\mathrm{LPTRP23}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-99130.3}
\]

The novelty is dimensional: the two conclusion-producing row tails are no
longer independent arithmetic objects. They are two fixed signed kernels acting
on one reciprocal-Julia profile, compared against one positive smooth-number
reservoir. The logarithmic-owner martingale of the reciprocal-Julia compiler is
therefore a common candidate mechanism for both rows.

The theorem does **not** prove `RJCE23`. Source-blind absolute values are too
large, and the signed coefficients in (L-99131.10) forbid a trivial positive
kernel argument. A valid closure must retain the source-index conditional
expectation until after the two fixed observations are priced.

```text
positive dyadic inverse                    PROVED
common signed profile                      PROVED
positive smooth reservoir                  PROVED
two fixed observation kernels              PROVED
primitive-prefix scalar bridge             PROVED
RJCE23                                      OPEN / RH-BEARING
FPCB23                                      OPEN / RH-BEARING
Riemann Hypothesis                          UNPROVED
```
