# Balanced Newton renormalization of the actual Mobius source

**PROPOSED research. No RH proof or unbounded native energy estimate.**
Author: Astra. Date: 2026-09-10.

The next attack is not another correction of an artificial Euler tail. Rebuild
an actual Mobius prefix at the square of the current scale, then control the
energy of this exact nonlinear arithmetic map. Two explicit late coefficients
remove its constant and reciprocal modes before the centered hyperbola
remainder is estimated. Their physical energy price remains in the state.

This combines the causal projection of PR836 with classical short-source
Mobius inversion and the repository's PR805 balanced-hyperbola programme.
It is NOT a claim to have discovered Newton/Mobius inversion or the idea of
balancing a hyperbola kernel. The differences are all-integer exact-prefix
preservation, TWO moment constraints, compact full-source norm control, and a
joint energy/mean recurrence that is genuinely repeatable after recompletion.

## Exact map and the proposed full-problem estimate

For b=Y+1 let

    E_Y=sum_(k<=Y) M(k)^2/[k(k+1)],
    u_Y=sum_(k<=Y) M(k)/[k(k+1)],
    A_Y=E_Y+2b u_Y^2.

The canonical finite c agrees with mu through Y, has support <=2b, and satisfies
`sum c_n=sum c_n/n=0`. Its ENTIRE energy is A_Y. Exactly,

    v=2c-1*c*c,
    v(n)=mu(n) for every n<(Y+1)^2.

The raw infinite-support v has a proved bounded cumulative tail and finite
whole-source norm. Retain its full new prefix and recomplete at
`B=(Y+1)^2-1`; the result is exactly the next canonical state. The prefix at
B is generated using only the prefix at Y, not a future arithmetic oracle.

A concrete OPEN sufficient target is

    1+A_B <= 2(1+A_Y)^(3/2)

on every sufficiently late stage of the ladder 1,3,15,255,65535,... . It would
give `E_X<=exp(O((log X)^log_2(3/2)))`, hence RH. More generally a gain below
the critical exponent two that is allowed to shrink, but has divergent total
along the ladder, suffices with summable normalized losses. That weaker
conditional theorem is proved; the arithmetic gains are not.

## What this packet actually proves

| ID | Component | Boundary |
|---|---|---|
| BNR26-1 | Unique optimal compact two-moment completion, full cost and orthogonality | Does not lower immutable prefix energy |
| BNR26-2 | Exact Newton prefix squaring, sharp first omitted coefficient, invariance under late source choices | Classical inversion lineage; no norm gain from algebra alone |
| BNR26-3 | Every raw quadratic stage is global L2 with an analytic full tail; recompletion costs at most a factor two | Not a uniformly small full-line residual or fixed-controller iteration |
| BNR26-4 | Exact centered hyperbola update of both E and u, including collar and integer Fourier endpoints | Signed centered form still needs a native estimate |
| BNR26-5 | Subquadratic or nonsummably accumulating vanishing gains imply RH | All native gain hypotheses OPEN; no converse asserted |
| BNR26-6 | Explicit two-moment non-Mobius sources force quadratic energy growth | Refutes generic balanced-vector shortcut, not RH or the native target |

[PROOF.md](PROOF.md) gives all six arguments. [RESEARCH_PLAN.md](RESEARCH_PLAN.md)
compares the prior routes and identifies the missing source-specific step.
[SOURCE_LOCK.json](SOURCE_LOCK.json) records exact source and reading scope.
[VALIDATION.md](VALIDATION.md) and [validation.json](validation.json) record
actual executions, finite scope and omissions.

## Finite evidence, not an asymptotic inference

Two implementations reconstruct the fixed report from primitive arithmetic.
The producer uses a sieve, scaled convolution and cumulative cells. The verifier
uses trial factorization, divisor fibers, signed work energies and direct floor
sums. Neither imports the other or repository modules.

All entries through 65535 are reproduced from the recursive seed and compared
with independent primitive arithmetic. The finite proposal is tested at 66 Y,
with 124 directed energy/mean panels. The exact finite result includes 72
projection tests, 440 centered-kernel/endpoint tests, 24 sharp boundary and
24 joint-state cases, four complete raw-future enclosures, and four non-Mobius
quadratic controls. Normal/optimized execution and twelve resealed corruption
tests are software evidence, not independent mathematical acceptance.

    python -S -B produce.py --check result.json
    python -S -B verify.py result.json --self-test
    python -S -O -B produce.py --check result.json
    python -S -O -B verify.py result.json --self-test

The decisive work is to prove a gain for the actual canonical source at
unbounded scales. More passing finite panels, a small continuum kernel, or
moment balance without the complete divisor identities does not supply it.
