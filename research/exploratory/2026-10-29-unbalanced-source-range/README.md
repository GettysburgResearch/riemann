# An unconditional long-source range from row count and pair conductors

**Status:** A derived character-operator estimate under standard fixed-field Kummer/Hecke identification and analytic continuation inputs described in the [four-cycle note](../2026-10-29-complete-source-four-cycle/README.md). It is independent of amplitude selection once a row count is supplied. It does not establish the balanced long-source seed, its compatibility with PR94 detector bins, or a zero-free region.

Let F be any finite set of M sixth-power-free Eisenstein element rows of norm at most Y and S any finite set of source ideals of norm at most L. With the original zero-extended sextic characters and all bad-prime source factors,

    selectedNorm(F,S) ≪_ε [L+MY](LY)^ε.                      (1)

The source length may be any L≥1. Indeed the [pair-conductor inequality](../2026-10-29-complete-source-four-cycle/README.md) gives `L + max_u Σ_v sqrt(Q(u,v))`, with bounded good-valuation blocks. For distinct blocks, Q divides the radical of the product of the row ideals, so `Q(u,v)≤Nu Nv≤Y²`; there are at most M terms. The remaining bounded-size identical-good-valuation blocks cost O(L). This proves (1).

If the source scales satisfy a fixed polynomial cap `L,Y≤Z^P`, and for every small loss the row count has the form `M≪Z^ε Y^α` uniformly in the required detector choices, then (1) yields the desired `Z^ε L` long-source norm whenever

    L ≥ Y^(1+α).                                              (2)

The standard unrestricted sixth-order large sieve has the four terms

    L + Y L^(1/6) + Y^(5/6)L^(1/3) + Y^(1/3)L^(5/6),       (3)

up to arbitrary small losses. Writing `L=Y^t` with `1≤t≤2`, its largest non-L exponent is `1/3+5t/6`. The pair-conductor bound replaces this by `1+α` when that is smaller. Thus the hybrid minimum improves the displayed unrestricted bound for

    t > 4/5 + 6α/5,

and reaches the desired exponent t for `t≥1+α`. At the PR94 bottleneck count value `α=137478360780643/225606975000000≈0.6093710568`, these thresholds are approximately `1.5312452682` and `1.6093710568`. The latter uses that specific count only **if** the chosen physical selected rows, scale, masks, and quantifiers match its source theorem. The selection of the tiny losses and mesh must be made in the order required by that source; the fixed polynomial cap alone does not establish that quantifier matching. With the separate broad-slot count `α=7/6−223/500=1081/1500≈0.720667`, the corresponding thresholds are about 1.6648 and 1.720667, subject to that count's stated source hypotheses.

This does not cover `L≈Y`, where (1) contributes `MY` and (3) contributes `Y^(7/6)`. Nor does it supply the source-uniform selection, mesh, or detector-zero transport needed for the global return. It is a rigorous range improvement over the displayed unrestricted inequality, not a claim to beat all known large sieves or a new asymptotic for the actual zero-free boundary.

**Independent review:** Families verified the pair-conductor implication, source-factor masks and the exponent crossovers, conditional on the named Kummer/Hecke inputs. The source-to-detector quantifier matching remains open.
