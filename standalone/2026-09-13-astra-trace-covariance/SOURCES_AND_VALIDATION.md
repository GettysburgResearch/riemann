# Sources, actual scope and replay contract

Date: 2026-09-13. Status: PROPOSED pending independent mathematical review.
Repository: GettysburgResearch/riemann. Intended parent: PR866 at
`cb05d3052611bd1804459887e84fdec3cb7064af`. Main observed at
`f99d9e3908dde4865377c75d9ca051c1f545bf4f`.

## Frozen mathematical sources

1. DG26, PR866, parent SHA above,
   `standalone/2026-09-12-astra-polynomial-degree-growth/PROOF.md`,
   Git blob `c68170e2dacd23c188c9e71482e51fe63566b587`.
   The full supplied local proof was read, and the current remote definitions,
   monomial formula and blob identity were checked. It supplies the identical
   K, phi, S_N and the proposed subpower-to-RH consumer. Its executable
   companion has now been uploaded by another agent; that uploader's scoped
   validation is attributed, not presented as a run in this continuation.

2. PR869, `5e559c9cbf5aee84ff7ed78dc91b55df744aef56`,
   `standalone/2026-09-12-four-route-deep-pass/arithmetic.md`.
   The relevant arithmetic chain, sharper exponent account, diagonal/covariance
   distinctions and S_N=o(N) argument were read. Its original arithmetic
   `BOUNDARY_CHANNELS.md` at `6603f8b04f9a2d073123a328ac0298a498c93a96` was also
   read. These are comparison inputs, not an independent acceptance of all
   claims in that four-route PR. No old computation was rerun.

3. A fresh updated-PR search returned 15 items: #869, #881, #880, #879, #878,
   #842, #877, #875, #876, #874, #866, #873, #872, #871, #870. Apart from the
   sources explicitly read above, this was metadata/description reconnaissance
   only. In particular the reciprocal-xi subordinator, infinite Ising
   completions, Newton-tail completion price and branching/gamma defect work
   are not imported as mathematical premises or independently reviewed here.
   The current PR866 and PR869 full heads were read directly. Other heads
   mentioned in the search results were not individually re-fetched.

4. Terence Tao, *A remark on partial sums involving the Mobius function*,
   arXiv:0908.4323, published in Bulletin of the Australian Mathematical Society.
   https://arxiv.org/abs/0908.4323
   https://doi.org/10.1017/S0004972709000884
   The primary abstract and published theorem summary were inspected. The
   prime-subsemigroup bound and PNT-based limit are explicitly IMPORTED:
   for the odd source, |m(x)|<=1 and m(x)->0. No RH is assumed. The diagonal
   theorem itself instead rederives its elementary squarefree counting input.

5. Classical Legendre recurrence, orthogonality and antiderivative identities;
   classical Hardy-adjoint inequality, Parseval, elementary Euler products,
   Markov and Borel--Cantelli. The exact identities needed for the new primitive
   energy are proved in the manuscript rather than treated as numerical data.
   For classical special-function context, NIST DLMF Chapters 14 and 18;
   https://dlmf.nist.gov/18.9 and https://dlmf.nist.gov/18.3 .
   This is not a comprehensive priority review. No claim is made to invent
   those classical tools or random multiplicative-function analysis.

No third-party PDF or font is redistributed. All files in this addition are
newly authored text or generated arithmetic receipts.

## New claims and exact boundaries

| ID | Claim | Boundary |
|---|---|---|
| TC26-1 | Exact primitive norm and explicit concentration error, all j | A Legendre/Hardy statement, not a Mobius cancellation bound |
| TC26-2 | Native direct diagonal c0 H_N+C_* with explicit summable error and safe-value constant | No upper bound on the signed covariance |
| TC26-3 | Complete source-ordered covariance and finite terminal correction/tail | Common cutoffs retained; not an absolutely convergent double sum |
| TC26-4 | Both native termwise sign parts diverge as log^2 of source cutoff | Does not refute a bound on the fully recombined covariance |
| TC26-5 | Random-prime reference has expected trace D_N and almost-sure log-times-loglog growth | Not the literal all-negative prime assignment or an RH proof |

The original source trace/rank exponents and the latest classical S_N=o(N)
refinement are NOT claimed as new. The direct diagonal is not the other
programmes' coalesced-product diagonal. No proof of the all-source/full-degree
covariance target or fixed power saving is claimed.

## Checker's arithmetic and scope

`check.py` uses only Python's standard library. Its principal finite tests are:

- 8192 sieve-versus-trial Mobius comparisons and 8192 complete-prefix
  squarefree-count error controls;
- 32 Rodrigues-versus-recurrence Legendre constructions with exact primitive
  energies, exact boundary values and exact ordinary primitive energies;
- 36 exact finite Parseval upper controls;
- 16 complete finite source/covariance panels, including 80 rational point
  comparisons against direct divisor-interval integration;
- three finite Euler-Walsh models, each averaging all eight prime-sign
  assignments, not randomly sampled configurations;
- all 16 native S and diagonal columns, with five reported cumulative trace
  cutoffs 1,2,4,8,16. Cross terms in each polynomial norm are all included.

Native numerical intervals use 512-bit OUTWARD dyadic integer arithmetic.
Machin's formula and alternating arctangent remainders enclose pi. Bernoulli
recursion plus classical exact even-zeta values give the native trace.
The diagonal's squarefree moments are directly summed through 8192, with
EVERY omitted tail bounded by M^(1-s)/(s-1); its second moment additionally
uses the exact 12/pi^2-1 formula and is checked against a full-tail direct
sum enclosure. No floating point enters acceptance. Results are rounded
outward to a 100-bit presentation grid. Formula for C_* is not numerically
certified by this finite protocol.

Both finite polynomial multiplication/integration and direct physical
source intervals are checked. This is one program with separately structured
arithmetic paths, NOT two independent author implementations. The true trace
values use one Machin/Bernoulli primitive path; no second independent high-
precision special-function implementation is claimed. A noncertifying mpmath
scout was used only to inspect candidate finite values, not in acceptance.

The mathematical infinite limits, diagonal asymptotic and random-source theorem
are written arguments. Finite substitutions do not machine-prove them.

## Execution record

The initial full reconstruction reached a receipt-presentation comparison and
raised TypeError because a decimal string was passed as a rational numerator.
The conversion was corrected before any successful receipt was recorded. This
failure is not counted as a pass. A dead exploratory expression was also removed.
One transcribed upload candidate for results.json had two incorrect digits. Its
Git blob identity failed comparison before any commit or branch update. The
replacement blob matches the tested canonical file exactly; the mismatching
unreferenced object is not included in the published tree.

The final normal, -O and -OO accepting commands reconstruct the entire expected
payload from primitive definitions. Each self-test accepts the pristine
receipt, rejects ten DISTINCT resealed modifications through the same acceptance
function, and rejects a duplicate JSON key. These are in-process refusal tests,
not ten independent CLI subprocesses. Canonical JSON comparison distinguishes
booleans from integers; floating input is rejected.

The same-author calculations and source manifests do not constitute independent
mathematical review. No full authenticated repository checkout, repository-wide
validator run, remote CI result, Lean build, zeta-zero computation or unbounded-
degree numerical campaign is claimed. Fresh isolated packet and patch/ZIP tests
are scoped delivery checks, not substitutes for those unavailable executions.

Publication must be verified from the actual remote branch after the non-force
update. The parent files, canonical statuses, other branches and workflows
must remain unchanged. Any publication SHA is recorded in the PR receipt,
not invented in this pre-publication document.

## Final canonical receipt

The fully reconstructed semantic SHA-256 is
`057c43716df4b62cf0d1be722bf2c98ca652a99885e84ea11fd11c0477ee686f`.
The six-file addition is authenticated by MANIFEST.sha256 for its five other
files. Manifest validation is a separate delivery operation, not silently
attributed to the arithmetic checker. The displayed decimal table is rounded
outward from the canonical dyadic intervals. The manuscript's explicit C_*
is a symbolic theorem, not a directed numerical entry in that table.
