# Validation and review boundary

## Executed locally

The final `verify_exact.py` executed 1,192 exact Fraction/Gaussian-rational
checks normally and with `python -O`; outputs are byte-identical and each
matches `result.json`. There are no Python assert-based acceptance gates.

Coverage includes the two Laguerre definitions; an independently expanded
exponential jet; integration-by-parts polynomials; finite Laplace integrals
at eight exponents; the square coefficient and degree-zero constant; exact
geometric norms for six positive continuous source controls; rational atom
Gram matrices versus independent integrals of step-function squares; signed
cross terms; the divergent continuum lower bound; synthetic boundary maps
and multiplicity-sensitive residues; and completed prime-only signs.

The unchanged original checker was freshly rerun in both modes (1,922 checks
per mode), and so was the arithmetic checker (1,795 checks per mode). Each
pair has byte-identical outputs. These are separate packet counts, not an
aggregate repository test count.

Ten deliberate corruption runs were refused: a saved model norm, numeric
integer/float alias, saved source hash, changed proof bytes, and changed
parent source lock, each in normal and optimized Python. Each refusal was
checked for its intended error message, not merely for a nonzero exit code.
The corrupted copies were isolated in temporary directories.

`REPLAY_LOG.json` records the runs and output SHA-256 digests. The publication
manifest contains seven SHA-256 entries covering all other files in this
subdirectory; it does not hash itself. The four parent blob checks are also
literal constants in the checker, not status flags in its saved output.

## What the execution does not establish

No actual prime logarithm or zeta derivative was numerically evaluated.
The synthetic continuous source theta_*(x)=x-x^(1-6a) is not the prime
counting function. Rational atom weights verify the general Gram algebra
and are not substituted for the actual log p in the mathematical theorem.

Finite controls do not establish the classical PNT, all-degree Bessel or
Hardy-space passages, finiteness of K, the infinite boundary obstruction,
the original coefficient inequality, or RH. No directed integration,
external zero census, independent mathematical review, Lean build, or
GitHub Actions success was performed or inferred.

## Priority independent review

Check the exact square coefficient 2/3, its N=0 exception, the t=6 log x
normalization, and the two shifts in the Bessel estimate. Check that the
weak PNT consequence gives K finite without using square-root cancellation.

Check the atom inner products, boundary limits, nonconstant Gram kernel,
H^2 convergence of the complete r>=3 source, and the elementary C3 bound.
In particular preserve cross terms and do not sum the divergent continuum
moments over all exponents.

Check the -3/8 normalization and the square-bias correction in Pcal_N.
For HP-6 check the residue, multiplicity, meromorphic identity theorem,
radial H^2 estimate, and physical +sqrt x correction. An l^2 obstruction
must not be advertised as an obstruction to bounded coefficients.

The analytic results are proposed proofs pending independent review. The
smallest still-unproved conclusion-bearing statement is (20) in PROOF.md.
