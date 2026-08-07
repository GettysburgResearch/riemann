# R-22801 — The truncated Bohr packet without its endpoint tail cannot prove RH

Claim ID: `R-22801`  
Status: **PROPOSED SCOPE FIREWALL**  
Authoring agent: `gpt56-pro-20`  
Created: 2026-08-07  
Issue: #228

## Invalid shortcut

The exact positive Bohr/Jordan factorization applies to

\[
S_D(x)=\sum_{d\le D}\mu(d)(\{x/d\}^2-1/3).
\]

It is tempting to combine

\[
\mathcal B_D\ll D
\]

with a generic local-to-global principle and declare the analytic-totient second moment closed. This is invalid unless the two completed channels

\[
\frac13M_D,
\qquad
x^2R_D,
\]

where

\[
M_D=\sum_{d\le D}\mu(d),
\qquad
R_D=\sum_{d>D}\mu(d)/d^2,
\]

are retained in the same localized quadratic form.

For `x<=D`, the exact identity is

\[
2E^{\rm AN}(x)
=1+S_D(x)+M_D/3+x^2R_D.
\]

The separate unconditional estimates for `M_D` and `R_D` are far too large at the critical second-moment scale. Their useful smallness comes from cancellation against the low Farey-frequency portion of `S_D`, not from isolated absolute bounds.

## Required semantics

A valid proof must use one of:

1. the completed packet `mathscr C_D` of `L-22801`;
2. the equivalent finite totient-ramp representation of `E^AN`;
3. another exact identity which retains the same endpoint cancellation before taking a norm.

The following substitutions are not valid:

- replacing `E^AN` by `S_D/2`;
- choosing an enormous denominator cutoff and bounding the tail absolutely;
- using the full-period mean of `S_D` as the physical dyadic moment;
- proving the transference only for frequencies bounded away from zero;
- assuming a Mertens estimate stronger than the theorem being proved.

## Review consequence

`T-22801` is load-bearing precisely because it includes the completed endpoint rows. A reviewer who verifies only the nonzero Farey determinant calculation has not verified the proposed RH proof.