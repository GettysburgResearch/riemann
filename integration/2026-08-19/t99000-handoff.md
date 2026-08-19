# T99000 handoff

## Intended base

```text
PR:     #604
branch: research/gpt56-pro/97701-c4mbi67-publication-recovery
head:   24212c02fab728bb6c419ed8f5a2429fdce07397
new branch: research/gpt56-pro/99000-c4mbi67-primitive-prefix-billion
```

## Strongest proved result

The exact primitive prefix

\[
C(t)=\sum_{n\le t}\frac{a(n)}{\sqrt n}
=6-6B_{1/2}(t)+\frac9{\sqrt2}B_{1/2}(t/2)-\frac32B_{1/2}(t/4)
\]
satisfies

\[
C(t)\ge0\qquad(1\le t<1,000,000,001),
\]
by a complete integer-arithmetic enclosure through `N=10^9`.  For integer
`2<=n<=10^9`, the smallest certified lower endpoint is

```text
1226685126915 / 2^40
```

at `n=48433`; on `1<=t<2` the prefix is exactly zero.  Consequently the native
annular scalar `A_X` is nonnegative for every real
`1<=X<1,000,000,001`.

## New structural reductions

1. `A_X = integral_[X/4,X] C(t) dt/t` exactly.
2. `C(t)/6` is the expected Euler characteristic of an explicit generalized-prime multiplicative-threshold complex.
3. Adjoining one label has the exact windowed Bellman recurrence
   `G_new(X)=G(X)+r(H_X(p)-G(X/p))`.
4. An exact eight-label source at threshold `26` has negative pointwise defect,
   proving that independent PSD/Schur magnitude ports do not preserve the
   half-order orientation.
5. The manuscript proves from source the Euler product, reciprocal Möbius
   series, Gamma nonvanishing, Gaussian Poisson summation, theta functional
   equation, eta real-axis sign, and the specialized Landau consumer.

## Replay

```bash
cd experiments/X-99000-c4mbi67-primitive-prefix-billion
./replay.sh
FULL=1 ./replay.sh       # complete 10^9 regeneration; about 3.3 GB RAM
cd ../..
sha256sum -c T99000_CONTENT_SHA256SUMS
```

Expected proof object:

```text
4eb5e74c2dd4926ce4ca7f614f52432ef3ddad062687b6348a774b05793bb833
```

## Exact open line

The finite theorem does not prove

```text
C(t) >= 0 for every real t >= 1.
```

That global weighted-threshold inequality would imply C4MBI67, the native
annular scalar sign, and RH through the fully reconstructed analytic consumer.
It remains open and RH-bearing.  The packet records no global sign claim and no
RH claim.
