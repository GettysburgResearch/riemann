# Validation and limits

Status: bounded author implementation checks, not independent mathematical
acceptance. Infinite analytic arguments are proposed proofs in PROOF.md and
COHERENT_SOURCE.md; no finite check certifies their unbounded quantifiers.

## Exact inputs and declared coverage

The source freezes and inspected layers are recorded in SOURCE_LOCK.json.
They were read through the GitHub connector. The packet authenticates its own
source-lock record, not a downloaded complete repository or every byte of every
referenced manuscript. No predecessor code or historical producer was run.

The fresh standard-library verifier uses only integers and Fraction arithmetic.
Its literal logarithms use a 64-term range-reduced atanh expansion with the
complete positive geometric remainder, rounded OUTWARD to 160-bit dyadics.
Every sum used by the scalar-root enclosure is rounded outward separately.
No ordinary float or special-function oracle enters acceptance.

- Four complete product-basis panels have 2,4,8,16 vertices. Orthogonality and
  each prime's generator equation are checked coefficientwise. Independent
  root-Poisson and Green norm identities use synthetic rational rates, explicitly
  NOT relabeled as logarithms.
- Six literal logarithmic anchored constants are enclosed for prime prefixes
  of lengths1,2,3,4,6,8 (largest prime19, largest box256 vertices). Their full
  scalar sums include all nonempty subsets; their extreme integer is9699690.
  Each root bracket is verified on both sides of the secular equation, including
  the pole domain; 44 fixed bisection iterations give outward displayed brackets.
- Ordinary Mobius sieve values are compared with independent trial factorization
  at EVERY integer1,...,256. Finite divisor inversion and the squarefree identity
  are separately reconstructed throughout that range.
- The stopped-source energy work law is checked at every N<=128. Thirteen fixed
  N panels independently expand all ordered pairs and the FULL prime-power graph,
  including higher-power outgoing terms. N=128 contains315 edges,91 higher powers.
  The terminal future M(N)^2/N is exact, not a numerical cutoff or a zero tail.
- The analytic asymptotic coefficient, survival law, all-N native edge asymptotic,
  and delayed-Laplace implication are paper proofs. No actual zero, zeta contour,
  prime-discrepancy energy or growing-horizon subpower bound is computed.

## Commands

Run from this packet, with isolated standard-library Python:

    python -I -S -B check.py
    python -I -S -B -O check.py
    python -I -S -B test_check.py
    python -I -S -B -O test_check.py

Default checking rejects extra/missing files, symlinks, incomplete/duplicate hash
manifests, source-lock drift, duplicate JSON, floats, constants and boolean aliases.
It compares exact recursively typed primitive results, not just a retained digest.
Acceptance does not use assert. `--emit` is separately a result-generation mode.

The four unittest methods include a pristine copied CLI control and fifteen
actual adverse cases in EACH mode: eight changed result/JSON cases, five package
or source-lock cases, and two resealed producer changes. These include a false
RH status, altered future term, false root enclosure, missing native panel,
changed prime birth rate and removed higher-power edges. Resealing is deliberate:
semantic and producer defects must fail reconstruction even after hashes change.
The symlink refusal is exercised on Linux; no Windows execution is claimed.

## Executed final results

On Linux, default check.py completed in both ordinary and optimized Python,
with byte-identical output and reconstructed mathematical fingerprint
`29de48797dac5a1d1c27c4498722633523ef240f3f26e694fcee0714c81fb9e8`.
All four test methods completed in both modes: one pristine copied CLI control
and all fifteen distinct corruptions per mode, including the Linux symlink case.
The initially successful suites took about3.3 and4.8seconds respectively; these
are retrospective command durations, not performance guarantees. Final sealed
and clean-extraction runs are separately recorded in the delivered receipt.

## Development failures and corrections

An initial root-comparison check required the ENTIRE numerical bracket to lie
within a sharp analytic comparison interval. At a one-prime equality, outward
rounding makes that stronger requirement false. It was replaced by the correct
interval-consistency check; strict opposite-sided secular evaluations remain
the actual acceptance predicate.

A first implementation summed rational root expressions with unnecessarily
large common denominators and timed out at45seconds. That incomplete command
is not a successful replay. The final version uses directed160-bit summation
and integer initial upper brackets; final producer/replays are bounded.

Before the first test-suite run, inspection found that a proposed mutation of
the N=2 future term would replace zero by zero. It was changed to a genuinely
false nonzero term; no no-op mutation is counted as a rejection test.

A separate ordinary NumPy discovery scout examined24 finite box/star/two-block
spectra through eight prime coordinates (at most256 vertices). It helped select
the root-anchoring question. It is NON-DIRECTED reconnaissance and excluded from
all proof inputs and acceptance. No large prime or zero campaign was launched.

## Publication and application boundaries

Only this new directory is proposed on a separate branch from the frozen main.
The final publication receipt is delivered separately: it records actual tests,
ZIP extraction, temporary-Git add-only patch application and remote readback.
A temporary-Git check is not a full repository checkout or build. The actual
source branches, canonical/formal records, review tables, workflows, permissions
and settings are unchanged. No remote CI, Lean, external referee acceptance,
all-history completeness or unconditional RH completion is claimed.
