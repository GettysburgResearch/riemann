# L-32401 — Affine-log boundary analytic-core factorization

Claim ID: `L-32401`  
Title: Every all-depth affine-log boundary splits exactly into the already-contracting Dirichlet–Taylor bank plus one capped channel  
Status: **PROPOSED COMPLETE EXACT/ANALYTIC LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-s`  
Created: 2026-08-08  
Dependencies: PR #316 `L-30902`; PR #321 `L-30503`; PR #286 `L-28401`  
Scope: exact decomposition of every fresh all-depth boundary; no recurrence for the capped channel and no RH claim

## 1. All-depth boundary profile

Retain the endpoint profile isolated in `L-30503/L-30902`. For

\[
 a\ge0,\qquad L=2^a,\qquad s\ge\frac12,
\]

put

\[
 h_{a,X,s}(x)
 =x^{-s}\log\!\left(\min\{L(x-1)+1,X\}\right),
 \qquad x\ge1.
\tag{L-32401.1}
\]

Let

\[
 x_*=1+\frac{X-1}{L},
 \qquad
 \alpha=1-\frac1L\in[0,1).
\tag{L-32401.2}
\]

Define the uncapped affine-log profile

\[
 u_{a,s}(x)=x^{-s}\log(L(x-1)+1).
\tag{L-32401.3}
\]

Then

\[
\boxed{
 h_{a,X,s}=u_{a,s}-c_{a,X,s},
}
\tag{L-32401.4}
\]

where the cap channel is the explicit nonnegative tail

\[
\boxed{
 c_{a,X,s}(x)
 =x^{-s}
 \log\!\frac{L(x-1)+1}{X}\,
 \mathbf1_{x\ge x_*}.
}
\tag{L-32401.5}
\]

The correction is continuous and vanishes at `x=x_*`.

## 2. Exact inverse-power expansion of the uncapped core

Since

\[
 L(x-1)+1=Lx\left(1-\frac\alpha x\right),
\]

and `0<=alpha/x<1` for every `x>=1`, the logarithmic series is absolutely convergent and gives

\[
\boxed{
\begin{aligned}
 u_{a,s}(x)
 ={}& (\log L)x^{-s}+x^{-s}\log x\\
 &-\sum_{\ell\ge1}
   \frac{\alpha^\ell}{\ell}\,x^{-s-\ell}.
\end{aligned}}
\tag{L-32401.6}
\]

For `a=0`, `alpha=0` and this reduces to `u=x^{-s}log x`.

Thus the complete uncapped profile lies in exactly the power/logarithmic Dirichlet–Taylor bank of `L-28401`; no new analytic species is created by arbitrary support-halving depth.

## 3. Uniform coefficient budget

In the coefficient norm of `L-28401` with radius `r=1/4`, the faster-power tail in (L-32401.6) has norm

\[
\begin{aligned}
 \sum_{\ell\ge1}
 \frac{\alpha^\ell}{\ell}4^{-\ell}
 &=-\log(1-\alpha/4)\\
 &\le -\log(3/4)
 =\log(4/3).
\end{aligned}
\]

Hence

\[
\boxed{
 \left\|
 \sum_{\ell\ge1}
 \frac{\alpha^\ell}{\ell}x^{-s-\ell}
 \right\|_{s,1/4}
 \le\log\frac43
}
\tag{L-32401.7}
\]

uniformly in the endpoint `X` and depth `a`.

The only depth dependence of the analytic core is the explicit scalar

\[
\log L=a\log2\le\log X
\]

whenever the depth is active at endpoint `X`.

## 4. Strict contraction of the entire uncapped channel

`L-28401` proves, for every `sigma>=1/2`,

\[
 \|\mathscr C f\|_{\sigma,1/4}
 \le\frac67\|f\|_{\sigma,1/4}
\tag{L-32401.8}
\]

for the pure-power coefficient bank, and proves that the logarithmic companion carries only a polynomial Jordan factor under iteration.

Equation (L-32401.6) therefore yields the uniform all-depth estimate

\[
\boxed{
 \mathscr C^j u_{a,s}
 =O_s\!\left((1+\log X+j)\left(\frac67\right)^{j-1}\right)
}
\tag{L-32401.9}
\]

in the augmented power/log coefficient norm of `L-28401`; the implied constant is independent of `a` and `X`.

Thus an all-generation obstruction cannot be hidden in the uncapped affine-log core. That complete channel belongs to the already-closed strictly contracting analytic sector.

## 5. Exact location of the unresolved channel

Combining (L-32401.4) and (L-32401.9), every fresh all-depth endpoint injection splits as

```text
fresh boundary
 = strictly contracting affine-log analytic core
   - explicit capped tail.
```

Accordingly a corrected boundary recurrence need not place the entire function `h_(a,X,s)` in one unknown state. It may pay `u_(a,s)` through the existing `6/7` bank and retain only `c_(a,X,s)` in the critical boundary state.

This is compatible with the zero-mode firewall on PR #323: the strict analytic bank is a low-frequency coefficient class and is not asserted to contain the complete zeta-zero mode. The RH-bearing mode must remain visible in the capped/source-specific channel.

## 6. Proof boundary

Established here, subject to review:

1. exact cap/uncapped decomposition;
2. exact inverse-power expansion of the uncapped profile;
3. a depth-uniform `log(4/3)` coefficient-tail budget;
4. membership of the uncapped profile in the already-contracting `L-28401` bank;
5. reduction of the fresh-boundary unknown to one explicit capped channel.

Not established:

1. a recurrence for propagated capped channels;
2. a coefficient-one critical boundary descent theorem;
3. Cycle Debt or RH.
