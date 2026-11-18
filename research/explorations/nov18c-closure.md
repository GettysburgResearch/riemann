# What a finite Euler product costs in the Nyman–Beurling approximation

**Status.** Proposed unconditional bounds for finite Euler products multiplied by arbitrary signed Dirichlet polynomials. The arithmetic inputs are the prime number theorem and the Brun–Titchmarsh upper bound for ordinary primes in an interval. The arguments use no numerical zero census. The uniform approximation needed to prove RH remains open.

Put
\[
 E_y(s)=\prod_{p\le y}(1-p^{-s}),\qquad
 C(s)=\sum_{j=1}^{k} c_j d_j^{-s},\qquad A(s)=E_y(s)C(s).
\]
The distinct integers \(d_j\ge1\) and complex coefficients are unrestricted. The cost \(k\) counts terms of the correction \(C\), before multiplying it by the sieve. Write \(c(1)\) for the coefficient at 1, with value zero if absent. Use the functions
\[
 F(u)=\lfloor u\rfloor-2\lfloor u/2\rfloor,\qquad
 G(u)=\mathbf1_{u\ge1}-2\mathbf1_{u\ge2}.
\]
For a Dirichlet polynomial \(A(s)=\sum a_d d^{-s}\), define \(A[D]F(u)=\sum a_d F(u/d)\). The squared norm is \(\int_1^\infty |f(u)|^2du/u^2\). Both functions vanish below one. Their Mellin transforms in the convention \(\widehat f(s)=\int_1^\infty f(u)u^{-s-1}du\) are
\[
 \widehat G(s)=t(s),\qquad \widehat F(s)=t(s)\zeta(s),\qquad
 t(s)=(1-2^{1-s})/s .
\]
The second identity holds initially to the right of one and continues to \(\Re s>0\). Mellin evaluation on the normed space has norm \((2\Re s-1)^{-1/2}\) for \(\Re s>1/2\).

## The first interval left by the sieve

Fix \(0<\delta<1\). For all sufficiently large \(y\), all \(1\le k\le y^{1-\delta}\), and all \(C\) as above,
\[
 \int_y^{2y}|G(u)-A[D]F(u)|^2\frac{du}{u^2}
 \gg_\delta |c(1)|^2\frac{y}{(k+1)^2\log^2 y}.                  \tag{1}
\]
For \(c(1)=1\) this order is attainable on the displayed interval. Consequently convergence in the full norm forces \(k\log y/\sqrt y\to\infty\). This restriction also applies when some base integers or coefficients are arbitrarily large.

Let \(\Phi_y(u)=\#\{n\le u: p\mid n\Rightarrow p>y\}\), counting 1. Inclusion–exclusion gives \(E_y[D]F(u)=\Phi_y(u)-2\Phi_y(u/2)\). On \(y<u<2y\) this equals \(\pi(u)-\pi(y)-1\). For every integer \(d\ge2\), one has \(u/d\le y\) on the same interval, whence \(E_y[D]F(u/d)=G(u/d)\). Thus the residual is \(-c(1)(\pi(u)-\pi(y))\) plus a function constant on at most \(2k+1\) intervals, with potential breakpoints only at the \(d_j\) and \(2d_j\).

Here is a bound uniform over these partitions and all complex constants. Assign the primes of \((y,2y)\) to the partition intervals, using half-open endpoints. Write \(P=\pi(2y)-\pi(y)+O(1)\asymp y/\log y\), \(J\le2k+1\) for the number of intervals, and \(m\) for the count in one interval. If \(m\ge16\), the span between its first and its \(\lfloor m/4\rfloor\)-th prime, and likewise that between its last and its \(\lfloor m/4\rfloor\)-th from last, both have length \(\gg m\log(2m)\). This follows by inverting the uniform sieve bound \(\pi(x+h)-\pi(x)\ll h/\log(2h)\) for \(h\ge2\). The values of \(\pi(u)\) on the two spans are separated by at least \(m/3\), apart from immaterial endpoints. At least one span stays a distance \(\ge m/6\) from the real part of any given constant. Its unweighted squared error is \(\gg m^3\log(2m)\). The intervals with \(m\ge P/(2J)\) contain at least \(P/2\) primes. In the range of (1), \(P/(2J)\gg y^\delta/\log y\). Summing the lower bounds and using \(u\le2y\) gives (1).

For the upper bound use \(c(1)=1\) and put a correcting step at every \(r\)-th prime of \((y,2y]\), with coefficient \(-r\). Each such dilation is a single upward unit step before its coefficient is applied. Taking \(r=\lceil P/(k-1)\rceil\) for \(k\ge2\) yields discrepancy at most \(r\), with at most \(k-1\) additional dilations. For \(k=1\) use the uncorrected product. This gives the matching upper bound in (1) at the asserted range of \(k\). On \([1,2)\) the approximant equals \(c(1)\), so full norm convergence forces \(c(1)\to1\). If \(k>y^{3/4}\) the claimed necessary divergence already holds, and in the remaining range it follows from (1). [Montgomery and Vaughan, *The large sieve*](https://doi.org/10.1112/S0025579300004708)

## How many terms a short complex segment detects

Fix \(1/2<a<1\), and put \(L=y^{1-a}/\log y\). To achieve
\[
 \sup_{0\le t\le 4\pi/(3\log y)}
  |1-\zeta(a+it)E_y(a+it)C(a+it)|\le 1/2                          \tag{2}
\]
requires \(k\gg_a L\). Conversely some correction with \(k\ll_a L\) achieves (2) for all large \(y\). This solves the term-count question on this segment with constants depending on \(a\).

For the lower bound, \(\log(1/E_y(a))=\sum_{p\le y}p^{-a}+O_a(1)\asymp_a L\). On \(2\pi/(3\log y)\le t\le4\pi/(3\log y)\), the same real log modulus is \(\sum_{p\le y}p^{-a}\cos(t\log p)+O_a(1)\). For \(y^{9/10}\le p\le y\), the cosine is bounded above by a fixed negative constant. The smaller primes contribute \(o(L)\). Thus (2) forces \(|C(a)|\ge e^{c_a L}\) and \(|C(a+it)|\le e^{-c_a L}\) throughout this latter subinterval, decreasing \(c_a>0\) if necessary. Here \(\zeta(a)\ne0\), and continuity supplies the uniform local bounds for \(\zeta\).

Take \(h=2\pi/(3k\log y)\), \(z_j=\exp(-ih\log d_j)\), and \(Q(z)=\prod_{j\le k}(1-z/z_j)\). Multiply \(Q\) by the Taylor polynomial of \(1/Q\) through degree \(k-1\) to get \(H(z)=1+\sum_{m=k}^{2k-1} h_m z^m\). Its coefficient norm is at most \(2^k\sum_{n<k}\binom{n+k-1}{k-1}\le8^k\). Since \(H(z_j)=0\), summing against \(c_jd_j^{-a}\) gives
\[
 |C(a)|\le8^k\max_{k\le m<2k}|C(a+imh)|.
\]
All samples on the right belong to the latter subinterval. This proves the lower bound without a frequency-spacing assumption.

For the upper bound, \(1/E_y(s)=\sum_{P^+(n)\le y} n^{-s}\) with \(n=1\) included. Regard the weights \(n^{-a}\) as a finite-mass positive measure on \(v=\log n\). Its mass is at most \(e^{C_aL}\), and \(|1/E_y(a+it)|\ge e^{-C_a L}\) everywhere by the product. Truncate the measure at \(U=K_a y^{1-a}\). Its discarded mass is at most
\[
 e^{-U/\log y}/E_y(a-1/\log y)\le e^{-(K_a-C'_a)L}.
\]
Take \(K_a\) sufficiently large. The remaining measure has finite support. Its moments through degree \(M\) are reproduced by a nonnegative measure on at most \(M+1\) of the same nodes. Indeed the normalized moment vector through degree \(M\) is a convex combination in \(\mathbb R^M\), so Carathéodory's theorem applies.

Uniformly on the segment, \(|tv|\ll_a L\) for \(0\le v\le U\). The degree-\(M\) Taylor polynomial of \(e^{-itv}\) has uniform remainder at most \(e^{|t|U}(e|t|U/(M+1))^{M+1}\). For \(M=\lceil K'_a L\rceil\), choosing \(K'_a\) large makes the error after multiplication by either measure's mass at most \(e^{-(C_a+2)L}\). Thus the compressed positive Dirichlet polynomial approximates \(1/E_y(a+it)\) with relative error tending uniformly to zero. A mass \(w\) at \(v=\log d\) contributes coefficient \(wd^a\). Multiplying this polynomial by \(1/\zeta(a)\) proves (2), since \(\zeta(a+it)/\zeta(a)\to1\) uniformly. All support bounds here apply to term count. The allowed dilation sizes can be exponential in \(U\).

## The lower cost on an entire real interval

Fix \(1/2<a<b<1\) and a relative tolerance \(0<\eta<1\). On the real interval \([a,b]\), the least possible term count for
\[
     |1-\zeta(s)E_y(s)C(s)|\le\eta\qquad(a\le s\le b)
\]
has order \(y^{(1-a)/2}/\sqrt{\log y}\), with constants allowed to depend on \(a,b,\eta\). An attaining upper bound can require \(c(1)=1\) and use every other dilation above \(2y\). Such approximants asymptotically invert zeta on each fixed right half-plane \(\Re s\ge1+\epsilon\), while their squared physical error on the single shell \((y,2y)\) is \(\gg y/\log^2y\). Even relative errors tending to zero on \([a,b]\) are possible by letting the constant controlling term count grow sufficiently slowly.

Set \(S(s)=\log[-1/(\zeta(s)E_y(s))]\) for real \(s\) in a fixed compact enlargement of \([a,b]\) inside \((1/2,1)\). Here \(\zeta(s)<0\). For \(r=1,2,3\),
\[
  (-1)^r S^{(r)}(s)\asymp_{a,b} y^{1-s}(\log y)^{r-1}.
\]
Indeed the prime-power expansion gives the main sum \(\sum_{p\le y} p^{-s}(\log p)^r\), with bounded error from higher powers and from \(\log(-\zeta)\). Apply the prime number theorem and partial summation, retaining primes between \(y/2\) and \(y\) for the lower bound. In the same way \(S(s)\asymp y^{1-s}/\log y\).

For the lower bound put \(h=1/(2k\log y)\) and sample \(C\) at \(a+(i+j)h\), \(0\le i,j\le k\). The resulting Hankel matrix has rank at most \(k\) since each term contributes one outer product. Multiply by minus one and divide row and column \(i\) by \(\exp(S(a+2ih)/2)\). The diagonal entries have modulus at least \(1-\eta\). Strong convexity on \([a,a+1/\log y]\) bounds the off-diagonal entries by
\[
 (1+\eta)\exp\bigl(-c_{a,b} y^{1-a}\log y\,h^2(i-j)^2\bigr).
\]
When \(k\) is smaller than a sufficiently small constant times \(y^{(1-a)/2}/\sqrt{\log y}\), every off-diagonal row sum is below \(1-\eta\). Strict diagonal dominance contradicts the rank bound.

For the construction extend the interval to \(I=[a-1/\log y,b+1/\log y]\). Put \(\lambda(x)=\sqrt{S''(x)}\), and use the coordinate \(d\xi=\lambda(x)dx\). Define
\[
 B(s,x)=S(s)-S(x)-S'(x)(s-x).
\]
Uniformly for \(s\in[a,b]\), one has
\[
      (2\pi)^{-1/2}\int_I e^{-B(s,x)}d\xi(x)=1+o(1).
\]
To see this, write \(v=\xi(x)-\xi(s)\). The maximum of \(|d\log\lambda/d\xi|\) on \(I\) tends to zero by the derivative bounds above. Since \(dB/dv=\lambda(x)(x-s)\), the derivative is \(v+o(1)\) uniformly on every bounded \(v\)-interval. For \(|v|\ge1\), the last unit of the coordinate integral from \(s\) to \(x\) gives \(|\lambda(x)(x-s)|\ge1/2\). Thus \(B\ge(|v|-1)/2\) there, and the integral converges uniformly to its Gaussian value. Both endpoints of \(I\) lie a coordinate distance tending to infinity from \([a,b]\).

Use a grid of width \(h_0>0\) in \(\xi\) and the actual interval lengths for any shorter end cell. At any \(s\) the integrand rises to 1 and falls, so the absolute rectangle-rule error is at most \(2h_0\). Choose \(h_0\) sufficiently small in terms of \(\eta\). Multiplying the quadrature by \(e^{S(s)}\) gives a positive sum of tangents \(w_j\exp(S(x_j)-x_jS'(x_j))\exp(sS'(x_j))\), with the normalized location weights \(w_j>0\). Replace \(\exp(-S'(x_j))\) by its nearest integer \(d_j\). The bases exceed \(\exp(c_{a,b} y^{1-b})\), so the positive sum changes by relative \(o(1)\) uniformly on \([a,b]\). Negate the sum to approximate \(1/(\zeta E_y)\) and add 1 to obtain \(c(1)=1\). The 1 has vanishing relative size there. The term count is at most
\[
 2+h_0^{-1}\int_I\sqrt{S''(x)}\,dx
       \ll_{a,b,\eta} y^{(1-a)/2}/\sqrt{\log y}.
\]
Coincident integer bases can be combined. At \(\Re s\ge1\), every tangent has modulus at most a constant times \(w_j\exp(-c_{a,b}y^{1-b})\), because \(\Re s-x_j\) stays positive and \(S(x_j)=O(-S'(x_j)/\log y)\). Rounding the base changes this bound by at most a fixed factor, using monotonicity of \(d_j^{-\Re s}\) to reduce to \(\Re s=1\). Thus \(C(s)\to1\) there. The finite Euler product converges uniformly to \(1/\zeta(s)\) on \(\Re s\ge1+\epsilon\). On the physical shell all correcting dilations exceed \(2y\), leaving the uncorrected prime staircase. This proves the stated norm divergence.

## Which compactness statement would resolve RH

Suppose \(A_j(s)=E_{y_j}(s)C_j(s)\), \(y_j\to\infty\), and \(\zeta(s)A_j(s)\to1\) on a real interval strictly inside \((1/2,1)\). If \(\sup_j\|A_j[D]F\|<\infty\), then RH holds. Indeed a weakly convergent subsequence exists in the Hilbert space. By bounded Mellin evaluation its weak limit has transform \(t(s)\) on the real interval, hence throughout \(\Re s>1/2\) by the identity theorem. At an off-line zero \(\rho\) in this half-plane the transform of every approximant vanishes but \(t(\rho)\ne0\), a contradiction. Weak convergence along that subsequence also forces \(c_j(1)\to1\) by testing the first unit interval.

Conversely RH gives norm approximants without any bound on term count. The strong Nyman–Beurling criterion approximates \(\mathbf1_{u\ge1}\) by linear combinations of integer-dilated fractional parts \(\{u/d\}\) in \(L^2((0,\infty),du/u^2)\). Apply the bounded map \(I-2D_2\), where \(D_2f(u)=f(u/2)\), to kill the linear terms and obtain combinations of \(F(u/d)\) approximating \(G\), absorbing the minus sign in the coefficients. For each fixed \(y\) the operator \(E_y[D]\) has a bounded inverse given by the sum of \(D_n\) over all \(y\)-smooth integers, since \(\|D_n\|=n^{-1/2}\) and \(\prod_{p\le y}(1-p^{-1/2})^{-1}<\infty\). Truncating this sum in operator norm permits the same approximation with \(A=E_y C\) at that \(y\). Diagonalize over \(y\to\infty\). [Báez-Duarte, *A strengthening of the Nyman–Beurling criterion for the Riemann hypothesis*](https://arxiv.org/abs/math/0202141)

The local constructions above supply no uniform full norm. For example the first-shell quantile steps control precisely \((y,2y)\). They create additional contributions at every higher dilation of that interval. The open estimate concerns their accumulated norm on the entire half-line. [Earlier smoothed Möbius construction and its remaining arithmetic hypothesis](nov18b-reciprocal-log-taper.md)
