# L-32702 — Dyadically filtered Jordan-2 source has an exact parity-signed carry profile

Claim ID: `L-32702`  
Title: Cancelling the main pole of the positive Jordan-totient source produces an exact alternating-square divisor potential whose carry sign is determined by parent parity  
Status: **PROPOSED COMPLETE EXACT LEMMA — independent review requested**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Dependencies: elementary Jordan totient convolution and finite carry algebra  
Scope: exact arithmetic source and Mellin firewall; no eventual sign theorem and no RH claim

## 1. Positive Jordan source

Let

\[
J_2(n)=n^2\prod_{p\mid n}(1-p^{-2})=(\mu*\operatorname{id}_2)(n).
\tag{L-32702.1}
\]

Its Dirichlet series is

\[
\sum_{n\ge1}\frac{J_2(n)}{n^s}
=\frac{\zeta(s-2)}{\zeta(s)}.
\tag{L-32702.2}
\]

The coefficient sequence is strictly positive.

## 2. Unique dyadic cancellation of the main pole

Define

\[
\boxed{
c_2=(\varepsilon-8\delta_2)*J_2.}
\tag{L-32702.3}
\]

The factor `8=2^3` is exactly the coefficient that cancels the numerator pole at `s=3`:

\[
\boxed{
\sum_{n\ge1}\frac{c_2(n)}{n^s}
=(1-2^{3-s})\frac{\zeta(s-2)}{\zeta(s)}
=\frac{\eta(s-2)}{\zeta(s)}.}
\tag{L-32702.4}
\]

Here `eta(u)=(1-2^(1-u))zeta(u)` is entire.

At the coefficient level, if `n=2^a m` with `m` odd,

\[
c_2(n)=
\begin{cases}
J_2(m),&a=0,\\
-5J_2(m),&a=1,\\
-J_2(2^a m),&a\ge2.
\end{cases}
\tag{L-32702.5}
\]

Thus

\[
\boxed{c_2(n)>0\iff n\text{ odd},\qquad c_2(n)<0\iff n\text{ even}.}
\tag{L-32702.6}
\]

## 3. Convolution collapse

Since `J_2=mu*id_2`,

\[
\mathbf1*c_2
=(\varepsilon-8\delta_2)*\operatorname{id}_2.
\tag{L-32702.7}
\]

For even `n=2m`, the second term is `8m^2=2n^2`, while for odd `n` it is absent. Hence

\[
\boxed{(\mathbf1*c_2)(n)=(-1)^{n-1}n^2.}
\tag{L-32702.8}
\]

Define the floor potential

\[
H(N)=\sum_{q\le N}c_2(q)\left\lfloor\frac Nq\right\rfloor.
\tag{L-32702.9}
\]

Then

\[
H(N)=\sum_{m\le N}(-1)^{m-1}m^2
=\boxed{(-1)^{N-1}\frac{N(N+1)}2.}
\tag{L-32702.10}
\]

The apparently complicated Jordan/Möbius source has therefore become one explicit alternating quadratic staircase.

## 4. Pointwise carry profile

For a split `n=j+k`, let

\[
Y_n(j)=\sum_{q\le n}c_2(q)\chi_{n,q}(j)
=H(n)-H(j)-H(k).
\tag{L-32702.11}
\]

The sign is completely classified.

### Odd parent

If `n` is odd, exactly one child is even. Let that even child have size `e`. Then

\[
\boxed{Y_n(j)=(n+1)e>0.}
\tag{L-32702.12}
\]

### Even parent, even children

If `n,j,k` are all even, then

\[
\boxed{Y_n(j)=-jk<0.}
\tag{L-32702.13}
\]

### Even parent, odd children

If `n` is even and `j,k` are odd, then

\[
\boxed{
Y_n(j)=-\frac{n(n+1)+j(j+1)+k(k+1)}2<0.}
\tag{L-32702.14}
\]

Thus

\[
\boxed{
Y_n(j)>0\text{ for every split of an odd parent,}\qquad
Y_n(j)<0\text{ for every split of an even parent.}}
\tag{L-32702.15}
\]

No exceptional row or quotient cell remains.

## 5. Riesz scalar and Mellin transform

Define

\[
\mathcal D_2(X)
=\sum_{n\le X}\frac{c_2(n)}{\sqrt n}\log\frac Xn.
\tag{L-32702.16}
\]

Equivalently, with

\[
P_2(X)=\sum_{n\le X}\frac{J_2(n)}{\sqrt n}\log\frac Xn,
\]

one has

\[
\boxed{\mathcal D_2(X)=P_2(X)-4\sqrt2\,P_2(X/2).}
\tag{L-32702.17}
\]

For `Re(z)>5/2` initially,

\[
\boxed{
\int_1^\infty \mathcal D_2(X)X^{-z-1}\,dX
=\frac{\eta(z-3/2)}{z^2\zeta(z+1/2)}.}
\tag{L-32702.18}
\]

The numerator cannot cancel a nontrivial denominator zero. At a zeta zero `rho`, the candidate pole occurs at `z=rho-1/2`, where the numerator is `eta(rho-2)`. The Euler factor cannot vanish because that would require `Re(rho)=3`; and `zeta(rho-2)` cannot vanish, since by the functional equation that would force a zero at `3-rho`, whose real part is greater than two.

The transform has no positive-real singularity arising from a zeta zero. Hence an eventual one-sided bound for `D_2` would be RH-bearing by Landau.

## 6. Flow interpretation

If `d(n,j)` is any exact carry saturation for a target `w`, finite interchange gives

\[
\sum_q c_2(q)w(q)=\sum_{n,j}d(n,j)Y_n(j).
\tag{L-32702.19}
\]

The source therefore measures, with explicit polynomial weights, the competition between odd-parent and even-parent fragmentation mass. Unlike the failed Mersenne menu, there are no artificial eta-factor poles introduced by the support geometry: the numerator in (L-32702.18) is entire and the denominator retains the actual zeta zeros.

This nominates a new source-specific attack:

```text
construct or deform an exact nonnegative carry flow
so that the explicit odd-parent reserve dominates the explicit even-parent debt.
```

The lemma does not claim that such a deformation has been produced.

## 7. Scope

Established exactly:

- dyadic main-pole cancellation;
- the sign of every arithmetic coefficient;
- the alternating-square convolution collapse;
- the closed floor potential;
- the complete pointwise carry sign classification;
- the Riesz/Mellin source and uncancelled-zero firewall.

Open:

- eventual one-sidedness of `D_2`;
- an odd-parent-dominant exact carry flow;
- RH.
