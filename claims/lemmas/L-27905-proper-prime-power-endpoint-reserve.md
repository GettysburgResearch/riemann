# L-27905 — Proper prime powers supply a logarithmic endpoint reserve

Claim ID: `L-27905`  
Title: The ordinary-prime endpoint scalar equals the complete von-Mangoldt scalar minus a positive `c log X` proper-power reserve  
Status: **PROPOSED COMPLETE ELEMENTARY THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Dependencies: endpoint source of `L-27903`; elementary Mertens and Chebyshev bounds  
Scope: endpoint-source decomposition; no estimate of the complete von-Mangoldt scalar and no RH conclusion

## 1. Endpoint residual at every integer coordinate

Retain

\[
\dot b_X(m)
=2\sqrt m(1-\sqrt{m/X})\mathbf1_{m\le X}
\tag{L-27905.1}
\]

and define, for every integer `q>=2`,

\[
\boxed{
\eta_X(q)
=v_q(\dot b_X)-q^{-1/2}.}
\tag{L-27905.2}

The ordinary-prime endpoint scalar is

\[
\mathcal A_{\mathbb P}(X)
=\sum_{p\le X}(\log p)\eta_X(p),
\tag{L-27905.3}
\]

while the complete von-Mangoldt scalar is

\[
\mathcal A_\Lambda(X)
=\sum_{q=p^a\le X}\Lambda(q)\eta_X(q).
\tag{L-27905.4}
\]

Their difference is the proper-power reserve

\[
\boxed{
\mathcal R_{\rm pp}(X)
=\mathcal A_\Lambda(X)-\mathcal A_{\mathbb P}(X)
=\sum_{a\ge2}\sum_{p^a\le X}(\log p)\eta_X(p^a).}
\tag{L-27905.5}

## 2. Exact finite formula

Let

\[
N_X(q)=\left\lfloor{X-1\over q}\right\rfloor.
\]

Every active multiple is strictly below the zero endpoint. Therefore

\[
\boxed{
\eta_X(q)
={2N_X(q)\over\sqrt X}
-2\sum_{k=1}^{N_X(q)}
 [\sqrt{kq+1}-\sqrt{kq}]
-{1\over\sqrt q}.}
\tag{L-27905.6}

This formula includes the divisibility case `q|X` correctly: the terminal multiple `X` contributes zero and is excluded by `N_X(q)`.

## 3. Continuum endpoint profile

For

\[
{1\over N+1}<\theta\le{1\over N},
\]

put

\[
\boxed{
d(\theta)
=2N-{S_N+1\over\sqrt\theta},
\qquad
S_N=\sum_{k=1}^Nk^{-1/2}.}
\tag{L-27905.7}

The same one-step mean-value estimate used in `L-27902` gives

\[
\boxed{
\eta_X(q)
=X^{-1/2}d(q/X)+O(q^{-3/2})}
\tag{L-27905.8}

uniformly in `2<=q<=X`.

On each reciprocal cell, `d` is strictly increasing. The decreasing-sum bound

\[
S_N\le2\sqrt N-1
\]

shows

\[
d(\theta)>0
\qquad(0<\theta\le1/10).
\tag{L-27905.9}

Indeed the minimum in cell `N` is at `theta=1/(N+1)`, and for `N>=10`

\[
2N-(S_N+1)\sqrt{N+1}>0.
\]

## 4. Uniform positive moat at low ratios

Set

\[
K_{\rm ep}(\theta)=\sqrt\theta\,d(\theta).
\]

Euler summation gives

\[
\boxed{
\lim_{\theta\downarrow0}K_{\rm ep}(\theta)
=-\zeta(1/2)-1>0.}
\tag{L-27905.10}

Since `d(theta)>0` on `(0,1/10]`, the normalized profile has a positive compact moat

\[
\boxed{
\kappa_{\rm ep}
:=\min_{0\le\theta\le1/10}K_{\rm ep}(\theta)>0.}
\tag{L-27905.11}

Combining with (L-27905.8), there is an absolute `Q` such that, for all sufficiently large `X`,

\[
\boxed{
Q\le q\le X/10
\Longrightarrow
\eta_X(q)
\ge{\kappa_{\rm ep}\over2\sqrt q}.}
\tag{L-27905.12}

## 5. Every fixed coordinate is eventually positive

For fixed `q`, use (L-27905.6) and the Hurwitz expansion of the shifted square-root sum. One obtains

\[
\boxed{
\begin{aligned}
\lim_{X\to\infty}\eta_X(q)
={}&-2\sqrt q
 [\zeta(-1/2,1+1/q)-\zeta(-1/2)]\\
&-{1\over\sqrt q}.
\end{aligned}}
\tag{L-27905.13}

Since

\[
\zeta(-1/2,1+1/q)-\zeta(-1/2)
={1\over2}\int_1^{1+1/q}\zeta(1/2,a)\,da
\]

and `zeta(1/2,a)<-1` for `a>=1`, the right side of (L-27905.13) is strictly positive.

Therefore the finite set `2<=q<Q` is also positive for all sufficiently large `X`. Combining with Section 4,

\[
\boxed{
\eta_X(q)>0
\qquad(2\le q\le X/10)}
\tag{L-27905.14}

cofinally.

## 6. Logarithmic reserve from prime squares

For every prime

\[
\sqrt Q\le p\le\sqrt{X/10},
\]

put `q=p^2` in (L-27905.12):

\[
\eta_X(p^2)
\ge{\kappa_{\rm ep}\over2p}.
\]

Hence

\[
\sum_{p^2\le X/10}(\log p)\eta_X(p^2)
\ge{\kappa_{\rm ep}\over2}
\sum_{p\le\sqrt{X/10}}{\log p\over p}-O(1).
\]

Mertens' elementary estimate

\[
\sum_{p\le y}{\log p\over p}
=\log y+O(1)
\]

gives

\[
\boxed{
\sum_{p^2\le X/10}(\log p)\eta_X(p^2)
\ge{\kappa_{\rm ep}\over4}\log X-O(1).}
\tag{L-27905.15}

## 7. The remaining proper-power tail is bounded

For `q>X/10`, formula (L-27905.6) has at most nine summands and gives

\[
|\eta_X(q)|\le C X^{-1/2}.
\tag{L-27905.16}
\]

For prime squares in `(X/10,X]`, Chebyshev's upper bound

\[
\pi(y)\ll y/\log y
\]

therefore yields total weighted absolute contribution `O(1)`.

For exponents `a>=3`, the number of powers in `(X/10,X]` is

\[
O(X^{1/3}\log X),
\]

so their total weighted contribution is

\[
O(X^{-1/6}\log^2X)=o(1).
\]

All proper powers below `X/10` have nonnegative residual by (L-27905.14). Thus

\[
\boxed{
\mathcal R_{\rm pp}(X)
\ge c_{\rm pp}\log X-O(1)}
\tag{L-27905.17}

for the absolute constant

\[
c_{\rm pp}=\kappa_{\rm ep}/4>0.
\]

## 8. Consequence for endpoint domination

Equations (L-27905.5) and (L-27905.17) give

\[
\boxed{
\mathcal A_{\mathbb P}(X)
\le
\mathcal A_\Lambda(X)
-c_{\rm pp}\log X+O(1).}
\tag{L-27905.18]
\]

The closing bracket in the tag above is typographical only.

Therefore the complete prime-power theorem

\[
\boxed{
\mathcal A_\Lambda(X)=o(\log X)}
\tag{CEP}
\]

implies `EPD` with a strict negative logarithmic moat.

This is a major source correction. The ordinary-prime endpoint sign is not asking the complete oscillatory source to be nonpositive. It has an independent deterministic reserve supplied mainly by prime squares.

## 9. Proof boundary

Closed here, subject to review:

- exact endpoint residual formula;
- continuum endpoint profile and its positive low-ratio sector;
- positive fixed-coordinate limits;
- uniform positive residual below ratio `1/10`;
- logarithmic prime-square reserve;
- bounded negative proper-power tail;
- `CEP -> EPD`.

Open:

- `CEP`, the complete von-Mangoldt endpoint bound;
- a reflected Selberg or explicit-formula proof of `CEP`;
- EPD, WSTS, and RH.
