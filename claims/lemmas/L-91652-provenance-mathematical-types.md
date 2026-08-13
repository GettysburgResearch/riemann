# L-91652 — Provenance-labelled mathematical types

Claim ID: `L-91652`  
Status: **PROVED FORMAL TYPE THEOREM**  
Created: 2026-08-13  
RH status: **unproved**

The proof distinguishes a free cone of labelled formulas from the vector of
endpoint quantities obtained after applying a fixed linear map. Coefficient
mass is measured before the map. Endpoint deficit is measured after the map.

For a base label `A` and a prime-labelled difference `C`, define

\[
R(A)=P_X,
\qquad
R(C)=P_X-p^{-1/2}U_pP_{X/p}.
\]

For a positive labelled sum `Z`, put

\[
\widehat\Delta_X(Z)=\Delta_X(RZ).
\]

Linearity of `R`, together with `L-91406`, gives positive homogeneity and
subadditivity of `widehat Delta`.

The reset coefficients of `L-91650` define

\[
A\mapsto s_kA+\sum_i\lambda_iC_i+
\sum_i\alpha_iA_i^{child}.
\]

After applying `R`, this equals `R(A)`. Current coefficient mass is one and
recursive coefficient mass is below one eighth. A `C` label remains current.
The construction extends linearly to positive sums.

This is the formal intermediary between the coefficient ledger and the endpoint
quantities requested by the independent review.