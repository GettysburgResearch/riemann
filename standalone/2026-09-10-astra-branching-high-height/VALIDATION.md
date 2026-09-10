# BHH26 validation and execution contract

Status: bounded author checks, not independent mathematical acceptance.
The all-depth theorem in PROOF.md is a written proposed proof, not a theorem
established by extrapolating the finite panels below.

## Arithmetic and coverage

All accepting arithmetic is standard-library Python integers, Fractions and
Gaussian rationals. No float, special-function oracle, sampled quadrature,
root finder, zeta-zero list, or assert-based acceptance occurs in check.py.

The expected nonempty result is regenerated from the primitive formulas before
canonical typed JSON comparison. JSON duplicate keys, noninteger numeric tokens
and nonfinite tokens reject. Boolean aliases reject by typed canonical
comparison. The exact nine-file regular-file inventory and eight-entry hash
manifest are checked before reconstruction. SOURCES.json binds the inherited
head and reading scope. These are content/source checks, not theorems.

The reconstruction contains:

- Ten exact coefficient rows n=0,...,9 and their telescoping root-bound identity;
  six separately generated unnormalized derivative-atom systems n=0,...,5.
- 156 full beta-pair derivative-moment identities, using uniform input laws,
  independent raw pair moments, and BOTH diagonal and off-diagonal terms.
- 364 scaled-atom derivative moment identities; every one includes both
  endpoints and the whole continuous term. Eighteen additional moments use
  the literal first uniform-scale law U^-2 and its entire derivative measure.
- 35 exact Gaussian-rational polynomial value/log-derivative comparisons.
- Seven complete rational majorant/threshold reconstructions n=0,...,6.
  These cutoffs are analytic upper bounds, not zero-counting campaigns.

The cases overlap conceptually and are not advertised as hundreds of separate
analytic theorems. In particular, finite moments do not machine-prove the BV
induction, the high-height phase bound, or the fixed-depth zero asymptotic.

## Commands and tests

The final accepting commands are:

```bash
python -I -S -B check.py --check result.json
python -I -S -B -O check.py --check result.json
python -I -S -B test_check.py
python -I -S -B -O test_check.py
```

The five test methods cover atom/polynomial reconstruction, the complete
finite derivative measures, Gaussian-rational polynomial checks, threshold
arithmetic, and actual subprocess acceptance/refusal. Each mode runs one
pristine copied CLI acceptance and sixteen distinct changed-copy refusals.
Selected data and primitive changes are rehashed, so a checksum alone cannot
explain their rejection. These include false RH/window statuses, a reduced
cutoff, deleted remainder, altered atom, omitted coverage, float/Boolean
aliases, duplicate JSON, source drift, changed proof, extra/missing files,
and primitive mutations changing coefficient squaring, deleting mixed beta
terms, or removing the common-uniform lower-endpoint factor.

Only successfully completed commands belong in the external execution receipt.
The producer command

```bash
python -I -S -B check.py --write result.json
```

is deliberately UNAUDITED emission, not an acceptance assertion. The payload
is sealed before the accepting runs. No test is conditional on symlink
privileges; no native Windows run is claimed in this author session.

## Authenticated predecessor

The supplied 15,453-byte parent PROOF.md matches the freshly returned GitHub
blob 0673f43b95570bcbe7fe29de3c2528fc5ada29a2 at PR857 head
3f1984867d23b588d09c88a892882411724b174b, and its SHA256 is in SOURCES.json.
The complete principal proof was read. No parent full checker, phase or root
certificate, old numerical campaign, or repository validator was rerun.
The new checker imports no predecessor module.

The factorization relevant to the new theorem is rederived in PROOF.md. The
parent's entire convergence is used only for the explicitly conditional RH
endpoint and remains at the parent's proposed-review status.

## Exploratory and unperformed work

Non-directed mpmath scouting of the first two prescribed depths preceded the
proof. It used high-precision moment series and gamma-normalized searches.
One early unnormalized root-search variant was unreliable because the raw
transform decays; it was not used for a claim. None of the exploratory root
coordinates or counts is accepted, and no numerical xi zero was evaluated.
A possible heat-flow interpretation was considered but no such theorem was
obtained or included. The proved mechanism is the derivative-atom/BV split.

No all-height computation of M_n, no zero census below T_n, no whole-repository
checkout/build, Lean/kernel proof, remote CI, exhaustive literature-priority
review, or independent referee acceptance is claimed. Local patch tests use
an explicitly minimal Git fixture and do not confer a real-repository PASS.

## Publication boundary

The current GitHub connector read PR857 and its exact source successfully.
Discovery exposed no write action; direct git ls-remote failed because the
runtime could not resolve github.com. No remote write was performed. The
external receipt distinguishes any later uploader's work from this session.
Only an add-only new research branch is proposed, stacked on the parent.
Main, prior research, integrated/canonical/formal status, workflows and
repository settings must remain unchanged.
