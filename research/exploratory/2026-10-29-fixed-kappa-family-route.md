# Fixed finite-character ceiling and an infinite-type target

**Status:** Conditional route; the zero-free conclusion below is *not established*. The limiting logic and parameter algebra are exact, subject to the explicit analytic imports. This note corrects the mistaken suggestion that one must impose `delta <= kappa` in the relevant short-witness row count.

**Sources:** Hu, [*A seven-eighths zero-free half-plane for unitary Weil L-functions*](https://hexagonmath.org/2610.00216v1), Theorem 4.2, §7, and family definition (2.2); Xu–Sang, [arXiv:2610.15291v2](https://arxiv.org/abs/2610.15291v2), Proposition 4.1; Liu, [arXiv:2610.26835v1](https://arxiv.org/abs/2610.26835v1), Proposition 14.3 and Lemmas 14.9–14.10. None is fully independently reviewed here.

## Exact conditional implication

Let `B_f=0.874886647039964...` be Liu's exact quartic root and set `kappa_f=2B_f-1`. For a field `K` containing `mu_12` and a fixed infinity-type family `F_omega` as in Hu (2.2), suppose all four of the following:

1. Every finite-order Hecke L-function over `K` is zero-free for `Re(s)>B_f`, with principal poles permitted.
2. Hu's paired fourth-moment theorem extends to `kappa=kappa_f`, including its finite-order zero-free premise, all fixed-type coefficient and exceptional-row conditions, original masks, and source-uniform mesh and height quantifiers.
3. The Xu–Sang/Liu detected-row count and Liu's amplified numerator estimate apply to Hu's same fixed-type physical probe at `kappa_f`, for all required detector bins, including those with `delta>kappa_f`, with their prime-slot masks and uniformity intact.
4. Liu's variable-geometry low/high contour and continuation proposition is valid for that same fixed-type probe, with all principal and nonprincipal terms, common target-uniform savings, errors and pole conventions preserved. In particular, each parameter triple admissible in Liu's Lemma 14.10 gives the corresponding bound for the full family `F_omega`.

Under these hypotheses, every member of `F_omega` is nonzero on `Re(s)>B_f`, away from its poles. For arbitrary unitary Hecke characters over an arbitrary number field, an additional fully justified abelian descent and shifted-pole argument would be required.

**Derivation.** Assume the family has a zero with real part `beta>B_f`; equivalently its zero supremum exceeds `B_f`. Liu Lemmas 14.9–14.10 assert that at `kappa_f`, the limiting tangent length `ell_*(kappa_f)` satisfies `B(ell_*)=(1+kappa_f)/2=B_f`, and that every sufficiently close `ell<ell_*` gives a strictly admissible triple with the same `kappa_f`. Because `B(ell)=11/12-ell/4` is continuous and decreases with `ell`, choose such an `ell` with `B_f < B(ell) < beta`. The common-probe continuation in hypothesis 4 then bounds the entire family by `B(ell)`, contradicting the zero at `beta`. Equivalently take the family supremum and choose a zero sufficiently close to it. The limit uses one strict admissible triple per contradiction, not an assertion that the boundary triple itself has a strict saving.

Hypothesis 1 licenses the finite-character moment at the fixed `kappa_f` because `(1+kappa_f)/2=B_f`. It does not require the infinite-type family already to be zero-free there. This distinction is exactly why fixed `kappa` may be useful.

## Why `delta > kappa` is not by itself an obstruction

For a detector bin set `delta=2a-1` and let `alpha=5/6`. Under Hu's claimed initial `7/8` family ceiling, `delta<=3/4<alpha` for a genuine witness. Xu–Sang Proposition 4.1 proves its short/long witness balance for the entire rectangle `0<delta<=alpha`, `13/18<=kappa<=1`, without imposing `delta<=kappa`: the plain-moment prime capacity is `(1-2m)/(6kappa)`, while `delta` is the spike exponent. The crossing and the positivity of the denominator use `1/(3kappa)<=6/13` and `delta<=alpha`. Hu Proposition 7.2 displays `delta<=kappa` only in its separate `alpha<=delta` branch, which is not relevant in this starting range. This observation does **not** prove that Xu–Sang's count has been transferred to Hu's infinite-type coefficients; it only removes an incorrectly inferred scalar restriction.

## Remaining mathematical work

The [fixed-type moment audit](../2026-10-29-hu-kappa-trace/README.md) identifies no extra displayed parameter obstruction, but its source induction and local tables remain imported. The [conditional low-side calculation](../2026-10-28-hu-variable-low/README.md) does not supply hypothesis 4's high-side contour. The principal missing theorem is a source-faithful high-side statement at variable geometry that simultaneously controls both target-dependent denominators and local errors while retaining the physical finite-order numerator and common slot profiles. Neither the finite-order theorem nor the scalar tangent certificate alone supplies that estimate.

**What was checked:** The finite- versus infinite-character premise distinction; Xu–Sang Proposition 4.1's algebraic range; Liu's tangent and fixed-point statements; and the limiting contradiction above. The imported analytic hypotheses, source proofs and formalizations were not independently proved or replayed.
