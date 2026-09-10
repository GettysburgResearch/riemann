# An arithmetic spectral gap with no exponent-depth loss

Status: PROPOSED COMPONENT PROOFS; independent review required.
RH and the cumulative prime-discrepancy upper bound remain unproved.

This is a deliberate change of target: instead of producing another local
prime-error criterion, prove a quantitative inverse bound for the literal
prime-power matrix already present in the source programme.

For every divisor-closed set S supported on primes at most P, and every
Hilbert-valued function f,

    sum_(n in S)||f(n)-fbar||^2/n
       <=48[1+log(16log P)]
          sum_(j p^k in S)(log p)/(j p^k)||f(j p^k)-f(j)||^2.

There is no dependence on exponent depth or cardinality. The theorem extends
to a countable fixed-prime reservoir. For S=1,...,N, it supplies the explicit
spectral gap of L_N=D_N-C_N on the complement of the known n^(-1/2) mode.
The actual primes and every allowed prime power are retained.

The proof uses a smallest-prime-removal tree, an elementary smooth-number
harmonic product bound, and a tunable alpha^omega weight. The comparison Euler
product counts positive path mass; it does NOT replace the physical source's
mixed prime phases or assume independence of its signs.

## Reading and reuse

Read PROOF.md Sections 1-3 for the theorem and elementary proof, Section 5 for
the infinite domain, and APPLICATION.md for the source-metric residual/Schur
certificate and the exact finite demonstration. CLAIMS.json states scopes.
SOURCES.json preserves the old divisor-cusp source and current square-grid
context; no old scientific verdict or source file is edited.

A positive complement is not a full RH theorem. The coherent coefficient
channel, the actual continuum/mean terms, and a complete critical source adapter
must still be accounted for. The graph spectrum is not identified with xi.
No absolute-constant gap or external novelty/priority claim is made.

## Reproduction

    python -I -S -B validate.py
    python -I -S -B check.py --check result.json
    python -I -S -B -O check.py --check result.json
    python -I -S -B test_rejections.py
    python -I -S -B -O test_rejections.py

The standard-library checker reconstructs finite factor/path identities,
rational coercivity controls, and ONE complete N=32 inverse enclosure. It does
not prove an infinite analytic theorem by enumerating examples. VALIDATION.md
states every executed scope and the exploratory calculations that are excluded
from the proof.
