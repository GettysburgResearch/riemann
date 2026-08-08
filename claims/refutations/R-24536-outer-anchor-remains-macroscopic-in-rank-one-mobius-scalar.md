# R-24536 — The unmatched outer-anchor collar is macroscopic even in the rank-one Möbius source functional

Claim ID: `R-24536`  
Title: Passing from ambient atomic norm to signed total source mass removes an unnecessary weight but does not permit the first odd collar to be terminalized before its inside even sibling is recombined  
Status: **EXACT SOURCE-BINDING FIREWALL**  
Authoring agent: `gpt56-pro-25`  
Created: 2026-08-08  
Issue: #245  
Dependencies: `R-24530`, `L-24535`  
Scope: correction of an overoptimistic scalar reading of the commutator boundary

## 1. Same-sign total outer-anchor mass

`R-24530` proves that after the complete positive stopped-endpoint layer cake is
summed, the coefficient at the physical outer anchor `m=3q` has one common
orientation and magnitude at least

\[
{\log(3/2)\over\sqrt{3q}}
\qquad(2\le q\le X/3).
\tag{R-24536.1}
\]

Therefore its signed total satisfies

\[
\boxed{
\left|\sum_m\sigma_X^{\rm outer}(m)\right|
 \ge {\log(3/2)\over\sqrt3}
      \sum_{2\le q\le X/3}{1\over\sqrt q}
 \ge c\sqrt X
}
\tag{R-24536.2}
\]

for an absolute `c>0` and all sufficiently large `X`.

The conclusion uses the sign before absolute values: the displayed family is not
being enlarged by total variation.

## 2. Möbius scalar response

By `L-24535`, the Möbius response of a divisor source lifted by adjacent
commutators is minus its signed total coefficient.  Hence the separated outer
collar contributes

\[
\boxed{
\left|
\sum_{q\ge2}\mu(q)
 L_q(\Phi(\sigma_X^{\rm outer}))
\right|
 \ge c\sqrt X.
}
\tag{R-24536.3}
\]

Thus changing the terminal norm from

\[
\sum_m\sqrt m|\sigma_m|
\]

to the correct rank-one source functional does not by itself close the collar.
It improves the lower bound from `Omega(X)` to `Omega(sqrt X)`, but the latter is
still far above every subpower RH-facing allowance.

## 3. Mandatory inside/outside recombination

For one stopped layer in the band `Y/3<q<Y/2`, the actual residual term is

\[
p_Y(2q-1).
\]

Writing it as

\[
[p(2q-1)-p(3q)]+p(3q)
\tag{R-24536.4}
\]

separates an analytic even/odd pair from the positive cutoff correction.  The
second term alone is the macroscopic family above.  A valid scalar proof must
retain (R-24536.4) as one source object until one of the following has occurred:

1. the paired eta mass has been formed;
2. the exact dyadic zeta filter has been applied;
3. an incoming-source relative Pascal replacement has been exhibited;
4. a lower-scale signed recurrence has been produced.

Terminalizing `p(3q)` first and hoping that a later analytic estimate cancels its
scalar charge is invalid: the sign separation has already destroyed the
required cancellation.

## 4. Relation to the common Hausdorff tail

`L-24534` proves zero debt for the complete decreasing/Hausdorff source tail.
Equation (R-24536.4) explains why that theorem must be applied to the **paired
source**, not to the omitted odd term alone.  The common tail and its cutoff
correction share a square-root-sized scalar component.

The genuine remaining object is therefore a signed parity boundary, not a
small terminal source.

## 5. Consequence for `CBMR`

The recurrence in `T-24508` cannot be proved by the sequence

```text
split analytic pair and collar
-> terminalize collar
-> contract analytic pair.
```

It must instead use

```text
complete analytic/cutoff source
-> eta parity recombination
-> dyadic Mobius filter
-> only then lower-scale routing or estimation.
```

The `2/3` outer-anchor band is a mandatory mutation of any claimed production
ledger.

## 6. Proof boundary

Proved exactly:

- square-root lower bound for the signed outer-anchor total;
- square-root lower bound for its Möbius scalar response;
- necessity of inside/outside source recombination.

Not refuted:

- a complete eta/dyadic boundary recurrence;
- a source-bound relative replacement using actual incoming capacity;
- `CBMR` itself;
- RH.
