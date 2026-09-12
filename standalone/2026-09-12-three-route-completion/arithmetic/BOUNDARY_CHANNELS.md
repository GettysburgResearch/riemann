# A finite arithmetic surrogate with the origin channel retained

**Proposed component construction; the covariance/trace upper estimate remains
open.** This is the second arithmetic completion attempt, using the same
objects and sources as [PROOF.md](PROOF.md). It does not make the discarded
origin region positive or orthogonal to the retained input.

Write \(m=m_o\), \(Z(s)=(1-2^{-s})\zeta(s)\), \(d=2N-1\), and let \(P_N\)
denote orthogonal projection onto \(\Pi_N\). For integer \(M\ge2\), define

\[
 (H_{N,M}f)(t)=\int_{1/M}^1m(t/u)(P_Nf)(u)\,\frac{du}{u},
 \qquad \ell_N(f)=(P_Nf)'(0).
\]

The first operator uses only odd Mobius values through \(3M\). Put

\[
 R_{M,2}(t)=\frac{m(Mt)}M+
 t\left[\frac1{Z(2)}-\sum_{n\le Mt,\ n\text{ odd}}\frac{\mu(n)}{n^2}\right].
 \tag{1}
\]

The constant \(1/Z(2)=8/\pi^2\) is an absolutely convergent safe-point
quantity. Define the finite surrogate

\[
 B_{N,M}=H_{N,M}+R_{M,2}\otimes\ell_N.
 \tag{2}
\]

Its second term is a retained rank-one origin channel. It is not a scalar
correction after squaring; every interference term with \(H_{N,M}\) belongs
to the norm of \(B_{N,M}\).

## 1. Exact source formula and complete error

**Theorem.** In the original input/output Lebesgue metrics,

\[
 \|KP_N-B_{N,M}\|_{\rm HS}
       \le 11\,\frac{d^{7/2}}{M^3}.
 \tag{3}
\]

In particular

\[
 \left|\sqrt{S_N}-\|B_{N,M}\|_{\rm HS}\right|
       \le11d^{7/2}/M^3.
 \tag{4}
\]

The entire finite surrogate uses only the native prefix through \(3M\) and
ONE even-zeta value. Taking \(M=\lceil d^{7/6}\rceil\), for \(N\ge2\),
gives an absolute Hilbert--Schmidt error at most eleven. A larger explicit
\(M\) gives any desired smaller tolerance. This improves the coverage
exponent of the crude origin bound while retaining, rather than estimating
away, its leading arithmetic channel.

**Proof of the exact channel.** For every even integer \(q\ge2\), partial
summation of the absolutely convergent tail gives

\[
 \int_0^{1/M}m(t/u)u^{q-2}du
 =\frac{M^{1-q}m(Mt)+t^{q-1}
 [1/Z(q)-\sum_{n\le Mt,\ n\text{ odd}}\mu(n)n^{-q}]}{q-1}.
 \tag{5}
\]

Indeed substitute \(x=t/u\), then integrate the Stieltjes jumps
\(\mu(n)/n\):

\[
 \int_X^\infty m(x)x^{-q}dx
 =\frac{m(X)X^{1-q}+\sum_{n>X,\ n\text{ odd}}\mu(n)n^{-q}}{q-1}.
\]

The formula holds also at an integer cutoff: the two changes in the right
side cancel at the activation point. Equation (1) is (5) at \(q=2\).
Taylor subtraction in the finite input polynomial therefore gives the exact
error columns

\[
 ((KP_N-B_{N,M})\phi_j)(t)
 =\int_0^{1/M}m(t/u)[\phi_j(u)-u\phi_j'(0)]\,\frac{du}{u}.
 \tag{6}
\]

**Explicit derivative bound.** For normalized odd Legendre degree \(l\),

\[
 \left|[\sqrt{2l+1}P_l]'''(u)\right|\le64l^3,
 \qquad |u|\le1/2.
 \tag{7}
\]

Here is a direct constant check. In the Laplace integral write
\(z=u+i\sqrt{1-u^2}\cos v\). On this interval,
\(|z'|<2\), \(|z''|<2\), \(|z'''|<4\). The Gaussian moment estimate in
PROOF.md gives \(\pi^{-1}\int_0^\pi|z|^q dv\le3/(2\sqrt q)\) for
\(q\ge1\). Differentiating \(z^l\) three times, for \(l\ge6\), bounds the
integral by

\[
 (8l^3+12l^2+4l)\frac3{\sqrt l}.
\]

After multiplying by \(\sqrt{2l+1}<2\sqrt l\), this is below \(64l^3\)
because \(6(8+12/l+4/l^2)<64\) for \(l\ge6\). The odd degrees \(1,3,5\)
are checked directly from their displayed classical polynomials.

Oddness and Taylor's integral remainder now imply

\[
 \left(\sum_{j<N}|\phi_j(u)-u\phi_j'(0)|^2\right)^{1/2}
 \le\frac{32}{3}d^{7/2}u^3,
\]

where \(\sum_{l\le d,\ l\text{ odd}}l^6\le d^7\) was used. Apply the
Hilbert--Schmidt triangle inequality to (6), with \(|m|\le2\) and output
interval length two. The bound is

\[
 \frac{64\sqrt2}{3}d^{7/2}\int_0^{1/M}u^2du
 =\frac{64\sqrt2}{9}\frac{d^{7/2}}{M^3}
 <11\frac{d^{7/2}}{M^3}.
\]

This proves (3), and the triangle inequality gives (4). QED.

## 2. Finite piecewise-polynomial construction

There are no unspecified infinite functions to evaluate in (2). For a
monomial \(u^r\), positive odd \(r\), and a cell on which \(J=\lfloor Mt\rfloor\)
is constant,

\[
 H_{N,M}(u^r)(t)=\frac1r\left[
 1+t^r\sum_{3\le n\le J,\ n\text{ odd}}\frac{\mu(n)}{n^{r+1}}
 -M^{-r}m(J)\right].
 \tag{8}
\]

This follows by integrating each active divisor interval
\([1/M,\min(1,t/n)]\); the \(n=1\) interval ends at one, and every \(n\ge3\)
ends at \(t/n\). Thus (2) is piecewise polynomial on the complete partition
\([j/M,(j+1)/M]\), \(M\le j<3M\), with coefficients formed from finitely
many rationals and \(8/\pi^2\). Its complete column integrals and all mixed
terms are finite arithmetic operations after one directed enclosure of pi.

The checker tests an actual instance \(N=4,M=32\). It reconstructs the
ENTIRE squared Hilbert--Schmidt error in (3) over every cell, using the exact
higher moments (5) and the actual even-zeta values for the true operator.
Those additional values are verification inputs, not needed to define the
surrogate itself. The checker also verifies continuity of each retained
moment across all its integer activation boundaries.

## 3. More retained moments and the actual remaining burden

For any fixed integer \(r\ge1\), retain the first \(r\) odd Taylor terms of
\(P_Nf\) at zero, and use (5) at \(q=2,4,\ldots,2r\). Repeated differentiation
of the same Laplace integral gives
\(\|[\sqrt{2l+1}P_l]^{(k)}\|_{[-1/2,1/2]}\le C_k l^k\): for \(l\ge2k\),
each term is a bounded derivative product times \(l^j\) and a moment
\(O(l^{-1/2})\), which cancels the normalization; finitely many smaller
degrees adjust \(C_k\). Taylor's remainder and the preceding proof yield

\[
 \|KP_N-B_{N,M}^{(r)}\|_{\rm HS}
       \le C_r\frac{d^{2r+3/2}}{M^{2r+1}}.
 \tag{9}
\]

The constants depend on the FIXED number of retained moments; no uniform
growing-r claim is made. For fixed r, coverage of order
\(N^{1+1/(4r+2)}\) pays a constant error. This is an arithmetic finite
surrogate with its complete origin channels, not a proof of small trace.

The attempt to turn it into a covariance sign encounters a precise burden:
the safe-moment tails in (5), the finite high-input term, and ALL their mixed
inner products still need a combined upper estimate. A small reciprocal
sum at one all-integer crossing does not control these odd-source functions
on the whole interval \(1<t<3\). Nor can their large Taylor coefficients be
discarded because the source has a balanced endpoint. The construction
locates and computes those coherent channels; it does not make them vanish
or prove XCC26's infinitely-often covariance sign.
