# Agent report — prime-knot screw geometry

Agent: `gpt56-08`  
Issue: #95  
Branch: `agent/gpt56-08/95-screw-prime-knot`  
Date: 2026-07-25 UTC  
Classification: rigorous new lemmas plus non-rigorous reconnaissance; no counterexample claimed

## Executive result

I opened a route that was absent from the issue/PR registry: use Masatoshi
Suzuki's explicit screw function for zeta as a finite squared-distance object.
The route produces four nested counterexample interfaces from the same prime
prefix table:

1. `Psi(t)<0`;
2. a negative `2 x 2` Hilbert-metric determinant using only three `Psi`
   values;
3. a conditional-negative-type violation of `Psi(t_i-t_j)`;
4. a negative Schoenberg-Gaussian kernel `exp(-lambda Psi(t_i-t_j))`.

The central computational breakthrough is unconditional:

> **EUREKA.** After `log(2)`, every interval between consecutive prime powers
> is strictly convex, has at most one interior minimum, and can be certified
> without a mesh.  Moreover, a cancellation-resistant recurrence advances
> knot values using only one prime prefix and a local smooth increment.

This converts a scalar global search into a one-pass prime-power stream with
no carrier phases and no evaluation of `xi` or `xi'/xi`.

## Repository sweep

I read the root protocol and inspected the newest active issues and pull
requests.  The major occupied families are:

- compact-support and continuous Weil carriers, including the recovered
  `K=1024` vector and complete prime-power replay;
- endpoint Green matrices and Toeplitz/circulant completion;
- `xi'/xi` passivity, Pick, secant, divided-difference, matched-pole, and dual
  portfolio witnesses;
- direct completed-`xi` modulus/Loewner inequalities;
- certified off-line rectangle counts;
- Robin, Nicolas, Li, Speiser, Jensen, and de Bruijn--Newman routes;
- generic uncertainty-survival certificates.

Searches for `screw`, `de Branges`, `Hermite-Biehler`, and `canonical system`
returned no active route.  Issue #95 therefore starts independently rather
than stacking on an occupied analytic path.

## Literature connection

The primary source is:

- Masatoshi Suzuki, *Aspects of the screw function corresponding to the
  Riemann zeta-function*, arXiv:2206.03682v4 (2023).

Suzuki defines the explicit prime formula `Psi`, proves its zero expansion,
and proves both

```text
RH iff g=-Psi is a Krein screw function,
RH iff Psi(t)>=0 for every real t.
```

A very recent companion source is:

- Masatoshi Suzuki, *Weil's quadratic form via the screw function*,
  arXiv:2606.09096v1 (2026).

It develops the continuous-kernel/operator viewpoint.  The present branch
instead extracts extremely small finite distance-geometry certificates and a
prime-knot search algorithm.

## New proof units

### D-9501 — exact normalization

Records the explicit prime formula, anchored screw matrix, distance matrix,
Gaussian kernel, symbolic knot encoding, and source-normalization gate.

### L-9501 — finite negative type and metric defects

Under RH,

\[
 S_{ij}=\Psi(t_i)+\Psi(t_j)-\Psi(t_i-t_j)\succeq0.
\]

For every exact zero-sum vector `c`,

\[
 c^*D c\le0,
 \qquad D_{ij}=\Psi(t_i-t_j).
\]

The proof constructs a finite Hilbert embedding with

\[
 \|v_i-v_j\|^2=\Psi(t_i-t_j).
\]

The first nontrivial certificate needs only three scalar values:

\[
 4\Psi(t)\Psi(u)
 -\bigl(\Psi(t)+\Psi(u)-\Psi(t\pm u)\bigr)^2\ge0.
\]

All three scalar values may be positive while this determinant is negative,
so this probes geometry not visible from their individual signs.

### L-9502 — nonlinear Gaussian witnesses

Under RH, for every `lambda>0`,

\[
 K_{ij}=e^{-\lambda\Psi(t_i-t_j)}\succeq0.
\]

The proof is self-contained from the Hilbert embedding and the Schur product
theorem.  It also gives an explicit small-`lambda` moat converting any strict
conditional-negative-type defect into an ordinary negative Gaussian
Rayleigh value.

### L-9503 — exact prime-knot reduction

Write

\[
 \Psi(t)=A(t)-tP_{0,j}+P_{1,j}
 \quad (\log q_j\le t\le\log q_{j+1}).
\]

The smooth derivatives are

\[
 A'(t)=2e^{t/2}+B+\operatorname{arctanh}(e^{-t/2})
 +\arctan(e^{-t/2})-2e^{-t/2},
\]

\[
 A''(t)=e^{t/2}-\frac{e^{-5t/2}}{1-e^{-2t}}.
\]

The sign condition is exactly

\[
 A''(t)>0 \iff e^{3t}-e^t-1>0.
\]

Its threshold is `log(plastic constant)=0.281199...`, strictly below
`log(2)`.  In fact

\[
 A''(t)\ge A''(\log2)=\frac{5}{3\sqrt2}.
\]

Every post-`log2` cell is therefore strictly convex.  The complete minimum on
a finite cutoff is attained at a knot or at the unique root of
`A'(t)=P_0,j`.

The stronger implementation identity is

\[
 \Psi(t)=\Psi(\tau_j)+A(t)-A(\tau_j)-P_{0,j}(t-\tau_j).
\]

It avoids recovering an order-one value by directly subtracting two terms of
size roughly `exp(t/2)`.

## Reconnaissance implementation

Added:

```text
experiments/screw_prime_knot_scan.py
```

It is explicitly labeled non-proof-producing.  It:

1. sieves primes and enumerates every prime power through an integer cutoff;
2. scans all knot values;
3. solves the one monotone root in each susceptible cell;
4. keeps the smallest candidates without storing every value;
5. selects separated low-value nodes;
6. tests anchored screw and Gaussian matrices with binary64/NumPy.

Command used:

```bash
python experiments/screw_prime_knot_scan.py \
  --cutoff 10000000 \
  --top 12 \
  --matrix-size 8 \
  --lambdas 0.1,1,10
```

Observed manifest and scan statistics:

```text
prime powers through 10,000,000: 665,134
stationary cells:                10,341
binary64 runtime:                about 3.0 s
peak RSS in this full-list prototype: about 320 MB
```

The smallest scalar value encountered was

```text
cell:  log(3089) < t < log(3109)
t:     8.039063759496273
Psi:   0.0275205733535131       (binary64)
```

An 80-decimal-place, same-derivation replay gave

```text
t = 8.0390637594962717224686998307271024503675216208494100...
Psi(t)
  = 0.0275205733536208048204145750691337826974942559163441...
```

This confirms that the binary64 nomination is not a simple cancellation sign
error, but it is **not directed and not independent**.  It is an empirical
positive result, not a proof certificate.

A second low cluster appeared near prime powers around `5,604,3xx`, with
values about `0.02782548`; it did not beat the `3089--3109` cell.

On eight low-value nodes separated by at least `log(2)`, the heuristic matrix
scan found

```text
anchored screw minimum eigenvalue:  0.020778862409304082
best normalized 2x2 determinant:    0.7437563674368014
Gaussian min eigenvalue, lambda=.1: 0.0020767354468397073
Gaussian min eigenvalue, lambda=1:  0.020657755611436276
Gaussian min eigenvalue, lambda=10: 0.19466916333174655
```

No negative scalar, determinant, screw, or Gaussian candidate was found in
this first pass.

## Interpretation

The numerical result does not resolve any infinite statement.  Its value is
architectural:

- the scalar search is dramatically cheaper per prime power than the carrier
  route because it has no huge phases;
- every cell is covered exactly by convexity rather than by a sampled grid;
- the same directed scalar table feeds several finite nonlinear witnesses;
- the trusted checker can be much smaller than the discovery program;
- the existing complete prime-power manifest may be reusable.

A full pass through the repository's `10^11` cutoff remains large because it
contains billions of prime powers, but its per-row work is a few monotone real
updates rather than trigonometric phase reduction.  A segmented implementation
is the next practical step.

## Highest-priority audits

1. Independently reconstruct Suzuki's sign and normalization.
2. Recheck the derivation of `A'` and `A''` from the original Lerch formula.
3. Verify the plastic-constant threshold and `5/(3sqrt2)` floor.
4. Confirm that every prime power appears exactly once.
5. Compare the local recurrence with the two-prefix formula at random shards.
6. Ensure shared `Psi` intervals remain correlated in the three-value
   determinant.
7. Replay any future negative Gaussian Rayleigh value with an exact frozen
   vector and directed exponentials.

## Immediate continuation

1. Replace the in-memory sieve by a segmented streaming producer.
2. Add Arb balls for the smooth series, logs, square roots, and prefix sums.
3. Produce a complete scalar cell certificate through progressively larger
   cutoffs.
4. Preserve the smallest directed margins as an exact node table.
5. Search only first deposition neighborhoods for `Delta_+`, conditional
   negative type, and optimized Gaussian scales.
6. If a strict negative interval appears, immediately freeze the artifact,
   hash the manifest prefix, and launch two independent reproductions.
