# R-25802 — Absolute recovery across the oversized-`V` wedge is not a proof

Claim ID: `R-25802`  
Title: The exact depletion resolvent cannot be converted into a top-source estimate by one absolute `mu_V` charge unless the depleted field is controlled uniformly with the original truncation parameter on every shifted block  
Status: **EXACT SCOPE CORRECTION OF THE FIRST `T-25801` DRAFT**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Issue: #258  
Targets: the absolute-recovery shortcut in the initial PADT draft  
Dependencies: `L-25803`; elementary block geometry

## 1. Exact recovery remains valid

For

\[
T=T_{K,V},
\qquad
Z=a_Q*T,
\]

`L-25803` proves coefficientwise through `V^K`

\[
\boxed{T=H_Q*\mu_V*Z.}
\tag{R-25802.1}
\]

This identity is retained.

## 2. The tempting absolute bound

In the square-root normalized physical field, (R-25802.1) formally gives

\[
\|T_J\|
\le
\sum_{a\le V}{|\mu(a)|\over\sqrt a}
\sum_{r\ge0}Q^{-r/2}
\|Z_{J-\log a-r\log Q}\|.
\tag{R-25802.2}
\]

The first factor is `V^(1/2+o(1))`. It is tempting to combine it with a bound
for `Z` at the current scale `J` and claim a `1/K` energy loss.

That step is invalid.

## 3. Oversized truncation at shifted blocks

The same `V` is used in every term of (R-25802.2). If

\[
V=e^{J/K+O_K(1)}
\]

and `a` is near `V`, then the shifted block has location

\[
y=J-\log a
=\left(1-{1\over K}\right)J+O_K(1),
\tag{R-25802.3}
\]

while

\[
V^{K-1}=e^{y+O_K(1)}.
\tag{R-25802.4}
\]

Thus at the lower edge of the recovery wedge the same truncation parameter has
full top-order capacity. The reciprocal-free expansion of `Z` need not contain
a free lattice of positive scale there.

A current-block estimate for

\[
Z_{K,V,Q}(J)
\]

therefore says nothing about

\[
Z_{K,V,Q}(J-\log a)
\]

uniformly for all `a<=V`.

## 4. Why this is the original balanced obstruction

At the lower edge (R-25802.3), the `K-1` truncated slots can carry the complete
output scale. Taking absolute values in (R-25802.2) has simply moved the
all-truncated balanced corner from the original top source into the recovery
wedge.

Consequently the statement

```text
Z is reciprocal-free at the current block
+ one absolute mu_V charge
-> T has exponent 1/K
```

is not established.

The exact identity does not fail. The proposed norm inference fails.

## 5. Correct use of the depletion identity

Retain instead the one-step identity

\[
\boxed{
D_{K,V,Q}
:=(\varepsilon-\delta_Q)*T_{K,V}
=\mu_V*Z_{K,V,Q}.}
\tag{R-25802.5}

In the physical field,

\[
\boxed{
T_J
=Q^{-1/2}T_{J-\log Q}+D_J.}
\tag{R-25802.6}

If `log Q=delta J+O(1)`, the first term is at a fixed smaller logarithmic scale
and also carries the normalization factor `Q^-1/2`.

The load-bearing theorem should therefore estimate the complete signed dipole
`D`, using the reciprocal-free potential `Z` and the signed `mu_V` transport,
rather than estimate `Z` and recover by absolute values.

## 6. Corrected PADT frontier

A valid `PADT(K,J)` certificate proves

\[
\|D_J\|^2
\le
\exp\{(\eta_K+o_K(1))J\}
\left[
1+\max_{u\le(1-\delta_1)J+C_K}E_K(u)
\right]
\tag{R-25802.7}
\]

with `eta_K->0`, while retaining the exact factorization

\[
D=\mu_V*Z.
\]

Then (R-25802.6), not (R-25802.2), supplies the fixed-scale recurrence.

## 7. Exact disposition

```text
exact source-specific depletion resolvent       retained
absolute one-coordinate recovery bound          rejected
reciprocal-free potential Z                      retained
signed mu_V transport for D                      open / load bearing
fixed-scale dipole recurrence                    exact
PADT family -> RH after correction               conditional complete
RH                                               unproved
```

## 8. Proof boundary

This correction does not refute the depletion mechanism. It prevents the
balanced tensor from being hidden in an absolute recovery wedge and sharpens the
remaining theorem to a direct signed estimate for the fixed-scale dipole.
