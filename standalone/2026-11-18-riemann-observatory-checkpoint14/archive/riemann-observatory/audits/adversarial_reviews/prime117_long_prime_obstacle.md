# The prescribed Fourier mode in the long-prime range

18 November 2026. The remaining prime convolution gives an additive twist at a prescribed Fourier mode that changes with each product of four band primes. This note gives a Mellin-separated formulation retaining that product, a sufficient phase-sensitive square estimate, and an explicit barrier to using only maximum progression discrepancies or total progression variance. The latter barrier already occurs at divisor argument 1. No estimate for the full remaining sum is asserted. [Larger inverse-prime regions](prime113_uniform_voronoi_envelope.md)

## A product-preserving target

Open the coefficient \(d_2*(\Lambda\log^2)\) and restrict the coprime von Mangoldt factor to first powers of primes. Write \(h\) for the divisor argument, with \(h\asymp D\), and \(p\asymp P\), \(k\asymp K\), against the previous cutoff at \(hp/k\asymp T\). Thus relevant dyadic blocks satisfy \(DP\asymp KT\). Put
\[
 R_k(h,p)
 = e(-hp/k)- \frac{\mu(k/(h,k))}{\varphi(k/(h,k))},
 \qquad (p,k)=1.
\]
This is the exact unit-centered kernel, with no coprimality assumption on \(h\). For \(g=(h,k)\), the effective modulus is \(k/g\). All pairs with \(k/g=1\) vanish identically. [Unit-average identity](prime98_fixed_arithmetic_sequence.md)

Let \(\alpha_r\) and \(\beta_s\) count ordered products of two band primes each. They can also encode separate dyadic restrictions on the four band-prime variables. They are bounded by 2, and for the unrestricted band \(a_k=\sum_{rs=k}\alpha_r\beta_s\). Let \(W(u)=w_T(Tu)\). Mellin inversion on the zero real line puts the full cutoff back by integrating the following form against \(\widetilde W(it)(2\pi/T)^{-it}\,dt/(2\pi)\):
\[
 \mathcal B_{K,D,P}(t)
 = \sum_{\substack{r,s\\K<rs\le2K}}
       \frac{\alpha_r\beta_s}{(rs)^{1-it}}
   \sum_{h\asymp D}\frac{d_2(h)}{h^{it}}
   \sum_{\substack{P<p\le2P\\(p,rs)=1}}
       \frac{(\log p)^3}{p^{it}}\,R_{rs}(h,p).
\]
The weights remain separate on the two pairs of modulus primes. For \((r,s)=1\) the additive part is exactly
\[
 e(-hp\bar s/r)\,e(-hp\bar r/s),
\]
by the Chinese remainder identity. The product couples the two inverse phases. If the pairs share factors, use \(R_{rs}\) with its actual gcd definition. In particular, grouping the four primes into pairs does not require removing repeated moduli or ignoring the unit subtraction. The endpoint \(K<rs\le2K\) can be kept without declaring arbitrary factorability.

For \(\delta=H/T\), the fixed-support cutoff satisfies \(|\widetilde W(it)|\ll_j (1+\delta|t|)^{-j}\). Given a small \(\epsilon>0\), choose \(\kappa<1\) so close to 1 that \(1-\kappa<\epsilon/2\). Then \(|t|>T^\epsilon\) has arbitrary power saving after integration by taking \(j\) large and using a polynomial triangle bound for the finite sums, and the Mellin \(L^1\) norm is \(O(\delta^{-1})\). Consequently a uniform bound \(|\mathcal B_{K,D,P}(t)|\ll T^{1-\eta}\) on \(|t|\le T^\epsilon\), with \(1-\kappa<\eta\), is sufficient after integration and dyadic summation. This specifies an estimate with the ordered product weights, including their known short factorizations, while preserving the additive phase. Taking absolute values before averaging over the two modulus pairs is not required by this formulation.

One possible, stronger input would be a square bound for the single prescribed Fourier mode of each pair:
\[
 \sum_{k\asymp K}\sum_{h\asymp D}
 \left|\sum_{\substack{p\asymp P\\(p,k)=1}}
    (\log p)^3p^{-it}R_k(h,p)\right|^2
 \ll T^{2-\eta}K/D.
\]
The sum over \(k\) may be limited to the actual band support. Indeed Cauchy–Schwarz in \((k,h)\), using \(a_k\ll1\) and \(d_2(h)\ll_\epsilon T^\epsilon\), has coefficient norm \(O(T^\epsilon\sqrt{D/K})\). This would give the requisite power saving after choosing the transition exponent with \(1-\kappa<\eta/2\) and allowing a small fixed margin for logarithms and divisor weights. The model square size \(KDP\) up to logarithms satisfies the displayed budget with a margin when \(P>K^2 T^c\) for fixed \(c>0\), because \(DP\asymp KT\) and \(KDP/(T^2K/D)\asymp K^2/P\). For shorter \(P\), even this square size need not suffice through Cauchy alone, and the ordered product phase may matter more directly.

## Why progression bounds do not give the prescribed mode

Consider the single \(h=1\) block with \(P\asymp KT\), \(K=T^\theta\) and \(\theta>1/2\). At a common prime endpoint, write \(E_{k,a}\) for the error of the prime mass in residue class \(a\) from the mean over units. The real signed sum is
\[
 \sum_{k\asymp K}\frac{a_k}{k}
       \sum_{a\bmod k}^{*}\cos(2\pi a/k)E_{k,a}.
\]
Here the mean cancels exactly. The following example is a statement about what follows from norms on progression errors, with no assertion about the behavior of actual primes.

Choose squarefree supported moduli \(\mathscr S\) in a single block near the top modulus scale, with \(S=|\mathscr S|\asymp K/\log^4T\). Such a set follows from choosing four distinct primes in a fixed multiplicative subinterval near the upper band edge, the prime number theorem, and partitioning the resulting moduli into finitely many comparable dyadic blocks. On this set \(a_k=24\). Define an array with zero mean across units by
\[
 E_{k,a}=\sqrt{P/S}\,
        \left(\cos(2\pi a/k)-\frac{\mu(k)}{\varphi(k)}\right)
\]
for \(k\in\mathscr S\), zero elsewhere. Each modulus is odd and has prime factors tending to infinity. Denote the parenthesized vector by \(r_k(a)\). Its mean is zero by the unit Ramanujan identity, and
\[
 \sum_{a\bmod k}^{*} r_k(a)^2
 =\frac{\varphi(k)+\mu(k)}{2}-\frac{\mu(k)^2}{\varphi(k)}
 \asymp k,
\]
using \((2,k)=1\) and \(\varphi(k)\asymp k\). Its sup norm is bounded by 2.

The array obeys \(\sum_k\max_a |E_{k,a}|\ll\sqrt{PS}\), which is \(O_A(P/\log^A T)\) for every fixed \(A\). It also satisfies the ideal-strength variance budget \(\sum_{k,a}|E_{k,a}|^2\ll PK\). Adding the mean \(P/\varphi(k)\) gives positive residue masses for large \(T\), since \(K\sqrt{P/S}/P\ll T^{-1/2}\log^2T\). But the real signed functional above equals a positive quantity of order
\[
 \sqrt{PS}\asymp K\sqrt T/\log^2T,
\]
well above \(T\log^4T\) at every fixed \(\theta>1/2\). Thus even the hypothetical simultaneous availability of maximum-error logarithmic savings and the ideal total variance would not, as abstract estimates, supply the required opposite phase correlation or force a small prescribed Fourier mode. The example is compatible with the exact unit-centering and with positivity of the underlying residue masses.

The ordinary additive large sieve likewise gives only the larger norm budget on this block. The fractions \(1/k\) for \(k\asymp K\) are separated by \(\gg K^{-2}\). Applying the large sieve to the prime polynomial of length \(P\) bounds the uncentered square sum by \(O((P+K^2)P\log^{O(1)}T)\). Excluding \(p\mid k\) changes each summand by at most four prime terms on the band support. The Ramanujan mean can be retained separately, but it does not improve the uncentered large-sieve bound. Since \(P=KT>K^2\), this is a budget of order \(P^2\) up to logs, whereas the sufficient square estimate at \(h=1\) asks for \(T^{2-\eta}K\). This comparison concerns the available norm bound, not a lower bound for the actual prime sums.

## What the closest published phase and dispersion results supply

Pascadi, *On the exponents of distribution of primes and smooth numbers*, arXiv:2505.00653v2, Definition 1.1 and Theorem 1.3 on p. 2, proves arbitrary-log savings for a **fixed** nonzero residue \(a\), with triply well-factorable weights up to \(Q=x^{5/8-\epsilon}\). Its other case concerns special upper-bound well-factorable linear sieve weights up to \(x^{3/5-\epsilon}\). In the longest prime block \(K\asymp T^\theta,\ P\asymp KT\), the modulus exponent relative to \(P\) is \(\theta/(1+\theta)<1/2\), so a larger progression exponent does not address the obstacle. The issue is the simultaneous oscillating use of all residue classes.

At the minimal-support level the band coefficient itself fails the factorability condition. At level \(Q\asymp Y^{4b}\), choose a legal split with \(Q_1=Y^{a/2}\) and \(Q_2Q_3=Q/Q_1\). For each supported modulus all nontrivial divisors exceed \(Y^a\), so every convolution term with first factor at most \(Q_1\) must use first factor 1. The remaining factors cannot reach moduli larger than \(Q/Q_1\). Supported products near the upper endpoint do exceed this threshold. The same argument applies to the coefficient divided by the modulus or multiplied by a Mellin phase. This excludes using that particular level and split, but does not address larger declared levels. [Pascadi v2, primary preprint](../../sources/prime117_references/pascadi.pdf)

**Padded-level correction.** The original minimal-level obstruction does not rule out applying Pascadi's coefficient hypothesis at a larger declared level. The exact four-prime coefficient divided by 24 is triply well-factorable at \(Q=Y^{6b}\), and so is its completely multiplicative twist \(k^{-1+it}\). In the longest block \(P\asymp Y^{1+4b}\) the padded level satisfies the theorem's \(5/8-\varepsilon\) range for \(b<1/6\). The fixed residue and oscillating Fourier-mode mismatch remains, as does the countermodel above. [Exact padded factorization](prime137_padded_factorability.md)

Matomäki, *A Bombieri–Vinogradov type exponential sum result with applications*, J. Number Theory 129 (2009), pp. 2214–2225, Theorem 1 and Corollary 3 on author manuscript p. 2, gives a relevant special case where an additive phase is retained. It estimates an average over progression moduli \(d\) with a fixed residue \(c\), against phases \(e(\alpha j n)\) with **common** \(\alpha\) and an independent integer multiplier \(j\) in a dyadic block with divisor-bounded coefficients. Corollary 3 is the \(j=1\) case with well-factorable modulus weights at level \(x^{1/2}/(\log x)^A\), and rational approximation denominator between \((\log x)^A\) and \(x/(\log x)^A\). Neither theorem allows the varying reciprocal frequency \(-h/k\), tied to the same product of four primes that is averaged, or the centered linear combination over all unit residues. It supplies a nearby phase-preserving dispersion result, but it does not furnish the displayed product form or its sufficient square estimate. [Matomäki, primary author manuscript](../../sources/prime117_references/matomaki.pdf)
