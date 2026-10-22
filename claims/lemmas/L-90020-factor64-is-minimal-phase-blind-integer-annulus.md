# L-90020 — Factor 64 is the minimal phase-blind integer-radix annulus

Claim ID: `L-90020` (provisional range; branch-qualified)  
Title: No finite integer-radix polynomial filter with annulus factor below 64 can satisfy the three critical cancellation moments and dominate the complete critical-line zero series by an absolute norm bound  
Status: **PROPOSED COMPLETE EXACT MINIMALITY/FIREWALL THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Date: 2026-08-10  
Depends on: `L-90016`, `L-90019`; the exact constant corridors in `X-90018`  
Scope: minimality inside the phase-blind absolute-zero-sum polynomial-filter class; no claim against phase-sensitive or nonpolynomial mechanisms

## 1. Admissible phase-blind filters

Fix an integer radix `R>=2`. Every polynomial filter satisfying

\[
 P(1)=P'(1)=P(\sqrt R)=0
\]

has the factorization

\[
\boxed{
 P(y)=(1-y)^2(1-R^{-1/2}y)Q(y).
}
\tag{L-90020.1}

Write

\[
 B_R(y)=(1-y)^2(1-R^{-1/2}y).
\]

The origin moat per unit `Q(1)` is

\[
 K_R
 =-{1+\zeta(1/2)\over2}
 (1-R^{-1/2})(\log R)^2>0.
\tag{L-90020.2}
\]

Under RH, the phase-blind absolute estimate bounds the zero series by

\[
 \Sigma_\xi\|B_RQ\|_{L^\infty(|y|=1)},
 \qquad
 \Sigma_\xi=(\log\xi)''(1/2).
\]

After harmless scalar normalization `Q(1)=1`, a positive certified margin requires

\[
\boxed{
 \|B_RQ\|_\infty<{K_R\over\Sigma_\xi}.
}
\tag{L-90020.3}
\]

## 2. Radix two: every degree-at-most-two dressing fails

For `R=2`, the retained exact constant corridors give

\[
\boxed{
 {K_2\over\Sigma_\xi}<0.71.
}
\tag{L-90020.4}

Suppose `deg Q<=2`, `Q(1)=1`, and (L-90020.3) holds. Put

\[
 v_0=Q(1),
 \quad v_1=Q(i),
 \quad v_2=Q(-1),
 \quad v_3=Q(-i).
\]

At the three relevant fourth roots of unity,

\[
 |B_2(-1)|=4(1+1/\sqrt2)>6.8,
\tag{L-90020.5}
\]

and

\[
 |B_2(i)|=|B_2(-i)|=\sqrt6>2.44.
\tag{L-90020.6}

Thus (L-90020.3)--(L-90020.6) imply

\[
 |v_2|<{0.71\over6.8},
 \qquad
 |v_1|,|v_3|<{0.71\over2.44}.
\tag{L-90020.7}

But every polynomial of degree at most two satisfies the exact four-point DFT identity

\[
\boxed{
 Q(1)+iQ(i)-Q(-1)-iQ(-i)=0.
}
\tag{L-90020.8}

Indeed the left side annihilates the monomials `1,y,y^2` separately. Since `v_0=1`,

\[
\begin{aligned}
 1-|v_2|
 &\le |1-v_2|\\
 &=|i(v_3-v_1)|\\
 &\le |v_1|+|v_3|.
\end{aligned}
\tag{L-90020.9}

The bounds (L-90020.7) make the left side greater than

\[
 1-{0.71\over6.8}>0.895,
\]

while the right side is less than

\[
 {2\cdot0.71\over2.44}<0.582.
\]

This contradiction proves

\[
\boxed{
 R=2,\quad\deg P\le5
 \Longrightarrow
 \text{no positive phase-blind margin}.}
\tag{L-90020.10}

No zero-safety assumption was needed for this no-go; it applies to every real or complex dressing polynomial of degree at most two.

## 3. Other integer radices below factor 64

The three prescribed roots force `deg P>=3`. If the annulus factor `R^(deg P)` is below 64, the only remaining integer-radix possibility is

```text
R=3, deg P=3, factor 27.
```

At degree three, the filter is unique up to scalar and is precisely the cubic member of `L-90016`. That theorem proves its phase-blind margin is strictly increasing in `R` and still negative at `R=4`; hence it is negative at `R=3`.

For `R>=4`, degree at least three already gives annulus factor at least 64.

Therefore

\[
\boxed{
 R^{\deg P}<64
 \Longrightarrow
 \text{no positive phase-blind margin}.}
\tag{L-90020.11}

## 4. Attainment at factor 64

`L-90019` supplies the radix-two degree-six filter

\[
 P_{64}(y)
 =(1-y)^2(1-y/\sqrt2)(1+y)(1+y+y^2),
\]

with exact factor-64 support and

\[
 \max_{|y|=1}|P_{64}(y)|<4.
\]

Its deterministic moat exceeds `0.194` in magnitude, while the critical-zero absolute bound is below `0.185`. Hence its phase-blind margin is strictly positive.

Combining with (L-90020.11),

\[
\boxed{
 64
 \text{ is the minimal integer annulus factor in this proof class}.}
\tag{L-90020.12}

## 5. Scope firewall

The minimality applies to filters which:

1. are finite polynomials in one integer-radix scale shift;
2. cancel the two neutral modes and the critical seed mode;
3. prove the RH side using the phase-blind bound
   `sup_|y|=1 |P(y)| * Sigma_xi`.

It does not rule out:

```text
phase-sensitive use of the actual zero ordinates;
nonpolynomial scale filters;
several incommensurable radices;
a direct arithmetic proof with no absolute zero-sum majorant.
```

## 6. Proof boundary

Closed exactly:

1. the phase-blind margin condition;
2. the radix-two degree-five DFT obstruction;
3. exclusion of every integer annulus below 64;
4. attainment by the cyclotomic factor-64 filter;
5. precise scope of the minimality claim.

Still open:

1. unconditional sign of the factor-64 endpoint;
2. RH.
