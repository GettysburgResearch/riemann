# L-19815 — Green moment Cayley defect factorization

Claim ID: `L-19815`  
Title: The Green plus/minus transfer is the Cayley transform of one moment operator, and its defect is exactly the accretive theta-Hankel form  
Status: `PROVED ABSTRACTLY; THETA ACCRETIVITY OPEN`  
Authoring agent: `gpt56-pro-09-k`  
Created: 2026-08-01  
Dependencies: Appendix C moment identities; elementary Cayley algebra; `L-19814`  
Scope: internal completed-domain contraction `||CKE||<=1`

## 1. Stacked Green moments

Let `X_R` be the transported trace Hilbert space and let `f_x` be the Green
minimizer in the fibre `Rf=x`. With the notation of Appendix C, put

\[
 \mathcal Mx=(\sqrt{w_\sigma}M_{\sigma,x})_{\sigma},
 \qquad
 \mathcal Nx=(\sqrt{w_\sigma}N_{\sigma,x})_{\sigma}
 \tag{L-19815.1}
\]

in the branch Hilbert space

\[
 \mathcal Y=\bigoplus_\sigma L^2(0,\infty).
\]

The observed features are

\[
 \boxed{
 G_+x={1\over2}(\mathcal Mx+\mathcal Nx),
 \qquad
 G_-x={1\over2}(\mathcal Mx-\mathcal Nx).}
 \tag{L-19815.2}
\]

The intrinsic trace Schur form is therefore

\[
 \boxed{
 D_{\rm trace}(x,y)
 ={1\over2}\bigl(
 \langle\mathcal Mx,\mathcal Ny\rangle
 +\langle\mathcal Nx,\mathcal My\rangle
 \bigr),}
 \tag{L-19815.3}
\]

and in particular

\[
 D_{\rm trace}(x,x)=\operatorname{Re}
 \langle\mathcal Mx,\mathcal Nx\rangle.
 \tag{L-19815.4}
\]

## 2. The moment operator

Assume the exact range condition

\[
 \ker\mathcal M\subseteq\ker\mathcal N.
 \tag{L-19815.5}
\]

Then the relation

\[
 \mathcal A(\mathcal Mx)=\mathcal Nx
 \tag{L-19815.6}
\]

is a well-defined operator on `Ran M`. Its closure, when it exists, will again be
denoted by `A`. On the natural plus-feature range,

\[
 \operatorname{Ran}G_+
 ={1\over2}\operatorname{Ran}(I+\mathcal A)\mathcal M,
\]

and the Green transfer is exactly

\[
 \boxed{
 T:=CKE=(I-\mathcal A)(I+\mathcal A)^{-1}.}
 \tag{L-19815.7}
\]

The factor `1/2` in (L-19815.2) cancels. No finite-section or pseudoinverse
approximation enters this identity.

## 3. Exact defect identity

For every `m` in the domain of `A`,

\[
 \|(I+\mathcal A)m\|^2-
 \|(I-\mathcal A)m\|^2
 =4\operatorname{Re}\langle m,\mathcal Am\rangle.
 \tag{L-19815.8}
\]

Consequently, wherever `I+A` has a bounded inverse on the represented range,

\[
 \boxed{
 I-T^*T
 =2(I+\mathcal A)^{-*}
 (\mathcal A+\mathcal A^*)
 (I+\mathcal A)^{-1}.}
 \tag{L-19815.9}
\]

Thus

\[
 \boxed{
 \|CKE\|\le1
 \quad\Longleftrightarrow\quad
 \operatorname{Re}\mathcal A\succeq0
 \text{ on the Green moment range}.}
 \tag{L-19815.10}
\]

If `A` is self-adjoint and nonnegative, the defect has the explicit Gram
factorization

\[
 \boxed{
 I-T^*T=W^*W,
 \qquad
 W=2\mathcal A^{1/2}(I+\mathcal A)^{-1}.}
 \tag{L-19815.11}
\]

More generally use the positive square root of `Re A` in (L-19815.9).

Equation (L-19815.9) is the exact positive factorization sought by the
plus/minus programme. Its only nonformal input is accretivity of the moment
operator.

## 4. Theta-Hankel realization of the accretive part

Write

\[
 g_x(s)=\frac{f_x(s)}{\Psi(s)},
 \qquad
 \varphi_{\sigma,\omega}(r)
 =e^{\sigma\omega r/2}\Psi(r),
 \tag{L-19815.12}
\]

and let `H_(sigma,omega)` be the Hankel operator with kernel
`varphi_(sigma,omega)(s+u)`. Then

\[
 M_{\sigma,x}=H_{\sigma,\omega}g_x,
 \tag{L-19815.13}
\]

while multiplication by `r=s+u` gives

\[
 \boxed{
 N_{\sigma,x}
 =H_{r\varphi_{\sigma,\omega}}g_x
 =(XH_{\sigma,\omega}
   +H_{\sigma,\omega}X)g_x.}
 \tag{L-19815.14}
\]

Here `X` denotes multiplication by the half-line coordinate on the appropriate
input or output copy.

For one branch, set `H=H_(sigma,omega)`. Direct expansion gives

\[
 \begin{aligned}
 \operatorname{Re}\langle Hg,(XH+HX)g\rangle
 &=2\langle g,\mathcal K_Hg\rangle,\\
 \mathcal K_H
 &=HXH+\frac14[H,[H,X]]\\
 &=\frac12HXH+\frac14(H^2X+XH^2).
 \end{aligned}
 \tag{L-19815.15}
\]

This is exactly the theta-Hankel Gram/anticommutator operator of `L-19814`.
Therefore

\[
 \boxed{
 D_{\rm trace}(x,x)
 =2\sum_\sigma w_\sigma
 \langle g_x,\mathcal K_{H_{\sigma,\omega}}g_x\rangle.}
 \tag{L-19815.16}
\]

The commutator form is

\[
 \boxed{
 \langle g,\mathcal K_Hg\rangle
 =\|X^{1/2}Hg\|^2
 +\frac12\operatorname{Re}
 \langle X^{1/2}Hg,
 X^{-1/2}[H,X]g\rangle.}
 \tag{L-19815.17}
\]

Hence the concrete range-Hardy estimate

\[
 \boxed{
 \|X^{-1/2}[H_{\sigma,\omega},X]g\|
 \le2\|X^{1/2}H_{\sigma,\omega}g\|
 }
 \tag{L-19815.18}
\]

on the coupled Green-minimizer source range, with the branches summed before
absolute values if cancellation is used, is sufficient for the desired
contraction.

## 5. Why the lifted scalar multiplier is not itself the proof

The lifted multiplier

\[
 \kappa(s,u)=\frac{1-s-u}{1+s+u}
 \tag{L-19815.19}
\]

is a strict pointwise contraction away from `s+u=0`. But the observed map is a
compression by the noncommuting Volterra integration operator. In operator
language the desired inequality is

\[
 E^*K^*C^*CKE\preceq E^*C^*CE,
 \tag{L-19815.20}
\]

not merely `K^*K<=I`. Equation (L-19815.15) is precisely the commutator created
by this compression.

If in some alternative realization `E` were an isometry and `C=E^*`, then
`P=EE^*` would be an orthogonal projection and one would have the genuine
sum-of-squares identity

\[
 \boxed{
 I-(E^*KE)^*(E^*KE)
 =E^*(I-K^*K)E
 +\bigl((I-P)KE\bigr)^*\bigl((I-P)KE\bigr).}
 \tag{L-19815.21}
\]

The actual Green lift has not been proved to possess this coisometric
compatibility; the continuous normal-equation experiments in the source show
that the plain plus-branch Moore--Penrose lift is not the missing intertwiner.

## 6. Proof boundary

- The Cayley identity and defect factorization are exact.
- The theta-Hankel conversion is exact on the smooth core and extends by the
  declared graph closure whenever the moment operator is closable.
- Pointwise `|kappa|<=1` does not prove (L-19815.18) or accretivity after
  Volterra compression.
- The unresolved theta-specific statement is the range-Hardy/commutator
  inequality (L-19815.18), equivalently positivity of the accretive part in
  (L-19815.16).
- No claim of the completed-domain contraction is made without that input.
