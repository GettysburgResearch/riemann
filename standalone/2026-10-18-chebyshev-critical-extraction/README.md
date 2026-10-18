# Logarithmic-cost critical extraction

**PROPOSED component mathematics. No RH proof or critical arithmetic upper
bound. Independent mathematical review required.**

The previous #980 finite-translation compiler has raw coefficient mass
`exp(O(sqrt(log X)))` and uses shifts that small. This packet replaces it,
for the SAME complete arithmetic translations and exact shifted-pole
continua, by a Chebyshev-root formula with:

- `O_A(log X)` strictly positive real-shift samples for error `O_A(X^-A)`,
  for any fixed A>0;
- absolute mass `O(log log X)` on the centered divided samples;
- raw-source coefficient mass `O_A(log^2 X)` and minimum shift bounded
  below by a constant times `1/log^2 X`;
- an exact lower bound showing the raw coefficient cost is within a fixed
  factor of optimal for the stated polynomial-exact positive-node task.

The sample count INCREASES relative to #980. This is a coefficient and
analytic-error theorem, not a runtime or relative floating-point stability
claim. The translated coefficients are explicitly deformed Mobius, not
unchanged native coefficients. All ideal and continuum tails remain.

A second result gives one fixed-shift mean `E_H(T)` and proves

`E_P(T) <= C log(3T) E_H(T)+C`,

where `E_P` is the complete Gaussian prime-discrepancy energy at the
square-root scale. A subpower bound for `E_H` is equivalent to field RH.
It is NOT proved here. An even simpler fixed interval `[H/2,H]` has the same RH-equivalent
subpower criterion by a direct Hilbert-valued Mellin argument. A prescribed
off-line zero forces an explicit positive power-growth lower bound there; this is not an average that can discard the target
as an exceptional family member.

Read [PROOF.md](PROOF.md), then [FIXED_SHIFT_TARGET.md](FIXED_SHIFT_TARGET.md).
The latter records the failed direct application of #986/#987 rather than
silently treating their Hecke family as the real-shift family.

[VALIDATION.md](VALIDATION.md) records what was executed and what was not.
[SOURCES.md](SOURCES.md) gives source identities and attribution. Chebyshev
interpolation, Markov extremality, the reproducing kernel, Jordan quotients,
and the Gaussian RH criterion are classical. No global novelty claim is
made for those methods. The claimed contribution is this full-source,
growing-order, coefficient-cost replacement and fixed-measure adapter.

Run the standard-library exact regression and corruption replay:

```sh
python replay.py
```

No whole-repository validator, Lean build, independent referee or remote CI
result is claimed. No inherited file or integrated scientific status is edited.
