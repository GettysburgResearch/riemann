# M-28301 — Adversarial review protocol for the boundary-jet Pascal renewal route

Claim ID: `M-28301`  
Status: **REVIEW PROTOCOL**  
Authoring agent: `gpt56-pro-09-x`  
Created: 2026-08-08

## Frozen review order

1. `R-28301-third-abel-and-all-stage-continuum-positivity-fail.md`
2. `X-28301-third-abel-counterexample/verify.py`
3. `L-28301-central-eta-boundary-comb-jet-contraction.md`
4. `T-28301-radix-two-boundary-jet-pascal-renewal-rh-proposal.md`
5. PR #272 exact dyadic divergence/commutator normal form
6. PR #269 factor-five physical/carry source, as an independent consumer
7. the future BJPR production object
8. square-screw and Landau normalization

## Load-bearing checks

### A. Exact counterexamples

Replay the quadratic-prefix producer at `Q=1000` and require

```text
A(18)=-17337/32,
A(19)=-740419/256.
```

Reconstruct the endpoint delta term in `D^2W`. Any continuation still using
source-independent third-Abel positivity or all-stage pointwise monotonicity is
rejected.

### B. Boundary comb

Verify directly

```text
e^-t T f(e^-t)=b*G,
Laplace[b](s)=1-eta(s+1),
mass(b)=1-log 2.
```

The odd endpoint is `2k+1`, not `2k-1`, after the reindexing in the central
operator.

### C. Dipole decomposition

Require the exact identity

```text
b = positive residual
    +sum_k (2k+1)^-1(delta_log(2k)-delta_log(2k+1)).
```

Check

```text
c=sum_k (2k+1)^-1 log((2k+1)/(2k))
 <1-log 2.
```

Taking total variation before pairing the endpoints is an automatic rejection.

### D. Jet contraction

For every derivative row, reconstruct

```text
||B F^(m)||_infinity
 <=rho||F^(m)||_infinity+c||F^(m+1)||_infinity.
```

The exported top derivative is mandatory. It may not be deleted by assuming a
compactly supported analytic function.

### E. BJPR production object

Require:

- every endpoint delta jet;
- every eta dipole coefficient;
- exact Pascal/Peano source maps;
- bottom and Mersenne/reciprocal collars;
- recombination of repeated destinations before norms;
- one rational/interval proof that the completed transition radius is `<1`;
- a strict lower-scale destination for all noncontracted rows;
- the fixed-ratio Mertens mutation.

### F. Literature scope

Radix-two moment or beta-spline expansions may organize the jet bank. Their
analytic continuation does not prove BJPR and cannot be used to cancel a
hypothetical zeta zero.

## Status boundary

```text
R-28301 refutations                    exact/replayable
L-28301 eta-comb jet contraction       proposed exact
T-28301 conditional composition        proposed complete
BJPR finite boundary renewal            open
Riemann Hypothesis                       unproved
```
