# L-90012 — The prime-power moat is explicitly negative and decreasing from 2000

Claim ID: `L-90012` (provisional range; chosen to avoid the live `L-90010` collision on PR #350)  
Title: An elementary complete-prime-power estimate gives `X M'(X)<-0.30` for every real endpoint above 2000  
Status: **PROPOSED COMPLETE EXPLICIT THEOREM — INDEPENDENT REVIEW REQUIRED; R-90006 REPAIR FOLDED IN**  
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

The function `M` is continuous at integer endpoints, and the directed
certificate `X-90012` gives

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

`L-90014` separately closes the finite base and upgrades this to the whole
natural domain `X>=2`.

## 2. Complete-prime-power base budget

Let

\[
 J_\Lambda(X)=\sum_{q\le X}\Lambda(q)v_q(X).
\]

Finite divisor switching gives, with `N=floor X`,

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

The two pieces must be bounded separately.  For the positive piece use

\[
\boxed{
 \log{m\over m-1}
 \le {1\over\sqrt{m(m-1)}}.
}
\tag{L-90012.7}
\]

For the negative piece use

\[
\boxed{
 \log{m\over m-1}
 =\log\left(1+{1\over m-1}\right)
 \ge {1\over m}.
}
\tag{L-90012.8}
\]

The first inequality is the symmetric logarithmic-mean bound; the second is
`log(1+x)>=x/(1+x)`.  Therefore

\[
\boxed{
 \mathcal D_XJ_\Lambda(X)
 \le 2S_{N-1}-{2(N-1)\over\sqrt X},
}
\tag{L-90012.9}
\]

where `S_n=sum_(k<=n)k^-1/2`.

`T-90002` P2 proves

\[
 S_n\le2\sqrt n+\zeta(1/2)+{1\over2\sqrt n}.
\tag{L-90012.10}
\]

Hence

\[
\begin{aligned}
 \mathcal D_XJ_\Lambda(X)-2\sqrt X
 \le{}&2\zeta(1/2)+{1\over\sqrt{N-1}}\\
 &-{2(\sqrt X-\sqrt{N-1})^2\over\sqrt X}\\
 \le{}&2\zeta(1/2)+{1\over\sqrt{N-1}}.
\end{aligned}
\tag{L-90012.11}
\]

For `X>=2000`, use `zeta(1/2)<-1.46035` and `sqrt(1999)>44`:

\[
\boxed{
 \mathcal D_XJ_\Lambda(X)-2\sqrt X<-2.8979.
}
\tag{L-90012.12}
\]

This is the negative base budget.  `R-90006` records why the split use of
(L-90012.7)--(L-90012.8) is necessary.

## 3. Higher-prime-power correction

Since

\[
 J_{\mathbb P}
 =J_\Lambda-\sum_{\substack{q=p^a\\a\ge2}}(\log p)v_q,
\]

one has

\[
\boxed{
 \mathcal D_X\mathfrak M(X)
 =\mathcal D_XJ_\Lambda(X)-2\sqrt X
 +\sum_{\substack{q=p^a\le N\\a\ge2}}
  (\log p)\left(q^{-1/2}-\mathcal D_Xv_q(X)\right).
}
\tag{L-90012.13}
\]

Only the positive part of the final sum requires an upper bound.  Fix one
prime power `q>=4`, and put

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
\tag{L-90012.14}
\]

Concavity of the square root gives

\[
 2q\left(\sqrt{k+1/q}-\sqrt k\right)
 ={2\over\sqrt{k+1/q}+\sqrt k}
 \le k^{-1/2}.
\]

Therefore

\[
\boxed{
 \sqrt q\left(q^{-1/2}-\mathcal D_Xv_qight)
 \le u_K:=1+S_K-{2K\over\sqrt{K+1}}.
}
\tag{L-90012.15}
\]

The sequence `u_K` is strictly decreasing, because

\[
 u_{K+1}-u_K
 ={2K+1\over\sqrt{K+1}}
 -{2(K+1)\over\sqrt{K+2}}<0,
\]

and squaring reduces the inequality to

\[
 4(K+1)^3-(2K+1)^2(K+2)=3K+2>0.
\]

The directed certificate gives

\[
 u_{10}<-0.0092,
\tag{L-90012.16}
\]

so a nonboundary prime power can contribute positively only for `K<=9`.

### Boundary columns

If `q|N`, the last difference is cut by the endpoint.  Its omitted second term
is replaced by the nonnegative quantity `D_Xb_X(N)`.  Dropping that quantity
and repeating the same estimate gives

\[
\boxed{
 \sqrt q\left(q^{-1/2}-\mathcal D_Xv_qight)
 \le v_K:=1+S_{K-1}-{2(K-1)\over\sqrt{K+1/4}}.
}
\tag{L-90012.17}
\]

Here `t<K+1/q<=K+1/4`.  The sequence `v_K` is strictly decreasing.  With

\[
 f(x)={2(x-1)\over\sqrt{x+1/4}},
\]

one has

\[
 v_{K+1}-v_K={1\over\sqrt K}-[f(K+1)-f(K)].
\]

Since

\[
 f''(x)=-{16(x+4)\over(4x+1)^{5/2}}<0,
\]

concavity gives `f(K+1)-f(K)>=f'(K+1)`, while

\[
 f'(K+1)>{1\over\sqrt K}
\]

because

\[
 16K(2K+5)^2-(4K+5)^3
 =5(16K^2+20K-25)>0.
\]

The certificate gives

\[
 v_{15}<-0.0142,
\tag{L-90012.18}
\]

so only the fourteen boundary quotients `K<=14` can contribute positively.

## 4. Nonboundary prime-power ledger

For `1<=K<=9`, put

\[
 w_K=u_K\sqrt{K+1}.
\]

The finite certificate proves

\[
 w_1>w_2>\cdots>w_9>0,
 \qquad w_1=2(\sqrt2-1).
\tag{L-90012.19}
\]

Fix an exponent `a>=2`.  Positive nonboundary terms lie in

\[
 \left({X\over K+1}\right)^{1/a}<p
 \le\left({X\over K}\right)^{1/a},
 \qquad1\le K\le9.
\]

On the `K`th interval,

\[
 p^{-a/2}\le\sqrt{K+1\over X}.
\]

Writing `theta(y)=sum_(p<=y)log p` and summing the nine intervals by parts,
monotonicity of `w_K` gives

\[
\begin{aligned}
 &\sum_{K=1}^{9}u_K
 \sum_{(X/(K+1))^{1/a}<p\le(X/K)^{1/a}}
 {\log p\over p^{a/2}}\\
 &\qquad\le{w_1\over\sqrt X}\vartheta(X^{1/a}).
\end{aligned}
\tag{L-90012.20}
\]

Use the classical explicit bound

\[
 \vartheta(y)\le1.01624\,y
 \qquad(y>0).
\tag{L-90012.21}
\]

Since `1.01624*2(sqrt2-1)<0.844`, all nonboundary exponents contribute at most

\[
 0.844\sum_{a=2}^{\lfloor\log_2X\rfloor}X^{1/a-1/2}.
\tag{L-90012.22}
\]

For `X>=2000`,

\[
\begin{aligned}
 \sum_{a=2}^{\lfloor\log_2X\rfloor}X^{1/a-1/2}
 \le{}&1+X^{-1/6}+X^{-1/4}+X^{-3/10}+X^{-1/3}\\
 &+(\log_2X)X^{-5/14}<2.352.
\end{aligned}
\tag{L-90012.23}
\]

The last inequality is largest at `X=2000` and is discharged by the rational
bounds retained in `X-90012`.  Therefore

\[
\boxed{
 \text{positive nonboundary correction}<1.986.
}
\tag{L-90012.24}
\]

## 5. Boundary prime-power ledger

For a boundary term, `q=N/K=p^a` with `a>=2`. Hence

\[
 {\log p\over\sqrt q}
 \le{\log N\over2}\sqrt{K\over N}.
\]

The directed certificate gives

\[
 {1\over2}\sum_{K=1}^{14}v_K^+\sqrt K<3.32.
\tag{L-90012.25}
\]

Therefore

\[
 \text{positive boundary correction}
 <3.32{\log N\over\sqrt N}.
\]

The function `log x/sqrt x` decreases for `x>e^2`; using `log2000<8` and
`sqrt2000>44`,

\[
\boxed{
 \text{positive boundary correction}<3.32{2\over11}<0.604.
}
\tag{L-90012.26}
\]

## 6. Completion

Combining the base and the two correction ledgers,

\[
 \mathcal D_X\mathfrak M(X)
 <-2.8979+1.986+0.604<-0.30.
\]

This proves (L-90012.2).  The same interval artifact evaluates
`M(2000)` by direct radical switching and proves (L-90012.3).  Continuity at
integers follows because every newly entering ramp and seed summand vanishes at
its own endpoint.  Integration in `dX/X` proves (L-90012.4).

## 7. Consequence for the RH-facing endpoint

The exact decomposition remains

\[
 A(X)=\Delta_\Lambda(X)+\mathfrak M(X).
\]

Thus every unresolved sign lies in the classical weighted-Chebyshev deficit,
not in the prime-only correction.  `L-90014` strengthens the conclusion to

```text
M(X)<0 and X M'(X)<-0.30 for every real X>=2.
```

This does not prove the upper-wall inequality

\[
 \Delta_\Lambda(X)<-\mathfrak M(X),
\]

which remains RH-equivalent by `T-90008` and `L-90009`.

## 8. Proof boundary

Closed explicitly, subject to review:

1. the corrected two-sided logarithm estimate;
2. the negative complete-prime-power base budget;
3. the nonboundary quotient cutoff `K<=9`;
4. the boundary quotient cutoff `K<=14`;
5. the decreasing nine-cell telescope;
6. the two explicit correction ledgers;
7. `D_XM<-0.30` for every noninteger `X>=2000`;
8. the directed value of `M(2000)`.

Imported classical input:

- `theta(x)<=1.01624x`, Rosser--Schoenfeld.

Still open:

1. the weighted-Chebyshev upper wall;
2. eventual negativity or monotonicity of `A`;
3. RH.
