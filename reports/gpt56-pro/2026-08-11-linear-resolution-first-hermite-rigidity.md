# Linear-resolution first-Hermite continuation — 2026-08-11

## Frozen base

```text
repository: gfreund123/riemann
base PR:    #390
base head:  ea20af8867c3119c23efc27738d343aac2f79362
branch:     research/gpt56-pro/390-linear-resolution-rigidity
```

## Result

PR #390 proved that negative first-Hermite centres are exponentially sparse for each heat resolution and simultaneously sparse through `q <= log^(1-epsilon) T`.

This continuation improves the cutoff from `exp(8q)` to `exp(aq)` for every fixed `a>2`:

\[
\sup_t|S_q(t)-S_{q,a}(t)|
\ll_a q^3e^{-a(a-2)q/4}.
\]

The corresponding \(2k\)-th moment transfer requires only

\[
akq\le\frac12\log T.
\]

For every fixed integer \(K\ge3\), use \(k=K\) and sum over

\[
q\le\frac{\log T}{4aK}.
\]

This gives

\[
\left|
\left\{
t\in[T,2T]:
\exists\,1\le q\le\frac{\log T}{4aK},
\ \mathcal M(q,t)<0
\right\}
\right|
\ll_{a,K}
T(\log T)^{1-K}.
\]

Thus, for every requested \(A>0\), positivity holds simultaneously for all integer

\[
q\le c_A\log T
\]

outside a set of measure \(O_A(T/\log^A T)\). The global exceptional set has finite logarithmic measure.

## Deterministic inverse theorem

A negative centre forces

\[
|S_{q,a}(t)|\gg\log T.
\]

Rotate by its argument and retain a minimum-cardinality subset of positive projections carrying half this mass. Since the coefficient square is \(q+O(\sqrt q)\), Cauchy--Schwarz gives

\[
\#\{\text{aligned prime powers}\}
\gg\frac{\log^2 T}{q}.
\]

Because the cutoff is \(p^r\le e^{aq}\), each prime supplies at most \(O_a(q)\) powers. Hence

\[
\#\{\text{aligned distinct primes}\}
\gg_a\frac{\log^2 T}{q^2}.
\]

At \(q\asymp\log\log T\), one exceptional terminal carrier must coordinate at least

\[
\gg\frac{\log^2 T}{(\log\log T)^2}
\]

distinct prime phases.

## Exact frontier

The unresolved step is no longer merely “exclude a large Dirichlet-polynomial value.” It is:

```text
exclude a high-codimension common-half-plane resonance
among log^2(T)/q^2 distinct primes
at a carrier capable of supporting an off-line zeta zero.
```

Average moments cannot remove one point. A final proof needs carrier-specific arithmetic or a deterministic avoidance theorem for the prime-log flow.

## Verification

```text
PASS_LINEAR_RESOLUTION_FIRST_HERMITE_RIGIDITY
```

The replay checks finite envelope and scaling identities only.

## Status

```text
adaptive Gaussian cutoff                         PROPOSED COMPLETE
linear-resolution density-one positivity         PROPOSED COMPLETE
arbitrary log-power exceptional saving           PROPOSED COMPLETE
finite-log-measure exceptional set               PROPOSED COMPLETE
prime-power/distinct-prime resonance codimension PROPOSED COMPLETE
one-point resonance exclusion                    OPEN / RH-EQUIVALENT
Riemann Hypothesis                               UNPROVED
```
