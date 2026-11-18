# The long-prime Fourier mode and padded modulus weights

18 November 2026. The remaining coprime first-power prime term has a prescribed additive phase that varies with the product of four band primes. The Mellin representation and the proposed sufficient square bound retain this phase. An exact residue-array countermodel shows why two phase-blind progression norms cannot replace it. The normalized prime-product coefficient does meet Pascadi's factorability condition at a padded level, which corrects an inference in the earlier unadmitted working argument. Pascadi's fixed-residue conclusion remains different from the required phase estimate. This note adjudicates the stated algebra and functional implications. It establishes no estimate for the genuine long-prime sum and makes no novelty claim. [Long-prime formulation](prime117_long_prime_obstacle.md) · [Independent norm check](weighted119_blackbox_phase_review.md) · [Common-modulus check](analytic129_long_prime_adjudication.md) · [Padded theorem](prime137_padded_factorability.md) · [Independent padded check](geometry137_padded_factorability_review.md)

## The exact prime form

Let \(T\asymp Y\), \(1/8<b<1/6\), and \(D_Y(s)=\sum_{Y^a<p\le Y^b}p^{-s}\), with \(0<a<b\). Write \(a_k=[k^{-s}]D_Y(s)^4\), so \(0\le a_k\le24\). The arithmetic reduction precedes this note. After opening \(d_2*(\Lambda\log^2)\), a coprime prime factor \(p\) has weight \((\log p)^3\), and the divisor argument \(h\) has weight \(d_2(h)\). The dyadic scales \(k\asymp K,\ h\asymp D,\ p\asymp P\) satisfy \(DP\asymp KT\) on the actual cutoff. For \((p,k)=1\), set
\[
 q=\frac{k}{(h,k)},\qquad
 R_k(h,p)=e(-hp/k)-\frac{\mu(q)}{\varphi(q)},\quad e(u)=e^{2\pi i u}.
\]
The average of \(e(uhp/k)\) over units \(u\bmod k\) equals \(\mu(q)/\varphi(q)\). To check all gcd blocks, reduce the unit group modulo \(q\) by the surjective map with constant fiber size. Multiplication by \(hp/(h,k)\) is a permutation of the resulting units. At \(q=1\) the difference vanishes exactly. This statement puts no unit restriction on \(h\). The coprime square-prime phase is a distinct stratum. [Fixed arithmetic sequence](prime98_fixed_arithmetic_sequence.md) · [Removed strata](prime101_coprime_prime_strata.md) · [Inverse-prime regions](prime113_uniform_voronoi_envelope.md)

Group the four ordered band-prime factors as two ordered pairs. If \(\alpha_r,\beta_s\) count the two pairs, then \(a_k=\sum_{rs=k}\alpha_r\beta_s\), and each pair coefficient is at most 2. This includes repeated primes. Separate interval restrictions on the four slots also fit this representation. For coprime \(r,s\), write \(\overline{s}\bmod r\) and \(\overline{r}\bmod s\) for the two inverses. By CRT, \(s\overline{s}+r\overline{r}\equiv1\pmod{rs}\), giving
\[
 e(-hp/(rs))
 =e(-hp\overline{s}/r)\,e(-hp\overline{r}/s).
\]
The two factors each depend on the other modulus, so the identity preserves the coupled phase. When \(r,s\) have common factors, retain the original \(R_{rs}\). Neither these phase identities nor the pair counting impose pairwise coprimality on the actual support. [Independent CRT check](weighted119_blackbox_phase_review.md)

Let \(w_T\) be the smooth cutoff at height scale \(T\), of transition width \(H=T^\kappa\), and \(W(u)=w_T(Tu)\), with support in a fixed compact subinterval of \((0,\infty)\). Mellin inversion of \(W(2\pi hp/(Tk))\) gives the phase-preserving form
\[
 \mathcal B_{K,D,P}(t)=
 \sum_{\substack{r,s\\K<rs\le2K}}
  \frac{\alpha_r\beta_s}{(rs)^{1-it}}
 \sum_{h\asymp D} d_2(h)h^{-it}
 \sum_{\substack{p\asymp P\\(p,rs)=1}}
    (\log p)^3p^{-it} R_{rs}(h,p).
\]
Its Mellin multiplier is \(\widetilde W(it)(2\pi/T)^{-it}\,dt/(2\pi)\), where \(\widetilde W(s)=\int W(u)u^{s-1}du\). Neither the dyadic product condition nor the unit subtraction is lost. With \(\delta=H/T\), logarithmic-coordinate integration by parts gives
\[
 |\widetilde W(it)|\ll_j(1+\delta|t|)^{-j},
 \qquad \int_{\mathbb R}|\widetilde W(it)|\,dt\ll\delta^{-1}.
\]
For a fixed small \(\epsilon>0\), choose \(1-\kappa<\epsilon/2\). The portion \(|t|>T^\epsilon\) is negligible to any fixed power using a sufficiently high fixed derivative order and the polynomial triangle bound for the underlying sums. This choice of \(\kappa\) is compatible with the preceding smooth saddle comparison. Dyadic summation costs only fixed log powers. [Smooth saddle comparison](prime96_smooth_saddle_review.md)

An open sufficient input on each remaining block, uniformly for \(|t|\le T^\epsilon\), is
\[
 \sum_{k\asymp K}\sum_{h\asymp D}
 \left|
 \sum_{\substack{p\asymp P\\(p,k)=1}}
    (\log p)^3p^{-it}R_k(h,p)
 \right|^2
 \ll T^{2-\eta}K/D
\]
for some fixed \(\eta>0\). The \(k\)-sum can be restricted to the true modulus support. The coefficient norm in Cauchy–Schwarz is \(O(T^\epsilon\sqrt{D/K})\) by \(a_k\le24\), \(k^{-1}\asymp K^{-1}\) and the divisor bound. This gives \(O(T^{1-\eta/2+\epsilon})\) before the Mellin integral. The smoothing cost \(T^{1-\kappa}\) and dyadic logs are absorbed with \(1-\kappa+\epsilon<\eta/2\) and strict margin. The model square size \(KDP\), disregarding logarithms, is smaller than the unsaved right-hand size \(T^2K/D\) by the factor \(K^2/P\). This shows why a square estimate of that scale could suffice at \(P>K^2T^c\), \(c>0\). It is a comparison of budgets.

For \(D=1\), \(P\asymp KT\), the fractions \(1/k\) are separated by \(\gg K^{-2}\). The ordinary additive large sieve bounds the square sum of the uncentered prime polynomial by \((P+K^2)P\log^{O(1)}T\), of order \(P^2\) up to logs in this range. Removing \(p\mid k\) costs at most four terms per supported modulus. The unit mean is a separate explicit term. The large-sieve budget still exceeds \(T^{2-\eta}K\). This comparison does not give a lower bound for actual primes. [Phase square and large-sieve comparison](prime117_long_prime_obstacle.md)

## An exact limitation of two progression norms

A norm-only countermodel can be placed on actual supported moduli at the longest prime scale. Choose fixed \(0<c<d<1\) with \((d/c)^4<2\), let \(K=c^4Y^{4b}\), \(P=KT\), and take \(\mathscr S\) to consist of the products of four distinct primes in \((cY^b,dY^b]\). Unique factorization and the PNT give
\[
 S=|\mathscr S|\asymp K/\log^4T.
\]
Every \(k\in\mathscr S\) belongs to \((K,2K]\), is odd and squarefree, and has \(a_k=24\). On each such row put
\[
 A=\sqrt{P/S},\qquad
 f_k(u)=\cos(2\pi u/k)-\frac{\mu(k)}{\varphi(k)},\quad
 E_{k,u}=A f_k(u),\qquad (u,k)=1.
\]
Use zero errors on other rows. The unit mean is zero, and the variance of one cosine row is exactly
\[
 V_k=\sum_{u\bmod k}^{*} f_k(u)^2
    =\frac{\varphi(k)+c_k(2)}2-\frac{c_k(1)^2}{\varphi(k)}
    =\frac{\varphi(k)+1}2-\frac1{\varphi(k)}
    =(1/2+o(1))k,
\]
where \(c_k(j)\) is the Ramanujan sum. The last equality is uniform because every prime factor tends to infinity. The fictitious masses \(P/\varphi(k)+E_{k,u}\) are nonnegative for large \(T\), because \(P/\varphi(k)\ge T/2\) and \(|E_{k,u}|\le2A=O(\sqrt T\log^2T)\). Their total on each row remains \(P\).

They satisfy simultaneously
\[
 \sum_k\max_u|E_{k,u}|\ll\sqrt{PS}
    =o(P/\log^B T)\ \text{for every fixed } B,\qquad
 \sum_{k,u}^{*}|E_{k,u}|^2\asymp PK.
\]
Thus maximum errors with arbitrary fixed logarithmic savings and even the ideal total variance scale \(PK\) allow this array. Its real projection onto the needed \(h=1\) mode is exactly
\[
 \sum_k\frac{a_k}{k}
       \sum_u^{*}\cos(2\pi u/k)\,E_{k,u}
 =24A\sum_{k\in\mathscr S}\frac{V_k}{k}
 =(12+o(1))\sqrt{PS}.
\]
The imaginary projection vanishes by negation symmetry. Since \(K\asymp T^{4b}\) with \(4b>1/2\), this is of order \(K\sqrt T/\log^2T\) and exceeds the target \(T\log^4T\) by a factor tending to infinity. The comparison establishes the failure of an abstract implication from these norms and row conditions alone. [Independent positive-row and variance calculations](weighted119_blackbox_phase_review.md)

The array does not arise from one common data sequence across moduli. To see this concretely, take three eligible primes with product \(g\) and two other eligible primes \(v_1,v_2\). Both \(k_i=gv_i\) belong to \(\mathscr S\). CRT gives the following marginal of the fictitious masses onto a unit \(a\bmod g\):
\[
 \frac P{\varphi(g)}
 +A\mu(v_i)\left[
      \cos(2\pi a\overline{v_i}/g)-\frac{\mu(g)}{\varphi(g)}
   \right].
\]
Indeed summing the \(gv_i\)-cosine over its fiber factors out the exponential at \(a\overline{v_i}/g\), leaving the unit sum \(\mu(v_i)\). The constant subtraction has \(\varphi(v_i)\) copies and reduces by multiplicativity. At \(a=1\) the two marginals differ, since \(v_1,v_2\) are distinct, \(v_1+v_2<g\) for large \(Y\), and their inverse residues are therefore distinct up to sign. A common sequence supported on units of both moduli would give matching marginals on \(g\). In the genuine longest block every prime \(p\asymp KT\) is a unit of each \(k\asymp K\) once \(T\) is large. The countermodel thus cannot be used as an arithmetic lower bound or against an estimate exploiting cross-modulus compatibility. [Exact common-divisor marginal test](analytic129_long_prime_adjudication.md)

## Exact padded factorability

For a nonempty finite set of primes with largest prime \(p_*\), write \(D(s)\) for its prime polynomial and \(c_m(k)=[k^{-s}]D(s)^m\). For integers \(m,r\ge1\), the least \(r\)-way well-factorable level of \(c_m/m!\) is
\[
 Q_{\min}=p_*^{m+r-1}.
\]
Here the definition is that for every real split \(Q=\prod_{i=1}^r Q_i\) with \(Q_i\ge1\), the whole sequence is a Dirichlet convolution of \(r\) complex sequences, each bounded in modulus by 1 and supported at integers at most \(Q_i\). This is Pascadi's definition at \(r=3\). A level may strictly exceed the sequence's support. The zero sequence from an empty band meets every legal level. [Pascadi, Definition 1.1, p. 2](../../sources/prime117_references/pascadi.pdf)

For sufficiency write \(t_i=\log_{p_*}Q_i\). If \(Q\ge Q_{\min}\), then \(\sum_i\lfloor t_i\rfloor>\log_{p_*}Q-r\ge m-1\), so choose integers \(0\le n_i\le\lfloor t_i\rfloor\) with \(\sum_i n_i=m\). The coefficients of \(D^{n_i}/n_i!\) are 1-bounded: at a product with multiplicities \(v_p\) the normalized coefficient is \(1/\prod_p v_p!\). Their support is at most \(p_*^{n_i}\le Q_i\), and the \(n_i=0\) factor is a unit mass at 1. Their convolution equals \(c_m/\prod_i n_i!\). Multiply one factor by \(\prod_i n_i!/m!\le1\) to obtain \(c_m/m!\) exactly at every integer.

For necessity assume \(1\le Q<Q_{\min}\), choose nonnegative integers \(f_i\) with \(\sum_i f_i=m-1\), and take the split
\[
 t_i=(f_i+1)\frac{\log_{p_*}Q}{m+r-1},
 \qquad Q_i=p_*^{t_i}.
\]
Then \(0\le t_i<f_i+1\), so a factor of \(p_*^m\) at most \(Q_i\) can carry at most \(f_i\) copies of \(p_*\). No \(r\)-tuple in the prescribed supports can produce \(p_*^m\). Its target coefficient equals \(1/m!>0\). Thus no cancellation or choice of complex factors can meet the definition. This gives exact finite sharpness, including \(r=1\). If an argument restricts to distinct near-top products, the same necessity test with the least prime in one such product gives the asymptotic lower exponent, without establishing sufficiency of the restricted coefficient. [Two independent exact-level proofs](prime137_padded_factorability.md) · [Alternative split proof](geometry137_padded_factorability_review.md)

Multiplication by a completely multiplicative \(g(k)\) with \(|g(k)|\le1\) preserves the upper bound: multiply each convolution factor by \(g\). If \(g(p_*)\ne0\) then the lower bound also survives. This covers both \(k^{it}\) and \(k^{-1+it}\) at real \(t\). A sharp restriction \(K<k\le2K\), or multiplication by \(e(-a/k)\), does not follow from this argument. At fixed residue a smooth modulus multiplier \(W(k/K)\) can be integrated against the \(k^{it}\) hypotheses by Fourier inversion in \(\log(k/K)\), with the \(L^1\) norm of its transform. This observation supplies no estimate in the varying residue.

The unadmitted working inference from failure at \(Q\asymp Y^{4b}\) to failure of Pascadi's coefficient hypothesis was too broad. The minimal-support obstruction is valid at the specified level. Since \(p_*\le Y^b\), the full \(a_k/24\) is triply well-factorable at \(Q=Y^{6b}\). At the longest scale \(x\asymp P\asymp Y^{1+4b}\),
\[
 6b<\frac58(1+4b)\ \Longleftrightarrow\ b<\frac5{28},
\]
so all the bands \(1/8<b<1/6\) fit Theorem 1.3(i) with a fixed positive exponent margin. For a smaller modulus scale \(K\asymp T^\vartheta\), admissibility of this same padded level needs the separate check \(6b<(5/8)(1+\vartheta)\). The theorem's signed conclusion applies at the padded level to the full factorable weight for a fixed nonzero residue \(a\). Its implied constant may depend on \(a\). [Pascadi, Theorem 1.3(i), p. 2](../../sources/prime117_references/pascadi.pdf) · [Transparent working-note correction](prime117_long_prime_obstacle.md)

The needed progression combination has \(e(-ha/k)\) tied to each \(k\) and sums over all unit \(a\bmod k\). Pascadi's theorem supplies no estimate for that simultaneous varying residue and Fourier mode. Matomäki's adjacent exponential-sum theorem retains a common \(\alpha\) in \(e(\alpha jn)\), with an independent multiplier \(j\) and fixed progression residue; it does not give the varying reciprocal choice \(\alpha j=-h/k\) coupled to the modulus. The exact padded weight theorem and the phase-sensitive open estimate therefore remain distinct. [Matomäki, Theorem 1 and Corollary 3](../../sources/prime117_references/matomaki.pdf)
