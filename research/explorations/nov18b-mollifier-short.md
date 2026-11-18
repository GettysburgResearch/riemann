# Recovering the low arithmetic coefficients on shorter height intervals

Let \(1/2<\sigma<1\) and fix \(A\ge0\). For a Dirichlet polynomial \(M\) with at most \(B\ge1\) terms, arbitrary positive integer frequencies, and coefficients bounded by \((2+B)^A\), the [finite local lower bound](nov18b-mollifier-local.md) holds with
\[
 H=C_{A,\sigma}B\log\log(100+|t_0|+B),\qquad
 \frac1{2H}\int_{t_0-H}^{t_0+H}|1-\zeta(\sigma+it)M(\sigma+it)|^2dt
 \gg_{A,\sigma} B^{1-2\sigma}.                                      \tag{1}
\]
The proof recovers the arithmetic coefficients individually with exponentially small error. Its dependence on height comes from the polynomial vertical growth of zeta. Short-interval lower bounds and quasianalytic obstructions for Dirichlet series have a substantial classical literature. Here the number of frequencies may grow and their locations are unrestricted. [Andersson, introduction and Theorem 1](https://arxiv.org/abs/1207.4624)

Put \(X=\lceil 4B/(2-\zeta(2))\rceil\), \(Y=C_0X\), \(\alpha=1-\sigma\), and \(f(t)=1-\zeta(\sigma+it)M(\sigma+it)\). For any center \(v\) normalize
\[
 w_v(t)=(t^2+\alpha^2)\exp[-\cosh((t-v)/Y)]/Z_v
\]
to have integral one. Here \(Z_v\asymp Y(v^2+Y^2+\alpha^2)\). For the Fourier convention of the companion proof,
\[
 |\widehat w_v(u)|\le C\exp(-Y|u|/2).                            \tag{2}
\]
Shift by \(-iY/2\) or \(+iY/2\) as appropriate. On the new line the exponential has modulus \(\exp[-\cos(1/2)\cosh((t-v)/Y)]\), and the polynomial factor costs a uniform constant after integration and normalization. The zero at \(-i\alpha\) cancels the pole of zeta. The contour calculation in the companion proof now gives for \(m\ge1\)
\[
 \langle f,m^{-it}\rangle_{w_v}=
   \sum_{n\ge1}e(n)n^{-\sigma}\widehat w_v(\log(n/m)),          \tag{3}
\]
with absolute convergence by (2) and \(|e(n)|\le1+B(2+B)^A\). In shifting to \(\Re s=2\) and back on individual monomials, the horizontal displacements in the \(t\) variable remain less than \(\pi Y/2\), where the integrals decay at both ends.

## A stable inverse on the first twice as many frequencies

Let \(G\) be the Gram matrix for \(j^{-it}\), \(1\le j\le 2X\). It has diagonal one and entries off the diagonal bounded by \(C\exp[-C_0|m-j|/4]\), by (2) and the spacing of \(\log n\). For any fixed \(b>0\) we may take \(C_0\) so large that
\[
 \max_i\sum_j |(I-G)_{ij}|e^{b|i-j|}<1/4 .
\]
The weighted row norm on the left is submultiplicative by the triangle inequality for index distances. The Neumann series supplies the same bound \(4/3\) for the weighted row norm of \(G^{-1}\). In ordinary operator norm the eigenvalues of \(G\) are in \([3/4,5/4]\). Let \(\psi_m\) be the dual vectors obtained by applying this inverse to the first \(2X\) monomials. For every vector \(f\) in the weighted space,
\[
 \sum_{m\le2X}|\langle f,\psi_m\rangle|^2\le(4/3)\|f\|^2 .
\]
This follows by factoring the synthesis operator into its isometry on the columns and \(G^{1/2}\).

For \(m\le X\), (3) and duality reproduce \(e(m)m^{-\sigma}\) up to an error from \(n>2X\). For \(j\le 3X/2\), the column of such terms has absolute size at most
\[
 C(1+B(2+B)^A)X^{1-\sigma}(3/4)^{Y/2}.
\]
Indeed sum \((j/n)^{Y/2}n^{-\sigma}\) by the integral bound starting at \(2X\). For larger \(j\le2X\), the same bound with the exponential factor omitted suffices. Its coefficient in the dual sum has total absolute value at most \((4/3)e^{-bX/2}\) because \(m\le X\). Thus the aggregate error in the first \(X\) coordinates in Euclidean norm is at most the square root of \(X\) times these polynomial factors times \(O(e^{-bX/2}+(3/4)^{Y/2})\). Choose \(b\), then \(C_0\), depending on \(A,\sigma\), so this is less than half the lower bound for \((\sum_{m\le X}|e(m)|^2m^{-2\sigma})^{1/2}\) in the [omitted-squarefree argument](nov18b-mollifier.md). Consequently \(\int |f|^2 w_v\gg_\sigma B^{1-2\sigma}\) at every center.

## Hard interval

Average these weights over \(|v-t_0|\le H/2\). Their pointwise bound is
\[
 w_v(t)\ll Y^{-1}(1+|t-v|/Y)^2 e^{-\cosh((t-v)/Y)} .
\]
The average is at most \(C/H\) everywhere. On \(|t-t_0|>H\), every \(|t-v|>H/2\). For each such \(v\), substituting \(u=|t-v|/Y\), the integral of \(|f|^2w_v\) on this tail is bounded by
\[
 (100+|t_0|+H+B+Y)^{O_{A,\sigma}(1)}
      \exp[-\tfrac14\exp(H/(2Y))] .
\]
Here we used the unconditional polynomial bound on zeta, then absorbed each fixed polynomial in \(u\) into half the exponential tail. Increasing \(C_{A,\sigma}\) makes the tail smaller than half the lower bound, including for bounded parameters. Averaging in \(v\) proves (1). This is a lower bound on the approximation error, with no assumption on the positions of zeta zeros.
