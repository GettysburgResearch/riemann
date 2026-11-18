# HLZ Lemma 6: rendered source and a separated-shift residue test

18 November 2026. Independent narrow audit of Heap–Li–Zhao, *Lower bounds for discrete negative moments of the Riemann zeta function*, Algebra & Number Theory 16(7), 2022, DOI 10.2140/ant.2022.16.1589, Lemma 6, printed pp. 1605–06. The Gaussian zeros specified by the lemma do not cancel the two numerator poles for generic shifts. There is a separated-shift example satisfying the normalization and the natural weight bounds of the paper and its preprint, with a missed main term of size \(\log T\). This is a local deduction check. No conclusion below depends on an error in the exponent of \(\log T\), and no conclusion about the separate Theorem 5 is inferred from this test.

## Exact versions and notation

I rendered the journal PDF's pages 17–18, which are printed pp. 1605–06. The printed Lemma 6 gives \(H(0)=1\) and zeros at \(2s=\beta-\alpha,\beta-\gamma\), repeated in the weight definition for Theorem 4 on p. 1593. The proof prints numerator arguments \(1+\alpha+\beta+2s,\ 1+\beta+\gamma+2s\) and denominator argument \(1+\beta+2s\). Its left contour is at \(-1/\log_3 T\), with 3 visibly subscripted. In this contour context \(\log_3 T=\log\log\log T\). In contrast its factor \((\log T)^3\) has a genuine superscript. For \(h=k=1\) the first error in (25) is \(T^{-2/\log_3 T}(\log T)^3\), which tends to zero faster than any fixed inverse power of \(\log T\). The displayed typesetting supplies no exponent objection. [Journal PDF, SHA-256 6162632530cbeee8c1664d7ea53e844cffa9dbc53fe00a8cd8270e2d713b6a82](../../sources/classical63_derivative_moments/hlz2022print.pdf)

The archive preprint is arXiv:2003.09368v1, 20 March 2020. Its Lemma 3 and (29), manuscript pp. 16–17, state the same signs under \(z_1,z_2,z_3\) standing for the actual three arguments of \(\widetilde{\mathcal Z}\): pole variables \(2s=-(z_1+z_2),-(z_2+z_3)\) in the proof versus zeros \(2s=z_2-z_1,z_2-z_3\) in the statement. Unlike the journal shorthand, the preprint explicitly allows \(H(u+iv)\ll_u(\log T)^2e^{-cv^2}\). The right error there has an extra polylogarithmic factor and still tends to zero in the example below. The public arXiv submission history showed v1 only at this check. [Pinned preprint, SHA-256 73c78d922741658678023e73bd0684c1003261906ccc97b48f2e727f5874f6f6](../../sources/classical63_derivative_moments/hlz2022.pdf) · [arXiv version history](https://arxiv.org/abs/2003.09368)

## Counterexample with separated real shifts

Take \(h=k=1\), \(L=\log T\), \(\delta=\kappa/L\) with fixed \(0<\kappa\le1/10\), and
\[
 \alpha=\delta,\qquad \beta=2\delta,\qquad \gamma=3\delta,\qquad
 H_T(s)=e^{s^2}(1-4s^2/\delta^2).
\]
The prescribed points are precisely \(\pm\delta/2\). This \(H_T\) is entire, even, real on the real axis, normalized at zero, and has a fixed Gaussian decay rate:
\[
 |H_T(\sigma+it)|\le C_{\sigma,\kappa} L^2 e^{-t^2/2}.
\]
On any bounded interval of real parts the constant can be uniform in \(\sigma\), since \((1+t^2)e^{-t^2/2}\) is bounded. In particular the family meets the preprint's explicit hypothesis, keeps a common Gaussian rate, and has only polynomial dependence on the inverse shift gaps. The journal describes \(H_{\alpha,\beta,\gamma}\); an estimate uniform in varying \(O(1/L)\) shifts needs the customary control on such families. If one allowed the constants in (25) to depend arbitrarily on the particular \(H_T\) at each \(T\), it would cease to give the estimate used by the source. Independently of that distinction, the alleged zero cancellation in the local residue calculation fails for each separated choice.

With \(h=k=1\), the sum and Euler product reduce exactly to a single ratio, without any local factors:
\[
 I_T(s) = \frac{H_T(s)T^{2s}}s
       \frac{\zeta(1+3\delta+2s)\zeta(1+5\delta+2s)}
            {\zeta(1+2\delta+2s)},\qquad
 \widetilde{\mathcal Z}_{\alpha,\beta,\gamma,1,1}
      =\frac1{2\pi i}\int_{(1/L)} I_T(s)\,ds .
\]
The Dirichlet series and the original definition converge on that right line for these positive shifts. The residue at zero is precisely \(\mathcal Z_{\alpha,\beta,\gamma,1,1}\). The other poles are at \(s_\alpha=-3\delta/2\) and \(s_\gamma=-5\delta/2\). They are distinct from zero and from the roots of \(H_T\). At the first, the remaining numerator and denominator are \(\zeta(1+2\delta),\zeta(1-\delta)\); at the second they are \(\zeta(1-2\delta),\zeta(1-3\delta)\). These factors are nonzero by the local Laurent expansion for sufficiently small \(\delta>0\). The denominator pole at \(s=-\delta\) gives a zero of its reciprocal, not a pole of the integrand.

In the two residues the pole of the relevant numerator zeta has coefficient \(1/2\) as a function of \(s\). Since \(H_T(s_\alpha)=-8e^{9\delta^2/4}\) and \(H_T(s_\gamma)=-24e^{25\delta^2/4}\), the Laurent expansion \(\zeta(1+x)=x^{-1}+O(1)\) gives
\[
 R_\alpha=-\frac4{3\delta}e^{-3\kappa}+O(1),\qquad
 R_\gamma=\frac{36}{5\delta}e^{-5\kappa}+O(1).
\]
Their sum has positive leading coefficient for \(0<\kappa\le1/10\), since \(e^{2\kappa}<27/5\). Thus neither a degeneracy of the shifts nor cancellation between the two residues explains the proof's contour identity.

For rigorously small contour remainders one can move to \(-a/\log_3 T\) for a fixed sufficiently small \(a>0\), using only the classical zero-free region and standard bounds there. Let \(U=B_A\sqrt{\log L}\). The available zero-free width up to imaginary height \(2U+1\) has order \(1/\log(2U+3)\asymp1/\log_3T\), so choosing a small \(a\) keeps the denominator zero-free in the truncated rectangle. Its pole is removable after reciprocation. One can instead use the Vinogradov–Korobov region for the printed left location. On the left edge, Laurent estimates near \(1\) and standard logarithmic-power zeta and reciprocal zeta bounds in a narrower zero-free strip elsewhere bound the ratios by fixed powers of \(L\). The factor \(1/s\) costs at most \(\log_3T/a\), and the Gaussian bound leaves a factor \(T^{-2a/\log_3 T}\) times a fixed power of \(L\). On the horizontal edges Gaussian decay gives \(L^{-A}\) for sufficiently large \(B_A\), as \(T^{2\Re s}\le e^2\). On the omitted vertical tails of the right edge, the Dirichlet-series bounds \(\zeta(\sigma)\ll L\) for the numerator and \(1/\zeta\) bounded by its absolutely convergent inverse Dirichlet majorant \(\zeta(\sigma)\ll L\) suffice. It follows that, for fixed \(A\),
\[
 \widetilde{\mathcal Z}_{\alpha,\beta,\gamma,1,1}
       -\mathcal Z_{\alpha,\beta,\gamma,1,1}
 =\delta^{-1}\!\left(\frac{36}{5}e^{-5\kappa}
                     -\frac43e^{-3\kappa}\right)+O(1).
\]
Both claimed errors in (25) go to zero, whereas the difference has size \(\log T\). The example also contradicts preprint (29) under its explicit \(L^2\) weight bound.

## Convention and repair boundary

For the named arguments \((\alpha,\beta,\gamma)\), the cancellation condition is that \(H\) vanish at \(2s=-(\alpha+\beta),\ -(\beta+\gamma)\) with the requisite multiplicities, not the printed differences. In the separate variables of journal (21)–(22), the arguments are \((z_1,-z_2,z_3)\), and the correct zeros there are indeed \(2s=z_2-z_1,z_2-z_3\). Translating these points back gives the negative sums in the actual three arguments. The proof of Lemma 6 itself explicitly retains the named arguments in both numerator factors. There is no second sign convention in that display that makes its printed hypothesis work. The version comparison makes a partial reparametrization plausible as an origin of the mismatch, without identifying editorial intent.

For separated shifts with the pole locations bounded below by a fixed multiple of \(1/L\), normalizing the polynomial factors at the actual poles and multiplying by the fixed Gaussian restores the contour residue identity and allows arbitrary logarithmic savings at \(h,k\le T^\theta,\ \theta<1/2\). Collisions with the origin do not permit simultaneous \(H(0)=1\) and a required root there. A use at coinciding shifts needs a separated-contour argument or an analytic continuation of appropriate combined expressions, with corresponding uniform bounds. Exact printed first error constants and uniformity on all \(h,k\le T\) after such a change are not established here. The sentence in the proof that the Euler expression is holomorphic on all \(\Re s>0\) also requires restricting the signs or placing the initial contour to the right of the possible shifted poles. The explicit counterexample has positive shifts and avoids this independent qualification.

The isolated lemma failure concerns the step removing individual \(\mathcal Z\) factors in favor of the smoothed diagonal. Theorem 5 is stated before that step and directly uses the \(\mathcal Z\) factors. Theorem 5-only applications therefore do not use this cancellation. This review neither assesses the full proof of Theorem 5 nor asserts whether a distinct argument based on cancellations among combined terms gives all of Theorem 4 as stated.
