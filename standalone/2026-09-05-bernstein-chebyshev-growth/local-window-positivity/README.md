# Full-source local positivity and exact window tails

**Proposed component proofs; independent review required. RH and global
full-source positivity remain unproved.**

This continues PR #792 from `dc4bb9dbb49876732eb656339e79ee4ec43b157f`.
It adds new files only and preserves all earlier mathematical records.

The main positive result is for the ACTUAL operator, not a raw arithmetic
cutoff: every nonzero L2 test supported in any interval of length at most
1/20 has strictly positive quadratic value. The proof gives an explicit
sum of squared sliding integrals and a quantitative primitive-norm bound.
It covers an infinite-dimensional class of tests. Its window length is
conservative; no best-known support claim or external priority is made.

The complementary all-window result is an exact tail identity. On [0,L],
all prime powers beyond any X>=exp(L) contribute precisely a rank-two
operator determined by the one safe number

    tau_X=-zeta'(2)/zeta(2)-sum_(n<=X)Lambda(n)/n^2.

Its two eigenvalues, norm and trace norm are explicit. This gives an exact
local completion rather than a continuum-tail approximation. The correction
is indefinite, so completion by itself is NOT positivity.

At the moving window L=log X, its trace norm is asymptotic to
`2/(3sqrt(3))*X^(-1/4)`. Together with the parent's upper bound and PNT,
this proves that the global raw arithmetic cutoff's trace-norm convergence
has sharp order X^(-1/4). A fixed window has a faster exact 1/X rate.

## Read and replay

Read `PROOF.md`, then `SOURCES.md` and `VALIDATION.md`.
With the unchanged `../cross-route-hardy-laguerre/BRIDGE.md` present:

```sh
python verify_window.py --check result.json
python -O verify_window.py --check result.json
sha256sum -c SHA256SUMS
```

The new standard-library checker reconstructs 194 finite exact checks,
including all source inequalities from rational outward Euler--Maclaurin
and elementary series. It authenticates the parent Git blob. Normal and
optimized outputs are compared in the execution receipt. Numerical fits
and stored PASS flags are not acceptance criteria.

## What does not follow

Short-window positivity does not control the cross terms of functions
supported in multiple distant intervals. The proof even constructs a
globally positive definite extension of the local kernel, but that extension
is explicitly NOT the full arithmetic kernel. Replacing the source by it
would invalidate the RH implication.

The parent cutoff witness has support length 30(1+log X), outside the
log X locality window. There is no conflict with its negative-index theorem
or with the new short-window positive factorization.
