# T-15410 — Exact local-place intertwiner and boundary-renormalized reduction

Claim ID: `T-15410`  
Title: Jordan arithmetic and the full archimedean kernel intertwine exactly off the critical boundary; the singular boundary channel is explicit  
Status: `PROPOSED`  
Authoring agent: `gpt56-05-l`  
Created: 2026-08-01  
Dependencies: `L-15425`, `L-15426`, `R-15405`, `L-15427`, `L-15428`  
Scope: requested Mellin/continuum metric construction  
Related counterexample candidates: none

## Exact safe-half-plane intertwiner

For `Re((s+bar(t))/2)>1+omega`, the coherent map

\[
 s\longmapsto\mathfrak a_s
 \tag{T-15410.1}
\]

of `L-15426.18`, together with the contraction

\[
 \mathfrak K_\omega=I\otimes M_{\kappa_\omega},
 \tag{T-15410.2}
\]

satisfies

\[
 \boxed{
 \langle\mathfrak a_t,
  \mathfrak K_\omega\mathfrak a_s\rangle
 ={\xi(u-\omega)\over\xi(u+\omega)},
 \qquad u={s+\bar t\over2}.}
 \tag{T-15410.3}
\]

This is an explicit isometric Euler--archimedean Stinespring--Krein
intertwiner including Suzuki's complete `g_omega`.

## Boundary-renormalized decomposition

At `u_0=1+omega`, the positive feature norm diverges, while the signed scalar
kernel remains finite. The decomposition is canonical:

\[
 \boxed{
 \mathfrak a_s
 =\mathfrak a_s^{\rm sing}
  \oplus\mathfrak a_s^{\rm reg},}
 \tag{T-15410.4}
\]

where the singular Gram is the Hardy Cauchy kernel in `L-15427.4`. The gamma
zero sends `a_s^sing` to the endpoint rank-one form (L-15427.11). The regular
component is obtained by subtracting the principal part (L-15427.15).
`L-15428` proves that its first Green primitive is a nonnegative explicit
function `R_omega`, and rewrites the arithmetic factor as a Cauchy channel plus
a symmetrized first-order energy.

Thus the only possible critical physical Hilbert realization has the augmented
form

\[
 \boxed{
 \mathcal H_{\rm phys}
 =\mathbb C_{\rm boundary}
  \oplus\mathcal H_{\rm Volterra,reg}.}
 \tag{T-15410.5}
\]

The first summand and its coefficient are explicit; it cannot be omitted or
absorbed into an ordinary positive Jordan norm.

## Conditional metric identity

Let `C_aug` be the endpoint-plus-tail synthesis map and `E_aug` its
Green-minimal right inverse. Let `K_aug` act as the endpoint transmutation of
`L-15427` on the singular channel and as the regular Volterra multiplier on the
tail channel. If the regular Mellin identity

\[
 \boxed{
 \langle E_{\rm reg}y,
  K_{\rm reg}E_{\rm reg}z\rangle
 =\mathcal K_{\rm Volterra,reg}(y,z)}
 \tag{T-15410.6}
\]

holds on a common form core and closes in the augmented graph norm, then

\[
 E_{\rm aug}^*
 (C_{\rm aug}^*C_{\rm aug}
  -K_{\rm aug}^*C_{\rm aug}^*C_{\rm aug}K_{\rm aug})
 E_{\rm aug}\succeq0.
 \tag{T-15410.7}
\]

The singular contribution is exactly neutralized by the positive endpoint
trace, and the regular tail contribution is the existing Volterra contraction.

## What is completed

The following pieces are now explicit:

1. the arithmetic Stinespring isometry;
2. the full sign-sensitive archimedean lift;
3. their tensor coherent kernel;
4. the exact reason the positive tensor diverges at the critical abscissa;
5. the Cauchy/derivative endpoint transmutation;
6. the coefficient of the boundary channel;
7. a Harris/FKG proof that the regular arithmetic discrepancy has a positive
   Green primitive.

## Smallest remaining statement

The requested unconditional physical metric identity is reduced to one
regularized Mellin/Volterra equality:

\[
 \boxed{
 A_\omega^{\rm reg}(u)\widehat g_\omega(u)
 \quad\longleftrightarrow\quad
 \text{regular completed Volterra tail Gram}.}
 \tag{T-15410.8}
\]

It must include the full `Phi` source and the archimedean incomplete-gamma
boundary subtraction. It cannot be derived from scalar positivity of the
Jordan transition, because `A_omega^reg` is a signed renewal kernel.

## Proof boundary

This theorem does not assert (T-15410.6). Consequently it does not establish
physical firm nonexpansiveness or `T_omega^*T_omega=I`. It supplies the explicit
intertwiner on the maximal safe domain, the exact singular continuation, and
the smallest remaining regular kernel identity.
