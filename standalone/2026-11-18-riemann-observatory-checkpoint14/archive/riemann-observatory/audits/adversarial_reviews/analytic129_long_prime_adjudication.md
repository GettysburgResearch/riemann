# Third check of the long-prime phase and progression-norm limitation

The single prescribed Fourier mode can be large for nonnegative, unit-centered residue arrays obeying both abstract progression budgets. The construction uses actual four-prime-supported moduli in one dyadic block. The array is inconsistent with a common sequence across those moduli, as an explicit common-divisor marginal test below shows. The genuine arithmetic sum and the proposed square estimate remain open. [Product-phase note](prime117_long_prime_obstacle.md) · [Independent review](weighted119_blackbox_phase_review.md)

## Supported rows and exact budgets

Fix constants \(0<c<d<1\) with \((d/c)^4<2\), set \(K=c^4Y^{4b}\), \(P=KT\), and let \(\mathcal S\) be all products of four distinct primes from \((cY^b,dY^b]\), with \(T\asymp Y\) and \(0<a<b\) fixed. For large \(Y\), those primes lie in the stated band \((Y^a,Y^b]\). Every such product lies in the **same** block \((K,2K]\), is odd and squarefree, and has fourth-power coefficient \(a_k=4!\) by unique factorization. The PNT with the fixed constants \(c,d\) gives \(N\sim(d-c)Y^b/(b\log Y)\) eligible primes and \(S=\binom N4\asymp K/\log^4T\) distinct moduli. In particular the construction is valid on an actual supported family; no prime estimates for residue classes are used.

Set \(A=\sqrt{P/S}\). On \(\mathcal S\) put
\[
 r_k(u)=\cos(2\pi u/k)-\mu(k)/\varphi(k),\qquad E_{k,u}=A r_k(u)
 \quad (u\bmod k,\ (u,k)=1),
\]
and use zero errors on the other rows. The Ramanujan sum gives exact zero unit mean. Also \(k\) is odd and has four distinct prime factors, so \(c_k(1)=c_k(2)=\mu(k)=1\), where \(c_k(j)\) here denotes a Ramanujan sum. Thus
\[
 \sum_{u\bmod k}^*r_k(u)^2
 =\frac{\varphi(k)+1}{2}-\frac1{\varphi(k)}
 = (1/2+o(1))k
quad (k\in\mathcal S).
\]
The uniform asymptotic follows since every factor exceeds \(cY^b\). The positive baseline \(P/\varphi(k)\ge T/2\) dominates \(|E_{k,u}|\le2A=O(\sqrt T\log^2T)\); every resulting row has total \(P\). The budgets for the block are
\[
 \sum_k\max_u|E_{k,u}|\ll\sqrt{PS},\qquad
 \sum_{k,u}^*|E_{k,u}|^2\asymp PK .
\]
The first is \(o(P\log^{-B}T)\) for each fixed \(B>0\), since \(\sqrt{PS}/P\asymp T^{-1/2}\log^{-2}T\). The second can meet any prescribed positive constant in an upper bound \(\ll PK\) by reducing \(A\) by a fixed positive factor. These are block budgets at a common endpoint. Extending the row errors by zero to other moduli preserves these budgets without assigning them any prime-counting interpretation. One can also make individually monotone fictitious endpoint profiles by multiplying each row's baseline and errors by the same nondecreasing scalar from zero to one. This does not impose cross-modulus consistency.

The real phase pairing is
\[
 \sum_k\frac{a_k}{k}\sum_{u\bmod k}^*\cos(2\pi u/k)E_{k,u}
   = 24 A\sum_{k\in\mathcal S}\frac1k\sum_u^*r_k(u)^2
   = (12+o(1))\sqrt{PS}.
\]
The imaginary part of the exponential pairing vanishes by negation symmetry. Since \(\theta=4b>1/2\), division by \(T\log^4T\) gives order \(T^{\theta-1/2}/\log^6T\to\infty\). This comparison uses the scale \(P=KT\) and holds with any fixed comparable positive constants. It is a limitation on an implication from norm budgets, even with row positivity and centering. It does not assert a lower bound for the smooth genuine-prime sum.

## Explicit incompatibility across moduli

Choose three eligible primes with product \(g\), and two other eligible primes \(v_1,v_2\). Both \(k_i=gv_i\) lie in \(\mathcal S\). For a unit \(a\bmod g\) sum the artificial nonnegative masses over unit classes \(u\bmod gv_i\) restricting to \(a\bmod g\). CRT gives the exact result
\[
 \frac P{\varphi(g)}+
 A\mu(v_i)\left[
 \cos(2\pi a\overline{v_i}/g)-\frac{\mu(g)}{\varphi(g)}
 \right],
\]
because the exponential contributes \(e(a\overline{v_i}/g)\) times a Ramanujan sum \(\mu(v_i)\), and the row-constant subtraction has \(\varphi(v_i)\) copies. At \(a=1\) the cosine values differ. In fact \(v_1\ne v_2\), and \(v_1+v_2<g\) for large \(Y\), so their residues and inverse residues are distinct up to sign modulo \(g\). A common weighted sequence supported on units of both moduli must instead give identical marginals on \(g\). In the actual prime block \(p\in(P,2P]\) every prime is a unit of every \(k\asymp K\) for sufficiently large \(T\). Therefore this is a concrete incompatibility with any such common sequence. A theorem using shared arithmetic data or signed correlations lies outside the scope of the row-norm example.

## Mellin form and the sufficient square estimate

For the genuine prime terms put \(g=(h,k)\), \(q=k/g\) and \(p\nmid k\). Reduction sends units of \(k\) onto units of \(q\) with constant fiber size, and multiplication by \(p(h/g)\) permutes the latter. Hence the centered phase is exactly
\[
 R_k(h,p)=e(-hp/k)-\frac{\mu(q)}{\varphi(q)}.
\]
At \(q=1\) it is zero. There is no assumption that \(h\) is coprime to \(k\). Factoring the fourth-power coefficients by two ordered pairs gives \(a_k=\sum_{rs=k}\alpha_r\beta_s\), each count at most two. This includes repeated primes. It also works if each slot has its own interval restriction, since the decomposition preserves their order.

Let \(W(u)=w_T(Tu)\) and use \(\widetilde W(s)=\int_0^\infty W(u)u^{s-1}du\). Mellin inversion at real part zero on the fixed positive support gives
\[
 w_T(2\pi hp/k)=\frac1{2\pi}\int_{\mathbb R}
 \widetilde W(it)(2\pi/T)^{-it} k^{it}h^{-it}p^{-it}dt.
\]
Inserting it preserves the product condition \(K<rs\le2K\), both pair coefficients, the outer \(1/(rs)\) and the actual centered phase. If \((r,s)=1\), then \(s\overline s+r\overline r\equiv1\pmod {rs}\) and the additive phase is \(e(-hp\overline s/r)e(-hp\overline r/s)\). This identity keeps dependence on the other modulus in both factors. In the dual inverse-prime case the corresponding factors are \(e(\pm l\overline{ps}/r)e(\pm l\overline{pr}/s)\), whenever \(p\) is a unit. The identities need neither \(h\) nor \(l\) to be a unit. Noncoprime pairs retain the original kernel, and having two ordered pair weights does not imply unrestricted well-factorability.

Logarithmic-coordinate integration by parts, using the compact support and derivatives at scale \(\delta=H/T\), gives \(|\widetilde W(it)|\ll_j(1+\delta|t|)^{-j}\) and an \(L^1\) cost \(O(\delta^{-1})\). Polynomial triangle bounds are sufficient to drop \(|t|>T^\epsilon\) to any fixed power after choosing \(1-\kappa<\epsilon/2\) and a large fixed derivative order. On the surviving dyadic blocks \(DP\asymp KT\), Cauchy–Schwarz in \((k,h)\) has coefficient norm \(O(T^\epsilon\sqrt{D/K})\) because \(a_k\le24\), \(1/k\asymp1/K\) and \(d_2(h)\ll_\epsilon T^\epsilon\). Hence the proposed sufficient input is
\[
 \sum_{k\asymp K}\sum_{h\asymp D}
 \left|\sum_{p\asymp P,\ p\nmid k}
    (\log p)^3p^{-it}R_k(h,p)\right|^2\ll T^{2-\eta}K/D
\]
uniformly in the retained Mellin range, for fixed \(\eta>0\). It bounds the inner product by \(T^{1-\eta/2+\epsilon}\) before smoothing, so \(1-\kappa+\epsilon<\eta/2\) and a small margin for block count suffice. A model budget \(KDP\) has ratio to the un-saved target \(T^2K/D\) of order \(K^2/P\), which explains the stated comparison for very long prime blocks and supplies no estimate on actual phases. At \(D=1\), the ordinary additive large sieve budget \((P+K^2)P\) is of order \(P^2\) in this range. This is an upper-bound comparison, with no lower bound implied for the true sums.

## Bounded adjacent-source check

I checked Pascadi v2, Definition 1.1 and Theorem 1.3, and Matomäki’s author manuscript, Theorem 1 and Corollary 3, against the local source manifest. Pascadi's fixed-residue theorem assumes triply well-factorable weights in its \(5/8-\epsilon\) branch. For the supported weights here, choose a legal split with first factor bound \(Q_1=Y^{a/2}\). The first divisor of every supported product must then be 1, and the other two factors cannot reach beyond \(Q/Q_1\). This is incompatible with the nonzero weights at scale \(Q\asymp Y^{4b}\). Matomäki retains a shared \(\alpha\) in \(e(\alpha jn)\), with the multiplier \(j\) separate from the averaged progression modulus and a fixed residue. It does not give the centered sum with frequency \(-h/k\) attached to the same \(k\). These are checks of the named hypotheses, with no assertion about other available dispersion estimates. The array and product-phase deductions above do not rely on either source. No adjacent-source admission or canonical record change is made. [Pascadi v2](../../sources/prime117_references/pascadi.pdf) · [Matomäki manuscript](../../sources/prime117_references/matomaki.pdf) · [Source pins](../../sources/prime117_references/SHA256SUMS)
