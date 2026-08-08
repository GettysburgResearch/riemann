# L-23823 — Normalized parabolic tails and fixed-ratio shell majorization

Claim ID: `L-23823`  
Title: Every fixed-ratio parabolic carry shell has an exact one-sided continuum transport order, with a quantitative square-root moat  
Status: **PROPOSED COMPLETE ELEMENTARY THEOREM — independent review requested**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Issue: #238  
Dependencies: PR #265 `L-26202` notation and its proved formula for the parabolic cumulative defect  
Scope: continuum carry geometry; no prime-sampling estimate or RH conclusion

## 1. The parabolic defect and its cumulative tail

Retain the continuum parabolic defect

\[
 E(\theta)
 =\sum_{1\le k\le1/\theta}g(k\theta)
  -\theta^{-1/2}\log(1/\theta),
 \qquad 0<\theta\le1,
\tag{L-23823.1}
\]

and put

\[
 H(\theta)=\int_\theta^1E(u)\,du.
\tag{L-23823.2}
\]

`L-26202` proves

\[
 H(\theta)\le0.
\tag{L-23823.3}
\]

On the reciprocal cell

\[
 \frac1{N+1}\le\theta\le\frac1N,
\]

write

\[
 S_N=\sum_{k=1}^Nk^{-1/2},
 \qquad
 A_N=\sum_{k=1}^Nk^{-1/2}\log k.
\]

The exact cell formula is

\[
\begin{aligned}
H_N(\theta)={}&4N\theta-4\\
&+\sqrt\theta\left[
4-4S_N-2A_N-2(S_N+1)\log\theta
\right].
\end{aligned}
\tag{L-23823.4}
\]

## 2. The normalized tail is monotone

Define

\[
 \boxed{J(\theta)=\frac{H(\theta)}{\sqrt\theta}.}
\tag{L-23823.5}
\]

Inside the `N`th reciprocal cell, differentiating (L-23823.4) gives

\[
\boxed{
J_N'(\theta)
=\frac{2}{\theta^{3/2}}
\left[
N\theta+1-(S_N+1)\sqrt\theta
\right].}
\tag{L-23823.6}
\]

The decreasing-sum estimate

\[
 S_N\le1+\int_1^Nx^{-1/2}dx=2\sqrt N-1
\tag{L-23823.7}
\]

implies

\[
N\theta+1-(S_N+1)\sqrt\theta
\ge
(\sqrt{N\theta}-1)^2\ge0.
\tag{L-23823.8}
\]

The cell formulas join continuously at reciprocal endpoints. Therefore

\[
\boxed{J(\theta)\text{ is nondecreasing on }(0,1].}
\tag{L-23823.9}
\]

This is stronger than the unnormalized tail sign (L-23823.3).

## 3. A quantitative derivative moat below one half

For `N>=2`, define

\[
 D_N=2\sqrt N-(S_N+1).
\]

Then

\[
D_{N+1}-D_N
=2(\sqrt{N+1}-\sqrt N)-\frac1{\sqrt{N+1}}>0.
\tag{L-23823.10}
\]

Moreover

\[
D_2=\frac3{\sqrt2}-2>\frac1{10}.
\tag{L-23823.11}
\]

Thus

\[
 S_N+1\le2\sqrt N-\frac1{10}
 \qquad(N\ge2).
\tag{L-23823.12}
\]

Substitution in (L-23823.6) gives, throughout `0<theta<=1/2`,

\[
\begin{aligned}
N\theta+1-(S_N+1)\sqrt\theta
&\ge
(\sqrt{N\theta}-1)^2+\frac1{10}\sqrt\theta,
\end{aligned}
\]

and hence

\[
\boxed{
J'(\theta)\ge\frac1{5\theta}
\qquad(0<\theta\le1/2),}
\tag{L-23823.13}
\]

away from reciprocal knots, with the integrated inequality valid across the
knots.

## 4. Fixed-ratio shell defect

Fix `0<c<1`. Define the continuum shell defect

\[
\boxed{
E_c(\theta)
=E(\theta)
-c^{-1/2}E(\theta/c)\mathbf1_{\theta\le c}.}
\tag{L-23823.14}
\]

This is exactly the defect of the parabolic endpoint layer obtained by
subtracting the endpoint `cX` from the endpoint `X`, after normalization by
`X^{-1/2}`.

Let

\[
 H_c(\theta)=\int_\theta^1E_c(u)\,du.
\tag{L-23823.15}
\]

For `theta>=c`,

\[
 H_c(\theta)=H(\theta).
\tag{L-23823.16}
\]

For `0<theta<c`, changing variables in the dilated term gives

\[
\begin{aligned}
H_c(\theta)
&=H(\theta)-\sqrt c\,H(\theta/c)\\
&=\sqrt\theta\,[J(\theta)-J(\theta/c)].
\end{aligned}
\tag{L-23823.17}
\]

By monotonicity of `J`,

\[
\boxed{
H_c(\theta)\le0
\qquad(0<\theta\le1).}
\tag{L-23823.18}
\]

Thus every fixed-ratio parabolic shell has the same upper-tail defect-to-slack
order as the full parabolic seed.

## 5. Quantitative shell moat

If

\[
0<\theta\le\frac c2,
\]

then the whole interval `[theta,theta/c]` lies below `1/2`. Integrating
(L-23823.13) yields

\[
J(\theta/c)-J(\theta)
\ge\frac15\log(1/c).
\tag{L-23823.19}
\]

Therefore

\[
\boxed{
H_c(\theta)
\le
-\frac15\sqrt\theta\log(1/c)
\qquad(0<\theta\le c/2).}
\tag{L-23823.20}
\]

For the dyadic shell `c=1/2`,

\[
\boxed{
H_{1/2}(\theta)
\le-\frac{\log2}{5}\sqrt\theta
\qquad(0<\theta\le1/4).}
\tag{L-23823.21}
\]

The shell tail also tends to zero at the origin. This follows directly from
(L-23823.4), which gives

\[
H(\theta)=O(\sqrt\theta[1+\log(1/\theta)]).
\]

## 6. Transport interpretation

Write

\[
E_c(\theta)d\theta=\mu_{c,+}-\mu_{c,-}.
\]

Equation (L-23823.18) says

\[
\mu_{c,+}([\theta,1])
\le
\mu_{c,-}([\theta,1])
\qquad(0<\theta<1).
\tag{L-23823.22}
\]

Hence the positive shell defect admits a monotone coupling into negative shell
slack at a greater column scale. The coupling is continuum and source-specific;
it is not a face-count or rank statement.

The finite arithmetic transfer must preserve the logarithmic prime weight and
the prime-sampling error. That separate exact interface is `L-23824`.

## 7. Why this survives the later mutations

- A same-sign rank-`K` Möbius cube changes the source representation but not the
  complete scalar defect `E_c`; no source-rank conclusion is used.
- No reflected Schur reserve appears.
- Positive and negative defect are retained together until the upper-tail
  order is formed.
- The theorem holds for every fixed ratio, so the first `2/3` Mertens shell is
  not discarded.

## 8. Proof boundary

Closed here:

1. normalized-tail monotonicity;
2. a quantitative derivative lower bound;
3. exact fixed-ratio shell tail majorization;
4. a quantitative square-root moat;
5. the continuum monotone transport order.

Open:

1. transfer of the weighted shell-tail order to the finite prime set with
   subpolynomial boundary loss;
2. the prime-ramp estimate;
3. RH.
