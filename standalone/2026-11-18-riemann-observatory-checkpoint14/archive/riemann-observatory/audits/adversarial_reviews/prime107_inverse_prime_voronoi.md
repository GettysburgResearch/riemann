# A published inverse-prime estimate removes a band of the smooth twist

18 November 2026. Baker's averaged Kloosterman-fraction estimate and divisor Voronoi summation control a power-width neighborhood of the prime-factor scale \(p=T/K\) on modulus blocks \(k\asymp K\) away from both exponent endpoints \(1/2\) and \(2/3\). This extends the short-factor removal in prime101 on these blocks. It leaves longer prime factors and does not by itself prove the fourth moment. [Fixed sequence](prime98_fixed_arithmetic_sequence.md) · [Prior short-factor cutoff](prime101_coprime_prime_strata.md)

## Character Dirichlet series and the obstruction to a single GL(2) transform

On the full unit block \((m,k)=1\), the nonprincipal additive factor is
\[
 \frac1{\varphi(k)}
 \sum_{\substack{\chi\bmod k\\\chi\ne\chi_0}}\tau(\bar\chi)\chi(-m).
\]
The character-twisted series of \(d_2*(\Lambda\log^2)\) is exactly
\[
 L(s,\chi)^2\,\bigl(-L'(s,\chi)/L(s,\chi)\bigr)''
\]
in the domain of absolute convergence, including imprimitive characters with the corresponding missing Euler factors. This is the square of the Dirichlet \(L\)-function times a differentiated logarithmic derivative of its degree-one factor. At a simple zero \(\rho\), its residue is \(-2L'(\rho,\chi)^2\), since the twice differentiated negative logarithmic derivative has leading term \(-2(s-\rho)^{-3}\). At a zero of multiplicity \(j\ge2\) the local exponent \(2j-3\) is nonnegative. Thus a Mellin move on the whole character-twisted coefficient sequence has additional zero residues whenever simple zeros are crossed. The standard Eisenstein or divisor Voronoi equation alone does not evaluate this product. One can instead freeze the prime factor and transform the two free divisor variables as follows.

## Primary source and exact phase match

Baker, *Kloosterman sums with prime variable*, Acta Arith. 156 (2012), pp. 351–372, Theorem 2 on p. 352, gives
\[
 \sum_{K<k\le2K}\max_{(A,k)=1}
 \left|\sum_{\substack{x<p\le2x\\(p,k)=1}} e(A\bar p/k)\right|
 \ll_\epsilon (K^{11/10} x^{4/5}+K x^{11/12}) K^\epsilon,
 \qquad K^{1/2}\le x\le2K.
\]
Here the theorem is for all integer moduli in the dyadic block. The prime sum in its definition is dyadic. By decomposing a prefix \(p\le t\) into dyadic intervals with lower endpoint at least \(K^{1/2}\), the same bound holds with \(x\) replaced by \(t\), plus \(O(K^{3/2})\) for the bottom prefix. For \(t\ge K^{1/2}\) the first term already dominates that loss. This inference is pointwise in a common \(t\), enough for integrated partial summation. [Primary journal PDF](https://www.impan.pl/shop/en/publication/transaction/download/product/82065)

Blomer–Harcos–Michel, *Bounds for modular L-functions in the level aspect*, §2.3, equations (2.25)–(2.27), pp. 708–709, gives the exact smooth divisor Voronoi formula at every integer modulus \(k\), for \((v,k)=1\). Its main term is independent of \(v\), and its two dual sums have phase \(e(\pm\bar v\,l/k)\) with kernels \(J^-(z)=-2\pi Y_0(4\pi z)\) and \(J^+(z)=4K_0(4\pi z)\). Freeze a prime \((p,k)=1\) in the remaining convolution and use \(v=-p\) or \(v=up\) for unit \(u\). The unit-average subtraction cancels the main term exactly. On the dual side, averaging \(\overline{up}\) over \(u\) gives the normalized Ramanujan sum \(c_k(l)/\varphi(k)\), independent of \(p\). The two remaining phases are \(e(\pm l\bar p/k)\). Both signs are covered by Baker whenever \(l\) is coprime to \(k\). [Primary journal PDF](https://www.numdam.org/item/10.1016/j.ansens.2007.05.003.pdf)

## A transition band with a power saving

Fix \(1/2<\vartheta_-<\vartheta_+<2/3\) and consider dyadic blocks \(T^{\vartheta_-}\le K\le T^{\vartheta_+}\). The prescribed arithmetic band ensures each prime factor of \(k\) with \(a_k\ne0\) is larger than \(Y^a\), and \(0\le a_k\le24\). Take fixed \(\eta>0\) sufficiently small in terms of the endpoint gaps and \(a\), in particular \(6\eta<a\), and choose the transition width so that \(\Delta=H/T\ge T^{-\eta}\), while \(H=o(T)\) by a fixed power. For \(p\asymp P\) with
\[
 T^{1-\eta}/K\le P\le T^{1+\eta}/K,
\]
put \(M=kT/p\). After changing the Voronoi integration variable to \(x=Mu\), the weight on the term with dual index \(l\), including the outer \(1/k\), is
\[
 B_{k,l}^{\pm}(p)
   =\frac{M}{k^2}\int_0^\infty w_T(2\pi T u)
                  J^\pm\left(\frac{\sqrt{lMu}}{k}\right)\,du.
\]
The \(u\) support is fixed and positive. The logarithmic prime coefficient is \((\log p)^3\).

The effective dual variable is \(lM/k^2\asymp lT/(KP)\). For \(l>T^{6\eta}\), the kernel argument on the weight support is \(\gg\sqrt l\,T^{-\eta/2}\), so its product with \(\Delta\) is \(\gg T^{3\eta/2}\). The \(K_0\) transform decays exponentially. The large-argument \(Y_0\) expansion gives phases \(\pm4\pi\sqrt{lM}\sqrt u/k\) with symbol of order \((\sqrt{lM}/k)^{-1/2}\). Integrating by parts \(j\) times gains \((\Delta\sqrt{lM}/k)^{-j}\) uniformly in \(k,p,l\). This uses fixed support, \(O_j(\Delta^{-j})\) derivatives of \(w_T(2\pi T u)\), and the nonvanishing derivatives of \(\sqrt u\). Since the gain also decays as \(l^{-j/2}\), summing over \(l>T^{6\eta}\) with \(d_2(l)\ll_\epsilon l^\epsilon\), and over \(k,p\) absolutely, gives arbitrary fixed power savings on increasing \(j\). [Bessel asymptotics](https://dlmf.nist.gov/10.17) · [Modified Bessel asymptotics](https://dlmf.nist.gov/10.40)

For \(l\le T^{6\eta}\), every \(k\) in the actual coefficient support is coprime to \(l\). The kernel arguments lie between fixed multiples of \(T^{-\eta/2}\) and \(T^{7\eta/2}\). For either kernel, \(|J(z)|+|zJ'(z)|\ll1+|\log z|+z^{1/2}\), by the small-argument series and large-argument asymptotics. Because \(p\,dM/dp=-M\), differentiating the integrand through the change of scale gives
\[
 |B_{k,l}^{\pm}(p)|+P|\partial_p B_{k,l}^{\pm}(p)|
 \ll T^{3\eta}\log T.
\]
Indeed \(M/k^2\ll T^\eta\) and the \(z^{1/2}\) bound costs at most \(T^{7\eta/4}\). The taper is independent of \(p\) in this representation, so this derivative does not cost \(T/H\). Including \((\log p)^3\) costs a fixed log power. For \(p\in[P,2P]\) the prefix decomposition for Baker is valid, since the strict exponent margins make \(P\gg K^{1/2}\) and \(2P\ll K\). Use Abel summation for each \(k,l\), bounding the endpoint and the \(p\)-integral by the displayed common weight envelope. At each common integration endpoint apply the averaged Baker bound. This step does not sum the supremum over different endpoints for each modulus. The Ramanujan-subtraction term in this short dual range costs at most \(O(P)\) times the common weight envelope after summing \(k\), since \(|c_k(l)|/\varphi(k)\ll1/k\) on the four-prime support. Summing \(l\le T^{6\eta}\) with its divisor coefficient, the full bound for each block is
\[
 \ll_\epsilon T^{9\eta+\epsilon}
       \bigl(K^{11/10}P^{4/5}+K P^{11/12}+P\bigr)+O_A(T^{-A}).
\]
Using \(P\le T^{1+\eta}/K\), the first two exponents are at most
\(4/5+3\vartheta_+/10+10\eta+\epsilon\) and
\(11/12+\vartheta_+/12+10\eta+\epsilon\). Both are strictly less than 1 with sufficiently small fixed \(\eta,\epsilon\). The same holds for the \(P\) term, and the dyadic sum costs only logarithms. Thus this stratum contributes \(O(T^{1-c})\) for some \(c>0\). The proof applies by the same Abel summation to a sliced interval within a dyadic \(P\) block when its endpoints are common across the moduli in the block.

Choosing additionally \(1-\kappa\ll\eta\), the earlier gcd-sensitive Poisson cutoff for coprime primes reaches past \(T^{1-\eta}/K\). The new and old bounds overlap on these modulus blocks. The new upper cutoff \(T^{1+\eta}/K\) is polynomially beyond \(T/K\).

## Limits of the primary estimates checked

Baker does not cover prime-square inverse phases \(e(\pm l\bar p^2/k)\), or even the prime-phase ranges with long dual \(l\) where coprimality and the dual weight budget require a new argument. For the square question, Ren, *On exponential sums over primes and application in Waring–Goldbach problem*, equation (1.4), p. 786, explicitly records Ghosh's different estimate for the **direct** quadratic phase with exact rational numerator. Separate arithmetic opening of the divisor variable is needed to exploit it. Ghosh's original is *The Distribution of \(\alpha p^2\) Modulo 1*, Proc. LMS 42 (1981), pp. 252–269. I checked Ren's primary article at the cited equation and the journal record for Ghosh. [Ren PDF](https://files.sciengine.com/pdfs/1006-9283/j3LzycXF2bBF4Z3tC.pdf) · [Ghosh journal record](https://doi.org/10.1112/plms/s3-42.2.252)

For linear phases, Ren's Corollary 1.2 directly gives the classical pointwise budget \(X^{1/2}k^{1/2}+X^{4/5}+Xk^{-1/2}\) up to divisor and log factors for \(X\)-length primes at unit rational \(a/k\). On the divisor-argument-1 block \(X\asymp kT\), taking absolute values over the actual moduli leaves \(K\sqrt T\) from the first term. This agrees with the triangle obstruction in prime101. [Ren PDF, p. 786](https://files.sciengine.com/pdfs/1006-9283/j3LzycXF2bBF4Z3tC.pdf)

The progression estimates have different weights. Maynard III, Theorem 1.1, permits \(\sup_a\) in specially factorized moduli just above \(x^{1/2}\) at cost of a weak error, and Theorem 1.2 permits arbitrary-log savings with a residue compatibility across one modulus factor. Lichtman, Corollary 1.5, handles a fixed residue class \(a\) and triply well-factorable weights up to \(x^\vartheta,\ \vartheta<66/107\). The ability to split our \(k\)'s into four chosen prime factors does not imply well-factorability at every prescribed factor-length split. For example, choose a split with first factor bound \(Q_1<Y^a\) and \(Q_1>1\). Any nonzero convolution coefficient corresponding to a supported modulus must then use first factor 1, so it cannot reach moduli above \(Q/Q_1\). Our support contains products of four distinct near-top primes, of size \(\asymp Q\) at level \(Q\asymp Y^\theta\). More basically, the exponential twist is the sum over all reduced residue classes with their oscillating phases. A maximum progression error bound would cost \(\varphi(k)\) on taking absolute values over those classes. Neither theorem gives the phase-weighted averaging used in the argument above. [Maynard III, primary preprint, Theorems 1.1–1.2](https://arxiv.org/pdf/2006.08250) · [Lichtman, primary preprint, Definition 1.4 and Corollary 1.5](https://arxiv.org/pdf/2309.08522)

[Local primary PDFs, text extracts, and version records](../../sources/prime107_references/README.md)
