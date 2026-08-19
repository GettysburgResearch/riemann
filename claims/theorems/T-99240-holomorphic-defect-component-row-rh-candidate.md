# T-99240 — Holomorphic-defect common-parent component-row RH candidate

Claim ID: `T-99240`  
Status: **PROPOSED COMPLETE UNCONDITIONAL PROOF CANDIDATE — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-19  
Base: PR #636 at `387f775f95d5e21e01c3fb39d91acc5b67f62b02`  
RH status: **not established by publication**

## The single new mechanism

Resolve the endpoint-nested Hall/causal source tree into a nonnegative physical
row, but do **not** require the finite/continuum calibration to be positive.
Keep every cell error, activation-knot atom and Volterra boundary mode in one
signed calibration ledger.

At each node the exact local identity is

\[
E_Y=J_Y+E_YT_Y+C_Y,
\tag{T-99240.1}
\]

where \(J_Y\) is positive, \(T_Y\) acts only on the positive residual-source
sort, and \(C_Y\) is the source-owned signed calibration.

Nilpotence gives

\[
\boxed{
D_X
=
J_X(I-T_X)^{-1}s_X
\ge0,
}
\tag{T-99240.2}
\]

and

\[
\boxed{
c_X
=
D_X+
C_X(I-T_X)^{-1}s_X.
}
\tag{T-99240.3}
\]

PR #638 shows that the complete distributional calibration on the compact
quotient has only finitely many knot atoms and two homogeneous boundary modes.
`L-99240` keeps those modes signed, adds the exact retained-cell formula, and
proves that the complete local calibration is bounded in every fixed row. No
positive two-anchor certificate is required. The root compact source has finite mass and only
\(\alpha\)-children recurse with total mass below \(1/8\). Therefore
`L-99241` gives, for every fixed \(j\),

\[
\boxed{
c_X(j)=D_X(j)+\mathfrak E_X(j),
\qquad
D_X(j)\ge0,
\qquad
\mathfrak E_X(j)=O_j(1).
}
\tag{T-99240.4}
\]

The exact positive signs of the two Volterra anchors and knot atoms are no
longer required.

`L-99242` then proves that the bounded defect has a Mellin transform
holomorphic in \(\Re s>0\), so the nonnegative surrogate \(D_X(j)\) retains
every reciprocal-zeta pole of the full row. Large-row noncancellation and
Landau exclude every off-line zero.

## Composition graph

```text
endpoint-nested canonical packet                 PR #636 / reconstruct
compact Hall source partition                    PR #636 / reconstruct
residual-only factor-67 child partition          PR #636 / reconstruct
finite/continuum + knot + boundary calibration   exact signed ledger
fixed-row calibration bound                      L-99240
child-mass resolved bound                         L-99241
nonnegative surrogate modulo O_j(1)               T-99240.4
fixed-row reciprocal-zeta transform               L-99242
large-row noncancellation                         L-99242
Landau + functional equation                      L-99242
RH candidate
```

## Removed interfaces

```text
positive exact equality-frame anchors      not required
4sqrt(X) literal-score identity            not used
ordinary/detail capacity                   not used
safe-point calibration/thinning            not used
prime-square moat                          not used
```

## Scientific boundary

The argument is candidate-complete once the local endpoint-nested
Hall/common-parent identity and the explicit signed identity
`E=J+ET+C` are independently reconstructed in the actual component rows. The retained finite checker verifies algebraic
interfaces and fail-closed status; it does not establish RH.

```text
fixed-row defect transfer                  proved exact
resolved boundedness                       proved exact on typed mass input
Mellin/Landau pole preservation            proved analytic
local common-parent arithmetic             pending hostile reconstruction
Riemann Hypothesis                         unproved
```
