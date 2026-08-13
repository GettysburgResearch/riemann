# L-91372 — The finite CFFP butterfly dual is a convex endpoint potential

Status: **proved exact finite-cone reduction; feasibility certificate still required; RH unproved**

Let `a_T` be the endpoint atoms, with positive mass `alpha_T` and strictly ordered state nodes `r_T`. The adjacent moment-neutral butterfly is

\[
\mathcal B_T=c_T^-a_{T-1}-a_T+c_T^+a_{T+1},
\]

where

\[
c_T^- =\frac{\alpha_T\theta_T}{\alpha_{T-1}},
\qquad
c_T^+ =\frac{\alpha_T(1-\theta_T)}{\alpha_{T+1}},
\]

and

\[
r_T=\theta_Tr_{T-1}+(1-\theta_T)r_{T+1}.
\]

For an arbitrary endpoint linear functional `y=(y_T)`, put

\[
g_T=\frac{y_T}{\alpha_T}.
\]

Then exactly

\[
\boxed{
\langle y,\mathcal B_T\rangle
=\alpha_T\left[
\theta_Tg_{T-1}+(1-\theta_T)g_{T+1}-g_T
\right].
}
\]

Therefore

\[
\boxed{
\langle y,\mathcal B_T\rangle\ge0\text{ for every }T
\iff
(g_T)\text{ is convex on the ordered nodes }r_T.
}
\]

This identifies the dual cone of nonnegative adjacent-butterfly intensities with discrete convex potentials.

## CFFP consequence

On one factor-54 generation, `L-91320/L-91321` convert every no-upward parity transport into

```text
nonnegative butterfly intensities;
one nonnegative upper-boundary measure;
exact ordinary and radix-four destinations;
nonnegative score gain.
```

Hence a failure of the Hall/butterfly CFFP route has a finite Farkas witness consisting of:

1. nonnegative multipliers on the physical row and detail constraints;
2. their pullback endpoint cost `y_T`;
3. a normalized convex potential `g_T=y_T/alpha_T` on the endpoint grid;
4. a strictly positive pairing with the required interval/boundary packet.

The endpoint entropy density is itself strictly convex in `r`, so every nonzero butterfly has positive score. Thus score cannot be the source of infeasibility; every separating witness must use an actual physical row, ordinary/detail column, or boundary-port constraint.

Because one reset uses only the endpoint grid through `55`, the dual witness is finite. A claimed positive producer can be reviewed by checking finitely many directed inequalities, while a failed producer must return an explicit convex-potential separator.

This gives a third, independent closure programme:

```text
Hall transport -> interval seed -> butterfly packet
 -> finite row/detail feasibility
 -> no convex-potential separator
 -> bounded local CFFP debt.
```

It does not rely on global canonical-row positivity or on the provenance hazard decomposition.

```text
butterfly dual = convex potential             EXACT
butterfly score is favorable                  EXACT / L-91102
interval/boundary factorization               EXACT / L-91321
finite fail-closed CFFP certificate            EXACT REDUCTION
absence of every physical separator            OPEN / FINITE
Riemann Hypothesis                              UNPROVEN
```
