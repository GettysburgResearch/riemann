# T-90013 — A factor-81 annular inequality with an exact fixed margin is equivalent to RH

Claim ID: `T-90013` (provisional range; branch-qualified)  
Title: The zero-safe radix-three quartic filter gives a five-scale integer criterion on `[N,81N]`, with an exact Bernstein-certified RH margin and a direct Landau converse  
Status: **PROPOSED COMPLETE RH EQUIVALENCE / EXACT-MARGIN THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Date: 2026-08-10  
Depends on: `L-90017`, `T-90008`; Landau's one-sign theorem  
Scope: factor-81 fixed-annulus criterion; no unconditional proof of its sign

## 1. Criterion

Define

\[
\begin{aligned}
 \mathcal V_3(X)
={}&3A(X)-(3+\sqrt3)A(X/3)\\
&+(-3+\sqrt3)A(X/9)\\
&+(3+\sqrt3)A(X/27)-\sqrt3 A(X/81).
\end{aligned}
\tag{T-90013.1}
\]

Then the following are equivalent:

1. RH;
2. `V_3(X)<0` for every sufficiently large real `X`;
3. `V_3(X)` is eventually one-signed;
4. there exists `epsilon>0` such that
   \[
   \begin{aligned}
   3A_{81N}-(3+\sqrt3)A_{27N}
   +(-3+\sqrt3)A_{9N}\\
   +(3+\sqrt3)A_{3N}-\sqrt3 A_N
   \le-\epsilon
   \end{aligned}
   \]
   for every sufficiently large integer `N`.

Moreover RH implies

\[
\boxed{
 \mathcal V_3(X)<-0.1
}
\tag{T-90013.2}
\]

for every sufficiently large `X`.

## 2. RH-side margin

`L-90017` gives the unscaled prime-power moat

\[
 C_3=-0.2348344907443489\ldots
\]

and the exact phase-blind critical-zero bound

\[
 Z_3\le\sqrt{18}(\log\xi)''(1/2)
 =0.1960499542311713\ldots .
\]

Therefore

\[
 C_3+Z_3
 =-0.0387845365131775\ldots<0.
\]

After multiplying by three,

\[
\boxed{
 \limsup_{X\to\infty}\mathcal V_3(X)
 \le-0.1163536095395325\ldots .
}
\tag{T-90013.3}
\]

This proves (T-90013.2). The bound is theorem-grade because the only unit-circle estimate is the exact Bernstein certificate `|P_3|^2<18` from `L-90017`.

## 3. Converse

The Mellin multiplier is

\[
 3P_3(3^{-z})
 =3(1-3^{-z})^2(1-3^{-z-1/2})(1+3^{-z}).
\]

If `rho` is a hypothetical zero with `Re rho>1/2`, then

\[
 |3^{-(\rho-1/2)}|<1.
\]

The multiplier roots have moduli `1` or `sqrt(3)>1`. Hence the pole at `rho-1/2` survives. The filtered transform has no singularity on the open positive real axis.

If `V_3(e^t)` were eventually one-signed, Landau's one-sign theorem would force a positive-real singularity at its abscissa of convergence in the presence of the surviving off-line pole. This contradicts the pole audit. Thus eventual one-sidedness implies RH.

Together with Section 2, items 1--3 are equivalent.

## 4. Integer-scale form

At `X=81N`, all five scales are integral:

\[
\boxed{
\begin{aligned}
 \mathcal V_3(81N)
={}&3A_{81N}-(3+\sqrt3)A_{27N}\\
&+(-3+\sqrt3)A_{9N}\\
&+(3+\sqrt3)A_{3N}-\sqrt3 A_N.
\end{aligned}}
\tag{T-90013.4}
\]

By the bounded-step interpolation of `L-90004.24`, a fixed eventual margin on this sequence extends to the real half-line. Conversely RH gives the margin `0.1`. Hence item 4 is equivalent to the first three.

`L-90017` identifies the exact finite arithmetic support:

\[
\boxed{N<m\le81N.}
\tag{T-90013.5}
\]

This improves the factor-125 four-scale criterion by one extra scale and a narrower zero-safe annulus.

## 5. Finite reconnaissance

`X-90017` checked every aligned endpoint `X=81N` through five million:

```text
aligned endpoints tested: 61,728;
nonnegative endpoints:     46;
last nonnegative endpoint:  6,399;
all aligned endpoints after 6,399 through the retained maximum: negative;
maximum unscaled value:     0.1630236226... at X=324;
minimum unscaled value:    -0.3955141969... at X=353,241;
last unscaled value:       -0.2435548082... at X=4,999,968.
```

The finite exceptions are compatible with an eventual theorem and are not used in the proof.

## 6. Optimized open target

The conclusion-producing statement is now the fixed factor-81 inequality

\[
\boxed{
\begin{aligned}
 3A_{81N}-(3+\sqrt3)A_{27N}
 +(-3+\sqrt3)A_{9N}\\
 +(3+\sqrt3)A_{3N}-\sqrt3 A_N<0
 \qquad(N\gg1).
\end{aligned}}
\tag{T-90013.6}
\]

It is supported on `[N,81N]`, has a fixed negative RH-side margin, and cannot miss any off-line zero. Proving it unconditionally would prove RH.

## 7. Proof boundary

Closed, subject to independent review:

1. RH implies a fixed margin exceeding `0.1`;
2. eventual one-sign implies RH;
3. real and aligned-integer margin forms are equivalent;
4. exact factor-81 support;
5. finite exceptions are isolated as reconnaissance only.

Still open:

1. unconditional proof of (T-90013.6);
2. RH.

Replay: `experiments/X-90017-radix3-quartic/verify.py`.
