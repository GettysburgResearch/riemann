# T-96601 — Source-complete annular positivity gives the Riemann Hypothesis

Claim ID: `T-96601`  
Status: **CANDIDATE COMPLETE UNCONDITIONAL RH PROOF PROPOSAL**  
Created: 2026-08-17  
Depends on: `T-96600`; PR #547 `L-96010`, `L-96011`, `T-96010`

For `j=2,3`, PR #547 proves the exact Mellin transform

\[
\int_1^\infty [c_X(j)-c_{X/4}(j)]X^{-s-1}\,dX
=(1-4^{-s})
\left[
 \frac{C_j}{s^2}
 +\frac{P_j(s+1/2)}{s^2\zeta(s+1/2)}
\right].
\]

The factor `1-4^{-s}` has no zero for `Re s>0`. The two finite numerators have
no common zero in the open critical strip: with `x=2^{-z}` their simultaneous
vanishing gives

\[
 -3(x-1)(x-2)=0,
\]

which would force `Re z=0` or `Re z=-1`.

`T-96600` supplies two nonnegative Mellin kernels. Landau's real-abscissa
theorem therefore excludes every zeta zero with `Re z>1/2`; the functional
equation excludes its reflected partner. The proposed conclusion is

\[
 \boxed{\mathrm{RH}.}
\]

Publication is not acceptance. Independent reconstruction should begin with
`L-96600` and the grouped-source induction in `L-96602`.
