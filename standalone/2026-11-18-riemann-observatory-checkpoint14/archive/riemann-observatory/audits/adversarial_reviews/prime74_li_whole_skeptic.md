# Independent whole-work audit of Li’s 1997 positivity criterion

18 November 2026. Work PAPER-E008, Xian-Jin Li, *The Positivity of a Sequence of Numbers and the Riemann Hypothesis*, J. Number Theory **65** (1997), 325–333, DOI 10.1006/jnth.1997.2137, PII S0022314X97921375. I read all nine journal pages, including both proofs, both Dedekind lemmas, the closing remark and the references. Both theorem statements hold. The rendered text confirms a nonvanishing-symbol slip in the proof of Lemma 3.1 and a normalization mismatch in the Dedekind theta integral as written. Both have local repairs. The main positivity argument survives. This report supplies an independent reconstruction and does not change the work’s canonical coverage record. [Journal-rendered copy from the mirror](../../sources/prime74_li_whole/li1997_journal_rendered_mirror.pdf) · [Publisher record](https://www.sciencedirect.com/science/article/pii/S0022314X97921375)

## Copy identity and access limits

The preserved PDF is 706,759 bytes, SHA-256 `8f5719751f869d71907c9da75270cb8c012b54f1453f54179461dbc331d255a1`. It is a journal-typeset PDF, with explicit original volume and article number, consecutive printed pages 325–333, original receipt and revision dates, and original publisher copyright. Metadata has title, author Li X.-J., subject Journal of Number Theory, Distiller on Macintosh, creation July 14, 1997, and modification April 29, 2015. It has no encryption. The public Paperzz landing page embeds a viewer iframe with a signed `file` pointer. The pointer in the loaded public HTML returned a PDF directly; the ordinary mirror download endpoint returned HTTP 403. The signed value is not preserved here. This is a recovered exact-rendering journal manifestation through a third-party mirror. Publisher-hosted delivery and byte identity with present publisher servers were not verified. The DOI retrieval was forbidden through the web service and the publisher PDF/API attempts supplied no file. Targeted title and author searches supplied the same journal record or mirror, and no distinct author manuscript was verified. The older full HTML extraction is independently pinned but less reliable for notation. [Public mirror](https://paperzz.com/doc/7086946/--science-direct) · [Older HTML extraction](../../sources/li_original_round2/li1997_paperzz_tool_response.json)

## Definitions, branch choice, and exact radius

On pp. 325–328 the completion is \(\Xi(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)\), twice the commonly normalized xi. Section 2 sets \(Z_k(s)=G_1(s)^{r_1}G_2(s)^{r_2}\zeta_k(s)\), with \(G_1(s)=\pi^{-s/2}\Gamma(s/2)\), \(G_2(s)=(2\pi)^{1-s}\Gamma(s)\), and
\[
 \Xi_k(s)=c_k^{-1}s(s-1)|d|^{s/2}Z_k(s),
 \qquad c_k=2^{r_1}(2\pi)^{r_2}hR/e.
\]
The classical Dedekind functional equation and residue formula give \(\Xi_k(s)=\Xi_k(1-s)\), \(\Xi_k(0)=\Xi_k(1)=1\) and an entire function of order at most one. The same holds for \(\Xi\). Each criterion is for one specified field, and uses the real numbers
\[
 \lambda_n=\frac1{(n-1)!}\left.\frac{d^n}{ds^n}
             \{s^{n-1}\log\Xi_k(s)\}\right|_{s=1},\qquad n=1,2,\ldots .
\]
A logarithm is needed only in a neighborhood of \(s=1\). The completion is real and positive on a sufficiently small real neighborhood of 1, so the real branch proves reality of \(\lambda_n\). Changing branch or multiplying the completion by a positive constant adds a constant inside the logarithm, killed by the \(n\)-th derivative of a degree-\(n-1\) polynomial.

For \(\phi(z)=\Xi_k((1-z)^{-1})\) one has \(\phi(0)=1\) and \(\phi\) is analytic everywhere in the open disk. With \(u=z/(1-z)\) and \(f=\log\Xi_k\) near 1, the coefficient of \(z^n\) in \(f(1+u)\) is
\[
 \sum_{j=1}^n\binom{n-1}{j-1}\frac{f^{(j)}(1)}{j!}.
\]
Multiplying by \(n\) agrees with Leibniz applied to the definition. Consequently \(\phi'/\phi=\sum_{n\ge1}\lambda_n z^{n-1}\) initially in a disk about zero. Li uses \(|z|<1/4\) on p. 326 for \(\mathbb Q\); this numerical disk is valid independently of RH. It maps into \(|s-1|<1/3\), \(\Re s>2/3\). For \(\Re s>0\), Euler summation yields
\[
 (s-1)\zeta(s)=s\left(1-(s-1)\int_1^\infty \{t\}t^{-s-1}\,dt\right).
\]
The product in the subtracted term has modulus \(<1/2\) on this disk, and the remaining gamma and elementary factors are nonzero there. The field case needs only a sufficiently small radius from \(\Xi_k(1)=1\).

The inverse map is \(z=1-1/s\), and \(|z|<1\) is equivalent to \(\Re s>1/2\). A zero of \(\phi\) produces a simple pole of the logarithmic derivative, with residue its positive multiplicity. Paired reflection of the completed zeros then gives zero-freeness of this disk exactly under RH for that field. If the disk has a zero, the Taylor radius of \(\phi'/\phi\) is precisely the least modulus of its disk zeros. If the disk is zero-free, that radius is exactly 1, including the endpoint obstruction at \(z=1\). Indeed for real \(s\to+\infty\), Stirling and the Dirichlet series give \(\Xi'_k(s)/\Xi_k(s)=(N/2)\log s+O_k(1)\), \(N=[k:\mathbb Q]\), and \(s'(z)=(1-z)^{-2}\). Thus the known positive real approach to \(z=1\) forces a singularity there. The proof requires analyticity only in the open disk and implies no full-boundary convergence statement.

## Products and paired sums

Equations (1.3), (1.4), (3.1) and Lemma 3.1 pair each \(\rho\) with \(1-\rho\), counted with multiplicity. A zero at the fixed point \(1/2\), if present, has even order by the reflection equation, hence can be paired with a second copy. For fixed \(s\) and an entire compact set of \(s\)'s the grouped factor is
\[
 (1-s/\rho)(1-s/(1-\rho))
       =1+\frac{s(s-1)}{\rho(1-\rho)}.
\]
The grouped factors have summable deviations from 1, since the order-one zero count implies \(\sum_\rho|\rho|^{-2}<\infty\). Hadamard factorization gives this genus-zero paired product times \(e^{as+b}\), as the grouped genus-one exponential factors can be absorbed into \(a\). The displayed pair product is invariant under \(s\mapsto1-s\), forcing \(a=0\), and \(\Xi_k(0)=1\) fixes \(e^b=1\). This also provides the product used in Lemma 3.1 from standard analytic inputs without using the particular normalization of Barner’s explicit formula.

On a closed small disk at \(s=0\), select logarithms of each pair with value 0 at zero. They are normally summable by the grouped \(O(|\rho|^{-2})\) bound, which gives termwise derivatives. Equation (3.3) on p. 329 has a real typographical error in its justification: the rendered preceding sentence says \(\zeta_k(s)\) is nonzero at zero. In fact \(\operatorname{ord}_{s=0}\zeta_k(s)=r_1+r_2-1\), since \(Z_k\) has a simple pole there and its gamma factors have total pole order \(r_1+r_2\). For example the printed claim fails in a real quadratic field. The needed premise is \(\Xi_k(0)=1\), already proved in §2. With that correction the expansion is valid. The paired double series can also be checked directly: only \(m=1\) in the expansion of the zero logarithms requires pairing, and the terms of degree \(m\ge2\) are absolutely summable on a sufficiently small closed disk.

At \(s=1\) single-factor differentiation first gives \(1-(1-1/\rho)^{-n}\), or equivalently the same positive power with \(\rho\) replaced by \(1-\rho\). The partner swaps the two values, giving Li’s grouped
\[
 \lambda_n=\sum_{\rho}^{\rm paired}\left(1-(1-1/\rho)^n\right).
\]
This is also obtained by expanding the logarithm at zero and using the reflection (3.2). A pair contributes \(O_n(|\rho|^{-2})\) by the binomial expansion. Individual summands cannot be arbitrarily reordered as an absolutely convergent series. If all zeros are on the line, each \(1-1/\rho\) has modulus 1, so each pair contributes \(2(1-\cos(n\arg(1-1/\rho)))\ge0\). The forward implication needs neither simplicity nor exclusion of a central zero.

## Real theta kernel and the apparent sign reversal

For \(\mathbb Q\), put \(\psi(x)=\sum_{m\ge1}e^{-\pi m^2x}\), and \(W(x)=(x^{3/2}\psi'(x))'\). Poisson summation of the Gaussian gives the usual theta transformation. Splitting the Mellin integral at 1, using that transformation on the small side, and multiplying by \(s(s-1)\) gives the normalized completion. Integrating by parts twice gives Eq. (1.2) in the form
\[
 \Xi(s)=4\int_1^\infty W(x)[x^{(s-1)/2}+x^{-s/2}]\,dx .
\]
One direct check is to set \(I(a)=\int_1^\infty\psi(x)x^{a-1}\,dx\). For \(b=a-\tfrac12\), integration by parts gives \(\int_1^\infty W(x)x^b dx=-\psi'(1)+b\psi(1)+b(b+\tfrac12)I(a)\). Sum this expression at \(a=s/2,(1-s)/2\), and use the derivative of the theta transformation at 1 to obtain \(4[-2\psi'(1)-\psi(1)/2]=1\). The remaining part is \(s(s-1)(I(s/2)+I((1-s)/2))\), as desired. On \(x\ge1\),
\[
 W(x)=\pi x^{1/2}\sum_{m\ge1}m^2(\pi m^2x-3/2)e^{-\pi m^2x}>0.
\]
Write \(A=\tfrac12\log x\), \(U=z/(1-z)\). After substituting \(s=1+U\), the bracket in the integral is \(e^{AU}+x^{-1/2}e^{-AU}\). Thus for \(j\ge1\) its \(z^j\) coefficient is
\[
 \sum_{\ell=1}^j\binom{j-1}{\ell-1}
       \frac{A^\ell}{\ell!}\left(1+(-1)^\ell x^{-1/2}\right)>0
 \quad (x>1).
\]
Every derivative or coefficient may be taken under the integral on compact disks, by exponential decay in \(x\), proving \(a_j>0\).

An apparent sign concern in Eq. (1.6) disappears on reading the actual p. 327 formula. Its initial **infinite** expansion Taylor-expands \(x^{-1/2}e^{As}+e^{-As}\) at \(s=0\), then substitutes \(s=(1-z)^{-1}\). Its \(\ell\)-th Taylor factor is indeed \(x^{-1/2}+(-1)^\ell\). The coefficient of \(z^j\) in \((1-z)^{-\ell}\) is \(\binom{j+\ell-1}{j}\), which matches the displayed factorials. Taking the derivative at \(s=1\) in the subsequent computation moves the center and produces the finite formula above. The same effect accounts for the change of brackets before Eq. (3.6) on p. 331. Neither is a sign error. The early infinite exchanges are valid by the same compact coefficient integral domination, with the absolute exponential expansion bounded by \(e^{A|s|}\).

## Dedekind theta normalization and Mellin repair

On p. 330 the rendered definition is
\[
 \Theta_k(x)=\sum_{\mathfrak b}
    \exp\{-\pi |d|^{-1/N}(N\mathfrak b)^{2/N}\sum_v\epsilon_v x_v\},
 \qquad |x|=\prod_v x_v^{\epsilon_v},
\]
with \(\epsilon_v=1,2\) at real and complex places, respectively, and the indicated product Lebesgue differentials \(dx=\prod_v dx_v\). Read \(dx/x\) as the product of logarithmic differentials. For \(\Re s>1\), elementary gamma integration in each coordinate, with the integral-ideal Dirichlet series and Tonelli applied first to a real exponent, gives
\[
 M(s):=\int_{\mathbb R_{>0}^{r_1+r_2}}\Theta_k(x)|x|^{s/2}
          \prod_v\frac{dx_v}{x_v}
  = |d|^{s/2}\zeta_k(s)
      \prod_v(\pi\epsilon_v)^{-\epsilon_v s/2}\Gamma(\epsilon_v s/2)
  = (2\pi)^{-r_2}|d|^{s/2}Z_k(s).
 \tag{A}
\]
This exact calculation detects a mismatch between the displayed \(G_2\) in §2 and the coefficient \(c_k^{-1}\) in (3.4). The latter must be \((2\pi)^{r_2}c_k^{-1}\) with that \(G_2\) and the product \(dx_v/x_v\). Equivalently, with the usual archimedean gamma factor \((2\pi)^{-s}\Gamma(s)\) instead of Li's \(G_2\), the corresponding residue constant is \((2\pi)^{-r_2}c_k\). One could also put a factor \(2\pi\) in the logarithmic measure for each complex place, but the product differential in the rendered p. 330 does not specify such a factor. In a one-coordinate complex example the ambiguity disappears: for \(k=\mathbb Q(i)\), the one-dimensional integral uses \(dx/x\), \(|x|=x^2\), and (A) is exactly \(\pi^{-s}\Gamma(s)\zeta_k(s)\). For real \(s\to\infty\), the first integral part over \(x\ge1\) differs from \(M(s)\) by a bounded small-\(x\) integral, and the second over \(x\ge1\) is bounded. Yet \(M(s)\to\infty\) by Stirling. The literal printed coefficient would therefore make the leading term \(1/(2\pi)\) of the value defined in §2. This confirms the mismatch independently of the general measure convention. The closing recurrence expression (3.7) then needs the same positive factor if \(b_m\) is defined by the literal unscaled integral in (3.5).

For the corrected identity, set \(u=\tfrac12\log|x|\), and let \(K(u)\,du\) be the pushforward of \(\Theta_k(x)\prod_v dx_v/x_v\). In the logarithms of the \(x_v\), \(u\) is a nonzero linear functional and the pushforward has a locally integrable density by disintegration and (A). Its exponentially weighted Fourier transform on any vertical line \(\sigma>1\) is \(M(\sigma+it)\), with exponential decay there by Stirling and the absolutely convergent ideal sum. Bilateral Laplace inversion identifies its density almost everywhere. By the standard functional equation and simple poles, \(M(s)=M(1-s)\) with residues \(-A_0,A_0\) at 0,1, where \(A_0=(2\pi)^{-r_2}c_k\). Shifting the inverse integral from \(\sigma>1\) to \(1-\sigma\) is valid by Stirling and the fixed-strip polynomial bound for Dedekind zeta. The two residues and the change of variable \(s\mapsto1-s\) give
\[
 K(u)=A_0(e^{-u}-1)+e^{-u}K(-u).
\]
Apply this for \(u<0\) in \(\int_{\mathbb R}K(u)e^{su}du\); for \(\Re s>1\) the residue part integrates to \(A_0/[s(s-1)]\). The positive-side integrals are analytic for every \(s\). Their compact domination follows by bounding \(e^{s u}\), \(e^{(1-s)u}\) and fixed powers of \(u\) by \(C e^{C'u}\) for \(u\ge0\), and applying (A) at a larger positive real argument. Therefore
\[
 \Xi_k(s)=1+\frac{s(s-1)}{A_0}
        \int_0^\infty K(u)(e^{su}+e^{(1-s)u})\,du .
\]
This repairs (3.4) without assuming an unstated normalization of a Hecke theta measure. It uses the classical Dedekind functional equation, poles and fixed-strip bounds as inputs, not a new proof of those facts.

For \(z\) in the disk put \(s=1+z/(1-z)\). The integrand in the last identity has nonnegative Taylor coefficients and strictly positive coefficients on \(u>0\), because the \(\ell\)-th coefficient in powers of \(s-1\) is \(u^\ell(e^u+(-1)^\ell)/\ell!\). The measure has positive mass on \(u>0\) by its original strictly positive density on all \(x_v>0\). Compact domination as above justifies the exchanges. The remaining factor \(s(s-1)=z/(1-z)^2\) has positive coefficients in all positive degrees. Thus each \(a_j>0\) as required by Lemma 3.2, with the corrected positive constant.

## Common converse and scope

The identity \(\phi'=\phi(\phi'/\phi)\) in a small disk gives \(n a_n=\lambda_n+\sum_{j=1}^{n-1}\lambda_j a_{n-j}\), with \(a_0=1\). It also follows from the finite composition coefficients in the logarithm on p. 326. If **all** \(\lambda_n\ge0\), then \(0\le\lambda_n\le n a_n\) for every \(n\). On each \(|z|\le r<1\) the majorant sums to \(\phi'(r)\). The logarithmic-derivative power series therefore extends analytically to the disk, and the identity with \(\phi'\) extends by the identity theorem. A zero of \(\phi\) would contradict the orders of vanishing on the two sides. The Möbius map and zero reflection now give the desired RH. The converse does not require a branch of the logarithm on the full disk before establishing zero-freeness. Nonnegativity through any finite index gives only finitely many coefficient bounds and does not allow the same continuation. The remark’s \(\lambda_1=a_1>0\) is immediate; the recurrence combined with the corrected integral gives finite symbolic coefficient formulas, not an effective criterion for all signs.

No simplicity assumption, conductor uniformity, or universal claim for arbitrary \(L\)-functions is part of either theorem. The sum of zero terms is grouped. Neither theorem proves RH for any field. The recovered primary article makes a whole-work mathematical audit possible even where the source dependencies can be replaced by direct derivations. Any change to the archive's whole-work status or correction taxonomy belongs to the director. [Earlier scoped audit](../li1997_round2.md)

## Checks against cited dependencies

- Barner, *On A. Weil's explicit formula*, p. 139 equations (2)–(4) and p. 142 Theorem 2 equations (11)–(13), was inspected in the GDZ digitization of the journal. He states order one and gives the logarithmic derivative and genus-zero product in order \(|\Im\rho|<T\). For Li's principal character, \(\rho\mapsto1-\rho\) preserves that order, so finite truncations can be grouped into the reflected pairs and the compact convergence above applies. This does not transfer Li's entire-disk positivity to arbitrary Hecke characters. [Barner journal scan](https://gdz.sub.uni-goettingen.de/download/pdf/PPN243919689_0323/LOG_0011.pdf)
- The Toronto PDF of Lang’s second edition reaches the full Chapter XIII, §3, pp. 253–260. Its Theorem 2 on p. 259 explicitly uses the polar numerator \(2^{r_1}hR/e=(2\pi)^{-r_2}c_k\) for \(F_k\), and Theorem 3 on p. 260 gives the stated ideal-norm integral with product logarithmic measure. This confirms exactly the different normalization when invoking Lang in Li's (3.4). The cited 1970 first-edition bytes were not obtained. The p. 330 correction here also follows independently from (A) and the explicit \(\mathbb Q(i)\) test, so it does not rely on edition identity. [Lang second-edition scan](https://www.math.toronto.edu/~ila/Lang%20--%20Algebraic%20number%20theory.pdf)
- Weil, *Basic Number Theory*, Chapter VII §6, Theorem 3 and its corollary, p. 129, were read in a later-edition primary reproduction. They give the continuation, simple poles at 0 and 1, functional equation and \(c_k\) as in Li's §2. The original 1967 edition was not obtained and the Springer chapter supplied a preview. The printed \(G_1(1)=G_2(1)=1\) agrees with Li's normalization and with the class-number residue. [Weil primary reproduction](https://studylib.net/doc/27697295/basic-number-theory--grundlehren-der-mathematischen----an...) · [Publisher chapter](https://link.springer.com/chapter/10.1007/978-3-662-05978-4_7)
- Edwards Chapter 2 is cited by Li for the classical zeta paired product. The exact 1974 book manifestation was not obtained in this run. The grouping and product normalization were instead derived above directly from classical Hadamard factorization and the functional equation. Normal convergence, the ordinary theta formula, the field theta integral, the endpoint radius, and the entire coefficient argument are thus covered in the reconstruction without making a claim of complete reading of the four dependency books and papers.
