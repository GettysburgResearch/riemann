# L-91307 — The prime scattering tangent has an explicit tail-Hankel Julia dilation

Claim ID: `L-91307`  
Status: **PROVED EXACT FIRST-CHAOS/HARDY EMBEDDING AT A FIXED SAFE SCALE**  
Created: 2026-08-12  
Depends on: `L-91029`, `L-91035`, `L-91036`, `L-91306`  
RH status: **unproved**

## 1. Purpose

The source-linear target cannot use higher Poisson chaoses by `L-91036`. This
lemma identifies the actual ordinary-prime first chaos of Suzuki's scattering
connection, proves that its Hardy output is a literal tail-Hankel operator, and
constructs a positive-metric Julia dilation with an explicit auxiliary
reserve.

This is the requested prime-output embedding at tangent level. The completed
gamma/pole gluing and final Fisher-curvature domination remain as stated in
`L-91306` and corrected `T-91008`.

## 2. Exact ordinary-prime connection measure

Fix `a>1/2`, put

\[
 c_a=a+\frac12,
\]

and let

\[
 Z_a(x)=\frac{\zeta(c_a+ix)}{\zeta(c_a-ix)}.
\]

The absolutely convergent Euler logarithm is

\[
 \log Z_a(x)
 =-2i\sum_{n=p^k}\frac1k n^{-c_a}\sin(x\log n).
 \tag{L-91307.1}
\]

The logarithmic-radius connection is

\[
 \chi_a^{\rm p}(x)=Z_a(x)^{-1}a\partial_aZ_a(x)
 =a\partial_a\log Z_a(x).
\]

Differentiating gives

\[
 \boxed{
 \chi_a^{\rm p}(x)
 =2ia\sum_{n=p^k}\frac{\log n}{k}
 n^{-c_a}\sin(x\log n).
 }
 \tag{L-91307.2}
\]

Since `(log n)/k=Lambda(n)` for `n=p^k`, define the finite positive measure

\[
 \boxed{
 d\beta_a(u)
 =a\sum_{n=p^k}\Lambda(n)n^{-c_a}\delta_{\log n}(du).
 }
 \tag{L-91307.3}
\]

Then

\[
 \boxed{
 \chi_a^{\rm p}(x)
 =\int_0^\infty(e^{ixu}-e^{-ixu})d\beta_a(u).
 }
 \tag{L-91307.4}
\]

The measure `beta_a` is the compensated first-chaos score of the ordinary-zeta
phase. It is not the normalized generalized-Jordan curvature measure of
`L-91037`; `R-91301` records the distinction.

Its total mass is

\[
 \boxed{
 m_a:=\beta_a((0,\infty))
 =a\left(-\frac{\zeta'}{\zeta}(a+1/2)\right).
 }
 \tag{L-91307.5}
\]

## 3. The Hardy block is exactly a tail-Hankel operator

Let `P_+` and `P_-` be the two Hardy projections in the convention of
`L-91306`. Under the Fourier identifications

\[
 H^2_+\simeq L^2(0,\infty),
 \qquad
 H^2_-\simeq L^2(0,\infty),
\]

with the second copy reflected, the Hankel block
`P_+M_(chi_a^p)P_-` is, up to the harmless convention-dependent overall
sign/reflection, the operator

\[
 \boxed{
 (\mathsf H_{\beta_a}g)(t)
 =\int_{(t,\infty)}g(u-t)d\beta_a(u),
 \qquad t>0.
 }
 \tag{L-91307.6}
\]

Indeed an input frequency `-s<0` reaches output frequency `t>0` only through
the positive Fourier atom `u=t+s`; the negative atom in (L-91307.4) remains in
the negative Hardy sector. Hence the matrix coefficient is exactly
`d beta_a(t+s)`.

This is a fully polarized operator identity, not a diagonal estimate.

## 4. Canonical triangular source space

For a finite positive measure `beta` on `(0,infinity)` put

\[
 W(t)=\beta((t,\infty)).
 \tag{L-91307.7}
\]

Let

\[
 \Omega=\{(t,u):0<t<u\},
 \qquad
 \mathcal S_\beta=L^2(\Omega,dt\,d\beta(u)).
\]

For `g in L2((0,infinity),W(v)dv)` define

\[
 \boxed{
 (V_\beta g)(t,u)=\mathbf1_{t<u}g(u-t).
 }
 \tag{L-91307.8}
\]

Fubini gives

\[
 \boxed{
 \|V_\beta g\|_{\mathcal S_\beta}^2
 =\int_0^\infty W(v)|g(v)|^2dv.
 }
 \tag{L-91307.9}
\]

Define the coisometry

\[
 \boxed{
 (P_\beta F)(t)
 =W(t)^{-1/2}\int_{u>t}F(t,u)d\beta(u).
 }
 \tag{L-91307.10}
\]

All formulas are restricted to `W(t)>0`; the zero-tail part is trivial. Its
adjoint is

\[
 (P_\beta^*h)(t,u)=\mathbf1_{t<u}W(t)^{-1/2}h(t),
\]

so `P_beta P_beta*=I`.

The normalized tail-Hankel contraction is

\[
 \boxed{
 Y_\beta=P_\beta V_\beta,
 \qquad
 (Y_\beta g)(t)=W(t)^{-1/2}(\mathsf H_\beta g)(t).
 }
 \tag{L-91307.11}
\]

## 5. Exact conditional-variance identity

Put

\[
 h(t)=\mathsf H_\beta g(t),
 \qquad
 \overline g_t=\frac{h(t)}{W(t)}.
\]

Orthogonal projection onto `Ran(P_beta*)` gives

\[
 \boxed{
\begin{aligned}
 \int_0^\infty W(v)|g(v)|^2dv
 ={}&\int_0^\infty\frac{|h(t)|^2}{W(t)}dt\\
 &+\int_0^\infty\int_{u>t}
 |g(u-t)-\overline g_t|^2d\beta(u)dt.
\end{aligned}}
 \tag{L-91307.12}
\]

The polarized form is

\[
\begin{aligned}
 \int Wg\overline k
 ={}&\int\frac{h_g\overline{h_k}}W\\
 &+\int\!\int_{u>t}
 (g(u-t)-\overline g_t)
 \overline{(k(u-t)-\overline k_t)}d\beta(u)dt.
\end{aligned}
 \tag{L-91307.13}
\]

Thus all cross-carrier information survives before taking a norm.

## 6. Explicit Julia dilation on ordinary Hardy space

Assume

\[
 \boxed{0<W(t)\le1.}
 \tag{L-91307.14}
\]

For `g in L2(0,infinity)` define

\[
\begin{aligned}
 D_0g(v)&=\sqrt{1-W(v)}g(v),\\
 D_1g(t,u)&=\mathbf1_{t<u}
 \left[g(u-t)-\frac{h(t)}{W(t)}\right],\\
 D_2g(t)&=\sqrt{W(t)^{-1}-1}h(t).
\end{aligned}
 \tag{L-91307.15}

Combining

\[
 \int|g|^2=\int W|g|^2+\int(1-W)|g|^2
\]

and

\[
 \int\frac{|h|^2}W=\int|h|^2+
 \int(W^{-1}-1)|h|^2
\]

with (L-91307.12) yields

\[
 \boxed{
 \|g\|_2^2
 =\|\mathsf H_\beta g\|_2^2
 +\|D_0g\|_2^2
 +\|D_1g\|_{\mathcal S_\beta}^2
 +\|D_2g\|_2^2.
 }
 \tag{L-91307.16}
\]

Therefore

\[
 \boxed{
 \mathcal U_\beta g
 =(\mathsf H_\beta g,D_0g,D_1g,D_2g)
 }
 \tag{L-91307.17}
\]

is a positive-metric isometry into one Hardy output plus three explicit
auxiliary spaces. No unknown square root or already-assumed Weil matrix occurs.

## 7. One explicit fixed safe scale

Take

\[
 \boxed{a_0=4,\qquad c_{a_0}=\frac92.}
\]

For `c>1`, monotone integral comparison gives

\[
 -\frac{\zeta'}{\zeta}(c)
 \le \log2\,2^{-c}
 +2^{1-c}\left[
 \frac{\log2}{c-1}+\frac1{(c-1)^2}
 \right].
 \tag{L-91307.18}
\]

Using `log 2<1`, `2^(-9/2)<1/16` and `2^(-7/2)<1/8`,

\[
 \boxed{
 m_4<4\left[
 \frac1{16}+\frac18\left(\frac27+\frac4{49}\right)
 \right]
 =\frac{85}{196}<1.
 }
 \tag{L-91307.19}
\]

Hence `W_4(t)<1` for every `t`, and the explicit Julia isometry applies to the
actual ordinary-prime scattering tangent at this one fixed safe scale.

## 8. Two-sided and delayed completion

Reflecting (L-91307.17) gives the anti-causal Hardy orientation. Direct sum of
the causal and reflected isometries gives a two-sided positive-metric prime
output. Carrier modulations, delay multipliers and the bridge extension act by
unitaries on the Hardy factors, so the operator identity preserves every
finite cross-carrier/cross-delay polarization.

Through `L-91306`, the explicit gamma/pole boundary factor acts as the
covariant unitary connection placing these prime outputs inside Suzuki's
completed normal tangent.

## 9. Exact scope

```text
actual ordinary-prime scattering score measure          EXACT
prime score -> Hardy tail-Hankel block                   EXACT
positive triangular first-chaos source                  EXACT
fully polarized conditional-variance identity           EXACT
explicit Julia isometry at a0=4                          EXACT
two-sided reflected/delayed prime output                 EXACT
gamma/pole placement as covariant connection             L-91306
completed Fisher curvature >= squared total shape        OPEN / RH-EQUIVALENT
Riemann Hypothesis                                       UNPROVED
```
