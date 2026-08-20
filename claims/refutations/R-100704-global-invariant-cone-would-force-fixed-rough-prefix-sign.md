# R-100704 — A global invariant-cone proof would force a false fixed-rough-prefix sign theorem

Status: **BINDING FIREWALL**  
RH status: **unproved**

The attempted proof of `BTHC100700` sought to show that the balanced homotopy derivative preserves the cone `F(s)>=0`, `F(s)/s` nonincreasing for every `0<=t<=1`.  For the critical Peano kernel

\[
\kappa(s)=1-(1-s)_+^2,
\]

one has exactly

\[
s\kappa'(s)-\kappa(s)=-\min(s^2,1).
\]

At `t=1`, the induced derivative-cone packet for a finite rough-prime set is precisely the reciprocal Möbius prefix kernel

\[
\prod_p(I-p^{-1}V_p)\mathbf 1_{x<1}.
\]

On exhaustion of any fixed rough-prime threshold this becomes the fixed rough reciprocal prefix

\[
A_z(Y)=\sum_{\substack{n\le Y\\P^-(n)\ge z}}\frac{\mu(n)}n.
\]

The repository's fixed-rough-prefix Landau firewall proves that no fixed `z` prefix may be eventually one-signed: its Mellin transform retains all reciprocal-zeta poles up to a finite Euler factor. Hence a theorem forcing `A_z(Y)>=0` for all sufficiently large `Y` would itself imply the forbidden one-sign conclusion.

Therefore the desired global invariant cone cannot hold through `t=1`.  The positive local transition theorem `L-100704` remains valid, but it cannot be promoted to pointwise positivity after arbitrary completion by the other rough primes.

The surviving task must preserve cancellation in the homotopy parameter `t` or in double-owner rectangles; it may not replace that cancellation by a pointwise rough-prefix sign assertion.
