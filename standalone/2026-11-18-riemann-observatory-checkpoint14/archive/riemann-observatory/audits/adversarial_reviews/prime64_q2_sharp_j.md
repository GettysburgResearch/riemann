# A direct sharp-cutoff bound for the fixed \(Q_2\) continuous term

This note proves the sharp-interval input used by the conditional power-saving error in [the fixed \(Q_2\) polynomial](prime64_q2_full_polynomial.md). It bypasses the passage from a smoothed long-polynomial theorem to an unweighted integral. The proof is unconditional for this continuous term, and its implied constants are independent of the shifts on the contours described below. It does not supply numerical values for all constants.

Let \(T\) be large, \(L_T=\log T\), \(|a|=c/L_T\), \(|b|=2c/L_T\) for a sufficiently small fixed absolute \(c>0\), and \(d=a+b\). Thus \(|d|\ge c/L_T\). Fix relatively prime positive integers \(h,k\) in \(\{1,2\}\). Write \(\ell(t)=\log(t/(2\pi))\). Then
\[
\begin{aligned}
 &\int_1^T \ell(t)\left(\frac{k}{h}\right)^{it}
      \zeta(\tfrac12+a+it)\zeta(\tfrac12+b-it)\,dt\\
 &=\frac{1}{\sqrt{hk}}\int_0^T \ell(t)
   \left[
       k^{-a}h^{-b}\zeta(1+d)
     + h^a k^b(t/(2\pi))^{-d}\zeta(1-d)
   \right]dt
   +O\!\left(T^{3/4}(1+L_T)^4\right).
\end{aligned}                                                    \tag{1}
\]
The result applies one pair at a time, so the complex conjugation conventions are inherited by direct expansion. For \(Q_2\), the additional factors from \(Q_2(1/2+it)Q_2(1/2-it)\) give the weights \(a(gh)a(gk)/(ghk)\) of HLZ equation (5). The \(O(1/t)\) correction in the log derivative of the functional equation in HLZ p. 1607 is separately \(O_\varepsilon(T^{1/2+\varepsilon})\) by classical convexity near the critical line. Alternatively the previously explicit \(t^{7/16}\) strip bound makes this correction \(O(T^{7/8})\), enough for the \(7/8+\varepsilon\) profile. [Primary AFE representation, Pratt–Robles equations (2.1)–(2.4)](../../sources/finite_moment63_uniform/pratt_robles_1706.04593v3.pdf) · [Independent sparse-continuous estimate](uniform64_exceptional_prime_clt_skeptic.md)

## Fixed-shift product AFE and uniform Mellin weights

Set \(s_1=1/2+a+it,\ s_2=1/2+b-it\) and
\[
 G_d(w)=e^{w^2}(1-4w^2/d^2),\qquad
 g(w,t)=\pi^{-w}\frac{\Gamma((s_1+w)/2)\Gamma((s_2+w)/2)}
                         {\Gamma(s_1/2)\Gamma(s_2/2)} .
\]
The product AFE has a first sum with coefficients
\(m^{-1/2-a}n^{-1/2-b}(n/m)^{it}\) and weight
\[
 V_{a,b}(y,t)=\frac1{2\pi i}\int_{(2)}
                          G_d(w)g(w,t)y^{-w}\frac{dw}{w}.
\]
The dual sum has the replacements \((a,b)\rightsquigarrow(-b,-a)\) and prefactor
\(\chi(s_1)\chi(s_2)=:X_{a,b}(t)\). In particular the positive-\(t\) argument has shift \(-b\) in the dual. These formulas follow by integrating the two completed zeta factors at \(s_1+w,s_2+w\) against \(G_d(w)/w\), shifting from \(2\) to \(-2\), and applying the functional equation in the second integral. The pole at \(w=0\) has the original product as its residue. Four other poles can occur at \(w=1-s_i,-s_i\), from the simple poles of \(\pi^{-s/2}\Gamma(s/2)\zeta(s)\). For \(t\ge1\) these locations are separated for small \(a,b\). The Gaussian at those points is \(O(e^{-t^2+O(t)})\). The other completed zeta factor has imaginary part of size \(2t\), away from its poles, and is bounded by a polynomial times its gamma decay. Thus their total after the gamma normalization is \(O_A((1+L_T)^2(1+t)^{-A})\) for any fixed \(A\). This contour also fixes the sign \((n/m)^{it}\) directly from Dirichlet expansion.

Here are the uniform bounds needed for the integral. On a block \(t\in[X,2X]\), \(X\ge1\), and for each fixed \(A\ge2\),
\[
 |V_{a,b}(y,t)|+t|\partial_tV_{a,b}(y,t)|
   \ll_A (1+L_T)^2\min\{1,(X/y)^A\}.                              \tag{2}
\]
The bound holds also for the dual weight including its prefactor. On \(\Re w\in\{-1/4,2,A\}\), the gamma arguments in \(g\) have real parts in a fixed compact positive interval. For \(|\Im w|\le t/2\), Stirling with remainder gives \(|g|\ll_A t^{\Re w}\). The exponential factors from the positive and negative height arguments cancel. The difference of digamma values under translation by \(w/2\) is \(O_A(|w|/t)\) by integrating the trigamma series bound \(O(1/t)\) in this range; hence \(t|\partial_tg|\ll_A t^{\Re w}(1+|w|)\). For \(|\Im w|>t/2\), the two numerator imaginary absolute values have sum at least the corresponding denominator sum, since the latter two imaginary arguments have opposite signs. Gamma bounds in the fixed real strip now give at most polynomial growth after cancellation of those exponential factors. The factor \(\exp(-(\Im w)^2)\) controls that part and its differentiated integral. All these estimates can use the positive-real-part Stirling remainder and the absolutely convergent digamma differences, as in the [explicit dyadic Hardy bound](prime64_sharper_moments.md). The polynomial factor \(1-4w^2/d^2\) costs \(O((1+L_T)^2(1+|w|)^2)\). Shifting to \(\Re w=A\) proves the large-\(y\) bound. Shifting to \(-1/4\) gives the residue 1 and a bounded remainder when \(y\le X\). The derivative of the residue is zero. This proves (2).

For the dual multiplier, Stirling gives \(X_{a,b}(t)=(t/(2\pi))^{-d}(1+O(1/t))\). The first derivative estimate follows directly from pairing the same-sign imaginary gamma arguments in its log derivative. Each pair differs by \(O(d)\), so trigamma control gives \(t|\partial_t X_{a,b}(t)|\ll1\), and \(|X_{a,b}(t)|\ll1\) for \(t\le T\). Thus (2) applies to the whole dual multiplier. The same fixed-strip arguments also give values and derivatives at bounded \(t\), with enlarged constants.

## Off diagonal and diagonal on sharp blocks

Integrate on a full or partial block \([X,2X]\subset[1,2T]\) with endpoints in \([1,T]\). The phase is \((kn/(hm))^{it}\). For \(kn\ne hm\), one integration by parts and (2) give an absolute bound
\[
 \frac{O_A((1+L_T)^3)\min\{1,(X/(mn))^A\}}
      {|\log(kn/(hm))|}.
\]
The extra logarithm comes from \(\ell(t)\); the integral of its product rule derivative is controlled by the same factor over a block. The small shifts multiply the coefficient \((mn)^{-1/2}\) by at most a constant for \(mn\le X\) and by \(O((mn/X)^{1/8})\) otherwise, for sufficiently large \(T\).

To sum the displayed bound, for a general \(P\ge1\) first remove the Mellin decay and sum over \(mn\le P\). If \(kn/(hm)\notin[1/2,2]\), the inverse logarithm is bounded and
\(\sum_{mn\le P}(mn)^{-1/2}\le2\sqrt P(1+\log P)\). For comparable \(kn,hm\), the inverse logarithm times \((mn)^{-1/2}\) is \(O_{h,k}(1/|kn-hm|)\). There are \(O_{h,k}(\sqrt P)\) possible values of \(m\); for each fixed \(m\), the distinct nonzero signed integer gaps give a harmonic sum \(O_{h,k}(1+\log P)\). Split \(mn>X\) into dyadic product segments and take \(A=3\), so the decay dominates both the shift power and the square-root growth. The full off-diagonal contribution on a block is \(O(\sqrt X(1+L_T)^4)\), with no smoothing of its time endpoints.

The diagonal is \(m=k u,\ n=h u\) for positive integer \(u\). Its first AFE part becomes \((hk)^{-1/2}k^{-a}h^{-b}\) times
\[
 \frac1{2\pi i}\int_{(2)}
   G_d(w)g(w,t)(hk)^{-w}\zeta(1+d+2w)\frac{dw}{w}.
\]
Move to \(\Re w=-1/4\). The pole at \(-d/2\) is removed by \(G_d\), and gamma arguments stay in the positive half plane. The residue at zero is \(\zeta(1+d)\). The remaining integral is \(O(X^{-1/4}(1+L_T)^2)\) by the gamma estimates just proved and ordinary Euler summation for \(\zeta\) in a fixed strip about real part \(1/2\), away from its pole. The dual gives the same estimate with \(d\) replaced by \(-d\). Its main term can use the simpler multiplier \((t/(2\pi))^{-d}\) at additional integrated cost \(O((1+L_T)^3)\), using the \(O(1/t)\) relative bound and \(\zeta(1-d)=O(L_T)\).

After multiplication by \(\ell(t)\) the diagonal integrated remainder is \(O(X^{3/4}(1+L_T)^3)\) on a block. The AFE residuals have integrable bounds. Summing the geometric height blocks gives the error in (1). The main expression extending from \(t=1\) down to \(t=0\) changes the result by \(O(1+L_T)\) because the small powers of \(t\) against \(\ell(t)\) are integrable. This proves (1). It supplies the required sharp \(J\) power saving on the two Cauchy circles without importing uniform cutoff constants from a smoothed moment theorem.
