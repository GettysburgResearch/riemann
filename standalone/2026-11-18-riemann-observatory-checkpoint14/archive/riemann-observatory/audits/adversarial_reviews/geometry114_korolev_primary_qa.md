# Korolev 2018 | Primary-source check of the local inverse-prime saving

I checked the remote MathNet primary PDF of M. A. Korolev, *New estimate for a Kloosterman sum with primes for a composite modulus*, *Sbornik: Mathematics* 209(5), 652–659 (2018), DOI 10.1070/SM8939, §1, printed pp. 652–653 (PDF pp. 1–2). This is the English journal translation of *Matematicheskii Sbornik* 209(5), 54–61. The eight-page primary PDF was accessible in the search-service reader. There are no verified local PDF bytes or hash in this scoped review. The staged paper ID is PAPER-WEIGHTED107-KOROLEV2018. [Remote primary PDF](https://www.mathnet.ru/php/getFT.phtml?jrnid=sm&option_lang=eng&paperid=8939&what=fullteng) · [MathNet metadata](https://www.mathnet.ru/eng/sm8939) · [Pending record](../../quality/pending_round14/weighted107_prime_estimate_records.jsonl)

## The exact source theorem

Equation (1.1) defines
\[
 T_q(X)=\sum_{\substack{1<n\le X\\(n,q)=1}}
             \Lambda(n)e(a\overline n/q),\qquad (a,q)=1 .
\]
The theorem on printed p. 653 requires fixed sufficiently small \(\epsilon>0\), \(q>q_0(\epsilon)\), and \(q^{7/10+\epsilon}\le X\le q\), and proves
\[
 T_q(X)\ll X(q^7X^{-10})^{1/74}q^\epsilon
         =X^{32/37}q^{7/74+\epsilon}.
\]
The sentence immediately before the theorem expressly allows arbitrary moduli. The numerator is uniform over unit residues, including both signs. The \(n=1\) term is irrelevant because \(\Lambda(1)=0\). The paper has a homogeneous inverse phase. Korolev's later arXiv:1911.09981v1, Theorem 1, has a phase with both inverse and linear terms and requires \((ab,q)=1\). It does not allow a zero linear coefficient at the moduli in this application. The exact 2018 theorem is the input here. Neither statement estimates \(e(a\overline p^{\,2}/q)\) by the bound above. [2018 §1](https://www.mathnet.ru/php/getFT.phtml?jrnid=sm&option_lang=eng&paperid=8939&what=fullteng) · [2019 v1, §1 Theorem 1](https://arxiv.org/pdf/1911.09981v1)

## Moduli, coefficients, and the common cutoff

I audited the genuine-prime local block in weighted107, with \(k\asymp K\asymp Y^\theta\), \(T\asymp Y\), \(1/2<\theta<10/17\), \(H=T^\kappa\), \(\delta=H/T\), and \(p\) in a dyadic interval at scale \(X\) with \(T^{1-\theta-\xi}\le X\le T^{1-\theta+\xi}\). Because the shared-prime stratum was handled previously, \((p,k)=1\) in the present block. The divisor-variable Mellin transform uses \(F_{k,p}(u)=w_T(2\pi pu/k)\), so
\[
 \widetilde F_{k,p}(s)=(k/(2\pi p))^s\widetilde w_T(s),\qquad
 M\asymp kT/p,\qquad U\asymp kX/(T\delta^2)=:U_X .
\]
The exact Hurwitz calculation leaves the two phases \(e(\pm\overline p\,h/k)\). Inversion permutes the units, so their respective unit averages are \(c_k(h)/\varphi(k)\). There is no coprimality restriction on the original divisor index. The polar part cancels in the centered transform. [Application under review](weighted107_quadratic_and_inverse_prime_savings.md) · [Exact centered Hurwitz transform](weighted101_single_mangoldt_strata.md)

Use a **common** cutoff \(N_k=\lceil\max(1,U_X)T^{\varepsilon_1}\rceil\) for all primes in the slice of this dyadic block at fixed \(k\). The lower-line absolute bound for \(h>N_k\), on \(\Re s=-A\) with fixed \(A>0\), is
\[
 \ll_A k\delta^{-2}\,U_{\rm true}^A
      \sum_{h>N_k}\frac{d_2(h)}{h^{1+A}}
 \ll_A k\delta^{-2}\,T^{-A\varepsilon_1}\log(2N_k),
\]
since \(U_{\rm true}/U_X\) is bounded by an absolute block constant. The cosine factors and gamma product give \(O_A((1+|t|)^{1+2A})\) after cancellation of their exponential factors. The taper bounds \(\widetilde w_T(-A+it)\ll_{A,j}T^{-A}(1+\delta|t|)^{-j}\) then give \(\delta^{-2-2A}\) before combining the scale factors into \(U_{\rm true}\). This first tail estimate is per prime. The remaining outer coefficients and number of primes have a fixed polynomial bound in \(T\), so increasing \(A\) gives arbitrary power saving after summation. The constants may depend on \(A\), fixed before \(T\) tends to infinity. Once the common finite cutoff is imposed, each retained integral may use \(\Re s=-B\), for example \(B=1\), independently of \(A\). The integrands have no poles on the intervening negative strip and on that strip the Mellin taper decays rapidly enough in \(|t|\) to discard the horizontal segments.

For the retained terms, \(U_X\ll T^{\xi+2(1-\kappa)}\). Choose \(\xi,\varepsilon_1,1-\kappa\) with \(\xi+2(1-\kappa)+\varepsilon_1<a\), with a fixed margin. Then \(N_k<Y^a\) for large \(T\). Every prime divisor of a supported \(k\) exceeds \(Y^a\), so each numerator \(h\) in the retained block is a unit. The unit average reduces to \(\mu(k)/\varphi(k)\). This argument is why no reduced-modulus cutoff or non-unit numerator version of Korolev is needed.

## Partial summation and the strict endpoint

The two constraints needed uniformly at all prefix endpoints within the prime slice follow from \(1-\theta>(7/10)\theta\) and \(1-\theta<\theta\). Both have strict margins on the stated range. Choose the band width \(\xi\) and source loss \(\epsilon\) small enough that \(k^{7/10+\epsilon}\le v\le k\) throughout the slice. The constant-factor uncertainty in \(v\asymp X\), \(k\asymp T^\theta\) is harmless with those margins. Difference of prefixes gives pointwise control at every moving Abel endpoint in the slice. The proper prime powers in a source prefix cost \(O(X^{1/2}\log^2(2X))\) after removing them and are dominated by the Korolev bound on this range. The prime weight before Abel summation is \(\log p\). The extra factor is \(\log^2p\,p^{-s}\), with supremum plus total variation \(O_B(X^B(1+|t|)\log^2(2X))\) on \(s=-B+it\). This estimate follows by differentiation and integrating \(dp/p\) over a comparable-size interval. It handles cuts at either end of the interval.

On the retained line the additional \(1+|t|\) changes the integrated vertical factor to \(\delta^{-3-2B}\). The remaining powers from the centered divisor formula, scale and weight are \(k^{1+2B} (k/(2\pi))^{-B}X^B T^{-B}\), up to fixed \(B\)-dependent constants. Their product with the vertical factor is \(O_B(k\delta^{-3}U_X^B)\). The dual \(h\)-sum is absolutely bounded by \(\sum_h d_2(h)h^{-1-B}\), without a factor \(N_k\). The external \(c_k/k\) sums to \(O(1)\) per modulus block because \(c_k\le24\). The principal subtraction uses \(\varphi(k)^{-1}\ll_\epsilon K^{-1+\epsilon}\) on the supported block. The resulting bound is
\[
 \ll_{\epsilon,B} T^{O(\epsilon)} K\delta^{-3}U_X^B
     \left(X^{32/37}K^{7/74}+XK^{-1}\right).
\]
Here epsilon denotes fixed small losses, with \(\xi,1-\kappa\) chosen separately. At the middle prime scale \(X\asymp T^{1-\theta}\), the first term's exponent before the small losses is
\[
 \theta+\frac{32}{37}(1-\theta)+\frac7{74}\theta
     =\frac{64+17\theta}{74}.
\]
It is below \(1\) exactly for \(\theta<10/17\). The subtraction term starts at exponent \(1-\theta\). Taking fixed \(B=1\) on retained terms, then choosing fixed \(\xi\), \(1-\kappa\), and source and auxiliary losses sufficiently small, gives a power saving throughout the whole declared local band. The source range has slack at \(\theta=10/17\), but this exponent calculation loses its power saving there. The verified statement concerns the local genuine-prime part of the smooth arithmetic remainder. The longer prime range, inverse-square phases, and RH-conditional transfer to the fourth zero moment are separate. No canonical files were changed.
