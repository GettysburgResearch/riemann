# Independent review: sixth-power stratified inverse

Reviewer: descent_synthesis, separate from authorship. Status: the stated deduction is mathematically supported, conditional on the exact mixed-label completed estimate (1.2) and the pinned theta/sieve inputs. This review does not independently establish that mixed-label input.

Reviewed source: SIXTH_POWER_STRATIFIED_INVERSE.md, SHA-256 `f98cc20e361ebb99af7dbd4b5ffef83a8a55ca11c4d3f24da238bc24be4cb2e9`.

## Exact statements checked

1. The sixth-power-free sieve (2.1) follows by setting V=1 in the two valuation-block bounds of PR #913. The ordinary-character alternative then has L+P0^2, and the exact monomial minimum absorbs the remaining P0 L/M term into (UL)^(2/3). Units, fixed bad-prime valuation patterns and nonunit masks are retained.
2. The decomposition k=u v^6 k0 is unique without (v,k0)=1. The identity chi_n(v^6)=1_((n,v)=1) holds with literal zeros. The new exclusion satisfies Q_v<=Q Nv even when v meets f, q or S.
3. R_v=min(K D^(1/3),R Nv) is a legitimate separate cutoff on each disjoint physical row stratum. At the support cap the long inverse is empty exactly. On every remaining stratum R_v=R Nv, which is needed for the negative tail powers. No invalid lower bound on a capped R_v is used.
4. In (4.1), substituting B_t=D/(Nt)^3 yields eta=9/2-3 beta, D^(beta-1/2), and the R_v^eta cost. The mixed completed family must retain its outer t mask. The raw long coefficient norm is subpower, and the sixth-power-free sieve removes the previous U_v^(1/6) copy term because those copies have already been frozen into the column mask.
5. The short v powers are -6, -13/2-3 beta and -17/3. The uncapped long powers are -6,-3,-6. All ideal sums converge. Physical row strata have disjoint supports, so adding squared norms is justified; this step is not Minkowski over v.
6. The optimization is exact: R1 balances the third increasing term with D^2 R^-3; R2 balances the second. H^2 FQ<=D^((5-2 beta)/2) ensures both cutoffs are at least one, H<=D, and the mixed tail is smaller than D^2 R^-3 at the chosen minimum. The phase transition H^(8 beta) F^(4 beta) Q^(5+2 beta)=D^(5-2 beta) is algebraically correct.
7. At beta=11/12 the two exponents are D^(6/5)H^(4/5)F^(2/5)Q^(1/5) and D H^(24/19)(FQ)^(12/19). The all-row f=q=1 benchmark at H=D^(1/2) is 31/19; its savings are 7/228 versus 379/228 and 103/228 versus 25/12. The range H<=D^(19/24) is an arithmetic row range.

## Exposition and input boundary

Near the physical support cap, B_t can lie in a fixed interval below one. The reviewed source explicitly includes the bounded nonempty-scale extension after its cap discussion: it rescales the fixed test at scale one, with uniformly bounded normalization and smooth seminorms on that compact interval. This covers the small-scale issue without changing an exponent or introducing a new analytic premise.

The positive estimate (1.2) is load-bearing. An assertion that moving exclusions are norm contractions would not justify this proof; the local q^6 and f^4 adapter must separately prove (1.2) with its overlaps, branch factors, masks and source tails. Once that input is supplied, this review finds no further analytic or algebraic gap in the stratified inversion argument.

No conclusion about the full Mobius fourth moment, 17/24, generalized hierarchy, or RH is approved by this review. No numerical experiments or Lean proof are being substituted for the argument.
