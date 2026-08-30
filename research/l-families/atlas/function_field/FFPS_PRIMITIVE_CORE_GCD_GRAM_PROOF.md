# Proof details for the primitive core shared-divisor Gram

Status: **proof extract for
[`FFPS_PRIMITIVE_CORE_GCD_GRAM_CLOSURE.md`](FFPS_PRIMITIVE_CORE_GCD_GRAM_CLOSURE.md)**.

## 1. Expanding COREAGG

Insert

\[
 \mathcal Z_{I,r}^\alpha
 =\sum_{(M,r)=1}{\mu(M)\over\sqrt M}\mathcal W_I^\alpha(rM)
\]

twice into `mathfrak C_alpha`. For one core set `N=rM`, `N'=rM'`.
Squarefreeness gives `(MM',r)=1`, and

\[
 {\tau(r)\over r^2\sqrt{MM'}}
 ={\tau(r)\over r\sqrt{NN'}},
 \qquad
 \mu(M)\mu(M')=\mu(N)\mu(N').
\]

For fixed `N,N'`, possible cores are exactly `r|(N,N')`. Summing their
weights proves

\[
 \mathscr K_2(N,N')=\sum_{r|(N,N')}\tau(r)/r
\]

and the exact Gram formula. Multiplicativity and squarefreeness give the
Euler product `prod_(p|gcd)(1+2/p)`.

## 2. Feature positivity and local spectrum

The identity

\[
 \mathscr K_2(N,M)=
 \sum_r{\tau(r)\over r}\mathbf1_{r|N}\mathbf1_{r|M}
\]

is a Gram representation. At one prime put `c=2/p`. The local block

\[
 \begin{pmatrix}1&1\\1&1+c\end{pmatrix}
 =\begin{pmatrix}1&0\\1&\sqrt c\end{pmatrix}
  \begin{pmatrix}1&1\\0&\sqrt c\end{pmatrix}
\]

has determinant `c`, trace `2+c`, and eigenvalues

\[
 1+1/p\pm\sqrt{1+1/p^2}.
\]

The smaller eigenvalue is `1/p+O(p^-2)` and the larger is
`2+O(p^-1)`, giving condition number `2p+O(1)`.

## 3. Detailed diagonal bound

For each squarefree product shell define height-layer coefficients
`c_t^alpha(N)` as in the main packet. Expanding the dyadic square function
and taking absolute values gives

\[
 \sum_I\left|\sum_{t\in I}c_t\right|^2
 \le\sum_{t,u}|c_t c_u|\,m(t,u),
\]

where `m(t,u)` counts aligned dyadic intervals containing both heights. At
each scale there is at most one, so `m(t,u)<=L_H`. Also

\[
 \sum_t|c_t|\le\|\mathcal R\|_\infty\tau(N).
\]

This proves the per-shell bound in the main packet.

Ratio-sixteen support means both physical coordinates are at least one
sixteenth of their maximum. If the maximum is at most `2H`, their product
`67^alpha N` is at most `4H^2`, hence `N<=4H^2/67^alpha`.

For squarefree `N`,

\[
 K_2(N,N)\tau(N)^2
 \le 3^{\omega(N)}4^{\omega(N)}=12^{\omega(N)}=d_{12}(N).
\]

The identity

\[
 d_{12}(n)=\sum_{n_1\cdots n_{12}=n}1
\]

and finite rearrangement give

\[
 \sum_{n\le X}d_{12}(n)/n
 \le\prod_{j=1}^{12}\sum_{m\le X}1/m
 \le(1+\log X)^{12}.
\]

No average prime theorem enters.

## 4. Gcd decomposition

For `N!=M`, set `g=(N,M)`, `N=ga`, `M=gb`. Squarefreeness gives
`(a,b)=(ab,g)=1`. Moreover

\[
 {\mu(N)\mu(M)\over\sqrt{NM}}
 ={\mu(g)^2\mu(a)\mu(b)\over g\sqrt{ab}}
 ={\mu(a)\mu(b)\over g\sqrt{ab}}.
\]

Since `K_2(N,M)=K_2(g,g)=kappa_2(g)`, substitution proves the exact gcd
formula. The excluded diagonal corresponds precisely to `(a,b)=(1,1)`.

## 5. Equivalence of the open gates

The Gram energy and diagonal are nonnegative. Thus

\[
 |O|=|C-D|\le C+D
\]

shows `COREAGG -> OFFGCDWAVE` after the paid diagonal, while

\[
 C=D+O\le D+|O|
\]

shows the reverse implication. Polylogarithmic factors are absorbed by
renaming the positive exponent. This is the exact all-exponent equivalence
used in the main packet.
