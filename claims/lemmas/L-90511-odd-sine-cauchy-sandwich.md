# L-90511 — The odd Weil form is a scalar sine symbol inside an explicit positive Cauchy sandwich

Claim ID: `L-90511`  
Status: **PROPOSED COMPLETE EXACT SPECTRAL / TRACE-CLASS LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Depends on: odd-sector reduction `L-90510`; Cauchy–Sobolev completion `L-90505`; the pole-free explicit formula  
Scope: exact sine diagonalisation and an explicit Wiener–Hopf–Hankel sandwich; no sign theorem

## 1. Odd extension and the sine transform

Let

\[
 (Uh)(x)=2^{-1/2}\operatorname{sgn}(x)h(|x|)
\]

be the unitary odd-extension map from `L^2(0,infinity)` to the odd subspace of `L^2(R)`, and let

\[
 (\mathcal Sh)(\tau)
 =\sqrt{\frac2\pi}\int_0^\infty h(x)\sin(\tau x)\,dx
\]

be the unitary Fourier sine transform.

For `y>=0`, the compression

\[
 C_y=U^*P_{\rm odd}T_yU
\]

is self-adjoint. Indeed reflection conjugates `T_y` to `T_-y`, while it acts as `-I` on the odd sector. Moreover

\[
 \boxed{
 \mathcal SC_y\mathcal S^{-1}
 =M_{\cos(y\tau)}.
 }
 \tag{L-90511.1}
\]

Consequently

\[
 \langle Uh,T_yUh\rangle
 =\int_0^\infty\cos(y\tau)|\mathcal Sh(\tau)|^2\,d\tau,
 \tag{L-90511.2}
\]

and

\[
 \|Uh-T_yUh\|_2^2
 =2\int_0^\infty[1-\cos(y\tau)]
   |\mathcal Sh(\tau)|^2\,d\tau.
 \tag{L-90511.3}
\]

The half-line Wiener–Hopf–Hankel formula of `L-90510` is therefore the physical-space kernel of the commuting Dirichlet-wave family `cos(y sqrt(-Delta_D))`.

## 2. The scalar pole-free symbol

On compactly supported odd tests define the even tempered distribution

\[
 \boxed{
 \mathfrak m(\tau)
 =2\pi\mu(\tau)
  -2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
       \cos(\tau\log n).
 }
 \tag{L-90511.4}
\]

The prime sum is interpreted distributionally; on one compactly supported physical test only finitely many translation correlations occur. Equations (L-90511.2)--(L-90511.3) and the Lévy identity give

\[
 \boxed{
 Q(Uh,Uh)
 =\left\langle\mathfrak m,
   |\mathcal Sh|^2\right\rangle.
 }
 \tag{L-90511.5}
\]

Thus all zeta arithmetic sits in one scalar distribution. The matrix and half-line forms are regularisations of this symbol, not independent noncommutative objects.

By `L-90510`,

\[
 \boxed{
 \mathrm{RH}
 \iff
 \langle\mathfrak m,|\mathcal Sh|^2\rangle\ge0
 \quad\text{for every }h\in C_c^\infty(0,\infty).
 }
 \tag{L-90511.6}
\]

## 3. Exact sine kernel of exponential confinement

For `a>0`, let `w_a(x)=e^{-ax}` on the half-line. The sine representation of multiplication by `w_a` is the integral operator `K_a` with kernel

\[
\begin{aligned}
 K_a(\tau,\sigma)
 &=\frac2\pi\int_0^\infty
 e^{-ax}\sin(\tau x)\sin(\sigma x)\,dx\\
 &=\boxed{
 \frac a\pi\left[
 {1\over a^2+(\tau-\sigma)^2}
 -{1\over a^2+(\tau+\sigma)^2}
 \right].}
\end{aligned}
 \tag{L-90511.7}
\]

It is a positive self-adjoint contraction and is pointwise strictly positive for `tau,sigma>0`. It is exactly a Cauchy Wiener–Hopf kernel minus its Hankel reflection.

Let

\[
 r_c(\tau)={1\over c^2+\tau^2}.
\]

The odd part of the Cauchy–Sobolev test map `J_(a,c)=B_c M_(e^{-a|u|})` becomes

\[
 \boxed{
 \mathcal S U^*J_{a,c}U\mathcal S^{-1}
 =M_{r_c}K_a.
 }
 \tag{L-90511.8}

## 4. Trace-class Cauchy sandwich

Let `A_(a,c)^odd` be the trace-class operator representing `Q` on the odd coefficient space. In sine coordinates its quadratic-form factorisation is

\[
 \boxed{
 A_{a,c}^{\rm odd}
 =K_aM_{r_c}
   M_{\mathfrak m}
   M_{r_c}K_a,
 }
 \tag{L-90511.9}
\]

where `M_m` is understood as the distributional form (L-90511.5). The left side is a genuine trace-class operator by `L-90505`; the right side is its exact scalar-symbol regularisation.

The regulariser is explicit, positive and arithmetic-free. Every prime/gamma interaction is confined to the scalar symbol `m`. This separates the final problem into:

```text
universal positive Cauchy Wiener–Hopf–Hankel sandwich
+
one scalar explicit-formula distribution.
```

## 5. Proof boundary

Proved here:

- exact sine diagonalisation of every odd compressed translation;
- the scalar pole-free symbol and its RH-equivalent square test;
- the explicit positive Cauchy difference kernel for exponential confinement;
- exact factorisation of the trace-class odd operator as a scalar-symbol sandwich.

Not proved:

- positivity of the scalar distribution on sine squares;
- a stable Wiener–Hopf factorisation of `m`;
- RH.
