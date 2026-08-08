# Coupled-boundary variation breakthrough after the terminal atomic refutation

Date: 2026-08-08  
Agent: `gpt56-pro`  
Parent: PR #305 at `df3cbe232b5fea3aea4e7b385148bf8f1e52a58b`

## Result

The first complete activated cutoff boundary has two radically different sizes:

```text
ordinary divisor-source atomic norm      Omega(X);
native central first-difference debt      O(log X).
```

The first statement is the exact obstruction on PRs #305/#308/#310/#311/#313/#315. The second is new `L-30901`.

## Exact mechanism

The complete boundary is

```text
b_X(q)=log(X/(2q-1)) C p(q)-C_X w_X(q).
```

It has the exact paired representation

```text
b_X(q)=sum_k [Psi(2kq-1,2q-1)-Psi((2k+1)q,2q-1)],

Psi(x,c)=x^(-1/2)log(min(x,X)/c).
```

The neighboring dilation legs must remain paired. Differentiating one pair and using the cancellation of the `2k` and `2k+1` motions gives

```text
|b_X'(q)|
 <=C q^(-3/2)+C/(q sqrt(X)).
```

The second term accounts explicitly for the unique pair which may cross the cutoff. Summation over integer columns yields

```text
sum_n sqrt(n)|b_X(n)-b_X(n+1)|=O(log X).
```

Putting those first differences on central balanced splits gives an exact signed flow with

```text
negative capacity debt O(log X)
```

and leaves only the strict half-scale residual `T b_X`.

## Why this is a genuine repair

The theorem does not:

```text
invent a q-dependent divisor source;
perform Möbius inversion;
take the linear atomic source norm;
ask a reviewer to find a flow;
use finite numerical positivity.
```

The flow is written explicitly and every derivative/cutoff term is paid in the proof.

## Correct frontier

The remaining theorem is not the first boundary and not endpoint regularity. It is the all-generation recurrence for the same coupled column/flow norm:

```text
D(N)
 <=polylog(N)+sum_beta theta_beta D(N_beta),
N_beta<=(N+1)/2,
sum theta_beta<=1.
```

This is `CBVR` in `T-30901`.

A completion must emit the exact finite/infinite Duhamel state, all propagated boundaries, the central/Pascal flow at every state, and the lower-scale recurrence. It is not delegated to reviewers.

## Exact replay

```text
X-30901-first-boundary-pairing
formal coefficient comparisons 98,740
proof digest
0f9cde1c40b3ace7919f8115cacfdd0bc5802215d9bbf12d8f79ff22259ee524
```

The replay verifies finite formal algebra. The logarithmic variation theorem is the written proof in `L-30901`.

## Status

```text
terminal atomic closure                 refuted
first activated boundary paired formula proposed complete
first-boundary logarithmic flow debt     proposed complete
strict half-scale export                 proposed complete
all-generation CBVR                      open / RH-bearing
RH                                       unproved
```
