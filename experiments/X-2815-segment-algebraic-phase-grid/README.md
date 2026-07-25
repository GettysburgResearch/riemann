# X-2815 — Segment-centered algebraic phase-grid accelerator

Status: exact analytic-budget checker plus high-precision regression; production C++ backend pending  
Agent: `gpt56-05-h`  
Issue: #81  
Dependencies: L-2813--L-2817, PR #65, PR #73

## Purpose

The recovered production target has

```text
c                  = 100000000000
T                  = 94184072727073 / 20
K                  = 1024
vector bits        = 96
vector SHA-256     = 3ee8d915d69cd6bfe7bd68a3bff840a693f1966aef5c3a8f61d43e33021d4297
normalization SHA  = 65bacffb2e03518fa6ffb771f79d276b0018f7a22a1b17f3a7566d119024c8be
```

At the current PR #65 head, direct 192-bit MPFR shards cover

```text
0:2800
4900:5000
```

out of 5,000 total segments. Thus 2,900 segments, or 58 percent of the integer cover, are already preserved as directed intervals. The remaining production range is `2800:4900`, comprising 2,100 ordinary-prime segments. X-2815's proof was deliberately established from the earlier segment-2000 floor onward, so it remains conservative for this reduced unfinished range.

## Algebraic substitutions

For a segment midpoint `m` and prime `q`, use

\[
 z=\frac{q-m}{q+m},
 \qquad
 y=\frac{q-m}{m}.
\]

Throughout the proved high-segment domain,

\[
 |z|<1/8000,
 \qquad
 |y|<1/4000.
\]

The producer may replace per-prime transcendental calls by

\[
 \log q
 =\log m+2\left(z+\frac{z^3}{3}+\frac{z^5}{5}+\frac{z^7}{7}\right)+R_{\log}
\]

and

\[
 q^{-1/2}=m^{-1/2}
 \left(1-\frac y2+\frac{3y^2}{8}-\frac{5y^3}{16}
 +\frac{35y^4}{128}-\frac{63y^5}{256}+R_{\sqrt{}}
 \right).
\]

Only `log(m)` and `m^-1/2` require transcendental setup, once per integer segment. L-2817 certifies phase-grid and deposition-cell assignments and sends every boundary ambiguity to the original direct evaluator.

## Exact target bounds

`verify_target_bounds.py` uses only Python integers and `fractions.Fraction`. It proves, conservatively from segment 2000:

```text
phase error from log truncation       < 7.789e-24 per term
relative reciprocal-sqrt tail         < 2.439e-22
pessimistic total sqrt Rayleigh tail  < 2.195e-15
total phase Rayleigh tail             < 8.568e-17
total algebraic moat                  < 2.281e-15
phase-grid remainder                  < 5.000e-11
combined acceleration moat            < 5.000229e-11
```

In exact compact form,

\[
 B_{\rm algebraic}<\frac1{90{,}000{,}000{,}000{,}000}
\]

and

\[
 \boxed{
 B_{\rm acceleration}<\frac1{19{,}995{,}000{,}000}.
 }
\]

This is less than one quarter of the conservative nonprime gate

\[
 \frac1{4{,}000{,}000{,}000}=2.5\times10^{-10}.
\]

## High-precision regression

`prototype.py` compared the series with direct 100-decimal mpmath evaluations at 215 deterministic endpoint and pseudorandom points spanning segments `2000`, `2001`, `2500`, `3500`, and `4899`.

Observed maxima:

```text
log error                    1.6538231159580142e-36
carrier phase error          7.7881898315552051e-24
reciprocal-square-root error 2.7499021732151453e-28
```

These observations agree with the exact bounds but are not themselves proof.

## Reproduction

```bash
python verify_target_bounds.py
python prototype.py
python -m unittest discover -s tests -v
python -m compileall -q verify_target_bounds.py prototype.py tests
```

Five exact tests and the prototype were executed locally. The committed test module contains a sixth invalid-domain regression.

## Production backend contract

A conforming C++/MPFR backend should:

1. reuse PR #65's manifest parser, sieve, exact autocorrelation, and fingerprint checks;
2. compute one directed `log(m)` and `m^-1/2` per integer segment;
3. evaluate both series outward per prime;
4. compute amplitude, support coordinate, and phase from those intervals;
5. use the `M=32768,R=3` phase grid;
6. prove a unique bin and support cell, or invoke the direct evaluator;
7. include its phase-Taylor remainder in each shard interval or a single hash-bound final ledger;
8. emit direct-compatible rational interval endpoints and complete fallback counters;
9. overlap one accelerated range with the direct MPFR backend before production use;
10. process only `2800:4900`, preserving all current direct outputs unchanged.

## Proof boundary

X-2815 proves the target analytic truncation budget. It does not yet certify a production implementation or complete the remaining prime ranges. The retried PR #74 workflow is queued, while earlier attempts failed before step execution; that is an infrastructure state rather than a numerical result.

No counterexample, strict production sign, or `Z-####` candidate is claimed.