# L-15612 — Dimension-uniform local-Weyl floor for shrinking boundary packets

Claim ID: `L-15612`  
Title: A graph-bounded shrinking packet has zero-side Weil form `(log R)G+O(G)` independently of its dimension  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-09-e`  
Created: 2026-07-31  
Dependencies: Riemann--von Mangoldt with an explicit remainder; Plancherel; repository `L-16209`; elementary localization-operator calculus  
Scope: the same-end/local part of the endpoint-visible block  
Related counterexample candidates: none

## 1. Fixed profile interval

Let `I_0=(-b,b)` with `b>0`. For `f in H_0^1(I_0)`, use

\[
 F(z)=\int_{I_0}f(x)e^{-izx}\,dx,
 \qquad
 \|F\|_2^2=2\pi\|f\|_2^2.
 \tag{1}
\]

Write every nontrivial zero as

\[
 \rho=\frac12+is_\rho,
 \qquad |\operatorname{Im}s_\rho|<\frac12.
\]

For `R>=2`, define the scaled zero-side form

\[
 \mathcal Z_R(f,g)
 =\frac1R\sum_\rho
 F_f(s_\rho/R)
 \overline{F_g(\overline{s_\rho}/R)},
 \tag{2}
\]

with multiplicity and the symmetric convention inherited from the Weil form.

Assume an explicit Riemann--von Mangoldt remainder

\[
 |N(T)-M(T)|\le A\log(T+2)
 \tag{3}
\]

for the declared counting convention.

## 2. Uniform graph class

Let `V_R subset H_0^1(I_0)` be any finite-dimensional space, of arbitrary
rank, satisfying

\[
 \boxed{
 \|f'\|_2\le M_R\|f\|_2
 \quad(f\in V_R).}
 \tag{4}
\]

Then there is an explicit constant `C_(A,b)` such that, for all `f in V_R`,

\[
\boxed{
\begin{aligned}
 \mathcal Z_R(f,f)
 ={}&(\log R)\|f\|_2^2\\
 &+\frac1{2\pi}\int_{\mathbb R}
   \log\frac{|x|}{2\pi}|F(x)|^2\,dx
 +\mathcal E_R(f),
\end{aligned}}
 \tag{5}
\]

and

\[
 \boxed{
 |\mathcal E_R(f)|
 \le
 C_{A,b}\frac{\log R}{R}(1+M_R)\|f\|_2^2.}
 \tag{6}
\]

The estimate includes every possible off-critical horizontal displacement and
does not assume RH.

## 3. Explicit lower floor

The negative part of the logarithmic integral is uniformly bounded. Since

\[
 |F(x)|^2\le2b\|f\|_2^2
\]

and `log(|x|/(2pi))` is negative only on `|x|<2pi`,

\[
 \frac1{2\pi}\int
 \log\frac{|x|}{2\pi}|F(x)|^2dx
 \ge-4b\|f\|_2^2.
 \tag{7}
\]

Therefore

\[
 \boxed{
 \mathcal Z_R|_{V_R}
 \succeq
 \left[
 \log R-4b
 -C_{A,b}\frac{\log R}{R}(1+M_R)
 \right]G_R,}
 \tag{8}
\]

where `G_R` is the ordinary `L2` Gram on the packet.

In particular, if

\[
 \boxed{
 M_R\frac{\log R}{R}\longrightarrow0,}
 \tag{9}
\]

then

\[
 \lambda_{\min}(\mathcal Z_R,G_R)
 =\log R+O(1)
 \tag{10}
\]

uniformly in the packet dimension.

## 4. Translation and boundary dilation

For a real center `x_0`, define the unitary shrinking packet

\[
 (U_{R,x_0}f)(t)=R^{1/2}f(R(t-x_0)).
 \tag{11}
\]

Its transform is

\[
 \widehat{U_{R,x_0}f}(z)
 =R^{-1/2}e^{-ix_0z}F(z/R).
 \tag{12}
\]

In the Hermitian zero-side pairing the common translation phase cancels:

\[
 e^{-ix_0s_\rho}
 \overline{e^{-ix_0\overline{s_\rho}}}=1.
\]

Thus (5)--(10) apply unchanged to a packet localized at either endpoint.
They do **not** control the cross term between the two endpoints; that cross is
precisely the centered terminal-prime Hankel matrix `E_a` of `L-15610`.

## 5. Proof of the local-Weyl estimate

### Main real-ordinate term

For

\[
 H_f(x)=|F(x)|^2,
\]

Stieltjes summation against the real zero ordinates gives

\[
 \frac1R\int H_f(t/R)dN(t).
\]

Insert `N=M+S`, with `M'(t)=(2pi)^-1 log(t/(2pi))`. The change of variables
`t=Rx` gives the first two terms of (5).

For the error, integration by parts gives

\[
 -\frac1R\int S(Rx)H_f'(x)dx.
 \tag{13}
\]

The support bound and Plancherel yield

\[
 \|F\|_2\ll\|f\|_2,
 \qquad
 \|F'\|_2\ll_b\|f\|_2,
\]

\[
 \|xF\|_2\ll\|f'\|_2,
 \qquad
 \|xF'\|_2\ll_b\|f\|_2+\|f'\|_2.
 \tag{14}
\]

Consequently

\[
 \int (1+\log(2+|x|))|H_f'(x)|dx
 \ll_b(1+M_R)\|f\|_2^2.
 \tag{15}
\]

Equations (3), (13), and (15) give (6) for the real ordinates.

### Off-critical displacement

Write

\[
 s_\rho=\gamma_\rho+i\eta_\rho,
 \qquad |\eta_\rho|<1/2.
\]

The arguments of the profiles in (2) differ from the real ordinate by at most
`1/(2R)`. Taylor's formula in the strip, together with the same support and
`H1` estimates as (14), shows that the induced profile and first-derivative
change in the weighted `W^{1,1}` norm of (15) is

\[
 O_b\left(\frac{1+M_R}{R}\right)\|f\|_2^2.
\]

Stieltjes summation with the total zero count introduces only the additional
`log R` factor already present in (6). This proves the full statement. QED.

## 6. Concentration-packet graph bound

Let `B subset [-Omega,Omega]` and

\[
 K_B=P_{I_0}\mathcal F^{-1}1_B\mathcal F P_{I_0}.
\]

Let `V_(B,eta)` be the spectral subspace of `K_B` for eigenvalues at least
`eta>0`. Then

\[
 \boxed{
 \|f'\|_2\le\frac{\Omega}{\eta}\|f\|_2
 \quad(f\in V_{B,\eta}).}
 \tag{16}
\]

Indeed, on that spectral subspace `K_B` is invertible with inverse norm at most
`eta^-1`. If `g=K_B^{-1}f`, then

\[
 f=P_{I_0}\mathcal F^{-1}1_B\widehat g,
\]

and Bernstein's inequality for a function bandlimited to `B` gives (16).

Therefore the dimension-uniform local floor closes whenever

\[
 \boxed{
 \frac{\Omega_R\log R}{\eta_RR}\longrightarrow0.}
 \tag{17}
\]

Sharp pre-plunge and plunge-count estimates schedule the packet rank but are not
needed in the proof of (16).

## 7. Consequence for the visible block

For the two endpoint packets, each same-end diagonal block has floor

\[
 \log R-O(1)-o(1).
\]

Every possible RH-sensitive exponential effect is confined to the
opposite-endpoint coupling `E_a`; no such effect is hidden in the local diagonal
or in the packet dimension. Thus one may take the local visible moat in
`T-15603` at scale

\[
 \sigma_a^2=\log R_a-O(1),
\]

provided the graph gate (17) and the remaining finite local terms are directed.
The final arithmetic target becomes

\[
 \boxed{
 \theta_a+\omega_a+\omega_a^2/h_a
 <\log R_a-O(1).}
 \tag{18}
\]

## 8. Gap audit

- The local-Weyl estimate is dimension-uniform but requires a uniform graph
  bound; a mere dimension or plunge count is insufficient.
- Opposite-boundary interference is intentionally excluded and is exactly
  `E_a`.
- The constant `C_(A,b)` is explicit once one fixed Riemann--von Mangoldt
  remainder and Fourier convention are inserted; a production certificate must
  record it.
- Equation (17) is a source/profile gate. It must be proved for the actual
  directed visible packet, not inferred from a floating eigenspace.
- This lemma does not bound the terminal-prime matrix and does not prove RH.