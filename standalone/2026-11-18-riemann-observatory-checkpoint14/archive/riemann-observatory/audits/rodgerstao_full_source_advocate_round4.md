# Rodgers–Tao: full primary reading, proof architecture, and scoped reconstruction

Researcher: `li_advocate`. Cutoff/read date: 2026-11-17. Existing canonical identity **PAPER-S004**; no second work is added. Actual source: arXiv:1801.05914v5, dated3July2021, **61 pages**, private files `sources/spectral/rodgerstao.pdf` and `.txt`. All61 pages, including every section, proof, and reference list, were substantively read sequentially. Selected displayed formulas on pp30,40,46,55 were also checked in rendered primary pages. This establishes whole-preprint Level1 reading, **not** a whole-paper technical audit. Journal identity remains Forum of Mathematics,Pi8(2020),e6, DOI10.1017/fmp.2020.6; the2021 preprint incorporates later corrections and is not the untouched2020 publication.

## Exact theorem and normalization

The source's equations(1)–(4), p2, are
\[
H_0(z)=\tfrac18\xi(\tfrac12+\tfrac{iz}{2}),\quad
H_t(z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,
\]
\[
\Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}}.
\]
The kernel is even and super-exponentially decaying. The evolution is the **backwards Fourier heat equation** \(\partial_tH_t=-\partial_z^2H_t\). Newman/deBruijn's real-zero preservation gives a finite threshold \(\Lambda\): all zeros of \(H_t\) are real iff \(t\ge\Lambda\), including the endpoint. Theorem1, p3, proves exactly **\(\Lambda\ge0\)**. RH is equivalent to the *opposite* inequality \(\Lambda\le0\); combining them would mean \(\Lambda=0\), but this paper does not prove that upper bound.

This source uses a Fourier argument twice the usual zeta ordinate: the positive zeros of \(H_0\) are \(x_j(0)=2\gamma_j\), when RH and simplicity hold. Its smooth counting function is therefore
\(\Psi(T)=T(\log(T/(4\pi))-1)/(4\pi)\), rather than the ordinate normalization with2π. Constants in cross-paper comparisons must follow this dilation.

## Proof architecture, with exact assumptions

The entire contradiction argument from §1.2 onward assumes **\(\Lambda<0\)**. This implies RH and supplies an interval of real **simple** zeros \(x_j(t)\), \(\Lambda<t\le0\), indexed increasingly by \(j\in\mathbb Z\setminus\{0\}\), with \(x_{-j}=-x_j\). Neither real-rootedness nor simplicity at0 is an unconditional premise imported into the theorem.

1. **§2, Lemmas4,6,7 (pp8–19): complex asymptotics.** Gaussian convolution controls upper bounds. A saddle-point contour shift, with a uniquely chosen saddle in a strip, controls lower bounds and logarithmic derivatives at imaginary heights comparable to \(\log x\). This replaces the usable Dirichlet expansions lost after negative heat time. Lemma7's Stirling/Gaussian proof explicitly acknowledges a repair suggested by AlexDobner, footnote8,p15.
2. **§3, Theorem9 and Corollary10 (pp19–26): macroscopic rigidity.** With \(\xi_j=\Psi^{-1}(j)\), one gets \(N_t([0,T])=\Psi(T)+O(\log^2T)\), a short-interval formula on physical length \(\asymp\log T\), and \(x_j(t)=\xi_j+O(\log\xi_j)\). The short-interval error is uniform in bounded interval-scale parameter. Argument principle/Jensen handle the counting formula; a normal-family argument uses the no-nonreal-zeros hypothesis. At0, classical Riemann–vonMangoldt and the RH-implied Littlewood estimate are sharper.
3. **§4, Theorem11 and Lemma12 (pp27–33): zero motion and local laws.** The motion is \(\dot x_k=2\sum_{j\ne k}'(x_k-x_j)^{-1}\), with symmetric principal value. Gap differences have absolutely convergent equations. Finite-subsystem energy, virial, cross-energy, and Hamiltonian identities retain interactions with the environment. Dropping those interactions is generally invalid.
4. **§5, Proposition13 (pp33–37): a very weak gap bound.** Iterated enlargement of a tightly packed cluster, using a virial/cross-energy estimate, gives \(\log(1/(x_{j+1}-x_j))\ll\log^2j\log\log j\) after narrowing time to \([\Lambda/2,0]\). The bound is weak but prevents excessively rapid growth of logarithmic interactions.
5. **§6, Proposition15 (pp37–38): preliminary integrability.** A pigeonhole choice of an expanded interval controls time-integrated inverse-square interactions by \(J^2\log^{O(1)}J\). This is an input to justified integration/summation in the next section, not the final energy estimate.
6. **§7, Theorem17 (pp38–55): renormalized relaxation.** Define \(V(r)=r^{-2}-1+2(|r|-1)\), and compare each actual gap with its classical gap. Nonnegative renormalized energy measures deviation from local spacing. Smooth spatial weights and a nearby-pair Hamiltonian make sums meaningful. Proposition22 differentiates the Hamiltonian with integrable domination and estimates all error terms. Lemma24 says large Hamiltonian forces large energy, and Corollary25 shrinks the Hamiltonian in finite time. The target is \(\int_{\Lambda/4}^0\widetilde E^{[.5T\log T,3T\log T]}(t)dt=o(T\log^3T)\).
7. **§8, Propositions26–28 (pp55–58): corrected passage to time0.** A *fixed reference interval* has controlled integrated energy in dyadic windows about its endpoints (Proposition27). Short time steps of size \(\ll\log^{-2}T\) propagate energy to a slightly shrunken interval (Proposition28). Boundary gaps chosen at the final step stay open backwards across that step. Repeating \(O(\log^2T)\) times loses only \(O(\log^5T)\) indices and polylogarithmic errors, yielding \(\widetilde E^{[T\log T,2T\log T]}(0)=o(T\log^3T)\). Footnote16,p55 explicitly thanks OferZeitouni for an error in a previous argument; this correction is distinct from the estimates examined below.
8. **§9 (p59): arithmetic non-clock behavior contradicts relaxation.** Nonnegativity and coercivity ofV imply almost every normalized neighboring gap tends to1. The Conrey–Ghosh–Goldston–Gonek–Heath-Brown small-gap theorem cited as[7] gives a positive fraction below any fixed \(\lambda>.77\), contradicting that conclusion. Its RH hypothesis is available under the standing contradiction assumption. The source also explains the relation with Montgomery's band-limited pair correlation; it does not assume GUE.

The principal bottleneck for an upper bound \(\Lambda\le0\) is different: one must prove **every** zero of the actual \(H_0\) is real, or construct a valid all-height certificate that forces it. The relaxation contradiction excludes a negative threshold; it supplies no argument excluding a positive one. Finite computation, a finite Li prefix, or a finite-height zero strip cannot replace that global assertion.

## Independent technical reconstruction: local Hamiltonian and boundary term

For a finite setK define ordered-pair sums
\(H_K=\sum_{k\ne l\in K}-\log|x_k-x_l|\),
\(E_K=\sum_{k\ne l\in K}(x_k-x_l)^{-2}\).
Starting with the source ODE, subtraction gives
\[
\frac d{dt}(x_k-x_l)=\frac4{x_k-x_l}
-2(x_k-x_l)\sum_{i\ne k,l}\frac1{(x_i-x_k)(x_i-x_l)}.
\]
The latter sum is absolutely convergent from the macroscopic estimate, because its tails are \(O(\log^2|i|/i^2)\). Thus ordinary differentiation of each finite pair yields
\[
H_K'=-4E_K+2\sum_{i\notin K}\sum_{k\ne l\in K}
\frac1{(x_i-x_k)(x_i-x_l)}.\tag{RT-A401}
\]
The internal triples vanish by the elementary identity
\[
\frac1{(c-a)(c-b)}+
\frac1{(a-b)(a-c)}+
\frac1{(b-a)(b-c)}=0.
\]
This proves source Lemma12(v), p30, with its factor2 and ordered-pair convention. On compact time intervals strict simplicity and the uniform macroscopic bounds justify the finite-pair differentiation and uniformly convergent external tail. IfK is an interval of indices, every external point is outside its spatial convex hull, so the environmental products are positive. Hence the environmental term cannot be silently discarded to obtain an upper differential bound. The formula explains exactly why local boundary control is mathematically necessary.

### A valid version of Lemma16's endpoint cancellation

Set \(\delta_j=x_j-\xi_j=O(\log(2+|j|))\). The difference between renormalized and unrenormalized-minus-classical interval energies is the finite linear correction
\(2\sum_{j\ne k\in I}(\delta_k-\delta_j)/(\xi_k-\xi_j)^3\).
For a positive interval \(I=[a,b]\cap\mathbb Z\), write
\(d_j=\min(j-a,b-j)\). Classical spacing and its first correction, source(44)–(45), give
\[
\left|\sum_{k\in I\setminus\{j\}}\frac1{(\xi_k-\xi_j)^3}\right|
\le\log^C(2+b)\left(\frac1j+\frac1{(1+d_j)^2}\right).\tag{RT-A402}
\]
Indeed, the range \(|k-j|\ge j/2\) is \(O(\log^Cb/j^2)\); in the remaining range the leading term is a constant times \((k-j)^{-3}\), while the error is \(O(\log^Cb/(j(k-j)^2))\). Pair the odd leading terms as long as both endpoints permit; the unmatched tail begins at the **nearest endpoint**, and its sum is \(O((1+d_j)^{-2})\). Summing( RT-A402) in j gives a polylogarithm, since \(\sum1/j\ll\log b\) and \(\sum(1+d_j)^{-2}\ll1\). Multiplying by \(\max|\delta_j|\) proves Lemma16's stated polylogarithmic energy correction. Negative intervals follow by symmetry. For an interval crossing0, the positive/negative cross correction is bounded absolutely by \(\sum_{r\ge1}\log^C(2+r)/r^2<\infty\), so the same result follows by splitting signs.

The source p40 instead prints a bound involving the *maximum* of endpoint distances, without1. That specific intermediate expression fails for j at a long interval's endpoint: the unmatched cubic sum is at least1 while the printed upper expression tends to0. The nearest-endpoint estimate above repairs the aggregate argument and retains Lemma16. This local discrepancy has independent semantic review; final classification is reserved to parent adjudication.

### Independently checked content of the corrected Proposition27

Put \(n=T\log T\). Average the two endpoint anchors independently over intervals of length \(.1n\). For a dyadic radiush, any fixed pair of indices can belong to an h-window about one anchor for at most2h units of that anchor's parameter; the other anchor contributes only its interval length. Nonnegativity and Tonelli therefore bound the double-anchor integral by \(O(hn)\widetilde E^{[.5n,3n]}(t)\). Multiply by \(h^{-1}\), sum the \(O(\log n)\) scales, and divide by anchor area \(\asymp n^2\): the mean of the time-integrated boundary-window functional is
\[
O\left(\frac{\log n}{n}\int_{\Lambda/4}^0
\widetilde E^{[.5n,3n]}(t)dt\right)=o(\log^3T)
\]
assuming Theorem17. Thus some fixed reference interval has a polylogarithmic boundary functional. This independently verifies the central averaging mechanism of Proposition27. It does not by itself certify every subsequent estimate in Proposition28.

## Additional printed estimate requiring a separate repair

The literal global positive-sum bound in Lemma21(ii), p46, has an extra \(\log T\) on the classical configuration. Taking \(n=\lfloor T\log T\rfloor\), j in[n,2n], and k=j+r for \(1\le r\le n\), the weights are bounded below by a constant and \(\xi_{j+r}-\xi_j\asymp r/\log T\). Thus the inverse-distance sum is \(\gg n\log T\log n\gg T\log^3T\), while the renormalized energy is zero. Its printed logarithmic prefactor makes it \(\gg T\log^4T\), incompatible with the stated \(O(T\log^3T)\) classical-configuration bound. The source's phrase "similarly if the xi are replaced by ξi throughout" makes this a direct local scope test; neither a fixed constant nor a nearby-pair restriction absorbs the harmonic logarithm.

This is separately corroborated in `audits/adversarial_reviews/rodgerstao_local_semantic_round4.md`. It is **not** a counterexample to Theorem1, nor an assertion about actual Riemann zeros under an impossible premise. A signed-far-field replacement for the critical X4 use has been independently derived in `audits/adversarial_reviews/rodgerstao_far_field_advocate_round4.md`; that reconstruction is pending further review. Later uses with polynomial error factors may absorb logarithmic losses, but a whole proof repair must check them explicitly. The whole paper remains Level1, with scoped technical reconstruction only.

## Compatible connections to the archive's heat countermodels

The normalization conversion to Newman1976 is already exact in THM-HF305: \(\Xi_b(x)=8H_{-4b}(2x)\), so \(\Lambda=-4b_0\). A generic model written as a Laplace transform F(w) corresponds to a Fourier transform through w=iz; multiplication of its kernel by \(e^{\tau u^2}\) has the same backwards-Fourier-heat sign as the source. When matching the source's zeta variable, however, \(w=s-1/2=iz/2\); that extra dilation changes numerical heat parameters by a factor4. The countermodel comparisons below concern signs and compatible hypotheses, not an unconverted numerical threshold.

* THM-HF306–309 give even nonnegative atomic kernels, and then strictly positive smooth super-Gaussian densities, with **positive finite** heat thresholds and arbitrarily long finite positive Li-type prefixes. The smooth version satisfies deBruijn's function hypotheses; the atomic version alone does not. These examples refute an upper bound \(\Lambda\le0\) deduced solely from those generic kernel conditions or finitely many such coefficients.
* Positive smooth quartic kernels can have threshold \(-\infty\). Therefore even the lower bound \(\Lambda\ge0\) is not a theorem of positivity/smoothness/super-Gaussian decay alone. Rodgers–Tao's actual Riemann macroscopic density and arithmetic non-clock gap input are substantive extra ingredients.
* The archive's Bessel-quartet model strengthens the upper-bound obstruction by matching the two smooth Riemann–vonMangoldt terms with bounded remainder and allowing only four off-line zeros, while retaining a positive smooth double-exponential kernel. It still fails the ordinary Dirichlet-series arithmetic boundary: its standard-gamma uncompletion grows as a positive constant times \(\sigma^{7/4}\) on the positive real axis. Hamburger converse inputs therefore cannot be imported into that model. It does not have the actual zeta small-gap arithmetic input assumed in the source contradiction.

The concrete research target is consequently not another generic positivity condition: it is a source-specific all-height zero-exclusion certificate, or an arithmetic statement supplying such a certificate while surviving these controls. A precise near-term audit target is a fully checked version of Proposition22 using the signed far-field asymptotic, followed by exact checking of each remaining use of Lemma21. This is a reusable proof-verification problem, not an RH proof campaign outcome.

## Evidence and audit limits

Private source and page hashes are recorded in `sources/rodgerstao_advocate_round4/source_manifest_advocate_round4.json`; no source PDF is added to the public archive by this note. Full version/correction comparison is the separate semantic support review. The source text was read fully, but earlier Csordas–Smith–Varga zero-dynamics inputs, the entire steepest-descent proof, and the small-gap theorem were not each given independent technical audits here. Main theorem status is an established published result being mapped, not newly proved by this research program. The local estimates and proposed repair are explicitly separated from that status.
