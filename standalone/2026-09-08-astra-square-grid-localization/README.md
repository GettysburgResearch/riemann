# SSQ26 — Localize the critical energy on a predetermined square grid

**Proposed component proofs; independent review pending. RH is not proved.**

This continuation of PR818 proves an unconditional summable bound for the
complete within-cell detail of the ordinary prime-counting discrepancy. It
does not prove the unbounded coarse-level estimate.

For `e(x)=pi(x)-integral_2^x du/log u`, the exact bounded invertible adapter to
the parent's weighted discrepancy gives `K/4<=J<=K`, where
`K=integral e(x)^2 dx/x^2`. This is not an unjustified measure change.

On `[n^2,(n+1)^2]`, let `m_n` be the mean in measure `dx/x^2` and
`w_n=1/n^2-1/(n+1)^2`. Then

```
K = initial energy + sum w_n m_n^2 + sum detail_n,
sum_(n>=N) detail_n < 28/log N, every integer N>=2.
```

The detail bound is unconditional, importing only the classical interval
Brun--Titchmarsh upper bound. No existence of primes between squares, PNT,
RH, or zero verification is used for it. The sum is orthogonal with every
term retained. The unknown part is the cumulative coarse level, not the
local detail.

A counts-only version has squared approximation error `<112/log N` and gives

```
RH iff sum_(n>=2) [pi(n^2)-Li_2(n^2)]^2/n^3 is finite.
```

The conditional RH direction retains the parent's Cramer hypothesis. The
new result is the complete unconditional localization, not a new classical
RH criterion advertised as a solution. A more general mesh works up to
`sqrt(x)(log x)^alpha` for each fixed `alpha<1/2` by the same sieve budget.

Read **PROOF.md**, then **ATTEMPT.md** for the missing signed upper bound and
its failed source-insensitive estimates. `SOURCES.json` fixes the source and
external inputs; `CLAIMS.json` separates proofs, imported/conditional facts,
and the open assertion. Classical sieve, orthogonal projection and Hardy
arguments are credited. No external novelty claim is made.

`check.py --check result.json` reconstructs seven finite groups and six
integer-directed sample-energy certificates through square endpoint `128^2`.
At `M=128`, `0.565641628407<S_M<0.565641628409`. This is NOT a certified
infinite coarse sum, a full J value, or a convergence experiment. See
VALIDATION.md for the exact executed checks and limits.

The change is add-only in its own research directory; no predecessor or
canonical mathematical status is changed.
