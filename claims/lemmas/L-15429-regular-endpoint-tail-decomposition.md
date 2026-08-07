# L-15429 — Exact regular endpoint/tail decomposition at the critical Mellin boundary

Claim ID: `L-15429`  
Title: The completed local-place kernel splits into a positive moving endpoint block and a raw regular tail, with an explicit boundary–tail cross term  
Status: `PROPOSED`  
Authoring agent: `gpt56-05-l`  
Created: 2026-08-01  
Dependencies: `L-15425`--`L-15428`; elementary Laurent algebra  
Scope: full-`Phi` regular augmented joint Gram after the singular Cauchy channel  
Related counterexample candidates: none

## Critical coordinates

Fix `0<omega<1/2`, and put

\[
 u_0=1+\omega,
 \qquad a=2\omega,
 \qquad q=u-u_0,
 \qquad c_\omega={1\over\zeta(1+2\omega)}.
 \tag{L-15429.1}
\]

Write

\[
 A_\omega(q)
 ={\zeta(1+q)\over\zeta(1+2\omega+q)},
 \tag{L-15429.2}
\]

\[
 B_\omega(q)
 =\pi^\omega
 {\Gamma(3/2+q/2)
  \over\Gamma(3/2+\omega+q/2)}.
 \tag{L-15429.3}
\]

Then the completed archimedean ratio is

\[
 \widehat g_\omega(u_0+q)
 =B_\omega(q){q\over q+a}.
 \tag{L-15429.4}
\]

By `L-15428`,

\[
 A_\omega(q)
 ={c_\omega\over q}
 +q\widehat R_\omega(q),
 \qquad
 \widehat R_\omega(q)
 =\int_0^\infty e^{-qt}R_\omega(t)dt,
 \quad R_\omega\ge0.
 \tag{L-15429.5}
\]

## Exact endpoint plus raw-tail split

Multiplying (L-15429.4) and (L-15429.5) gives

\[
 \boxed{
 {\xi(u-\omega)\over\xi(u+\omega)}
 =E_\omega(q)+T_\omega^{\rm raw}(q),}
 \tag{L-15429.6}
\]

where

\[
 \boxed{
 E_\omega(q)
 =c_\omega{B_\omega(q)\over q+a}}
 \tag{L-15429.7}
\]

and

\[
 \boxed{
 T_\omega^{\rm raw}(q)
 ={q^2B_\omega(q)\widehat R_\omega(q)
   \over q+a}.}
 \tag{L-15429.8}
\]

The endpoint term is not merely its value at `q=0`. It is a complete moving
positive kernel.

Let

\[
 E_{\omega,0}
 =E_\omega(0)
 ={c_\omega B_\omega(0)\over a}.
 \tag{L-15429.9}
\]

Then the regular boundary–tail cross term is

\[
 \boxed{
 X_\omega^{\rm bt}(q)
 =E_\omega(q)-E_{\omega,0}
 =c_\omega\left[
 {B_\omega(q)\over q+a}
 -{B_\omega(0)\over a}
 \right].}
 \tag{L-15429.10}
\]

Thus

\[
 {\xi(u-\omega)\over\xi(u+\omega)}
 =E_{\omega,0}
  +X_\omega^{\rm bt}(q)
  +T_\omega^{\rm raw}(q).
 \tag{L-15429.11}
\]

The cross term is load-bearing. It is strictly decreasing at the boundary:

\[
 (X_\omega^{\rm bt})'(0)
 =c_\omega\left[
 {B_\omega'(0)\over a}
 -{B_\omega(0)\over a^2}
 \right]<0,
 \tag{L-15429.12}
\]

because

\[
 {B_\omega'(0)\over B_\omega(0)}
 ={1\over2}\left[
 \psi(3/2)-\psi(3/2+\omega)
 \right]<0.
 \tag{L-15429.13}
\]

By contrast, the raw regular tail has positive first-order pressure; see
`R-15406`.

## Positive moving endpoint dilation

Let

\[
 \beta_\omega(r)
 =e^{-(1+\omega)r}b_\omega(e^{-r})\ge0,
 \tag{L-15429.14}
\]

and

\[
 n_\omega(r)
 =\int_0^r
  e^{-a(r-t)}\beta_\omega(t)dt\ge0.
 \tag{L-15429.15}
\]

Then

\[
 \widehat n_\omega(q)
 ={B_\omega(q)\over q+a},
 \tag{L-15429.16}
\]

so

\[
 E_\omega(q)=c_\omega\widehat n_\omega(q).
 \tag{L-15429.17}
\]

For polarized variables `q=(z+bar(w))/2`, define

\[
 \phi_z(r)
 =e^{-zr/2}\sqrt{c_\omega n_\omega(r)}.
 \tag{L-15429.18}
\]

Then

\[
 \boxed{
 E_\omega(z,w)=\langle\phi_w,\phi_z\rangle.}
 \tag{L-15429.19}
\]

Therefore the entire endpoint block, including every regular boundary–tail
cross term, is an ordinary positive Gram. Splitting off only the constant
`E_(omega,0)` converts that positive joint block into the anchored expression

\[
\begin{aligned}
 X_\omega^{\rm bt}(z,w)
 ={}&\langle\phi_w-\phi_0,
           \phi_z-\phi_0\rangle\\
 &+\langle\phi_w-\phi_0,\phi_0\rangle
  +\langle\phi_0,\phi_z-\phi_0\rangle.
\end{aligned}
 \tag{L-15429.20}
\]

This is the exact regular boundary–tail cross ledger. It cannot be discarded
when the singular endpoint constant is removed.

## One-Green regular kernel

Define

\[
 \boxed{
 G_\omega^{\rm reg}(q)
 ={T_\omega^{\rm raw}(q)\over q}
 ={qB_\omega(q)\widehat R_\omega(q)
   \over q+a}.}
 \tag{L-15429.21}
\]

Let

\[
 m_\omega=n_\omega*R_\omega.
 \tag{L-15429.22}
\]

Since `m_omega(0)=0`,

\[
 \boxed{
 G_\omega^{\rm reg}(q)
 =q\widehat m_\omega(q)
 =\widehat{m_\omega'}(q)}
 \tag{L-15429.23}
\]

in the distributional sense. This is the correct one-Green tail object behind
the augmented Mellin primitive trace. Its positivity is treated in `L-15430`.

## Gap audit

- The decomposition is exact in the half-plane `q>0` and extends
  meromorphically wherever the scalar factors do.
- `E_omega` is a positive kernel; `X_bt` alone is not.
- The raw tail is not a positive Gram; see `R-15406`.
- The regular Volterra-tail metric must include the one-Green primitive and the
  full moving endpoint block, not merely the singular endpoint constant.
