# A rough-mask phase bound and the unit-baseline gap

Consider the squarefree subfamily \(\mathcal S\) of prime161, with \(K\asymp T^\theta\), \(1/2<\theta<2/3\), \(P\asymp KT\), and four distinct factors in a fixed narrow band \(\mathcal P=[X,(1+\eta)X]\cap\mathbb P\), \(K=X^4\). Use \(J=[P,2P)\cap\mathbb Z\), and let \(R\) consist of integers divisible by no prime of \(\mathcal P\). There is a uniform lower bound for the moving-phase energy on \(J\cap R\). This gives a rigorous partial result on imposing true unit support. Weighted \(P/\varphi(k)\) progression bounds for a positive common sequence remain unresolved.

## Phase energy survives the global rough mask

For
\[
 h_k(n)=\mathbf1_{(n,k)=1}\left(\cos(2\pi n/k)-\frac{\mu(k)}{\varphi(k)}\right),
 \qquad H(n)=\sum_{k\in\mathcal S}d_kh_k(n),\qquad d_k\asymp1,\quad d_k>0,
\]
write vectors of periodic Fourier coefficients on the circle using reduced fractions. For any subfamily \(\mathcal U\subset\mathcal S\),
\[
 \|\operatorname{coeff}(H_\mathcal U)\|_2^2\ll|\mathcal U|,\qquad
 H_\mathcal U=\sum_{k\in\mathcal U}d_k h_k.
\]
To prove this, decompose by exact reduced denominator \(q\mid k\) for each \(h_k\). The projection onto the denominators dividing \(q\) equals the conditional average over a class mod \(q\). Put \(r=k/q\). For a unit class modulo \(q\), Chinese remaindering in \(\mathbf1_{(n,k)=1}e(n/k)\) produces a unit sum over the missing \(r\) component with primitive additive numerator, hence the factor \(\mu(r)/r\) after averaging. For a nonunit class the projection vanishes. The projection of the constant correction is at most \(1/\varphi(k)\ll1/r\). Each exact denominator \(q\) therefore has squared energy \(\ll r^{-2}\), by bounding it by the whole dividing-\(q\) projection. For fixed \(q\) with \(4-m\) factors, the number of possible \(k\) is \(O(X^m)\). Cauchy–Schwarz over these compatible \(k\) and then summing \(q\) gives per original \(k\) a cost at most \(\sum_{q\mid k}O(X^m r^{-2})=O(1)\). The \(q=1\) coefficient is zero. For the full family, the frequency \(1/k\) comes only from the single \(k\) and has coefficient bounded below, as computed in prime161. Thus the full squared energy is \(\asymp|\mathcal S|\).

The interval Gram estimate in prime161 gives \(\sum_{n\in J}|H(n)|^2\gg P|\mathcal S|\). For any \(p\in\mathcal P\), when \(p\mid n\) the terms with \(p\mid k\) vanish exactly. On this lattice the remaining sum is \(H_{\mathcal U_p}(pm)\) with \(\mathcal U_p=\{k\in\mathcal S:p\nmid k\}\). Every reduced denominator in this subfamily is coprime to \(p\). Scaling rational frequencies by \(p\) preserves distinctness and leaves reduced denominators at most \(2K\), so the same \(O(K^2\log K)\) Gram row estimate applies to the interval of \(m\)'s of length \(P/p+O(1)\). The hypothesis \(P/p\gg K^2\log K\) holds here since \(P/p\asymp KT/X\) and \(T/(KX)\) grows polynomially for \(\theta<2/3\). Consequently
\[
 \sum_{\substack{n\in J\\p\mid n}}|H(n)|^2\ll (P/p)|\mathcal S|.
\]
Since \(\sum_{p\in\mathcal P}1/p=O(1/\log X)\) by the prime number theorem upper bound on the band, the union bound yields
\[
 \sum_{n\in J\cap R}|H(n)|^2\gg P|\mathcal S|.
\]
There is no loss of the scale of the phase in squared energy from imposing simultaneous unit support on the band.

One corollary separates the energy statement from centering. The average of \(H\) on \(J\) is \(O(K|\mathcal S|/P)\) since each \(h_k\) is periodic and mean zero. On the excluded set its total is \(O(P\sqrt{|\mathcal S|}/\log X)\) by Cauchy–Schwarz, the lattice energy just proved, and \(|J\setminus R|=O(P/\log X)\). Thus subtracting the mean on \(J\cap R\) still leaves energy \(\gg P|\mathcal S|\).

## Why this does not establish the baseline budgets

For the original positive model, even the unperturbed all-integer row has error relative to the unit baseline of order \(P/(KX)\) on nearly every unit class of each \(k\in\mathcal S\). Indeed \(1-\varphi(k)/k\asymp1/X\) and the integer progression remainder is \(O(1)\). The resulting cumulative variance is \(\asymp P^2/(X^2\log^4 X)\), exceeding \(PK\) by a factor of order \(T/(X^2\log^4 X)\). Positivity and centering by the induced unit mass do not correct it.

For a rough-uniform baseline, one may count unit classes after deleting multiples of band primes. Fix a unit class mod \(k\in\mathcal S\). For a product \(d\) of distinct band primes outside \(k\), the CRT count in that class with \(d\mid n\) is \(P/(kd)+O(1)\). With \(\lambda=\sum_{p\in\mathcal P}1/p\), truncating inclusion-exclusion at fixed order \(r\) and using the next Bonferroni sum yields an error bounded by
\[
 O_r\left((P/k)\lambda^{r+1}+(1+|\mathcal P|)^{r+1}\right)
\]
relative to \((P/k)\prod_{p\in\mathcal P,\,p\nmid k}(1-1/p)\). The same calculation for the total count gives the corresponding product for the normalization. If one could use exact products, normalizing the mass to \(P\) would yield \(P/\varphi(k)\) since all factors of \(k\) lie in the band. However a uniform per-class bound sufficient by summing squares over the supported \(k\)'s would be \(O(\sqrt{P/|\mathcal S|})=O(\sqrt T\log^2 X)\), while the first term above at any fixed \(r\) is of scale \(T/\log^{r+1}X\). Increasing \(r\) in this absolute floor-error estimate also drives the second term above the budget. This is a failed sufficient estimate, with no lower bound for the actual rough-uniform error.

Likewise, the prime161 perturbation uses the identity \(\widehat{\psi*g}=\widehat\psi\,\widehat g\) to suppress low denominators in the sum of progression variances. Multiplying by \(\mathbf1_R\) after convolution removes that identity. The lattice phase estimate above concerns the energy of \(H\), and gives no analogous low-denominator multiplier estimate for a masked arbitrary perturbation. It also does not control the progression deviations of the rough baseline. Constructing a simultaneous baseline and perturbation with \(PK\) variance, mass \(P\) and nonnegativity, even on \(\mathcal S\), remains open in this check. The stronger conditions covering all \(k\le2K\) and imposing a von Mangoldt pointwise cap are additional requirements.

The phase proof uses squarefree moduli, because the missing factors in its conditional-average step are coprime to the retained denominator. It is a restricted lemma on the same band and scale as the earlier common-sequence example. [Earlier positive common-sequence construction](prime161_common_sequence_phase_campaign.md)

In particular, positivity, mass and phase size can be achieved together with the rough support if the progression budgets are dropped. Write \(E=J\cap R\), \(H_0=(H-\langle H\rangle_E)\mathbf1_E\), \(M=\|H_0\|_2\asymp\sqrt{P|\mathcal S|}\), and set \(b^\pm=P|E|^{-1}\mathbf1_E+(K/M)(H_0^\pm-\langle H_0^\pm\rangle_E\mathbf1_E)\). These sequences have mass \(P\) and are nonnegative since their negative correction is at most \(K/\sqrt{|E|}=o(1)\). Their phase difference against \(H/K\) equals \(M\), so one has absolute phase at least \(M/2\). This elementary corollary carries neither a progression-error norm bound nor a pointwise upper bound.
