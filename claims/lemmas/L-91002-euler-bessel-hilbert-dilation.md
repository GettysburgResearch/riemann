# L-91002 — An Euler–Bessel Hilbert dilation and positive localizer for the safe-line prime weights

Claim ID: `L-91002`  
Status: **PROPOSED COMPLETE EXACT HILBERT-DILATION THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `L-90906`, `L-91001`  
RH status: **unproved**

## 1. The generalized inverse-Gaussian measure

For `t>0`, define the positive measure

\[
\boxed{
 d\nu_t(q)
 =\frac1{\sqrt\pi}q^{-1/2}
   e^{-q-t^2/(4q)}\,dq,
 \qquad q>0.
}
\tag{L-91002.1}
\]

Its total mass is `e^{-t}`. The Gamma--Bessel identity of `L-90906` becomes

\[
\boxed{
 e^{-t}P_k(t)
 =\int_0^\infty q^k\left(q-\frac{t^2}{2}\right)d\nu_t(q).
}
\tag{L-91002.2}
\]

The ordinary moments are reverse Bessel polynomials:

\[
\boxed{
 \int_0^\infty q^m\,d\nu_t(q)
 =e^{-t}\frac{\theta_m(t)}{2^m}.
}
\tag{L-91002.3}
\]

Equations (L-91002.2)--(L-91002.3) are equivalent to
`Q_k=theta_(k+1)-t^2 theta_k`.

## 2. A pointwise positive polynomial localizer

Put `a=t^2/2`. Then

\[
\boxed{
 e^{-t}\left(P_{k+1}(t)-\frac{t^2}{2}P_k(t)\right)
 =\int_0^\infty q^k(q-a)^2d\nu_t(q)>0.
}
\tag{L-91002.4}
\]

Thus the polynomial

\[
\boxed{
R_k(t):=P_{k+1}(t)-\frac{t^2}{2}P_k(t)
}
\tag{L-91002.5}
\]

is strictly positive for every `t>0` and every `k>=0`, despite `P_k` itself
having one sign change.

More generally, every Hankel matrix

\[
\boxed{
\left(
 e^{-t}\left[P_{i+j+1}(t)-\frac{t^2}{2}P_{i+j}(t)\right]
\right)_{0\le i,j\le d}\succeq0
}
\tag{L-91002.6}
\]

because it is the Gram matrix of the functions
`q^i(q-a)` in `L^2(nu_t)`.

This is a previously hidden total-positivity constraint coupling all derivative
orders.

## 3. Prime-power direct-sum Hilbert space

Let

\[
t_n=\log n,
\qquad
w_n=\frac{\Lambda(n)}{\sqrt n}>0,
\]

and define

\[
\mathcal K
=\bigoplus_{n\ge2}L^2((0,\infty),w_n\nu_{t_n}).
\tag{L-91002.7}
\]

For integers `i>=0` and real `x`, set

\[
U_{i,x}(n,q)=q^i e^{-ixt_n},
\qquad
V_{i,x}(n,q)=\left(q-\frac{t_n^2}{2}\right)q^i e^{-ixt_n}.
\tag{L-91002.8}
\]

For every finite selection of order/centre indices the vectors lie in the
direct sum, since the moments grow only polynomially in `log n` while the total
prime weight is `Lambda(n)n^{-3/2}`. Their cross Gram matrix is

\[
\boxed{
\begin{aligned}
C_{(i,x),(j,y)}
&:=\langle U_{i,x},V_{j,y}\rangle_{\mathcal K}\\
&=\sum_{n\ge2}
 \frac{\Lambda(n)}{n^{3/2}}
 P_{i+j}(\log n)
 e^{i(x-y)\log n}.
\end{aligned}}
\tag{L-91002.9}
\]

This is exactly the prime component of the single-safe-line hierarchy, now
realized as a cross Gram block rather than a signed scalar series.

## 4. Positive block completion

Define

\[
M_{ab}=\langle U_a,U_b\rangle,
\qquad
N_{ab}=\langle V_a,V_b\rangle,
\qquad
C_{ab}=\langle U_a,V_b\rangle.
\]

For every finite selection of order/centre indices,

\[
\boxed{
\begin{pmatrix}
M&C\\
C^*&N
\end{pmatrix}\succeq0.
}
\tag{L-91002.10}
\]

Consequently

\[
\boxed{
 C^*M^\dagger C\preceq N
}
\tag{L-91002.11}
\]

on the range of `M`, and every singular value of
`M^{-1/2}CN^{-1/2}` is at most one.

The current scalar prime term is therefore not arbitrary oscillation: it is the
cross channel of a canonical positive two-copy feature space.

## 5. Conditional negative definiteness of the localizer channel

Since `R_k(t)>0`, the function

\[
\mathcal R_k(x)
=\sum_{n\ge2}\frac{\Lambda(n)}{n^{3/2}}
 R_k(\log n)e^{-ix\log n}
\tag{L-91002.12}
\]

is positive definite on the additive group `R`. In particular

\[
\boxed{
\Re\mathcal R_k(0)-\Re\mathcal R_k(x)
=\sum_{n\ge2}\frac{\Lambda(n)}{n^{3/2}}
 R_k(\log n)(1-\cos(x\log n))\ge0.
}
\tag{L-91002.13}
\]

In differential notation the prime series obeys the positive-definite raising
law

\[
\mathcal R_k
=\mathcal P_{k+1}+\frac12\partial_x^2\mathcal P_k,
\tag{L-91002.14}
\]

where `Pcal_k` is the order-`k` prime series.

## 6. Exact remaining bridge

The completed scalar also contains the rational and gamma channels of
`mathscr X`. The Hilbert dilation shows what a non-circular proof now has to do:
construct an archimedean/pole feature block `A` such that the full completed
scalar is a Schur complement or a diagonal of

\[
\begin{pmatrix}
M&C\\
C^*&N+A
\end{pmatrix}\succeq0
\tag{L-91002.15}
\]

through the continuation region `r<=1/2` identified by `L-91001`.

Proving (L-91002.15) with the exact completed channels would prove the
Hausdorff/Borel criterion and hence RH. It is not proved here. The advance is
that the finite-prime part already possesses the required positive dilation;
only the completed archimedean domination and analytic continuation remain.
