# Branching renormalization: a new Xi proof programme

**Proposed component proofs; independent review required. RH is not proved.**
This packet changes the construction, rather than refining the previous
divisor gap or the theta-truncation error. Its target is a zero-safe invariant
class for a positive stochastic map with a uniquely identified Xi fixed law.

For mean-one probability laws, set

    T nu = Law((X_1+X_2)/U^2), U uniform[1,2].

The same U is used for both independent children. The exact classical
Brownian fixed law encodes the original completed xi function. This packet
proves an explicit sqrt(7/12) Wasserstein contraction and source-error bound
from the single one-step residual W_2(nu,Tnu).

The second component is a starting FAMILY with a complete critical-strip
zero theorem: X~Gamma(k,rate k), every real k>=1. Starting at k=5/2 matches
the fixed law's mean and variance exactly, and those two moments remain exact
under iteration. The reflected Mellin transforms converge to actual xi on
every compact part of the critical strip. There is no unknown source adapter,
no zeta zero used as an input, and no unpriced physical tail in this limit.

**What remains open:** prove that off-central critical-strip zeros stay absent
along an unbounded sequence of those iterates. The starting-law proof does not
prove this propagation. Positivity and contraction of probability laws do not
imply zero-location preservation. Preliminary noncertified first-step work
warns that the strongest monotone-ratio proof invariant need not propagate.

An alternative is to construct zero-safe approximate fixed points (possibly
through #842's ferromagnetic class). A finite rational residual certificate is
supplied. It prices the whole continuous uniform input by conditional means;
the first three exact quantized transitions have 1, 2, 10, and 350 support atoms.
No claim is made that these particular quantized laws are zero-safe.

## Read and reproduce

Read [PROPOSAL.md](PROPOSAL.md), especially Sections 2--4; [SOURCES.json](SOURCES.json)
records the classical and repository boundaries. [VALIDATION.md](VALIDATION.md)
records actual execution and the unproved assertion.

```
python -I -S -B check.py --check verification.json
python -I -S -B -O check.py --check verification.json
python -I -S -B test_check.py
python -I -S -B -O test_check.py
```

The checks reconstruct finite rational laws, moments, transport costs, and a
complete continuum Bernstein-polynomial certificate for the gamma proof.
They do not machine-prove the analytic theorems or a later-stage zero claim.
`--emit` is explicitly producer-only. No float enters accepting arithmetic.

The underlying Brownian fixed-point identity is in Biane--Pitman--Yor (1999),
equation (45), and their Proposition 1 is the source identity. #296 already
uses a different Brownian cutoff construction; #842 uses finite Ising models.
These connections are credited, not claimed as newly discovered. No exhaustive
novelty search or independent acceptance is asserted.

This delivery is LOCAL and prepared add-only from main
`f99d9e3908dde4865377c75d9ca051c1f545bf4f`. No repository write was performed in the author session. A later uploader may
publish these unchanged files; this sentence records the original delivery.
