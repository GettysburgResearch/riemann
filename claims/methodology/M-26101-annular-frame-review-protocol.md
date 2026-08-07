# M-26101 — Adversarial protocol for the annular dual-frame proposal

Claim ID: `M-26101`  
Status: **PROPOSED REVIEW PROTOCOL**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Issue: #261

## 1. Review order

1. `L-26101` — exact divisor-gradient and Gram algebra;
2. `X-26101/verify.py` — exact finite replay and mutations;
3. `L-26102` — annular positivity and objective transfer;
4. `L-26104` — elementary polylog initial-residual budget;
5. `L-26105` — exact Hilbert–Farkas primal/dual equality;
6. `X-26101/verify_dual.py` — exact dual/potential replay;
7. `L-26106` — monotone projected-dual recursion;
8. `O-26102` — additive-rigidity proof route;
9. `L-26103` — corrected active-set algebra and withdrawn half-step invariant;
10. `T-26101` — `ADF` to the prime ramp and RH;
11. `O-26101/recon.py` only as floating discovery;
12. inherited square-screw/Landau normalization.

## 2. Automatic rejection conditions

Reject the proposal if any one of the following occurs.

### Algebra/source failures

- the adjacent-flow update does not equal `-A_XF` on every prime-power row;
- a prime-power multiplicity is omitted from the formal identity for `log(m/(m-1))`;
- identical annular rows are compressed without retaining the maximum residual;
- the flow is applied to non-prime-power constraints as though they were part of the dual;
- the parabolic seed or target normalization differs across files.

### Initial-budget failures

- the final zero term when `q|X` is counted as a nonzero continuous interval;
- the periodic selector primitive is allowed to grow with `q` rather than being bounded by one;
- the boundary term at `T_q` is omitted;
- the sum over prime powers is estimated without the `1/q` factor;
- the `q=X` endpoint is not treated separately.

### Positivity/cost failures

- a proposed flow has norm large enough to exhaust the fixed annular seed slack;
- the two boundary sites adjacent to the annulus are not checked;
- objective cost is estimated with a pointwise `j^-2` bound but the number of sites is forgotten;
- signed objective gain is silently replaced by an absolute loss with the wrong orientation.

### Hilbert–Farkas / `ADF` failures

- the dual multipliers are not restricted to the nonnegative cone;
- a positive dual null vector is ignored in the infeasible case;
- the homogeneous ratio is stated without its positive numerator part;
- the denominator omits a neighbor channel or a prime-power row;
- `ADF` is proved only for an arbitrary convenient subclass of dual vectors;
- the von-Mangoldt near-null vector is bounded by a generic frame estimate rather than by the signed source pairing;
- the logarithmic mode is removed before the first-cell/prime-ramp mutation is checked.

### Recursive-producer failures

- projected-dual ascent uses a step larger than the inverse Gram spectral bound;
- monotonicity is asserted for the positive-residual norm instead of the dual energy;
- the withdrawn uniform half-step leakage contraction is silently reused;
- floating pseudoinverses are presented as an all-scale proof;
- the emitted flow norm is not reconstructed from the dual/primal object.

### Global-transfer failures

- the resulting flow does not make every prime-power row feasible;
- the prime-ramp identity omits higher prime powers;
- the square-screw constant `4` or the sign of the one-sided envelope is changed;
- Landau continuation is invoked from sparse samples without the derivative/interpolation bridge.

## 3. Minimum production object

A proof-grade annular object should contain:

```text
X, alpha, beta, annulus endpoints
complete prime-power manifest
exact parabolic residual intervals
L-26104 pointwise residual majorants
exact A_X and A_X^* formulas
one of:
  an ADF proof covering every nonnegative lambda; or
  a source-bound primal flow with norm X^o(1)
minimum repaired b coordinate
maximum final prime-power defect
exact objective-loss enclosure
von-Mangoldt near-null mutation
source and producer digests
```

For a projected-dual producer, also retain:

```text
dual iterates
safe step bound
monotone dual energy
primal flow A_X^* lambda
KKT residual and complementarity
```

A finite ladder is not an all-scale proof.

## 4. Mandatory mutations

The consumer should reject at least:

1. deleting the `-1_(q|j+1)` channel;
2. replacing the central coefficient `2` by `1`;
3. omitting a highest prime-power row such as `16`;
4. using `A_S^*r_S` without the Gram inverse in the active diagnostic;
5. retaining a weaker duplicate-row residual instead of the class maximum;
6. taking the positive part of the seed defect before accounting for negative slack;
7. dropping the positive part in the homogeneous dual numerator;
8. reporting a flow norm or objective cost not reconstructed from the emitted object.

## 5. Status discipline

The exact algebra, initial source budget, duality, and recursive potential may be classified independently. Until `ADF` is proved for all sufficiently large `X`, the correct global status is

```text
FULL ELEMENTARY PROPOSAL
ANNULAR DUAL FRAME INEQUALITY OPEN
RH UNPROVED
```

No numerical trend should be described as evidence that RH is true.