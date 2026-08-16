# Hostile review specification

## Freeze

Review the successor commit only against parent

```text
6cc0da2fa5711017e260ebdcea4ba8c22e453288
```

and verify that PR #498 itself remains unchanged.

## Reconstruction obligations

1. Recompute the Bernoulli norm, cubic antiderivative, endpoint predecessor,
   Mellin multiplier, and open-strip noncancellation.
2. Verify the exact Laurent identity for `P`, its positivity on the real line,
   and its strict positivity at every depth `0<|y|<1/2`.
3. Derive the prime-log shift operator from the Fourier convention; do not
   accept a sign-swapped translation.
4. Conjugate by `e^(u/2)` and verify
   `(I-T_L)(4I-T_-L)` coefficient by coefficient.
5. Reconstruct the Chebyshev shell lemma and the high-order Hermite derivative
   estimate, including the growing-order constants.
6. Check the gamma lower bound uniformly when `m=o(q)` and retain the
   `exp(Cm)` negative-density error.
7. Reconstruct the monotone-envelope quantifier in the arbitrary-Delta theorem.
8. Reprove variable-order terminal dominance with a bounded-window / Gaussian
   tail split.
9. Reconstruct the maximum-modulus boundary and ensure it is not stated as a
   no-go for genuinely signed arithmetic.
10. Verify the positive generalized-prime annulus and its real `s=1` pole.

## Automatic rejection conditions

Reject any claimed closure that uses:

```text
CPBD as an estimate;
psi(x)=x+O(sqrt(x)polylog x);
a macroscopic RH-strength Selberg integral;
large-sieve averaging to decide one fixed low mode;
block count as an upper bound;
zero density to eliminate one prescribed carrier;
a fixed leading-constant gain inferred only from the scalar filter.
```

## Computational scope

The replay authenticates finite identities, exact shift moments, endpoint
projections, finite diagnostics, and hostile mutations. It does not authenticate
Chebyshev/Stirling, terminal-pair theory, asymptotic derivative bounds,
coefficient variance, or RH.
