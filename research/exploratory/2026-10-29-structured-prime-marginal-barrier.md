# A marginal-moment barrier for the blocking detector bin

**Status:** Elementary information-theoretic obstruction to one *use* of a proposed moment input. No statement is made that the source moment applies to the physical selected slots, that the model below is realizable by sextic characters, or that a weighted/mixed arithmetic theorem cannot exist.

**Sources and scope:** Xu–Sang, [*A lower bound for the sextic large sieve and structured prime moments*, arXiv:2610.17675v2](https://arxiv.org/abs/2610.17675v2), Theorem 1.2 and Proposition 7.2, claim a structured unnormalized second moment with principal exponent `kappa_6=(37-10 sqrt(6))/6`; the source has coefficient, scale, smoothness and proof dependencies. The blocking bin and existing count are documented in [the return-gate note](../2026-10-29-arvi-return/pr93-joint-gate.md). Neither source is independently established here.

## Exact comparison

Grant, for this comparison only, the best-case matching in which a physical selected product `Q(u)` has row scale `U`, its total column scale also equals `U`, all coefficient, mask, smoothness and squarefree hypotheses apply, and the second moment satisfies

    sum_(u in row dyad) |Q(u)|^2 << U^(rho+epsilon),
    rho = kappa_6-1 = (31-10 sqrt(6))/6.

The subtraction of 1 is the square of central normalization by the square root of the total column scale. The source's additional discrepancy term can only make this comparison weaker; it has not been discarded in a claimed application.

At the identified bin the guaranteed squared response is `|Q(u)|^2 >= U^(sigma-o(1))` with `sigma=223/500`. Markov's inequality alone yields

    #selected << U^(rho-sigma+epsilon),
    rho-sigma = 7081/1500-5 sqrt(6)/3
              = 0.638183762028... .

The existing asserted count at the same point is

    R = 137478360780643/225606975000000
      = 0.609371056815... .

Thus the structured pure moment is weaker there by

    rho-sigma-R = 0.028812705212... > 0.

The positive gap can be checked exactly from the displayed rational expressions and `sqrt(6)`; no fitted quantity is used. This is before losses. If the actual physical column length is not the row length, the source's balanced theorem cannot simply be applied without an additional unbalanced/scale adapter, so the displayed comparison is deliberately favorable to the proposed branch.

## Why a weight alone cannot pay the gap

The following abstract example shows the limit of *marginal information*. Let `U` grow, let an event `E` contain `floor(U^R)` abstract rows, and set `|Q(u)|^2=U^sigma` on `E` and zero outside it. Then

    sum |Q(u)|^2 <= U^(R+sigma) <= U^rho

for large U, while `#E` has exponent `R`. On the same event one may put any other nonnegative witness factors exactly at their prescribed lower thresholds, setting them to zero elsewhere, whenever the existing scalar moment budgets are compatible with `U^R` such rows. Thus knowing the pure `Q` moment and those marginal inequalities alone does not rule out their simultaneous concentration on the existing-sized event. Restricting the `Q` sum by a weight between zero and one or applying Markov to it supplies no additional factor; any conclusion excluding this model needs an additional inequality relating the **actual** `Q` to the witness or selected rows.

This is not a counterexample within the sextic-character family and does not rule out a new mixed moment, an amplifier with extra arithmetic structure, a conditional row-restricted estimate, or a different profile. It says those are genuinely new inputs rather than consequences of the cited pure second moment by an unspecified Hölder or positive-weight step. A candidate mixed estimate must preserve the source's physical prime character, slot normalizations, all masks and row scales, and should be evaluated against the `0.0288127...` exponent gap before deployment.

**What was checked:** Exact algebra and symbolic evaluation of the two exponents; the abstract co-concentration example. No source proof, character realization, mixed moment, physical scale adapter, or zero-free theorem was proved here.
