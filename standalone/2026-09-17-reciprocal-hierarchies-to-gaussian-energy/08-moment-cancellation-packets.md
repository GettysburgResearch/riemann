# 08. Moment cancellation inside the actual arithmetic source

**Status:** explicit component inequalities, a finite sign-preserving algorithm, and rerun finite exact experiments. The uniform remainder and inter-packet covariance bounds remain OPEN.

## 1. Change representation, not coefficients

In H=L^2((0,infinity),t^2dt), put v_x(t)=x e^(-xt). Then
\[
\langle v_a,v_b\rangle=2ab/(a+b)^3,\quad
\|v_x\|=1/(2\sqrt x),\quad
Q_0(N)=\left\|\sum_{n\le N}\mu(n)v_n\right\|^2.
\]
For two opposite signs,
\[
\|v_a-v_b\|\le|a^{-1/2}-b^{-1/2}|.
\]
This follows by integrating ||partial_x v_x||=(1/2)x^(-3/2). When b-a is small compared with a, the combined cost is roughly (b-a)/(2a^(3/2)), much smaller than separate norm costs.

## 2. General moment-packet inequality

A finite group (x_i,c_i) has order k if
\[
\sum_i c_i x_i^\ell=0,\quad0\le\ell<k.
\]
Suppose A<=x_i<=A+H. Differentiation and a gamma integral give
\[
\partial_x^k v_x(t)=(-1)^kt^{k-1}(xt-k)e^{-xt},
\]
\[
\|\partial_x^k v_x\|^2
=\frac{(k+1)(2k)!}{2^{2k+2}}x^{-2k-1}.
\]
Hilbert-space Taylor expansion around A cancels every polynomial term below k, giving
\[
\boxed{\left\|\sum_i c_i v_{x_i}\right\|
\le\frac{\sqrt{(k+1)(2k)!}}{2^{k+1}k!}
\frac{H^k}{A^{k+1/2}}\sum_i|c_i|.}
\]
The coefficient grows only like k^(1/4)/(2 pi^(1/4)), not factorially.

For the general detector, use
\[
v_{j,x}(t)=\left(\frac{2^{2j+1}}{\Gamma(2j+3)}\right)^{1/2}
x^{j+1}e^{-xt}
\]
in H_j=L^2(t^(2j+2)dt). Its Gram kernel is Q_j, and
\[
\boxed{\|\partial_x^k v_{j,x}\|^2
=\frac{(2k)!(j+2)_k}{2^{2k+2}k!}\,x^{-2k-1}.}
\]
One proof differentiates the Gram kernel at a=x+h,b=x-h:
\[
\langle v_{j,x+h},v_{j,x-h}\rangle
=\frac1{4x}(1-h^2/x^2)^{j+1}.
\]
Apply partial_a^k partial_b^k=4^(-k)(partial_x^2-partial_h^2)^k, then Vandermonde's identity. The packet bound follows with constant
\[
C_{j,k}=\sqrt{(2k)!(j+2)_k/(2^{2k+2}k!)}
\]
and prefactor C_(j,k)/k!. For fixed k, the extra cost is O_k(j^(k/2)), hence polylogarithmic at j=log^4N.

If a block near X, of total absolute mass O(X), is fully decomposed into order-k groups of diameter <=X^theta, the triangle bound is O(X^(1/2-k(1-theta))). The threshold is theta=1-1/(2k): sqrt X for k=1, X^(3/4) for k=2, X^(5/6) for k=3. This is conditional on complete grouping and paid residuals, not an arithmetic density theorem.

## 3. Exact sign-preserving extraction

Take increasing nodes x_0<...<x_k whose current residual coefficients have alternating signs and positive magnitudes r_i. Put
\[
d_i=\prod_{l\ne i}|x_i-x_l|,\quad
\lambda=\min_i r_id_i,\quad
c_i=\operatorname{sgn}(r(x_i))\lambda/d_i.
\]
No coefficient exceeds the available magnitude, at least one node is exhausted, and the denominator signs in Lagrange interpolation give
\[
\sum_i c_i x_i^\ell=0,\quad\ell<k.
\]
Repeated extraction terminates after finitely many steps. The remainder has at most k-1 sign changes, because otherwise an alternating subsequence of length k+1 remains. Applied in prescribed intervals, this controls packet diameters.

Every coefficient is reconstructed exactly and absolute mass is conserved:
\[
\sum_P\sum_n|c_P(n)|+\sum_n|r(n)|=\sum_n|c_{\rm original}(n)|.
\]
This is an application of classical interpolation, not a novel general interpolation theorem. A small number of residual sign changes does not imply small residual mass.

## 4. Actual Prouhet-pattern Möbius examples

The supplied program searches arithmetic progressions and independently factors their nodes. It finds:

| Order | Nodes | Q_0 of isolated packet / its diagonal |
|---|---|---:|
| 2 | 15+2r, 0<=r<4 | about 6.92998e-4 |
| 3 | 377+6r, 0<=r<8 | about 4.23846e-9 |
| 4 | 51097+30r, 0<=r<16 | about 2.74820e-21 |

Their Möbius signs agree with (-1)^(binary-digit-sum(r)). The classical Prouhet–Thue–Morse product [PTM]
\[
\sum_{r=0}^{2^k-1}(-1)^{s_2(r)}z^r
=\prod_{l=0}^{k-1}(1-z^{2^l})
\]
forces moments below k to vanish. For the order-four group the moments through degree four are exactly
\(0,0,0,0,1244160000\).

The tiny energy ratios include internal cross terms only. They do not control interactions with other groups or the omitted source. They are finite rational results, not fitted asymptotic exponents.

## 5. Coprime dilations create infinite families, not an RH bound

Let P contain all primes dividing a fixed squarefree-node packet a_i. For squarefree r coprime to P,
\[
\mu(a_ir)=\mu(a_i)\mu(r).
\]
All moments still cancel, and the copies are disjoint because the P-smooth part identifies a_i. Their energy scales exactly as
\[
Q_j[\text{packet dilated by }r]=Q_j[\text{packet}]/r.
\]
But relative diameter H/A is unchanged. Estimating norms separately introduces sum r^(-1/2), and cross-packet terms are not orthogonal by fiat.

For T(s)=sum_i mu(a_i)a_i^(-s), the complete coprime-dilation series is
\[
\frac{T(s)}{\zeta(s)}\prod_{p\mid P}(1-p^{-s})^{-1}.
\]
Moment cancellation says T(0)=T(-1)=...=T(-(k-1))=0. It does not say T(rho)=0 at a zeta zero. Fixed-template cancellation may therefore leave an off-critical reciprocal-zeta pole intact.

## 6. The complete finite-prefix test

The inherited checker covers the entire Möbius prefix through 512, partitioned into dyadic blocks and intervals at the corresponding threshold widths. Its exact reconstruction retains all residual coefficients.

| Order | Packet count | Residual norm budget | Total norm bound |
|---|---:|---:|---:|
| 1 | 108 | about 5.655 | about 5.925 |
| 2 | 179 | about 6.455 | about 6.591 |
| 3 | 171 | about 7.198 | about 7.266 |
| 4 | 163 | about 7.433 | about 7.504 |

The actual Q_0(512) is about 0.322427930947825, so its norm is about 0.567827. Higher-order packets become cheaper, but the retained remainder dominates and these triangle budgets do not approach the true energy.

For any exact decomposition mu*1_[1,N]=sum_P c_P+r_N,
\[
\sqrt{Q_j(N)}\le
\sum_P\frac{C_{j,k_P}}{k_P!}
\frac{H_P^{k_P}}{A_P^{k_P+1/2}}\sum_n|c_P(n)|
+\frac12\sum_{n\le N}|r_N(n)|/\sqrt n.
\]
A stronger estimate may retain sqrt(Q_j[r_N]) instead of the final absolute norm. In either case, no residual is dropped. Since every packet has zero total mass,
\[
\sum_n r_N(n)=M(N),\qquad
\frac12\sum|r_N(n)|/\sqrt n\ge|M(N)|/(2\sqrt N).
\]
The residual cannot hide a large Mertens sum.

## 7. Evidence contract

The two files under `evidence/` were supplied with the conversation and are preserved unchanged. The publication session reran the full default computation in ordinary and optimized Python and reproduced the JSON byte-for-byte. It checks 35 derivative identities, exact factorization/sign/moment assertions, two independent energy accumulations, finite dilations, seven small full-prefix energies and four complete prefix decompositions. Display decimals are not interval enclosures; the decisive finite comparisons use rational arithmetic and rational square-root upper bounds.

These computations certify their finite assertions only. They do not certify an all-scale packet cover, residual bound, Gaussian integral, unbounded crossing sequence with small energy, or RH. See [VALIDATION](VALIDATION.md).
