# DPG26 validation and execution boundaries

The analytic all-support Poincare theorem is a PAPER PROOF. A bounded matrix
replay is a control on arithmetic, conventions and implementation, not a
machine verification of its infinite quantifiers. Independent review remains
required. No RH result, independent acceptance or external novelty is claimed.

## Fixed scope and primitives

`check.py` uses Python standard-library integers and Fraction arithmetic.
No NumPy, floating value, zeta/zero oracle or numerical spectral solver enters
acceptance. Logarithms are enclosed using the positive atanh series after
reduction to [1,2], with 32 terms and explicit tail

    0 <= log(x)-2 sum_(j<m) z^(2j+1)/(2j+1)
       <=2z^(2m+1)/[(2m+1)(1-z^2)], z=(x-1)/(x+1).

The lower and upper endpoints are rounded OUTWARD to rational multiples of
2^-24. Prime-log weights in the finite matrix tests use the LOWER endpoints.
Reducing the positive edge weights reduces the quadratic form, so a verified
matrix lower bound for these rational matrices is also one for the actual
logarithmic graph. The rational source constant Z_P(p)/lower_log(p) is checked
below24 on every tested support, and the three-prime improvement uses1/6.

The bounded replay contains eight named groups:

- Trial factorization and an independent sieve agree at every integer1..1024.
- Six explicit logarithm enclosures and the fixed {2,3,5} logarithmic margins.
- Nineteen divisor-closed graph supports. Thirteen are integer prefixes with
  N=1,2,3,4,5,6,8,10,12,16,20,24,32; the other six are irregular divisor unions,
  divisors360, a 2/3/5-free support, a squarefree support, a 2/3 exponent box,
  and powers2. There are266 vertex instances,545 complete prime-power edge
  instances and247 tree edges across these panels; max support integer864.
  Exact lower-matrix LDL certificates cover all18 nontrivial panels and247
  positive pivots. Max matrix order32, or31 after anchoring the root.
- Forty one-prime spectral panels: p=2,3,5,7,11 and m=1,...,8. Each exact
  eigenvector, eigenvalue, weighted norm and pairwise orthogonality is checked.
  These are small rational formulas, not enumeration up to11^8.
- One complete six-dimensional two-prime tensor spectrum, comparing the
  coefficients of log2 and log3 separately, not assigning floating logarithms.
- Four reverse-tree descendant controls, N=8,16,32,64.
- One non-divisor-closed counterexample, S={1,6}, with exact zero induced
  energy and positive weighted variance1/7.
- Three rational Schur panels and nine completion-of-squares tests in a
  synthetic spectral basis. These do not claim an actual Weil decomposition.

There are no broad prime/zero campaigns. The local fixed-prime infinite
spectrum is proved analytically, not declared checked by finite matrices.

## Implementation authentication and adverse tests

The checker requires exactly nine regular files and an exact nonempty
eight-entry SHA256 manifest. It checks the source lock against the pinned
metadata literal and compares the canonical JSON of a freshly reconstructed
result to the retained result. JSON duplicate keys, floating numbers and
NaN/Infinity are forbidden; canonical comparison distinguishes Boolean aliases.
No assert statement implements acceptance.

Four unittest methods include a pristine actual CLI control and SIXTEEN
intentional corruptions in each interpreter mode. Twelve semantic/algorithmic
cases reseal the packet: false RH status, wrong constant, Boolean/float aliases,
wrong omega convention, dropped-power flag, source drift, duplicate JSON,
empty groups, removing higher-power edges in the producer, reversing the tree,
and changing an exact eigenvalue. Four package cases exercise altered proof
bytes, missing manifest, an extra file, and a proof symlink. The proof-byte
case is deliberately unresealed; it is an integrity test, not a mathematical
check of altered prose. The three algorithm edits must fail the independent
reconstruction even after their hashes are resealed.

`--write` is a producer mode to generate a new verification.json; it is not
an acceptance command. It refuses a symlink output. The sealed read/check mode
is the one used by the tests and the publication replay.

## Commands and results

Final commands, from this directory:

```sh
python -I -S -B check.py
python -I -S -B -O check.py
python -I -S -B test_check.py
python -I -S -B -O test_check.py
```

Both sealed check commands completed and produced byte-identical stdout.
All four unit methods completed successfully in BOTH normal and optimized
Python, including the pristine CLI run and all16 deliberate refusals per mode.
The final command receipts and bundle/application receipts accompany the ZIP.
No result from an interrupted command is counted as PASS. The published files
are checked against local Git blob IDs and the packet tree; the comparison
against the stated main source must show additions only.

A first exploratory import generated an unwanted __pycache__ directory. It
was removed before sealing, and all final executions use -B; the final flat
inventory rejects it rather than silently accepting undeclared inputs. The
factorization cross-check was extended from256 through1024 before the final
seal so that it covers every integer used by the actual graph panels.

## Exploratory calculations excluded from proof acceptance

Before the proof, ordinary NumPy eigenvalue scouting was performed on the
actual cutoff graph at N=2,3,4,5,8,12,20,32,50,100,200,400; root-Dirichlet
sections at N=5,10,50,100,200,400; and one-prime matrices of size120 for
q=1/2,1/3,1/10. Those non-directed values suggested the exact one-coordinate
spectrum and a potentially larger cutoff gap. None is a certificate or a
premise, and no uniform-in-N constant gap is inferred from them.

## Unperformed checks and scope

No parent code/suite, full W-kernel certificate, actual xi or zeta calculation,
Lean build, full repository checkout, Windows run, remote CI, or independent
referee review was performed. The parent source and exact file metadata were
read through authenticated GitHub; its bytes are not an executable dependency
of this self-contained replay. Literature searching established the classical
canonical-path context but was not an exhaustive novelty search.
