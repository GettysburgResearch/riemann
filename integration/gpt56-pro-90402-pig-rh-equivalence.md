# Integration handoff — PIG is an RH-equivalent filtered Chebyshev mean square

Branch: `research/gpt56-pro/90402-pig-rh-equivalence`  
Base: PR #357 branch `research/gpt56-sol/90300-claude-inertia-q4`  
Status: proposed mathematics; independent review required; RH unproved

## Load-bearing files

```text
claims/theorems/T-90404-positive-innovation-gate-is-rh-equivalent.md
claims/lemmas/L-90405-central-q4-innovation-multiplier-is-zero-safe.md
experiments/X-90402-pig-equivalence/
reports/gpt56-pro/2026-08-10-q4-pig-is-rh-equivalent.md
```

## Contribution

- Expands the compact innovation into an exact finite difference of `psi(x)-x`.
- Proves the delayed `b4` gauge is logarithmic.
- Uses the standard von Koch RH consequence to prove pointwise `|I_circ|^2/n << log^4 n`, hence PIG.
- Combines with `T-90302` to identify the surviving gate as RH-equivalent.
- Proves the central spectral multiplier `(4^z-4)(1-2^(1-z))` has no zero in the open critical strip and the delayed gauge cannot cancel the leading zeta pole.

## Review gate

1. Recheck the sign and constant `-4 log 4` in the aligned carry formula.
2. Recheck `1*b4=epsilon-3 sum_(r>=1) delta_(4^r)` from the Euler multiplier.
3. Recheck the scaling identity for `delta4*b4`.
4. Verify the use and uniformity of the von Koch bound.
5. Audit that the block measure assumed by `T-90302` is positive with bounded total mass.
6. Treat `PIG=>RH` only at the exact status of `T-90302` and its pole-energy dependency.

## Honest consequence

This branch narrows the full-RH frontier but does not make it easier by declaration: after the source/state/inertia repairs, the positive innovation gate is itself an RH-equivalent theorem. A further proof must introduce new information about the positive product block.
