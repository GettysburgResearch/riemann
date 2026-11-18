# Sharp padded factorability for prime-band powers

The four-prime coefficient meets Pascadi’s triply well-factorable weight hypothesis after padding the level. The earlier obstruction at the minimal support scale persists, but it does not rule out the padded application. Pascadi’s estimate then controls a signed progression discrepancy for a fixed residue. It does not supply the centered, modulus-dependent phase estimate in the arithmetic remainder. [Pinned Pascadi v2](../../sources/prime117_references/pascadi.pdf) · [Earlier minimal-level obstruction](prime117_long_prime_obstacle.md) · [Long-prime adjudication](analytic129_long_prime_adjudication.md)

## Source definition and exact least level

I reread Pascadi arXiv:2505.00653v2, p. 2, Definition 1.1 and Theorem 1.3(i). His definition allows real \(Q_i\ge1\) with \(Q_1Q_2Q_3=Q\), and demands a genuine Dirichlet convolution of complex factors each bounded by one, supported at their corresponding \(Q_i\), for *every* such split. The sequence may have support strictly below \(Q\); there is no lower constraint on its top support. Outside the support it is extended by zero, and the convolution identity is required for all \(q\). The source hash is 2d0ba49950c69ea94b67d3f45e432f4a7fc7dc8dbb0d5c911e99db8c5f2f13b3. The statements below use the same definition with \(r\) factors for a fixed integer \(r\ge1\). [Pascadi, p. 2](https://arxiv.org/pdf/2505.00653v2#page=2)

Fix \(0<a<b\), a nonempty prime band \(\mathcal P=\{p:Y^a<p\le Y^b\}\), and \(m\ge1\). Let \(P_*=\max\mathcal P\), \(D(s)=\sum_{p\in\mathcal P}p^{-s}\), and \(c_m(k)\) be the coefficient of \(k^{-s}\) in \(D(s)^m\). Then the **least** \(r\)-factorable level of \(\lambda(k)=c_m(k)/m!\) is exactly
\[
 Q_{\min}=P_*^{m+r-1}.
\]

For sufficiency choose \(Q\ge Q_{\min}\) and an arbitrary multiplicative split \(Q=\prod_i Q_i\), \(Q_i\ge1\). Put \(t_i=\log Q_i/\log P_*\). The sum of the floors satisfies
\[
 \sum_i\lfloor t_i\rfloor>\sum_i t_i-r\ge m-1.
\]
Hence there are nonnegative integers \(n_i\le\lfloor t_i\rfloor\) with \(\sum_i n_i=m\). Use the coefficients of \(D^{n_i}/n_i!\) in factor \(i\), with \(n_i=0\) giving the sequence supported at 1 of value 1. Each factor is bounded by one since for any product of \(n_i\) primes with exponents \(v_p\), its normalized coefficient is \(1/\prod_pv_p!\). Its support is at most \(P_*^{n_i}\le Q_i\). Multiply one factor by \(\prod_i n_i!/m!\le1\). The resulting convolution is exactly \(\lambda\) at every integer, including products with repeated primes and integers outside the original support. No nonnegativity condition on the allowed factors is used in the definition.

For necessity assume \(1\le Q<Q_{\min}\), and put \(\tau=\log Q/\log P_*\). Choose nonnegative integers \(k_i\) with \(\sum_i k_i=m-1\), and prescribe
\[
 t_i=(k_i+1)\frac{\tau}{m+r-1},\qquad Q_i=P_*^{t_i}.
\]
This is a legal split, with each \(t_i<k_i+1\), hence \(\lfloor t_i\rfloor\le k_i\). The coefficient at \(P_*^m\) is \(1/m!>0\). Every possible factor contributing to it must be a power of \(P_*\) with exponent at most \(k_i\), because all factors are integers dividing \(P_*^m\). Their exponents can sum to at most \(m-1\), so no convolution term is present. Complex phases or cancellations in the factors cannot change an empty factorization. This necessity includes \(Q=1\) and gives exact sharpness, stronger than an exponent statement.

For fixed \(0<a<b\), Bertrand's postulate gives \(P_*\asymp Y^b\) for large \(Y\). Thus \(Y^{(m+r-1)b}\) is sufficient, and levels at most \(Y^{(m+r-1)b-\eta}\), for fixed \(\eta>0\), eventually fail whenever they are legal levels at all. If an argument deliberately restricts to squarefree products, the *necessity* also follows from any nonzero product of \(m\) distinct near-top primes: use the least prime in that product in place of \(P_*\) in the split. Such a necessity witness does not prove sufficiency for an arbitrary restricted coefficient. The exact sufficiency above is for the full coefficient of \(D^m\). An empty band instead gives the zero sequence, which meets every legal level.

## Pascadi's actual application and its limit

For \(m=4\), \(r=3\), set \(Q=Y^{6b}\). At the long-prime scale \(P\asymp Y^{1+4b}\) this level is admissible for Theorem 1.3(i) with a fixed exponent margin because
\[
 6b<\tfrac58(1+4b)\quad\Longleftrightarrow\quad b<5/28 .
\]
In particular the full interval \(1/8<b<1/6\) under study fits. One may take any fixed \(\varepsilon\) smaller than \(5/8-6b/(1+4b)\); the constants in \(P\asymp Y^{1+4b}\) are then harmless for large \(Y\). For a fixed nonzero residue \(a_0\), the source gives
\[
 \sum_{\substack{k\le Q\\(k,a_0)=1}}
 \lambda(k)\left(\pi(P;k,a_0)-\frac{\pi(P)}{\varphi(k)}\right)
 \ll_{\varepsilon,A,a_0} P(\log P)^{-A}.
\]
It is the signed weighted estimate (1.2), and its implicit constant is permitted to depend on \(a_0\). Multiplying the coefficient by a completely multiplicative \(v(k)\) with \(|v(k)|\le1\), such as \(k^{-1}\) or \(k^{it}\), preserves the convolution support and bounds. In contrast an arbitrary sharp dyadic restriction on \(k\) is not supplied by the factorability proof. For a fixed smooth compact modulus multiplier \(W(k/K)\), Fourier inversion in \(\log(k/K)\) expresses it as an integrable superposition of \(k^{it}\) multipliers; the fixed-residue theorem can then be integrated with cost the \(L^1\) norm of that Fourier transform. These observations concern the progression estimate at the stated long scale, not a claim at all smaller prime lengths.

The centered additive target has phases depending on \(k\) and on the residue being summed, such as \(e(-hc/k)\) on the class \(c\bmod k\). Applying the fixed-residue theorem separately for each possible \(c\) would lose the stated uniformity and cancellation, and inserting the \(k\)-dependent phase into the modulus weight does not preserve the completely multiplicative argument. Padding therefore repairs only the stated weight hypothesis. The minimal-level obstruction at \(Q\asymp Y^{4b}\) remains true, while the available fixed-residue theorem can now be used at a larger level with the requested weight. It supplies no new long-prime phase bound. No canonical records changed.
