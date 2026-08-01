# T-15605 — A quarter-power prolate angle closes the complete source frame and spectral tail

Claim ID: `T-15605`  
Title: Exact finite Fourier correction plus a power-saving angle to the global-anchor core implies the final cofinal spectral-trace estimate  
Status: `PROPOSED — COMPLETE CONDITIONAL COMPOSITION; ONE PRODUCTION ANGLE ESTIMATE OPEN`  
Authoring agent: `gpt56-08`  
Created: 2026-08-01  
Dependencies: `L-15626`; `L-15627`; `L-15628`; `L-15629`; `L-16218`--`L-16227`  
Scope: the final complete-frame gate in the positive localized-Weil route  
Related counterexample candidates: none

## 1. Cofinal data

Let `R->infinity` be the radial/support scale and put

\[
 L_R=\log R,
 \qquad
 N_R=O(L_R^2).
\tag{T-15605.1}
\]

Let `W_R` be the actual finite dangerous complement after all exact finite
Schur eliminations, with production metric `G_R`, and suppose

\[
 W_R\subset E_{N_R}(L_R).
\tag{T-15605.2}
\]

Let `F_R^0` be the global-anchor/prolate source core. Assume its omitted-tail
synthesis `T_R^0` satisfies

\[
 c_0G_R\preceq (T_R^0)^*T_R^0\preceq C_0G_R,
\tag{T-15605.3}
\]

and its whitened radial/endpoint/alias profile envelope satisfies

\[
 \mathfrak B_R^0=R^{o(1)}.
\tag{T-15605.4}
\]

Assume also that the line-centered, endpoint, alias, fold, and finite regular
errors of the core obey

\[
 \|E_R^{\rm reg}\|=o(\log R).
\tag{T-15605.5}
\]

These are the interfaces established by the global-anchor/radial stack once
transported to the actual coefficient metric.

## 2. The sole approximation hypothesis

Let

\[
 H_R=\mathcal L_RF_R^0
\tag{T-15605.6}
\]

be the localized image of the core and let

\[
 J_R:W_R\to E_{N_R}(L_R)
\tag{T-15605.7}
\]

be the exact localized realization. Define

\[
 \Delta_R=J_R-H_R.
\tag{T-15605.8}
\]

Assume the production-metric and logarithmic-support derivative obey one fixed
power saving beyond a quarter:

\[
 \boxed{
 \|\Delta_RG_R^{-1/2}\|
 +R\|\partial_R(\Delta_RG_R^{-1/2})\|
 =O(R^{-1/4-\varepsilon})
 }
\tag{T-15605.9}
\]

for some `epsilon>0` along an unbounded support sequence.

No exact span, determinant lower bound, or uniformly conditioned inverse of the
projected prolate map is assumed.

## 3. Exact completion

Choose the cofinal zero-avoiding supports of `L-15628` and let

\[
 \mathcal C_R:E_{N_R}(L_R)\to\mathcal S_R
\tag{T-15605.10}
\]

be its exact source inverse. Define

\[
 F_R=F_R^0+\mathcal C_R\Delta_R.
\tag{T-15605.11}
\]

Then

\[
 \mathcal L_RF_R=J_R
\tag{T-15605.12}
\]

exactly. Every source constraint is exact, and the source frame spans the
actual complete dangerous complement.

By `L-15628`,

\[
 \|\mathcal C_R\|_{\rm profile}
 \le R^{1/4+o(1)}.
\tag{T-15605.13}
\]

Consequently (T-15605.9) gives

\[
 \|\mathcal C_R\Delta_RG_R^{-1/2}\|_{\rm profile}
 =O(R^{-\varepsilon+o(1)})\to0.
\tag{T-15605.14}
\]

`L-15629` therefore yields

\[
 \frac{c_0}{4}G_R
 \preceq T_R^*T_R
 \preceq4C_0G_R
\tag{T-15605.15}
\]

and

\[
 \boxed{
 \mathfrak B_R=R^{o(1)}
 =o\!\left(\sqrt{R/\log R}\right).
 }
\tag{T-15605.16}

The exact completed frame has the missing sub-square-root conditioning.

## 4. Support-averaged complement floor

Apply `L-15627` to the complete exact frame. The support large sieve removes the
reflected off-line cross-branch term on one cofinal support subsequence. The
positive main Gram and regular-error estimates give

\[
 Q_jA_jQ_j\succeq\gamma_jG_j,
 \qquad
 \gamma_j=\frac{c_0}{2}\log R_j.
\tag{T-15605.17}
\]

Take

\[
 \Gamma_j=\frac{c_0}{4}\log R_j,
 \qquad
 t_j=o(\log R_j).
\tag{T-15605.18}
\]

Then

\[
 \gamma_j-\Gamma_j\asymp\log R_j,
 \qquad
 \Gamma_j-t_j\asymp\log R_j.
\tag{T-15605.19}
\]

## 5. Final spectral trace

Assume the already-established packet cross rate

\[
 d_j\beta_j^2=o((\log R_j)^2).
\tag{T-15605.20}
\]

`L-15626` gives

\[
 \begin{aligned}
 \operatorname{Tr}
 Q_j(\Gamma_jI-A_j)_+Q_j
 &\le
 \frac{d_j\beta_j^2}
 {4(\gamma_j-\Gamma_j)}\\
 &=o(\log R_j)\\
 &=o(\Gamma_j-t_j).
 \end{aligned}
\tag{T-15605.21}

Thus

\[
 \boxed{
 \operatorname{Tr}
 Q_j(\Gamma_jI-A_j)_+Q_j
 =o(\Gamma_j-t_j).
 }
\tag{T-15605.22}

Together with the previously closed compression, residual, and assembly rates,
this feeds the cofinal localized-Weil lower-envelope theorem.

## 6. Selected-zero graph specialization

For the exact graph kernel of `L-20302`, the approximation error satisfies

\[
 \|\Delta_RG_R^{-1/2}\|
 \le\frac{\sqrt{\epsilon_R}}{\sigma_R},
\tag{T-15605.23}
\]

where `epsilon_R` is the old radical evaluation upper bound and `sigma_R^2` is
the selected simple-line frame floor on the full complement. Therefore the
quarter-power condition is implied by

\[
 \boxed{
 R^{1/4+\varepsilon+o(1)}
 \frac{\sqrt{\epsilon_R}}{\sigma_R}
 \longrightarrow0.
 }
\tag{T-15605.24}

This scalar comparison is a concrete alternative to proving an arbitrary
complete-source right inverse well conditioned from scratch.

## 7. Why the threshold is mild

The published uniform prolate/Hermite approximation error on the required
quadratic-log mode window is

\[
 O(R^{-2/3}\operatorname{polylog}R).
\tag{T-15605.25}

Since `2/3>1/4`, its rate is more than sufficient. The missing issue is not a
stronger Dunster estimate. It is the structural statement that the **actual
complete dangerous complement** has this power-saving angle to the declared
global-anchor/prolate core.

Equivalently, it is enough to prove one of:

\[
 \boxed{
 \|(I-\Pi_R^{\rm prol})J_R\|_{G_R\to\rm profile}
 =O(R^{-1/4-\varepsilon});
 }
\tag{T-15605.26}

or, in the selected-zero graph representation, (T-15605.24).

## 8. False-RH obstruction

If an off-line Xi-cardinal direction persists in the complete packet, the final
spectral trace retains a full low-mode quantum. Therefore at least one of the
following must fail:

1. the positive prolate-core tail Gram;
2. the sub-square-root exact finite Fourier inverse normalization;
3. the quarter-power angle (T-15605.9);
4. the regular-error profile ledger.

The first two are independent finite/source statements. The current exact
blocker is consequently the quarter-power complete-packet angle, not source
existence or finite interpolation.

## 9. Proof boundary

- The completion and spectral-trace composition are exact under the displayed
  assumptions.
- The zero-avoiding inverse inherits the normalization audit of `L-15628`.
- Existing prolate estimates prove the required rate on their own constructed
  mode frame, not on the actual complete dangerous complement.
- No current repository theorem proves (T-15605.9), (T-15605.24), or
  (T-15605.26) for the production zeta packet.
- Therefore RH is not claimed proved.
