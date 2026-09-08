# Validation and exact limits of the evidence

This packet is author-proposed research, not an independent referee verdict.
No unconditional RH proof or new unconditional zero-free region is claimed.

## Executed bounded checks

Python 3.13.5, standard library only. The two mathematical replays use
`python -B checks.py` and `python -O -B checks.py`. Their complete JSON outputs
are byte-identical. There are seven groups and 231 bounded cases per mode:
30 full state/physical-Gram comparisons; 150 signed cutoff-tail comparisons;
30 finite-average controls; six strict physical Grams; the literal prime-2
normalization; two constant payloads; twelve synthetic Taylor-tail controls.
These numbers are fixtures, not 231 independent mathematical theorems.

The state fixtures have rational amplitudes at logarithmic integer sites.
They test general signed-measure identities, NOT a full actual prime/continuum
energy. Only the separately named prime-2 normalization is actual-prime data.
No entropy integral, large-cutoff prime-discrepancy energy, or zero ordinate is
computed. Infinite Jensen, Cramer, Hardy, and convergence arguments remain
paper arguments, not consequences of the finite checker.

The code uses explicit exceptions, not assertions whose removal could alter
acceptance. Stored outputs are compared with freshly reconstructed canonical
JSON; duplicate keys and numeric aliases are not accepted as equal evidence.

## Negative tests and inventory

`rejections.py` executes the actual checker CLIs. Six result corruptions per
mode are rejected: RH status, fixture count, floating count alias, extra field,
duplicate JSON key, and altered finite-norm digest. Four packet mutations per
mode are rejected: altered proof, missing proof, extra file, duplicate manifest.
There are four pristine controls. `rejections.json` retains all outcomes.
A combined command completed both validation runs and the first full rejection
run, then timed out during a redundant second rejection run. The incomplete
repeat is not counted; the complete first result is the retained record.

`validate.py` checks the exact fourteen-file inventory and thirteen SHA-256
entries, rejecting nonregular entries and any manifest omission/duplication.
`python -B validate.py --replay` re-executes both mathematical modes.
This is content integrity and bounded-algebra verification, not an authenticated
external primitive pipeline or protection against an author resealing all files.

## Analytic imports and source inspection

The parent PDS26 manuscript was read in full from the live exact source and
its locally retained Git blob was confirmed as
`ff50df2505be5cb91a767c06775a5e6ba1fffdd2` (15,828 bytes).
The later EPD26 manuscript was inspected for overlap, not used as a theorem
premise. Parent mathematical checkers were not rerun.

Brent--Platt--Trudgian arXiv:2008.06140v1, pages 1-3, was inspected in parsed
text and page screenshots. Its qualitative upper mean-square bound is imported
ONLY under RH. No numerical constant, zero table, or external computation is
replayed. The full external paper has not received a fresh proof audit here.
Standard Fourier/Hardy/complex-analysis facts are specified at their uses.

Two abandoned non-directed scouts tested low derivative signs of small finite
Euler completions and real-axis values through cutoff 200,000. They furnished
no theorem and are not proof inputs, certificates, or an unbounded trend.

## Publication boundary

Only the new standalone directory is intended for publication, on a research
branch based on the frozen PR811 head. Main, the parent branch, all previous
proofs, reviewer records, canonical/formal sources and workflows are unchanged.
No full repository checkout was obtained: direct Git access failed DNS
resolution. Local patch tests use a temporary Git fixture, not the real checkout.
No Lean, Comparator, remote CI, external referee acceptance, or novelty claim.
The publication receipt is outside this immutable packet.
