# Partial estimates for the single Mangoldt remainder

This note concerns the compact-local signed remainder in the [fixed-sequence reduction](weighted98_fixed_sequence_review.md), with \(T\asymp Y\), \(y=Y^\theta\), \(1/2<\theta=4b<2/3\), \(H=T^\kappa\) and \(\delta=H/T\). The contribution sharing a band prime with the modulus can be removed. With \(\kappa\) chosen sufficiently close to one, proper prime powers of exponent at least three can also be removed. The remaining prime terms and a middle square-prime range require an additional estimate.

## Exact fixed-factor conductor and dual length

Write \(\ell=p^j\), \(g=(k,\ell)\), \(q=k/g\), and \(M=kT/\ell\). On expanding \(d_2*(\Lambda\log^2)\), the inner divisor variable \(n=m/\ell\) has weight
\[
 F_{k,\ell}(x)=w_T(2\pi\ell x/k),
 \qquad x\asymp M.
\]
The principal subtraction for \(m=\ell n\) is the average of \(e(-a\ell n/k)\) over units \(a\bmod k\). Reduction maps these units onto units modulo \(q\) with equal fibers, and \(\ell/g\) is a unit modulo \(q\). Thus it is exactly the average of \(e(-a'n/q)\) over units \(a'\bmod q\), while the original numerator is \(a'=\ell/g\). In particular \(q=1\) gives zero identically. The divisor variable \(n\) is unrestricted by coprimality. If the fixed positive compact support has upper bound \(C M\) and \(CM<1\), the original inner sum is empty. Otherwise \(M\ge1/C\), the uniform lower bound used below.

For \(a'\) a unit, use the Estermann series \(Z_q(s,a')=\sum_{n\ge1}d_2(n)e(-a'n/q)n^{-s}\). From the finite Hurwitz expression in the previous review, its polar principal part is independent of \(a'\). On \(\Re s<0\), expanding the two exact Hurwitz cosines into exponentials and completing the finite sum gives
\[
 Z_q(s,a')=2(2\pi)^{2s-2}q^{1-2s}\Gamma(1-s)^2
 \sum_{h\ge1}d_2(h)h^{s-1}
 \bigl[\cos(\pi(1-s))e(\overline{a'}h/q)
                     +e(-\overline{a'}h/q)\bigr].
\]
Indeed the finite phase with the two cosine signs \(\epsilon,\epsilon'\) is \(-a'rv-\epsilon n r-\epsilon' m v\) modulo \(q\). The \(r\)-sum forces \(v=-\epsilon n\overline{a'}\), leaving \(+\epsilon\epsilon' nm\overline{a'}\) and the factor \(q\). Equal signs give the cosine, and opposite signs give the constant term. The real logarithmic weight \(\Lambda(\ell)(\log\ell)^2\) remains entirely outside this transform. [Hurwitz equation](https://dlmf.nist.gov/25.11.E9) · [Mellin and pole details](weighted98_fixed_sequence_review.md)

After subtracting the unit average, each dual phase is replaced by
\[
 e(\pm\overline{\ell/g}\,h/q)-
 \frac{\mu(q/(h,q))}{\varphi(q/(h,q))},
\]
with the sign paired with its own transform. The inversion permutation of units justifies this average independently for either sign. The target now correlates the prime-power factor with an inverse phase and with a kernel whose scale depends on that factor. There is also a nontrivial principal subtraction for noncoprime dual indices.

On the line \(\Re s=-B\) for any fixed real \(B>0\), the smoothed test satisfies \(\widetilde F_{k,\ell}(-B+it)\ll_{B,j} M^{-B}(1+\delta|t|)^{-j}\). In the dual formula the product of gamma and cosine factors costs at most \(O_B((1+|t|)^{1+2B})\) on this line by Stirling. Thus the absolute dual contribution of indices \(h>N\) is at most
\[
 \ll_B q\delta^{-2}\,U^B
          \sum_{h>N}\frac{d_2(h)}{h^{1+B}},
 \qquad U=\frac{q^2}{M\delta^2}
         =\frac{q^2\ell T}{kH^2}.
\]
If \(U\ge1\), taking \(N\ge U T^\varepsilon\) leaves a rapidly decaying dual tail, by choosing \(B\) large. The same holds with \(N\ge \max(1,U)T^\varepsilon\) for all \(U\). If \(U\le T^{-\varepsilon}\), taking the whole dual sum makes it rapidly decaying. This is the precise smooth transition criterion
\[
 \frac{\ell}{g^2}\le \frac{H^2}{kT}\,T^{-\varepsilon}.
\]
The strict power margin is needed. The inverse-numerator signs are derived here without a Bessel normalization convention. In the Bessel version the reciprocal transition scale is \(\delta\sqrt{hM}/q\). The corresponding dual resolution is the same \(U\).

## Absolute estimates that remove some strata

Let \(R_{k,\ell}\) be the signed divisor sum just transformed. The entire dual sum on \(-B\), and also a trivial divisor sum on \(x\asymp M\), give
\[
 |R_{k,\ell}|\ll_B
   \min\left(q\delta^{-2}\left(\frac{q^2}{M\delta^2}\right)^B,\
             M\log(2+M)\right),\qquad M\ge 1/C.
\]
The latter estimate holds down to \(M=1/C\) with a support-dependent constant, by the elementary divisor hyperbola or the bound \(\sum_{n\le CM}d_2(n)\ll CM\log(2+CM)\). No small-\(M\) error is inserted when the sum is empty. Since \(q\le y\), choose \(\kappa<1\) arbitrarily close to one and then \(B>0\) arbitrarily small. For any prescribed small \(\eta>0\) the first estimate is \(O_\eta(qT^\eta)\) with those choices, uniformly over nonempty supports. Explicitly it is enough to choose \(2(1-\kappa)+B(2\theta+2(1-\kappa))<\eta\). This weak pointwise estimate with arbitrarily small exponent is a choice of \(\kappa\) and \(B\), rather than a statement for every \(\kappa>(1+\theta)/2\). The rapid small-\(U\) estimate above holds throughout the latter range when its power-margin condition is met.

**Common prime factors.** If \(p\mid k\) and \(\ell=p^j\), then \(q/k\le1/p\), and \(p>Y^a\). There are \(O_{a,b}(1)\) possible \(j\) for each such \(p\) since \(\ell\ll kT\). Each supported \(k\) has at most four distinct prime factors. Thus summing the fixed-factor estimate against \(c_k/k\) and absorbing \(\Lambda(\ell)(\log\ell)^2\ll(\log T)^3\) gives \(O(T^{\theta-a+\eta}\log^3T)\). This is power saving for a sufficiently small choice of \(\eta\). It removes the complete common-factor stratum, also when \(j>2v_p(k)\), for which the small-\(U\) criterion need not apply.

**Prime powers \(j\ge3\).** For \(\ell\le T\), use \(O(kT^\eta)\) and count the distinct pairs \(p,j\) with \(p^j\le T,\ j\ge3\) by \(O(T^{1/3}\log(2T))\). For \(\ell>T\), use \(O(kT\log T/\ell)\). Dyadic counting gives
\[
 \sum_{p^j>T,\ j\ge3}(p^j)^{-1}
 \ll T^{-2/3}\log(2T).
\]
For example the contribution at \(p^j\in(X,2X]\) is \(O(X^{-2/3}\log(2X))\), summable geometrically. Thus the large-\(\ell\) tail is bounded even after extending it beyond the original \(\ell\ll kT\) support. The full \(j\ge3\) sum, including the outer coefficients and log weights, is \(O(y\,T^{1/3+\eta}\log^C T)=o(T)\) with \(\eta<2/3-\theta\) and a fixed power margin. Primality is unnecessary for these counting bounds.

**Some squares.** On a dyadic modulus block \(k\asymp K\), the same pointwise bound disposes of \(p^2\) with \(p\le T^{1-\upsilon}/K\), by counting the primes absolutely and choosing \(\eta<\upsilon\). Indeed the block contribution is \(O(KT^\eta\cdot T^{1-\upsilon}/K)\) up to logs. The trivial \(M\log(2+M)\) bound disposes of squares with \(p\ge KT^\upsilon\), from the reciprocal bound \(\sum_{p>X}p^{-2}\ll X^{-1}\). These estimates leave a nonempty middle range when \(K\asymp T^\theta\) above \(\sqrt T\). Applying the cube argument at \(j=2\) would instead give \(O(y\,T^{1/2+\eta}\log^C T)\).

## Surviving analytic problem

Away from the common-factor stratum, \(q=k\) and the cutoff is \(U=k\ell T/H^2\). Even for \(\kappa\) close to one, primes \(\ell\) above about \(H^2/(kT)\) have genuine dual terms. The dual length grows with \(\ell\). Uniform absolute estimates for the divisor transform do not exploit the inverse prime numerator. For the large prime portion, swapping the sums and treating primes in residue classes also incurs a conductor loss: taking the worst residue-class error and summing the unit Fourier vector costs up to \(k\). Even an average bound for the squared errors on their natural variance scale \(XK\) over moduli \(k\asymp K\) and prime height \(X\asymp KT\) would, after the two Cauchy–Schwarz steps grouping all residue classes and moduli, give only \(O(\sqrt{XK})=O(K\sqrt T)\) up to logs with the outer \(c_k/k\) weights. This already exceeds \(T\) for \(K\asymp T^\theta\), and is a loss in that argument rather than a lower bound for the signed sum. Equivalently, on the contribution \(n=1\) of the original divisor variable, term-by-term square-root estimates for primitive character twists at length \(kT\), followed by absolute summation of the Gauss weights and all \(k\), have the same power obstruction. General square-root character estimates of that type would themselves be extra input beyond RH for the Riemann zeta function.

The precise unfinished estimate needs cancellation for the signed inverse-numerator sums over the remaining primes or middle squares, including the dependence of the smooth dual transforms on \(\ell\) and \(k\), or an estimate that combines those parts without taking these absolute values. The elementary bounds give no matching counterexample and no proof of the fourth moment. No canonical file was changed.

## Cross-check of the independent Poisson argument

The [prime review](prime101_coprime_prime_strata.md) reaches the same small-factor criterion without using the Hurwitz functional equation. Its smooth hyperbola may be implemented using a fixed smooth \(\varphi(v)\) for \(v>0\), equal to one near zero and zero for \(v\) large, with \(\varphi(v)+\varphi(1/v)=1\). Symmetry makes the \(d_2\) sum twice the half with factor \(\varphi(d/e)\). For a fixed \(d\ll\sqrt M\), the rescaled function in \(e\asymp M/d\) has derivative scale \(L_d=M\delta/d\). Derivatives of the partition are on the natural larger scale \(M/d\), so they preserve the stated bound. Extend the function by zero on the negative real axis and apply Poisson.

If \(q\mid d\), its Poisson or original contribution cancels identically in the unit average. Otherwise, for each unit \(v\bmod q\), the nearest frequency \(\lambda\in\mathbb Z-vd/q\) has \(|\lambda|\ge(q,d)/q\). In the large-decay regime \(L_d\gg1\), all other frequencies have a summable tail bounded by \(O_B(L_d^{-B})\) up to the at most one additional tied nearest term. In fact
\[
  L_d\frac{(q,d)}q
   =\frac{H g(q,d)}{\ell d}
   =\frac{H(k,\ell d)}{\ell d}
   \gg \frac{Hg}{\sqrt{kT\ell}} = U^{-1/2}.
\]
The equality uses \((q,\ell/g)=1\). When \(U^{-1/2}\) is bounded, the trivial divisor sum supplies the claimed uniform bound after adjusting its constant. Harmonic summation over \(d\) gives \(O_B(M\log(2+M)(1+U^{-1/2})^{-B})\). Thus the independent proof correctly retains both the original gcd in the short-factor criterion and the further gcd \((q,d)\) in the intermediate estimate. Its arbitrary power saving with a strict margin works for every fixed \(\kappa>(1+\theta)/2\). The all-shared-factor and cubic-power elimination use the separate pointwise argument above with \(\kappa\) freely chosen close to one.
