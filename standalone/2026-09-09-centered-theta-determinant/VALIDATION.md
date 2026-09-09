# Executed validation and limits

The paper's infinite theorems require independent mathematical review. The
finite controls below do not establish RH, actual spectral reality, or the
operator-domain and infinite determinant theorems by computation.

## Source authentication

The complete 21,611-byte uploaded parent proof was read and its Git blob
recomputed as 648a8a867be1ce808a30364d0bb6d4ab7ab3b6f6, matching the
repository read at 2787339f8f1feb619f1679afb96cb9995e440958. This is byte
authentication and mathematical source reading, not independent acceptance.
Parent code, prior minimum certificates and previous campaigns were not run.

NIST DLMF 25.4 was read. Zumbrun's determinant appendix and Volterra calculation
were inspected in parsed PDF text. Both requested web page images failed;
there is no claim of visual PDF inspection or complete external-source audit.
Only the stated standard determinant properties are used. The impossible
printed lower determinant bound in the preprint's (A.2) is excluded explicitly.

## Bounded reconstruction

    python -I -S -B check.py --check result.json
    python -I -S -B -O check.py --check result.json

Both modes completed with identical mathematical JSON output, containing:

- 28 finite nilpotent-Volterra/rank-one cases, including the det_2 exponential;
- 15 finite parity-block determinant cases, without doubling the answer;
- 27 polynomial-antiderivative cases for three declared compact probability laws;
- 4 complete rational piecewise-density integrals checking Tr K^2=-variance;
- 36 finite adjoint-chain relations.

These are 110 bounded cases across five groups, not independent infinite
proofs. All arithmetic is standard-library integer/Fraction arithmetic.
There is no floating spectral solve, actual theta-value evaluation, numerical
zeta contour, zero list or special-function oracle in acceptance. The finite
Volterra matrices are algebraic controls, not a theta spectrum approximation.

## Actual rejection and delivery tests

In each interpreter mode a pristine copied packet passed. Six changed copies
were then refused: a false RH flag, a float/integer schema alias, duplicate JSON,
a resealed producer sign change in the rank-one determinant, changed unsealed
proof bytes, and an extra file. The semantic producer mutation reaches the
mathematical reconstruction rather than failing only a file hash.

The packet has eight regular files and seven SHA256SUMS entries. The checker
uses explicit exceptions, not assert-based acceptance, rejects symlinks, checks
exact inventory, and compares result types recursively. SHA256SUMS is a local
integrity seal, not external authentication of a mathematical claim.

A minimal temporary-Git add-only patch roundtrip reproduced the eight bytestrings
and replayed both modes while retaining an unrelated sentinel. A clean ZIP
extraction likewise reproduced and replayed the package. Those are local
publication checks, not a full repository checkout or source-wide validation.

## What was not done

No actual theta eigenvalue, spectral sign, infinite determinant or zero-free
region was numerically certified. No new finite norm or positivity range is
claimed. No Lean/Comparator/kernel build, Windows run, remote CI run, exhaustive
repository audit, or non-author review occurred. Analytic proofs, source tails,
Fredholm continuity and the adjoint-domain arguments remain paper proofs.
