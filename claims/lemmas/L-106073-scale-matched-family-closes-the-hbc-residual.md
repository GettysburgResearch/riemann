# L-106073 — Retraction of the quartic-to-quadratic scale-matched family adapter

Claim ID: `L-106073`  
Status: **RETRACTED AFTER HOSTILE SELF-AUDIT**  
Created: 2026-08-25  
Retracted: 2026-08-25  
Superseded by: `R-106071`, `L-106074--L-106075`, `T-106071`  
Programme issues: #743, #736, #737  
RH status: **unproved**

The first version of this file claimed that the scale-matched quartic
matched-pair occupancy in `L-106071--L-106072` controlled the quadratic
Dirichlet-character family moment and hence `HBCQDSP102888`.

That claim is false.

## 1. First invalid interface

For one block-colour packet, exact character orthogonality gives

\[
\frac1{\ell-1}
\sum_\chi\|V_\chi\|^2
=
\sum_{r\ne0}
\left\|
\sum_{Pc^2\equiv r}Z_{P,c}
\right\|^2.
\tag{L-106073.R1}
\]

This is quadratic in the source atoms.

The quantity bounded in the first `L-106071.8` and `L-106072.6` was

\[
\ell
\sum_{P,Q,d}
\|Z_{P,c(d)}\|^2\|Z_{Q,d}\|^2,
\tag{L-106073.R2}
\]

which is quartic.  The asserted adapter from (L-106073.R2) to
(L-106073.R1) is impossible by homogeneity and fails on the explicit
many-owner one-residue fixture in `R-106071`.

The first invalid displayed statement was the claimed CROP-to-family estimate
that appeared as equation `(L-106073.6)` in the attempted closure version.
It was not proved by `T-106060`; `T-106060` only identified a quadratic
same-root-residue obligation and left it open.

## 2. Why line injectivity is insufficient

The scale-matched modulus proves that, for a **fixed owner pair**, each
collision line is a partial matching of actual cores.  It does not prevent
many different owners from contributing parallel vectors to the same physical
residue cell

\[
r=Pc^2\pmod\ell.
\]

That coherent owner sum is exactly what the quadratic norm in
(L-106073.R1) measures.

## 3. Valid results retained

The following parts of the attempted packet remain valid:

```text
R-106070 source-order firewall;
L-106070 linear block/colour prime palette;
L-106071 core-line partial matching;
L-106072 diagonal conductor payment;
L-106072 quartic Hilbert--Schmidt tensor bound;
X-106070 finite palette/matching/payment replay.
```

None of them, alone or together, proves the quadratic owner-residue Gram.

## 4. Correct replacement

`L-106074` proves the exact conclusion-facing normal form

\[
\mathcal Q_{\mathcal B,A}
=
\sum_{r\ne0}
\left\|
\sum_{Pc^2\equiv r}Z_{P,c}
\right\|^2.
\]

Its diagonal is conductor-paid, and `L-106075` closes every residue cell
containing only `X^(o(1))` distinct owner packets.  The remaining theorem is
high-crowding quadratic owner assembly `HQORO106071`, stated in `T-106071`.

## Exact correction

```text
claimed HBC logarithmic L2 in first L-106073       RETRACTED
claimed HBCQDSP102888 closure                       RETRACTED
claimed RH composition in first T-106070            RETRACTED
quadratic residue normal form                       PROVED IN L-106074
low owner-crowding sector                           PROVED IN L-106075
high owner-crowding sector                          OPEN / RH-BEARING
Riemann Hypothesis                                  UNPROVED
```

This file remains in the tree as a permanent provenance record so that the
same homogeneity error cannot silently reappear.