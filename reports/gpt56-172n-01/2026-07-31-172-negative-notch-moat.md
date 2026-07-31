# Negative-route notched-filter checkpoint

Agent: `gpt56-172n-01`  
Issue: #172, with the issue #171 terminal-prime criterion as analytic context  
Branch: `agent/gpt56-172n-01/172-negative-notch`  
Starting hypothesis: A finite strip-safe notch ladder, followed by directed
prime-side evaluation, might produce a sign-separated support or a finite
mean-square block incompatible with the RH zero spectrum.

## Approaches attempted

1. Reconstructed the explicit-formula normalization and support bookkeeping
   from PR #165 and claims `T-15404`--`T-15405`.
2. Built a finite exact-rational ten-notch convolution-square filter and used
   an exact first-ten zero census plus the positive reciprocal-zero identity
   to bound every nontrivial-zero residue.
3. Added two strip-safe `q=8` translated differences which annihilate the
   first two shifted trivial zeros and move the useful raw-prime domain to
   `x>=18`.
4. Ran complete `10^7` prime-power FFT reconnaissance and an independent
   exact-rational high-pass experiment.
5. Audited the proposed finite-block mean-square fallback and replaced the
   invalid Bohr-limit comparison by the full finite sinc/Gram inequality.

## New results

Proved facts, conditional only where explicitly stated in the claims:

- `R-17201` gives a one-frequency counterexample to treating the limiting
  Bohr variance as an upper bound for a finite block.
- `M-17201` records the corrected RH finite-block ceiling, retaining every
  zero--zero, zero--trivial, and trivial--trivial cross term.
- Each profile notch of width `r` enlarges the convolution-square terminal
  support by `2r`, not `r`.

Certified computational facts, conditional on RH and the stated raw explicit
formula:

- `L-17201/X-17202` constructs an exact 14-box profile and proves
  `sum_rho |Ghat(i gamma)| < 4e-18`, `|Q_G(x)|<1e-17` for `x>=28`, and the
  deliberately coarse all-real theorem constant
  `|Q_G(x)|<18000` for every real `x`.
- The exact rational replay gives total nontrivial contribution
  `3.9866375159027520374e-18`; 320-bit Arb certifies ten disjoint count jumps,
  `N(14)=0`, `N(52.9)=10`, and the reciprocal-zero constant.
- `L-17202/X-17203` adds two safe annihilators with zeros only on
  `Re z=-5/2,-9/2`, support endpoint `<6499/600`, and proves
  `|Q_G8(x)|<6e-18` for every `x>=18`.
- `L-17203/X-17204` certifies one hundred disjoint count jumps and `N(237)=100`.
  Direct 320-bit transform balls plus the positive Hadamard remainder sharpen
  the same filter to `|Q_G8(x)|<3.5e-26` for every `x>=18`; the computed upper
  enclosure is `3.4781388191451717897e-26`.
- `X-17201` independently produces a zero-table-free rational envelope
  `B_G=1.0393217045517102e-7` for its matching two-notch/high-pass filter
  beyond support.

## Candidate counterexamples

None.  No exact sign-separated support and no corrected finite-block
mean-square violation was certified.  The checkpoint verdict is `UNRESOLVED`,
not a claim for or against RH.

## Certified computations

- `X-17202`: exact `Fraction` replay plus python-flint/Arb 0.9.0 at 320 bits;
  four fail-closed mutation tests.
- `X-17203`: exact inherited rational replay; six fail-closed mutation tests.
- `X-17204`: exact dependency/hash precheck, 320-bit hundred-zero Arb replay,
  explicit outward ball endpoints, and eight fail-closed mutation tests.
- `X-17201`: seven exact-core tests and a duplicate-free 665,134-record
  prime-power manifest with SHA-256
  `ad1fe1520966ca5c41885166f4a28a0d543922f087881175c0c15e89425fc56a`.

The Arb census presently has one numerical backend.  All claims depending on
it remain `PROPOSED`.

## Failed approaches

- The matching high-pass `10^7` scan had range
  `[-1.4359116748533417e-14, 1.4008960266677526e-14]`, only about
  `1.38e-7` of its rigorous envelope.  There was no candidate to direct.
- A separate 320-bit first-hundred refinement enclosed that filter's complete
  RH line contribution below `1.494e-14`; at the apparent FFT minimum the
  first-hundred value was `-1.37345054697737e-14` and the rigorous higher-zero
  allowance was `9.409e-16`.  The FFT point lies inside the permitted interval,
  so the earlier first-fifty crossing is conclusively not a witness.
- The `q=8` FFT scans disagreed across resolutions by `1.777e-9`, over eight
  orders above the `6e-18` moat.  Their apparent excursions shrink with
  resolution and are explicitly classified `NON_DIRECTED`.
- Exact generalized Irwin--Hall support evaluation becomes impractical for
  the full multi-box, 665,134-prime-power ledger.
- A finite block exceeding the asymptotic Bohr variance would not be a valid
  RH contradiction; finite sinc cross terms can almost double the one-mode
  variance on short blocks.

## Potential errors

- `T-15404` and its finite-spline extension remain proposed analytic
  dependencies, although `L-17201` supplies a direct distributional
  derivation from the classical `psi_0` formula for this `C_c^26` spline.
- The Arb zero census and `xi` enclosure need an independent backend before
  promotion.
- A prime-side witness at `1e-26` scale needs directed high-precision spline
  evaluation; complex128 FFT inversion is categorically inadequate.
- Cumulative zero-count upper bounds may not be subtracted to create shell
  counts, and multiplicity enters a limiting variance quadratically.

## Files changed

- `claims/lemmas/L-17201-rational-ten-notch-rh-moat.md`
- `claims/lemmas/L-17202-q8-trivial-annihilator-tail-moat.md`
- `claims/lemmas/L-17203-hundred-zero-q8-tail-moat.md`
- `claims/refutations/R-17201-bohr-variance-is-not-a-finite-block-bound.md`
- `claims/methodology/M-17201-corrected-directed-finite-block-bound.md`
- `experiments/X-17201-directed-notch-negative/`
- `experiments/X-17202-rational-ten-notch-moat/`
- `experiments/X-17203-q8-two-trivial-annihilator/`
- `experiments/X-17204-hundred-zero-q8-moat/`
- this report and `.gitignore`

## Claims affected

Added `L-17201`, `L-17202`, `L-17203`, `R-17201`, and `M-17201`.  `R-17201` narrows the
permissible interpretation of the finite-block suggestion following
`T-15405.9`; it does not refute the qualitative mean-square/RH equivalence.

## Recommended next actions

1. Build a directed 160--256-bit prime-side evaluator for the `q=8` filter on
   `[18,18.118]`, using common-error interval convolution rather than
   independent pointwise widening.
2. Independently reproduce the zero census with a second Turing/argument-
   principle implementation.
3. Formalize the `psi_0` distributional derivation as a reviewed finite-
   regularity replacement for the smooth-window dependency.
4. If mean square is revisited, certify the complete finite Gram matrix and a
   pointwise residual before comparing it with an exactly integrated prime
   block.

## Organizational improvement ideas

- Distinguish profile support cost `sum r` from convolution-square manifest
  cost `2 sum r` in every scheduler artifact.
- Require every mean-square experiment to label either `BOHR_LIMIT` or
  `FINITE_BLOCK_GRAM`; never use one as the other's bound.
- Standardize result metadata for `EXACT_RATIONAL`, `ARB_DIRECTED`, and
  `NON_DIRECTED_FLOATING` so a visually tiny number cannot be mistaken for a
  certificate.

## Publication status

Publication initially paused because the local `gh` CLI is absent.  The user
then supplied the authenticated GitHub plugin explicitly for the push; the
checkpoint was resumed through local Git plus the plugin's PR API.  No
unrelated worktree changes were present.

## Handoff

HANDOFF FROM: `gpt56-172n-01`  
HANDOFF TO: any directed-numerics verifier  
CURRENT CLAIM OR CANDIDATE: `L-17203` / `X-17204`  
BLOCKING STEP: evaluate the finite prime-power statistic on a nondegenerate
support at substantially better than `1e-26` absolute error  
FILES TO READ: `L-17201`, `L-17203`, `X-17203/results/recon-fft2p18-2p20-1e7.json`,
and `X-17204/results/verification.json`  
FAILED ATTEMPTS: complex128 FFT at two resolutions; generic two-notch/high-pass
candidate; direct generalized Irwin--Hall exact support evaluation  
MOST PROMISING NEXT MOVE: a common-error Arb convolution/sweep over the complete
`10^7` manifest, exploiting repeated box widths rather than independently
widening 665,134 spline values  
MAIN ANALYTIC OR NUMERICAL RISK: catastrophic cancellation is at least seventeen
digits beyond binary64, and a point sample is not a sign-separated support  
POSSIBLE ORGANIZATIONAL IMPROVEMENT: standardize a reusable directed finite-
spline sweep certificate with manifest, knot, derivative, and support ledgers

## Memory-bounded evaluator sketch

The repeated-width structure avoids the naive `2^28` inclusion--exclusion
table.  If the 14 profile widths are `r_j`, then, up to the exact translation
and normalization, the convolution-square density is

```text
sum over k in {0,1,2}^14 of
  (-1)^sum(k) product_j binomial(2,k_j)
  * (u - sum_j k_j r_j)_+^27.
```

There are exactly `3^14 = 4,782,969` weighted rational knots.  Sort those
knots once.  Sort the eight translated query streams generated by the
665,134-record prime-power manifest, giving at most `5,321,072` queries.
During one merged sweep maintain the 28 prefix moments

```text
M_j = sum_(s<u) weight(s) * (-s)^j,  0<=j<=27.
```

Then each spline value is the 28-term binomial evaluation of
`sum_j binomial(27,j) u^(27-j) M_j`.  No per-query copy of all prefix moments
is needed.  Exact common-denominator integer knot keys plus 256--512-bit Arb
query balls should keep the principal arrays below one gigabyte.  Ambiguous
query/knot orderings must trigger interval subdivision, and a directed
derivative bound must inflate a certified point sign into a nondegenerate
support.  This is the concrete next implementation target; it is not yet a
certificate.
