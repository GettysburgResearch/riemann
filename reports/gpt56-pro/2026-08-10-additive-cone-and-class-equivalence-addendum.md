# Addendum — additive extremality cone and the completed multiplicative ramp criterion

Date: 2026-08-10  
Branch: `research/gpt56-pro/90102-liouville-bernstein-extremality`  
Status: exact strengthening of `L-90201`; exact RH criterion conditional only on the resident Landau consumer; RH unproved

## 1. The local theorem is a cone theorem

`L-90201` used `g(n)=log n`. The proof actually applies to every nonnegative completely additive observable

\[
 g(n)=\sum_pv_p(n)a_p,
 \qquad a_p\ge0.
\]

For real prime parameters `x_p in [-1,1]`, with `y_p=(1+x_p)/2`, the squarefree generalized extraction is

\[
 \begin{aligned}
 ((\mu^2f_x)*g)(n)
 ={}&2^{r-1}\sum_{q\mid\operatorname{rad}(n)}
 g(q)\prod_{p\mid n,p\ne q}y_p\\
 &+2^r[g(n)-g(\operatorname{rad}(n))]\prod_{p\mid n}y_p,
 \end{aligned}
\]

where the first sum is over prime `q`. Every term is nonnegative. At Liouville the coefficient is `g(p)` on prime powers and zero elsewhere.

Thus Liouville simultaneously minimizes every nonnegative valuation/prime-cost observation under every nonnegative arithmetic test weight. The statement extends to commuting positive contractions because the Bernstein monomials remain positive.

This is `L-90202`; `X-90202` verifies 710 vertex cases and 5,975 interior real-cube cases with exact `Fraction` arithmetic.

## 2. The class bootstrap is an exact RH equivalence

Under RH, the classical Chebyshev error

\[
 \psi(t)=t+O(\sqrt t\log^2(2t))
\]

and Stieltjes integration give

\[
 \sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}\log\frac Xn
 =4\sqrt X+O(\log^4(2X)).
\]

`L-90201` transfers this bound pointwise to every sign source and every real prime-cube point. Conversely, uniform Form A specializes to Liouville and the resident `T-90001 §4` Landau consumer yields RH.

Therefore `T-90202` proves the exact criterion

\[
 \boxed{
 \mathrm{RH}
 \Longleftrightarrow
 \text{Form A at Liouville}
 \Longleftrightarrow
 \text{Form A uniformly over }\mathcal H
 \Longleftrightarrow
 \text{Form A uniformly over }[-1,1]^{\mathcal P}.
 }
\]

Claude's fifth dispatch established only the forward reduction from the class criterion and left the comparison with Liouville conjectural. The class bootstrap is now complete in both directions.

## 3. Correct deficit statement

The remaining deficit is not uniformity in the multiplicative class. Uniformity is exact and free. The surviving RH-bearing task is the single Liouville/empty coefficient:

```text
positive ramp class directions                 CLOSED;
nonnegative additive source coordinates        CLOSED;
nonempty GFEP Boolean directions                DESCENDANT THEOREM;
current Liouville / empty coefficient           OPEN.
```

No claim here proves that final coefficient or RH.
