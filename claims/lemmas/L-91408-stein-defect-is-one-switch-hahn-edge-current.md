# L-91408 — The Stein defect is an explicit one-switch Hahn edge current and one normalized Jacobi port

Claim ID: `L-91408`  
Status: **EXACT FINITE EDGE-CURRENT AND CONTINUUM PORT THEOREM**  
Created: 2026-08-12  
Depends on: `L-91405`, `L-91406`  
RH status: **unproved**

## 1. Finite edge-current form

Let

\[
 \delta\tau_N=\tau_N-v_N
 =-\frac12X_N-\frac14H_{2,N}.
\]

Because

\[
 -\mathcal L_NX_N=X_N,
 \qquad
 -\mathcal L_NH_{2,N}=\frac52H_{2,N},
\]

one has, for every test `g`,

\[
 \boxed{
 \langle\delta\tau_N,g\rangle_{\pi_N}
 =-\frac12\mathcal E_N(X_N,g)
  -\frac1{10}\mathcal E_N(H_{2,N},g).
 }
\tag{L-91408.1}
\]

The edge increments are

\[
 X_N(k+1)-X_N(k)=1,
\]

\[
 H_{2,N}(k+1)-H_{2,N}(k)=2k-N+1.
\]

Therefore

\[
 \boxed{
 \langle\delta\tau_N,g\rangle_{\pi_N}
 =-\frac1{40}
 \sum_{k=0}^{N-1}
 \pi_N(k)\lambda_k(2k-N+6)
 [g(k+1)-g(k)].
 }
\tag{L-91408.2}
\]

The coefficient `2k-N+6` has at most one sign change. Thus the whole finite Stein-variability correction is one explicit oriented edge current, not an arbitrary signed function on the `N+1` states.

## 2. Exact mode norms

The two nonconstant mode norms are

\[
 \boxed{
 \|X_N\|_2^2=\frac{N(N+4)}{20},
 }
\tag{L-91408.3}
\]

and

\[
 \boxed{
 \|H_{2,N}\|_2^2
 =\frac{N(N-1)(N+4)(N+5)}{350}.
 }
\tag{L-91408.4}
\]

They are orthogonal, and these identities recover

\[
 \operatorname{Var}(\tau_N)
 =\frac14\|X_N\|_2^2+
  \frac1{16}\|H_{2,N}\|_2^2.
\]

## 3. Continuum Jacobi port

For the transformed `Beta(2,2)` law, put

\[
 h_2(v)=v^2-\frac15.
\]

Then

\[
 \|h_2\|_{L^2(\rho)}^2=\frac8{175},
 \qquad
 -\mathcal L_\beta h_2=\frac52h_2,
\]

and

\[
 \delta\tau(v)=-\frac14h_2(v).
\]

If

\[
 e_2=\sqrt{\frac{175}{8}}\,h_2,
\]

then `e_2` is unit norm and

\[
 \boxed{
 \delta\tau=-\frac1{\sqrt{350}}e_2.
 }
\tag{L-91408.5}
\]

Equivalently,

\[
 \boxed{
 \langle\delta\tau,g\rangle_ho
 =-\frac1{10}\mathcal E_\beta(h_2,g)
 =-\frac1{20}\mathbb E_\rho[
   v(1-v^2)g'(v)
  ].
 }
\tag{L-91408.6}
\]

The flux `v(1-v^2)` has exactly one sign change.

## 4. Brownian/theta consequence

At the Jacobi-shadow level, the Stein defect in each Brownian copy is one scalar observation of the derivative observable with exact gain

\[
 \boxed{350^{-1/2}.}
\]

The two-copy defect therefore uses two copies of one normalized quadratic port. All remaining Jacobi modes are orthogonal to it.

A source-specific Brownian/theta completion may now be sought as a finite Schur complement involving:

```text
positive rank-two boundary bulk;
two normalized quadratic ports of gain 1/sqrt(350);
the theta pairwise-variance reserve.
```

The Schur domination itself remains open. The theorem fixes every port, gain, and sign needed to test it.
