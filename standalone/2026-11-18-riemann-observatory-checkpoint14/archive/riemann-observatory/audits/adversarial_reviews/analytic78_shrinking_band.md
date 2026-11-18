# Gaussian limit on shrinking logarithmic prime bands

18 November 2026. Assume RH. Let \(L=\log Y\), \(a=a(Y)\), \(b=b(Y)\), with \(0<a<b\) eventually, \(b\to0\), \(a/b\to r\in(0,1)\) and \(aL\to\infty\). Use the probability law on the strict two-sided tail \(|\gamma|>Y\) of zeta zeros with masses proportional to \(|\zeta'(1/2+i\gamma)|^2/(1/4+\gamma^2)\). Set
\[
 {\cal P}_Y=\{p:Y^a<p\le Y^b\},\qquad
 W_Y=\sum_{{\cal P}_Y}p^{-1/2}\cos(\gamma\log p),\qquad
 H_Y=\sum_{{\cal P}_Y}p^{-1}.
\]
Both \(W_Y-E_YW_Y\) and \(W_Y-H_Y\) converge weakly and in every fixed moment to \(N(0,\frac12\log(1/r))\). This concerns one scalar at each \(Y\). No process topology or tightness statement across band endpoints is used.

Fix \(0<r_-<r<r_+<1\), a moment order \(j\ge1\) and a log-saving parameter \(M\ge1\). For either centering the discrepancy in the \(j\)-th moment from that target normal law is
\[
 O^{\rm eff}_{j,M,r_-,r_+}\!
 \left(b+L^{-M}+e^{-aL/2}+\frac1{aL}+\left|\frac ab-r\right|\right)
 \tag{1}
\]
when \(a/b\in[r_-,r_+]\), \(aL\ge1\), \(2\max(j,2)b\le1/4\), and \(Y\) exceeds a fixed effective threshold for those parameters. Here effectivity uses the exceptional-prime version of the HLZ aggregate estimate. Constants can be extracted in principle from that proof, but are not tabulated numerically. Without exceptional-prime removal the ordinary shifted theorem gives the same convergence and a possibly ineffective bound, dropping the exponential term.

## Uniform prefix comparison

For \(T\ge Y\), let \(E_T\) denote the normalized prefix expectation with weights \(|\zeta'(\rho)|^2\) at \(0<\gamma\le T\). Keep the prime set fixed at its \(Y\)-values when varying \(T\). Write \(D(s)=\sum_{{\cal P}_Y}p^{-s}\), with \(W_Y=\Re D(\rho)\). Binomially expand \((D+\bar D)^k/2^k\), where \(k\le J=2\max(j,2)\). Each \(D^u\) has nonnegative real coefficients bounded by \(u!\) and support at most \(Y^{ub}\). In every cross term \(u+v=k\), so both arrays fit into declared length \(T^{1/4}\) under the stated cutoff. The union of the two divisor closures is also within this length. Use the four signs of a common positive baseline of sufficiently large fixed size on that union. On the support all entries stay between two positive constants. Each factor of a supported product belongs to the support, so the required submultiplicative bound holds with a common constant. Four-sign polarization recovers the symmetrized cross term. This is the real part under RH after differentiating the shifted zeta factors. It suffices because the power expansion is real and pairs each word with its conjugate. This retains the aggregate remainder with arbitrary fixed log savings before Cauchy differentiation. There is no factor proportional to the support size multiplying that remainder. [HLZ journal Theorem 5, p. 1605, and (5), (24)](../../sources/classical63_derivative_moments/hlz2022print.pdf) · [Bounded coefficient cutoff audit](weighted70_hlz_cutoff_review.md)

For indices \(m=gh,n=gk'\), the exact main term carries \(1/\operatorname{lcm}(m,n)\). On fixed separated Cauchy circles of radius proportional to \(1/\log T\), compare its arithmetic multiplier to the one at \(h=k'=1\) before differentiating. The monomial factors \(h^{-v/\log T}\) and their counterparts in (5) are \(1+O(\log(hk')/\log T)\). For a prime power \(p^e\Vert k'\), the exact source local quotient is the shifted series over \(f_{d+e}\) divided by the series over \(f_d\), both evaluated at \(t=p^{-1-v/\log T}\), where
\[
 \sum_{d\ge0}f_dt^d=\frac{1-t}{(1-Ut)(1-Wt)},\qquad
 U=p^{-u/\log T},\qquad W=p^{-w/\log T}.
\]
The quotient equals one at \(U=W=1\), for all the allowed \(t\). For \(e\le J\), differentiating the rational generating expression, or its absolutely convergent series with bounded \(e\), gives \(1+O_J(e\log p/\log T)\). In detail, the contours may be chosen small enough that \(|Ut|,|Wt|,|t|\) are uniformly below one. The series coefficients and the derivatives in bounded \(U,W\) are bounded by a fixed polynomial in \(d+e\) times \(\max(1,|U|,|W|)^{d+e}\), giving bounded derivatives of the quotient on the small neighborhood of the unit pair. There are at most \(J\) distinct primes in these comparisons. With the total \(\log(mn)/\log T\le k b L/\log T\), the product of the local factors differs from the untwisted one by \(O_J(bL/\log T)\). This comparison works also on the coincidence loci. The shifted zeta and integrated time factors are common to the twisted and untwisted comparisons. Their scaling and mixed differentiation give \(O(T(\log T)^4)\) times that relative bound for the pair after factoring out the lcm weight. For \(m=n\) the exact arithmetic factor is the untwisted one. [HLZ local comparison and source scaling](director_hlz_uniform_round9.md) · [Aggregate version at power length](weighted70_hlz_cutoff_review.md)

Introduce independent circle variables \(Z_p\) with Poisson radii \(p^{-1/2}\), so \(E_\star Z_p^e=p^{-|e|/2}\) for every signed integer \(e\), and \(W_\star=\Re\sum_{{\cal P}_Y}p^{-1/2}Z_p\). With the Dirichlet factors \((mn)^{-1/2}\) included, each corresponding model cross term has weight \(1/\operatorname{lcm}(m,n)\). These weights and all the coefficients in the raw powers are nonnegative. Therefore summing the absolute main-term error costs its \(O_J(bL/\log T)\) multiplier times the corresponding positive Poisson moment. All fixed even moments of \(\sum_p p^{-1/2}Z_p\) are bounded when \(H_Y\) is bounded. For the real and imaginary centered components, independence, the coordinate bound \(2/\sqrt p\), and \(\sum E_\star|p^{-1/2}(Z_p-E_\star Z_p)|^2\le H_Y\) give these bounds by independent moment expansion. The real mean is \(H_Y\). The raw centered powers also have bounded moments. Hence uniformly for \(T\ge Y\) the arithmetic moments differ from the model moments by \(O_{J,M,r_-,r_+}(b+L^{-M})\). Centering by \(H_Y\) is a bounded-coefficient binomial expansion and obeys the same bound.

## Effectivity and strict-tail transfer

For effective comparison, use the full-length bounded coefficient version of the earlier exceptional-prime argument. HLZ §4.4 has a coefficient \(a(kq)\) in the nonprincipal terms, with \(q\) the conductor there. In the small-modulus range there is at most one primitive real conductor requiring exclusion by effective Landau–Page. Avoid one prime divisor of that conductor in all the arrays at the same prefix height. If this prime is outside \({\cal P}_Y\), no change is needed. Since the pad is supported on the divisor closure, it preserves the exclusion. This kills the corresponding coefficient for the exceptional conductor. The remaining small-modulus characters use the effective zero-free rectangle and reciprocal bound. The larger-modulus contribution uses the full-length Proposition 11 with the polylogarithmic split chosen after the log saving, so the effective proof does not need \(Y^{Jb}\) below \(\exp(c\sqrt{\log T})\). This distinction matters for slowly shrinking \(b\). The untwisted normalization has no nonprincipal term and is \(T(\log T)^4/(24\pi)+O^{\rm eff}(T(\log T)^3)\). [Full-length effective cutoff audit](weighted70_hlz_cutoff_review.md) · [Director's exceptional-prime adjudication at the earlier polylogarithmic cutoff](director_effective_scalar_clt_round10.md)

At each \(T\) restore the omitted prime before any tail integration. Its pointwise contribution has size at most \(e^{-aL/2}\), and the difference for the individually centered contribution is at most \(2e^{-aL/2}\). If \(X\) is the retained statistic and \(|d|\le2e^{-aL/2}\), then
\[
 |(X+d)^k-X^k|\le k|d|(|X|+|d|)^{k-1}.
\]
Uniform \(J\)-th even moments for retained arithmetic and model statistics bound the expectations of the right side by \(O_{J,r_-,r_+}(e^{-aL/2})\). This holds regardless of which prime is removed or whether it varies with \(T\). It also restores the fixed full model at every \(T\). Thus for \(B_k(t)=\sum_{0<\gamma\le t}|\zeta'(\rho)|^2(W_Y-H_Y)^k\) and \(A(t)\) the untwisted prefix mass, we get
\[
 B_k(t)=A(t)\left(E_\star[(W_\star-H_Y)^k]
             +O^{\rm eff}(b+L^{-M}+e^{-aL/2})\right)
 \qquad(t\ge Y).
\]
The normalization comparison is against the true untwisted prefix, so no separate \(L^{-1}\) error is incurred from replacing its leading term in the model main term.

On RH the strict positive tail has kernel \(g(t)=(1/4+t^2)^{-1}\), and the numerator equals \(-g(Y)B_k(Y)+\int_Y^\infty(-g'(t))B_k(t)\,dt\). The inclusive endpoint in \(B_k(Y)\) is essential. The term at infinity vanishes by the prefix bound. The same linear functional on \(A\) is asymptotic to \(Y^{-1}L^4/(24\pi)\) effectively, while the sum of absolute endpoint and integral masses is \(O^{\rm eff}(Y^{-1}L^4)\). For example rescale \(t=Yu\), use \(-g'(t)\sim2t^{-3}\) and bound the log factors by the integrable weight \(u^{-2}(1+\log u)^4\). The untwisted error \(O(t(\log t)^3)\) after normalization is \(O(L^{-1})\) and gives an effective lower bound for the denominator. Hence the same uniform model comparison transfers to the strict tail. Since cosines and derivative-square weights are even, adding the negative ordinates changes neither normalized law nor moments. Multiplicities pose no extra assumption, as multiple zeros have zero weight.

## Model, limiting variance and moments

Mertens' reciprocal-prime estimate with effective \(O(1/\log x)\) remainder gives
\[
 H_Y=\log(b/a)+O^{\rm eff}(1/(aL)).
\]
For this elementary error one may use \(\sum_{n\le x}\Lambda(n)/n=\log x+O(1)\), proved using the factorial convolution \(\log n!=\sum_{d\le n}\Lambda(d)\lfloor n/d\rfloor\) and the effective Chebyshev bound. Removing higher prime powers gives \(\sum_{p\le x}\log(p)/p=\log x+O(1)\). Partial summation divides by \(\log p\), yielding a constant plus \(O(1/\log x)\); the constant cancels across the band. Thus the harmonic mass is bounded on the claimed ratio range. The model has mean \(H_Y\) and exact variance
\[
 V_Y=\frac12\sum_{p\in{\cal P}_Y}(p^{-1}-p^{-2})
     =\frac12\log(1/r)
       +O^{\rm eff}_{r_-,r_+}\left((aL)^{-1}+\left|a/b-r\right|+e^{-aL}\right).
\]
Each centered real coordinate has magnitude at most \(2e^{-aL/2}\). Its \(k\)-th cumulant in absolute value for fixed \(k\ge3\) is bounded by \(C_k(2e^{-aL/2})^{k-2}\) times its second moment. This follows by the finite moment–cumulant formula, using \(E|X|^i\le\|X\|_\infty^{i-2}EX^2\) for \(i\ge2\) and \(EX=0\). Cumulants add under independence, and the variances sum to \(V_Y=O(1)\). The moment–cumulant formula then gives discrepancy \(O^{\rm eff}_{j,r_-,r_+}(e^{-aL/2})\) from the moments of \(N(0,V_Y)\). The latter moments have bounded derivatives in \(V_Y\) on this bounded variance range. Combining this with the strict-tail comparison proves (1) for centering by \(H_Y\). The first-moment comparison gives \(E_YW_Y=H_Y+O^{\rm eff}(b+L^{-M}+e^{-aL/2})\). Binomially shifting to this actual mean costs the same order because all required moments are bounded. The resulting second moment gives scalar tightness, and the limiting Gaussian law is moment determinate. All fixed moments converge, including each even absolute moment. Each other finite absolute moment converges by weak convergence and uniform integrability from a larger even moment.

## Computability and comparison with fixed bands

For effectively specified \(r\) and effective moduli for \(b\to0\), \(a/b\to r\), and \(aL\to\infty\), (1) supplies an in-principle computable conditional height for any fixed list of moments and error tolerance. Pointwise computability of band endpoints does not give such moduli. There is no universal numerical rate in \(Y\) alone, as each of the three band conditions permits arbitrarily slow approach. The bound is in the observed parameters, and its constants stem from the effective HLZ repair described above.

There is also a finite-distribution tolerance procedure. Here are quantitative details, since qualitative moment determinacy alone does not supply effectivity. Write \(X=W_Y-E_YW_Y\), \(G\sim N(0,\sigma^2)\) with \(\sigma^2=\frac12\log(1/r)>0\), and add independent \(N(0,\tau^2)\) noise. The Kolmogorov distance between the smoothed laws is bounded by
\[
 \frac1\pi\int_0^\infty|\phi_X(t)-\phi_G(t)|e^{-\tau^2t^2/2}\,\frac{dt}{t}.
\]
This is Fourier inversion of the difference of the CDFs, with absolute convergence at zero from the finite first moments and at infinity from the smoothing. Beyond a cutoff \(R\) the bound is at most \(2e^{-\tau^2R^2/2}/(\pi\tau^2 R^2)\). Through \(R\), the Taylor polynomial of degree \(2m-1\) bounds the integral by
\[
 \frac1\pi\sum_{k=1}^{2m-1}
  |EX^k-EG^k|\,\frac{R^k}{k\,k!}
   +\frac{(E|X|^{2m}+EG^{2m})R^{2m}}{\pi(2m)(2m)!}.
\]
For \(m\) fixed the last expectation is eventually at most \(2EG^{2m}\) for \(X\), effectively by (1). The Gaussian moments \((2m)!\sigma^{2m}/(2^m m!)\) make the Taylor remainder arbitrarily small at fixed \(R\) by choosing \(m\). Removing smoothing costs at most \(2P(|N(0,\tau^2)|>h)+2h/(\sigma\sqrt{2\pi})\), by two CDF comparisons across intervals of width \(h\). Choose \(h,\tau,R,m\) in that order for a given tolerance, then use finitely many instances of (1) with effective band moduli. This proves effectivity in principle for the scalar Kolmogorov distance, without a practical onset height.

For fixed \(0<a<b<1/6\), the arithmetic band is different. Its order-one log-frequency correction to the raw Poisson kernel survives and the limiting centered third moment is strictly negative, with fourth uniform integrability. In the shrinking regime the same aggregate correction is bounded by \(O_j(b)\) and vanishes at every fixed order, while the reciprocal prime mass stays positive because \(a/b\to r\). One cannot justify the new limit by substituting moving endpoints into the fixed-band result. The uniform aggregate estimate and infinitesimal model coordinates supply that proof independently. No publication priority or canonical change is claimed. [Fixed-band non-Gaussian audit](analytic76_hlz_third_skeptic.md)
