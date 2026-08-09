# L-90016 — The critical-annular filter family and the minimal certified integer radix

Claim ID: `L-90016` (provisional range; branch-qualified)  
Title: Every radix carries a unique cubic filter which kills the two logarithmic modes and the critical seed mode; its RH margin is monotone in the radix and first becomes phase-blind positive at integer radix five  
Status: **PROPOSED COMPLETE EXACT FILTER/MARGIN LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Date: 2026-08-10  
Depends on: `L-90004`, `L-90015`, `T-90011`  
Scope: general filter algebra and optimization; no unconditional endpoint sign

## 1. The unique cubic critical-annular filter

Fix a real radix `R>1`, put

\[
 q=R^{-1/2},
\]

and define

\[
\boxed{
 P_R(y)=(1-y)^2(1-qy)
 =1-(2+q)y+(1+2q)y^2-qy^3.
}
\tag{L-90016.1}
\]

For the endpoint scalar `A(X)`, put

\[
\boxed{
\begin{aligned}
 \mathcal U_R(X)
 ={}&A(X)-(2+q)A(X/R)\\
 &+(1+2q)A(X/R^2)-qA(X/R^3).
\end{aligned}}
\tag{L-90016.2}
\]

The coefficient vector satisfies

\[
 \sum_{j=0}^3a_j=0,
 \qquad
 \sum_{j=0}^3ja_j=0,
 \qquad
 \sum_{j=0}^3a_jR^{j/2}=0.
\tag{L-90016.3}
\]

Therefore the proof of `L-90015` applies verbatim:

\[
\boxed{
 \mathcal U_R(X)
 \text{ has exact radical/ramp support in }
 (X/R^3,X].
}
\tag{L-90016.4}
\]

The polynomial is unique up to scalar among cubic filters with a double root at the neutral scale mode `y=1` and a root at the critical seed mode `y=sqrt(R)`.

## 2. Transform and moat constant

The Mellin multiplier is

\[
\boxed{
 \widehat{\mathcal U_R}(z)
 =P_R(R^{-z})\widehat A(z).
}
\tag{L-90016.5}
\]

Near `z=0`,

\[
 P_R(R^{-z})
 =(1-R^{-1/2})(\log R)^2z^2+O(z^3).
\]

Since

\[
 \widehat A(z)
 ={1+\zeta(1/2)\over2z^3}+O(z^{-2}),
\]

the filtered prime-power moat is

\[
\boxed{
 C_R
 ={1+\zeta(1/2)\over2}
 (1-R^{-1/2})(\log R)^2<0.
}
\tag{L-90016.6}
\]

For a hypothetical off-line zero `z_rho=rho-1/2` one has `|R^{-z_rho}|<1`, whereas the roots of `P_R` are `1` and `sqrt(R)>1`. Thus no off-line zero is canceled for any `R>1`.

## 3. Phase-blind RH margin

Under RH, put

\[
 \Sigma_\xi=(\log\xi)''(1/2)
 =0.04620998623083794157\ldots .
\]

On the unit circle,

\[
 |P_R(y)|
 =|1-y|^2|1-qy|
 \le4(1+q).
\]

Hence the complete critical-line zero contribution is bounded absolutely by

\[
\boxed{
 Z_R=4(1+R^{-1/2})\Sigma_\xi.
}
\tag{L-90016.7}
\]

The phase-blind certified margin is

\[
\boxed{
 \mathfrak m(R)
 =-C_R-Z_R.
}
\tag{L-90016.8}
\]

If `m(R)>0`, then RH gives

\[
 \limsup_{X\to\infty}\mathcal U_R(X)
 \le-\mathfrak m(R)<0.
\tag{L-90016.9}
\]

## 4. Monotonicity of the certified margin

Write

\[
 a=-{1+\zeta(1/2)\over2}>0,
 \qquad S=\Sigma_\xi>0.
\]

Then

\[
 \mathfrak m(R)
 =a(1-R^{-1/2})(\log R)^2
 -4S(1+R^{-1/2}).
\]

Direct differentiation gives

\[
\begin{aligned}
 \mathfrak m'(R)
 ={}&a\left[
 {R^{-3/2}\over2}(\log R)^2
 +{2(1-R^{-1/2})\log R\over R}
 \right]\\
 &+2S R^{-3/2}>0
 \qquad(R>1).
\end{aligned}
\tag{L-90016.10}
\]

Thus the phase-blind margin is strictly increasing with the radix.

Numerically, with broad retained intervals,

\[
 \mathfrak m(4)
 =-0.1121600546\ldots<0,
\]

while

\[
\boxed{
 \mathfrak m(5)
 =0.06211115903708618\ldots>0.
}
\tag{L-90016.11}
\]

Therefore:

\[
\boxed{
 R=5
 \text{ is the smallest integer radix certified by the absolute-zero bound.}
}
\tag{L-90016.12}
\]

This is a statement about this phase-blind proof. It does not refute a sharper phase-sensitive theorem at radix four.

## 5. The optimized integer filter

For `R=5`, multiply (L-90016.2) by `sqrt(5)` and define

\[
\boxed{
\begin{aligned}
 \mathcal V_5(X)
 ={}&\sqrt5\,A(X)-(2\sqrt5+1)A(X/5)\\
 &+(\sqrt5+2)A(X/25)-A(X/125).
\end{aligned}}
\tag{L-90016.13}
\]

At `X=125N` this is the pure integer-scale expression

\[
\boxed{
 \mathcal V_5(125N)
 =\sqrt5\,A_{125N}
 -(2\sqrt5+1)A_{25N}
 +(\sqrt5+2)A_{5N}-A_N.
}
\tag{L-90016.14}
\]

It depends only on radical/ramp data in `[N,125N]`.

The scaled RH-side margin is

\[
\boxed{
 \sqrt5\,\mathfrak m(5)
 =0.13888471955955921\ldots .
}
\tag{L-90016.15}
\]

## 6. Proof boundary

Closed exactly, subject to review:

1. the general cubic filter and its uniqueness;
2. exact factor-`R^3` annularization;
3. the moat and zero-series bounds;
4. strict monotonicity of the certified margin;
5. minimality of integer radix five for this proof;
6. the factor-125 integer-scale filter.

Still open:

1. unconditional sign of the radix-five annular scalar;
2. a phase-sensitive radix-four result;
3. RH.
