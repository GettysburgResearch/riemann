# T-90015 — The improved rational factor-64 annular inequality is equivalent to RH

Claim ID: `T-90015` (provisional range; branch-qualified)  
Title: The zero-safe rational unit-circle dressing gives a seven-scale criterion on `[N,64N]` with a fixed aligned RH margin exceeding `0.13`  
Status: **PROPOSED COMPLETE RH EQUIVALENCE / IMPROVED FIXED-MARGIN THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Date: 2026-08-10  
Depends on: `L-90022`, `T-90008`; Landau's one-sign theorem  
Scope: improved factor-64 fixed-annulus criterion; no unconditional proof of its sign

## 1. Criterion

Define

\[
\begin{aligned}
 \mathcal V_{64}^*(X)={}&4\sqrt2 A(X)
 -(4+\sqrt2)A(X/2)\\
 &+(1-3\sqrt2)A(X/4)
 +(3-3\sqrt2)A(X/8)\\
 &+(3-\sqrt2)A(X/16)
 +(1+4\sqrt2)A(X/32)-4A(X/64).
\end{aligned}
\tag{T-90015.1}

Then the following are equivalent:

1. RH;
2. `V_64^*(X)<0` for every sufficiently large real `X`;
3. `V_64^*(X)` is eventually one-signed;
4. there exists `epsilon>0` such that
   \[
   \begin{aligned}
   4\sqrt2 A_{64N}-(4+\sqrt2)A_{32N}
   +(1-3\sqrt2)A_{16N}\\
   +(3-3\sqrt2)A_{8N}+(3-\sqrt2)A_{4N}\\
   +(1+4\sqrt2)A_{2N}-4A_N\le-\epsilon
   \end{aligned}
   \]
   for every sufficiently large integer `N`.

Moreover RH implies

\[
\boxed{
 \mathcal V_{64}^*(X)<-0.13
}
\tag{T-90015.2}

for every sufficiently large `X`.

## 2. RH-side margin

`L-90022` proves that the unscaled filter has deterministic moat

\[
 C_{64}^*<-0.178
\]

and exact unit-circle norm

\[
 \max_{|y|=1}|P_{64}^*(y)|<\sqrt{11}.
\]

Under RH the complete critical-line zero series is therefore bounded by

\[
 \sqrt{11}(\log\xi)''(1/2)<0.154.
\]

Hence

\[
\boxed{
 \limsup_{X\to\infty}\mathcal U_{64}^*(X)<-0.024.
}
\tag{T-90015.3}

Multiplication by `4sqrt(2)` gives

\[
\boxed{
 \limsup_{X\to\infty}\mathcal V_{64}^*(X)<-0.13.
}
\tag{T-90015.4}

This proves (T-90015.2).

## 3. Converse

The Mellin multiplier is

\[
 4\sqrt2 P_{64}^*(2^{-z}).
\]

Its roots are the double root `1`, the critical root `sqrt(2)`, the root `-1`, and the two conjugate roots of

\[
 y^2+{3\over4}y+1.
\]

The latter pair lies on the unit circle. Thus every multiplier root has modulus at least one.

If `rho` is a hypothetical nontrivial zero with `Re rho>1/2`, then

\[
 |2^{-(\rho-1/2)}|<1,
\]

so the pole at `rho-1/2` survives. The filtered transform has no singularity on the open positive real axis.

If `V_64^*(e^t)` were eventually one-signed, Landau's one-sign theorem would force a positive-real singularity at its abscissa of convergence in the presence of the surviving off-line pole. This contradicts the pole audit. Therefore eventual one-sidedness implies RH.

Together with Section 2, items 1--3 are equivalent.

## 4. Integer-scale form

At `X=64N`, all seven scales are integers and the expression in item 4 is exact. The bounded-step interpolation of `L-90004.24` shows that a fixed eventual margin on the aligned sequence extends to the full real half-line. Conversely RH supplies the margin `0.13`. Hence item 4 is equivalent to the first three.

`L-90022` gives exact arithmetic support

\[
\boxed{N<m\le64N.}
\tag{T-90015.5}

## 5. Relation to the minimality theorem

`L-90020` proves that no phase-blind integer-radix polynomial filter can have annulus factor below 64. `L-90019/T-90014` attain that factor with the simplest cyclotomic dressing. The present theorem retains the same minimal annulus and zero safety while providing a much larger theorem-grade margin.

Thus the roles are:

```text
T-90014: simplest minimal-annulus equivalence;
T-90015: preferred minimal-annulus producer.
```

## 6. Preferred open theorem

The conclusion-producing inequality is

\[
\boxed{
\begin{aligned}
 4\sqrt2 A_{64N}-(4+\sqrt2)A_{32N}
 +(1-3\sqrt2)A_{16N}\\
 +(3-3\sqrt2)A_{8N}+(3-\sqrt2)A_{4N}\\
 +(1+4\sqrt2)A_{2N}-4A_N<0
 \qquad(N\gg1).
\end{aligned}}
\tag{T-90015.6}

It is supported on the minimal annulus `[N,64N]`, has a fixed aligned RH-side margin exceeding `0.13`, and cannot miss any off-line zero. Proving it unconditionally would prove RH.

## 7. Proof boundary

Closed, subject to independent review:

1. RH implies the fixed negative margin;
2. eventual one-sign implies RH;
3. real and aligned-integer fixed-margin forms are equivalent;
4. exact factor-64 support and zero safety;
5. relation to phase-blind minimality.

Still open:

1. unconditional proof of (T-90015.6);
2. RH.

Replay: `experiments/X-90019-factor64-rational/verify.py`.
