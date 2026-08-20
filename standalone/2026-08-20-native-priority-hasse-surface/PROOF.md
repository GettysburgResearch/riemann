# Native priority-Hasse transport for the normalized factor-67 box

**Status:** exact theorem packet; `UPBF67` and RH remain unproved.

## 1. Literal source

The normalized factor-67 box is

\[
B(X)=\frac{(\mathcal S_{67}h)(X)}{\sqrt X}
=\sum_{n\le X}\frac{\beta(n)}n\Phi_{67}(X/n),
\qquad \beta=(\varepsilon-\delta_{67})*\mu.
\]

Its finite Boolean model has one label of activity `1/p` for every prime `p!=67` and two labelled copies of 67, each of activity `1/67`.  Aggregating the two copies gives

\[
1,-2/67,1/67^2,
\]

the exact native local factor.

## 2. Priority flow

For ordered activities `a_i`, define

\[
w(A)=\prod_{i\in A}a_i,
\quad s_i=\prod_{h\le i}(1-a_h),
\quad \lambda_i=a_is_{i-1}.
\]

For `A subset {i+1,...,k}`, place `J_(i,A)=lambda_i w(A)` on the edge between `A` and `A union {i}`, from odd to even.  If `i=min S`, the incident mass at any nonempty vertex is

\[
s_{i-1}w(S)+\sum_{j<i}\lambda_jw(S)=w(S).
\]

Thus every odd demand and every nonempty even capacity is matched exactly; the empty vertex retains `s_k`.

## 3. Activation

Multiply each edge by the smaller endpoint potential.  The resulting flow is feasible.  An odd endpoint loses mass only when it is the smaller-product endpoint of an earlier-owner edge.  The total loss is

\[
\mathcal U_X
=\sum_i\sum_{A\text{ odd}}
\lambda_iw(A)
[\Phi_X(P_A)-\Phi_X(p_iP_A)].
\]

Consequently

\[
[-B(X)]_+\le\mathcal U_X,
\qquad
[-(\mathcal S_{67}h)(X)]_+\le\sqrt X\,\mathcal U_X.
\]

## 4. Coarea

Because `Phi_X(P)` decreases with `P`, let `dnu_X=-dPhi_X`.  Then

\[
\mathcal U_X=\int\mathcal C_X(t)d\nu_X(t),
\]

where `C_X(t)` sums exactly those first-owner edges whose product interval crosses `t`.

## 5. Hardy identity

For finite real `c_n`,

\[
\int\left|\sum c_nn^{\tau-i\gamma}\right|^2P_\tau(\gamma)d\gamma
=2\tau\int_0^\infty u^{2\tau-1}\left(\sum_{n\ge u}c_n\right)^2du.
\]

Thus the latest Poisson-owner route and the Hasse route both ask for control of native multiplicative boundary tails.

## 6. Exact open theorem

Prove

\[
\mathrm{UPBF67}:\quad
\int_2^Y\sqrt X\,\mathcal U_X\frac{dX}{X}=Y^{o(1)}.
\]

Then the normalized zero-free box has subpower logarithmic negative mass, and the frozen Mellin-Landau consumer gives RH.

The exact negative control

\[
\sum_{n\le13}\mu(n)/n=-2323/30030
\]

shows that full-cube matching alone cannot remove the activation surface.  No proof of `UPBF67` or RH is claimed.
