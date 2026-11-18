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
If the conductor \(D\) of \(\chi\) tends to infinity, the left hand side is at least \((2/(3\sqrt3))\log D-O(\log\log D)\), with an absolute implied constant. These assertions are unconditional. Thus, for every \(q>2\), the residue classes with positive limiting supremum have images spanning \((\mathbf Z/q)^\times/((\mathbf Z/q)^\times)^2\). In particular at least its \(\mathbf F_2\)-dimension many classes with independent images fail the eventual strict negativity asked about in [Zhao's §8(2)](https://doi.org/10.1007/s40993-025-00640-y). For \(q=3,4,6\), the unique nonsquare class is respectively \(2,3,5\).

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

For any fixed \(t>0\), when the remaining zeros lie on the line,
\[
       K(t)= (e^{-t/2}-e^{-3t/2})\log D+O_t(\log\log(3D)). \tag{4a}
\]
Use the inverse transform \(g(v)=k(v+t)\) with \(k(v)=(e^{-v/2}-e^{-3v/2})\mathbf1_{v>0}\), so its transform at a real ordinate is \(e^{it\gamma}/[\rho(1+\rho)]\). Choose a fixed smooth cutoff, translated so it is one up to \(R\) and zero after \(R+1\), and multiply \(g\) by this cutoff to give \(g_R\). Its support is contained in \([-t,R+1]\). The Fourier transform of the removed tail is \(O_t(e^{-R/2}/(1+\gamma^2))\), because the tail and its first two derivatives have \(L^1\) norms \(O_t(e^{-R/2})\). The classical unit-interval zero counts for the two functions are \(O(\log(D(2+|\gamma|)))\) even without either individual GRH. Thus replacing the kernel in the signed series over remaining real ordinates costs \(O_t(e^{-R/2}\log(3D))\).

Apply the Dirichlet explicit formula to the difference of the primitive character and zeta zero sums for the compactly supported \(g_R\). It is continuous and piecewise smooth with a single jump in its first derivative, admissible by ordinary smooth approximation. Its transform is entire, so any off-line zeros common to both functions with equal multiplicity cancel exactly. The conductor term is \(g_R(0)\log D=k(t)\log D\). The prime contributions are \(O_t(1+R)\): on positive logarithms \(|g_R(\log n)|\ll_t n^{-1/2}\) for \(n\le e^{R+1}\), while \(g_R(-\log n)\) is supported on \(n\le e^t\). Use \(\sum_{n\le x}\Lambda(n)/n\ll\log(2x)\). The gamma terms are \(O_t(1)\) because the real-axis transforms are uniformly \(O_t((1+\gamma^2)^{-1})\). The two pole terms of the zeta formula, equal to the transforms at \(\pm i/2\), cost \(O_t(1+R)\) by integrating \(|g_R(v)|e^{\pm v/2}\) on its support. Take \(R=4\log\log(3D)\) to prove (4a). Finally \(k(\log 3)=2/(3\sqrt3)\) and recurrence gives the claimed limiting supremum. In the off-critical case (2) already exceeds any finite lower bound.

Finally, if the images of the classes satisfying \(\limsup J_a>0\) generated a proper subgroup of the quotient by squares, some nontrivial quadratic character would be one on this entire subgroup. This contradicts (1). This spanning statement does not identify a particular nonsquare class when the coset has multiple elements.

## A positive proportion of individual classes per prime modulus

Assume the Dirichlet \(L\)-functions modulo a prime \(q\) have no real zero in \((1/2,1)\). In particular GRH is sufficient. Fix \(0<\delta<1/4\). For all sufficiently large \(q\), each prime
\[
 \delta q\log q <p<(1/2-\delta)q\log q,\quad
 a\equiv p\pmod q,\quad a\not\equiv0,1,-1\pmod q
\]
satisfies
\[
               \limsup_{X\to\infty}J_a(X)\gg_\delta\sqrt{q\log q}. \tag{4}
\]
These explicitly specified classes number \(\gg_\delta q\) for each sufficiently large prime modulus. This includes classes on either side of the square-class partition whenever they have a prime witness as above.

Use the weight \(\mu_a(\rho)=\sum_{\chi\bmod q}\bar\chi(a)m_\chi(\rho)\) on zero multiplicities of the primitive \(L\)-functions, with \(\zeta\) for the principal character. If some off-critical weight is nonzero, reflection across the critical line for each character gives a nonzero weight at a zero with \(\beta>1/2\). For each \(1/2<c<\beta\), the unnormalized integral then has limiting supremum and infimum \(+\infty,-\infty\) after division by \(X^{1+c}\). Indeed, its Mellin transform times \(s(s+1)\varphi(q)\) is \(\sum_\chi\bar\chi(a)\log L(s,\chi^*)+\log(s-1)\) plus a holomorphic term for \(\Re s>1/2\), by prime orthogonality. The missing Euler factor at \(q\) is holomorphic there too. Its derivative has residue \(\mu_a(\rho)\) at the chosen zero, but the real segment of continuation above \(1/2\) is regular by the hypothesis. Apply the one-sided Landau argument from (2) to either sign. Complex character weights pair to real values along the real axis.

In the remaining case all off-critical terms cancel. Character orthogonality, the once-integrated explicit formula and the prime number theorem in fixed progressions give the real almost-periodic profile
\[
 J_a(X)=-2C_q(a)/3-K_a(\log X)+o_q(1),\qquad
 K_a(t)=\sum_\gamma\frac{\mu_a(1/2+i\gamma)e^{i\gamma t}}{(1/2+i\gamma)(3/2+i\gamma)} .
\]
Here \(C_q(a)\) counts square roots of \(a\) modulo \(q\), hence is at most two. The squares in the normalized \(\psi\)-to-\(\vartheta\) transition contribute \(C_q(a)\sqrt x+o_q(\sqrt x)\). As in (3) the remaining absolutely convergent sum gives a value approached arbitrarily late at each specified phase.

For \(2\le Y\le q^2\) choose \(t=\log Y\). Use the compact kernel \(g_R(v)=k(v+t)\chi_R(v)\) from (4a), with \(0\le\chi_R\le1\), \(R=4\log q\). On the remaining real ordinates its replacement error in the Fourier sum is \(O(q\log q\,e^{-R/2}/\sqrt Y)\), by two tail integrations by parts and summation of the unit-interval counts over all characters. The explicit formula before this approximation has exact cancellation at all common off-line terms with \(\mu_a(\rho)=0\).

In the convention \(h(z)=\int g_R(v)e^{-izv}dv\), the right vertical line pairs \(\chi(n)\) with \(g_R(-\log n)\); the reflected line pairs \(\bar\chi(n)\) with \(g_R(\log n)\). Thus the direct and reflected prime contributions to \(-K_a(t)\) are respectively
\[
 \begin{split}
 Y^{-1/2}\sum_{n<Y}\Lambda(n)(1-n/Y)
   \left((q-1)\mathbf1_{n\equiv a\ (q)}+\mathbf1_{q\mid n}\right),\\
 Y^{-1/2}\sum_{n\ge2}\frac{\Lambda(n)}n(1-1/(Yn))\chi_R(\log n)
   \left((q-1)\mathbf1_{n\equiv a^{-1}\ (q)}+\mathbf1_{q\mid n}\right).
 \end{split}
\]
The extra terms at powers of \(q\) are from the principal primitive function \(\zeta\). Both displayed sums are nonnegative. The conductor term costs \(O(\log q/\sqrt Y)\), since the sum of \(\bar\chi(a)\) over nonprincipal characters is \(-1\). The gamma contributions vanish: summed over all characters, both parity totals vanish for \(a\ne\pm1\). The pole contribution from \(\zeta\) in \(-K_a(t)\) is minus the sum of the transforms at \(\pm i/2\). Its magnitude is
\[
              \sqrt Y/2+O((1+R+\log Y)/\sqrt Y).
\]
Indeed the term with \(e^{-v/2}\) integrated against the uncut \(g\) is \(\sqrt Y\int_0^\infty(e^{-w}-e^{-2w})\,dw=\sqrt Y/2\), and cutting off its tail costs \(O(e^{-R}/\sqrt Y)\). For \(e^{v/2}\) the integrand is at most \(Y^{-1/2}\) over its support of length \(R+1+\log Y\).

Take \(Y=2p\). The direct atom at \(n=p\) supplies \((q-1)\log p/(2\sqrt Y)\). Dropping the other nonnegative prime terms gives
\[
  \limsup J_a(X)\ \ge\ \frac{(q-1)\log p/2-p}{\sqrt{2p}}-O(1+\log q/\sqrt p).
\]
For the displayed interval of primes this proves (4). Recurrence uses \(X\to\infty\) for each fixed \(q\).

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

In the same setting take \(2\le a\le q-2\) as its least positive representative and let \(b\in[1,q-1]\) represent its inverse. Now set \(Y=a\). The direct sum above has no positive term from the class \(a\): the first possible representative is the zero-weight endpoint. The direct sum therefore vanishes and the poles contribute \(-\sqrt a/2+O(\log q/\sqrt a)\). Bound the reflected sum up to its support endpoint \(Z=e q^4\) by counting every integer in the class \(b\), together with \(O(\log q/q)\) from the ramified powers. Specifically,
\[
    (q-1)\sum_{n\le Z,\ n\equiv b\ (q)}\frac{\Lambda(n)}n
       \ll q\log q/b+\log^2 q.
\]
This follows by isolating \(b\) and summing \((b+jq)^{-1}\le(jq)^{-1}\) thereafter. The same cutoff, conductor and gamma estimates apply. Consequently
\[
 \liminf_{X\to\infty} J_a(X)
 \le -(1/2+o(1))\sqrt a
      +O\left(1+\frac{q\log q/b+\log^2 q}{\sqrt a}\right).
\]
For any \(f(q)\to\infty\) with \(f(q)^2\log^2 q=o(q)\), all but \(O(q/f(q)+1)\) classes have both \(a,b\ge q/f(q)\), so their limiting infimum is at most \(-(1/2-o(1))\sqrt{q/f(q)}\). For the positive-proportion conclusion in (4), fix a sufficiently small constant \(c>0\) and exclude the at most \(2cq+2\) classes with \(a<cq\) or \(b<cq\). A positive proportion of all classes then have both a positive limiting supremum \(\gg\sqrt{q\log q}\) and a negative limiting infimum \(\ll-\sqrt q\). The implied constants can be fixed, for example, by first taking \(\delta=1/10\) in (4).
