# SEP26 — improve a zeta proportion, not another RH criterion

**Proposed proof requiring independent review. RH is not proved.**

The previous moment-cone work was published in #875. Its fixed-dimensional
certificates and alternative closure criteria did not prove the missing
unbounded native estimate. This continuation deliberately does not extend
that sequence of finite moment fits.

Instead it strengthens the existing simple-critical-zero proportion argument:

| Deduction | Lower bound for simple critical zeros / all zeros |
|---|---:|
| Imported optimized trace baseline | 0.6725007036794116... |
| Pinned seven-point / 269-block deduction | 0.6730085279277797... |
| Pinned review's 280-block deduction | 0.6730096522791369... |
| **New separated-core transfer** | **0.6730583253156109...** |

All entries refer to asymptotic proportions in `(T,2T]`, with the denominator
counted with multiplicity. The new proposed distinct-zero bound is
`0.8365291626578054...`. The increment over the pinned 280-block result is
about **0.0048673 percentage points**, not a large jump toward 100%.

## The change that produces the gain

The rank-stability defect equals squared Gram energy only when eigenvalues
are at most two. Previous fixed-size blocks paid a spectral clipping loss.

For points separated by at least 2/3, a single elementary Fourier majorant
bounds the WHOLE Gram norm below two at every cardinality. Other points are
paired inside their close clusters and pay more than their pressure share.
This gives, for the literal Montgomery--Taylor kernel and every finite set,

    tr Psi(M) + span/500 >= (19/5000)(number_of_points-6).

The proof transfers this estimate to the actual tapered finite-grid vectors
using Loewner domination by the full grid. It does not sum an entrywise o(1)
error over a growing matrix to claim a small operator norm.

Read [PROOF.md](PROOF.md), especially Sections 2--4, then
[VALIDATION.md](VALIDATION.md) and [SOURCES.json](SOURCES.json).

## Dependencies and boundaries

The seven-point inequality is inherited from ainta and the independently
implemented repository replay. It is rerun here, not claimed as newly found.
The finite-Gabor number-theoretic trace and tail estimates are the named
imports from the August 10, 2026 primary paper's Theorem D/Section 4.
No new unproved RH-strength estimate is inserted in the deduction. However,
this is not independent referee acceptance of the old analytic preprint or of
the new manuscript. No exhaustive originality/world-record claim is made.

The all-cardinality kernel transfer is the new proved-on-paper component;
its correctness still merits independent review. The packet changes no
canonical/formal status and proves none of the old three routes' missing
Mertens-energy, all-order Ising, or gamma-defect estimates.

## Reproduction

From this directory (ordinary mode shown):

```bash
python -S -B verify.py
python -S -B test_verify.py
python -S -B verify.py --full-seven /path/outside/packet/seven.json
```

Add `-O` before the script for optimized mode. Default verification repeats
all new bounded rational controls and checks the stored seven-point receipt.
Only `--full-seven` repeats the exhaustive continuum certificate. The test
suite's CLI acceptance and refusal tests are bounded, not full seven-point
searches. See the execution record for what actually ran.

The vendor sources are byte-identical copies from the pinned main branch,
with attribution and authenticated hashes. They use dyadic transcendental
bounds AND outward-rounded binary64 range-minimum/accumulation operations;
this is not an all-rational search or an independent new implementation.
