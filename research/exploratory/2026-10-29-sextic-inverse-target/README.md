# An explicit sextic inverse-moment target below the current candidate

**Status:** A precise conditional research target and a source-qualified comparison; the needed improved moment is **not proved**. The implication uses the exact [sixth-power-sector growth identity](../2026-10-29-mobius-marked-boundary/README.md). The benchmark uses the preprint's [Lemma 17.6](https://wcook04.github.io/plectis-atlas/papers/The-Quasi-Riemann-Hypothesis-September-30-2026.html), not only the unrestricted sextic large sieve. Its proposed extension to varying masks is independently auditable as below.

Let K=Q(√−3), W be the fixed smooth compact-annular profile whose Mellin transform has no zeros in `Re s>0`, and let the inverse polynomial use the original zero-extended sextic symbol and Möbius coefficients, with a fixed finite good-prime set S. If one could prove

    Σ_(u∈O, 0<Nu≤U) |D^(−1/2) Σ_(a,S)=1 μ_K(a) χ_a(u)W(Na/D)|²
       ≪_ε U^(1+ε),                 D=U^(28/25),              (1)

then the exact sixth-power-sector identity would imply

    Θ_(ζ_K) ≤ 1/2 + 5/[12·(28/25)] = 293/336
               ≈ 0.8720238095238095.                         (2)

Since `ζ_K(s)=ζ(s)L(s,χ_{−3})`, this would in particular show `ζ(s)≠0` for `Re s>293/336`. It would improve on the tracker candidate `0.8738702` by approximately `0.00184639`, but (1) is **not known or established here**. The same W works for every zero and is fixed independently of U. Condition (1) includes all element rows, including sixth powers; a bound restricted to sixth-free or physically selected rows does not imply (2) without additional work.

The exact sixth-power growth also shows why (1) is hard. The contribution of rows `u=v^6` alone has logarithmic limsup exponent

    1/6 + (56/25)(Θ_(ζ_K)−1/2).

It exceeds 1 if `Θ_(ζ_K)>293/336`. Therefore a proof of (1) necessarily resolves at least this base zero-free question; this is an exact special-family obstruction, not an arithmetic counterexample to (1). The candidate strip `Θ_(ζ_K)≤0.8738702`, even if verified, by itself permits sector exponents up to `1.0041359147` at r=28/25 and `1.0639551467` at r=6/5; it does not exclude the values needed to violate the target. These are upper limits from the strip, not lower bounds on the actual moment.

A more ambitious single-scale target is the same all-row estimate with `D=U^(6/5)`. By the same exact sixth-power identity, it would imply

    Θ_(ζ_K) ≤ 1/2+5/[12·(6/5)] = 61/72 ≈ 0.8472222222,

and therefore `ζ(s)≠0` to the right of `61/72`. This would be a substantial improvement, but this stronger moment bound is also **unproved**. The source-conditional benchmark below is `U^(7/6+ε)` at this scale.

## Comparison with the source amplification estimate

Conditional on the published Lemma 17.6 with its fixed-field, smoothing and power-loss uniformity, the all-row unmarked inverse norm has the following upper bound in any fixed polynomial range for U,D:

    Σ_(0<Nu≤U)|M_u(D)|²
       ≪_ε [U+U^(1/6) D^(5/6)](UD)^ε.                       (3)

At `D=U^(28/25)` this is `U^(11/10+ε)`, so the target (1) asks for a fixed exponent saving of 1/10 compared with this particular source bound. At `D=U^(6/5)` it is `U^(7/6+ε)`, a required saving of 1/6. This does not claim (3) is the strongest bound available in the literature.

For completeness, here is the mask transfer from the stated sixth-free lemma. Write each row uniquely at the ideal level as `u=w v^6`, with w sixth-free; choose primary generators and account for the finitely many units. For fixed v let A=U/(Nv)^6. The inverse row at `wv^6` has the ordinary w-character multiplied by the original mask `1_(a,v)=1`. Its Euler identity is

    M_(w v^6)(D)
       = Σ_(d supported on primes dividing v, (d,S)=1)
           ψ_w(d)/(Nd)^(1/2) · M_w(D/Nd),                    (4)

where `ψ_w(d)=χ_d(w)` (or its fixed finite ray twist). The sum is finite because W is annular and d is a norm divisor of a supported source. It includes arbitrary exponents of those primes; using only squarefree d would be incorrect. The identity follows by multiplying the Möbius Euler product by `∏_(p|v)(1−ψ_w(p)Np^(−s))^(−1)` and retains the zero mask at p|w.

Weighted Cauchy gives a factor

    Σ_(d|rad(v)^∞) (Nd)^(−1/2)
       = ∏_(p|v,p∉S) (1−Np^(−1/2))^(−1) ≪_ε (Nv)^ε.     (5)

Apply Lemma 17.6, on the finitely many dyadic w ranges up to A, to each `D/Nd`. The source lemma is explicitly for **all** sixth-free element rows, with no principal-character exclusion, and its all-row input is (17.87); in particular its bounded dyad includes w=1 and any other fixed bad-prime/unit presentation. This source dependence is essential. The extra weights in (4), the same geometric Euler bound, fixed units and dyadic logarithms are absorbed by `(UD)^ε`; bounded scales `D/Nd<1` are handled directly. This gives `≪_ε [A+A^(1/6)D^(5/6)](UD)^ε` for each v. Summing over `Nv≪U^(1/6)` uses the convergent `Σ_v (Nv)^(−6)` and harmonic `Σ_(Nv≤U^(1/6)) (Nv)^(−1)≪log U`, giving (3). The fixed parameter c>0 in the source lemma's `D^{5(1+c)/6}` can be chosen in advance sufficiently small for the requested ε and the fixed polynomial range of D.

By contrast, directly applying the quoted unrestricted sixth-order large sieve to all rows gives the four-term expression `U+D U^(1/6)+U^(5/6)D^(1/3)+U^(1/3)D^(5/6)`. Its largest exponent at r=28/25 is `193/150≈1.28667`, so it does not itself provide the 1.1 benchmark.

**Independent review:** Families and High_match checked the mask Euler expansion, all prime-power terms, weighted Cauchy, dyadic and v sums, and fixed-scale treatment. Families separately verified that the actual printed Lemma 17.6 includes principal sixth-free rows; a different nonprincipal-only moment theorem would not suffice. The cited analytic lemma has not been independently proved here.

**Literature reconnaissance:** An independent search found no stated Möbius-specific all-row sextic estimate beating this benchmark at `D≈U^(6/5)`. The [OpenAI October 5 manuscript](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex) has a Möbius-to-cubic-theta construction, but its cited main family estimate requires row height `H=D^(1+ϑ)>D`; it does not cover the target `D>U`. The [rStation post 9](https://rstation.ai/r/riemann_hypothesis/posts/9) treats special squarefree `p q²` families and moving masks. These scope checks are not a comprehensive priority search.

## Why the published Möbius-to-theta range does not directly extend

The October 5 manuscript's outline first applies Poisson in the rows and introduces a dual norm scale `ℋ≈D²/U`. It reduces a simplified problem to `Σ_(Nh≤ℋ)|P_h(D)|²≪D`, and its completed-theta estimate has the form `ℋ+ℋ²/D` before removing cube factors. Its cube cutoff and subsequent argument explicitly require `ℋ≤D`, corresponding to U≥D. At the proposed scale `D=U^(6/5)`, the dual scale is `ℋ=D^(7/6)>D`, and the displayed completed-theta bound is already `D^(4/3)`; the cutoff `(D/ℋ)^(2/3)` is below 1. A direct extrapolation of those upper bounds therefore misses the simplified dual target by a power `D^(1/3)`. Even the first displayed term ℋ exceeds D.

This is a comparison with the manuscript's **schematic** dual target and sufficient bound; its full proof has additional gcd, congruence and mask parameters. It is not a lower bound for the actual theta sum or an impossibility result. Reaching the proposed U^(1+ε) moment would need an alternative that controls those long-dual correlations or avoids the positive separation that creates this loss.

**Theta-range review:** Literature independently checked the cited outline formulas, the ℋ≤D prerequisite, and the exponents ℋ=D^(7/6), completed bound D^(4/3) and cutoff D^(−1/9). The comparison remains schematic, not a lower bound on the actual dual sum.

**A long-dual obstruction to the schematic sufficient bound:** The independently reviewed, source-conditional [theta-family diagonal calculation](../2026-10-29-sextic-dual-diagonal-obstruction.md) uses rStation paper 5's stated nonprincipal off-diagonal estimate to show that the unmarked positive dual θ-family has mean `≫ℋ` for `ℋ=D^(7/6)`. Thus a naive extrapolation requiring that whole family to be `≪D^(1+ε)` is false in this range. This does not contradict the October 5 manuscript, which uses `ℋ<D`, and it does not rule out cancellation in the signed, coupled full physical Poisson expression or settle the original inverse target.

A source-qualified [partial-frame calculation](../2026-10-29-theta-partial-frame/README.md) suppresses the Möbius projection onto many inverse-oriented Gauss directions at D=U^(6/5). It does not bound the remaining source component or control all prime profiles, so it does not establish either target in this note.

The later source-qualified [full Gram argument](../2026-10-29-theta-partial-frame/full-gram.md) now controls the projection onto the entire inverse-oriented profile span with full-norm index Nh≤P^(25/54−δ), rather than only a selected high-Gram subspace. The source component orthogonal to that span, physical masks and detector profiles remain unbounded by this result, and the target moment remains unproved.
