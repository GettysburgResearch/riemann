# Independent check of the Lagarias interval from 55,440 to 720,720

Reviewer rt_repair_62, 17 November 2026. Reviewed the [shared-parameter proposal](../../proposals/independent_campaigns/lagarias_shared_ca_latest62_round5.md), its integer interval replay, and its saved JSON. This audit treats the previously reviewed [global concavity theorem](../../proposals/independent_campaigns/lagarias_global_concavity_round2.md) as an input.

## Prime-power support and equality

For \(\epsilon>0\), \(\sigma(n)n^{-(1+\epsilon)}\) is a finite product of prime-power factors by multiplicativity. At a prime \(p\), putting \(R(k)=\sigma(p^k)p^{-k(1+\epsilon)}\), division gives
\[
 R(k)/R(k-1)=p^{-\epsilon}\frac{p^{k+1}-1}{p(p^k-1)}
 =p^{\epsilon_{p,k}-\epsilon},\qquad
 \epsilon_{p,k}=\frac{\log(1+(p-1)/(p(p^k-1)))}{\log p}.
\]
The thresholds strictly decrease to zero with \(k\). If consecutive thresholds straddle \(\epsilon\) strictly, the local sequence increases up to the sole maximizing exponent and decreases after it. If a threshold equals \(\epsilon\), it creates precisely a tie of its two neighboring exponents. No numerical equality check is needed for \(p=13,k=1\), because the ratio inside the logarithm there is exactly \(14/13\) and \(\epsilon_*=\log(14/13)/\log 13\) by definition.

The independent replay confirms the maximizers \(4,2,1,1,1\) at \(p=2,3,5,7,11\), respectively, and the strict comparisons \(\epsilon_{13,2}<\epsilon_*\) and \(\epsilon_{17,1}<\epsilon_*\). For real \(p>1\), \(\epsilon_{p,1}=\log(1+1/p)/\log p\) decreases strictly because the numerator is positive decreasing and denominator positive increasing. Every prime \(p\ge17\) therefore has sole maximizing exponent zero. The only primes below 17 are \(2,3,5,7,11,13\). It follows that the product of local maxima involves just these six primes. Every finite factorization is bounded by that product, and attaining it requires every factor, including omitted primes where the exponent is zero, to be a local maximizer. Exactly the two integers \(2^4 3^2 5\cdot7\cdot11=55{,}440\) and \(13\cdot55{,}440=720{,}720\) attain it.

There is also no maximizing integer at any other \(\epsilon>0\) strictly between these two values. At \(\epsilon>\epsilon_*\), the increasing portions of each local sequence cannot extend beyond the smallest maximizing exponent at \(\epsilon_*\). At \(0<\epsilon<\epsilon_*\), each local maximum has exponent at least the largest maximizing one at \(\epsilon_*\). These statements follow immediately from the strict threshold signs on the corresponding sides of \(\epsilon_*\), including at the exactly tied threshold. Thus the higher-parameter integers divide \(55{,}440\), and the lower-parameter integers are multiples of \(720{,}720\). The argument works with ties allowed in the definition of colossally abundant.

## Interval directions and replay

The integer replay passed in read-only mode and matched its saved JSON. Its harmonic bounds enclose \(H_n\) because each floor contributes an error in \([0,1/S)\), with \(S=2^{192}\). Rational log inputs are outward-rounded before the log calculation. Its interval implementation range-reduces log by powers of two, and encloses the reduced log by the positive series for \(2\operatorname{atanh}((y-1)/(y+1))\). Its claimed geometric tail \(3\cdot 2^{-2M}\) bounds the omitted terms for ratio at most \(1/2\). For exp it reduces the argument to \([0,1]\), adds the positive Taylor tail bounded by \(3/(M+1)!\), then squares positive interval values. Log and exp take lower endpoints for lower bounds and upper endpoints for upper bounds because both functions increase. The four signed products and exact integer floor/ceiling formula preserve interval direction. In particular the endpoint operation computes a lower bound for \(H_n+e^{H_n}\log H_n\), not for a rounded point value.

A separate [Decimal replay](../../experiments/code/lagarias_ca_rt62.py) uses standard-library Decimal correctly rounded log and exp at 65 significant digits, widened by one context spacing on each side, and independently directed floor and ceiling for basic arithmetic. Harmonic sums are accumulated as rational bounds with decimal scale \(10^{65}\) and the divisor sums are computed by summing divisor pairs up to \(\lfloor\sqrt n\rfloor\), separately from the prime-power formula. It confirms every strict threshold sign and the strict endpoint bounds
\[
 \begin{array}{c|r|c}
 n&\sigma(n)&B(n)-\sigma(n)\\\hline
 55{,}440&232{,}128&(9051.9211023638,\ 9051.9211023639)\\
 720{,}720&3{,}249{,}792&(143828.5957097173,\ 143828.5957097174).
 \end{array}
\]
The script asserts that each gap lies strictly between its claimed integer floor and the following integer, and prints its full interval. No floating-point or approximate tie test is involved.

## Interpolation and scope

With \(t=\log n\) and \(M_*\) the common maximum, \(\log(\sigma(n)/n)\le\log M_*+\epsilon_*t\). At the two endpoints this affine function equals \(\log(\sigma(n)/n)\) and is strictly below \(g(t)=\log(B(e^t)/e^t)\) by the arithmetic replay. On the closed interval the difference of \(g\) and the affine function is concave, so its value is at least the convex combination of its two strictly positive endpoint values. At each integer \(n\) in that range the digamma continuation agrees with the ordinary harmonic sum. Concavity therefore certifies precisely the requested strict Lagarias bound at all \(720{,}720-55{,}440+1=665{,}281\) integers in the closed interval. The count added beyond the earlier certificate is \(665{,}280\).

The existing [initial certificate](../../experiments/results/lagarias_55440_summary.json) covers \(1\) through \(55{,}440\) with equality only at \(1\). The common endpoint makes the union contiguous. The combined range is \(1\) through \(720{,}720\). This does not give an infinite tail bound.
