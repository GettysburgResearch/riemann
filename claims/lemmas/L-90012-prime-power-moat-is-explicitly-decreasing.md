# L-90012 — The prime-power moat is explicitly negative and decreasing from 2000

Claim ID: `L-90012` (provisional range; chosen to avoid the live `L-90010` collision on PR #350)  
Title: An elementary complete-prime-power estimate gives `X M'(X)<-0.30` for every real endpoint above 2000  
Status: **PROPOSED COMPLETE EXPLICIT THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Date: 2026-08-09  
Depends on: `L-90009`; `T-90002` P2; Rosser--Schoenfeld's explicit `theta(x)<=1.01624x`; elementary concavity  
Scope: the zero-insensitive moat only; no sign theorem for the RH-sensitive complete deficit

## 1. Statement

Retain the exact moat of `L-90009`,

\[
 \mathfrak M(X)
 =J_{\mathbb P}(X)
 +\sum_{\substack{p^a\le X\\a\ge2}}
  {\log p\over p^{a/2}}\log{X\over p^a}
 -4\sqrt X.
\tag{L-90012.1}
\]

For every noninteger real `X>=2000`,

\[
\boxed{
 X\mathfrak M'(X)<-0.30.
}
\tag{L-90012.2}
\]

The function `M` is continuous at every integer endpoint, and the directed
finite certificate `X-90010` gives

\[
\boxed{
 -29.417<\mathfrak M(2000)<-29.416.
}
\tag{L-90012.3}
\]

Consequently

\[
\boxed{
 \mathfrak M(X)<-29.416-0.30\log(X/2000)<0
 \qquad(X\ge2000).
}
\tag{L-90012.4}
\]

Thus the prime-power moat is not merely eventually negative by a zero-free
contour. It is explicitly negative and strictly decreasing on the whole
half-line `[2000,infinity)`.

## 2. Complete-prime-power seed

Let

\[
 J_\Lambda(X)=\sum_{q\le X}\Lambda(q)v_q(X).
\]

Finite divisor switching gives, for `N=floor X`,

\[
 J_\Lambda(X)
 =\sum_{m=2}^{N}b_X(m)\log{m\over m-1}.
\tag{L-90012.5}
\]

On an open interval `(N,N+1)`, put

\[
 \mathcal D_X=X{d\over dX}.
\]

Since

\[
 \mathcal D_Xb_X(m)=2\sqrt m-{2m\over\sqrt X},
\]

one has exactly

\[
 \mathcal D_XJ_\Lambda(X)
 =\sum_{m=2}^{N}
 \left(2\sqrt m-{2m\over\sqrt X}\right)
 \log{m\over m-1}.
\tag{L-90012.6}
\]

The coefficient in parentheses is nonnegative. The elementary logarithmic
inequality

\[
 \log{b\over a}\le{b-a\over\sqrt{ab}}
 \qquad(0<a<b)
\tag{L-90012.7}
\]

therefore gives

\[
\begin{aligned}
 \mathcal D_XJ_\Lambda(X)
 &\le2\sum_{r=1}^{N-1}{1\over\sqrt r}
 -{2\over\sqrt X}\sum_{m=2}^{N}\sqrt{m\over m-1}\\
 &\le2S_{N-1}-{2(N-1)\over\sqrt X},
\end{aligned}
\tag{L-90012.8}
\]

where `S_n=sum_(k<=n) k^-1/2`.

`T-90002` P2 proves the explicit Euler--Maclaurin upper bound

\[
 S_n\le2\sqrt n+\zeta(1/2)+{1\over2\sqrt n}.
\tag{L-90012.9}
\]

Hence

\[
\begin{aligned}
 \mathcal D_XJ_\Lambda(X)-2\sqrt X
 \le{}&2\zeta(1/2)+{1\over\sqrt{N-1}}\\
 &-{2(\sqrt X-\sqrt{N-1})^2\over\sqrt X}\\
 \le{}&2\zeta(1/2)+{1\over\sqrt{N-1}}.
\end{aligned}
\tag{L-90012.10}
\]

For `X>=2000`, `N>=2000`. Using the certified elementary value

\[
 \zeta(1/2)<-1.46035
\]

and `sqrt(1999)>44`,

\[
\boxed{
 \mathcal D_XJ_\Lambda(X)-2\sqrt X<-2.8979.
}
\tag{L-90012.11}
\]

This is the negative base budget.

## 3. Higher-prime-power correction

From

\[
 J_{\mathbb P}
 =J_\Lambda-\sum_{\substack{q=p^a\\a\ge2}}(\log p)v_q
\]

and (L-90012.1),

\[
\boxed{
 \mathcal D_X\mathfrak M(X)
 =\mathcal D_XJ_\Lambda(X)-2\sqrt X
 +\sum_{\substack{q=p^a\le N\\a\ge2}}
  (\log p)\left(q^{-1/2}-\mathcal D_Xv_q(X)\right).
}
\tag{L-90012.12}
\]

Only the positive part of the final sum needs an upper bound.

Fix one prime power `q>=4` and put

\[
 K=\left\lfloor{X\over q}\right\rfloor,
 \qquad t={X\over q}\in(K,K+1).
\]

### Nonboundary columns

If `q` does not divide `N`, then `Kq+1<=N`, and direct differentiation gives

\[
 \sqrt q\,\mathcal D_Xv_q
 ={2K\over\sqrt t}
 -2q\sum_{k=1}^{K}
  \left(\sqrt{k+1/q}-\sqrt k\right).
\tag{L-90012.13}
\]

Concavity of the square root gives

\[
 2q\left(\sqrt{k+1/q}-\sqrt k\right)
 ={2\over\sqrt{k+1/q}+\sqrt k}
 \le{k^{-1/2}}.
\]

Therefore

\[
\boxed{
 \sqrt q\left(q^{-1/2}-\mathcal D_Xv_qight)
 \le u_K
 :=1+S_K-{2K\over\sqrt{K+1}}.
}
\tag{L-90012.14}
\]

The sequence `u_K` is strictly decreasing, because

\[
 u_{K+1}-u_K
 ={2K+1\over\sqrt{K+1}}
 -{2(K+1)\over\sqrt{K+2}}<0,
\]

and squaring the two positive terms reduces the inequality to

\[
 4(K+1)^3-(2K+1)^2(K+2)=3K+2>0.
\]

The interval certificate gives

\[
 u_{10}<-0.0092,
\tag{L-90012.15}
\]

so a nonboundary prime power can contribute positively only when `1<=K<=9`.

### Boundary columns

If `q|N`, the final difference is cut by the endpoint. Its omitted second term
is replaced by the nonnegative quantity `D_X b_X(N)`. Dropping that quantity
and repeating the preceding estimate gives

\[
\boxed{
 \sqrt q\left(q^{-1/2}-\mathcal D_Xv_qight)
 \le v_K
 :=1+S_{K-1}-{2(K-1)\over\sqrt{K+1/4}}.
}
\tag{L-90012.16}
\]

Here `q>=4` was used to obtain

\[
 t<K+1/q\le K+1/4.
\]

The sequence `v_K` is also strictly decreasing. Indeed, with

\[
 f(x)={2(x-1)\over\sqrt{x+1/4}},
\]

one has

\[
 v_{K+1}-v_K={1\over\sqrt K}-[f(K+1)-f(K)].
\]

Now

\[
 f''(x)=-{16(x+4)\over(4x+1)^{5/2}}<0,
\]

so `f(K+1)-f(K)>=f'(K+1)`, while

\[
 f'(K+1)>{1\over\sqrt K}
\]

because, after squaring,

\[
 16K(2K+5)^2-(4K+5)^3
 =5(16K^2+20K-25)>0.
\]

The interval certificate gives

\[
 v_{15}<-0.0142.
\tag{L-90012.17}
\]

Thus only the fourteen boundary quotients `K<=14` can contribute positively.

## 4. Summing the nonboundary prime powers

For `1<=K<=9` put

\[
 w_K=u_K\sqrt{K+1}.
\]

The finite radical certificate proves

\[
 w_1>w_2>\cdots>w_9>0,
\qquad
 w_1=2(\sqrt2-1).
\tag{L-90012.18}
\]

Fix an exponent `a>=2`. The positive nonboundary terms lie in the intervals

\[
 \left({X\over K+1}\right)^{1/a}<p
 \le\left({X\over K}\right)^{1/a},
 \qquad1\le K\le9.
\]

On the `K`th interval,

\[
 p^{-a/2}\le\sqrt{K+1\over X}.
\]

Writing `theta(y)=sum_(p<=y) log p` and summing the nine intervals by parts,
monotonicity (L-90012.18) gives

\[
\begin{aligned}
 &\sum_{K=1}^{9}u_K
 \sum_{(X/(K+1))^{1/a}<p\le(X/K)^{1/a}}
 {\log p\over p^{a/2}}\\
 &\qquad\le{w_1\over\sqrt X}\,\vartheta(X^{1/a}).
\end{aligned}
\tag{L-90012.19}
\]

Use the classical explicit bound

\[
 \vartheta(y)\le1.01624\,y
 \qquad(y>0).
\tag{L-90012.20}
\]

Since `1.01624*2(sqrt2-1)<0.844`, the complete nonboundary contribution is at
most

\[
 0.844\sum_{a=2}^{\lfloor\log_2X\rfloor}X^{1/a-1/2}.
\tag{L-90012.21}
\]

For `X>=2000`,

\[
\begin{aligned}
 \sum_{a=2}^{\lfloor\log_2X\rfloor}X^{1/a-1/2}
 \le{}&1+X^{-1/6}+X^{-1/4}+X^{-3/10}+X^{-1/3}\\
 &+(\log_2X)X^{-5/14}.
\end{aligned}
\tag{L-90012.22}
\]

Every term on the right is decreasing for `X>=2000`. At `X=2000`, the simple
rational bounds

```text
X^-1/6 < 0.282,   X^-1/4 < 0.150,
X^-3/10 < 0.103,  X^-1/3 < 0.080,
log_2(X) X^-5/14 < 11*0.067 = 0.737
```

give

\[
\boxed{
 \text{positive nonboundary correction}<0.844(2.352)<1.986.
}
\tag{L-90012.23}
\]

## 5. Summing the boundary prime powers

For a boundary term, `q=N/K=p^a` and `a>=2`. Hence

\[
 {\log p\over\sqrt q}
 \le{\log N\over2}\sqrt{K\over N}.
\]

The finite interval certificate gives

\[
 {1\over2}\sum_{K=1}^{14}v_K^+\sqrt K<3.32.
\tag{L-90012.24}
\]

Therefore

\[
 \text{positive boundary correction}
 <3.32{\log N\over\sqrt N}.
\]

The function `log x/sqrt x` decreases for `x>e^2`; at `N>=2000`, using
`log 2000<8` and `sqrt 2000>44`,

\[
\boxed{
 \text{positive boundary correction}<3.32{2\over11}<0.604.
}
\tag{L-90012.25}
\]

## 6. Completion

Combining (L-90012.11), (L-90012.23), and (L-90012.25),

\[
 \mathcal D_X\mathfrak M(X)
 <-2.8979+1.986+0.604<-0.30.
\]

This proves (L-90012.2).

The same interval artifact evaluates (L-90012.1) directly at `X=2000`, using
radical switching, and gives (L-90012.3). Continuity at integers follows because
every newly entering ramp and seed coefficient vanishes at its own endpoint.
Integrating (L-90012.2) in `dX/X` proves (L-90012.4).

## 7. Consequence for the RH-facing endpoint

The exact decomposition remains

\[
 A(X)=\Delta_\Lambda(X)+\mathfrak M(X).
\]

The present theorem completely closes the moat side for `X>=2000`:

```text
M(X) < 0;
M is strictly decreasing;
-M(X) > 29.416+0.30 log(X/2000).
```

Thus every unresolved sign and every possible loss of monotonicity of `A` lies
in the classical weighted-Chebyshev deficit `Delta_Lambda`, not in the
prime-only correction.

This does not prove the upper-wall inequality

\[
 \Delta_\Lambda(X)<-\mathfrak M(X),
\]

which remains RH-equivalent by `T-90008` and `L-90009`.

## 8. Proof boundary

Closed explicitly, subject to review:

1. the negative complete-prime-power base budget;
2. the nonboundary quotient cutoff `K<=9`;
3. the boundary quotient cutoff `K<=14`;
4. the decreasing nine-cell weight telescope;
5. the explicit nonboundary and boundary prime-power sums;
6. `D_X M<-0.30` for every noninteger `X>=2000`;
7. the directed value of `M(2000)`;
8. explicit negativity and strict decrease on `[2000,infinity)`.

Imported classical input:

- `theta(x)<=1.01624x`, Rosser--Schoenfeld.

Still open:

1. the weighted-Chebyshev upper wall;
2. eventual negativity or monotonicity of `A`;
3. RH.
