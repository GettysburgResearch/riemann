# Four-adic endpoint-packing RH proposal v1

This directory is the standalone publication packet for `T-94200`.

## Scientific status

This is an **unconditional proof proposal**, not an accepted proof of the Riemann Hypothesis. No RH-equivalent estimate is listed as an assumption. The one new load-bearing argument is the first-crossing adjacent estimate `L-94200`; its proof is included in `main.tex`, but it has not been independently reconstructed. A defect there invalidates the proposal.

The proposal combines:

- the exact native radix-four von Mangoldt dual `L-91378`;
- positive parabolic endpoint atoms from `L-26201`, strengthened to positive radix-four detail by `L-94100`;
- the exact all-scale finite compiler `L-94101`;
- the sparse-dual summability theorem `L-19885`;
- the one-sided endpoint consumer `T-91313` and its reviewed prime-square/Mellin-Landau inputs;
- new `L-94200/T-94200` first-crossing and logarithmic-deficit arguments.

## Build

```bash
./build.sh
```

The build fixes `SOURCE_DATE_EPOCH=1786867200` (2026-08-16 08:00:00 UTC).

## Replay

```bash
./replay.sh
```

Expected status:

```text
PASS_T94200_FOUR_ADIC_ENDPOINT_PACKING_CANDIDATE
RH_CANDIDATE_UNDER_UNREVIEWED_FIRST_CROSSING_LEMMA
```

The finite replay is a regression and mutation firewall, not a proof of the all-scale first-crossing lemma. It checks exact integer support/recurrences and 70-digit finite instances through endpoint 512.

## Review order

1. Equation (4.9), the normalized cross-ratio estimate, residue class by residue class.
2. Equation (4.10), the target-ratio analogue.
3. The cancellation using the least live minimizer.
4. The diagonal response bound and sparse `Y_4` sum.
5. The exact endpoint-deficit orientation.
6. Prime-square moat, Mellin normalization, and Landau transfer.
