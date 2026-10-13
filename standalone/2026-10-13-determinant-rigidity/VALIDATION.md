# Validation and mathematical scope

## Proposed mathematics, not an acceptance report

The author checked the complete arguments in PROOF.md and wrote the exact
finite diagnostic. There was no independent author, agent, or human referee.
Theorems 2.1 and 4.1 are necessity results; Theorem 3.1 is an unconditional
norm comparison; Theorem 5.1 retains an explicit unproved native moment input.
None is asserted to prove the full generalized native moment or RH.

The analytic proof has these load-bearing boundaries:

1. The finite-ray moment hypothesis includes every dual character and the
   displayed fixed small-prime exclusion. It is not one untwisted estimate.
2. The nonabelian theorem requires every irreducible character-valued prime
   probe. These are generally outside the original one-dimensional family.
3. Only the classical Artin germ at one is used. Its order is deduced using
   Brauer induction, Frobenius reciprocity, and Hecke nonvanishing at one;
   global Artin holomorphy is not assumed.
4. Both Euler comparison kernels retain signed coefficients, literal row
   zeros, common factors, and the SAME original exclusion.
5. A small prime can make the square-root-weighted inverse kernel diverge.
   The fixed cutoff Np>4r^2 is not omitted in the norm theorem.
6. Every shorter column sum in the comparison and conditional product
   theorem uses the same physical row measure. The rank-r moment consumes
   order 2kr and does not improve its power excess.

## What actually ran

The author executed

    python -I -S -B verify.py > results.json
    python -I -S -B -O verify.py > replay.optimized.json
    cmp results.json replay.optimized.json

The ordinary and optimized reports were byte-identical. Acceptance uses
explicit runtime exceptions rather than assert statements. The Python
source also parsed successfully with ast.parse.

The report has 20,535 explicit predicates including setup/domain checks.
It verifies 1,555 local eigenvalue lists through power 12; 1,040 rational
points in the local absolute-majorant inequalities; finite negative-character
classifications for C2, C3 and S3; and 1,944 pairs of physical forward/inverse
sum identities. The count is not a count of independent analytic theorems.

The arithmetic uses exact Z[omega] and rational arithmetic, with no floating
point acceptance. Sextic symbols are computed in explicit quotient fields:
four split ideals of norms 7,7,13,19 and one inert ideal of norm 25. Both
conjugate ideals of norm 7 are kept distinct. Actual finite-ray coefficient
examples use characters of the ideal norm modulo 4 and 9.

All 54 nonzero Eisenstein elements of norm at most 13 are included. The
columns are restricted to the 24 ideals in this five-prime semigroup of
norm at most 512. Tests use annular cutoffs at 31,128,512 and four original
exclusion masks, including the full mask. This is NOT coverage of all
native column ideals up to 512. The small-prime examples test algebra;
they do not purport to satisfy the analytic theorem's larger prime cutoff.

Four deliberate invalid substitutions are rejected: a new coprimality
restriction in convolution; taking absolute values in signed inversion;
deleting the small-prime kernel gate; and using only one-dimensional
probes in the nonabelian classification. The finite S3 example is not a
computation of Frobenius elements in a new extension.

## Source authentication and limits

The supplied #935 packet's MATHEMATICS.md and verify.py were read, and their
byte counts, SHA-256 values and Git blob IDs matched its manifest. The
GitHub base commit/tree were fetched live. The parent tests were not rerun.
The current #931/#936/#937 reading depths are recorded in SOURCES.json.

No full-repository checkout, repository-wide validator, remote CI,
proof-assistant build, independent theorem review, or reconstruction of the
classical prime ideal and Hecke/Brauer theorems was performed. The finite
checks support the named identities and bookkeeping; they do not certify
any infinite analytic statement. The SHA-256/Git manifest authenticates
payload bytes, not mathematical correctness.

Publication is add-only on a new branch with #935's exact head as parent.
No historical proof, main branch, workflow, or integrated status is to be
changed. A remote tree/commit comparison is a publication check only; its
outcome is reported separately from the mathematical status.
