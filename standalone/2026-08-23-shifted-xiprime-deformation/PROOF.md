# The low-order Pick matrix as a shifted xi-prime derivative

Set

\[
E_\alpha=F'-\alpha F.
\]

For a regular contour and holomorphic `H`, the argument-principle statistic

\[
Z_H(\alpha)={1\over2\pi i}\oint H{E_\alpha'\over E_\alpha}
\]

is analytic for small alpha. Since

\[
\partial_\alpha\log E_\alpha=-F/E_\alpha,
\]

closed-contour integration by parts gives

\[
Z_H'(0)={1\over2\pi i}\oint H'{F\over F'}
=\sum_{F'(c)=0}H'(c){F(c)\over F''(c)}.
\]

Choosing `H_ij'=-W^2 phi_i phi_j` produces the exact Wick-preconditioned
Hermite--Pick entry. Thus the low-order matrix is a zero-motion derivative,
not an independent construction.

On a safe line put `Lcal=F'/F`. Then

\[
{E_\alpha'\over E_\alpha}
=Lcal+{Lcal'\over Lcal-\alpha}.
\]

For xi, the prime coefficient sequence is therefore `C(N;L-alpha)`. The
T-105320 convolution identity yields

\[
\partial_\alpha C(N;L-\alpha)|_0
=-\partial_LC(N;L)=\log N\,b_L(N).
\]

The primitive test divides by `log N`, recovering exactly the reciprocal
source. The functional equation gives

\[
E_\alpha(1-s)=-E_{-\alpha}(s),
\]

so the correct shifted zero formula is the oriented plus/minus pair.

If a matrix explicit formula is analytic on `|alpha|<=r_T` with uniform error
`epsilon_T`, Cauchy's estimate gives derivative error at most
`epsilon_T/r_T`. This is the exact remaining route from the formal xi-prime
formula to the low-order Pick matrix. Pointwise unshifted error is not enough.

No new zero proportion or RH theorem is proved here.
