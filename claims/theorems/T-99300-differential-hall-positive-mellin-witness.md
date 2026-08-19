# T-99300 — Differential-Hall positive Mellin witness closure

Claim ID: `T-99300`  
Status: **PROPOSED COMPLETE COMPOSITION ON FROZEN LOCAL INPUTS**  
Created: 2026-08-19  
RH status: unproved

## Statement

Assume the following previously frozen local inputs survive direct reconstruction:

1. the compact factor-67 Hall prefix inequalities for the native endpoint fibres;
2. monotonicity of the fixed component-row profile in the Hall orientation;
3. the native first-owner coefficient/activation ledger for the Möbius source;
4. same-index child observation under each active rough prime;
5. the fixed-row Mellin identity and noncancellation asymptotic for `P_j`.

Then for every sufficiently large fixed component row `j` there is a nonnegative function `D_X(j)` and an error `E_X(j)` such that

\[
c_X(j)=D_X(j)+E_X(j),
\]

with

\[
\int_1^\infty |E_X(j)|X^{-\sigma-1}\,dX<\infty
\quad(\sigma>0).
\]

Hence any zero of `zeta` with real part greater than `1/2` yields, in some sufficiently large fixed row, a nonreal pole of the Mellin transform of `D_X(j)` in `Re s>0`. Since `D_X(j)>=0`, Landau forces a real singularity at its abscissa of convergence, while the explicit transform is holomorphic on the positive real axis. Therefore no such zero exists; the functional equation then gives RH.

## Construction

Factor each squarefree source index uniquely as `n=d m`, with `d|(P_61)` and every prime factor of `m` at least `67`. Order the rough prime factors of `m`. This is the first-owner label.

At each compact endpoint fibre, perform Hall pointwise in the endpoint parameter. The residual even source becomes one positive endpoint vector measure after integration; the Hall edge bonus is a nonnegative row-only term and remains current-owned.

Partition the residual source by one common random key into disjoint rough-prime children. Apply the exact causal identity. Only alpha-children recurse, with total source mass below `1/sqrt(67)<1/8`; therefore the typed tree is finite/subcritical in mass and no source occurrence is duplicated.

Observe the entire tree in one fixed component row. The ideal first-owner expansion equals the canonical Möbius row by finite Fubini and uniqueness of the source factorization. Finite/continuum, endpoint-anchor, knot and realization discrepancies are kept as signed fixed-row calibration data. PR #641 already proves bounded calibration on the typed mass input; bounded functions lie in the stronger Mellin-holomorphic class required by L-99300. More generally any correction satisfying the displayed `A_+` condition is admissible.

The conclusion then follows from L-99300.

## Firewalls

The proof does **not** use any of the following as a hidden substitute:

- `H(c_X)=4 sqrt(X)` (false; the native equality row has literal score `P_Lambda(X)`);
- independent coordinatewise Hall couplings as one physical parent;
- survival/lambda current terms as recursive descendants;
- positivity of all Volterra knot atoms or both homogeneous boundary modes;
- optional overthinning as a repair for an already-constructed stronger same row.

## Exact review boundary

This theorem introduces no new global asymptotic estimate. Its only non-abstract obligations are the five local frozen inputs listed at the start. Accordingly this publication is a conclusion-oriented candidate, not an assertion that RH has been established.
