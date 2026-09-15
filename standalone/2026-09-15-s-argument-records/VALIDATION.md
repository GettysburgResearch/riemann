# Sources, scope and execution record

Date: 15 September 2026. Programme: SARG26.
Author of this packet: GPT-6 Astra Pro, acting at Gideon's request.

## Pinned repository boundary

Repository: GettysburgResearch/riemann.
Base main: `f99d9e3908dde4865377c75d9ca051c1f545bf4f`.
Base tree: `8bddd12122e8a772683c9ed0b37dbcb945036893`.
Destination: `standalone/2026-09-15-s-argument-records/`.

The pinned README, AGENTS and STATUS were read. Their blob identities are,
respectively, `d5941f749029fab5798dbffe4b609c1594077cbf`,
`c2181ad9ebf037614f3daa8957df640159f8d968` and
`a8d4e57165106e74d7ee224d7e5d972091883301`.
Recent PR descriptions were inspected for context, including the separate
simple-zero-density programmes #887-#890. They are NOT proof dependencies here.
A targeted PR search for the string 4.1843 found no existing import at that time.
This was not an exhaustive audit of all branches or the repository mathematics.

Eight additive files are intended. No main, old research file, canonical or
formal status, settings or workflow is edited. The final PR and verified head
belong in the publication receipt, not as an invented self-referential SHA here.

## Primary and supplied sources

1. `news.txt`: the user's supplied transcription of the X announcement and
   certificates, received 2026-09-15. The numeric lists and text are retained,
   with ordinary paragraph spacing and a final newline. This is not a fetched
   archival export. Its exact SHA256 is in `results.json` and `SHA256SUMS`.
2. Announcement: https://x.com/avi_eisen/status/2099622967751663749
   Certificate reply: https://x.com/avi_eisen/status/2099622971455275255
   Search-index results identified Avraham Eisenberg and the matching exact
   heights, S ranges, and Turing constants. The announcement was indexed as
   14 September 2026. Direct retrieval of both pages returned HTTP 403. We
   therefore corroborate the source link/attribution through indexed primary
   pages, but do not authenticate every supplied byte against the live thread.
   The original source code, execution log and complete numerical endpoint
   enclosures were not obtained. Earlier mirror snippets were only discovery
   leads and are not mathematical or provenance dependencies.
3. Timothy Trudgian, *Improvements to Turing's method*, arXiv:0903.1885v3,
   https://arxiv.org/abs/0903.1885v3 and https://arxiv.org/pdf/0903.1885.
   Theorem 2.2 and its t1>168*pi domain were inspected, including a screenshot
   of printed page 3. The constants 2.067 and .059 are imported analytic inputs.
   The full proof of that published theorem was not independently re-proved.
4. Jonathan W. Bober and Ghaith A. Hiary, *New computations of the Riemann zeta
   function on the critical line*, arXiv:1607.00709v1, 4 July 2016,
   https://arxiv.org/abs/1607.00709v1 and https://arxiv.org/pdf/1607.00709.
   Sections 2-4 and Table 2 were inspected; printed page 7 was viewed as an
   image. This supports the 3.3455 historical comparison, one-sided convention,
   and relevant accelerated/multi-evaluation approach. No authors' computation
   or source build was rerun. No PDF byte hash or exhaustive priority survey
   is claimed.
5. NIST DLMF, https://dlmf.nist.gov/5.11.ii, the complex logarithmic Stirling
   remainder bound. Together with elementary log/atan bounds it gives (2)-(3)
   in RESEARCH.md. This analytic special-function input is explicit; no numerical
   special-function oracle is used by the checker.

The announcement is third-party material and retains its original rights. The
import must not be described as our record discovery or as relicensed MIT text.

## What the checker authenticates

It parses both supplied integer anchors/counts, all 844 coarse brackets and fine
refinements. It checks counts, domains, strict disjointness and anchor adjacency;
the fine endpoint intervals are checked for their QUOTED signs and binding, not
recomputed from Z. It reconstructs both full midpoint integrals, total width
errors, conservative analytic Turing bounds, quoted D enclosures and quoted
strict S ranges. It separately constructs the compressed 310-bracket certificate,
inner cores and adjacent gaps with full theta approximation errors.

Acceptance uses 384-bit outward integer intervals and exact fractions, complete
convergent-series tails, explicit exceptions, and exact typed JSON comparisons.
Duplicate keys, floating input aliases, altered results and scope promotions
are refused. A supplied hash is never used in place of mathematical reconstruction.
The source SHA binds this particular transcription, not the truth of its Z claims.

The output always says primitive_z_replayed=false,
record_independently_certified=false, and rh_established=false.
`--require-primitive` unconditionally refuses. There is no external signed-JSON
bypass and no hidden backend. The reported zero-census/record implications are
conditional on the missing primitive signs and the written analytic proof.

## Executed local checks

Environment: Python 3.13.5 on Linux; production and tests use the standard library.
The ordinary, -O and -OO complete reconstructions all passed and produced identical
JSON output bytes. All three six-method test suites passed, with no failures,
errors or skips. Each suite executed:

- 961 rational point-pair and 64 rational interval-pair arithmetic controls;
- a separate Fraction-series pi enclosure and three logarithmic series controls;
- 448 exact finite monotone-defect staircases, including peripheral missing jumps;
- complete reconstruction of both records and all 310 exact-rational jobs;
- ten altered-source rejections and one insufficient-padding rejection in-process;
- one pristine full CLI acceptance, six altered-result CLI refusals, one duplicate-
  key CLI refusal and one primitive-required CLI refusal (eight refusals total).

The distinct arithmetic/truncation control is the same author's implementation;
it is not an independent analytic review. The finite staircase cases are controls,
not a machine proof of the general monotonicity lemma.

A prior mpmath calculation/scout was non-rigorous and used only for orientation
and choosing padding candidates. It is not part of final acceptance. No attempt
to evaluate a naive 10^14-term Z sum is reported. The initially explored periodic-
Bernoulli remainder route was not needed: the final manuscript uses the explicitly
cited DLMF remainder bound and the conservative 1/t estimate.

Commands from the packet directory:

```sh
python -I -S -B check.py --check results.json --jobs /tmp/sarg26-jobs.tsv
python -I -S -B test_check.py
python -I -S -B -O check.py --check results.json
python -I -S -B -O test_check.py
python -I -S -B -OO check.py --check results.json
python -I -S -B -OO test_check.py
```

## Delivery and exclusions

`SHA256SUMS` covers the other seven files, excluding itself. The sealed archive
and an additive temporary-Git fixture are replayed before publication; their
actual outcome is recorded in the PR receipt. The fixture is not a complete
Riemann checkout. A direct clone failed DNS in this environment; GitHub connector
reads and writes are separate and available.

Not performed: primitive Hardy-Z evaluations at any of the supplied endpoints;
a complete independent S-record certificate; a high-height backend build;
an exhaustive source/priority survey; full repository validation; Lean or remote
CI; independent mathematical referee acceptance; or a search for a new record.
Those missing steps are not hidden behind the scalar margins or the imported
Turing theorem. The next acceptance target is the 620 endpoint replay plus
independent review of the local-completeness and rounding arguments.
