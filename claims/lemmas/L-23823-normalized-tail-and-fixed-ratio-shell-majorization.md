# L-23823 — Normalized parabolic tails and fixed-ratio shell majorization

Claim ID: `L-23823`  
Title: Every fixed-ratio parabolic carry shell has an exact one-sided continuum transport order, with a quantitative square-root moat  
Status: **PROPOSED COMPLETE ELEMENTARY THEOREM — independent review requested**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Consolidated: 2026-08-08 to remove the former cross-PR dependence on `L-26202`  
Issue: #238  
Dependencies: elementary calculus and the parabolic profile displayed below  
Scope: continuum carry geometry; no prime-sampling estimate or RH conclusion

## 1. Parabolic defect and exact reciprocal-cell tail

Put

\[
B(u)=2\sqrt u\left[\log(1/u)-2(1-\sqrt u)\right],
\qquad 0<u\le1,
\tag{L-23823.1}
\]

and

\[
g(u)=-B'(u)=\frac{\log u+4}{\sqrt u}-4.
\tag{L-23823.2}
\]

Define

\[
E(\theta)
=\sum_{1\le k\le1/\theta}g(k\theta)
-\theta^{-1/2}\log(1/\theta),
\qquad 0<\theta\le1,
\tag{L-23823.3}
\]

and its cumulative upper tail

\[
H(\theta)=\int_\theta^1E(u)\,du.
\tag{L-23823.4}
\]

Fix an integer `N>=1` and

\[
\frac1{N+1}\le\theta\le\frac1N.
\]

Write

\[
S_N=\sum_{k=1}^Nk^{-1/2},
\qquad
A_N=\sum_{k=1}^Nk^{-1/2}\log k.
\tag{L-23823.5}
\]

Because `g=-B'` and `B(1)=0`, finite substitution gives

\[
\int_\theta^1\sum_{k\le1/u}g(ku)\,du
=\sum_{k=1}^N\frac{B(k\theta)}k.
\tag{L-23823.6}
\]

Also

\[
\int_\theta^1u^{-1/2}\log(1/u)\,du
=4(1-\sqrt\theta)+2\sqrt\theta\log\theta.
\tag{L-23823.7}
\]

Expanding the finite sum in (L-23823.6) therefore yields the exact cell formula

\[
\boxed{
\begin{aligned}
H_N(\theta)={}&4N\theta-4\\
&+\sqrt\theta\left[
4-4S_N-2A_N-2(S_N+1)\log\theta
\right].
\end{aligned}}
\tag{L-23823.8}
\]

The entering term at a reciprocal boundary is `B(1)=0`, so adjacent cell formulas agree continuously. In particular,

\[
H(1)=0.
\tag{L-23823.9}
\]

## 2. The normalized tail is monotone and nonpositive

Define

\[
\boxed{J(\theta)=\frac{H(\theta)}{\sqrt\theta}.}
\tag{L-23823.10}
\]

Inside the `N`th reciprocal cell, differentiating (L-23823.8) gives

\[
\boxed{
J_N'(\theta)
=\frac{2}{\theta^{3/2}}
\left[N\theta+1-(S_N+1)\sqrt\theta\right].}
\tag{L-23823.11}
\]

The decreasing-sum estimate

\[
S_N\le1+\int_1^Nx^{-1/2}dx=2\sqrt N-1
\tag{L-23823.12}
\]

implies

\[
N\theta+1-(S_N+1)\sqrt\theta
\ge(\sqrt{N\theta}-1)^2\ge0.
\tag{L-23823.13}
\]

Hence `J` is nondecreasing on every cell and, by continuity, on all of `(0,1]`.
Since `J(1)=0`,

\[
\boxed{
J(\theta)\le0,
\qquad
H(\theta)\le0
\qquad(0<\theta\le1).}
\tag{L-23823.14}
\]

Thus the full continuum tail sign is proved inside this file; no imported sign theorem remains.

## 3. Quantitative derivative moat below one half

For `N>=2`, put

\[
D_N=2\sqrt N-(S_N+1).
\]

Then

\[
D_{N+1}-D_N
=2(\sqrt{N+1}-\sqrt N)-\frac1{\sqrt{N+1}}>0,
\tag{L-23823.15}
\]

and

\[
D_2=\frac3{\sqrt2}-2>\frac1{10}.
\tag{L-23823.16}
\]

Therefore

\[
S_N+1\le2\sqrt N-\frac1{10}
\qquad(N\ge2).
\tag{L-23823.17}
\]

Substitution in (L-23823.11) gives, throughout `0<theta<=1/2`,

\[
N\theta+1-(S_N+1)\sqrt\theta
\ge(\sqrt{N\theta}-1)^2+\frac1{10}\sqrt\theta,
\]

and hence

\[
\boxed{
J'(\theta)\ge\frac1{5\theta}
\qquad(0<\theta\le1/2),}
\tag{L-23823.18}
\]

away from reciprocal knots, with the integrated inequality valid across the knots.

## 4. Fixed-ratio shell defect

Fix `0<c<1`. Define

\[
\boxed{
E_c(\theta)
=E(\theta)-c^{-1/2}E(\theta/c)\mathbf1_{\theta\le c}.}
\tag{L-23823.19}
\]

Let

\[
H_c(\theta)=\int_\theta^1E_c(u)\,du.
\tag{L-23823.20}
\]

For `theta>=c`,

\[
H_c(\theta)=H(\theta)\le0.
\tag{L-23823.21}
\]

For `0<theta<c`, changing variables in the dilated term gives

\[
\begin{aligned}
H_c(\theta)
&=H(\theta)-\sqrt c\,H(\theta/c)\\
&=\sqrt\theta\,[J(\theta)-J(\theta/c)].
\end{aligned}
\tag{L-23823.22}
\]

By monotonicity of `J`,

\[
\boxed{
H_c(\theta)\le0
\qquad(0<\theta\le1).}
\tag{L-23823.23}
\]

Thus every fixed-ratio parabolic shell has an exact continuum upper-tail defect-to-slack order.

## 5. Quantitative shell moat

If

\[
0<\theta\le\frac c2,
\]

then `[theta,theta/c]` lies below `1/2`. Integrating (L-23823.18) yields

\[
J(\theta/c)-J(\theta)
\ge\frac15\log(1/c).
\tag{L-23823.24}
\]

Therefore

\[
\boxed{
H_c(\theta)
\le-\frac15\sqrt\theta\log(1/c)
\qquad(0<\theta\le c/2).}
\tag{L-23823.25}
\]

For the dyadic shell `c=1/2`,

\[
\boxed{
H_{1/2}(\theta)
\le-\frac{\log2}{5}\sqrt\theta
\qquad(0<\theta\le1/4).}
\tag{L-23823.26}
\]

Formula (L-23823.8) also gives

\[
H(\theta)=O\!\left(\sqrt\theta[1+\log(1/\theta)]\right),
\]

so every shell tail tends to zero at the origin.

## 6. Transport interpretation and review scope

Writing

\[
E_c(\theta)d\theta=\mu_{c,+}-\mu_{c,-},
\]

( L-23823.23 ) is exactly

\[
\mu_{c,+}([\theta,1])
\le\mu_{c,-}([\theta,1])
\qquad(0<\theta<1).
\tag{L-23823.27}
\]

Hence the positive shell defect admits a monotone coupling into negative shell slack at a greater column scale. This statement concerns the complete scalar shell after all source coordinates have been summed; it uses no source-rank, face-count, or reflected-reserve assertion.

The finite arithmetic transfer must preserve the logarithmic prime weight and the prime-sampling error. Those are treated separately in `L-23824` and `L-23825`.

## 7. Proof boundary

Closed here:

1. the exact reciprocal-cell cumulative-tail formula;
2. normalized-tail monotonicity;
3. the full tail sign `H<=0` without an imported theorem;
4. a quantitative derivative lower bound;
5. exact fixed-ratio shell majorization;
6. a quantitative square-root moat;
7. the continuum monotone transport order.

Open:

1. transfer of the weighted shell-tail order to the finite prime set with subpolynomial boundary loss;
2. the prime-ramp estimate;
3. RH.
