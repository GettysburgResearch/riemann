# SR26 source ledger and execution scope

Date: 2026-09-14. Proposed research, not an integrated acceptance.

## 1. Frozen repository and publication verification

Main was read at `f99d9e3908dde4865377c75d9ca051c1f545bf4f`.
The latest prior TC26 work is actually on draft PR866, head
`a27285abe428835ac0171fe9eb8cbbc97a64a33a`, not merely in the local archive.
The six source-file Git blob hashes were recomputed from the supplied
`riemann_astra_trace_covariance.zip` and compared with the connector's frozen
remote directory listing. All six matched. This pass did not rerun that old
checker and does not claim an independent review of all TC26 proofs.

No existing source file, status, review, main, workflow or repository setting is
changed by this addition. Publication uses a separate branch from the frozen
main. The actual new remote commit and PR must be supplied by the publication
receipt; they are not guessed inside this pre-commit file.

## 2. Exact mathematical dependencies and reading depth

### P7 and the existing 280-block baseline

Repository `GettysburgResearch/riemann`, main SHA above:
`reviews/A/supplement/REPORT.md`, Sections S01--S02,
Git blob `e1359f93c399c783e01c86d614fa02e86666671a`.

These sections were read, including the 1/3000 versus 1/500 span accounting,
trace normalization warning, and the named analytic transfer boundaries.
S01 records an independently written 713,315-node interval exhaustion for the
entire six-gap continuum; that historical execution is NOT a new execution by
this pass. S02 records the old 269 and 280 constants. Its original low-E
matrix formula is generalized, not silently reclassified or overwritten.

Original source: `ainta/zeta-simple-zeros` at
`040c5e899e658aed7b56a2a87f501798fe10761d`, `docs/proof.md`.
The complete displayed proof sketch was read. Its c=2 stability-enhanced
rank--inertia lemma, seven-point constants, and window method are credited.
This pass does not claim the original project's 707,901-node production run,
formal build, or all upstream theorem interfaces have been independently
reproduced. No upstream source is copied into the new packet.

The original spectral precursor was also read at PR731's reviewed source
`6d440eb6c82d989c046e87e13f9bdabf087f920f`, path
`claims/lemmas/L-106550-spectral-defect-beyond-unit-cap.md`, blob
`a2123bc7df024fceb7918036a91b0926223c358e`. It treats c=2, the exact
one-spike range E<2, and a weaker lower bound for E>=2. SR26's all-energy,
variable-c statement is a proposed extension of that precise source, not a
claim that the prior sharp local calculation was wrong.

### Direct finite-multiset and pair-correlation formulation

Y. Lamzouri, *A new proof that more than 2/3 of the zeros of the Riemann zeta
function are simple and on the critical line*, arXiv:2609.02882 (2026).
The repository import is PR788; its full description and source audit were
read. The current web abstract was located; the paper PDF could not be fetched
in this pass and is NOT described as freshly page-audited.

Primary formal source consulted:
`AxiomMath/ZetaZeros@4bcaf70e544506c311d83a5a5b143a134b9fc5f7`:

* `Challenge/Basic.lean`, blob `0ada9aee591827e28e8063dc412ff23abcf97ee2`:
  the exact Fourier convention, multiset and multiplicity definitions, and the
  imported RiemannVonMangoldt / PairCorrelation propositions were read. This is
  the CHALLENGE statement file with placeholders, not a purported closed proof.
* `ZetaZeros/Zeta/Transfer.lean`, blob
  `941189f3ecf1cd631f742fbe87254bb1eafa836e`: the full production transfer file
  was read for conjugation, scaling and counts. No Lean build or axiom audit
  was run, and the new stability theorem is not asserted formally verified.

The operator proof and smooth weight-removal argument used by SR26 are written
self-contained in PROOF Sections 3 and 5; no unexamined formal source lemma is
silently imported as their proof.

Analytic input: S. A. C. Baluyot, D. A. Goldston, A. I. Suriajaya and
C. L. Turnage-Butterbaugh, *An unconditional Montgomery theorem for pair
correlation of zeros of the Riemann zeta-function*, Acta Arithmetica 214
(2024), 357--376, DOI 10.4064/aa230612-20-3, arXiv:2306.04799.
Publisher metadata and abstract were checked. The exact smooth test version is
stated as an imported input in PROOF (5.1), aligned with the primary formal
interface above. No fresh line-by-line audit of the complete BGST proof is
claimed. Its separate thin-box simple-zero corollary is not confused with the
unconditional pair-correlation theorem itself.

Classical spectral diagonalization, von Neumann's trace inequality, elementary
trace Jensen/pinching, Fourier differentiation and zero symmetries are used.
The special trace pinching and the finite-rank realization are also explained
in the proof. The number-theoretic density corollary is SOURCE-QUALIFIED to P7,
PC and Riemann--von Mangoldt; the elementary matrix theorems need none of them.

No third-party PDF, font, large certificate transcript or protected source file
is redistributed. Links and exact pins are attribution, not permission claims.
No comprehensive priority search has been completed.

## 3. The critique: what was and was not established here

The criticism of the preceding arithmetic line is materially correct: its
exact identities and diagonal bounds did not establish a new upper bound for
the RH-equivalent native covariance. A count of PRs or checks did not change
that. That is why SR26 targets a strict quantitative consequence instead.

This pass is NOT an independent seven-programme audit. It does not endorse
without checking the critique's exact entropy comparison, all gamma-flow
assertions, historical priority claims for every kernel, or current numerical
records in unrelated zero problems. It uses the critique's proposed simple-zero
opportunity after reading the relevant actual mathematics. Nor does it announce
parallel reviewers, background work, or future review results.

## 4. New exact computation

`check.py` is one standard-library implementation. It uses exact Fraction
arithmetic, alternating sine/cosine remainders at squared argument 1/2 and
220-bit integer-square-root enclosures. No floating arithmetic enters its
accepting calculation. It reconstructs the entire expected payload before
comparison. JSON floats, NaNs and duplicate keys are rejected, and canonical
serialization distinguishes Boolean from integer fields.

Coverage in the final record:

* 36,935 rational trace/variance envelope checks;
* 250 exact attaining spectra;
* 8,125 scalar minimization comparisons;
* 8,640 exact noncommuting rank--inertia examples, with known inertia through a
  rational Householder conjugation, not approximate eigenvalue computation;
* 36 complete finite offset-accounting panels;
* rational enclosures for H0, the inherited 269 and 280 expressions, the new
  281 expression, its defect, and the strict gain.

These are bounded controls of the written proofs, not counts of universally
verified theorems. A negative control retains the failure of Delta>=variance
when an eigenvalue lies above the clipping threshold.

The self-test rejects SIX altered and resealed records through the same actual
acceptance function: changed pressure, block count, clipping threshold,
Boolean alias, falsely claimed RH status, and inflated density bound. A separate
duplicate-key parser control also rejects. These are in-process comparator
checks, not six separate CLI subprocesses or an independent proof verifier.

Executed on the final mathematical payload:

```sh
python -B check.py --check results.json --self-test
python -O -B check.py --check results.json --self-test
python -OO -B check.py --check results.json --self-test
```

Execution outcomes and semantic digest are in the delivery receipt. The
addition-only patch and clean ZIP are replayed separately before delivery.
No full authenticated repository checkout was obtained. Therefore no
repository-wide validator, remote CI, Lean, original P7 interval exhaustion,
new zeta-zero census, or independent referee acceptance is claimed.

Discovery used a binary64 scalar search over block sizes and clipping thresholds
to suggest the fixed rational choice. That scouting calculation is NOT an
input to the exact certificate and does not prove a globally optimal choice.
The seven-point pressure is unchanged.
