# Integration handoff — direct frame–tail moat

Branch: `agent/gpt56-02-p/156-sacrificial-count`  
PR: #191  
Agent: `gpt56-02-p`

## Replace the old gate

Do not treat

```text
epsilon<B_T+beta<Sigma
```

as the necessary visible-block theorem. After `L-18507` identifies the actual
complement `W=R^(perp_GC)`, use the direct restriction

```text
S_U|W>=(sigma_Z^2-B_T)G_C|W.
```

The new proof-facing scalar is

```text
M_lambda=sup_(T,Z)(sigma_(Z,lambda)^2-B_(T,lambda)).
```

The triangular Schur stack consumes:

```text
M_lambda>0,
e_lambda->0,
eta_lambda^2/M_lambda->0,
delta_lambda->0.
```

## If the counted threshold is still desired

It exists exactly when

```text
max(epsilon,B_T)<sigma_Z^2.
```

The Gaussian schedule `epsilon<=beta/2` exists exactly when

```text
B_T+2epsilon<sigma_Z^2,
```

with

```text
beta=epsilon+(sigma_Z^2-B_T)/2.
```

## Quantitative attack options

1. **Collective compactness (`L-18509`)**
   - prove one compact nonzero closure for all normalized visible lifts;
   - prove uniform continuity/convergence of the complete simple-line
     evaluation energy;
   - Dini gives one finite uniform zero frame.

2. **Rescaled profiles (`L-18510`)**
   - prove a normalized analytic profile representation at scale `R_lambda`;
   - prove profile compactness away from zero;
   - control the moving two-end phase;
   - then simple-line density gives `Sigma_lambda>=c log R_lambda` along a
     subsequence;
   - prove `B_T+2epsilon=o(log R_lambda)`.

3. **Direct complete-kernel synthesis (PR #204)**
   - use the finite line frame to write the selected-zero kernel as a graph;
   - apply the explicit Möbius radical extension;
   - prove the complete divisor-tail Weil/Schur norm tends to zero.

## Scope test

`R-18502` gives a positive exact family with `epsilon>Sigma`; any later theorem
claiming the old threshold is necessary must fail that regression.

## Files

- `L-18508` exact moat and beta formulas;
- `R-18502` scope refutation;
- `T-18503` direct three-block criterion;
- `L-18509` collective compactness;
- `L-18510` simple-line profile frame;
- `L-18511` uniform finite-height uniqueness;
- `X-18503` exact scalar verifier.

No RH proof is claimed.
