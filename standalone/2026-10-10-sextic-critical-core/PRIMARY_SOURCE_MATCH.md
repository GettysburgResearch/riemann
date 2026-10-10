# Primary-source matching for the reunited Gauss series

**Status:** bounded source audit, 2026-10-10. No theorem directly controlling the exact deformed series below was established among the examined sources. This is a failure to establish a coefficient match and the required uniform estimates, not a theorem that no such match exists.

The relevant object is the unreindexed squarefree theta series from [REUNITED_RAMANUJAN_EULER_PRODUCT.md](REUNITED_RAMANUJAN_EULER_PRODUCT.md). Its coefficient is

\[
\gamma_2(n)\rho(n)\vartheta(n)\alpha(n)\chi_k(n)^3
\mathcal E_{k,n}(w,v),
\qquad
\vartheta(n)=\overline{\chi_n(\lambda)}^{\,2},
\tag{1}
\]

and its Dirichlet weight is \((Nn)^{-s}\), with
\(r=3s-\tfrac12\) and \(v=w+r-1\). The outer index \(n\) is squarefree outside the fixed bad-prime set. The angular factor has type \(+1\); the quadratic character \(\chi_k^3\), all its nonunit zeros, and the finite bad-ray components remain. The product preceding this series is
\(L_S(r,\chi^+)L_S(v,\kappa_k)/L_S(w,\chi^-)\).

## 1. Exact OpenAI family 023 inputs examined

The pinned source is OpenAI/math commit
\( \texttt{adc7f1241b42e322a6451854ab7e4b4c146bf78a} \),
*An unconditional first moment for cubic Gauss sums*, September 25, 2026.

| Primary source | Git blob | SHA256 |
|---|---|---|
| [build/sections/dual.tex](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/build/sections/dual.tex) | 8dcddce96894146ca745b8227c922c34f5990dcf | 1209fd17cee79f4a21b71d66d3d8b60b210216fa783ec555959d2ebff2fba483 |
| [build/sections/background-type1.tex](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/build/sections/background-type1.tex) | 3d31d5791ef3cf55c9608066997f9dc6c6bb861a | 1c7be908c862dc440772964cfdd59e095e7b0f079cec11d99f5c7a9644198dd1 |

The pinned source links, Git blobs and content hashes bind the sources examined; SOURCE_LOCK.json independently records the same paths and bytes.

In dual.tex, equation label eq:prime-convolution and Proposition label prop:dual specify bounded-order convolutions of large prime sequences. Each prime factor is at least a fixed power of the total length, and each has an independently specified smooth norm weight. Equation eq:exceptional-moment proves a saving only for that class and the stated small auxiliary parameters. Coefficient (1) is not shown to belong to this class.

In background-type1.tex, Theorem label thm:hb-height concerns precisely
\[
f_r(s)=\sum_uG(ru)(Nu)^{-s},
\]
and explicitly uses angular index zero. Theorem thm:voronoi-background is a completed level summation formula. These are useful analytic building blocks; neither states an estimate for the deformation \(\mathcal E_{k,n}(w,v)\). In particular, multiplying their coefficients by an arbitrary divisor-dependent weight is not authorized by their hypotheses.

## 2. The periodic theta building block has a wider scope

The primary reference is Dunn–Radziwiłł, [Bias in cubic Gauss sums: Patterson's conjecture, arXiv:2109.07463v3](https://arxiv.org/html/2109.07463v3).

Section 5.3, Lemma 5.2 and Corollary 5.1, treats periodic twists of completed theta coefficients, with an explicit Fourier-support condition. Section 5.4, Proposition 5.1, gives continuation and a functional equation with integer angular indices. Thus a nonzero angular mode, or a noncubic finite character considered through the periodic-twist framework, is not by itself a fundamental obstruction.

The more specialized squarefree Gauss-series statement, Proposition 5.2 in Section 5.5, assumes a cubic twisting character. Applying the general completed-theta statement to a different character requires the appropriate completion, Fourier-support conditions, ramified normalization and conductor dependence. None may be omitted merely because the coefficients contain cubic Gauss sums.

The decisive additional issue here is that \(\mathcal E_{k,n}\) changes at every prime dividing the summation index \(n\). Across the full series this is neither one fixed periodic twist nor a fixed finite collection of modified Euler factors. The general theta statement therefore does not, without a further summability argument, continue or bound the series with coefficient (1).

## 3. Multiple Dirichlet series require an exact coefficient system

The primary reference is Chinta–Gunnells, [Constructing Weyl group multiple Dirichlet series, arXiv:0803.0691](https://arxiv.org/pdf/0803.0691).

Their Section 4 defines the coefficients through the specified prime-power polynomials, equation (4.2), and twisted multiplicativity, equation (4.3). The local functional equation of Theorem 4.1 supplies a load-bearing step. The continuation and Weyl-group functional equations in Theorem 6.1 apply to the series constructed with that coefficient system.

The reunited local factors have not been identified with those coefficients or shown to satisfy their local functional equations. A cubic Gauss factor and an Euler correction alone do not establish such an identification. This audit therefore does not import Theorem 6.1 as a continuation theorem for (1).

## 4. The remaining deformation can be isolated exactly

Retain the companion note's variables
\[
x_p=\chi^-(p)q^{-w},\qquad z_p=\kappa_k(p)q^{-v},
\qquad q=Np.
\]

Initially assume \(\Re w>1\) and \(\Re r>1\), hence \(\Re v>1\). Then
\[
|x_p|+|z_p|<2/q\le1,
\]
so \(1-x_p+z_p\), \(1-x_p\), and \(1-z_p\) are nonzero. The normally convergent product \(\mathcal E_{k,1}\) is also nonzero in this region. For squarefree \(n\), direct division of the exact local factors gives
\[
\frac{\mathcal E_{k,n}(w,v)}{\mathcal E_{k,1}(w,v)}
=\prod_{p\mid n}\frac{1+(q-1)x_p}{1-x_p+z_p}
=\sum_{d\mid n}h_{k,w,v}(d),
\tag{2}
\]
where \(h\) is multiplicative on squarefree ideals and
\[
h_{k,w,v}(p)=\frac{q x_p-z_p}{1-x_p+z_p}.
\tag{3}
\]

All masks remain: \(h(p)=0\) when the original characters vanish at \(p\). Equation (2) is a finite divisor identity for each \(n\). Termwise expansion of the full outer series is justified, for example, in the explicit initial region \(\Re s>1,\Re w>1\), with \(r=3s-\tfrac12\), because both the original and absolutely expanded sums converge there. No division by \(1-x_p+z_p\) is asserted on the companion note's entire enlarged domain, where that expression can vanish.

Writing \(n=dm\) in this initial region produces infinitely many divisor-conditioned Gauss series. Gauss CRT adds the corresponding cubic cross-symbol, and the row character and coprimality restrictions must remain. The analytic level now involves the moving \(d\), in addition to \(k\) and the fixed bad primes.

The local numerator \(q x_p\) has size \(q^{1-\Re w}\) at good primes. Near the desired region this can grow, so summing conductor-dependent bounds term by term is not an automatic absolutely convergent operation. A usable next theorem must either control these moving-level series with a summable cost, or identify the entire coefficient system with an established multiple Dirichlet series and prove the required uniform bound there.

The source comparison identifies this precise missing interface. It supplies neither a new contour shift through the reunited polar divisor nor a higher-moment estimate.
