# HIST-QP-T-103080 — Retracted quarter-power Boolean closure proposal

Historical packet label: `T-103080`  
Canonical status: **RETRACTED / SUPERSEDED BY `T-103110`**  
Original landing: `e56c9813`  
Binding correction: `R-103110`  
RH status: **unproved**

The original proposal correctly proved that, for a fixed canonical owner
product, the quarter-power balanced core is outside physical support. It also
proved a subpower Type-I estimate in each fixed owner/core fibre.

It did **not** prove that the block-dependent pair-indexed Type-I fibres may be
collapsed coherently over different owner products. That missing physical
restriction is exactly the RH-bearing harmonic/BCI current.

The corrected live theorem is

```text
claims/theorems/T-103110-corrected-quarter-power-boolean-frontier.md
```

with live gate

```text
QPTI103112 <=> BCI102990 <=> HMO102940 -> RH.
```

The `T-103080` token also collided with the pre-existing `ASPH103080` frontier
named by `R-103010`. The binding identifier map is

```text
integration/2026-08-26/t103080-quarter-power-disambiguation.tsv
```

Do not cite this historical path as a complete theorem or proof of RH. The
original proposal is recoverable from Git history at commit `e56c9813`.