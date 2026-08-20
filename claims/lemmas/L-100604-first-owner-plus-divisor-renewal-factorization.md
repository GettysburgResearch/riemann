# L-100604 — A first-owner future monomial is a dilation, not a divisor restriction

Claim ID: `L-100604`  
Status: **WITHDRAWN AS STATED; EXACT TYPE FIREWALL PROVED**  
Depends on: PR #652 `L-99601`; PR #671 `L-99961`  
RH status: **unproved**

The exact sequential first-owner identity is

\[
\prod_i(I-r_iU_i)f
=s_kf+\sum_i\lambda_i(I-U_i)
\prod_{h>i}(I-r_hU_h)f.
\tag{L-100604.1}
\]

Expanding the future product gives

\[
\prod_{h>i}(I-r_hU_h)f
=
\sum_d \mu(d)d^{-1/2}U_df,
\tag{L-100604.2}
\]

where `d` ranges over future-prime subset products.  Each `U_df` is a **dilation of the owner-frozen base packet**.

PR #671 instead proves a positive factorization for the restriction

\[
\sum_m\beta(dm)m^{-z},
\tag{L-100604.3}
\]

which selects multiples of `d` in the already assembled native coefficient sequence.  Equations (L-100604.2) and (L-100604.3) are not the same operation.

A minimal test is decisive: for `f=e_1`, the future monomial `U_de_1=e_d` is one labelled atom, while the divisor-restricted beta tail in (L-100604.3) has an infinite Euler-supported quotient sequence whenever `beta(d)!=0`.  No positive renewal identity turns one into the other.

Consequently the former formulas

\[
\Delta_i^{\rm fut}f
=\sum_d\beta(d)\mathcal P_{i,d}f
\]

and the claimed reduction `FCHD67 -> ODSB100604` are withdrawn.

## Surviving statement

The coefficient-exact first-owner identity (L-100604.1) remains valid and retains the complete future Euler profile.  PR #671's divisor renewal may be inserted only after a separate source theorem produces a literal divisibility restriction.  It cannot be used merely because a future monomial has been labelled by the same integer `d`.
