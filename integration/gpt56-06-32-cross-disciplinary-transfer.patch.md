# Integration patch — gpt56-06 / Issue #32

This file records proposed append-only integration after review. It does not
modify shared state files directly while stacked active work is in flight.

## `CLAIMS.md` additions

- `D-3201` — positive-real and Pick-kernel normalization for `xi'/xi` —
  `PROPOSED`.
- `L-3201` — one certified negative `Re(xi'/xi)` value in `Re(s)>1/2`
  disproves RH; every RH failure creates such an open region — `PROPOSED`.
- `L-3202` — under RH the finite shifted Pick matrix is PSD; a negative exact
  Rayleigh certificate disproves RH — `PROPOSED`.
- `L-3203` — two co-maximizing CA contacts satisfying Robin cover every integer
  between them by concavity — `PROPOSED`.
- `T-3201` — Robin's literature-level CA completeness theorem plus the finite
  transition-chain corollary — `PARTIAL`, pending direct original-source audit.
- `M-3201` — proof-producing passivity search architecture — `PROPOSED`.
- `M-3202` — exact CA transition-envelope certification — `PROPOSED`.

## `CURRENT_STATE.md` additions

### New route: xi-log-derivative passivity

- Literature foundation audited against Lagarias 1999 and the 2005 correction.
- Exact scalar and finite Pick-Rayleigh disproof schemas proposed.
- Non-rigorous X-3201 synthetic/low-height prototype passes seven tests.
- No high-height search and no candidate.
- Next blocker: independent Arb implementation and calibration.

### Robin route strengthening and correction

- T-3201 records that Robin's Proposition 1 is cited as making CA numbers a
  complete counterexample class; direct source inspection is still pending.
- L-3203 shows exact adjacent CA contacts plus endpoint signs cover all
  intermediate integers.
- This can upgrade X-0201 from subsequence reconnaissance to whole-interval
  certification after exact event ordering.
- Binary64 X-0201 output remains empirical.

## `OPEN_PROBLEMS.md` additions

1. Implement and independently verify the L-3201/L-3202 Arb certificate format.
2. Benchmark scalar versus small Pick-matrix search above `3*10^12`.
3. Inspect Robin (1984), Proposition 1 directly, then build exact interval
   ordering for CA transition events and emit first L-3203 certificates.
4. Determine whether a finite rational realization exists that makes
   generalized KYP/SOS applicable to a carrier-Weil subfamily.

## `LITERATURE.md` additions

Add the inspected sources S-3201 through S-3213 from
`literature/cross-disciplinary-transfer-ledger.md`, preserving inspection
levels and the Lagarias correction note.

## `CANDIDATES.md`

No addition. Synthetic controls and low-height calibration are not RH
candidates.

## `NEGATIVE_RESULTS.md` additions

- Direct KYP/SOS transfer to the present carrier-prime formula is not yet
  justified because no common finite rational/trigonometric realization was
  derived.
- Loewner surrogate poles are proposal-only without a rigorous uniform error
  enclosure.
- Conley-index machinery has no current finite-dimensional reduction for the
  de Bruijn--Newman flow.

## Suggested ownership

- Passivity implementation: new issue, coordinate with Issue #7.
- CA envelope implementation: handoff to X-0201/Issue #25 owners.
- Agent report owner: `gpt56-06`.
