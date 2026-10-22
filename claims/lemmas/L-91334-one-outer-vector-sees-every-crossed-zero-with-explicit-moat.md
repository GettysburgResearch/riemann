# L-91334 — One outer vector detects every crossed zero with an explicit positive moat

Claim ID: `L-91334`  
Status: **EXACT QUANTITATIVE MODEL-SPACE VISIBILITY THEOREM**  
Created: 2026-08-12  
Depends on: `L-91333`; standard half-plane reproducing kernels  
RH status: **unproved**

## 1. Right-half-plane normalization

Work in

\[
\mathbb H=\{z:\Re z>0\}
\]

with Hardy norm

\[
\|f\|_{H^2(\mathbb H)}^2
=\frac1{2\pi}\int_{\mathbb R}|f(iy)|^2dy.
\tag{L-91334.1}
\]

For \(p\in\mathbb H\), the reproducing kernel and normalized kernel are

\[
k_p(z)=\frac1{z+\bar p},
\qquad
 e_p(z)=\sqrt{2\Re p}\,k_p(z),
\tag{L-91334.2}
\]

with

\[
\|k_p\|^2=k_p(p)=\frac1{2\Re p},
\qquad
\langle f,e_p\rangle
=\sqrt{2\Re p}\,f(p).
\tag{L-91334.3}
\]

Let

\[
b_p(z)=\frac{z-p}{z+\bar p}.
\tag{L-91334.4}
\]

Then

\[
K_{b_p}=H^2\ominus b_pH^2=\operatorname{span}\{e_p\}.
\tag{L-91334.5}
\]

## 2. One-factor lower bound

Let \(B\) be an inner Blaschke product having \(p\) as a zero. Factor

\[
B=b_pB_1.
\tag{L-91334.6}
\]

The product-space decomposition gives

\[
K_B=K_{b_p}\oplus b_pK_{B_1}.
\tag{L-91334.7}
\]

Therefore, for every \(f\in H^2(\mathbb H)\),

\[
\boxed{
\|P_{K_B}f\|^2
\ge
\|P_{K_{b_p}}f\|^2
=
2\Re p\,|f(p)|^2.
}
\tag{L-91334.8}
\]

The same bound holds when \(p\) has higher multiplicity, since
\(K_{b_p}\subset K_{b_p^m}\subset K_B\).

## 3. Application to the Xi scattering quotient

Let

\[
\Theta_\omega=\frac{\mathfrak A_\omega}{B_\omega}
\tag{L-91334.9}
\]

be the coprime pole-removed factorization of `L-91034`, and let \(r\) be any outer Hardy vector. By `L-91333`,

\[
\|P_-(\Theta_\omega r)\|^2
=
\|P_{K_{B_\omega}}(\mathfrak A_\omega r)\|^2.
\tag{L-91334.10}
\]

If \(p\) is any crossed-zero pole, then \(B_\omega(p)=0\). Coprimality gives
\(\mathfrak A_\omega(p)\ne0\), and outerness gives \(r(p)\ne0\). Hence

\[
\boxed{
\|P_-(\Theta_\omega r)\|^2
\ge
2\Re p\,
|\mathfrak A_\omega(p)r(p)|^2
>0.
}
\tag{L-91334.11}
\]

Thus one fixed outer vector sees every individual crossed zero with a strict, finite-rank moat. No crossed zero can hide solely in an infinite-height tail or by cancellation with other model-space coordinates.

## 4. Finite certificate

For a finite crossed-zero packet, order any chosen target pole first in a Takenaka--Malmquist basis. Equation (L-91334.11) is then the first square in the exact expansion

\[
\|P_-(\Theta_\omega r)\|^2
=
\sum_j|\langle\mathfrak A_\omega r,e_j\rangle|^2.
\tag{L-91334.12}
\]

Repeated poles add Cauchy-jet squares. Consequently false RH produces a finite positive-energy defect at one scale and one outer vector; the remaining source theorem must force that explicitly positive defect to be zero.

## 5. Boundary

```text
one crossed pole -> strict outer-vector defect       EXACT
finite packet -> finite sum-of-squares witness       EXACT
source-defined proof that the defect vanishes        OPEN / RH-BEARING
Riemann Hypothesis                                   UNPROVED
```
