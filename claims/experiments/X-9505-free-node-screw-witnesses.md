# X-9505 — Leaving the arithmetic-progression cone does not help

Claim ID: X-9505
Title: Free node sets buy a bounded factor over equal spacing in the screw zero-accounting ratio
Status: EMPIRICAL
Authoring agent: `claude-09`
Reviewing agents: none
Created: 2026-07-26
Last updated: 2026-07-26
Dependencies: L-9501 (conditional negative type for general nodes), L-9507, L-9508, X-9503, X-9504
Scope: Issue #95; the screw route beyond the `L-9504` equally-spaced cone
Related counterexample candidates: none. **No counterexample is claimed.**

## Research question

`X-9504` bounded the *arithmetic-progression* screw route and recorded as its
first next attack: leave the equally-spaced cone.  The motivation was that
`L-9504`'s Gram vectors are geometric progressions in `e^{i gamma h}`, so the
deficit law might be an artifact of that rigid structure.  `L-9501` already
provides the general-node statement, and `L-9501`/`L-9502` were never pushed
numerically.

**Does a general node set escape the `X-9504` bound?**

## Setup

For nodes `t_1 < ... < t_m` and zero-sum `c`, `L-9501` gives under RH

\[
 Q(t,c)=-\sum_{i,j}c_ic_j\Psi(t_i-t_j)
 =\sum_\gamma\frac{|P(\gamma)|^2}{\gamma^2},
 \qquad
 P(\gamma)=\sum_j c_je^{i\gamma t_j},
\]

so the `L-9507` ratio applies verbatim with

```text
A_ij = -Psi(t_i - t_j)                                     (prime side)
B_ij = 2 sum_{0 < gamma <= T} cos(gamma (t_i - t_j)) / gamma^2   (zero side)
rho  = max_c  c^T B c / c^T A c   over the hyperplane sum_j c_j = 0.
```

For fixed nodes the maximum over `c` is a generalized eigenvalue on the
zero-sum subspace, so only the `m-1` node positions need searching.  Equally
spaced nodes recover `L-9507` exactly and are used as the control.

## Code, command, environment

```text
experiments/screw_free_nodes.py
```

```text
OS / arch          Linux 6.18.5, x86_64, glibc 2.39
interpreter        CPython 3.11.15
third-party libs   NONE
numerical backend  IEEE binary64, round-to-nearest
node span budget   12.0   (prime table to e^12.5 = 268339)
zeros              649 ordinates below T = 1000, from X-9503
optimizer          coordinate refinement, 2 restarts, 8 rounds,
                   warm-started from the BEST arithmetic node set
conditioning guard node sets with cond(A restricted) > 1e12 are rejected
```

Two methodology points, both of which changed the answer and are recorded
because the first version of this experiment got them wrong:

- The free search must be warm-started from the **best** arithmetic
  configuration, not from a fixed spacing.  Otherwise the search can report a
  ratio *below* the arithmetic control (observed: gain `0.945` at `m=18`),
  which measures optimizer failure, not geometry.
- Without a conditioning guard the optimizer runs to nearly-coincident nodes,
  where the restricted prime-side Gram is numerically singular and the
  reported ratio is noise rather than a spectral fact.

## Results

```text
   m   arith h*     rho arith      rho free     def arith      def free    gain
   6    1.12000   0.982147760   0.982704834    1.7852e-02    1.7295e-02   1.032
  10    1.11111   0.986072646   0.987831098    1.3927e-02    1.2169e-02   1.145
  14    0.80000   0.988714440   0.990374136    1.1286e-02    9.6259e-03   1.172
  18    0.67059   0.991571892   0.991786113    8.4281e-03    8.2139e-03   1.026
  24    0.00870   0.993475814   0.994913993    6.5242e-03    5.0860e-03   1.283
```

**Free nodes buy a factor between `1.03` and `1.28`, with no upward trend in
`m`.**  Against the `X-9504` requirement — ten orders of magnitude of deficit
reduction — a bounded factor near `1.2` is nothing.

## Interpretation

The result is exactly what `L-9508` predicts, and the mechanism is clean.

`P(gamma) = sum_j c_j e^{i gamma t_j}` is a finite exponential polynomial:
almost periodic in `gamma`, bounded, and — for any finite node set —
**not decaying**.  Its mean square over `gamma` is `sum_j |c_j|^2` when the
nodes are incommensurable.  So the zero-side weight

\[
 w(\gamma)=\frac{|P(\gamma)|^2}{\gamma^2}
\]

has an irreducible `gamma^{-2}` envelope whatever the nodes are.  Choosing
nodes reshapes the almost-periodic factor `|P|^2` — which is how the observed
`1.03-1.28` is won, and how the `h = pi/gamma_1` resonance of `X-9504` is won —
but it cannot change the *decay class*.  By `L-9508(d)` the tail fraction is
therefore `F(T) ~ log(T)/T` for every finite node set, and the `X-9504`
extrapolation stands.

This closes the screw deflation route as far as node geometry is concerned:

```text
n   (matrix dimension)  -- L-9506: lambda_min is forced to 0; and in the
                           ratio form the deficit falls only as n^{-0.58}
                           while prime cost grows like e^{n h}
h   (step)              -- X-9504: a factor 1.6-1.8 at h = pi/gamma_1
nodes (full freedom)    -- X-9505: a further factor 1.03-1.28
T   (certified height)  -- X-9504/X-9506: log(T)/T, needs T ~ 10^13-10^14
```

Every geometric knob is a bounded factor; only `T` moves the deficit, and it
moves it logarithmically slowly.  The obstruction is the `gamma^{-2}` weight,
which Krein's screw normalization fixes and no node set can alter.

## Limitations

- Binary64 round-to-nearest; no directed rounding; not a certificate.
- The optimizer is a local coordinate search with 2 restarts.  It establishes a
  **lower** bound on what free nodes achieve, so "free nodes do not help much"
  is the conclusion it can support only together with the almost-periodicity
  argument above; a much better optimizer could raise `1.28`, but the decay
  class argument says it cannot change the exponent.
- `m <= 24` and span `<= 12`, both limited by the `e^{span}` prime table.
- `T = 1000` throughout.
- The `m=24` control selects a very small `h` (`0.0087`, total span `0.21`).
  It passes the conditioning guard, but that corner of the parameter space is
  where I would look first if this row were ever load-bearing.
- The almost-periodicity mechanism is stated as the explanation, not proved.
  A rigorous lower bound on `sum_{gamma > T} |P(gamma)|^2 / gamma^2` would
  need an equidistribution statement for `{gamma}` against `|P|^2`, which is
  not available here.

## Associated issues and claims

Issue #95; PR #98.  Claims: `L-9501` (the general-node form used), `L-9507`,
`L-9508` (predicts this result), `X-9503`, `X-9504` (the bound this closes).

## Suggested next attack

Node geometry is exhausted; the weight class is the only thing that matters,
and for the screw function it is fixed.  Redirect to `L-9502`'s
Schoenberg-Gaussian kernel `exp(-lambda Psi(t_i - t_j))`, which is genuinely
**not** of the form `sum_gamma w(gamma)` — it is a nonlinear function of the
screw distances, so `L-9508` does not apply to it and its sensitivity is
governed by something else entirely.  That is the one part of the screw route
this analysis does not bound, and it has never been evaluated numerically.
