# M-26101 — Adversarial protocol for the annular divisor-frame proposal

Claim ID: `M-26101`  
Status: **PROPOSED REVIEW PROTOCOL**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Issue: #261

## 1. Review order

1. `L-26101` — exact divisor-gradient and Gram algebra;
2. `X-26101` — exact finite replay and mutations;
3. `L-26102` — annular positivity and objective transfer;
4. `L-26103` Sections 1--4 — compression, projection, and complete-period model;
5. `L-26103` Section 5 — the open `SAF` theorem;
6. `T-26101` — conditional prime-ramp and RH composition;
7. `O-26101` and `recon.py` only as floating discovery;
8. inherited square-screw/Landau normalization.

## 2. Automatic rejection conditions

Reject the proposal if any one of the following occurs.

### Algebra/source failures

- the adjacent-flow update does not equal `-A_XF` on every prime-power row;
- a prime-power multiplicity is omitted from the formal identity for `log(m/(m-1)`;
- identical annular rows are compressed without retaining the maximum residual;
- the flow is applied to non-prime-power constraints as though they were part of the dual;
- the parabolic seed or target normalization differs across files.

### Positivity/cost failures

- a proposed flow has norm large enough to exhaust the fixed annular seed slack;
- the two boundary sites adjacent to the annulus are not checked;
- objective cost is estimated with a pointwise `j^-2` bound but the number of sites is forgotten;
- signed objective gain is silently replaced by an absolute loss with the wrong orientation.

### `SAF` failures

- a generated active Gram has a singular or superpolynomially small positive eigenvalue after exact row compression;
- leakage creates an active residual set for which the stated contraction fails;
- a frame estimate is proved only for the initial active set, not every generated set;
- an arbitrary-subset frame theorem is substituted for the source-specific quantifier;
- the iteration uses floating pseudoinverses without a symbolic or directed proof;
- prime-power-chain duplicates or the exceptional cluster `{2,3,4,5}` are ignored;
- negative seed slack is set to zero before leakage is tested.

### Global-transfer failures

- the resulting flow does not make every prime-power row feasible;
- the prime-ramp identity omits higher prime powers;
- the square-screw constant `4` or the sign of the one-sided envelope is changed;
- Landau continuation is invoked from sparse samples without the derivative/interpolation bridge.

## 3. Minimum production object

A proof-grade `SAF_X` object should contain:

```text
X, alpha, beta, annulus endpoints
complete prime-power manifest
exact parabolic residual intervals
identical-row equivalence classes
for every iteration:
  active representatives
  exact/directed Gram matrix
  lower frame eigenvalue
  active residual vector
  exact/directed minimum-norm increment
  leakage residual on every inactive row
  positive-residual contraction ratio
cumulative flow and L2 norm
minimum repaired b coordinate
maximum final prime-power defect
exact objective-loss enclosure
source and producer digests
```

A finite ladder is not an all-scale theorem. Production blocks are useful only after the symbolic mechanism establishing uniform `SAF1`--`SAF3` is identified.

## 4. Mandatory mutations

The consumer should reject at least:

1. deleting the `-1_(q|j+1)` channel;
2. replacing the central coefficient `2` by `1`;
3. omitting a highest prime-power row such as `16`;
4. using `A_S^*r_S` without the Gram inverse;
5. retaining a weaker duplicate-row residual instead of the class maximum;
6. dropping the exceptional cluster;
7. taking the positive part of the seed defect before accounting for negative slack;
8. reporting a flow norm or objective cost not reconstructed from the emitted flow.

## 5. Status discipline

The exact algebra and conditional transfer may be classified independently. Until `SAF1`--`SAF3` are proved for all sufficiently large `X`, the correct global status is

```text
FULL ELEMENTARY PROPOSAL
ACTIVE-FRAME THEOREM OPEN
RH UNPROVED
```

No numerical convergence trend should be described as evidence that RH is true.