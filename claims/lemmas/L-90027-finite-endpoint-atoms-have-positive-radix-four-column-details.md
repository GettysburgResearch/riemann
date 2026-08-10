# L-90027 — Every finite endpoint atom has a positive radix-four column detail

Claim ID: `L-90027` (provisional range; branch-qualified)  
Title: The exact endpoint-scale response matrix satisfies `Gamma_T(q)>2 Gamma_T(4q)`; every endpoint atom therefore has a finite positive radix-four column-renewal expansion  
Status: **PROPOSED COMPLETE EXACT FINITE POSITIVITY THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Date: 2026-08-10  
Depends on: the positive endpoint atoms of PR #265 `L-26201`; the square-root-sum inequality proved in `L-90025`; elementary logarithmic-mean and convexity inequalities  
Scope: exact finite endpoint/column geometry; no estimate of the final scale weights and no RH conclusion

## 1. Endpoint atom response

Let

\[
 e_T(m)=b_T(m)-b_{T-1}(m),
 \qquad T\ge3,
\tag{L-90027.1}
\]

with zero extension outside the support, and let

\[
 \Gamma_T(q)=v_q(b_T)-v_q(b_{T-1})=v_q(e_T).
\tag{L-90027.2}
\]

PR #265 proves `Gamma_T(q)>0` for every `2<=q<T` because `e_T` is the column response of a nonnegative endpoint row atom.

The new assertion is

\[
\boxed{
 \Gamma_T(q)>2\Gamma_T(4q)
 \qquad(2\le q,\ 4q<T).
}
\tag{L-90027.3}
\]

As usual, set `Gamma_T(q)=0` for `q>=T`; then the weak inequality holds for every column and is strict whenever the right side is active.

## 2. Exact scalar formula

Put

\[
 M=T-1,
 \qquad
 a=2\log{T\over M},
 \qquad
 d=4\left(M^{-1/2}-T^{-1/2}\right).
\tag{L-90027.4}
\]

For every old node `m<=M`,

\[
\boxed{
 e_T(m)=a\sqrt m-dm.
}
\tag{L-90027.5}
\]

At `m=T`, the endpoint increment is zero. Define

\[
 h_k(\varepsilon)
 ={1\over\sqrt{k+\varepsilon}+\sqrt k},
 \qquad
 H_K(\varepsilon)=\sum_{k=1}^{K}h_k(\varepsilon).
\tag{L-90027.6}
\]

For one column put

\[
 \varepsilon={1\over q},
 \qquad
 K=\left\lfloor{M\over q}\right\rfloor.
\tag{L-90027.7}
\]

If `q` does not divide `M`, every active unit interval is complete and

\[
\boxed{
 \Gamma_T(q)=Kd-aq^{-1/2}H_K(\varepsilon).
}
\tag{L-90027.8}
\]

If `q|M`, the formula acquires the endpoint correction

\[
\boxed{
 \Gamma_T(q)=Kd-aq^{-1/2}H_K(\varepsilon)+E_T,
 \qquad
 E_T=a\sqrt T-dT<0.
}
\tag{L-90027.9}
\]

The sign of `E_T` follows from the strict logarithmic-mean bound below.

Write

\[
 K=4L+r,
 \qquad0\le r\le3,
\tag{L-90027.10}
\]

and put

\[
 D_K(\varepsilon)
 =H_K(\varepsilon)-H_L(\varepsilon/4).
\tag{L-90027.11}
\]

The identity

\[
 h_j(\varepsilon/4)=2h_{4j}(\varepsilon)
\tag{L-90027.12}
\]

is exact.

## 3. The divided-difference packet decreases in `epsilon`

Define

\[
 g_k(\varepsilon)=-h_k'(\varepsilon)
 ={1\over
 2\sqrt{k+\varepsilon}
 (\sqrt{k+\varepsilon}+\sqrt k)^2}.
\tag{L-90027.13}
\]

The sequence `g_k` decreases strictly in `k`. Differentiating (L-90027.11), using

\[
 g_j(\varepsilon/4)=8g_{4j}(\varepsilon),
\]

gives

\[
\begin{aligned}
 D_K'(\varepsilon)
 &=-\sum_{k=1}^{K}g_k(\varepsilon)
   +2\sum_{j=1}^{L}g_{4j}(\varepsilon)\\
 &=-\sum_{j=1}^{L}
 [g_{4j-3}+g_{4j-2}+g_{4j-1}-g_{4j}]
   -\sum_{k=4L+1}^{K}g_k<0.
\end{aligned}
\tag{L-90027.14}
\]

Therefore

\[
\boxed{
 D_K(\varepsilon)<D_K(0)
 ={1\over2}(S_K-S_L).
}
\tag{L-90027.15}
\]

This is the finite-unit-cell strengthening of the continuum comparison in `L-90025`.

## 4. The scale coefficient

Put

\[
 \lambda={d\sqrt q\over a}.
\tag{L-90027.16}
\]

The symmetric logarithmic-mean inequality

\[
 \log{T\over M}<{1\over\sqrt{MT}}
\]

gives

\[
\boxed{
 \lambda>
 {2\over\sqrt{M/q}+\sqrt{T/q}}.
}
\tag{L-90027.17}
\]

If `q` does not divide `M`, then `T/q<=K+1`; if `q|M`, then
`M/q=K` and `T/q=K+epsilon<K+1`. In either case

\[
\boxed{
 \lambda>{1\over\sqrt{K+1}}.
}
\tag{L-90027.18}

## 5. Nonboundary columns

Assume `q` does not divide `M`. Since

\[
 \Gamma_T(4q)
 =Ld-a(4q)^{-1/2}H_L(\varepsilon/4),
\]

one has

\[
\begin{aligned}
 \Gamma_T(q)-2\Gamma_T(4q)
 =aq^{-1/2}
 [\lambda(K-2L)-D_K(\varepsilon)].
\end{aligned}
\tag{L-90027.19}
\]

By (L-90027.15)--(L-90027.18), the bracket is strictly larger than

\[
 {K-2L\over\sqrt{K+1}}
 -{1\over2}(S_K-S_L),
\]

which is positive by `L-90025.7` with `n=K,m=L`. This proves (L-90027.3) for every nonboundary column.

## 6. Boundary columns: `r=0`

Assume `q|M` and `K=4L`. Then `4q|M` as well. The two endpoint corrections combine as

\[
 E_T-2E_T=-E_T>0.
\]

The nonboundary core remains positive by the argument of Section 5. Thus the result follows.

## 7. Boundary columns: `r=2,3`

Now `q|M` but `4q` does not divide `M`. The correction `E_T` is adverse. Put

\[
 B_T=-{E_T\over a}={dT\over a}-\sqrt T>0.
\]

Let

\[
 s=\sqrt{T/M}<2.
\]

The logarithmic mean satisfies

\[
 {s-1\over\log s}<{s+1\over2}.
\]

A direct substitution into `B_T` gives

\[
\boxed{
 B_T<{1\over3\sqrt M}.
}
\tag{L-90027.20}
\]

Indeed

\[
 B_T\sqrt M
 ={s\over s^2-1}
 \left({s-1\over\log s}-1\right)
 <{s\over2(s+1)}<{1\over3}.
\]

It remains to lower-bound the core margin. Convex midpoint integration gives

\[
 {1\over2}(S_K-S_L)
 <\sqrt{K+\frac12}-\sqrt{L+\frac12}.
\tag{L-90027.21}
\]

For `K=4L+2`,

\[
 {K-2L\over\sqrt{K+1}}
 -\left(\sqrt{K+\frac12}-\sqrt{L+\frac12}\right)
 >{1\over3\sqrt K}.
\tag{L-90027.22}
\]

After the elementary lower bound

\[
 \sqrt{K+\frac12}-\sqrt{L+\frac12}
 <{3L+2\over3\sqrt{L+1/2}},
\]

squaring (L-90027.22) reduces exactly to

\[
 12L^2+8L-3>0.
\]

For `K=4L+3`, the same argument gives

\[
 {K-2L\over\sqrt{K+1}}
 -\left(\sqrt{K+\frac12}-\sqrt{L+\frac12}\right)
 >{1\over3\sqrt K}.
\tag{L-90027.23}
\]

For `L>=2`, it reduces after squaring to

\[
 12L^2+4L-17>0.
\]

For `L=1`, the direct rational radical bounds

\[
 \sqrt2<{71\over50},
 \quad
 \sqrt{15/2}<{137\over50},
 \quad
 \sqrt{3/2}>{61\over50},
 \quad
 \sqrt7>{132\over50}
\]

give the positive lower remainder

\[
 {40171\over351450}>0.
\]

Combining (L-90027.15), (L-90027.18), (L-90027.20), and
(L-90027.22)--(L-90027.23) shows that the positive core exceeds the adverse endpoint correction.

## 8. Boundary columns: `r=1`

Let `K=4L+1`. Separate the final endpoint term:

\[
 \Gamma_T(q)
 =\sum_{k=1}^{4L}[e_T(kq)-e_T(kq+1)]+e_T(M),
\tag{L-90027.24}
\]

where `e_T(M)=b_T(M)>0`. The first sum minus `2Gamma_T(4q)` equals

\[
 aq^{-1/2}F_L(\varepsilon),
\]

with

\[
\boxed{
 F_L(\varepsilon)
 =4Lh_{4L+1}(\varepsilon)-D_{4L}(\varepsilon).
}
\tag{L-90027.25}
\]

At `epsilon=0`,

\[
 F_L(0)
 ={2L\over\sqrt{4L+1}}
 -{1\over2}(S_{4L}-S_L)>0
\]

by the aligned case of `L-90025`.

Furthermore

\[
 F_L'(\varepsilon)
 =\sum_{j=1}^{L}
 [g_{4j-3}+g_{4j-2}+g_{4j-1}-g_{4j}]
 -4L g_{4L+1}.
\tag{L-90027.26}
\]

The first block is strictly larger than `g_1`, while all later blocks are positive. For `0<=epsilon<=1/2`,

\[
 g_1>{1\over16},
 \qquad
 4L g_{4L+1}< {1\over16\sqrt L}\le{1\over16}.
\]

Thus `F_L'>0`. Hence `F_L(epsilon)>0`, and adding the positive terminal term `e_T(M)` proves the result in the last case.

Sections 5--8 establish (L-90027.3) for every endpoint and column.

## 9. Positive finite column renewal

Define the exact radix-four detail

\[
\boxed{
 \Xi_T(q)=\Gamma_T(q)-2\Gamma_T(4q).
}
\tag{L-90027.27}
\]

Then

\[
 \Xi_T(q)>0\qquad(2\le q<T).
\]

Iterating (L-90027.27) gives the finite positive renewal expansion

\[
\boxed{
 \Gamma_T(q)
 =\sum_{j\ge0}2^j\Xi_T(4^jq),
}
\tag{L-90027.28}
\]

where the sum stops as soon as `4^j q>=T`.

Thus every nonnegative endpoint atom `a_T` has a second exact positive coordinate:

```text
endpoint scale T
x
radix-four column block 4^j q.
```

This is the finite counterpart of `varrho=sum eta_4` from `L-90025`; no continuum limit or asymptotic sign is used.

## 10. Consequence for the closing programme

The first factor of the preferred factor-64 state now has matching positivity on both sides:

```text
continuum endpoint law:
    (1-S^2)varrho = eta_4 > 0;

finite endpoint response matrix:
    Gamma_T(q)-2Gamma_T(4q) = Xi_T(q) > 0.
```

Together with `L-90026`, the radix-four block has a Gamma martingale at continuum level and an exact nonnegative column packet at finite level. The remaining work is no longer to create positivity: it is to lift the two first-order detail filters through these positive packets with subcritical signed score loss.

## 11. Proof boundary

Closed exactly, subject to independent review:

1. the scalar endpoint-response formula;
2. monotonicity of the divided-difference packet in the unit-cell parameter;
3. all nonboundary columns;
4. all four boundary quotient classes;
5. strict positivity of the radix-four column detail;
6. the finite positive renewal expansion.

Still open:

1. a positive/martingale lift through the remaining ordinary and critical Haar details;
2. a subcritical endpoint-scale score-loss bound;
3. the factor-64 endpoint inequality;
4. RH.
