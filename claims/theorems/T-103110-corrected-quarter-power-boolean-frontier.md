# T-103110 — Corrected quarter-power Boolean frontier

Claim ID: `T-103110`  
Status: **CORRECTED EXACT NORMAL FORM; ONE RH-BEARING PHYSICAL RESTRICTION OPEN**  
Created: 2026-08-26  
Supersedes: historical quarter-power `T-103080` conclusion  
Depends on: `L-103110--L-103112`, binding `R-103110`, parent `T-102990`  
RH status: **unproved**

## 1. Exact mathematics retained

On every dyadic physical/owner block, the quarter-power cutoff

\[
V_A=\left\lfloor(2Y/A)^{1/4}\right\rfloor
\]

has two exact properties:

```text
fixed-owner/core Type-I lattice:      subpower;
balanced equal-pair source:            support-empty.
```

The arbitrary-cutoff Boolean identity and cutoff-transfer identity remain
coefficient-exact.

## 2. Binding correction

The complementary Type-I field is indexed by the canonical owner pair and its
cutoff varies with that owner block. The frozen Type-I theorem controls each
fixed owner/core lattice (or the historical unpaired Type-I source). It does
not prove that the coherent physical collapse across different owner products
is subpower.

The same-occurrence pair multiplicity theorem cannot supply that missing
cross-product restriction. This is the first broken arrow in historical
`L-103070.6` and `L-103072.5`.

## 3. Exact new normal form

Because the balanced source vanishes, `L-103112` proves

\[
\boxed{
H_{\rm harm}^{\rm eq}
=
\sum_A
\mathcal O_{K_L}[\Pi_AE\mathcal T_{V_A}]
+H_{\rm closed}.
}
\]

Define

```text
QPTI103112:
  after exact carrier, equal-product, repeated-label, squared-activity and
  terminal recombination, the coherent physical sum of the block-dependent
  quarter-power Type-I lifts has subpower logarithmic negative mass.
```

Then, at the frozen exact/polylogarithmic transfer scope,

\[
\boxed{
\mathrm{QPTI}_{103112}
\Longleftrightarrow
\mathrm{BCI}_{102990}
\Longleftrightarrow
\mathrm{HMO}_{102940}
\Longrightarrow
\mathrm{RH}.
}
\]

The quarter-power method therefore supplies a sharp alternative coordinate for
the final arithmetic current, not a proof of that current.

## 4. Relation to PR #756

PR #756's corrected physical-squareclass contract is consistent with this
boundary. A successful family attack must retain the full products `Pc^2` and
`Qd^2`, correlate distinct fibres before squaring, preserve the varying-
conductor signed recombination, control Wick contractions, and isolate the
principal member. Its current FFPS/CYSEL and Wick-family results do not prove
`QPTI103112` or `BCI102990`.

## 5. Exact status

```text
quarter-power fixed-fibre endpoint          PROVED
quarter-power balanced support              PROVED EMPTY
cutoff-transfer algebra                     PROVED EXACT
complete owner assembly in old proposal     UNPROVEN / GAP
QPTI103112                                  OPEN / RH-BEARING
BCI102990                                   OPEN / RH-BEARING
historical T-103080 complete conclusion      SUPERSEDED
Riemann Hypothesis                          UNPROVED
```
