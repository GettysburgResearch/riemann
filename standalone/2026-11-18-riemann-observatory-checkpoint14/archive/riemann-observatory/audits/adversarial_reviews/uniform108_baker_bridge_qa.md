# Independent QA of the Baker inverse-prime bridge

18 November 2026. I checked the primary journal statement and the fixed-endpoint argument needed to use it with the transformed weights. This is a scoped source and proof check for the pending bridge, with no canonical change. [Baker, *Kloosterman sums with prime variable*, Acta Arith. 156 (2012), pp. 351–352](https://www.impan.pl/shop/en/publication/transaction/download/product/82065) · [Upstream Estermann formula](weighted101_single_mangoldt_strata.md)

## Primary theorem and endpoint conversion

Baker defines \(S_q(a;x)=\sum_{x<p\le2x,(p,q)=1}e(a\bar p/q)\). Theorem 2 is an estimate for a fixed common annulus parameter \(\sqrt Q\le x\le2Q\), with summation over \(Q<q\le2Q\) outside the maximum over unit numerators. Its bound is
\[
 Q^\varepsilon (Q^{11/10}x^{4/5}+Q x^{11/12}).
\]
The source definition is annular. A fixed-prefix estimate follows by writing \(p\le t\) as the union of dyadic annuli \(t/2^{j+1}<p\le t/2^j\), retaining annuli with base at least \(\sqrt Q\). If \(t\le4Q\), the first annulus base does not exceed \(2Q\). The residual primes number \(O(\sqrt Q)\) per modulus, contributing \(O(Q^{3/2})\). On a common prime block \((P,2P]\) with \(\sqrt Q\le P\le2Q\), this residual is absorbed by \(Q^{11/10}P^{4/5}\). Summing the geometric series and taking differences of fixed prefixes therefore bounds \(\sum_{q\asymp Q}\max_{(a,q)=1}|\sum_{P<p\le t} e(a\bar p/q)|\) for each fixed \(P\le t\le2P\), by the same expression at \(P\), up to constants.

This gives no direct bound with a supremum over \(t\) inside the modulus average. The issue also arises for modulus-dependent sharp cutoffs. For arbitrary such cutoffs on \([P,2P]\), a grid of \(L\) common endpoints gives at best an immediate bound of order \(L\) times the fixed-endpoint estimate plus \(O(Q(P/L+1))\) from the snapped differences. The smooth route does not need this loss. It uses partial summation on a common interval, under the modulus sum and with the endpoint integral outside that sum.

## Transformed weights and gcd blocks

Let \(V_T(u)=w_T(Tu)\), \(M=kT/(2\pi p)\), and \(F_{k,p}(x)=V_T(x/M)\). The exact Mellin identity is \(\widetilde F_{k,p}(s)=M^s\widetilde V_T(s)\). Consequently the dependence on \(p\) on \(s=-B+it\) is the common factor \(p^{B-it}\) times the outer \(\log^3p\); the dependence on \(k\) is in coefficients independent of \(p\). The factor \(T^{-B}k^Bp^B\), after the Dirichlet factor and \(1/k\) are included at the block level, can be bounded by a small fixed power using \(B>0\) small. Partial summation on a common prime block costs \(O_B(P^B\log^3 T(1+|t|))\) from the prime weight, and applies the source estimate at one fixed endpoint at a time. The Mellin integral of the resulting gamma power and the cutoff decay costs \(O_B(\delta^{-3-2B})\), where \(\delta=H/T\). This includes the extra \((1+|t|)\) from partial summation. A sufficiently large fixed integration-by-parts order gives this bound.

For fixed dual index \(h\), partition by \(d=(h,k)\), \(q=k/d\), so \(a=h/d\) is a unit modulo \(q\). The original phase reduces from \(e(\pm h\bar p/k)\) to \(e(\pm a\bar p/q)\). The normalized Ramanujan subtraction becomes \(\mu(q)/\varphi(q)\) after reducing the unit group. On a fixed modulus block the coefficients of the outer sum are bounded independently of the prime. The condition \((p,k)=1\) can be replaced by \((p,q)=1\) for Baker at a cost of at most the finitely many primes dividing \(d\) per modulus; these may be subtracted separately, uniformly in any fixed endpoint. Centering causes no further loss because the centered sum is the fixed-numerator sum minus an average of unit-numerator sums, each bounded by the same maximum for a common endpoint. The case \(q=1\) vanishes identically.

For the good blocks \(P\le2Q\asymp K/d\) and \(P\ge\sqrt Q\), summing over \(d\mid h\) majorizes the contribution by \(\tau(h)\) times Baker's bound at modulus parameter \(K\). When \(P<\sqrt Q\) the bound \(QP\) is already at most \(Q^{11/10}P^{4/5}\). For the small-conductor blocks \(Q<P/2\), the trivial estimate \(QP\) is \(O(P^2)\) per divisor \(d\mid h\). One can sum the resulting fixed-index estimate over all \(h\), without a prime- or modulus-dependent truncation: \(\sum_{h\ge1}d_2(h)\tau(h)h^{-1-B}<\infty\) for each fixed \(B>0\). If a truncated variant is used instead, take a single upper bound for the whole \((K,P)\) block and estimate its tail before any Baker invocation. No prime dependent inner cutoff can silently be substituted into the theorem.

Thus a general safe block bound with this treatment is
\[
 \ll_{\eta}T^\eta\big(K^{11/10}P^{4/5}+KP^{11/12}+P^2+K\big),
\]
for fixed polynomial-size \(K,P\), after choosing \(B\) sufficiently small and \(\kappa<1\) sufficiently close to one. The \(K\) term includes the finitely many removed primes per modulus. One can also count large \(d\) as divisors inside the absolutely convergent dual sum rather than use \(\tau(h)\); this is not needed for the displayed bound.

## The actual short-dual Bessel proof in Prime107

The Prime107 argument uses a narrower transition block and avoids the gcd fallback above. I checked the primary Blomer–Harcos–Michel formulas (2.25)–(2.27), pp. 708–709. They give an additive-numerator-independent main term, and dual prefactor \(1/k\) with \(J^-=-2\pi Y_0(4\pi z)\) and \(J^+=4K_0(4\pi z)\). Together with the original \(1/k\) and the substitution \(x=Mu\), this gives exactly \(M/k^2\) in the transformed weight. In each kernel's own indexing, the phase for numerator \(-p\) is \(e(\mp l\bar p/k)\). The unit average subtracts \(c_k(l)/\varphi(k)\) for either sign. No sign issue affects Baker's maximum, but the paired signs matter in an exact formula. [Primary divisor Voronoi formula](https://www.numdam.org/item/10.1016/j.ansens.2007.05.003.pdf#page=13) · [Prime107 bridge](prime107_inverse_prime_voronoi.md)

On \(T^{1-\eta}/K\le P\le T^{1+\eta}/K\), put \(R=\sqrt{lM}/k\). Then \(M/k^2\ll T^\eta\), \(R\gg l^{1/2}T^{-\eta/2}\) and \(\Delta R\gg l^{1/2}T^{-3\eta/2}\) for \(\Delta\ge T^{-\eta}\). When \(l>T^{6\eta}\) the latter is at least a fixed positive constant times \(T^{3\eta/2}\). On the weight support, \(u\) is bounded away from zero and infinity. The derivative of \(\sqrt u\) is bounded away from zero, so each integration by parts costs at most \((\Delta R)^{-1}\), by the symbol bounds and \(O_j(\Delta^{-j})\) cutoff derivatives. The Bessel asymptotics can be taken to enough orders or in Hankel symbol form. Dropping the extra favorable symbol factor, the full tail is bounded by \(T^\eta(KP) T^{3j\eta/2}\sum_{l>T^{6\eta}} l^{\epsilon-j/2}\) up to powers of \(\log T\). For \(j>2+2\epsilon\), its exponent is at most \(1+8\eta+6\epsilon\eta-3j\eta/2\), with fixed log losses, so any fixed power saving follows by choosing \(j\) large. The modified Bessel kernel has stronger exponential decay.

For \(l\le T^{6\eta}\) choose \(6\eta<a\). The support primes of \(k\) exceed \(Y^a\asymp T^a\), so \((k,l)=1\) for sufficiently large \(T\). The kernel arguments lie between constants times \(T^{-\eta/2}\) and \(T^{7\eta/2}\). The bounds for \(J,zJ'\) imply a common pointwise envelope \(T^{3\eta}\log^C T\) for the full logarithmic prime weight and \(P\) times its first derivative. Indeed \(pM'=-M\), and differentiating the Bessel argument multiplies its derivative by \(-z/(2p)\). The common taper is independent of \(p\) in the \(u\)-integral, so this differentiation costs no \(\Delta^{-1}\). On an interval \([u_0,u_1]\) common to the moduli, the integrated contribution is bounded using
\[
 \int_{u_0}^{u_1}\sup_k |W'_{k,l}(t)|
       \left(\sum_k\left|\sum_{u_0<p\le t} e(\mp l\bar p/k)\right|\right)dt
\]
with the separate fixed endpoint term. This is valid because the derivative bound is a common pointwise envelope. Each fixed-endpoint sum over \(k\) is a subset of Baker's full modulus block. The factor \(\mu(k)/\varphi(k)\) satisfies \(|\mu(k)/\varphi(k)|\ll1/k\) on the four-prime support, giving the stated \(P\) term after summing \(k\). The short dual sum costs \(T^{6\eta}\log^{O(1)}T\).

The needed strict conditions can be imposed at once. A sufficient list is
\[
 \eta<\min\{2\vartheta_--1,\ 1-3\vartheta_+/2,\ a/6\},\qquad
 10\eta+\epsilon<\min\{1/5-3\vartheta_+/10,\ (1-\vartheta_+)/12\}.
\]
The first two margins place all common endpoints in the converted prefix domain; the latter two margins come from the exponent table
\[
 \begin{array}{c|c}
 \text{block term before losses}&\text{largest exponent after short-dual loss}\hline
 K^{11/10}P^{4/5}&4/5+3\vartheta_+/10+10\eta+\epsilon\
 KP^{11/12}&11/12+\vartheta_+/12+10\eta+\epsilon
 \end{array}
\]
where \(P\le T^{1+\eta}/K\) is used. The \(P\) term has exponent at most \(1-\vartheta_-+10\eta+\epsilon\), also less than one. Choose \(2(1-\kappa)+\delta_0<\eta\) for overlap with the prior coprime short-factor region, reserving strict margins for fixed dyadic factors and the earlier saddle condition.

**Disposition.** No mathematical blocker found in the local inverse-prime bridge. The shortened journal page span in the initial draft should read 351–372, and its final sliced-interval sentence should say the interval endpoints are common across the moduli. A weight that varies with the modulus is already covered by the common derivative envelope; an arbitrary moving sharp endpoint is a different hypothesis. The result does not handle long-dual contributions or inverse squares by Baker. The arithmetic fourth moment stays unresolved.
