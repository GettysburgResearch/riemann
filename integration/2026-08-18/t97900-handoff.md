# T-97900 handoff — post-LAPBR root localization

```text
base PR:       #594
base SHA:      ef76157a516c520a0f829ea4ee346c62759743ed
head branch:   agent/logarithmic-cube-subpower-corridor
namespace:     97900--97905
RH status:     unproved
```

## Controlling results

1. `L-97903`: the complete native cube through
   `(log X)^2 log log X` is positive.
2. `L-97901`: every top history has an exact completion into a fully completed
   state with finitely omitted Euler factors.
3. `L-97904`: owners above `exp((log log X)^4)` contribute only
   `O((loglog X)^-2)`.
4. `T-97901`: the unfiltered root problem is exactly the signed corridor
   `QPCB67` between those two cutoffs.
5. `L-97905`: one extra factor-four difference cancels the base constant and
   permits a positive cube through `X^(1/(loglog X)^2)`.
6. `T-97902`: every filtered interior top history is PNT-small; the remaining
   theorem `FABP67` is one centered activation-boundary sign.

## Review priorities

- Check the activated divisor split in `L-97903`; the primorial itself is not
  assumed below `X`.
- Check that `L-97901` is source-exact, while the inverse omitted-factor series
  in `L-97902` is analytic bookkeeping only.
- Check the upper-bound sieve in `L-97904` on the short multiplicative boundary.
- Check normalization of the additional factor-four filter and its Mellin
  multiplier.
- Do not infer the sign of the centered boundary from its leading asymptotic
  cancellation.

## Next mathematical attack

The strongest explicit target is `FABP67`. Expand terminal values by their
finite native coefficient dictionaries, interchange the boundary product and
terminal sums, and seek a Buchstab/Type-II coboundary whose main rough density
cancels exactly. The alternate target `QPCB67` should be retained as an
unfiltered audit of any proposed boundary mechanism.