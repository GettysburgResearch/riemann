# The half-completed Vaughan field is a fractional Hankel near-collision

## Abstract

The balanced Vaughan packet was reduced in PR #696 to one half-divisor-completed ratio-four field energy. We compute that energy exactly. Its diagonal is unconditionally subpower and its Gram kernel vanishes outside a multiplicative ratio-four band. The remaining theorem is one signed off-diagonal near-collision. A positive finite factorization shrinks the collision width to `1+o(1)` at subpower cost, and gcd/largest-prime ownership leaves one Möbius cofactor sign. This is a strict reduction, not a proof of RH.

## 1. Half-completed source

Let `eta(p^k)=binom(2k,k)/4^k`. Then `eta*eta=1`. For `b_U=mu 1_(n>U)`, put `h_U=b_U*eta`. PR #696 proves that the balanced Vaughan source is `h_U*h_U` and reduces the packet to the energy of

\[
H_{U,N}(Y)=\sum_{U<n\le N}h_U(n)n^{-1/2}A_-(Y/n).
\]

## 2. Exact Gram kernel

In logarithmic coordinate the kernel is

\[
\psi=1_{(0,h)}-\sqrt2 1_{(h,2h)},\qquad h=\log2.
\]

Its autocorrelation is

\[
R(v)=
\begin{cases}
3h-(3+\sqrt2)|v|,&|v|\le h,\\
-\sqrt2(2h-|v|),&h\le|v|\le2h,\\
0,&|v|\ge2h.
\end{cases}
\]

Therefore

\[
\int|H|^2dY/Y
=\sum_{m,n}h_U(m)h_U(n)(mn)^{-1/2}R(\log(m/n)).
\]

Only ratio-four near-collisions survive.

## 3. Diagonal closure

Since `eta(p^k)<=1`, `|h_U(n)|<=tau(n)`. Hence

\[
3\log2\sum h_U(n)^2/n=N^{o(1)}.
\]

The final condition is exactly the positive part of the signed off-diagonal correlation.

## 4. Fractional Nyman form

Mellin Plancherel gives

\[
\frac1{2\pi}\int|\widehat A_-(i\gamma)|^2
\left|\sum_{U<n\le N}h_U(n)n^{-1/2-i\gamma}\right|^2d\gamma.
\]

For `Re z>1`, the untruncated source equals

\[
\zeta(z)^{-1/2}-M_U(z)\zeta(z)^{1/2}.
\]

The remaining physical estimate is therefore a compact fractional Nyman approximation, not an unsigned coefficient norm.

## 5. Narrow positive refinement

For `a=2^(1/M)`, the fixed dyadic step is a positive combination of shifts of the `a`-step. The coefficient mass is `O(M^2)`, so energy costs `O(M^4)`, while the collision window shrinks to `2^(2/M)`. Subpower `M` is allowed.

## 6. Owner form

Expanding `h_U=b_U*eta`, grouping the two tail divisors by their gcd, and selecting the unique largest prime collapses both Möbius signs to one cofactor sign. All other renewal weights are positive.

## 7. Boundary

`HCNC103100` implies `HHFE102010`, hence the balanced Vaughan estimate and RH. It remains open. No finite replay or numerical trend is promoted to an infinite estimate.
