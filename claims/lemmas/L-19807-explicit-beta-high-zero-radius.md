# L-19807 — Explicit beta-cell high-zero radius

Claim ID: `L-19807`  
Title: The complete unverified zero tail of the beta square-cell criterion has a closed numerical logarithmic radius  
Status: `PROPOSED — COMPLETE EXPLICIT ESTIMATE`  
Authoring agent: `gpt56-pro-09-i`  
Created: 2026-08-01  
Dependencies: `T-19804`; Trudgian's explicit zero-count theorem, arXiv:1206.1844, Theorem 2 with `K=Q`

## 1. Explicit unit-shell zero count

Let

\[
Z(T)=\#\{\rho:\zeta(\rho)=0,\ 0<\Re\rho<1,
 |\Im\rho|\le T\},
\tag{L-19807.1}
\]

counting multiplicity and both signs of the ordinate. Trudgian's theorem gives,
for `T>=1`,

\[
\left|
Z(T)-{T\over\pi}\log{T\over2\pi e}
\right|
\le0.317\log T+9.815.
\tag{L-19807.2}
\]

Indeed his Dedekind theorem has `n_K=1`, `d_K=1`, and constant
`6.333+3.482=9.815` for `K=Q`.

Let

\[
M(T)={T\over\pi}\log{T\over2\pi e}.
\]

Since

\[
M'(T)={1\over\pi}\log{T\over2\pi},
\]

for every integer `k>=1`,

\[
\begin{aligned}
Z(k+1)-Z(k)
&\le |M(k+1)-M(k)|\\
&\quad+0.317[\log(k+1)+\log k]+19.63\\
&\le20\log(k+2).
\end{aligned}
\tag{L-19807.3}
\]

The final numerical inequality follows from

\[
|M(k+1)-M(k)|
\le\pi^{-1}[\log(k+1)+\log(2\pi)]
\]

and is already strict at `k=1`; the difference increases thereafter.

Thus every unit shell in the absolute centered ordinate contains at most

\[
\boxed{20\log(k+2)}
\tag{L-19807.4}
\]

zeros, counting multiplicity and both signs.

## 2. Explicit beta filter bound

Use

\[
w(u)=30u^2(1-u)^2,
\qquad
x(u)=n^2+(2n+1)u,
\tag{L-19807.5}
\]

and

\[
J_n(\gamma)=\int_0^1w(u)x(u)^{-i\gamma}du.
\tag{L-19807.6}
\]

Write

\[
\gamma=a+ib,
\qquad |b|\le1/2.
\tag{L-19807.7}
\]

Because `w=w'=0` at both endpoints, two integrations by parts have no boundary
terms. With

\[
\phi(u)=\log x(u),
\qquad
{1\over\phi'(u)}={x(u)\over2n+1},
\]

the exact second transformed amplitude is

\[
\begin{aligned}
T^2(wx^b)={}&
 {w''x^{b+2}\over(2n+1)^2}
 +(2b+3){w'x^{b+1}\over2n+1}
 +(b+1)^2wx^b.
\end{aligned}
\tag{L-19807.8}
\]

The elementary norms are

\[
\|w\|_1=1,
\qquad
\|w'\|_1={15\over4},
\qquad
\|w''\|_1={40\sqrt3\over3}.
\tag{L-19807.9}
\]

Moreover

\[
x(u)^b\le n+1,
\qquad
{x(u)\over2n+1}\le n+1.
\tag{L-19807.10}
\]

Therefore, for `a!=0`,

\[
\begin{aligned}
|J_n(a+ib)|
&\le {|a|^{-2}}
 \left({40\sqrt3\over3}+15+{9\over4}\right)(n+1)^3\\
&\le\boxed{{323n^3\over a^2}}
\qquad(n\ge1).
\end{aligned}
\tag{L-19807.11}
\]

No RH assumption enters this estimate.

## 3. Closed high-zero radius

Fix `A>0` and put

\[
K=\lceil An\rceil\ge2,
\qquad
L_K=\log(2K).
\tag{L-19807.12}
\]

For every zero in the shell `k<=|a|<k+1`,

\[
\left|{1-J_n(\gamma)\over\gamma^2}\right|
\le {1\over k^2}+{323n^3\over k^4}.
\tag{L-19807.13}
\]

Equations (L-19807.4) and (L-19807.13) give

\[
\begin{aligned}
\mathcal T_{\beta}(n,A)
&:=\left|
\sum_{|\Re\gamma|\ge An}
 m_\gamma{1-J_n(\gamma)\over\gamma^2}
\right|\\
&\le20\sum_{k=K}^\infty
 \log(k+2)\left(k^{-2}+323n^3k^{-4}\right).
\end{aligned}
\tag{L-19807.14}
\]

For `K>=2`, monotone integral comparison gives

\[
\sum_{k=K}^\infty{\log(k+2)\over k^2}
\le{(3/2)L_K+1\over K},
\tag{L-19807.15}
\]

and

\[
\sum_{k=K}^\infty{\log(k+2)\over k^4}
\le{L_K+1\over K^3}.
\tag{L-19807.16}
\]

Consequently

\[
\boxed{
\mathcal T_\beta(n,A)
\le
 {20[(3/2)L_K+1]\over K}
 +{6460n^3(L_K+1)\over K^3}.}
\tag{L-19807.17}
\]

A support-only version is

\[
\boxed{
\mathcal T_\beta(n,A)
\le
 {20[(3/2)\log(2(An+1))+1]\over An}
 +{6460[\log(2(An+1))+1]\over A^3}.}
\tag{L-19807.18}
\]

This is an explicit unconditional radius for every unverified zero above height
`An`, including hypothetical off-line zeros.

## 4. Verified-height lower floor

If every zero with

\[
|\Re\gamma|<An
\]

has been certified on the critical line with complete multiplicity, its paired
beta-cell contribution is nonnegative. Hence

\[
\boxed{
\mathscr C_\beta(n)
\ge-\mathcal T_\beta(n,A).}
\tag{L-19807.19}
\]

The same radius may be combined with an explicit selected-zero phase sum rather
than discarding the nonnegative inner block.

Since (L-19807.17) is `O_A(log n)`, it is already subpolynomial. The only
asymptotic obstruction is the finite moving block below height `An`.

## 5. Proof-producing schema

A zero-side certificate binds:

1. integer `n` and rational `A` with `K=ceil(An)>=2`;
2. complete certified line-zero count through `An`;
3. the exact rational/logarithmic value in (L-19807.17);
4. an optional directed inner phase sum;
5. the resulting lower interval for `mathscr C_beta(n)`.

It is cross-checked against the independent finite-prime formula in `T-19804`.

## 6. Proof boundary

- The constants are deliberately conservative and may be sharpened.
- The zero-count input is an explicit published theorem; a production artifact
  must bind the exact theorem version and normalization.
- A finite verified height still gives only finitely many beta cells.
- The radius does not prove the beta-cell inequality or RH cofinally.