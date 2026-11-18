# Li 1997 whole-work advocate audit

18 November 2026. Reviewed all nine journal-typeset pages 325–333 of Xian-Jin Li, *The Positivity of a Sequence of Numbers and the Riemann Hypothesis*, J. Number Theory 65(2), Aug. 1997, DOI 10.1006/jnth.1997.2137, article NT972137. The full Theorems 1 and 2 proof mechanisms withstand reconstruction. A letter substitution at p. 329 and a genuine normalization mismatch in (3.4), inherited by (3.7), are visible in the typeset copy. The corrected positive normalization preserves Lemma 3.2, both equivalences, and the last remark's method. The correction does change the explicitly normalized Dedekind coefficients in (3.7). [Journal-typeset mirror copy](../../sources/li_original_round2/li1997_journal_typeset_mirror.pdf)

## Manifestation and access

The publisher HTML confirms issue, pages, title, author, DOI and abstract. Its PDF and Elsevier API routes gave 403/blocked tunnel responses. Paperzz's ordinary download page gave 403. Its public document HTML, however, embeds an iframe whose URL supplies the PDF via a signed viewer file path at s3p.paperzz.com. This supplied 706,759 bytes, a valid nine-page PDF with the printed publisher article, manuscript dates (received 10 Sept. 1996, revised 16 Dec. 1996), full equations and reference page. PDF metadata identify title, subject Journal of Number Theory, author Li, X.-J., Acrobat Distiller 3.0 for Macintosh, creation 14 July 1997 and file modification 29 Apr. 2015. Each page carries its typeset production mark and pages are consecutive. The independent sibling downloaded identical bytes. These facts verify the typeset journal manifestation from a mirror, without asserting a byte match to today's inaccessible publisher download. Source SHA-256 **8f5719751f869d71907c9da75270cb8c012b54f1453f54179461dbc331d255a1**. The previous degraded reproduction SHA-256 **845a2d9b2c86da1acf3502f9ed2f7f17ae5e922f87761d42c34f321708ba6f2c** remains unchanged. DOI/title corrigendum searches and the stored Crossref record yielded no verified correction. Search coverage is bounded. [Publisher landing page](https://www.sciencedirect.com/science/article/pii/S0022314X97921375) · [Mirror landing page](https://paperzz.com/doc/7086946/--science-direct)

## Shared analytic mechanism and local conventions

For the classical zeta case Li's \(\xi(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)\) is twice the convention with \(\xi(1)=1/2\). It instead has \(\xi(0)=\xi(1)=1\). For the Dedekind case the normalized completion is given below. Write \(\Xi\) for the applicable completion and let
\[
 \lambda_n=\frac{1}{(n-1)!}\frac{d^n}{ds^n}
 [s^{n-1}\log\Xi(s)]_{s=1},\qquad
 \phi(z)=\Xi\!\left(\frac{1}{1-z}\right).
\]
A logarithm is chosen locally at 1. A branch change adds a constant times \(s^{n-1}\), killed by the \(n\)-th derivative. Positive rescaling has the same invariance. Reality follows from conjugation of \(\Xi\) and the real germ of the normalized logarithm. The map \(z=1-1/s\) identifies the unit disk with \(\Re s>1/2\), since \(|s-1|^2<|s|^2\) iff \(2\Re s>1\). The normalized completion obeys \(\Xi(s)=\Xi(1-s)\); no zero at 0 or 1 belongs in either sum. A zero of \(\phi\) of order \(m\) gives a pole of \(\phi'/\phi\) with residue \(m\). Thus \(\phi'/\phi\) holomorphic in the disk is equivalent to the applicable critical-line assertion by reflection, with multiplicities allowed.

The paired product in (1.3)/(3.1) is standard. For completeness, using \(\rho\) and \(1-\rho\),
\[
 (1-s/\rho)(1-s/(1-\rho))
      =1+\frac{s(s-1)}{\rho(1-\rho)}.
\]
The completed zetas have order at most one, hence \(\sum_\rho(1+|\rho|)^{-2}<\infty\). Alternatively the standard number-field zero count is \(O_k(T\log(2T))\). The paired product converges normally, and a potential central zero has even multiplicity by the reflection identity, so it too can be paired. Comparison with genus-one Hadamard factors leaves a factor \(e^{A+Bs}\). Both the whole completion and the paired product satisfy the reflection identity, so \(B=0\); normalization at zero fixes the multiplier to 1. This establishes (1.3)/(3.1) with the required grouping. It does not claim absolute convergence of the individual genus-zero factors. In particular the grouped logarithm at zero converges normally after taking its branch with \(\log\Xi(0)=0\). Individual \(m=1\) contributions in (3.3) require pairing, while \(m\ge2\) terms are normally absolutely summable after reducing the local radius.

Since \(\Xi(1/(1-z))=\Xi(-z/(1-z))\), each pair of factors in the product becomes the corresponding product of \((1-w_\rho z)/(1-z)\), with \(w_\rho=1-1/\rho\). Local logarithmic differentiation gives
\[
 \frac{\phi'(z)}{\phi(z)}=\sum_{n\ge1}\lambda_n z^{n-1},
 \qquad
 \lambda_n=\sum_{\rho\ {\rm paired}}(1-w_\rho^n).
\]
Here the paired fixed-order summand is \(O_n(|\rho|^{-2})\), since the first-order reciprocal terms cancel. Derivative verification independent of the product uses \(u=z/(1-z)\) and \(f(s)=\log\Xi(s)\) near 1. Then \(n[z^n]f(1+u)=n\sum_{j=1}^n\binom{n-1}{j-1} f^{(j)}(1)/j!\), which is the derivative in the definition. The direct individual zero contribution computed at \(s=1\) is \(1-w_\rho^{-n}\). Its sum agrees with the displayed formula because the partner swaps \(w\) with \(w^{-1}\). This accounts for the intermediate p. 326 \((\rho-1)^{k-n}\) expression. Passage to the next line is valid only after legitimate within-pair relabeling. In Lemma 3.1 the reflection differentiation contributes \((-1)^n\) in (3.2); expanding \((1-s)^{n-1}\log\Xi(s)\) at zero then gives \(-\sum_{m=1}^n(-1)^m\binom{n}{m}\rho^{-m}=1-w_\rho^n\) after combining the two signs. If the zeros are critical, partners satisfy \(w^{-1}=\bar w\), and a pair contributes \(2-2\cos(n\arg w)\ge0\).

If \(\phi(z)=\sum a_jz^j,\ a_0=1\), with \(a_j\ge0\) for all \(j\), the local identity gives
\[
\lambda_n=na_n-\sum_{j=1}^{n-1}\lambda_j a_{n-j}.
\]
Thus all \(\lambda_j\ge0\) imply \(0\le\lambda_n\le na_n\) for each \(n\). The Taylor series of \(\phi\) converges on every closed disk of radius \(r<1\). Hence the logarithmic derivative Taylor series extends to the whole disk, with absolute sum at most \(\phi'(r)\) on the radius-\(r\) disk. The identity \(\phi'=\phi L\) with this extended analytic \(L\) holds globally by the identity theorem. It precludes zeros because the order of \(\phi'\) at a zero of \(\phi\) would be smaller than the order of the right-hand side. This completes both converse implications once the positive Taylor coefficients are justified. A finite coefficient prefix does not provide the needed analytic extension. The p. 326 finite composition expression for \(\lambda_n\) comes directly from \(n[z^n]\log(1+\sum_{j\ge1}a_jz^j)\). This log expansion is local only.

## Section 1, classical theta integral and printed series

Set \(\psi(x)=\sum_{n\ge1}e^{-\pi n^2x}\), \(W(x)=(x^{3/2}\psi'(x))'\). On \(x\ge1\),
\[
 W(x)=\pi x^{1/2}\sum_{n\ge1}n^2(\pi n^2x-3/2)e^{-\pi n^2x}>0.
\]
Splitting the initial Mellin integral of \(\psi\) at 1 and using Jacobi inversion gives
\[
 \pi^{-s/2}\Gamma(s/2)\zeta(s)=\frac{1}{s(s-1)}
 +\int_1^\infty \psi(x)\big(x^{s/2}+x^{(1-s)/2}\big)\frac{dx}{x}.
\]
Jacobi inversion also gives \(\psi'(1)=-(1+2\psi(1))/8\). Integrating \(W x^a\) by parts twice yields \(-\psi'(1)+a\psi(1)+a(a+1/2)\int_1^\infty\psi(x)x^{a-1/2}dx\). Take \(a=(s-1)/2\) and \(-s/2\). Their sum is \(-1/2\), their \(a(a+1/2)\) both equal \(s(s-1)/4\), and the boundary constants, multiplied by 4, sum to 1. This proves (1.2), including its factor 4 and endpoint constant. Faster-than-power decay permits all fixed derivatives, power-series expansions in \(s\), and coefficient extraction in \(z\) uniformly on compact subsets of the unit disk. The integral also gives order at most one using elementary gamma bounds on the moment of the exponential tail.

For explicit coefficient verification let \(L=\tfrac12\log x\), \(t=(1-z)^{-1}\). The (1.2) factor is \(x^{-1/2}e^{Lt}+e^{-Lt}\). Its expansion in powers of \(t\) uses the bracket \(x^{-1/2}+(-1)^l\), exactly as the printed (1.6). For \(j\ge1\), \([z^j]t^l=\binom{j+l-1}{j}\). This is the printed rising product divided by the appropriate factorial; the two orientations of the product both give the same binomial coefficient. The intermediate derivative in \(t\) uses \(j!^{-1}D^j(t^{j-1}t^l)|_{t=1}\). Both terms independent of \(t\) may be discarded because \(D^j t^{j-1}=0\). After recentering at \(t=1+u\), the exponentials instead give \(e^{Lu}+x^{-1/2}e^{-Lu}\), so
\[
 a_j=4\sum_{l=1}^j\binom{j-1}{l-1}
          \int_1^\infty W(x)\frac{L^l}{l!}
                        [1+(-1)^l x^{-1/2}]\,dx>0 .
\]
This agrees with the final finite formula. The swapped-looking brackets are consistent because the expansion centers differ. The specific p. 326 starting radius \(|z|<1/4\) also holds without an empirical zero list. After establishing coefficient positivity, \(|\phi(z)-1|\le\phi(1/4)-1\) on the closed radius-\(1/4\) disk. At \(s=4/3\), integral comparison gives \(\zeta(4/3)\le4\), and log-convexity gives \(\Gamma(2/3)\le\sqrt\pi\). Thus \(\phi(1/4)\le (16/9)\pi^{-1/6}<2\). The paired product can then be differentiated throughout the open radius-\(1/4\) disk by normal convergence and absence of zeros. The local identity itself only needs an arbitrarily small positive radius.

## Sections 2–3, Dedekind normalization and independent repair

Fix a number field \(k\), absolute discriminant \(D\), signature \((r_1,r_2)\), degree \(N=r_1+2r_2\), regulator \(R_k\), class number \(h\), and root-of-unity number \(e\). The mathematical content of p. 328 matches Weil's Ch. VII §6 Theorem 3, in the checked 3rd-edition reproduction. In the article
\[
 G_1(s)=\pi^{-s/2}\Gamma(s/2),\quad
 G_2(s)=(2\pi)^{1-s}\Gamma(s),\quad
 Z_k(s)=G_1(s)^{r_1}G_2(s)^{r_2}\zeta_k(s).
\]
Euler product holds for \(\Re s>1\), the completed \(Z_k\) has only the two simple poles 0 and 1 with the stated residues, and \(D^{s/2} Z_k(s)\) is unchanged by \(s\mapsto 1-s\). Its residues at 0 and 1 are \(-c_k,+c_k\), \(c_k=2^{r_1}(2\pi)^{r_2}hR_k/e\). Hence \(\xi_k(s)=s(s-1)D^{s/2} Z_k(s)/c_k\) is entire with endpoints both 1. Its zeros are the nontrivial zeros of \(\zeta_k\); the archimedean gamma poles cancel the trivial zeros.

**Printed p. 329 normalization typo.** The sentence before (3.3) literally has \(\zeta_k(s)\) nonvanishing at 0, whereas the displayed logarithm and the preceding product concern \(\xi_k\). The correct assertion is \(\xi_k(0)=1\). In fact the archimedean factors and \(Z_k\)'s simple pole imply \(\operatorname{ord}_{s=0}\zeta_k=r_1+r_2-1\), which is positive for a real quadratic field. The local branch and the stated zero-sum result survive with \(\xi_k\) in that sentence.

**Printed (3.4) normalization.** With \(\epsilon_v=1\) or 2 as printed, \(r(x)=|x|=\prod_v x_v^{\epsilon_v}\), and \(d\mu=\prod_v dx_v/x_v\) (the article writes \(dx/x\) with \(x=\prod_v x_v\)), the printed ideal sum is
\[
 \Theta_k(x)=\sum_{\mathfrak b\ne0}
 \exp\!\left[-\pi D^{-1/N}(N\mathfrak b)^{2/N}
                        \sum_v\epsilon_v x_v\right].
\]
For \(\Re s>1\), positivity at \(\Re s\) and factorwise Euler gamma integration yield exactly
\[
 F(s)=\int \Theta_k(x)r(x)^{s/2}\,d\mu
      =(2\pi)^{-r_2}D^{s/2} Z_k(s).
\]
Indeed a real place contributes \(\pi^{-s/2}\Gamma(s/2)\), a complex place contributes \((2\pi)^{-s}\Gamma(s)\), and common scalar powers contribute \(D^{s/2}(N\mathfrak b)^{-s}\). The integrals cover the full positive orthant. Thus \(F\) is symmetric and has residues \(\pm A_k\) at \(1,0\) respectively, where \(A_k=c_k/(2\pi)^{r_2}>0\).

Here is a direct derivation of the split, without equating the printed ideal kernel to a lattice-theta convention. Push \(\Theta_k\,d\mu\) to the variable \(u=\tfrac12\log r(x)\) with density \(g(u)\). The weighted pushforward \(e^{cu}g(u)\) is integrable for \(c>1\) by the same gamma integral. Coordinate change in the log variables gives absolute continuity. On a fixed strip the ordinary polynomial-growth estimate for \(\zeta_k\) and Stirling give exponential decay for \(F\) at large imaginary part, uniformly across the strip. Fourier inversion on \(\Re s=c\) then recovers \(g\) a.e. from \((2\pi i)^{-1}\int_{(c)}F(s)e^{-su}ds\), using its continuous version. Moving the contour to \(1-c\) crosses the two simple poles, and reflection on the new line gives
\[
 g(u)=A_k(e^{-u}-1)+e^{-u}g(-u).
\]
The horizontal integrals vanish by the same uniform strip decay. Using this at \(-u\) for \(u>0\) in the initial full Mellin integral gives
\[
 F(s)=\frac{A_k}{s(s-1)}
     +\int_{r(x)\ge1}\Theta_k(x)
                 (r(x)^{s/2}+r(x)^{(1-s)/2})\,d\mu .
\]
The last integral is entire. On a compact set of \(s\)-values, all powers and fixed log derivatives at \(r\ge1\) are bounded by \(C r^{c'/2}\) for a sufficiently large real \(c'>1\), whose integral is finite. The estimate follows from the right half-plane integral and so does not presuppose continuity of the split. Hence
\[
 \xi_k(s)=1+A_k^{-1}s(s-1)
                \int_{r(x)\ge1}\Theta_k(x)
                 (r(x)^{s/2}+r(x)^{(1-s)/2})\,d\mu .
\]
The printed multiplier \(c_k^{-1}\) in (3.4) must instead be \(A_k^{-1}=(2\pi)^{r_2}/c_k\), or equivalently the printed kernel must be multiplied by \((2\pi)^{r_2}\). This also changes (3.7) to \(A_k a_j=\sum_{m=0}^{j-1}(j-m)b_m\) when the kernel in (3.5) is left as printed.

**Exact witness independent of strip growth.** For \(k=\mathbb Q(i)\), \(D=4,\ N=2,\ r_2=1,\ c_k=\pi/2,\ A_k=1/4\). Principal ideals correspond four-to-one to nonzero Gaussian integers. With a single positive coordinate \(x\), the printed kernel is \(\Theta_k(x)=(\vartheta(x)^2-1)/4\), \(\vartheta(x)=\sum_{n\in\mathbb Z}e^{-\pi n^2 x}\), and \(r(x)=x^2\). Jacobi inversion gives \(\Theta_k(x)=x^{-1}\Theta_k(1/x)+(x^{-1}-1)/4\). The direct Mellin split therefore gives residue term \(1/[4s(s-1)]\) and the positive integral over \(x\ge1\) exactly as in (3.4). The normalized prefactor is 4, while the printed prefactor is \(2/\pi\). At \(s=2\) the integral is strictly positive, so the discrepancy cannot be absorbed by an endpoint or vanishing term. The example verifies the mismatch in the source's own normalization with elementary arithmetic.

**Lemma 3.2 and end of Theorem 2.** With \(u=t-1=z/(1-z)\) and \(L=\tfrac12\log r\), (3.5)'s bracket is \(e^{Lt}+r^{1/2}e^{-Lt}\). At \(t=0\) its \(l\)-th coefficient has bracket \(1+(-1)^l r^{1/2}\) as printed. At \(t=1+u\), the bracket is \(r^{1/2}e^{Lu}+e^{-Lu}\), yielding \([r^{1/2}+(-1)^l]L^l/l!\) in the finite formula (3.6). Multiplication by \([z^m]u^l=\binom{m-1}{l-1}\) and integration reproduce that formula exactly. Absolute exchanges use the compact domination just given, or for the initial infinite series bound its absolute terms by a sufficiently large power of \(r\). Thus \(b_0>0\) and \(b_m>0\) for every \(m\), with strictness on \(r>1\). Since \(s(s-1)=z/(1-z)^2=\sum_{j\ge1}jz^j\), the corrected (3.7) follows and \(a_j>0\) for all \(j\). The \(s(s-1)\) endpoint factor is essential. Bounds by real-axis gamma integrals on the half-plane \(\Re s>1\) also bound the split on a disk \(|s|\le R\) by \(\exp(O_k(R\log(R+2)))\), giving the order input for Hadamard. Equations (3.8)–(3.11) are precisely the shared local product, recurrence and analytic continuation above. The final Remark \(\lambda_1=a_1>0\) is valid, and its explicit coefficient prescription uses the corrected scalar.

## Coverage and reference ledger

| Printed pages | Items reviewed | Disposition |
|---|---|---|
| 325 | Header, abstract, (1.1)–(1.2), Theorem 1 | Matching edition and valid definitions and constants. |
| 326 | (1.3)–(1.5), product substitution, \(1/4\) radius, direct derivative and composition sum | Grouping and reflection incorporated. All justified above. |
| 327–328 | (1.6), finite coefficient formula, recurrence, both directions, §2 Euler product and completion | Riemann formulas agree at their respective centers. Dedekind gamma normalization and residue read literally. |
| 329 | Theorem 2, Lemma 3.1, (3.1)–(3.3) | \(\zeta_k\) in the nonvanishing sentence is a printed typo. Repaired by normalized \(\xi_k\). |
| 330–331 | Remaining Lemma 3.1 derivative, Lemma 3.2, (3.4)–(3.8) | Printed (3.4) and inherited scalar in (3.7) corrected. Remaining formulas checked including signs, factorials and all positive Taylor coefficients. |
| 332 | (3.9)–(3.11), both directions, remark | Local to global analytic conditions and remark justified. |
| 333 | Acknowledgment and all four references | Source roles and limitations below. |

1. **Barner 1981**, *On A. Weil's explicit formula*, 323, 139–152. The actual GDZ digitization, printed p. 142, Theorem 2, (11)–(12), gives the height-ordered logarithmic derivative and product of the associated entire completion. This matches the role of [1] in (3.1). Li's reflection grouping is independently validated by the paired Hadamard argument. The critical-strip ordinates give absolute summability of the grouped differences, so the grouped prescription and Barner's height convention agree. [GDZ source page](https://gdz.sub.uni-goettingen.de/fulltext/PPN243919689_0323/00000146?_format=xml)
2. **Edwards 1974**, *Riemann's Zeta Function*, cited Ch. 2 (especially §2.8). The text reproduction locates the classical Riemann product in the specified chapter; the analytic proof reconstructed above provides the normal-convergence input. No claim is made about an audit of the entire book or an original-edition PDF match. [Text reproduction](https://djvu.online/file/hmm3mraNeo082)
3. **Lang 1970**, *Algebraic Number Theory*, Ch. XIII §3 Theorem 3. The chapter identity and functional equation topic are confirmed from the 1970 reissue's publisher chapter listing. The available 1994 file here contains front matter only. Lagarias–Rains, *On a two-variable zeta function for number fields*, published pp. 65–66, follows Lang's Ch. XIII and explicitly uses theta over ideal-class representatives and unit shape parameters, with functional equation and recovery of completed zeta. That is a matching arithmetic framework, and not evidence that the article's own ideal-sum formula has the printed multiplier. The cited 1970 Lang theorem's exact printed measure was not recovered, and the independent Mellin derivation and Gaussian-field witness remove reliance on an inferred Lang coefficient. [Lang chapter](https://link.springer.com/chapter/10.1007/978-1-4684-0296-4_13) · [Lagarias–Rains appendix](https://www.numdam.org/article/AIF_2003__53_1_1_0.pdf)
4. **Weil 1967**, *Basic Number Theory*, Ch. VII §6 Theorem 3. Checked its matching theorem in the available third-edition text reproduction, including pole residues and \(D^{1/2-s}\) functional equation. First-edition typeset chapter bytes were unavailable. The arithmetic result matches the article's displayed factor and residue with its stated convention. [Original edition metadata](https://link.springer.com/book/10.1007/978-3-662-00046-5) · [Later edition text reproduction](https://studylib.net/doc/27697295/basic-number-theory--grundlehren-der-mathematischen----an...)

This checks every article page and reconstructs both equivalences, with explicit typeset evidence and repair for the Dedekind normalization. Reference-edition boundaries and the magnitude of the correction are documented above. Canonical adjudication and any description of formal correction status are separate.
