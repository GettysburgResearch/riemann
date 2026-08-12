# L-91307 — The prime scattering tangent has an explicit tail-Hankel Julia dilation

Claim ID: `L-91307`  
Status: **PROVED EXACT ORDINARY-PRIME FIRST-CHAOS/HARDY DILATION AT A FIXED SAFE SCALE**  
Created: 2026-08-12  
Corrected: 2026-08-12  
Depends on: `L-91029`, `L-91035`, `L-91036`, `L-91306`, `L-91401`, `R-91402`  
RH status: **unproved**

## 1. Exact ordinary-prime connection measure

Fix `a>1/2`, put

\[
 c_a=a+\frac12,
\]

and define

\[
 Z_a(x)=\frac{\zeta(c_a+ix)}{\zeta(c_a-ix)}.
\]

The absolutely convergent Euler logarithm gives

\[
 \log Z_a(x)
 =-2i\sum_{n=p^k}\frac1k n^{-c_a}\sin(x\log n).
\tag{L-91307.1}
\]

Its logarithmic-radius connection is

\[
 \chi_a^{\rm p}(x)
 =a\partial_a\log Z_a(x)
 =2ia\sum_{n=p^k}rac{\log n}{k}
 n^{-c_a}\sin(x\log n).
\tag{L-91307.2}
\]

Since `(log n)/k=Lambda(n)` on prime powers, define

\[
 \boxed{
 d\beta_a(u)
 =a\sum_{n=p^k}\Lambda(n)n^{-c_a}
  \delta_{\log n}(du).
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

The total mass is

\[
 \boxed{
 m_a=\beta_a((0,\infty))
 =a\left(-\frac{\zeta'}{\zeta}(a+1/2)\right).
 }
\tag{L-91307.5}
\]

This is the actual ordinary-prime scattering-score first chaos.  It is not the
normalized generalized-Jordan curvature measure; see `R-91301`.

## 2. Exact Hardy tail-Hankel block

After the standard reflection identifying the negative Hardy input with
`L^2(0,infinity)`, the block `P_+M_(chi_a^p)P_-` is

\[
 \boxed{
 (\mathsf H_{\beta_a}g)(t)
 =\int_{(t,\infty)}g(u-t)d\beta_a(u),
 \qquad t>0.
 }
\tag{L-91307.6}
\]

Indeed, an input frequency `-s<0` reaches output frequency `t>0` through the
positive atom `u=t+s`; the negative atom in (L-91307.4) remains in the negative
Hardy sector.  The matrix coefficient is therefore `d beta_a(t+s)`.

This is an operator identity retaining every carrier cross term.

## 3. Triangular first-chaos source

For a finite positive measure `beta` on `(0,infinity)`, put

\[
 W(t)=\beta((t,\infty)),
 \qquad
 \Omega=\{(t,u):0<t<u\}.
\tag{L-91307.7}
\]

Let

\[
 \mathcal S_\beta=L^2(\Omega,dt\,d\beta(u))
\]

and define

\[
 (V_\beta g)(t,u)=\mathbf1_{t<u}g(u-t).
\tag{L-91307.8}
\]

Then

\[
 \|V_\beta g\|_{\mathcal S_\beta}^2
 =\int_0^\infty W(v)|g(v)|^2dv.
\tag{L-91307.9}
\]

The coisometry

\[
 (P_\beta F)(t)
 =W(t)^{-1/2}\int_{u>t}F(t,u)d\beta(u)
\tag{L-91307.10}
\]

satisfies

\[
 P_\beta V_\beta g
 =W^{-1/2}\mathsf H_\beta g.
\tag{L-91307.11}
\]

## 4. Fully polarized conditional variance

Write

\[
 h_g(t)=\mathsf H_\beta g(t),
 \qquad
 \bar g_t=h_g(t)/W(t).
\]

Orthogonal projection onto the conditional-mean fibre gives

\[
 \boxed{
\begin{aligned}
 \int W(v)|g(v)|^2dv
 ={}&\int\frac{|h_g(t)|^2}{W(t)}dt\\
 &+\iint_{u>t}|g(u-t)-\bar g_t|^2d\beta(u)dt.
\end{aligned}}
\tag{L-91307.12}
\]

The polarized identity is

\[
 \boxed{
\begin{aligned}
 \int Wg\bar k
 ={}&\int\frac{h_g\overline{h_k}}W\\
 &+\iint_{u>t}
 (g(u-t)-\bar g_t)
 \overline{(k(u-t)-\bar k_t)}d\beta(u)dt.
\end{aligned}}
\tag{L-91307.13}
\]

Thus no off-diagonal carrier information is discarded.

## 5. Explicit Julia dilation

Assume

\[
 0<W(t)\le1.
\tag{L-91307.14}
\]

Define

\[
 D_0g(v)=\sqrt{1-W(v)}g(v),
\]

\[
 D_1g(t,u)=\mathbf1_{t<u}
 \left[g(u-t)-\frac{h_g(t)}{W(t)}\right],
\]

and

\[
 D_2g(t)=\sqrt{W(t)^{-1}-1}\,h_g(t).
\tag{L-91307.15}
\]

Then

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

Hence

\[
 \boxed{
 \mathcal U_\beta g
 =(\mathsf H_\beta g,D_0g,D_1g,D_2g)
 }
\tag{L-91307.17}
\]

is an explicit positive-metric isometry.

## 6. One fixed safe scale

Take

\[
 a_0=4,
 \qquad
 c_{a_0}=\frac92.
\]

For `c>1`, monotone integral comparison yields

\[
 -\frac{\zeta'}{\zeta}(c)
 \le \log2\,2^{-c}
 +2^{1-c}\left[
  \frac{\log2}{c-1}+\frac1{(c-1)^2}
 \right].
\tag{L-91307.18}
\]

Using `log 2<1`, `2^(-9/2)<1/16`, and `2^(-7/2)<1/8`,

\[
 \boxed{
 m_4<4\left[
  \frac1{16}+\frac18\left(\frac27+\frac4{49}\right)
 \right]
 =\frac{85}{196}<1.
 }
\tag{L-91307.19}
\]

Thus `W_4(t)<1` for all `t`, and the Julia dilation applies to the actual
ordinary-prime scattering tangent at one fixed safe scale.

## 7. Gamma/pole placement

On the real boundary write

\[
 \Theta_a=\Gamma_aZ_a.
\]

`L-91306` proves that `Gamma_a` enters the normal tangent as a skew covariant
connection in a moving-unitary factorization.  Therefore the prime block and
the gamma/pole derivative are placed in one observed completed boundary
tangent without dropping their interference.

This is an output-level covariant identity.  It does not identify the prime
Poisson source law with the completed xi Fisher law; that shortcut is refuted
by `R-91402`.

## 8. Correct two-sided and delayed extension

Reflection gives the anti-causal prime Hardy block.  A raw positive delay does
not generally preserve Suzuki's model space.  Instead, `L-91401` gives

\[
 S_\tau g=T_\tau g+M_{\Theta_a}R_\tau g
\tag{L-91307.20}
\]

with

\[
 T_\tau^*T_\tau+R_\tau^*R_\tau=I.
\tag{L-91307.21}
\]

For arbitrary mixed delays,

\[
 \langle S_{\tau_i}g_i,S_{\tau_j}g_j\rangle
 =\langle T_{\tau_i}g_i,T_{\tau_j}g_j\rangle
  +\langle R_{\tau_i}g_i,R_{\tau_j}g_j\rangle.
\tag{L-91307.22}
\]

Thus every cross-delay term is preserved by the resident compressed delay plus
explicit leakage.  Raw delay invariance is not claimed.

## 9. Exact scope

```text
ordinary-prime scattering-score measure              EXACT
prime score -> Hardy tail-Hankel block               EXACT
positive triangular first-chaos source               EXACT
fully polarized conditional-variance identity        EXACT
explicit Julia isometry at a0=4                      EXACT
gamma/pole observed covariant placement              EXACT
raw-delay invariance                                 REFUTED
compressed two-sided delayed extension               EXACT
prime Poisson source = completed Fisher source       REFUTED
renormalized common-source completion                OPEN
common-source defect = delayed screw/Weil Gram       OPEN / RH-BEARING
Riemann Hypothesis                                   UNPROVED
```
