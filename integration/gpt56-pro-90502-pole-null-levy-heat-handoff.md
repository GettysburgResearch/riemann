# Integration handoff — pole-null Lévy/heat continuation

Proposed base: the Fredholm-Pontryagin branch stacked on PR #365  
Status: proposed exact theorem packet; finite replay; RH unproved

## Import order

1. `L-90505-cauchy-sobolev-trace-class-completion.md`
2. `L-90506-pole-cardinals-and-exact-index-one-shift.md`
3. `L-90507-archimedean-levy-form-and-entire-heat-criterion.md`
4. `T-90502-pole-null-fredholm-heat-rh-equivalence.md`
5. external proof note and report
6. `X-90502-pole-null-heat` replay

## Interaction with prior branches

- PR #365 supplies the super-Gaussian Xi-cardinals used in the lower-index proof.
- PR #366's confluent jets remain finite-coordinate diagnostics; the global pole-null cardinal modification bypasses finite cluster conditioning for a fixed actual pair.
- `L-90501` remains valid as a smooth abstract completion. `L-90505` is an alternative explicit-kernel completion, not a replacement.
- `T-90501` remains valid. `T-90502` removes the pole term and adds an entire heat criterion.

## Exact new frontier

```text
prove n_-(Q)<=1,
```

or equivalently

```text
prove the pole-null heat trace never becomes positive.
```

The verifier is finite algebra/numerical identity checking only. Independent analytic review is required before promotion.
