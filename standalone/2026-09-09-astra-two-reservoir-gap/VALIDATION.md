# TRG26 validation and limits

## Paper proof versus bounded execution

PROOF.md supplies the proposed all-cutoff asymptotic and graph theorems. The
checker does NOT prove these infinite statements, RH, or a critical-source
comparison. Independent mathematical review is required. All graphs used by
the main theorem are finite at each prime cutoff, but grow without a fixed rank.

The accepted numerical objects are exactly the two finite gap brackets in
result.json. They concern actual prime-logarithmic divisor graphs, not zeta
zeros, Xi kernels, or native residual energies. No large-prime asymptotic is
inferred from these small examples.

## Mathematical replay actually executed

Both commands completed and produced byte-identical JSON:

    python -I -S -B verify.py --check result.json
    python -I -S -B -O verify.py --check result.json

The retained output has SHA256
9e7a5f37b0c88b899465a15d94a4a0bc126abd2394eebcc80c4671c44f612b28.

Bounded coverage:

- Sieve and independent trial primality agree on all 256 integers 2,...,257.
- Seven complete formal rational-rate graph panels, totaling 45 vertex instances
  and 54 edge instances, verify the actual permitted graph and shared-root gluing.
  These panels use explicitly rational test rates, NOT numerical logarithms.
- Twenty-one exact determinant identities reconstruct the full gluing equation.
  Thirty-eight product eigenvectors, fourteen root Green identities and seven
  complete globally centered trial variances are checked in Fraction arithmetic.
- A separate exact coincident-root case verifies the root-zero eigenvector and
  secular equation when division by a root resolvent would be invalid.
- The P17 certificate retains 65 vertices, 193 edges and 64 visible nonconstant
  product modes. P31 retains 1025 vertices, 5121 edges and 1024 visible modes.
  Every permitted edge is independently counted from the actual integer support.
  The scalar equation is evaluated on every visible mode, not a sampled subset.

The last two enclosures use 160-bit outward dyadic intervals. Each logarithm is
range-reduced to [1,2] and evaluated by 100 terms of its positive atanh series,
with the entire remaining geometric tail included. Integer arithmetic, isqrt,
and Fraction are the only numerical primitives in the accepting program.
There is no floating-point, zeta, gamma, quadrature, or eigenvalue oracle.

Small floating sparse-tree spectra and a 60-digit scalar scout were exploratory.
The latter proposed readable decimal brackets. The accepting code re-encloses
the actual logarithmic secular expression independently; the scout values are
not used as evidence or imported by the checker.

## Adverse accepting-boundary tests

Each of the following commands completed, with no skipped cases:

    python -I -S -B test_rejections.py --part 1
    python -I -S -B test_rejections.py --part 2
    python -I -S -B -O test_rejections.py --optimized --part 1
    python -I -S -B -O test_rejections.py --optimized --part 2

In EACH mode two pristine copied-packet controls pass and nine actual CLI
mutations reject. The cases are: false RH flag; wrong gap endpoint; a Boolean
integer alias; duplicate JSON keys; a float alias; a resealed producer with the
wrong shared-root mass; a resealed extra file; changed proof bytes; symlink core.
The first six semantic/producer mutations are resealed where applicable so hash
checking alone cannot explain all refusals. The root-mass mutation is rejected
by the independent finite graph determinant reconstruction. Symlink tests ran
on Linux; no Windows execution is claimed.

The accepting command authenticates a fixed nine-file inventory plus SHA256SUMS.
JSON aliases and duplicate keys are not treated as mathematical certificates.
`--emit` is explicitly unauthenticated producer mode, not an acceptance path.
Checksum validation is anchored by the publication's file identities; it is not
a claim that a maliciously rewritten proof/checker can certify its own correctness.

## Packaging and publication boundary

The final sealed code and result were replayed in both modes. A temporary local
Git add-only patch application preserves an unrelated sentinel, reproduces every
payload byte, and replays both modes. Clean ZIP extraction also replays both
modes. These are minimal fixtures, NOT a complete Riemann checkout or CI build.
Publication receipts and replay stdout are retained separately in the archive,
not used as numerical input. Remote publication is claimed only in the external
receipt after the branch, PR head and complete added subtree have been read back.

No parent executable, historical certificate suite, full repository test, Lean
build, external zero verification, actual prime-error/entropy campaign, or
independent referee-identity certification was performed. The parent proof was
read and byte-pinned; the new lower construction and required elementary inputs
are rederived. The mathematical conclusion concerns graph gaps only.
