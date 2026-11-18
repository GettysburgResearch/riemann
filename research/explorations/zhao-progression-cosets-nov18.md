# Unconditional positive excursions for residue classes outside the squares

For each reduced class \(a\bmod q\) put
\[
 J_a(X)=\frac{\varphi(q)\log X}{X^{3/2}}\int_2^X
  \left(\pi(t;q,a)-\frac{\operatorname{li}(t)}{\varphi(q)}\right)dt.
\]
For every nonprincipal quadratic character \(\chi\bmod q\),
\[
 \max_{a:\chi(a)=-1}\limsup_{X\to\infty}J_a(X)>0. \tag{1}
\]
If the conductor \(D\) of \(\chi\) tends to infinity, the left hand side is at least \(4/3-O((\log\log D)^{-2})\), with an absolute implied constant. These assertions are unconditional. Thus, for every \(q>2\), the residue classes with positive limiting supremum have images spanning \((\mathbf Z/q)^\times/((\mathbf Z/q)^\times)^2\). In particular at least its \(\mathbf F_2\)-dimension many classes with independent images fail the eventual strict negativity asked about in [Zhao's §8(2)](https://doi.org/10.1007/s40993-025-00640-y). For \(q=3,4,6\), the unique nonsquare class is respectively \(2,3,5\).

## The average over a quadratic coset

Let \(\chi^*\) be the real primitive character inducing \(\chi\), and let
\[
 H(X)=\int_2^X(\pi(t)-\operatorname{li}(t)-\pi(t,\chi^*))dt.
\]
Since \(2\mathbf1_{\chi(p)=-1}=1-\chi^*(p)\) at primes not dividing \(q\), the average of \(J_a(X)\) over \(\chi(a)=-1\) is \(X^{-3/2}\log X\,H(X)+O_q(X^{-1/2}\log X)\). It suffices to bound the limiting supremum of this average. Finitely many reduced classes then allow us to select one class for arbitrarily large \(X\).

## Off-critical zeros that remain after cancellation

Use the multiset difference with signed multiplicity \(m(\rho)=m_{L(\cdot,\chi^*)}(\rho)-m_\zeta(\rho)\). Suppose there is some unmatched zero off the critical line. Reflection gives one at \(\rho\) with \(\beta=\Re\rho>1/2\). For each \(1/2<c<\beta\),
\[
        \limsup_{X\to\infty}X^{-1-c}H(X)=+\infty. \tag{2}
\]
To see this, put \(M(s)=\int_2^\infty H(X)X^{-s-2}dX\) for \(\Re s>1\). Integrating the prime powers and the logarithmic integral gives
\[
    s(s+1) M(s)
    = \log\big((s-1)\zeta(s)/L(s,\chi^*)\big)+ U(s)
\]
with \(U\) single-valued and holomorphic on \(\Re s>1/2\). Indeed, a prime's integral equals \(p^{-s}/[s(s+1)]\), the series of second and higher prime powers converges absolutely there, and the pole at 1 is removed by the logarithmic-integral term. Explicitly \(\int_{\log 2}^{\infty} e^{-(s-1)v}dv/v+\log(s-1)\) extends to an entire function, as seen by differentiation and its finite limit at 1. The endpoint \(\operatorname{li}(2)2^{-s}\) is entire.

Suppose \(A X^{1+c}-H(X)\ge0\) eventually for some constant \(A\). Its similarly weighted Mellin transform has abscissa of convergence \(\sigma_0\ge\beta\), since otherwise the identity above would give a holomorphic continuation of the logarithm near \(\rho\) in a half-plane, contrary to the pole of its derivative. Also \(\sigma_0\le1\). Landau's theorem gives a singularity on the real axis at \(\sigma_0\). The factor \((s-1)\zeta(s)\) is positive throughout the real interval \((1/2,\infty)\), including its value 1 at the removable point. Consequently a singularity here would have to be a real zero of \(L(s,\chi^*)\). There are none to the right of \(\sigma_0\), by the convergent Mellin identity. At such a zero at \(\sigma_0\) we would have \(M(\sigma)\to+\infty\) as \(\sigma\downarrow\sigma_0\). This too is impossible, since our eventual upper bound majorizes the real integral uniformly down to \(\sigma_0>c\). This proves (2), including the case of a positive real off-critical zero.

## When the remaining zeros lie on the line

No condition on the location of zeros common to the two functions with equal multiplicity is needed. The once-integrated explicit formula gives
\[
 \frac{\log X}{X^{3/2}}H(X)=
 K(\log X)+o_q(1),\qquad
 K(v)=\sum_{\rho=1/2+i\gamma}\frac{m(\rho)e^{i\gamma v}}{\rho(1+\rho)}. \tag{3}
\]
Indeed subtracting the once-integrated explicit formulas for \(\psi(t)-t\) and \(\psi(t,\chi^*)\) cancels all common zero terms, and the resulting zero series converges absolutely. The unintegrated prime squares cancel except at the finitely many ramified primes, whose powers contribute \(O_q(\log t)\). Higher powers contribute \(O(t^{1/3}\log^2 t)\). Replacing \(\psi\) with \(\vartheta\) in the difference of primitives therefore costs \(O_q(X^{4/3}\log^2 X)\). Partial summation as in the [prime-tail identity](zhao-bias-kernel-nov18.md) converts this primitive to \(H(X)\), dividing its main term by \(\log X\) with error \(O_q(X^{3/2}/\log^2 X)\).

The uniformly almost-periodic series \(K\) has mean \(4m(1/2)/3\ge0\). If the mean is positive, this already proves (1). Otherwise \(K\) is nonzero: the positive-height zero counts for primitive \(L(s,\chi^*)\) and \(\zeta(s)\) differ by \((T/(2\pi))\log D+O_D(\log T)\), which guarantees an unmatched noncentral zero. Uniqueness of Fourier coefficients gives \(K\not\equiv0\), and a nonzero uniformly almost-periodic real function of mean zero attains positive values recurrently. More quantitatively, the nonnegative function \(\sup K-K\) has each nonconstant coefficient bounded in modulus by its own mean, so \(\sup K\ge 4m(1/2)/3+|m(\rho)/(\rho(1+\rho))|\) for any unmatched noncentral zero on the line.

## Uniform lower bound as the conductor grows

When \(m(1/2)\ge1\), (3) already gives \(\limsup K\ge4/3\). Otherwise use the real even test
\[
 h_R(t)=(1-R^2t^2)(\sin(Rt)/(Rt))^4,\qquad R=\tfrac13\log\log D.
\]
The inverse transform has support \([-4R,4R]\), supremum norm \(O(1/R)\), and value \(1/(12R)\) at zero by the [low-zero calculation](zhao-bias-central-nov18.md). Apply the explicit formula to the *difference* of the primitive character and zeta zero sums for this entire test. Common off-line terms cancel even if their individual ordinates make the test argument complex. The ramified and ordinary prime terms are \(O(e^{2R}/R)\) by Chebyshev's bound. Contributions of the two gamma factors are \(O(1/R)\) after integration, and the pole terms \(h_R(\pm i/2)\) of the zeta formula are \(O(e^{2R}/R^2)\). Thus
\[
 \sum_{\gamma}m(1/2+i\gamma)h_R(\gamma)
 =\log D/(12R)+O(e^{2R}/R)>0
\]
for large \(D\). On \(|\gamma|\ge1/R\), the test is nonpositive. Terms there with negative multiplicity difference can contribute positively, but are bounded in sum by \(O(R^{-2})\): they come from critical-line zeta ordinates, all of which have \(|\gamma|>14\), and \(|h_R(\gamma)|\ll (R|\gamma|)^{-2}\). Since the total is \(\gg \log D/R\), some unmatched noncentral character ordinate has \(|\gamma|<1/R\). Its coefficient has modulus at least \(4/3-O(R^{-2})\). Almost-periodicity in (3) and the bound for \(\sup K\) give the asserted lower bound.

Finally, if the images of the classes satisfying \(\limsup J_a>0\) generated a proper subgroup of the quotient by squares, some nontrivial quadratic character would be one on this entire subgroup. This contradicts (1). This spanning statement does not identify a particular nonsquare class when the coset has multiple elements.

## A positive proportion of individual classes per prime modulus under GRH

Assume GRH for the Dirichlet characters modulo a prime \(q\), including RH for the principal character. Fix \(0<\delta<1/4\). For all sufficiently large \(q\), each prime
\[
 \delta q\log q <p<(1/2-\delta)q\log q,\quad
 a\equiv p\pmod q,\quad a\not\equiv0,1,-1\pmod q
\]
satisfies
\[
               \limsup_{X\to\infty}J_a(X)\gg_\delta\sqrt{q\log q}. \tag{4}
\]
These explicitly specified classes number \(\gg_\delta q\) for each sufficiently large prime modulus. This includes classes on either side of the square-class partition whenever they have a prime witness as above.

For each nonprincipal \(\chi\bmod q\), all primitive, let \(K_\chi(t)=\sum_{\rho_\chi}e^{i\gamma t}/[\rho(1+\rho)]\) and use \(K_\zeta\) for the principal term. Character orthogonality, the once-integrated explicit formula and the prime number theorem in fixed progressions give
\[
 J_a(X)=-2C_q(a)/3-K_\zeta(\log X)
      -\sum_{\chi\ne\chi_0}\bar\chi(a)K_\chi(\log X)+o_q(1),
\]
where \(C_q(a)\) is the number of square roots of \(a\) modulo \(q\), hence at most two. Indeed the squares in the normalized \(\psi\)-to-\(\vartheta\) transition contribute \(C_q(a)\sqrt t+o_q(\sqrt t)\). All Fourier series are absolutely convergent under the stated GRH. Their combined real almost-periodic profile is approached arbitrarily late at any specified phase \(t\).

Choose \(Y=2p\) and \(t=\log Y\). In the explicit formula for \(K_\chi(t)\), the inverse Fourier kernel is \(g(v)=k(v+t)\), with \(k(v)=(e^{-v/2}-e^{-3v/2})\mathbf1_{v>0}\). In the convention \(h(z)=\int g(v)e^{-izv}dv\), expanding the logarithmic derivative on the right vertical line pairs \(\chi(n)\) with \(g(-\log n)\); the reflected line pairs \(\bar\chi(n)\) with \(g(\log n)\). Thus the direct prime contribution to \(-\sum_{\chi\ne\chi_0}\bar\chi(a)K_\chi(t)\) equals
\[
 Y^{-1/2}\sum_{n<Y}\Lambda(n)(1-n/Y)
 \left((q-1)\mathbf1_{n\equiv a\ (q)}-\mathbf1_{q\nmid n}\right).
\]
At \(n=p\) the first term alone supplies \((q-1)\log p/(2\sqrt Y)\). All other first terms are nonnegative. The full subtractive sum is at most \((1/2+o(1))\sqrt Y\) by the ordinary prime number theorem and partial summation.

The reflected prime terms give
\[
 Y^{-1/2}\sum_{n\ge2}\frac{\Lambda(n)}{n}(1-1/(Yn))
 \left((q-1)\mathbf1_{n\equiv a^{-1}\ (q)}-\mathbf1_{q\nmid n}\right).
\]
Truncate these at \(Z=q^4\). The tail costs \(O(q Y^{-1/2} Z^{-1/2}\log^2(qZ))\) by partial summation of \(\psi(x,\chi)\ll\sqrt x\log^2(qx)\) for each nonprincipal character. In the initial part discard the nonnegative term and bound the subtractive sum by \(O(\log Z/\sqrt Y)\). These ordinary convergent reflected sums agree with the explicit formula by damping the translated kernel on its support and then using Abel convergence.

The conductor term costs \(O(\log q/\sqrt Y)\), since the sum of \(\bar\chi(a)\) over nonprincipal characters is \(-1\). Their signed parity totals for \(a\ne\pm1\) are \(-1\) for even characters and zero for odd characters, so the combined gamma term is \(O(1)\). Each parity integral has this absolute bound uniformly in \(t\) by integration of \(O(\log(2+|v|)/(1+v^2))\) on the ordinate axis. The critical zeta term is also \(O(1)\) by absolute convergence. The resulting limsup bound is
\[
 \frac{(q-1)\log p/2-(1+o(1))p}{\sqrt{2p}}-O(1+\log q/\sqrt p).
\]
For the displayed interval of primes this proves (4). The approximation \(o_q(1)\) in the profile is used only by letting \(X\to\infty\) for each fixed \(q\).

To count the distinct classes, put \(x=q\log q\) and let \(N_a\) be the number of primes in that interval belonging to class \(a\bmod q\). The ordinary prime number theorem gives \(\sum N_a\gg_\delta q\). The classical Selberg upper-bound sieve for a pair of linear forms gives, uniformly for even \(0<h\le x\),
\[
 \#\{p\le x:p,p+h\text{ prime}\}
 \ll \frac{x}{\log^2 x}\prod_{\ell\mid h,\ \ell>2}\left(1+\frac1{\ell-2}\right).
\]
For odd \(h\) at most one such pair has both entries prime. This is the standard twin-prime upper bound with local factors at the primes dividing the shift retained. For \(h=jq\), the product is at most twice that for \(j\) alone. Its average over \(j\le L\) is bounded by \(\prod_{\ell>2}(1+1/[\ell(\ell-2)])\), by expanding into squarefree divisors and counting multiples. Thus
\[
  \sum_a\binom{N_a}{2}
   \ll (x/\log^2 x)(x/q)+x/q\ll q.
\]
Cauchy–Schwarz yields \(\#\{a:N_a>0\}\gg_\delta q\); omitting \(0,1,-1\) has negligible effect. The pair bound requires no assumption about an asymptotic for prime pairs. [H. Halberstam and H.-E. Richert, *Sieve Methods*](https://openlibrary.org/works/OL27997677W)

### A negative phase for almost every class

In the same setting take \(2\le a\le q-2\) as its least positive representative and let \(b\in[1,q-1]\) represent its inverse. Now set \(Y=a\). The direct sum above has no positive term from the class \(a\): the first possible representative is the zero-weight endpoint. Its subtractive contribution is \(-(1/2+o(1))\sqrt a\) as \(a\to\infty\). In the reflected sum bound the positive part before \(Z=q^4\) by counting every integer in the class \(b\). Specifically,
\[
    (q-1)\sum_{n\le Z,\ n\equiv b\ (q)}\frac{\Lambda(n)}n
       \ll q\log q/b+\log^2 q.
\]
This follows by isolating \(b\) and summing \((b+jq)^{-1}\le(jq)^{-1}\) thereafter. The same tail, conductor and gamma estimates apply. Consequently
\[
 \liminf_{X\to\infty} J_a(X)
 \le -(1/2+o(1))\sqrt a
      +O\left(1+\frac{q\log q/b+\log^2 q}{\sqrt a}\right).
\]
For any \(f(q)\to\infty\) with \(f(q)^2\log^2 q=o(q)\), all but \(O(q/f(q)+1)\) classes have both \(a,b\ge q/f(q)\), so their limiting infimum is at most \(-(1/2-o(1))\sqrt{q/f(q)}\). For the positive-proportion conclusion in (4), fix a sufficiently small constant \(c>0\) and exclude the at most \(2cq+2\) classes with \(a<cq\) or \(b<cq\). A positive proportion of all classes then have both a positive limiting supremum \(\gg\sqrt{q\log q}\) and a negative limiting infimum \(\ll-\sqrt q\). The implied constants can be fixed, for example, by first taking \(\delta=1/10\) in (4).
