# Power savings for prime squares and a local band of inverse-prime twists

Let \(k\) have the coefficients \(c_k\) of the fourth band polynomial, so \(0\le c_k\le24\) and \(k\le Y^\theta\), with \(\theta=4b\in(1/2,2/3)\). Put \(T\asymp Y\), \(H=T^\kappa\), and \(\delta=H/T\). The smooth signed remainder for \(d_2*(\Lambda\log^2)\) uses the taper \(w_T(2\pi m/k)\) and the difference of \(e(-m/k)\) from its average over unit numerators. Choose a standard taper with two monotone transitions and \(\kappa<1\) sufficiently close to one. There are two partial unconditional cancellation results for the arithmetic remainder. For \(1/2<\theta<9/17\), the entire prime-square contribution saves a power. For \(1/2<\theta<10/17\) and \(k\asymp Y^\theta\), one genuine-prime subrange near \(T^{1-\theta}\) also saves a power. The longer prime portion still needs an estimate. [Strata and dual transform](weighted101_single_mangoldt_strata.md) · [Fixed-sequence reduction](weighted98_fixed_sequence_review.md)

## Ghosh's bound and the entire square-prime stratum

I rendered p. 4, PDF page 12, of Amit Ghosh's 1981 Nottingham thesis, *Topics in prime number theory*. Chapter 1, Theorem 2 gives, for \((a,q)=1\), \(|\alpha-a/q|<q^{-2}\), and any positive integer \(N\),
\[
 \left|\sum_{n\le N}\Lambda(n)e(\alpha n^2)\right|
 \ll_\epsilon N^{1+\epsilon}
       (q^{-1}+N^{-1/2}+qN^{-2})^{1/4}.
\]
The theorem inherits the approximation hypotheses of Theorem 1, with positive integers \(a,q\) and real \(\alpha\). For the exact rational phases below, choose the representative \(1\le a<q\) and \(\alpha=a/q\), so the approximation error is zero. The theorem has no further restriction relating \(q\) and \(N\). Ren restates the formula in (1.4). The journal version is a separate publication of this result. [Ghosh thesis, primary scan p. 4](https://repository.nottingham.ac.uk/bitstreams/8f8d2034-326a-4974-9c1f-e5b488b1fa4e/download#page=12) · [Ghosh journal](https://doi.org/10.1112/plms/s3-42.2.252) · [Ren author preprint](https://www.math.hku.hk/imrwww/IMRPreprintSeries/2004/IMR2004-9.pdf)

Use dyadic \(k\asymp K\) and square bases \(p\asymp X\). Swap the divisor variable \(n\) and the prime \(p\), so \(n\ll KT/X^2\). For fixed \(k,n\) put \(g=(k,n)\) and \(q=k/g\). If \(q=1\), the phase and its average agree exactly. Otherwise every unit numerator over \(k\) gives a reduced exact rational with denominator \(q\), since \((n/g,q)=1\). The reduction of units is surjective with equal fibers, so the average obeys the same uniform Ghosh estimate. No condition \(n\le k\) is used.

Use differences of the Ghosh prefix estimate at endpoints of intervals inside \([X,2X]\). Removing the terms with base variable a proper prime power costs \(O(X^{1/2}(\log T)^C)\), absorbed by \(X^{7/8+\epsilon}\). Excluding primes dividing \(k\) costs at most four terms, also absorbed. The actual weight from \(\ell=p^2\) is \(\Lambda(p^2)(\log(p^2))^2=4\log^3p\). The prime \(\log p\) is already provided by the estimate, and partial summation inserts the remaining log square and the taper. The composition \(w_T(2\pi np^2/k)\) has bounded total variation in \(p\) because its argument is monotone and the taper has two monotone transitions. Restricting to a dyadic subinterval, including an end slice of a cutoff, adds only bounded endpoint terms. Thus the fixed-\(k,n\) bound is, after absorbing fixed logs,
\[
 \ll T^\epsilon X\bigl(q^{-1/4}+X^{-1/8}
                              +q^{1/4}X^{-1/2}\bigr).
\]

Since \(\sum_{n\le CKT/X^2,\ g\mid n} d_2(n)\ll T^\epsilon KT/(gX^2)\) for every contributing \(g\), gcd summation absorbs the factor \(g^{1/4}\) in \(q^{-1/4}\). It also absorbs \(1\) in the conductor-independent term and \(g^{-1/4}\) from \(q^{1/4}\). Each divisor sum in \(g\mid k\) is \(O(T^\epsilon)\). Summing \(c_k/k\) over one dyadic block costs \(O(1)\), so the resulting block bound is
\[
 \ll T^\epsilon \frac{KT}{X}\left(K^{-1/4}
                                      +X^{-1/8}
                                      +K^{1/4}X^{-1/2}\right).
\]
For \(X\le T^{1-\nu}/K\), use the previous pointwise divisor estimate \(O(kT^\eta)\) and count the prime bases absolutely. It yields \(O(T^{1-\nu+\eta}\log^C T)\) on each modulus block, with \(\eta<\nu\) by choosing \(\kappa\) near one. For larger \(X\), the three braces after multiplication by \(KT/X\) decrease with \(X\), so the bounds at the threshold are
\[
 K^{7/4}T^\nu,\qquad
 K^{17/8}T^{-1/8+9\nu/8},\qquad
 K^{11/4}T^{-1/2+3\nu/2}.
\]
For \(K\le Y^\theta\) the limiting restrictions on \(\theta\), as \(\nu\downarrow0\), are \(4/7,\ 9/17,\ 6/11\), respectively. Thus \(1/2<\theta<9/17\) permits fixed sufficiently small positive \(\nu,\eta,\epsilon\), and the dyadic totals save a power. Equivalently the arithmetic range for eliminating squares is \(1/8<b<9/68\). This conclusion concerns the squared prime factor in the Mangoldt convolution, including the previously unresolved middle squares.

## A local band of genuine primes via Korolev

Korolev's published homogeneous prime-inverse theorem applies to any modulus \(q\ge q_0(\epsilon)\), unit numerator \(h\), and \(q^{7/10+\epsilon}\le X\le q\). Its prefix over integers coprime to \(q\), weighted by \(\Lambda\) against \(e(h\bar n/q)\), is bounded by \(X^{32/37}q^{7/74+\epsilon}\). This is the theorem of the 2018 *Sbornik: Mathematics* paper, distinct from the later arXiv:1911.09981 Theorem 1, where both the inverse and linear coefficients must be units. The latter theorem does not permit a zero linear coefficient. Neither theorem directly handles inverse squares. [Korolev's 2018 primary paper, theorem](https://www.mathnet.ru/links/773516eb2c3834048a042453ddd33e9a/sm8939_eng.pdf) · [Later inhomogeneous theorem](https://arxiv.org/pdf/1911.09981)

Fix \(1/2<\theta<10/17\) and \(k\asymp K\asymp Y^\theta\). Take a dyadic prime interval of scale \(X\) with
\[
 T^{1-\theta-\xi}\le X\le T^{1-\theta+\xi},
\]
where \(\xi>0\) is sufficiently small in terms of \(a,\theta\). The shared-prime cases have already been removed, so the divisor dual has denominator \(k\). Let \(U_X=kX/(T\delta^2)\). For primes on the block the effective dual length is comparable to \(U_X\). Truncate the dual at \(N=\lceil \max(1,U_X)T^\epsilon\rceil\). The exact Hurwitz transform and large-left-line estimate in the previous review show that the sum over \(h>N\) has arbitrary power saving, even after summing over all original primes and modulus coefficients. Choose \(\kappa\) close to one and \(\xi,\epsilon\) sufficiently small that \(N<Y^a\). Every retained \(h\) is then coprime to \(k\), whose prime divisors exceed \(Y^a\). Thus the prime inverse estimate may be used with the original modulus and unit numerator \(h\), and the dual principal subtraction is simply \(\mu(k)/\varphi(k)\).

For clarity, sum the primes in the exact Mellin expression. On \(\Re s=-B\), the taper \(F_{k,p}(x)=w_T(2\pi px/k)\) satisfies
\[
 \widetilde F_{k,p}(s)=(k/(2\pi p))^s\widetilde w_T(s).
\]
For fixed \(s=-B+it\), inserting \(p^{-s}\) and the extra \(\log^2 p\) in the Korolev sum by partial summation costs \(O_B(X^B(1+|t|)\log^2T)\). All interval endpoints where the theorem is needed lie inside its range by the strict inequalities \(1-\theta>(7/10)\theta\) and \(1-\theta<\theta\), with \(\xi,\epsilon\) small. Removing proper prime powers from Korolev's prefix has a smaller cost \(O(X^{1/2}\log^C T)\). The subtraction \(\mu(k)/\varphi(k)\) is bounded trivially by \(O(X^{1+\epsilon}/\varphi(k))\). The same estimates apply for both inverse signs. Unit averages with \(h\) noncoprime need no estimate here because the retained length excluded them.

By Stirling, with either dual sign the Mellin integrand on \(-B\) costs \(O_B((1+|t|)^{1+2B})\) from its gamma and trigonometric factors. Allowing the extra \(1+|t|\) from prime partial summation changes the integrated taper factor to \(O_B(\delta^{-3-2B})\), with \(w_T\) on support of height \(\asymp T\). Together with \(k^{1+2B}\), \((k/(2\pi))^{-B}\), \(X^B\), \(T^{-B}\), and \(\sum_{h\le N}d_2(h)h^{-1-B}\ll_B1\), this gives the bound for a dyadic prime and modulus block
\[
 \ll T^{O(\epsilon)} K\delta^{-3}U_X^B
       \left(X^{32/37}K^{7/74}+XK^{-1}\right).
\]
The weight \(c_k/k\) again sums to \(O(1)\) on the modulus block. One can use \(B=1\) for the retained dual terms and a sufficiently large fixed \(B\) for the tail. This is justified by contour shift for each dual term on \(\Re s<0\), where its gamma product is holomorphic and the Mellin transform decays rapidly on vertical lines. At \(X=T^{1-\theta}\), with the arbitrarily small transition losses set aside, the exponent in the inverse-prime term is
\[
 \theta+\frac{32}{37}(1-\theta)+\frac7{74}\theta
   =\frac{64+17\theta}{74}<1 .
\]
Since \(U_X\ll T^{\xi+2(1-\kappa)}\), one can choose fixed positive \(\xi,\epsilon,1-\kappa\) small enough to preserve a strict saving throughout the dyadic interval. The principal subtraction has the smaller exponent \(1-\theta\) before the small transition losses. This proves a power saving in the specified genuine-prime band. In particular it reaches beyond the elementary short-factor condition near \(H^2/(kT)\) when \(K\asymp Y^\theta\). Any slice at the ends of this band is handled by the same prime partial summation.

## Where these methods stop

The genuine-prime argument is localized before the dual length encounters modulus factors. At larger \(X\), noncoprime \(h\) force reduced moduli and the simple comparison with Korolev's \(X\le q\) condition fails for some \(h\). Even setting aside gcds and the source's upper endpoint, the pointwise estimate followed by absolute dual summation has the scale \(KX^{32/37}K^{7/74}\) up to taper losses. At \(X\asymp K\) this is \(K^{145/74}\), already too large for \(\theta>74/145\). For much longer primes the absolute character or residue-class argument still loses the factor that gives \(K\sqrt T\) at the divisor argument \(n=1\).

The composite-modulus bilinear Kloosterman and \(q\)-van der Corput estimates identified in the source search concern bilinear forms of *complete* Kloosterman sums or require extra structure on the two factors. The present dual terms are bare inverse-prime phases \(e(\pm h\bar p/k)\) with an \(h,p,k\)-dependent transform. A passage to complete sums introduces completion coefficients and a new length calculation. I have not verified an estimate for that transformed aggregate, so it provides no further saving here. The partial arithmetic bounds above do not finish the fourth moment. No canonical file was changed. [Bilinear forms with Kloosterman sums, prime-modulus formulation](https://annals.math.princeton.edu/wp-content/uploads/annals-v186-n2-p02-p.pdf) · [Composite-modulus non-abelian amplification](https://link.springer.com/article/10.1007/s00039-026-00746-0)
