# X-26204 — Critical hyperbola bank split

This exact standard-library regression supports `L-26211`.

It verifies, for every integer scale `N=3,...,64`:

- complete inclusion–exclusion of all factor pairs with product below `N^2`;
- equality with the fixed output
  
  \[
  \varepsilon-\frac52\delta_2+\delta_4;
  \]
- the equivalent first-bank plus lower-scale-remainder decomposition;
- strict support of every remainder monomial in
  
  \[
  N\le nd<N^2;
  \]
- rejection of the mutation omitting the hyperbola overlap correction.

Run:

```bash
python experiments/X-26204-critical-hyperbola-bank/verify.py
```

Expected verdict:

```text
PASS_EXACT_CRITICAL_HYPERBOLA_BANK_SPLIT
```

Proof-object SHA-256, computed before inserting the digest field:

```text
c8b457f5f9e6b398826d7ae17e57340b1460bd444f578b6183184a1a56dcf970
```

## Scope

The checker certifies finite coefficient coverage and strict support only. It does not certify a physical estimate for the lower-scale remainder, a uniform recurrence, or RH.
