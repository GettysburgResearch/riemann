# Integration handoff — Chebyshev–Christoffel Hankel and rational-safe-pole attack

## Freeze

```text
base PR:      #395
base SHA:     7106b3b2e06b8193861851890db12767a03b5df4
branch:       research/gpt56-pro/395-chebyshev-hankel-amplifier
scientific:   RH remains unproved
```

## Review order

1. `claims/lemmas/L-91010-catalan-hankel-is-chebyshev-identity.md`
2. `claims/theorems/T-91005-growing-full-hankel-positivity-at-chebyshev-edge.md`
3. `claims/lemmas/L-91011-offline-pair-has-optimal-christoffel-hankel-amplifier.md`
4. `claims/refutations/R-91004-subcritical-polynomial-hankel-tests-are-sharply-blind.md`
5. `claims/lemmas/L-91012-one-safe-pole-rational-chebyshev-accelerator.md`
6. `claims/lemmas/L-91013-safe-halfplane-blaschke-amplification-is-sharp.md`
7. `experiments/X-91010-chebyshev-hankel-amplifier/verify.py`
8. retained JSON and checksum ledger
9. session report
10. parent PRs #395, #394, #393

## Importable exact core

```text
shifted Chebyshev-U diagonalization of beta(3/2,3/2) moments;
exact Christoffel kernel and extremizer;
one matching pair as a negative rank-one Hankel perturbation;
closed depth-dependent Christoffel growth law;
one-safe-pole rational Chebyshev construction;
finite derivative evaluation at one absolutely convergent Euler sample;
safe-half-plane Blaschke Green-function upper bound;
rate optimality of the repeated boundary pole.
```

## Proposed analytic theorem requiring review

```text
parabolic integrated remainder bound;
Chebyshev-preconditioned operator estimate
  ||H_n^sharp-ell_x I|| <= C n^7 9^n;
full Hankel positivity through
  n <= (1/(2 log 3)-epsilon) log log |x|.
```

The proof uses the full parabolic direct-Euler domain, not a circular contour. Reviewers should check:

1. the orientation and decay in the parabolic Cauchy formula;
2. uniform treatment of `v approximately plus or minus x` in the moving gamma sample;
3. the integrated `delta^-4` remainder estimate;
4. complex-coefficient handling through `p^sharp`;
5. uniformity when `n` grows like `log log |x|`.

## Lifecycle recommendations

- Keep every theorem labeled `PROPOSED` until independent analytic review.
- The exact orthogonal-polynomial and rational identities may be imported separately from the growing-matrix theorem.
- Preserve `R-91004` beside `T-91005`: the same constant that proves subcritical positivity is the first possible deepest-pair detection constant.
- Do not describe rational acceleration as a proof. The conditioning loss as the safe pole approaches `r=1/2` is still the RH-bearing gate.
- Do not transfer Anthropic Lean status to any file in this stack.

## Next conclusion-producing target

The strongest next theorem is a uniform sign theorem for the rational quadratic forms

\[
 Q_x[R_{n,b}]
\]

in a coupled boundary regime

```text
b -> 4/3 from above,
n -> infinity,
|x| -> infinity.
```

Equivalent coordinates:

```text
safe-line derivative jets at r_b -> 1/2+;
rational Pick matrices with coalescing nodes;
Blaschke products approaching the Euler boundary;
source-ordered prime sums after Catalan preconditioning.
```

The safe-inner exponent is now known to be optimal, so any improvement must come from arithmetic sign, not from a more elaborate analytic amplifier.
