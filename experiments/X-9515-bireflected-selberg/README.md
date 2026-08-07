# X-9515 — Two-frequency reflected Selberg and terminal-geometry review regression

This standard-library experiment supports the adversarial review of PR #226 at
frozen head

```text
63a4d7c0f482a57893db420e64b22f6a605c72e6
```

It verifies the exact algebraic repair `L-9518` and records a terminal-scale
mutation against the proposed absolute endpoint-coordinate bound in `L-9517`.

## Run

```bash
python3 verify.py
```

## Exact algebra checked

The verifier uses two independent Laurent-variable blocks, one for the twist
`n^(-it)` and one for `n^(is)`. A completely additive integer derivation
replaces `log n`.

Coefficientwise through `n=24`, it checks:

1. the generalized Selberg identity
   ```text
   b*(a ell^2)=Lambda_A ell+Lambda_A*Lambda_A;
   ```
2. the correct sign
   ```text
   Lambda_A=b*(a ell),
   ```
   and rejection of the mutated negative sign;
3. the product logarithmic derivative
   ```text
   Lambda_(t,-s)=Lambda_t+Lambda_(-s);
   ```
4. the independent-frequency reflected identity
   ```text
   C_(t,-s)-C_t-C_(-s)=2 Lambda_t*Lambda_(-s).
   ```

The diagonal specialization `s=t` is the Hermitian identity of `L-9516`. The
independent-frequency form is the algebra needed by the localized normal-block
formula in `L-9518`.

## Terminal geometry mutation

Fix

```text
delta=1/5,
V=X^(1/K),
j_K=floor(K/5)-1.
```

The verifier records the family with `j_K` short residual/divisor coordinates,
each at exponent `1/K`, and one long coordinate at the complementary exponent.
For

```text
K=20,30,50,100,200
```

the free-coordinate counts are

```text
3,5,9,19,39.
```

The short product remains strictly below the terminal reserve while the number
of short coordinates grows linearly with `K`.

This does not prove that exact signed recombination cannot cancel those faces.
It proves that an absolute bound independent of `K` does not follow merely from
terminal scale geometry, spline degree, or the high-order null moments.

## Retained result

```text
verdict
PASS_EXACT_BIREFLECTED_IDENTITY_AND_TERMINAL_GEOMETRY_MUTATION

proof-object SHA-256
c194c7cdcc5a13cf69baaed6cdf798666656b925ddfd07f614106c7a1a591165
```

## Proof boundary

This regression proves only exact finite Laurent algebra and rational exponent
geometry. It does not prove:

- the double-Fourier analytic interchange in `L-9518`;
- cancellation of growing-dimensional terminal faces;
- any packet-specific Selberg inequality;
- the balanced Type-II theorem;
- RH.
