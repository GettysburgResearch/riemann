# R-99100 — Current and survival coefficients cannot be counted as recursive score debt

Claim ID: `R-99100`  
Status: **PROVED EXACT TYPE FIREWALL**  
Created: 2026-08-19  
RH status: **not assumed**

For rough weights `r_i`, the causal coefficients satisfy

\[
s_k+\sum_i\lambda_i=1,
\qquad
\alpha_i=r_i\lambda_i.
\tag{R-99100.1}
\]

The exact physical identity is

\[
P=s_kP+
\sum_i\lambda_i(P-r_iU_iP_i)+
\sum_i\alpha_iU_iP_i.
\tag{R-99100.2}
\]

Only the `alpha_i U_iP_i` packets are later recursive states. The survival and
current-difference terms are current-owned physical rows.

If all three coefficient families are incorrectly treated as recursive mass,
then

\[
s_k+\sum_i\lambda_i+\sum_i\alpha_i
=1+\sum_i\alpha_i>1
\tag{R-99100.3}
\]

whenever an active rough prime is present. No contraction or debt induction is
possible in that untyped bookkeeping.

Likewise, replacing the actual branching tree by one distinguished sequence

\[
X/(d67^j)
\]

is not an owner identity when the live children use varying primes. Such a
sequence can be used only as a scale majorant, not as the literal source path
on which score debt telescopes.

The correct theorem is `L-99100`: current mass is charged locally, alpha-child
mass carries descendant debt, and exact target-mass conservation supplies the
Bellman envelope.

This firewall does not refute PR #620's local causal identity. It forbids an
incorrect proof of its all-depth score bound.
