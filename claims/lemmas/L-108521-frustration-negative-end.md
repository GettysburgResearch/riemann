# L-108521 — Frustration forces the negative end: lambda_min <= -3 + 4f/n for cubic graphs

```text
Claim ID: L-108521
Status:   PROVED (one-paragraph Rayleigh argument below; machine
          consistency checks against the exact corpus rows). Together
          with L-108520 this gives both poles of the O-108517
          dichotomy a proved mechanism.
Created:  2026-08-31 (pass 3 continuation, Lane 3)
Programme: #763 (graph purity mechanisms)
Depends on: none (self-contained)
RH status: RH and GRH are unproved; this claim does not address them.
```

## Statement

Let `G` be a cubic graph on `n` vertices with frustration index `f`
(minimum number of edges whose deletion makes G bipartite). Then

```text
lambda_min(G) <= -3 + 4f/n .
```

**Corollary 1 (low frustration = negative-end breach).** If
`f < n (3 - 2 sqrt 2)/4` (~ 0.0429 n), then
`lambda_min < -2 sqrt 2`: the graph breaches the NEGATIVE Ramanujan
end. In particular every cubic graph with `f = 2` and `n >= 47` is a
negative-end breacher.

**Corollary 2 (positive-end-only needs LINEAR frustration).** A
positive-end-only graph (no negative breach) must have
`f >= n (3 - 2 sqrt 2)/4`. So along any infinite positive-end-only
family (e.g. GP(n', 2), n' >= 24, on n = 2n' vertices — T-108514)
the frustration index grows at least linearly; and the O-108517
observation that the f = 2 corpus members all enter at the negative
end is the small-n shadow of a theorem that becomes unconditional at
n >= 47.

## Proof

Let `F` be a frustration-optimal edge set (`|F| = f`, `H = G - F`
bipartite and spanning), and let `x in {+-1}^n` be the bipartition
sign vector of `H` (constant on each side). Every edge of `H` joins
opposite signs and every edge contributes `2 x_u x_v` to
`x^T A_G x`, so

```text
x^T A_G x = -2 |E(H)| + sum_{(u,v) in F} 2 x_u x_v
          <= -2 (3n/2 - f) + 2f = -3n + 4f ,
```

and `lambda_min <= x^T A_G x / x^T x = -3 + 4f/n`. ∎

(Sharpness at the ends: `f = 0` gives the bipartite value `-3`; the
bound degrades linearly at rate 4/n exactly as an added
frustration edge can cancel at most two units of the quotient.)

## Machine consistency (exact corpus rows, phase_diagram.json)

Every corpus row satisfies the bound, e.g. GP(9,1): f = 2, n = 18,
bound -2.556, actual lambda_min < -2 sqrt 2 (Sturm); Moebius8: f = 2,
n = 16, bound -2.5, actual < -2 sqrt 2; the window families' f = 4
rows at n = 16..22 have bounds -2 to -2.27, consistent with their
POSITIVE-only phase (lambda_min > -2 sqrt 2 there, and indeed
4f/n = 1 to 0.73 > 3 - 2 sqrt 2). At n = 16 the bound requires only
f >= 1 for positive-only graphs; the exhaustive value is f = 4
(pos16_frustration.json) — the gap between the linear-rate constant
here and the observed constants is deposited as the remaining
quantitative question (is the true threshold rate the Rayleigh 4/n,
or does an expander-type argument force more?).

## Mechanism reading

O-108517's two exact dichotomies now both have proofs at their poles:
LOW FRUSTRATION forces the negative end (this lemma, rate 4f/n);
LONG CORRIDORS force both ends (L-108520). The two-invariant diagram
is the finite-size portrait of these two theorems plus the
still-open middle (the h <= 1/4 expansion dichotomy, whose provable
Cheeger constant is three times smaller than observed).
```
