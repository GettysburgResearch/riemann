# The achievable window for growing positive integer marks

Date: 2026-10-25.

Status: complete arithmetic component proof, subject to independent
review. No improved zero-free half-plane is claimed.

Scope: the ordinary squarefree count with a positive integer
prime-factor parameter and one explicitly specified nonnegative smooth
profile. The result is uniform in that integer parameter. It is not
asserted for a varying character family.

Dependencies: the elementary Chebyshev upper bound for prime counting,
Euler summation for zeta, Cauchy's derivative formula, and the explicitly
proved smooth-weight estimates below. The companion
GROWING_INTEGER_RESONANCE.md supplies the separate lower obstruction;
its proof uses the prime number theorem.

What was actually run: no numerical experiment is used in this proof.
The companion finite convolution checker concerns a different, fixed
marked-count identity and does not certify the estimates here.

Smallest remaining gap for an improved zero-free region: a bound for a
noninteger marked parameter, or its derivative, that survives the full
growth of the integer interpolation problem. The theorem below does not
provide that bound.

## 1. Statement

Choose real numbers
\[
 0<A<B<\log 2
\]
and fix the nonnegative profile
\[
 W(x)=
 \begin{cases}
 \exp\!\left(-\dfrac1{(\log x-A)(B-\log x)}\right),
       &e^A<x<e^B,\\
 0,&\text{otherwise}.
 \end{cases}                                                   \tag{1}
\]
Then \(W\in C_c^\infty((1,2))\), and \(W\) is not identically zero.
For a positive integer \(K\), put
\[
 A_K(X)=\sum_n\mu^2(n)K^{\omega(n)}W(n/X),
\]
\[
 F_K(s)=\zeta(s)^K H_K(s),\qquad
 H_K(s)=\prod_p(1+Kp^{-s})(1-p^{-s})^K,
\]
and use the complete pole main term
\[
 C_K(X)=\operatorname{Res}_{s=1}
          \bigl(\widehat W(s)F_K(s)X^s\bigr).                    \tag{2}
\]
Here \(C_K\) is \(X\) times the exact polynomial in \(\log X\) of
degree \(K-1\); no truncation in that polynomial is permitted.

**Theorem 1.** For every fixed \(1/2<\sigma<1\), there are constants
\(C_{\sigma,W}\) and \(D_{\sigma,W}\), independent of \(K\) and \(X\),
such that, for all positive integers \(K\) and all \(X\ge1\),
\[
 \boxed{\begin{aligned}
 |A_K(X)-C_K(X)|
 \le{}&C_{\sigma,W}X^\sigma\\
 &{}\times\exp\!\left[
 D_{\sigma,W}
 \left(\frac{K^{1/\sigma}}{\log(2K)}
                   +K\log(2K)\right)\right].
 \end{aligned}}                                                \tag{3}
\]

**Corollary 2.** Fix \(0<\theta<1\) and \(\varepsilon>0\).
Uniformly for
\[
             1\le K\le(\log X)^\theta,\qquad X\ge3,
\]
one has
\[
 \boxed{\displaystyle
 A_K(X)-C_K(X)
 =O_{\theta,\varepsilon,W}
   \left(X^{\max(1/2,\theta)+\varepsilon}\right).}                \tag{4}
\]
The same assertion holds if the upper bound for \(K\) is multiplied
by any fixed power of \(\log\log X\).

Thus there is a real growing-parameter theorem. Together with the
resonance obstruction, it identifies the exponent threshold for these
power-sized windows in \(\log X\), up to arbitrary small exponent
losses, whenever \(1/2<\theta<1\).

## 2. The Mellin decay of the chosen profile

For \(\sigma\) in any fixed compact real interval, define
\[
 \phi_\sigma(v)=
 \begin{cases}
 \exp(\sigma v)
 \exp\!\left(-\dfrac1{(v-A)(B-v)}\right),&A<v<B,\\
 0,&\text{otherwise}.
 \end{cases}
\]
Then
\[
 \widehat W(\sigma+it)
       =\int_A^B\phi_\sigma(v)e^{itv}\,dv.                       \tag{5}
\]
We claim that there are constants \(C,c>0\), uniform over that compact
interval, such that
\[
              |\widehat W(\sigma+it)|
                      \le C\exp(-c\sqrt{|t|}).                  \tag{6}
\]

Here is a proof including the derivative constants. Put
\(q(z)=(z-A)(B-z)\), and, for real \(v\in(A,B)\), set
\(d(v)=\min(v-A,B-v)\). There is a fixed small \(\eta>0\), depending
only on \(B-A\), such that on
\[
                    |z-v|\le\eta d(v)
\]
one has
\[
 \Re(1/q(z))\ge \frac{c_0}{q(v)}
                         \ge \frac{c_1}{d(v)}.                 \tag{7}
\]
Indeed \(q(v)>0\), \(q(v)\) is comparable to \(d(v)\), and the relative
change of \(q\) on that disk is at most a fixed small constant.
The analytic function \(\exp(\sigma z-1/q(z))\) is therefore bounded
there by \(C\exp(-c_1/d(v))\). Cauchy's formula gives
\[
 |\phi_\sigma^{(j)}(v)|
 \le C j!(\eta d(v))^{-j}\exp(-c_1/d(v))
 \le C^{j+1}(j!)^2.                                             \tag{8}
\]
For the last inequality, maximize \(d^{-j}e^{-c_1/d}\) over positive
\(d\); its maximum is \((j/(c_1e))^j\le c_1^{-j}j!\).
The same estimates show that all derivatives vanish at both endpoints,
so extension by zero is smooth.

Integrating (5) by parts \(j\) times yields
\[
 |\widehat W(\sigma+it)|
       \le C^{j+1}(j!)^2 |t|^{-j}.
\]
Choose \(j\) to be a sufficiently small constant times \(\sqrt{|t|}\).
The elementary bound \(j!\le j^j\) proves (6). Bounded \(t\) is absorbed
by increasing \(C\).

## 3. A uniform bound for the Euler correction

Fix \(1/2<\sigma<1\). We prove, uniformly in real \(t\) and positive
integers \(K\),
\[
       |H_K(\sigma+it)|
       \le \exp\!\left(
           C_\sigma\frac{K^{1/\sigma}}{\log(2K)}\right).         \tag{9}
\]
It suffices to consider large \(K\). Split the primes at
\[
                         P=(2K)^{1/\sigma}.
\]
For \(p\le P\), elementary logarithmic upper bounds give
\[
 \log\left|(1+Kp^{-s})(1-p^{-s})^K\right|
        \le 2Kp^{-\sigma}+C_\sigma Kp^{-2\sigma}.
\]
Summing and using the Chebyshev upper bound by partial summation gives
\[
 K\sum_{p\le P}p^{-\sigma}+K\sum_p p^{-2\sigma}
       \ll_\sigma
       \frac{KP^{1-\sigma}}{\log P}+K
       \ll_\sigma\frac{K^{1/\sigma}}{\log K}.                   \tag{10}
\]

For \(p>P\), one has \(Kp^{-\sigma}<1/2\). The linear terms of the
two logarithms cancel. The absolutely convergent Taylor expansions
therefore give
\[
 \left|\log(1+Kp^{-s})+K\log(1-p^{-s})\right|
                       \ll K^2p^{-2\sigma}.
\]
Again by partial summation from Chebyshev,
\[
 K^2\sum_{p>P}p^{-2\sigma}
       \ll_\sigma\frac{K^2P^{1-2\sigma}}{\log P}
       \ll_\sigma\frac{K^{1/\sigma}}{\log K}.                   \tag{11}
\]
Equations (10) and (11) prove (9). If a finite Euler factor vanishes,
the modulus bound remains valid; no logarithm at that zero is needed.
The tail logarithms are well-defined by their convergent Taylor
series.

For every fixed \(K\), the same local cancellation proves that
\(H_K\) is holomorphic in \(\Re s>1/2\). Because \(K\) is an integer,
\(F_K=\zeta^K H_K\) has no branch singularities and has only a pole
at one in that half-plane.

## 4. Uniform contour integration

Euler summation, with any fixed \(\sigma>0\), gives the elementary
bound
\[
             |\zeta(\sigma+it)|
                        \le C_\sigma(1+|t|).                   \tag{12}
\]
The factor \(1/(\sigma+it-1)\) is bounded on the chosen vertical
line, because \(\sigma<1\) is fixed. No zero-free region is used.

For each fixed \(K\), Mellin inversion and a contour shift past the
pole at one give the exact identity
\[
 A_K(X)-C_K(X)=
 \frac1{2\pi i}\int_{\sigma-i\infty}^{\sigma+i\infty}
               \widehat W(s)F_K(s)X^s\,ds.                    \tag{13}
\]
The horizontal edges tend to zero: for this fixed \(K\), (6) beats
the polynomial growth of \(\zeta(s)^K\), and the bound for \(H_K\)
is uniform in height on every closed substrip with real part
greater than \(1/2\).

For the uniform estimate on (13), insert (6), (9), and (12):
\[
 \begin{aligned}
 |A_K(X)-C_K(X)|
 \le{}&C X^\sigma
   \exp\!\left(C_\sigma K^{1/\sigma}/\log(2K)\right)\\
 &{}\times C_\sigma^K
       \int_0^\infty (1+t)^K e^{-c\sqrt t}\,dt.
 \end{aligned}                                                 \tag{14}
\]
After \(u=\sqrt t\), the last integral is bounded by
\[
 C^{K+1}(2K+2)!.
\]
Its logarithm is \(O(K\log(2K))\), by the elementary factorial
bound. This proves (3), with constants independent of \(K\).

To obtain (4), choose
\[
 \max(1/2,\theta)<\sigma<
       \min\!\left(1,\max(1/2,\theta)+\varepsilon\right).
\]
If \(K\le(\log X)^\theta\), both terms in the exponential in (3)
are \(o(\log X)\), uniformly:
\[
 \frac{K^{1/\sigma}}{\log(2K)}
       \ll(\log X)^{\theta/\sigma},\qquad
 K\log(2K)\ll(\log X)^\theta\log\log(3X).
\]
The unused part of \(\varepsilon\) absorbs these terms. Fixed powers
of \(\log\log X\) do not change these strict inequalities between
the powers of \(\log X\). This proves Corollary 2.

## 5. What this does and does not allow

For the same positive profile, the companion resonance theorem proves:
if \(1/2<\theta\le1\) and a uniform bound \(O(X^b)\) holds throughout
\(K\le(\log X)^\theta\), then \(b\ge\theta\).
Thus, for \(1/2<\theta<1\), (4) reaches the necessary exponent
threshold with arbitrary small losses. The proof gives an explicit
source of the growth: the primes around \(K^{1/\sigma}\), supplemented
by the cost of integrating \(\zeta(s)^K\) against the smooth profile.

This positive result cannot be extrapolated to the much larger
range \(K\asymp\log X/\log\log X\) with a fixed exponent \(b<1\);
the companion theorem rules out precisely that scalar conclusion
even after subtracting the complete pole main term.

There is also a useful correction to a naive local-zero heuristic.
For a zero of multiplicity \(m\), the factor \(\zeta(s)^z\),
differentiated at the integer parameter \(K\), contributes a local
logarithmic branch of order \(Km\). Write \(N\) for the actual order
in the complete arithmetic transform: \(N=Km\) if \(H_K\) and the
smoothing transform are nonzero at that zero, and their vanishing
orders must otherwise be added. Finite Euler factors of \(H_K\) can
vanish. The leading inverse-Laplace coefficient of
\((s-\rho)^N\log(s-\rho)\) is
\[
              (-1)^{N+1}N!\,
                   \frac{X^\rho}{(\log X)^{N+1}}.               \tag{15}
\]
If \(L=\log X\) and \(N=o(L)\), Stirling's formula gives
\[
 \log\!\left(\frac{N!}{L^N}\right)
      =-N\log(L/N)-N+O(\log(N+1))=o(L).                         \tag{16}
\]
In particular, even \(N\asymp L/\log L\) supplies only a
subpower factor in this bare coefficient. Ignoring \(N!\) wrongly
turns \(L^{-N}\) alone into a fixed power saving. A fixed power
from the coefficient (15) requires \(N\) of order \(L\), unless
some additional normalization or arithmetic factor changes the
calculation. The cost of such a normalization must then be included
in the complete estimate.

Equations (15) and (16) concern this exact elementary coefficient.
They are not a uniform expansion of a moving-order arithmetic
Hankel integral. In that integral the remaining analytic factors
also depend on \(K\); controlling them is an additional problem,
not a consequence of (16).

The completed result is therefore a parameter-uniform arithmetic
theorem with an essentially matching obstruction for its natural
logarithmic windows. It does not establish the marked derivative
remainder needed to move the zero-free boundary.
