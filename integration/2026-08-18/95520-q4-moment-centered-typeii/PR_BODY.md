## Purpose

Continue the Q4-only route from PR #580 at exact head
`812e7fcbaff2dd1c2c53c885def7b6c0d0e68a05`.

This add-only packet proves an arbitrary polylog-stable zero-moment tower
`(I-S)^M`, reconstructs the exact intrinsic double/simple zeros of the Q4
kernels at `z=1/2`, and proves a filter barrier: no finite dyadic filter with
only polylogarithmic inverse cost can add another zero there.

Thus the continuous prime mode and the first logarithmic prime mode are already
removed exactly, while further safe filtering cannot close the balanced
coprime Type-II core. `SACF` remains open and **RH remains unproved**.

## Main results

1. `L-95520`: for every fixed `M`, `(I-S)^M` gives `M` exact boundary moments,
   has a finite endpoint inverse of polylogarithmic mass, and preserves the
   conclusion-producing estimate up to a fixed logarithmic exponent.
2. `L-95521`: the frozen Q4 kernels intrinsically have order two and one at
   `z=1/2`; the continuous prime mode is removed before estimation.
3. `R-95520`: a finite dyadic filter that adds another zero at `z=1/2` must
   have power-sized inverse cost and therefore cannot be polylog-stable.
4. `T-95520`: moment-centered SACF is the sharpened, still-open Q4 frontier.

## Replay

```bash
python3 experiments/X-95520-q4-moment-centering/verify.py
sha256sum -c T95520_CONTENT_SHA256SUMS
```

Expected:

```text
PASS_X95520_Q4_MOMENT_CENTERING_ALGEBRA
efd06455c291019ae7a0f500d6cebfe9313e5d58cbec58789aeb4b0b5609f5ad
```

## Collision-safe publication

The supplied route used `95500–95501`, which collides with PR #597. This PR
therefore publishes it as `95520–95521`; see the source lock and provenance
note for the exact map and original hashes. The only additional scientific-file
hardening is explicit UTF-8/LF retained-result output.

Exact-path `.gitattributes` rules keep every route ledger target LF-stable in
fresh Windows checkouts with `core.autocrlf=true`.

PR #595's one-sided subpower/moment-compression result and PR #597's resonance
analysis are related siblings, but neither contains or supersedes this
zero-moment/filter-barrier result.

## Exact boundary

```text
arbitrary boundary zero moments             PROVED EXACT
polylog inverse equivalence                  PROVED EXACT
continuous prime mode in J0,J1              CANCELLED EXACTLY
first log prime mode in J0                   CANCELLED EXACTLY
additional safe-line zero by stable filter  IMPOSSIBLE
centered balanced coprime Type-II SACF       OPEN / RH-BEARING
Riemann Hypothesis                           UNPROVEN
```
