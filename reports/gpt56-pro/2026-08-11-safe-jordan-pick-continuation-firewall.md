# Safe Jordan-to-Pick continuation: exact firewall and corrected criterion

Date: 2026-08-11  
Agent: `gpt56-pro`  
Status: research report; **RH remains unproved**

## Verdict

The requested abstract continuation theorem is false. Positive Jordan/compound-
Poisson structure, positive completed one-Green Hankel kernels, the horizontal
cocycle, and boundary unitarity do not force the de Branges--Rovnyak kernel to be
positive in the moving half-plane.

An exact symmetric polynomial control already has a completely monotone one-Green
ratio while every nontrivial two-point target Pick matrix is indefinite. A stronger
control obtained by multiplying the genuine completed xi function by the same
symmetric factor retains the actual zeta Jordan channel and a positive full
one-Green factorization, but inserts an uncancelled pole in the target half-plane.

The correct theorem is different: positivity of the **exact target Pick matrix** on
any safe uniqueness set already gives the global continuation by finite
Nevanlinna--Pick interpolation plus Montel compactness. Thus the analytic
continuation step is automatic; the entire RH burden is the safe-side Cauchy
multiplier contraction

\[
 C_u-D_{\vartheta_u}C_uD_{\vartheta_u}\succeq0.
\]

## Exact control

For

\[
 F_y(s)=(s-1/2)^2-y^2,
 \qquad 0<u<2y<1,
\]

`F_y(1-s)=F_y(s)` and the quotient `F_y(s-u)/F_y(s)` is unimodular on the
moving boundary. Its safe one-Green function has three positive simple-pole
terms. Nevertheless, at two distinct positive safe parameters `q,r`, the target
Pick determinant is

\[
 -\frac{256u^2(q-r)^2(2y-u)(2y+u)}{D(q)^2D(r)^2}<0.
\]

The local Schwarz--Pick inequality fails by the exact amount

\[
 -\frac{16u(2y-u)(2y+u)}{D(q)^2}.
\]

For the stronger control `xi_y=F_y xi`, choose `y=1/4,u=1/8`. The modified
rational one-Green channel is

\[
 \frac{35/96}{q+1/8}
 +\frac{5/16}{q+3/8}
 +\frac{5/48}{q+7/8}
 +\frac{7/32}{q+9/8},
\]

so the complete beta x Jordan x rational feature measure stays positive. The
arithmetic Jordan factor is unchanged. Yet the horizontal quotient has a pole at
`s=3/4` inside `Re(s)>9/16`.

## Corrected countable theorem

Put

\[
 \vartheta_u(q)=\xi(1+q)/\xi(1+u+q).
\]

RH is equivalent to positivity, for all positive rational `u,q_i`, of

\[
 \left(
 \frac{1-\vartheta_u(q_i)\vartheta_u(q_j)}
      {1+u+q_i+q_j}
 \right)_{i,j}.
\]

All samples lie in `Re(s)>1`. If these matrices are positive, finite
Nevanlinna--Pick interpolation constructs Schur functions for every finite packet;
Montel compactness and the identity theorem produce the unique global continuation.
An off-line zero gives an uncancelled pole for some rational shift `u`, so false RH
forces a finite strict matrix failure.

## Strategic consequence

Do not attempt to continue the one-Green feature kernel by abstract positivity.
Instead construct one of

1. a contractive colligation whose transfer values are `vartheta_u(q)`;
2. a completely positive `u`-evolution for the exact Cauchy Pick kernel;
3. an archimedean Schur complement completing the positive Euler--Bessel block;
4. a direct source-ordered proof of `C-DCD >= 0` on every finite safe packet.

Any one of these proves RH. None is supplied here.
