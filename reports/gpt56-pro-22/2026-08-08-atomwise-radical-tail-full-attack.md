# Atomwise radical-tail attack on the full Riemann problem

Date: 2026-08-08  
Branch: `agent/gpt56-pro-22/237-greedy-carry-parity`  
Primary new files: `L-23717`, `L-23718`, `T-23706`, `M-23703`, `O-23709`

## Executive result

The live repository has consolidated the elementary carry programme to Weighted Shell-Tail Stability (`WSTS`), an RH-equivalent finite prime-sampling theorem.  This pass attacks that scalar before the dyadic shell is assembled.

The parabolic seed is an increasing sum of nonnegative endpoint-scale carry atoms.  For one endpoint `T`, define its target-minus-response residual `e_T(q)`.  The exact new decomposition is

\[
s_{X,Y}(q)=\sum_{T=Y+1}^{X}e_T(q).
\]

Thus one atomwise theorem,

\[
\sum_{z\le p<T}(\log p)e_T(p)\le0,
\]

would make every finite shell tail nonpositive and force the WSTS charge to be identically zero.

This is the proposed **Atomwise Weighted-Tail Order** (`AWTO`).  It is not proved.

## Exact mathematics obtained

### Closed endpoint profile

With `N=T-1` and `ell_T=log(T/(T-1))`, the entire endpoint increment is

\[
F_T(m)=2\ell_T\sqrt m
+4m(T^{-1/2}-N^{-1/2}),
\qquad2\le m\le N,
\]

with the entering endpoint set to zero.  Every column response is

\[
\Gamma_T(q)=
\sum_{kq\le N}[F_T(kq)-F_T(kq+1)].
\]

### Radical-tail coordinate

For

\[
L_z(m)=\sum_{p\mid m,\ p\ge z}\log p,
\]

the weighted prime response is exactly

\[
\sum_{z\le p<T}(\log p)\Gamma_T(p)
=
\sum_{m=2}^{N}F_T(m)[L_z(m)-L_z(m-1)].
\]

This is the correct source-complete finite coordinate.  It retains neighboring divisibility, the ordinary-prime radical, and the squarefull reserve.

### Upper-half closure

For every integer

\[
(T-1)/2<q<T,
\]

the endpoint residual satisfies

\[
e_T(q)\le0.
\]

Hence every positive endpoint violation is already below half scale.  This is unconditional and uses only two elementary logarithmic inequalities.

### Radical-chord front door

Let

\[
D_X=J_X^{\mathbb P}(b_X)-P_X
\]

be the ordinary-prime parabolic deficit.  Define the finite radical prefixes `A_N,C_N,U_N` and margin `mathfrak R_N` in `L-23718`.  Then exactly

\[
D_{N+1}-D_N
=-\log(1+1/N)\,\mathfrak R_N.
\]

Thus the scalar theorem

\[
\mathfrak R_N\ge0\qquad(N\ge2)
\]

would make the deficit monotone, give `P_X>=J_X^P`, produce the sharp prime ramp, and prove RH.  This `RCT` theorem is weaker than AWTO but still RH-bearing.

## Relationship to the repository’s other fronts

### WSTS

AWTO implies `mathcal B_X=0` shell by shell, so it is a strong direct producer for the final WSTS consolidation on PR #276.

### Greedy Slack / DCRS

The mass-slack conservation law on this branch and the cross-route audit identify Greedy Slack with DCRS.  AWTO bypasses the nonlinear greedy blocker map: it certifies each positive endpoint atom directly in the logarithmic prime objective.

### Endpoint-scale frame

PR #265 supplies the essential positivity: each endpoint increment is an actual nonnegative combination of average-binomial rows.  The new theorem asks whether its complete ordinary-prime tail is already below the matching critical target increment.

### Reflected Selberg

Only the lower-half, trace-zero neighboring-radical residue should enter the reflected square.  The upper half is closed directly.  A valid continuation must use the reviewed two-frequency physical block from PR #241 and retain every proper-power/digital correction.

### Base-five cumulative shell

The centered base-five route remains independently present on the branch.  Its finite cumulative state is positive through the retained annulus, but its cofinal Hardy theorem remains open.  AWTO is a different front door: it operates on endpoint derivatives before cumulative inversion.

## Floating reconnaissance

Ordinary double-precision scans found no positive endpoint prime tail at representative endpoints through `T=10000`.  Direct dyadic WSTS charges were zero at tested endpoints through `X=10^6`.  The ordinary-prime parabolic deficit was monotonically decreasing through `X=10^7` in one vectorized floating scan.

These are observations only.  An off-line zero could produce a failure beyond every finite scan.

## Proposed proof architecture

1. Group the lower-half endpoint response into complete quotient layers.
2. Use the radical formula before absolute values.
3. Split complete prime-power entropy from the squarefull/digital reserve.
4. Cancel all affine and endpoint terms using the exact atom profile.
5. Apply the two-frequency reflected square only to the remaining trace-zero fluctuation.
6. Route every nonboundary term to an endpoint at most half as large.
7. Telescope the endpoint ladder.

The review object must display every source and cross term.  The phrases “factorial majorization,” “digital reserve,” or “reflected positivity” are not substitutes for the finite identity.

## Exact status

```text
endpoint atom and shell decomposition      PROPOSED EXACT
radical-tail identity                      PROPOSED EXACT
upper-half endpoint order                  PROPOSED COMPLETE
radical-chord coordinate                   PROPOSED EXACT
AWTO                                       OPEN / RH-BEARING
RCT                                        OPEN / RH-BEARING
AWTO or RCT -> prime ramp -> RH             PROPOSED COMPLETE
Riemann Hypothesis                         UNPROVED
```

No unconditional proof is claimed.  The contribution is a new full-problem front door with an exact finite source and a proved factor-two scale reduction.
