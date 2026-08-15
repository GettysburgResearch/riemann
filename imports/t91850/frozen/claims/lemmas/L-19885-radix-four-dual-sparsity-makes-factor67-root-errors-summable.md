# L-19885 — Radix-four dual sparsity makes the factor-67 root errors summable

Claim ID: `L-19885`  
Status: **PROPOSED EXACT ARITHMETIC ESTIMATE — PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-x`  
Created: 2026-08-14  
Depends on: `L-91378`, `L-91691`, `L-91115`, `L-19882`  
Frozen factor-67 head: `13ad1fdbf06edc931dc0c524327b701c5c8f86a3`  
RH status: **unproved**

## 1. Exact support of the radix-four dual

Recall

\[
 Y_4(q)=\sum_{k=0}^{v_4(q)}2^k\Lambda(q/4^k).
 \tag{L-19885.1}
\]

Write `q=2^e m` with `m` odd.

If `m=1`, every nonzero term is a power of two and

\[
\boxed{
 Y_4(2^e)
 =\bigl(2^{\lceil e/2\rceil}-1\bigr)\log2.
}
\tag{L-19885.2}

If `m=p^a` for an odd prime `p`, then `q/4^k` can be a prime power only when
all factors of two have been removed.  This requires `e=2v` and `k=v`, giving

\[
\boxed{
 Y_4(4^vp^a)=2^v\log p.
}
\tag{L-19885.3}

If `m` contains two distinct odd primes, or if `m=p^a` and `e` is odd, every
term in (L-19885.1) contains at least two prime factors and

\[
\boxed{Y_4(q)=0.}
\tag{L-19885.4}

Thus `Y_4` is supported only on powers of two and radix-four lifts of odd prime
powers.  The thousands of zero columns observed in PR #470 are the finite
shadow of this exact support theorem.

## 2. A globally summable mismatch weight

Put

\[
 \Sigma_{3/2}
 =\sum_{q\ge2}\frac{Y_4(q)}{q^{3/2}}.
\]

For powers of two, splitting `e=2v` and `e=2v+1` gives

\[
 \sum_{e\ge1}\frac{Y_4(2^e)}{2^{3e/2}}
 <\frac13+\frac4{3\sqrt2}<\frac53.
\tag{L-19885.5}

For odd prime powers, (L-19885.3) gives

\[
\begin{aligned}
 \sum_{v\ge0}\sum_{p\ {m odd}}\sum_{a\ge1}
 \frac{2^v\log p}{(4^vp^a)^{3/2}}
 &=\frac43\sum_{p\ {m odd}}\sum_{a\ge1}
   \frac{\log p}{p^{3a/2}}\\
 &\le\frac43\sum_{n\ge2}\frac{\log n}{n^{3/2}}.
\end{aligned}
\tag{L-19885.6}

The function `log(x)x^(-3/2)` is decreasing on `[2,infinity)`, so

\[
 \sum_{n\ge2}\frac{\log n}{n^{3/2}}
 \le\frac{\log2}{2\sqrt2}
 +\int_2^\infty\frac{\log x}{x^{3/2}}dx
 <\frac{13}{2}.
\tag{L-19885.7}

Consequently

\[
\boxed{
 \Sigma_{3/2}<\frac53+\frac{26}{3}<11.
}
\tag{L-19885.8}

No prime number theorem is used.

## 3. A soft partial-sum bound

For `X>=2`, put `L=log(2X)`.  The power-of-two contribution satisfies

\[
 \sum_{2^e\le X}\frac{Y_4(2^e)}{2^e}<3.
\tag{L-19885.9}

For odd prime powers,

\[
\begin{aligned}
 \sum_{4^vp^a\le X}
 \frac{Y_4(4^vp^a)}{4^vp^a}
 &=\sum_{v\ge0}2^{-v}
   \sum_{p^a\le X/4^v}\frac{\log p}{p^a}\\
 &\le2L(1+L),
\end{aligned}
\tag{L-19885.10}

because `Lambda(n)<=L` and the harmonic sum up to `X` is at most `1+L`.
Hence

\[
\boxed{
 \sum_{q\le X}\frac{Y_4(q)}q
 \le3+2L+2L^2.
}
\tag{L-19885.11}

This deliberately elementary estimate is more than sufficient below.

## 4. Factor-67 finite/continuum mismatch

`L-91691.8` gives, for every outer column `q>=K`,

\[
 |e_X^{\rm mis}(q)|
 <\frac{285}{8}q^{-3/2}.
\tag{L-19885.12}

Therefore (L-19885.8) gives the absolute native-dual cost

\[
\boxed{
 \sum_{q\ge K}Y_4(q)|e_X^{\rm mis}(q)|
 <\frac{285}{8}\,11
 <392.
}
\tag{L-19885.13}

The finite/continuum discrepancy is thus uniformly summable in the exact native
metric.  Its coordinatewise `q^(-3/2)` estimate is much stronger after the
prime-power sparsity of `Y_4` is retained.

## 5. Factor-67 quantization collar

`L-91691.9` gives

\[
 |e_X^{\rm col}(q)|
 <\frac{200}{q\sqrt K}.
\tag{L-19885.14}

Equations (L-19885.11) and `K>X/67` imply

\[
\boxed{
 \sum_{K\le q\le X}Y_4(q)|e_X^{\rm col}(q)|
 \le
 \frac{200}{\sqrt K}(3+2L+2L^2)
 =o(1).
}
\tag{L-19885.15}

Thus the width-three martingale collar has vanishing native-dual cost even
under a completely elementary prime-power bound.

## 6. Global safety thinning

The safety factor of `L-91691` is

\[
 \sigma_K=(1+178/K)^{-1},
 \qquad
 1-\sigma_K<178/K.
\tag{L-19885.16}

The exact native benchmark obeys the elementary estimate

\[
\begin{aligned}
 J_\Lambda(X)
 &=\sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}
   \log\frac Xn\\
 &\le2\sqrt X\,\log^2(2X).
\end{aligned}
\tag{L-19885.17}

Therefore the complete native-dual cost of globally thinning one full parent
packet is

\[
\boxed{
 (1-\sigma_K)J_\Lambda(X)
 \le23852\frac{\log^2(2X)}{\sqrt X}
 =o(1).
}
\tag{L-19885.18}

This estimate includes the source-owned inner children because the safety
factor is applied once to the common parent before physical realization.

## 7. Top omission and bounded positive corrections

The omitted top packet of `L-91115` is a positive endpoint packet with
nonnegative detail response.  By the exact dual identity,

\[
 \sum_qY_4(q)\Xi_{\rm top}(q)
 =\mathcal H(P_{\rm top}).
\tag{L-19885.19}

`L-91115.19` gives

\[
 \mathcal H(P_{\rm top})
 =O(WX^{-1/2}\log^2(2X))=O(1).
\tag{L-19885.20}

The finite base correction and the single current-owned port in `L-91691` have
bounded literal score on the frozen construction, hence bounded `Y_4` cost by
the same dual identity.  Root Hall and the causal current/child identity create
no additional literal-score loss: they are exact in every component row, and
all row bonuses are nonnegative.

## 8. Direct factor-67 root slack bound

Let the exact finite equality packet have native detail vector `Omega_X`.
Reserve every exact inner child capacity before insertion, and let `r_X>=0` be
the unused parent detail vector after:

```text
one common-parent Hall/causal decomposition;
one global martingale quantizer;
one safety thinning;
one top omission;
one finite/continuum correction reserve;
one finite base correction and shared port.
```

Feasibility gives `r_X>=0`.  Since the ideal Hall/causal decomposition is exact
in component rows and full child capacities, the only possible native-dual
losses are those bounded in Sections 4--7.  Hence

\[
\boxed{
 \delta_X:=\langle Y_4,r_X\rangle=O(1).
}
\tag{L-19885.21}

More explicitly, the mismatch contribution is below `392`, the collar and
safety contributions tend to zero, and the fixed top/base/port contributions
are bounded.

Combining (L-19885.21) with the exact slack cocycle of `L-19882` and
`sum alpha_b<1/8` gives

\[
\boxed{
 J_\Lambda(X)-\mathcal H(d_X)
 =\langle Y_4,s_X\rangle=O(1)
}
\tag{L-19885.22}

on the frozen factor-67 common-parent hypotheses.

This is the corrected native conclusion.  It does **not** imply
`4 sqrt(X)-H(d_X)=O(1)`; under RH those two quantities differ by the positive
logarithmic term identified in `R-19882`.

## 9. Exact boundary

```text
support formula for Y4                              EXACT
sum Y4(q)q^(-3/2)<11                               EXACT ELEMENTARY
sum_(q<=X) Y4(q)/q <=3+2L+2L^2                    EXACT ELEMENTARY
factor-67 mismatch native cost <392                 EXACT ON L-91691.8
factor-67 collar native cost o(1)                   EXACT ON L-91691.9
global safety native cost o(1)                      EXACT
fixed top/base/port native cost O(1)                FROZEN POSITIVE-PACKET INPUT
factor-67 root native slack O(1)                    PROPOSED COMPLETE ON FROZEN INPUTS
Riemann Hypothesis                                  UNPROVED PENDING FULL REVIEW
```
