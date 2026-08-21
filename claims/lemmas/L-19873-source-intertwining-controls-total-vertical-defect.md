# L-19873 — A source derivative-intertwining estimate controls the complete vertical Darboux defect

Claim ID: `L-19873`  
Status: **PROVED ABSTRACT SOURCE/COMPANION THEOREM; ARITHMETIC INTERTWINING RATE OPEN**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-12  
Dependencies: `L-19869`, `T-19815`; elementary Green-commutator algebra and Schur triangularization  
Scope: exact bridge from a prime/source lift to `V_j -> 0`  
Nonclaim: the required source derivative-intertwining estimate is not proved for the current exterior-cardinal reservoir, and RH is not proved

## 1. Finite setup

Let `V=R^n`, let

\[
 \Lambda=\Lambda^{\mathsf T},
 \qquad
 \eta^{\mathsf T}\xi=1,
 \tag{L-19873.1}
\]

and put

\[
 P=I-|\xi\rangle\langle\eta|,
 \qquad
 T_\xi=\Lambda-|\Lambda\xi\rangle\langle\eta|=\Lambda P.
 \tag{L-19873.2}
\]

Thus `P^2=P`, `P xi=0`, and `eta^T P=0`.

Let `K` be a real Hilbert space, let `A=A^*` on a domain containing the range of a finite-rank map

\[
 W:V\longrightarrow K,
 \tag{L-19873.3}
\]

and write

\[
 D=W^*W.
 \tag{L-19873.4}
\]

Let `G=G^T` be positive definite and suppose that, for one real `lambda`,

\[
 Q=D-\lambda G\succeq0,
 \qquad
 \ker Q=\mathbb R\xi.
 \tag{L-19873.5}
\]

Assume that the source lift obeys the rank-one Green-intertwining identity

\[
 \boxed{
 AW-W\Lambda=|g\rangle\langle\eta|+R
 }
 \tag{L-19873.6}
\]

for one `g in K` and one error map `R:V->K`.

The rank-one term is the allowed boundary channel.  The theorem charges only the genuinely non-Green remainder `R` and the metric commutator `[G,Lambda]`.

## 2. Exact projected commutator identity

Put

\[
 S=R^*W-W^*R-\lambda(G\Lambda-\Lambda G).
 \tag{L-19873.7}
\]

Then `S^T=-S`.  Define

\[
 \alpha=Q\Lambda\xi.
 \tag{L-19873.8}
\]

The complete CCM companion defect is exactly

\[
 \boxed{
 QT_\xi-T_\xi^{\mathsf T}Q
 =P^{\mathsf T}SP.
 }
 \tag{L-19873.9}
\]

### Proof

Let `beta=W^*g`.  From (L-19873.6),

\[
 W\Lambda=AW-|g\rangle\langle\eta|-R.
\]

Since `A=A^*`,

\[
\begin{aligned}
 D\Lambda-\Lambda D
 &=W^*W\Lambda-(W\Lambda)^*W\\
 &=|\eta\rangle\langle\beta|
   -|\beta\rangle\langle\eta|
   +R^*W-W^*R.
\end{aligned}
 \tag{L-19873.10}
\]

Hence

\[
 Q\Lambda-\Lambda Q
 =|\eta\rangle\langle\beta|
  -|\beta\rangle\langle\eta|+S.
 \tag{L-19873.11}
\]

Because `Q xi=0`,

\[
 \alpha=(Q\Lambda-\Lambda Q)\xi
 =\eta\langle\beta,\xi\rangle-\beta+S\xi.
 \tag{L-19873.12}
\]

Expanding `QT_xi-T_xi^TQ` and substituting (L-19873.11)--(L-19873.12) gives

\[
 QT_\xi-T_\xi^{\mathsf T}Q
 =S-S|\xi\rangle\langle\eta|
   -|\eta\rangle\langle\xi|S.
 \tag{L-19873.13}
\]

Since `S` is real skew-symmetric,

\[
 \langle\xi,S\xi\rangle=0.
\]

Therefore the right side of (L-19873.13) equals

\[
 (I-|\eta\rangle\langle\xi|)
 S
 (I-|\xi\rangle\langle\eta|)
 =P^TSP,
\]

which proves (L-19873.9).  QED.

## 3. Quotient norm and operator bound

Let

\[
 \mathcal H=V/\mathbb R\xi.
\]

The form induced by `Q` is positive definite on `mathcal H`.  Use `P` as the canonical representative in `ker eta^T`, and define

\[
 \kappa_W
 =\left\|WPQ_{\mathcal H}^{-1/2}\right\|_{\rm op},
 \tag{L-19873.14}
\]

\[
 \rho_R
 =\left\|RPQ_{\mathcal H}^{-1/2}\right\|_{\rm HS},
 \tag{L-19873.15}
\]

and

\[
 \chi_G
 =\left\|
 Q_{\mathcal H}^{-1/2}
 P^T(G\Lambda-\Lambda G)P
 Q_{\mathcal H}^{-1/2}
 \right\|_{\rm HS}.
 \tag{L-19873.16}
\]

Equation (L-19873.9) and the Hilbert--Schmidt ideal inequality give

\[
 \boxed{
 \left\|
 Q_{\mathcal H}^{-1/2}
 (QT_\xi-T_\xi^TQ)_{\mathcal H}
 Q_{\mathcal H}^{-1/2}
 \right\|_{\rm HS}
 \le 2\kappa_W\rho_R+|\lambda|\chi_G.
 }
 \tag{L-19873.17}
\]

Indeed, the `R` part is

\[
 (RPQ^{-1/2})^*(WPQ^{-1/2})
 -(WPQ^{-1/2})^*(RPQ^{-1/2}),
\]

whose Hilbert--Schmidt norm is at most `2 kappa_W rho_R`; the `G` term is exactly the second summand.

## 4. Complete total-vertical-defect estimate

Let

\[
 z_1,\ldots,z_{n-1}
\]

be the nonzero eigenvalues of the quotient companion, counted algebraically.  These are the nonuniversal finite-transform zeros in the CCM determinant identity.  Put

\[
 V(\xi)
 =\sum_{\operatorname{Im}z_\ell>0}
   (\operatorname{Im}z_\ell)^2.
 \tag{L-19873.18}
\]

Then

\[
 \boxed{
 V(\xi)
 \le {1\over8}
 \left\|
 Q_{\mathcal H}^{-1/2}
 (QT_\xi-T_\xi^TQ)_{\mathcal H}
 Q_{\mathcal H}^{-1/2}
 \right\|_{\rm HS}^2.
 }
 \tag{L-19873.19}
\]

Consequently,

\[
 \boxed{
 V(\xi)
 \le {1\over8}
 \left(2\kappa_W\rho_R+|\lambda|\chi_G\right)^2.
 }
 \tag{L-19873.20}
\]

### Proof

In the positive quotient metric, put

\[
 B=Q_{\mathcal H}^{1/2}
 T_\xi
 Q_{\mathcal H}^{-1/2}.
\]

A complex Schur decomposition makes `B` upper triangular with diagonal `z_l`.  The diagonal and strictly off-diagonal parts of `B-B^*` are orthogonal in Hilbert--Schmidt norm.  Hence

\[
 \|B-B^*\|_{\rm HS}^2
 \ge4\sum_l(\operatorname{Im}z_l)^2
 =8V(\xi),
\]

because the nonreal eigenvalues occur in conjugate pairs.  This proves (L-19873.19); (L-19873.20) follows from (L-19873.17).  QED.

## 5. Arithmetic residual interpretation

Let `J_j:V_j->H_global` be an exact global arithmetic-radical lift and let `iota_j` be the finite zero-extension map.  Put

\[
 W_j=J_j-\iota_j.
 \tag{L-19873.21}
\]

For the finite Fourier/scaling operator `Lambda_j`, the zero-extension Green formula has one common endpoint evaluation functional after the two endpoint deltas are grouped.  Therefore

\[
 A\iota_j-\iota_j\Lambda_j
 =|g_j\rangle\langle\eta_j|
 \tag{L-19873.22}
\]

in the natural graph-dual formulation.  It follows that (L-19873.6) holds with

\[
 \boxed{
 R_j=AJ_j-J_j\Lambda_j.
 }
 \tag{L-19873.23}
\]

Thus the source-side conclusion-producing quantity is not an unspecified positive completion.  It is the explicit derivative-intertwining error

\[
 \boxed{
 \rho_j
 =\left\|
 (AJ_j-J_j\Lambda_j)
 P_j(Q_j)_{\mathcal H}^{-1/2}
 \right\|_{\rm HS}.
 }
 \tag{L-19873.24}
\]

If

\[
 \kappa_{W,j}=O(1),
 \qquad
 \rho_j\to0,
 \qquad
 |\lambda_j|\chi_{G,j}\to0,
 \tag{L-19873.25}
\]

then

\[
 \boxed{V_j\to0.}
 \tag{L-19873.26}
\]

Combining `T-19815`, `L-19868`, and (L-19873.26) proves RH.

A quantitative sufficient form is

\[
 2\kappa_{W,j}\rho_j+|\lambda_j|\chi_{G,j}=o(1).
 \tag{L-19873.27}
\]

No factor of the finite degree is lost because the intertwining remainder is measured in Hilbert--Schmidt norm before spectral extraction.

## 6. What the current exterior-cardinal reservoir does not yet prove

`L-19862` proves a constant quotient floor and exponentially small target residual for one exact exterior-cardinal reservoir.  It does not estimate (L-19873.24).

This distinction is load bearing.  Making the complement Gram nearly isotropic does not control the scaling commutator: `R-19850` gives the exact parity-area defect.  Conversely, forcing derivative compatibility on the target's complete Krylov orbit creates additional near-radical directions and destroys a one-line quotient floor unless a new source-specific anisotropic construction is supplied.

Therefore (L-19873.24), rather than another complement eigenvalue estimate, is the precise prime/source theorem still required.

## 7. Lower-semicontinuity firewall

Suppose the finite transforms converge locally uniformly to `Xi`.  If `Xi` has a nonreal zero `rho`, Hurwitz gives a finite zero `rho_j->rho`.  Hence

\[
 \liminf_jV_j
 \ge |\operatorname{Im}\rho|^2.
 \tag{L-19873.28}
\]

Combining this with (L-19873.20) shows that, in a false-RH world,

\[
 \liminf_j
 \left(2\kappa_{W,j}\rho_j+|\lambda_j|\chi_{G,j}\right)
 \ge2\sqrt2\,|\operatorname{Im}\rho|.
 \tag{L-19873.29}
\]

Thus no source construction can make the normalized intertwining error vanish by merely increasing support or precision if an off-line zero persists.  The estimate is a genuine RH-strength theorem, not a routine cardinal-tail bound.

## 8. Proof boundary

- The projected Green-commutator identity and the total vertical-defect estimate are exact.
- The theorem gives a concrete source-side sufficient condition for `V_j->0`, with no unrestricted metric optimization and no inspection of the finite roots.
- It does not prove the arithmetic derivative-intertwining rate (L-19873.25) for the current source reservoir.
- In particular, no accepted proof of RH is claimed.
