# X-90201 — Liouville pointwise extremality and the Boolean descendant hierarchy

This package independently replays the finite identities accompanying
`L-90201` and `T-90201`.

## Run

```bash
python3 verify.py
```

Dependency:

```text
mpmath
```

A successful run prints

```text
PASS_X_90201_LIOUVILLE_BERNSTEIN_RIGIDITY
```

and rewrites

```text
results/verification.json
```

## Assurance layers

### 1. Local generalized-von-Mangoldt identity

For every `2 <= n <= 240`, all vertex signs on the distinct prime divisors are
enumerated. The direct divisor convolution

```text
sum_(d|n, d squarefree) f(d) log(n/d)
```

is checked against the manifestly nonnegative Bernstein formula in
`L-90201.3`. The test is repeated on a five-point real grid in each prime
coordinate for all cases with at most three distinct primes.

The retained run checks 996 vertex cases and 2,550 interior-cube cases at 70
decimal digits.

### 2. Exact Boolean polynomial algebra

For an arbitrary rational kernel supported through `K=30`, `Fraction` checks:

1. the complete Boolean Bernstein expansion at all `2^10=1,024` class
   vertices;
2. every mixed coefficient `B_c(a)`;
3. the semigroup/primitive identity
   ```text
   B_c(a)/2^omega(a) = sum_(rad(r)|a) P_c(ar);
   ```
4. a mutation in which prime-power semigroup descendants are deleted.

This layer is exact and deliberately uses a kernel with mixed signs, so it does
not assume the conclusion.

### 3. Actual GFEP descendant identities

For four finite first-entrance networks, the path values `G_p(m)` are computed
with `Fraction`. Logarithmic coefficients are evaluated at 70 decimal digits.
The script checks:

1. `P_c(q) = q^(-1/2) Sigma_(X/q,n)(p)` at 109 descendants;
2. every mixed Bernstein coefficient against its complete semigroup of scaled
   descendants;
3. the empty-coefficient renewal `c(1)=sum_q P_c(q)`;
4. exhaustive class minima for the four small prime cubes.

The largest retained discrepancy is below `2e-70`.

### 4. Large-point reconnaissance

A separate double-precision layer evaluates the binding bottom exits at

```text
(2000,20), (3000,25), (4000,15), (10000,20).
```

No negative nonempty Bernstein coefficient is found. This layer is finite
reconnaissance only; the exact theorem is the symbolic descendant identity.

### 5. Ramp extremality

At `X=30` and `X=60`, every active prime-sign assignment is enumerated. The
script checks:

1. divisor switching between the transported ramp and the generalized
   von-Mangoldt form;
2. Liouville as the exact active-prime minimizer;
3. the explicit coercivity lower bound from the `2p` coordinates.

## Mutation-sensitive points

The verifier fails if one:

- changes the factor `2^omega(a)` in the Boolean expansion;
- omits the coprimality condition in the direct mixed derivative;
- drops prime-power members of the semigroup `S(a)`;
- reverses the endpoint scaling `q^(-1/2)`;
- deletes the terminal interval in the first-entrance coefficient;
- changes either term in the local generalized-von-Mangoldt Bernstein formula;
- replaces the empty coefficient by a nonempty descendant.

## Scope

The package authenticates exact finite algebra and the declared numerical
reconnaissance. It does **not** prove the empty GFEP coefficient nonnegative at
unbounded depth, producer positivity, Form A, or RH.

`SHA256SUMS` binds this README, the verifier, and the retained JSON result.
