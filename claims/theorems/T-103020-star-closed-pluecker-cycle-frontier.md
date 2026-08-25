# T-103020 — Star-closed Plücker-cycle frontier

Claim ID: `T-103020`  
Status: **MAJOR UNCONDITIONAL HODGE-SECTOR CLOSURE; RH UNPROVED**  
Created: 2026-08-25  
Depends on: `L-102961`; `L-103000--L-103005`; `T-102980`; PR #730 `T-105440--T-105450`  
RH status: **unproved**

The concentrated minimum-owner route previously left one combined star/Plücker curl `COCURL102980`.

`L-103005` closes its complete radial star component.

## 1. Exact remaining owner-gauge current

For one depth-`k` occurrence, `L-102961` gives the orthogonal decomposition

\[
w=g+c,
\]

where:

```text
g  is the complete-graph star component;
c  has zero row sums and lies in the pair-cycle space.
```

The exact energies are

\[
\|g\|^2={2\over k},
\qquad
\|c\|^2={k-3\over k-1}.
\]

By `L-103005`, the physical common-mother observation of `g` is pointwise one-sided, apart from a squared endpoint field of polylogarithmic cost.

Thus every adverse contribution of the minimum-pair owner-gauge change is carried by `c`.

## 2. Four-label localization

PR #730 proves that every row-zero pair current localizes exactly to its four-label Plücker rectangles. Each clean rectangle factors into:

```text
one left endpoint discrepancy;
one middle Euler block;
one right endpoint discrepancy;
```

and `L-105451` identifies the two endpoint discrepancies with nontrivial augmentation local systems. The common positive half-kernel is `TP_2`, so every order-concordant endpoint minor is already one-sided by `L-103003`.

The only remaining rectangles are those whose signed middle-source coefficient creates an order-inverting Plücker minor.

## 3. Canonical remaining theorem

Define

```text
PLC103020:
  after exact carrier, Boolean-Vaughan, common-core, shared-owner,
  owner/core-overlap, endpoint-color and finite-boundary recombination, the
  row-zero Pluecker cycle current supported on order-inverting four-label
  rectangles has subpower logarithmic negative mass in the fixed
  derivative/outer observation.
```

Equivalently, `PLC103020` is the cycle-space restriction of `DORI103010`.

## 4. Implication chain

\[
\boxed{
\mathrm{PLC}_{103020}
\Longrightarrow
\mathrm{COCURL}_{102980}
\Longrightarrow
\mathrm{OICP}_{102960}
\Longrightarrow
\mathrm{HMO}_{102940}
\Longrightarrow
\mathrm{RH}.
}
\]

The owner-gauge-invariant equal-pair route remains

\[
\mathrm{BCI}_{102990}\Longrightarrow\mathrm{RH}.
\]

The two routes now meet on the same literal coprime Boolean core but use different coordinates:

```text
equal-pair coordinate:     BCI102990;
minimum-pair Hodge cycle:  PLC103020.
```

## Exact boundary

```text
common-mother TP2 / Wronskian sign        PROVED EXACT
minimum-pair radial star current           CLOSED ONE-SIDED
squared endpoint boundary                  CLOSED POLYLOG
row-zero cycle localization                PROVED EXACT
order-concordant rectangles                CLOSED ONE-SIDED
PLC103020 order-inverting cycle            OPEN / RH-BEARING
BCI102990 equal-pair Boolean core           OPEN / RH-BEARING
Riemann Hypothesis                         UNPROVED
```

The remaining minimum-owner obstruction is no longer a general owner transfer. It is one explicit row-zero cycle current.