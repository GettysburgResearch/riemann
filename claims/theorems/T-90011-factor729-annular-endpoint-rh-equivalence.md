# T-90011 — A fixed factor-729 annular inequality is equivalent to RH with a strict margin

Claim ID: `T-90011` (provisional range; branch-qualified)  
Title: The 3–7–5–1 endpoint filter retains every off-line zero, while under RH its critical-line zero series is uniformly smaller than the explicit negative prime-square moat  
Status: **PROPOSED COMPLETE RH EQUIVALENCE / CONDITIONAL MARGIN THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Date: 2026-08-10  
Depends on: `L-90004`, `T-90008`, `L-90015`; Hadamard factorization of `xi`; Landau's one-sign theorem  
Scope: one fixed annular scalar; no unconditional sign and no proof of RH

## 1. Statement

Retain

\[
 \mathcal U_9(X)
 =3A(X)-7A(X/9)+5A(X/81)-A(X/729).
\]

The following are equivalent:

1. RH;
2. `U_9(X)<0` for every sufficiently large real `X`;
3. `U_9(X)` is eventually one-signed;
4. there is an `epsilon>0` such that
   \[
   3A_{729N}-7A_{81N}+5A_{9N}-A_N\le-\epsilon
   \]
   for every sufficiently large integer `N`.

Moreover RH implies the explicit robust form

\[
\boxed{
 \mathcal U_9(X)<-1.4
}
\tag{T-90011.1}
\]

for every sufficiently large `X`. Thus one may take `epsilon=1.4` in item 4.

## 2. RH explicit formula

Let

\[
 Q_9(z)=3-7\,9^{-z}+5\,9^{-2z}-9^{-3z}
 =(1-9^{-z})^2(3-9^{-z}).
\]

`T-90008` gives under RH, for every fixed `0<eta<1/6`,

\[
 A(X)
 ={1+\zeta(1/2)\over4}\log^2X
 +C_1\log X+C_0
 +\sum_\rho{m_\rho X^{\rho-1/2}\over(\rho-1/2)^2}
 +O_\eta(X^{-\eta}\log^2(2X)).
\]

Applying the filter and using `Q_9(0)=Q_9'(0)=0` gives

\[
\boxed{
\begin{aligned}
 \mathcal U_9(X)
 ={}&C_9\\
 &+\sum_\rho
 {m_\rho Q_9(\rho-1/2)\over(\rho-1/2)^2}
 X^{\rho-1/2}\\
 &+O_\eta(X^{-\eta}\log^2(2X)),
\end{aligned}}
\tag{T-90011.2}
\]

where

\[
 C_9=(1+\zeta(1/2))(\log9)^2
 =-2.22249758405246967649\ldots .
\tag{T-90011.3}
\]

## 3. Exact total mass of the critical-line zero coefficients

Put

\[
 \xi(s)={1\over2}s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]

Under RH the centered Hadamard product gives

\[
 \xi(1/2+z)
 =\xi(1/2)
 \prod_{\gamma>0}
 \left(1+{z^2\over\gamma^2}\right)^{m_\gamma}.
\]

Therefore

\[
\boxed{
 \Sigma_\xi
 :=(\log\xi)''(1/2)
 =\sum_\rho{m_\rho\over\gamma_\rho^2}
 =0.04620998623083794157\ldots .
}
\tag{T-90011.4}
\]

The sum on the right counts both conjugate zeros with multiplicity.

For `rho=1/2+i gamma`, put `y=9^{-i gamma}`, so `|y|=1`. Then

\[
 |Q_9(i\gamma)|
 =|1-y|^2|3-y|
 \le4\cdot4=16.
\tag{T-90011.5}
\]

Consequently the entire critical-line zero series in (T-90011.2) satisfies the uniform bound

\[
\boxed{
 \left|\sum_\rho
 {m_\rho Q_9(i\gamma)\over(i\gamma)^2}
 X^{i\gamma}\right|
 \le16\Sigma_\xi
 =0.73935977969340706524\ldots .
}
\tag{T-90011.6}
\]

Combining (T-90011.3) and (T-90011.6),

\[
 C_9+16\Sigma_\xi
 =-1.48313780435906261125\ldots<-1.48.
\tag{T-90011.7}
\]

The remainder in (T-90011.2) tends to zero. Hence RH implies (T-90011.1).

This is stronger than an unspecified eventual sign: the deterministic moat dominates the complete critical-line zero series by an explicit fixed amount.

## 4. Eventual one-sidedness implies RH

By `L-90015`,

\[
 \widehat{\mathcal U_9}(z)=Q_9(z)\widehat A(z),
\]

where here `Q_9(z)` abbreviates the scale multiplier

\[
 Q_9(z)=3-7\,9^{-z}+5\,9^{-2z}-9^{-3z}.
\]

If `rho` is a hypothetical zero with `Re rho>1/2`, then

\[
 |9^{-(\rho-1/2)}|<1.
\]

The roots of `(1-y)^2(3-y)` are `1` and `3`, so the off-line pole of `Ahat` at `rho-1/2` survives. The filtered transform has no singularity on the open positive real axis: the main pole at `s=1` already cancels in `Ahat`, the origin lies on the boundary, and every further prime-zeta copy lies in `Re z<=0`.

If `U_9(e^t)` were eventually one-signed, change sign if needed and alter it on a compact interval to obtain a nonnegative function. Landau's one-sign theorem would force a singularity at the real abscissa of convergence. The positive-real pole audit forbids it, while the surviving off-line pole forces positive abscissa. This contradiction excludes every zero to the right of the critical line. Functional-equation symmetry gives RH.

Thus

\[
\boxed{
 \mathcal U_9(X)\text{ eventually one-signed}
 \Longrightarrow\mathrm{RH}.
}
\tag{T-90011.8}
\]

Together with Section 3 this proves the equivalence of items 1--3.

## 5. Pure integer annular criterion

At `X=729N`, `L-90015` gives the exact finite identity

\[
 \mathcal U_9(729N)=3A_{729N}-7A_{81N}+5A_{9N}-A_N.
\tag{T-90011.9}
\]

`L-90004.24` gives bounded-step interpolation

\[
 A(X)-A(\lfloor X\rfloor)
 =O\left({\log(2X)\over\sqrt X}\right).
\]

Summing this estimate over at most 729 adjacent endpoint intervals and over the four fixed scales shows

\[
 \sup_{729N\le X\le729(N+1)}
 |\mathcal U_9(X)-\mathcal U_9(729N)|=o(1).
\tag{T-90011.10}
\]

Therefore an eventual fixed negative margin on the integer sequence (T-90011.9) implies eventual negativity on the full real half-line and hence RH by Section 4. Conversely RH supplies the margin `1.4` by Section 3.

This proves the equivalence with item 4.

## 6. Finite reconnaissance

`X-90015` evaluates `A_N` by exact radical switching and checks every multiple of 729 through the retained endpoint `5,000,000`.

```text
multiples tested: 6,858;
maximum value:     -1.3302554743085073 at X=729;
minimum value:     -2.8176255274546094 at X=199,017;
last value:        -2.4858667332464393 at X=4,999,482.
```

The checker also reconstructs selected values directly from the annular formula (L-90015.9). The finite scan is not used to infer the cofinal sign.

## 7. Strategic consequence

The criterion has three simultaneous features not present together in the earlier front doors:

```text
fixed finite arithmetic window: [N,729N];
all off-line zeros retained;
under-RH sign margin bounded away from zero.
```

The remaining theorem can therefore be posed as one scale-stationary annular inequality:

\[
\boxed{
 3A_{729N}-7A_{81N}+5A_{9N}-A_N<0
 \quad(N\gg1).
}
\tag{T-90011.11}
\]

A proof with any fixed negative margin would prove RH. The present theorem proves the reverse implication and exposes the exact moat available to such a proof; it does not prove (T-90011.11) unconditionally.

## 8. Proof boundary

Closed, subject to independent review:

1. the filtered explicit formula;
2. the exact critical-zero square mass;
3. the absolute zero-series bound;
4. the strict RH-side margin;
5. the direct Landau converse;
6. the all-real / integer-margin equivalence;
7. the fixed-annulus formulation.

Still open:

1. an unconditional proof of the annular inequality;
2. RH.

Replay: `experiments/X-90015-annular-endpoint/verify.py`.
