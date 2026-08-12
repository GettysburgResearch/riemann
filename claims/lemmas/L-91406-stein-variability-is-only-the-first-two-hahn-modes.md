# L-91406 — Beta-binomial Stein variability is rank two, and its Jacobi limit is one pure quadratic mode

Claim ID: `L-91406`  
Status: **EXACT FINITE AND CONTINUUM STEIN DECOMPOSITION**  
Created: 2026-08-12  
Depends on: `L-91405`; PR #401 `L-91319`  
RH status: **unproved**

## 1. Exact finite Stein kernel

Let `K` have law `pi_N`. For every test `f`, summation by parts and detailed balance give

\[
 \boxed{
 \mathbb E\left[(K-\tfrac N2)f(K)\right]
 =\frac14\mathbb E\left[
   (K+2)(N-K)(f(K+1)-f(K))
  \right].
 }
\tag{L-91406.1}
\]

Thus the forward discrete Stein kernel is

\[
 \tau_N(K)=\frac14(K+2)(N-K).
\tag{L-91406.2}
\]

Its mean is exactly

\[
 \mathbb E\tau_N(K)=v_N=\frac{N(N+4)}{20}.
\tag{L-91406.3}
\]

## 2. Rank-two fluctuation

With `X_N` and `H_(2,N)` from `L-91405`, the elementary identity

\[
 (K+2)(N-K)
 =\frac{N(N+4)}4-2X_N-X_N^2
\]

gives

\[
 \boxed{
 \tau_N-v_N
 =-\frac12X_N-\frac14H_{2,N}.
 }
\tag{L-91406.4}
\]

Therefore, for every test `g`,

\[
 \boxed{
 \mathbb E[(\tau_N-v_N)g]
 =-\frac12\langle X_N,g\rangle_{\pi_N}
  -\frac14\langle H_{2,N},g\rangle_{\pi_N}.
 }
\tag{L-91406.5}
\]

The Stein-variability functional annihilates every Hahn mode of degree at least three. It is exactly rank two.

The variance is also explicit:

\[
 \boxed{
 \operatorname{Var}(\tau_N)
 =\frac{N(N+4)(N^2+4N+65)}{5600}.
 }
\tag{L-91406.6}
\]

## 3. Critical scaling and the Jacobi limit

Put

\[
 V_N=\frac{2K-N}{N},
 \qquad
 \theta_N=\frac{(K+2)(N-K)}{N^2}.
\]

Then

\[
 \mathbb E\theta_N=\operatorname{Var}(V_N)=\frac{N+4}{5N},
\]

and (L-91406.4) becomes

\[
 \boxed{
 \theta_N-\mathbb E\theta_N
 =-\frac1N V_N
  -\frac14\left(V_N^2-\mathbb EV_N^2\right).
 }
\tag{L-91406.7}
\]

As `N` tends to infinity, `V_N` converges to the transformed `Beta(2,2)` law

\[
 \rho(v)=\frac34(1-v^2)\mathbf1_{(-1,1)}(v).
\]

Its canonical Stein kernel is

\[
 \tau(v)=\frac{1-v^2}{4},
 \qquad
 \mathbb E\tau=\frac15.
\]

Hence

\[
 \boxed{
 \tau(v)-\frac15
 =-\frac14\left(v^2-rac15\right).
 }
\tag{L-91406.8}
\]

The continuum Stein variability is one pure degree-two Jacobi mode. Moreover

\[
 \boxed{
 \operatorname{Var}(\tau)=\frac1{350},
 \qquad
 -\mathcal L_\beta(v^2-	frac15)
 =\frac52(v^2-	frac15).
 }
\tag{L-91406.9}
\]

## 4. Consequence for the Brownian/theta defect

PR #401 `L-91319` writes the Brownian Fisher covariance as a positive constant-Stein rank-two bulk plus

\[
 \mathcal D(F)
 =\mathbb E[(\tau_1-V)\partial_1\mathcal A_F
            +(\tau_2-V)\partial_2\mathcal A_F].
\]

At every beta-binomial truncation, (L-91406.5) proves that this defect sees only the first two Hahn projections of each coordinate derivative. In the Jacobi limit, (L-91406.8) proves that it sees only the quadratic Jacobi projection.

Thus the arbitrary-phase Brownian obstruction is not an uncontrolled infinite-dimensional defect. After the positive rank-two boundary bulk is separated, the non-Gaussian remainder is one explicit second-chaos boundary port, plus an `O(N^-1)` linear finite-grid port.

A completion of the Brownian/theta route may therefore target one finite Schur complement coupling this quadratic port to the theta variance square. Such a coupling remains unproved, but the required port dimension is now exact.
