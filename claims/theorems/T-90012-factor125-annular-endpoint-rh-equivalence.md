# T-90012 — A factor-125 finite annular inequality with fixed margin is equivalent to RH

Claim ID: `T-90012` (provisional range; branch-qualified)  
Title: The optimized radix-five critical-annular filter yields a pure integer four-scale criterion on `[N,125N]`, retains every off-line zero, and is uniformly negative under RH  
Status: **PROPOSED COMPLETE RH EQUIVALENCE / OPTIMIZED ANNULAR THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Date: 2026-08-10  
Depends on: `L-90016`, `T-90008`; Landau's one-sign theorem  
Scope: optimized fixed-annulus criterion; no unconditional proof of its sign

## 1. Criterion

Define

\[
\begin{aligned}
 \mathcal V_5(X)
 ={}&\sqrt5\,A(X)-(2\sqrt5+1)A(X/5)\\
 &+(\sqrt5+2)A(X/25)-A(X/125).
\end{aligned}
\]

Then the following are equivalent:

1. RH;
2. `V_5(X)<0` for every sufficiently large real `X`;
3. `V_5(X)` is eventually one-signed;
4. there is an `epsilon>0` such that
   \[
   \sqrt5\,A_{125N}
   -(2\sqrt5+1)A_{25N}
   +(\sqrt5+2)A_{5N}-A_N
   \le-\epsilon
   \]
   for every sufficiently large integer `N`.

RH gives the explicit margin

\[
\boxed{
 \mathcal V_5(X)<-0.1
}
\tag{T-90012.1}
\]

for every sufficiently large `X`.

## 2. RH-side bound

The unscaled radix-five moat and zero bounds of `L-90016` are

\[
 C_5
 ={1+\zeta(1/2)\over2}
 (1-5^{-1/2})(\log5)^2
 =-0.32958558866578774368\ldots,
\]

and

\[
 Z_5
 =4(1+5^{-1/2})(\log\xi)''(1/2)
 =0.26750288128453810713\ldots .
\]

Thus

\[
 C_5+Z_5
 =-0.06208270738124963655\ldots .
\]

After multiplication by `sqrt(5)`,

\[
\boxed{
 \limsup_{X\to\infty}\mathcal V_5(X)
 \le-0.13882115393170214001\ldots .
}
\tag{T-90012.2}
\]

This proves (T-90012.1).

## 3. Converse

The Mellin multiplier of the unscaled filter is

\[
 (1-5^{-z})^2(1-5^{-z-1/2}).
\]

If `rho` is an off-line zero and `z_rho=rho-1/2`, then `|5^{-z_rho}|<1`. The multiplier roots have modulus one or `sqrt(5)>1`, so the pole at `z_rho` survives. There is no positive-real singularity.

Therefore eventual one-sidedness of `V_5(e^t)` contradicts Landau's theorem in the presence of any off-line zero. Functional-equation symmetry gives RH.

This proves the equivalence of items 1--3.

## 4. Integer-scale form

At `X=125N`, all four endpoints are integers:

\[
 \mathcal V_5(125N)
 =\sqrt5\,A_{125N}
 -(2\sqrt5+1)A_{25N}
 +(\sqrt5+2)A_{5N}-A_N.
\]

The bounded-step interpolation of `L-90004.24` shows that a fixed eventual margin on this sequence extends to the real half-line. Hence item 4 is equivalent to the first three.

By `L-90016`, the finite radical-switching representation uses only the annulus

\[
\boxed{N<m\le125N.}
\tag{T-90012.3}
\]

This is the narrowest integer-radix annulus presently supplied with a phase-blind theorem-grade RH margin.

## 5. Finite reconnaissance

`X-90016` checked every aligned endpoint `X=125N` through five million:

```text
aligned endpoints tested: 40,000;
nonnegative endpoints:    X=125 only;
all X=125N from 250 through 5,000,000: negative;
minimum unscaled value:   -0.5083854021... at X=5,125;
last unscaled value:      -0.3222706704... at X=5,000,000.
```

The first endpoint correction is a finite-base fact and has no bearing on the eventual theorem. This evidence is not used in the proof.

## 6. Frontier

The optimized open theorem is now

\[
\boxed{
 \sqrt5\,A_{125N}
 -(2\sqrt5+1)A_{25N}
 +(\sqrt5+2)A_{5N}-A_N<0
 \quad(N\gg1).
}
\tag{T-90012.4}
\]

It is a fixed factor-125 arithmetic statement, has a strict RH-side margin, and loses no off-line zero. Proving it unconditionally would prove RH.

## 7. Proof boundary

Closed, subject to independent review:

1. RH implies the fixed negative margin;
2. eventual one-sign implies RH;
3. real and integer fixed-margin forms are equivalent;
4. exact factor-125 annular support;
5. minimal integer-radix status within the phase-blind cubic family.

Still open:

1. unconditional proof of (T-90012.4);
2. RH.

Replay: `experiments/X-90016-radix5-annular/verify.py`.
