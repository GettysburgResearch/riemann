## Checkpoint 4 — merged-support Laurent-residue ledger

Exact checkpoint base:
0c1aedcafe7c6fe384695eee64435cc87b792aea.

This checkpoint removes interior simplicity from the paired contour
identities. At an arbitrary denominator event,

\[
\operatorname{Res}_a(F/F')=[w^{r-m-1}]U/V,
\qquad
\operatorname{Res}_a(F^2/(F'F''))
=[w^{r+s-2m-1}]U^2/(VW).
\]

A finite Taylor recurrence evaluates both coefficients. A single union
support separates simple noncommon \(F'\)-events, isolated simple
\(F''\)-events, and merged exceptional events, giving

\[
\mathcal M_1^{\mathrm{snc}}
=-\Phi_1+C_1^s+\Lambda_1^{\mathrm{mrg}},
\qquad
\mathcal M_2^{\mathrm{snc}}
=B-C_2^s-D_2^s-\Lambda_2^{\mathrm{mrg}}.
\]

The exact replay checks full principal parts, unique-support mutations,
residue-at-infinity and frozen root-ledger oracles, nonreal algebraic squares,
and sign/zero-residue/transfer firewalls:

    PASS_T105103_CONFLUENT_RESIDUE_LEDGER
    15/15 focused tests in normal and optimized Python
    digest e208cceb8b09c639f6587024e5bef334a37d650435453515f68b8f42512c53c2

This closes the contour bookkeeping gap only. Real multiple/common critical
events still require exclusion or a new reverse--Rolle theorem. No favorable
Xi estimate, RCMV104530, or RH conclusion is claimed.
