# X-14201 — Exact dyadic FIR refinement controls

Status: exact finite synthetic regression  
Agent: `gpt56-05-k`  
Issue: #142  
Claims: T-14201

## Purpose

T-14201 states that the zeta screw criterion may be searched on one countable
family of dyadic arithmetic-progression Toeplitz matrices. X-14201 checks the
finite algebra used by that reduction:

- zero-sum FIR coefficients;
- cumulative increment vectors;
- equality between the screw form and the increment Toeplitz quadratic;
- exact preservation under dyadic grid refinement.

It does not evaluate the Riemann zeta function.

## Synthetic kernel

Use

\[
 \Psi(t)=-t^2.
\]

For spacing `h=1/16` and coefficients supported at indices `0` and `5`,

```text
c = (1,0,0,0,0,-1),
b = (1,1,1,1,1).
```

The exact screw and Toeplitz forms agree:

\[
 \mathcal W_h(c)=b^THb=-\frac{25}{128}.
\]

Refining to `h=1/32`, inserting zeros at odd coefficient indices, and duplicating
each increment coordinate preserves the physical nodes and the exact value
`-25/128`.

This is a synthetic negative-kernel control, not a Riemann-Hypothesis witness.

## Reproduction

```bash
python verify.py certificates/synthetic.json \
  --output results/synthetic-verification.json
python -m unittest discover -s tests -v
python -m compileall -q verify.py tests
```

Seven deterministic tests pass.

## Fail-closed tests

The checker rejects:

- nonzero coefficient sum;
- false sign or exact-value claims;
- Boolean values masquerading as integers;
- invalid refinement factors;
- any refinement that changes the physical quadratic value.

## Production handoff

Replace the synthetic quadratic kernel by one correlated directed table for
Suzuki's exact `Psi(r/2^k)`. Preserve symbolic prime-power knots and prove every
`log q` comparison outwardly. The final checker should consume only exact
vectors and rational interval endpoints.
