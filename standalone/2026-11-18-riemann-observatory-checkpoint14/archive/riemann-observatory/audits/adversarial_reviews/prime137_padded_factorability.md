# Exact padded factorability for products of band primes

18 November 2026. The four-prime modulus coefficient satisfies Pascadi's triply well-factorable hypothesis after padding its level. The minimal-support obstruction in prime117 still holds at that level. The padded level fits Pascadi's exponent range in the longest prime block. The fixed-residue condition remains a separate obstruction to applying that theorem to the required phase-weighted sum. [Pascadi, Definition 1.1 and Theorem 1.3, p. 2](../../sources/prime117_references/pascadi.pdf) · [Earlier long-prime analysis](prime117_long_prime_obstacle.md)

## Factorization at every prescribed split

Let \(\mathcal P\) be a nonempty finite set of band primes and \(p_{\max}\) its largest element. Write \(D(s)=\sum_{p\in\mathcal P}p^{-s}\) and let \(c^{(m)}_k\) be the coefficient of \(k^{-s}\) in \(D(s)^m\). The coefficients are nonnegative, \(c^{(m)}_k\le m!\), and
\[
 c^{(m_1)}*\cdots*c^{(m_r)}=c^{(m)}
 \quad\text{if }\sum_i m_i=m.
\]
The case \(m_i=0\) means the delta function at 1. For \(m,r\ge1\), the sequence \(c^{(m)}/m!\) is \(r\)-way well-factorable of level \(Q\) exactly when
\[
 Q\ge p_{\max}^{m+r-1}.
\]
Here \(r\)-way means the direct analogue of Pascadi's Definition 1.1: for every split \(Q=\prod_i Q_i\), \(Q_i\ge1\), one has a Dirichlet convolution of \(r\) sequences, each 1-bounded and each supported in its prescribed range \([1,Q_i]\).

For sufficiency put \(f_i=\lfloor\log_{p_{\max}}Q_i\rfloor\). Because \(\sum_i f_i>\log_{p_{\max}}Q-r\) and the left side is integral, \(\sum_i f_i\ge m\). Choose nonnegative integers \(m_i\le f_i\) adding to \(m\). The sequence \(c^{(m_i)}/m_i!\) is 1-bounded, and every support point is at most \(p_{\max}^{m_i}\le Q_i\). The convolution of these \(r\) sequences is \(c^{(m)}/\prod_i m_i!\). Multiply one factor by \(\prod_i m_i!/m!\), a constant at most 1 by the integral multinomial coefficient. The resulting convolution is exactly \(c^{(m)}/m!\). It holds for all integer arguments, including outside the support, because it is an identity of the full Dirichlet polynomials.

For necessity, the coefficient at \(p_{\max}^m\) is nonzero, so \(Q<p_{\max}^m\) already fails the support requirement. If \(p_{\max}^m\le Q<p_{\max}^{m+r-1}\), choose nonnegative integers \(f_i\) with sum \(m-1\), and set
\[
 u=\frac{\log_{p_{\max}}Q-(m-1)}r,\qquad Q_i=p_{\max}^{f_i+u}.
\]
Then \(0<u<1\) and \(\prod_iQ_i=Q\). Every tuple of factors whose product is \(p_{\max}^m\) has factors \(p_{\max}^{v_i}\). Their prescribed bounds would force \(v_i\le f_i\), hence \(\sum_i v_i\le m-1\). The convolution coefficient must be zero regardless of the candidate factors' signs or complex phases. The case \(r=1\) has no intermediate interval and follows directly.

The sufficiency remains valid after multiplying the final sequence by any completely multiplicative function \(g\) with \(|g(n)|\le1\): multiply each constituent by \(g\). If \(g(p_{\max})\ne0\), the same necessity applies. In particular \(g(k)=k^{-1+it}\) for real \(t\) is eligible and nonvanishing. All norms remain 1-bounded independently of \(t\). The identical argument with \(g(k)=k^{it}\) also holds. A separate factor \(1_{K<k\le2K}\) or an additive phase \(e(-a/k)\) is not covered by this multiplication rule.

For the specific band \(Y^a<p\le Y^b\), \(p_{\max}\le Y^b\) gives the sufficient level \(Y^{(m+r-1)b}\). The prime number theorem in any fixed multiplicative neighborhood of \(Y^b\) implies \(p_{\max}=Y^{b+o(1)}\); hence the power exponent is asymptotically necessary. Even if considering only \(m\) distinct near-top primes, the same lower exponent obstruction holds with fixed slack: for any level exponent strictly below \((m+r-1)b\), choose the prescribed \(Q_i\) exponents below their next capacity thresholds, then take all \(m\) primes sufficiently near \(Y^b\) that a divisor with one too many primes still exceeds \(Q_i\). This distinct-prime observation is only a lower bound for such a restriction. The convolution construction above concerns the actual untruncated coefficient.

## Applying the exact hypothesis in the longest block

For \(m=4,r=3\), Pascadi's \(\lambda_k=c^{(4)}_k/24\), or \(\lambda_k=c^{(4)}_k k^{-1+it}/24\), is triply well-factorable at \(Q=Y^{6b}\). In the longest prime block with \(K\asymp Y^{4b}\), \(T\asymp Y\), \(x\asymp P\asymp KT\), one has
\[
 6b<\frac58(1+4b)\quad\Longleftrightarrow\quad b<\frac5{28}.
\]
This holds throughout the band \(1/8<b<1/6\). Strictness leaves room for the theorem's \(\varepsilon\) and for fixed comparison constants in \(x\). If \(K\) instead has a smaller exponent \(\vartheta\), then \(P\asymp KT\) alone gives the condition \(6b<(5/8)(1+\vartheta)\), which must be checked separately for this same full sequence and padded level. Hard shell restrictions on \(k\) are additional weights and are not asserted to preserve the convolution property.

Pascadi's Theorem 1.3(i) sums progression errors against such a sequence for one **fixed** nonzero residue \(a\), and its constant may depend on \(a\). The long-prime application requires the mode \(e(-ha/k)\) over all units \(a\bmod k\), with modulus-dependent residue ranges and the centered unit average. Padding solves the specified coefficient-factorability issue. It gives no estimate for this prescribed mode or for the sum over all its changing residue classes. The norm countermodel in prime117 concerns that separate obstruction and is unaffected by padding. [Exact long-prime kernel and norm countermodel](prime117_long_prime_obstacle.md)
