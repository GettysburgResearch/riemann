# T-106110 — One-sided dual-amplified principal frontier and superseded uncentered family conjunction

Claim ID: `T-106110`  
Programme aliases: `LFAM1.DUAL_AMPLIFIED_CONTROLLING_FRONTIER`, `LFAM2.PRIME_PRODUCT_COLLISION_MOMENT`, `STRESS.COMPLETE_OPPOSITE_OWNER_AMPLIFIER`  
Status: **EXACT ONE-SIDED FAMILY REDUCTION; PRINCIPAL GATE SUFFICIENT; UNCENTERED NONPRINCIPAL ATOMIC CLAIM CORRECTED BY `R-106131`; SUPERSEDED BY BILATERAL `T-106140`**  
Created: 2026-08-25  
Corrected: 2026-08-25  
Depends on: `L-106110--L-106113`; `R-106110`; `R-106131`; parent `BCI102990`  
Programme issues: #743, #736, #737  
RH status: **unproved**

The exact one-sided dual amplification remains valid:

```text
complete left-anchor sum
AND complete opposite-owner sum
  -> one additive member
  -> Gauss/even-character decomposition
  -> one square.
```

For each common core `g`, least-discrepancy prime `ell`, and owner quadratic
class `sigma`, the principal member is the native unphased member. Define the
principal source-dual moment

\[
\begin{aligned}
\mathfrak P_{\rm DA}(Y)
={1\over2\pi}
\sum_{g,\ell}g^2\ell
\sum_\sigma
\int|\widehat\kappa(t)|^2
\frac{\ell+1}{\ell-1}
|\mathcal Z_{g,\ell,\sigma,\mathbf1}(t)|^2dt.
\end{aligned}
\tag{T-106110.1}
\]

The source-dual Cauchy argument gives

\[
\boxed{
\mathfrak P_{\rm DA}(Y)=Y^{o(1)}
\Longrightarrow
\mathrm{BCI}_{102990}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-106110.2}
\]

This was the gate `DAPRO106110`. It is sufficient on its own.

## Binding correction to the former conjunction

The first version also required the complete uncentered nonprincipal moment
`DAKUM106110` and claimed that the literal atomic diagonal of the full family
was already paid.

For one atom, however,

\[
\sum_{\eta\ {\rm even}}w_\ell(\eta)=\ell-1.
\]

Thus the complete atomic coefficient is

\[
g^2\ell(\ell-1)|z_\omega|^2,
\]

while the calculation in `L-106112` pays only the bounded principal coefficient

\[
g^2\ell\frac{\ell+1}{\ell-1}|z_\omega|^2.
\]

Accordingly:

```text
DAPRO106110 principal atomic diagonal       paid;
DAPRO106110                                open / sufficient;
uncentered DAKUM106110 atomic diagonal      not paid;
uncentered DAKUM106110                      not a required companion.
```

The exact owner Wick factorization and physical-squareclass collision geometry
remain valid.

## Preferred continuation

The source-symmetric bilateral tensor is `L-106120`. Its corrected
physical-squareclass frontier is `T-106121`. The preferred family repair is
the atomic-free conjunction `T-106140`, which compares:

```text
a Wick-centered additive/CV-XD trace;
a Wick-centered nonprincipal Kummer trace.
```

No claim of RH is made.
