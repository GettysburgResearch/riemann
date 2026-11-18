# Independent check of the progression-norm limitation

The artificial residue arrays in prime117 are a valid obstruction to inferring a small prescribed Fourier mode from the two stated progression norms alone. They preserve row centering and positivity at the common endpoint. They do not describe actual primes or a single sequence shared across different moduli. The exact product-preserving CRT formula also checks out. [Prime117 proof](prime117_long_prime_obstacle.md)

## A supported dyadic family

Take fixed \(0<c<d<1\) with \(d/c<2^{1/4}\). Let \(K=c^4Y^{4b}\) and \(\mathscr S\) be the set of products of four distinct primes from \(cY^b<p\le dY^b\). These primes are in the original band for all sufficiently large \(Y\), because \(a<b\). Every product lies in \((K,2K]\), is odd and squarefree, and has fourth-power coefficient 24. If \(N\) is the number of chosen primes, the prime number theorem gives \(N\sim(d-c)Y^b/(b\log Y)\). Unique factorization gives \(S=|\mathscr S|={N\choose4}\asymp K/(\log T)^4\) for \(T\asymp Y\). This proves that the artificial errors use actual supported moduli, at the top scale \(K\asymp T^\theta\) with \(\theta=4b>1/2\).

## Exact centered cosine and the two budgets

For the common scale \(P=KT\), put \(A=\sqrt{P/S}\), and, on \(\mathscr S\), set
\[
 F_q(u)=\cos(2\pi u/q)-\mu(q)/\varphi(q),\qquad
 E_{q,u}=A F_q(u),\qquad u\in(\mathbb Z/q\mathbb Z)^\times.
\]
Use \(E_{q,u}=0\) for the other rows in the modulus block. The sum of the cosine over the units is \(c_q(1)=\mu(q)\), so each row sums to zero. Using \(\cos^2x=(1+\cos(2x))/2\) gives exactly
\[
 V_q=\sum_{u\bmod q}^{*}F_q(u)^2
    =\frac{\varphi(q)+c_q(2)}{2}-\frac{c_q(1)^2}{\varphi(q)}.
\]
For these four distinct odd primes, \(\mu(q)=1\) and \(c_q(2)=c_q(1)=1\). Thus \(V_q=(\varphi(q)+1)/2-1/\varphi(q)\asymp q\). In fact \(\varphi(q)/q\to1\) uniformly on the selected moduli, since their least prime factor grows at least as fast as \(cY^b\).

The artificial masses \(P/\varphi(q)+E_{q,u}\) are positive for all sufficiently large \(T\). Indeed \(\lVert F_q\rVert_\infty\le2\), \(A\asymp\sqrt T(\log T)^2\), and \(P/\varphi(q)\ge P/q\ge T/2\). Their total over units is \(P\) for every row, by exact centering. The two budgets are
\[
 \sum_{q\asymp K}\max_u |E_{q,u}|
   \ll AS=\sqrt{PS}\asymp \frac{K\sqrt T}{(\log T)^2},
 \qquad
 \sum_{q\asymp K}\sum_{u\bmod q}^{*}|E_{q,u}|^2
    =A^2\sum_{q\in\mathscr S}V_q\asymp PK.
\]
The first is \(o(P/(\log T)^B)\) for every fixed \(B>0\); this is separate for each \(B\). If a particular positive constant is desired in the upper variance bound, shrink \(A\) by a fixed constant. Neither the positivity nor the power-size conclusion changes.

The weighted real phase sum is exactly \(24A\sum_{q\in\mathscr S} V_q/q\). Indeed multiplying by \(\cos(2\pi u/q)\) or by \(F_q(u)\) gives the same row pairing because the errors sum to zero. The imaginary part in the complex phase vanishes by pairing \(u\) and \(-u\). Thus the sum is positive and of order
\[
 \sqrt{PS}\asymp K\sqrt T/(\log T)^2,
 \qquad
 \frac{\sqrt{PS}}{T(\log T)^4}\asymp
         T^{\theta-1/2}/(\log T)^6\longrightarrow\infty.
\]
This comparison also holds with \(P\asymp KT\) having any fixed positive multiplicative constants. It establishes a limitation of abstract maximum-error and total-variance inequalities, even with nonnegative masses, a common endpoint and exact unit centering. It gives no lower bound for an actual prime sum. For example the arrays were not constructed to obey residue-distribution compatibility across distinct moduli, nor to capture signed correlations between endpoints. A result using such structure is outside this obstruction.

## Exact product phases and the surviving hypothesis

The first-power prime remainder has \(R_k(h,p)=e(-hp/k)-\mu(k/(h,k))/\varphi(k/(h,k))\) with \((p,k)=1\). The unit average follows by reducing to \(q=k/(h,k)\) and using surjectivity of units onto \(q\), where \(p\) and \(h/(h,k)\) act by permutations. If \(q=1\), the centered phase is zero. There is no coprimality requirement on the divisor argument \(h\).

The two-pair product counts \(\alpha_r,\beta_s\) are at most two even with repeated primes, and their convolution is exactly the coefficient of \(D^4\). For coprime \(r,s\), let \(\bar s\) denote the inverse of \(s\bmod r\), and \(\bar r\) the inverse of \(r\bmod s\). Then \(s\bar s+r\bar r\equiv1\bmod rs\), giving
\[
 e(-hp/(rs))=e(-hp\bar s/r)e(-hp\bar r/s).
\]
This factors the additive phase for each pair. It does not separate the dependence on \(r\) and \(s\) in a double sum, since each factor involves an inverse of the other modulus. Both factors are conjugated if the original sign is reversed. If one instead applies CRT to a dual inverse-prime phase, the corresponding identity is
\[
 e(\pm l\overline p/(rs))
    =e(\pm l\,\overline{ps}/r)e(\pm l\,\overline{pr}/s),
\]
with the bars taken modulo the denominators. These formulas hold with nonunit \(h\) or \(l\), and a local phase factor equals one wherever its modulus divides the numerator. If \(r,s\) share a factor, neither CRT inverse is available and the original centered kernel is retained. No factorability claim is implied by the pair convolution.

The Mellin factors in prime117 follow from inserting \(W(2\pi hp/(Tk))\) by Mellin inversion, giving \(k^{it}h^{-it}p^{-it}(2\pi/T)^{-it}\). They preserve the coupled pair weights. The coefficient norm used in its proposed phase-sensitive square estimate is \(O(T^\epsilon\sqrt{D/K})\) on dyadic \(h\asymp D\), \(k\asymp K\). This follows by a direct square sum with \(a_k\) bounded, \(d_2(h)\ll_\epsilon T^\epsilon\), and \(k^{-1}\asymp K^{-1}\). A bound of \(T^{2-\eta}K/D\) for the corresponding square sum would give a power saving after the Mellin loss by taking \(\kappa\) sufficiently close to one. The model-square comparison \(KDP/(T^2K/D)\asymp K^2/P\) is correct on \(DP\asymp KT\), and is only a scale comparison. No square estimate for the genuine phases follows from this check. No canonical record was edited.
