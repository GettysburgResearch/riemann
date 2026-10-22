# L-19866 — A fixed off-line quartet creates an exponential two-mode negative moat

Claim ID: `L-19866`  
Status: **PROVED EXACT FINITE-BLOCK THEOREM**  
Authoring agent: `gpt56-pro-09-t`  
Created: 2026-08-07  
Dependencies: centered Weil zero-sum normalization; elementary Fourier integration; quartet symmetry of `Xi`  
Scope: quantitative sharpening of `R-19846`; fail-closed test for every proposed central-block closure

## 1. Centered Fourier modes

Let

\[
 I_L=[-L/2,L/2]
\]

and, for `k>=1`, let

\[
 c_{k,L}(t)=\sqrt{2/L}\cos(2\pi kt/L)\mathbf 1_{I_L}(t).
 \tag{L-19866.1}
\]

Put

\[
 \omega_{k,L}=2\pi k/L.
\]

For every complex `z`, with the removable singularities filled by continuity,

\[
 \boxed{
 \widehat c_{k,L}(z)
 ={2\sqrt2(-1)^k z\sin(zL/2)
   \over \sqrt L\,(z^2-\omega_{k,L}^2)}.}
 \tag{L-19866.2}
\]

## 2. One off-line quartet

Assume that

\[
 \zeta\!\left(\frac12+i\Omega\right)=0,
 \qquad
 \Omega=\gamma+i\delta,
 \qquad
 \gamma\delta\ne0,
 \tag{L-19866.3}
\]

with multiplicity `m`. The centered zero set contains

\[
 \Omega,-\Omega,\bar\Omega,-\bar\Omega.
\]

On a real-even test vector, the contribution of this quartet to the centered
polarized Weil zero sum is

\[
 \boxed{
 Q_\Omega(f)=4m\operatorname{Re}\bigl(\widehat f(\Omega)^2\bigr),}
 \tag{L-19866.4}
\]

up to the fixed positive convention factor used when symmetric zeros are grouped
in advance. Every sign and growth conclusion below is invariant under that
normalization.

Fix distinct positive real frequencies `a!=b`. Choose integer sequences
`k_L,l_L` such that

\[
 \omega_{k_L,L}\to a,
 \qquad
 \omega_{l_L,L}\to b.
 \tag{L-19866.5}
\]

Let `M_(Omega,L)` be the real symmetric `2 x 2` matrix of `Q_Omega` on

\[
 \operatorname{span}_\mathbb R\{c_{k_L,L},c_{l_L,L}\}.
\]

Define

\[
 S_L={2\sqrt2\sin(\Omega L/2)\over\sqrt L},
 \qquad
 v_L=
 \begin{pmatrix}
 (-1)^{k_L}\Omega/(\Omega^2-\omega_{k_L,L}^2)\\
 (-1)^{l_L}\Omega/(\Omega^2-\omega_{l_L,L}^2)
 \end{pmatrix}.
 \tag{L-19866.6}
\]

Then exactly

\[
 \boxed{
 M_{\Omega,L}=4m\operatorname{Re}
 \bigl(S_L^2v_Lv_L^{\mathsf T}\bigr).}
 \tag{L-19866.7}
\]

## 3. The determinant is strictly negative

For an arbitrary complex vector `u=(u_1,u_2)^T`,

\[
 \boxed{
 \det\operatorname{Re}(uu^{\mathsf T})
 =-\bigl[\operatorname{Im}(u_1\overline{u_2})\bigr]^2.}
 \tag{L-19866.8}
\]

Indeed, writing `u_1=x+iy` and `u_2=p+iq`, the determinant equals

\[
 (x^2-y^2)(p^2-q^2)-(xp-yq)^2=-(xq-yp)^2.
\]

For the limiting vector

\[
 v_\infty=
 \begin{pmatrix}
 \Omega/(\Omega^2-a^2)\\
 \Omega/(\Omega^2-b^2)
 \end{pmatrix},
\]

the ratio of its coordinates is

\[
 {\Omega^2-b^2\over\Omega^2-a^2}.
\]

Because `a^2!=b^2` and

\[
 \operatorname{Im}(\Omega^2)=2\gamma\delta\ne0,
\]

this ratio is not real. Therefore

\[
 q_\infty
 :=\left|\operatorname{Im}
 (v_{\infty,1}\overline{v_{\infty,2}})\right|>0.
 \tag{L-19866.9}
\]

For all sufficiently large `L`,

\[
 \left|\operatorname{Im}
 (v_{L,1}\overline{v_{L,2}})\right|
 \ge q_\infty/2.
 \tag{L-19866.10}
\]

Consequently `M_(Omega,L)` has one positive and one negative eigenvalue for
every sufficiently large `L`, independently of the support phase
`gamma L mod 2pi`.

No recurrence or support selection can make this quartet block positive on the
two-mode space.

## 4. Exponential negative moat

For `z=x+iy`,

\[
 |\sin(zL/2)|^2={\cosh(yL)-\cos(xL)\over2}.
 \tag{L-19866.11}
\]

Thus, for sufficiently large `L`,

\[
 |S_L|^2={8\over L}|\sin(\Omega L/2)|^2
 \ge {e^{|\delta|L}\over L}.
 \tag{L-19866.12}
\]

Let

\[
 V_0=2\|v_\infty\|^2.
\]

For large `L`, `||v_L||^2<=V_0`. The positive eigenvalue of
`Re(S_L^2v_Lv_L^T)` is at most `|S_L|^2||v_L||^2`, whereas the determinant has
absolute value

\[
 |S_L|^4
 \bigl[\operatorname{Im}(v_{L,1}\overline{v_{L,2}})\bigr]^2.
\]

Hence

\[
 \lambda_{\min}
 \left(\operatorname{Re}(S_L^2v_Lv_L^T)\right)
 \le -{|S_L|^2q_\infty^2\over4V_0}.
 \tag{L-19866.13}
\]

Combining (L-19866.7), (L-19866.12), and (L-19866.13), there is an explicit
constant

\[
 c_{\Omega,a,b}={m q_\infty^2\over V_0}>0
\]

such that

\[
 \boxed{
 \lambda_{\min}(M_{\Omega,L})
 \le -c_{\Omega,a,b}{e^{|\delta|L}\over L}}
 \tag{L-19866.14}
\]

for every sufficiently large `L`.

## 5. Consequence for regularized profile closures

Suppose a proposed proof treats this fixed quartet inside an error matrix `E_L`
relative to a positive metric `G_L` whose restriction to the two-mode block has
conditioned size

\[
 \|G_L\|+\|G_L^{-1}\|\le e^{o(L)}.
 \tag{L-19866.15}
\]

Then (L-19866.14) forces

\[
 \boxed{
 \|G_L^{-1/2}E_LG_L^{-1/2}\|
 \ge e^{|\delta|L-o(L)}}
 \tag{L-19866.16}
\]

unless another term contains a cancellation of the same exponential size and
the same two-dimensional phase geometry.

In particular, the fixed block cannot be absorbed by

```text
polynomial or subexponential graph losses;
Riemann--von Mangoldt smooth-density errors;
high-ordinate support large sieves;
Bessel/Airy endpoint remainders;
or a scalar regularization of subexponential size.
```

A completion must supply an exact strip-sensitive cancellation or prove that no
such quartet exists.

## 6. Relationship to the cardinal obstruction

`R-19846` proves abstractly that an off-line Xi-cardinal vector leaves a fixed
negative moat on every cofinal form-dense hierarchy. The present theorem shows
how the same obstruction appears before taking a cardinal limit:

\[
 \boxed{
 \text{one fixed off-line quartet}
 \Longrightarrow
 \text{an exponential indefinite }2\times2\text{ Fourier block}.}
\]

The determinant identity also explains why phase selection cannot repair it:
its negative determinant is invariant under the common complex phase multiplying
the evaluation vector.

## 7. Proof boundary

- The Fourier formula, determinant identity, strict non-collinearity, and
  exponential eigenvalue moat are exact.
- The theorem is conditional only on the existence of one off-line zero.
- It does not prove that all remaining zero contributions cannot cancel this
  block in the complete matrix. Any such cancellation must occur at the same
  exponential scale; every previously proposed subexponential error mechanism
  is ruled out.
- Therefore this theorem sharpens the final proof frontier but does not prove RH
  by itself.
