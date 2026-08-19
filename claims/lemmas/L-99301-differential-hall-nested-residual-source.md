# L-99301 — Differential Hall yields one endpoint-nested residual source

Claim ID: `L-99301`  
Status: **EXACT COMPOSITION THEOREM ON FROZEN LOCAL HALL INPUTS**  
Created: 2026-08-19  
RH status: not assumed

Fix one compact factor-67 fibre and an endpoint parameter `s`. Let positive even-source capacities be `a_e(s)>=0`, odd demands be `b_o(s)>=0`, and let the admissible Hall graph be the frozen no-upward graph `e<=o`.

Assume every Hall prefix inequality required by this graph holds pointwise in `s`. Choose a measurable fractional Hall flow `t_{oe}(s)>=0` with

\[
\sum_e t_{oe}(s)=b_o(s),\qquad
\sum_o t_{oe}(s)\le a_e(s).
\]

Define residual source density

\[
r_e(s)=a_e(s)-\sum_o t_{oe}(s)\ge0.
\]

For any component profile `rho_j(s,e)` monotone in the Hall orientation,

\[
e\le o\implies \rho_j(s,e)\ge \rho_j(s,o),
\]

finite algebra gives the pointwise identity

\[
\sum_e a_e\rho_j(e)-\sum_o b_o\rho_j(o)
=
\sum_e r_e\rho_j(e)
+
\sum_{o,e}t_{oe}[\rho_j(e)-\rho_j(o)].
\]

The second term is coefficientwise nonnegative. It is declared current-owned and receives no child coordinate.

Now integrate in `s` only after the pointwise Hall split. Because `r_e(s)ds` is a positive vector measure, restrictions to nested endpoint sets are automatically compatible. This removes the noncommutativity defect that arises when independent cumulative Hall solutions are chosen separately at different endpoints.

Apply the rough-prime causal identity to the residual source measure only. With ordered rough primes `p_i>=67`, `r_i=p_i^{-1/2}`, `s_i=prod_{h<=i}(1-r_h)`, `lambda_i=r_i s_{i-1}` and `alpha_i=r_i lambda_i`, one has

\[
P=s_kP+\sum_i\lambda_i(P-r_iU_iP_i)+\sum_i\alpha_iU_iP_i.
\]

Only the `alpha_i` terms recurse. Since

\[
\sum_i\alpha_i\le r_1\sum_i\lambda_i<67^{-1/2}<1/8,
\]

the recursively owned source mass is strictly subcritical. The current Hall bonus is never duplicated.

Therefore pointwise Hall followed by endpoint integration gives one literal common-parent source compatible with all later child restrictions, provided the frozen compact Hall inequalities and profile monotonicities hold pointwise.
