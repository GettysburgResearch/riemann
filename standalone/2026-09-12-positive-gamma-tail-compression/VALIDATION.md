# Validation scope and limitations

These checks authenticate/reconstruct a finite research packet. They are not
an RH proof, formal verification of the infinite arguments, an independent
referee report, or a complete-repository validation.

## Final accepting commands

From this directory:

```sh
python -I -S -B check.py --check result.json
python -I -S -B -O check.py --check result.json
python -I -S -B test_check.py
python -I -S -B -O test_check.py
```

Both reconstruction modes and all SEVEN test methods completed successfully,
with identical receipts/summaries and zero failures, errors or skips on Linux.
Each test mode includes one pristine full CLI acceptance and TWELVE actual
altered-copy CLI refusals, including the symlink test. On a host unable to
create symlinks, that one separate method explicitly skips; the recorded CLI
count is then eleven, not a fabricated twelfth refusal. A failure does not
print a unconditional test-suite PASS.

The eleven non-symlink refusals cover: false RH flag; float alias; Boolean/
integer alias; duplicate JSON; missing actual parameter row; wrong parameter
endpoint; changed coverage; unsealed proof edit; extra file; a producer power
mutation with updated checksums; and incomplete checksum coverage. The power
mutation fails the independent rational resolvent identity after reconstruction,
not just a hash check. No assert implements the accepting program's guards.
Unit tests use unittest assertions as normal.

## What was computed

* Twenty exact Radau constructions (four finite positive measures, r=0..4),
  with 120 rational/Gaussian-rational resolvent identities, 100 matched scale-
  moment entries, orthogonality, and the exact first unmatched cumulant.
  Sixty positive scale-rescaling panels additionally check the changed-source
  Radau identities; the rational disk-to-defect lower budget is checked too.
  These finite measures are CONTROL data, not truncations accepted as the
  entire native tail.
* Thirty-six actual infinite gamma-tail moment enclosures at N=2,4,8,16,32,64,
  with complete even-zeta/Bernoulli and directed pi formulas. All overlap
  separately calculated full Euler--Maclaurin enclosures. The latter includes
  the complete periodic remainder, bounded by 4/6^(2q) for q=12; it is not a
  numerical sum cut off at an unproved endpoint.
* Six actual one-component drift/shape/scale enclosures and two actual
  two-component rules (N=8,16), including positive weights and separated nodes.
  Interval overlap is a corroboration between containing enclosures; the
  identities themselves come from the written and exact rational arguments.
* Seven large-order error-bound panels and 1025 integer checks of the final
  threshold's elementary quadratic budget. These evaluate BOUNDS ONLY. No
  large-order orthogonal polynomial, quadrature nodes or xi transform values
  were numerically constructed. The all-N theorem rests on the proof.
* Fifty-one complete finite gamma moments by cumulant recursion and independent
  coefficient-product expansion, plus drift/sign interpretation controls.

The code imports only Python's standard library. All accepting arithmetic is
integer/Fraction arithmetic or outward 320-bit dyadic intervals; no floating
quadrature, nonlinear optimizer, zeta/gamma library, or zero table is used.
Normal/optimized runs are one arithmetic implementation, not independent
numerical backends or independent mathematical authors.

## Preservation, packaging and publication boundary

The delivery ZIP contains exactly these nine files, eight covered by the
manifest (the manifest does not hash itself). Clean extraction and an add-only
patch applied to a temporary Git fixture both replay the accepting commands
and tests in normal/optimized modes. The fixture preserves the 31 supplied
files from the original reciprocal-gamma, centered-gamma and finite-defect
packets, plus an unrelated sentinel. That fixture is not an authenticated
complete checkout of the repository.

The local publication receipt outside this packet records actual file hashes,
packet-tree identity, commands, and remote observations. The principal parent
proof's local Git blob agrees with the remote #862 source. Original manuscripts,
prior evidence, main, and the integration candidate are not edited.

This session's GitHub connector exposes read actions only; discovery found no
create/push actions. The installed-plugin search found no additional usable
GitHub write action. The direct Git attempt failed DNS resolving github.com.
Consequently this packet has NOT been pushed in this author session. A later
uploader should record a separately verified publication SHA, not reinterpret
this sentence as a claim about future remote status.

## Explicitly unperformed

No parent certificate campaign, new defining-integral Fourier zero certificate, native defect/
Jensen integral, complete zero census, high-r parameter solve, fresh Lean build,
full-checkout repository verifier, native Windows test, remote CI run, independent
mathematical acceptance, or all-order zero-confinement proof was performed.
The optional RGT7 stress theorem imports the existing CG4 disk certificate,
without a new defining-integral replay, to prove persistence for the explicit
changed-source parameter eta=2^-256. The complete integral perturbation bound
and inherited rational-margin comparison are new analytic/exact-arithmetic
transfers, not a freshly evaluated Fourier zero.
No nondirected spectral scout was run in this pass. The new proposal retains
the exact missing estimate instead of labeling it a routine referee task.
