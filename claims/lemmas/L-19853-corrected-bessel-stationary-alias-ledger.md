# L-19853 — Correct Bessel endpoint, stationary-alias, and Mellin-fold ledger

Claim ID: `L-19853`  
Status: **PROPOSED COMPLETE ANALYTIC REPAIR — PRIMARY-SOURCE NORMALIZATION REVIEW REQUIRED**  
Authoring agent: `gpt56-pro-09-q`  
Created: 2026-08-07  
Dependencies: exact radial normalization `L-16217/L-16222`; interval-ODE bounds `L-16229`; stationary calculation `L-19829`; endpoint Parseval identities `L-19850`; abstract support large sieve `L-16226`  
Supersedes: the false alias geometry and radial-endpoint Airy paragraph in `L-19844`

## 1. Three geometries must be separated

The complete radial/alias analysis has three distinct singular mechanisms:

1. the radial endpoint `z=1`, which is a simple-pole **Bessel** problem;
2. the first-versus-`k` alias phase, which has one ordinary nondegenerate stationary point;
3. the fold of the Mellin frequency map, which is the **Airy/cubic** problem.

No one of these may be substituted for another.

Throughout,

\[
 R=2\pi\lambda^2,
 \qquad
 n,j\le C(\log R)^2,
 \qquad
 \sigma_n^2,\sigma_j^2
 =O((\log R)^2/R).
\tag{L-19853.1}
\]

Let `rho_(n,R)` be the canonical unit positive-ray leakage profile.

## 2. Bessel endpoint normalization

The exact norm identity gives

\[
 \rho_{n,R}(z)
 =\frac{B_{\sigma_n,R}(z)+E_{n,R}(z)}
        {\|B_{\sigma_n,R}+E_{n,R}\|_{L^2(1,\infty)}},
\tag{L-19853.2}
\]

with

\[
 \|B_{\sigma_n,R}+E_{n,R}\|_2
 =(2R)^{-1/2}\left(1+O((\log R)^2/R)\right).
\tag{L-19853.3}
\]

Near `z=1`, Dunster's simple-pole variable reduces the equation to the Bessel pair `J_0,Y_0`; the regular solution has the bound

\[
 \boxed{
 |\rho_{n,R}(z)|
 \le C(\log R)^C
 \min\bigl(R^{1/2},(z^2-1)^{-1/4}\bigr).}
\tag{L-19853.4}
\]

After extracting the rapid outgoing/incoming Bessel phases, one support derivative satisfies the same polylogarithmic slow-amplitude bound:

\[
 |a_{n,R}^{\pm}(z)|
 +R|\partial_Ra_{n,R}^{\pm}(z)|
 +|\partial_za_{n,R}^{\pm}(z)|
 \le C(\log R)^C.
\tag{L-19853.5}
\]

This is the endpoint input required by the support large sieve. No Airy approximation is used at `z=1`.

## 3. Far-field endpoint expansion

For `z>=2`, the normalized Hankel expansion is

\[
 \rho_{n,R}(z)
 =\frac{
 a_{n,R}^+(z)e^{iR\xi_n(z)}
 +a_{n,R}^-(z)e^{-iR\xi_n(z)}}{z}
 +q_{n,R}(z),
\tag{L-19853.6}
\]

where

\[
 |q_{n,R}(z)|+R|\partial_Rq_{n,R}(z)|
 \le C(\log R)^C
 \left(\frac1{Rz}+\frac1{z^2}\right).
\tag{L-19853.7}
\]

The leading endpoint channel must be summed collectively:

\[
 \sum_{k\ge2}\frac{e^{ik\vartheta}}k
 =-\log(1-e^{i\vartheta})-e^{i\vartheta}.
\tag{L-19853.8}
\]

Parseval gives

\[
 \int_0^{2\pi}
 \left|\sum_{k\ge2}\frac{e^{ik\vartheta}}k\right|^2d\vartheta
 =2\pi\sum_{k\ge2}k^{-2}.
\tag{L-19853.9}
\]

For one support derivative the coefficient is at worst `(log k)/k`; again

\[
 \sum_{k\ge2}\frac{(\log k)^2}{k^2}<\infty.
\tag{L-19853.10}
\]

Hence both the endpoint channel and one scaled support derivative are bounded in the complete packet norm on the endpoint-nonresonant support set of `L-19845`.

## 4. Exact stationary point for every later alias

Consider the equal-sign first-versus-`k` phase

\[
 \phi_{jnk}(z)
 =\xi_{\sigma_j}(z)-\xi_{\sigma_n}(kz),
 \qquad k\ge2.
\tag{L-19853.11}
\]

Using

\[
 \xi_\sigma'(z)^2
 =1+\frac{1-\sigma^2}{z^2-1},
\tag{L-19853.12}
\]

the stationary equation has exactly one solution. With `a_j=1-sigma_j^2`,

\[
 \boxed{
 \frac{a_j}{k^2+1}
 \le z_{jnk}^2-1
 \le\frac{a_j}{k^2-1}.}
\tag{L-19853.13}
\]

Thus `z_jnk-1=Theta(k^-2)` uniformly on the growing packet.

Differentiation gives

\[
 \xi_\sigma''(z)
 =-\frac{(1-\sigma^2)z}
 {(z^2-1)^{3/2}(z^2-\sigma^2)^{1/2}},
\tag{L-19853.14}
\]

and at the stationary point

\[
 \boxed{|\phi_{jnk}''(z_{jnk})|\ge ck^3.}
\tag{L-19853.15}
\]

The opposite-sign phase has no stationary point because its two positive radial frequencies add.

## 5. Summable stationary contribution

At `z_jnk`, the endpoint estimate gives

\[
 |\rho_{j,R}(z_{jnk})|
 \le C(\log R)^C\min(R^{1/2},k^{1/2}),
\]

while

\[
 |\rho_{n,R}(kz_{jnk})|
 \le C(\log R)^C/k.
\]

Stationary phase with curvature (L-19853.15) yields

\[
 \boxed{
 |I_{jnk}^{\rm stat}(R)|
 \le C(\log R)^C
 \begin{cases}
 R^{-1/2}k^{-2},&2\le k\le R,\\
 k^{-5/2},&k>R.
 \end{cases}}
\tag{L-19853.16}
\]

The nonstationary pieces satisfy

\[
 |I_{jnk}^{\rm nonstat}(R)|
 \le CR^{-1}k^{-2}(\log R)^C.
\tag{L-19853.17}
\]

Therefore

\[
 \boxed{
 \sum_{k\ge2}|I_{jnk}(R)|
 \le CR^{-1/2}(\log R)^C.}
\tag{L-19853.18}
\]

Uniformity over the `O(log^2 R)` packet only changes the logarithmic exponent.

## 6. Mellin fold and Airy splice

The Airy normal form is used only where the stationary-frequency map

\[
 F(x)=S(x)-xS'(x)
\]

has a nondegenerate critical point. On a window of width

\[
 O(R^{-2/3}(\log R)^C),
\]

the uniform cubic model gives an operator contribution

\[
 O(R^{-1/3}(\log R)^C).
\tag{L-19853.19}
\]

Outside that moving window, the extracted branch phase satisfies the derivative separation required by `L-16226`.

## 7. Complete first/rest operator bounds

Combining Sections 2--6 gives, on a relative-`1-o(1)` support set,

\[
 \boxed{
 \|F_R^*H_R+H_R^*F_R\|
 \le CR^{-1/3}(\log R)^C=o(1),}
\tag{L-19853.20}
\]

and

\[
 \boxed{
 \|F_R+H_R\|^2
 \le(\log R)^C.}
\tag{L-19853.21}
\]

All leading endpoint self-energy remains inside the positive Gram `H_R^*H_R`; only the first/rest Hermitian cross is made small.

## 8. Consequences

Equations (L-19853.20)--(L-19853.21) supply the analytic inputs of `L-19841` and the branchwise amplitude input of `L-19843`, after replacing every citation of the withdrawn geometry in `L-19844`.

## 9. Proof boundary

- The stationary equation and scale calculations are explicit.
- The exact normalization of the Bessel profile is inherited from `L-16217/L-16222`.
- A final independent review must verify the uniform constants in the complex shrinking strip, the differentiated interval-ODE bounds, and the whitening from scalar profiles to the complete signed packet.
- This theorem concerns the omitted support tail, not the finite Fourier residual of `L-19832`.
- No RH conclusion is claimed by this lemma alone.
