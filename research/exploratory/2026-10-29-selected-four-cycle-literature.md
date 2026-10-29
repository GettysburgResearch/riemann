# Source scan for prime-selected fourth cycles

**Status:** Targeted scan, not an exhaustive literature review or proof of the proposed four-cycle bound. See [the cycle reduction](2026-10-29-complete-source-four-cycle/README.md) for its exact row, mask and complete-source conventions. No source below was independently verified in full.

The desired long-source conclusion at balance is an operator inequality for **every** source coefficient vector, on rows passing a common prime-amplitude test. A bound for a single structured source vector, a count of selected rows, or an average absolute pair correlation does not alone supply it. No directly matching theorem was found in this search.

## Weighted cubic Gram with a prime-amplifier block

[rStation Paper 55 v2, Theorem 4 and Proposition 7](https://rstation.ai/problems/riemann_hypothesis/papers/55) is a relatively close recent source. It works with natural cubic Eisenstein rows and common smooth profiles. Theorem 4 permits bounded coefficient blocks supported on ideals with only sufficiently small prime divisors, while Proposition 7 couples such blocks to an unrestricted **divisor-bounded** cofactor using a weighted Gram estimate and a cubic Burgess pair-correlation input. Its (14.6) states, in the notation there,

```text
T <= B^epsilon [ R V^(1/j) W^(1−1/j) + C^(1/j) W ],
W = P+P^(2/3) V^(1/3) S^(2/3),
C = min(P, P^b_m R^(j/m)), b_m=(m−1)(2m−1)/(2m²),
```

with fixed integers `j,m>=2`, a sufficiently small smoothness mesh, and the paper's definitions of `V,S,R`; profiles and masks must be common and nonprincipal rows are retained. For a single short prime block `S=Y^w`, fixed unit ordinary factors, row cutoff `P=Y`, and unrestricted cofactor length `R=Y`, one has `V=Y^w` and `W<<Y` for `w<=1/3`. Here `C=Y` for every allowed `j,m`, because `b_m+j/m>1`. Thus the displayed source bound is

```text
T << Y^[max(2−(1−w)/j, 1+1/j)+epsilon].
```

Dividing by the prime selection threshold `Y^(sigma w)` gives, at `sigma=223/500`, an exponent at least `3/2+(1/2−sigma)w>1` for every `j>=2`. The resulting estimate does **not** reach the required `O(Y^(1+epsilon))`. This calculation uses the source's bound, not a lower bound on the actual selected norm. Further, the source is cubic and its cofactor coefficients are divisor-bounded, not a uniform arbitrary unit `l²` vector; it does not assert the sextic selected-row theorem.

The same paper's Theorem 2 bounds a product of two full ordinary sums and short prime blocks under `n1+n2+3z<=1`. At a balanced ordinary source of length Y (`n1=1`), that capacity leaves no positive prime length. Its unmarked Theorem 1 has longer full-sum ranges, but requires the prescribed ordinary coefficients and does not grant arbitrary source vectors. The paper itself says the complementary unrestricted inverse remainder is unestimated.

## Pair Gram and structured-prime estimates

[OpenAI, *An unconditional first moment for cubic Gauss sums*, Lemma 4.3](https://github.com/openai/math/blob/main/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/paper.pdf) states for squarefree cubic rows of norm `~P` and a compactly supported smooth source of length `Z` that, uniformly in a fixed row,

```text
sum_(p' != p) |T_(p,p')|² << (PZ)^epsilon Z [P+(P³/Z)^(2/3)].
```

A subset of the available p' is allowed. At `P=Z=Y`, this is `O(Y^(7/3+epsilon))` per row. It is an absolute **pair** second moment, not a signed four-cycle estimate and not an amplitude-selected operator theorem. In particular, summing it over M selected rows and using `Tr E⁴<=(Tr E²)²` yields only `O(M²Y^(14/3+epsilon))` for the cubic analogue, far larger than the softened `O(Y^(4+epsilon)+Y² M³)` target at `M=Y^0.6094`. The cited source addresses cubic squarefree rows, not the complete sextic row family.

[Xu–Sang v2, Theorem 1.2 and Proposition 7.2](https://arxiv.org/abs/2610.17675v2) estimates fixed smooth prime sums and fixed bounded rough prime convolutions on sextic rows, with polynomial dependence on the specified profiles and the source's cited moment/detector inputs. At balance its second-moment exponent is `(37−10sqrt(6))/6=2.08418...`, with the additional repeated-prime error `Y^(13/6−c+epsilon)` for prime factors at least `Y^c`. This is a genuine structured-coefficient saving but is not uniform over arbitrary source vectors and does not control selected four-cycles.

## Other relevant techniques and limits

[Blomer–Humphries–Khan–Milinovich, Theorem 4](https://arxiv.org/abs/1902.07042) proves a twisted fourth moment of central Dirichlet L-values for the full character family modulo a rational prime, with arbitrary squarefree-supported amplifier coefficients of length at most `q^(1/4)`. Spectral reciprocity is its new analytic mechanism. Its fixed-modulus rational-character family and central L-value source differ from the moving-conductor sextic Hecke matrix and arbitrary source vector, so the theorem cannot simply be substituted here.

[David–de Faveri–Dunn–Stucky](https://arxiv.org/abs/2410.03048v3) obtain a power-saving mollified second moment for a squarefree cubic Hecke family using metaplectic spectral analysis. The coefficients are a specific mollifier and the statistic is an average central L-value, so this does not directly supply a prime-selected operator bound. Their method is a plausible place to look for a new signed spectral decomposition, not an available proof of the four-cycle estimate.

The [OpenAI first-moment manuscript, Proposition 4.1](https://github.com/openai/math/blob/main/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/paper.pdf) uses fixed convolutions of smooth prime coefficients, together with a reflected sum and off-diagonal Gram inequality, to save powers in specific cubic dispersion configurations. Those structured coefficients do not carry an arbitrary `l²` source vector, and the proposition's cubic conductor geometry differs from the balanced sextic problem.

The softened target `Tr(E⁴)<<Y^epsilon(Y⁴+Y²M³)` avoids demanding square-root cancellation for every two-row pair, but it still requires cancellation or a bounded-rank spectral decomposition beyond the absolute pair estimates surveyed here. In particular, none of these sources proves it for the actual physical selected rows at `sigma≈0.446`, `L≈Y`.
