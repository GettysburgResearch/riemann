# Independent final QA of the Round 15 Mellin director note

**Disposition.** The packet witness, both explicit sampling constants, tail indexing, both approximation arguments, smooth strict inclusion and finite-cutoff correction pass. One explanatory sentence should identify multiplication by a log-coordinate cutoff as a weighted Fourier convolution. The bounds and conclusions require no change. Checked the complete director note and the controlling author-manuscript passages, with no journal extrapolation or canonical mutation. [Director note](director_mellin_explicit_formula_round15.md)

## Source and packet witness

The 12-page manuscript `sources/uniform121_bombieri_lagarias/bombieri_lagarias_author.pdf` has SHA-256 `cd13c8560f961c68e21256e5ba107bdd08fa7f34ce1e2cffbd4b63a16e8d48e0`. The rendered p. 5 gives (A), (B) and the involution. Rendered p. 6 gives the explicit formula with the actual inclusive height cutoff. Page 7 evaluates the finite part and defines the polynomial inverse Mellin test, p. 8 gives the compact truncation and (3.5), and pp. 9–10 use the limit. The source's stated classical compact test formula is sufficient for the repair, independently of its extension to the broad printed class. I did not inspect a separate journal manifestation for this QA. [Pinned author source](../../sources/uniform121_bombieri_lagarias/bombieri_lagarias_author.pdf)

For the divergent packet test, the phase bound on a radius-\(1/(20j)\) cell is indeed \((j+1/8)/(20j)\le9/160\). The resonant half has a real coefficient at least \(\tfrac12\cos(9/160)e^{-1/16}b_j>b_j/3\), uniformly in \(0\le\beta\le1\). Past, future and nonresonant costs of at most \(b_j/24\) each leave more than \(b_j/5\). The induction constraints are uniform over candidate frequencies above a sufficiently large threshold and over the eventual cell deviations. Riemann–von Mangoldt and pigeonholing still give a cell above that threshold with at least \(j/b_j\) ordinates. One can take a generic lower bin endpoint \(T\) so none of its equal partition endpoints are zero ordinates, excluding only a countable set as the number of cells varies. Conjugation gives the lower bound \(2j/5\) on the real increment. The arithmetic terms are absolutely defined by support at 1 and the stated value bounds. Under the involution, \(\widehat{\widetilde f}(\rho)=\widehat f(1-\rho)\) and the exact finite height subsets are preserved, so symmetrization doubles the failure.

## Exact constants and cutoff indexing

For \(r=\min(\epsilon/2,1/4)\), the radius-\(r\) disk about every point of \([0,1]+i[n,n+1)\) lies in the expanded real-height rectangle used in the note. Let \(E_n\) denote the weighted area integral on that rectangle. The height intervals \([n-r,n+1+r]\) overlap at most twice, since their length is \(1+2r<2\). Also \(|n-t|\le1+r\le5/4\) in each. The bound
\[
 1+n^2\le1+2t^2+2(5/4)^2\le5(1+t^2)
\]
therefore gives the Sobolev comparison \(5^s\). For the critical log weight, \((e+|t|)+5/4\le(e+|t|)^2\), so \(\log(e+|n|)\le2\log(e+|t|)\). Combining the two inequalities gives exactly the required admissible comparison \(w_p(n)\le\sqrt5\,2^p w_p(t)\). These constants need not be sharp.

Disk mean value for \(|h|^2\) gives a cell bound \((\sqrt\pi r)^{-1}(C_w E_n/w(n))^{1/2}\), where the unweighted count constant is absent at this stage. Multiplying by the count \(C_N\log(2+|n|)\) and applying Cauchy–Schwarz over cells brings in the overlap factor 2 under the square root. With \(C_w=\sqrt5\,2^p\), the claimed critical constant is consequently
\[
 \frac{C_N}{\sqrt\pi r}
 \left[2\sqrt5\,2^p
 \sum_{n\in\mathbb Z}\frac{\log^2(2+|n|)}{w_p(n)}\right]^{1/2}.
\]
The analogous Sobolev formula follows by taking \(C_w=5^s\). Both use the half-open bookkeeping cells, regardless of the inclusive spectral cutoff. For a removed ordinate \(\gamma>T\), its integer cell has \(n> T-1\). For \(\gamma<-T\), it has \(n\le\gamma<-T\), so the same restriction \(|n|>T-1\) is valid. Integral comparison then gives the power-log and logarithmic tail bounds printed in the note.

Integrating the disk estimate over a fixed vertical line cell by cell proves the required weighted trace on every \(\beta\in[0,1]\). For example, applying the disk bound directly with comparability of \(w(v)\) and \(w(t)\) when \(|v-t|\le r\) gives a finite constant independent of the selected \(\beta\). The exact coefficient above is for **zero sampling**. The trace assertion only needs a bounded constant and does not use \(C_N\).

## Archimedean endpoint and approximation

For the critical trace, split the Cauchy–Schwarz integral for the central modulus at \(\sqrt R,R\) with \(R=1/|u|\). The three bounds are \(O(R^{-1})\), \(O((\log R)^{-p})\) and \(O((\log R)^{1-p})\). Indeed in the first range \(u^2t^2/\langle t\rangle\le u^2|t|\), in the second one also has \(\log(e+|t|)\gg\log R\), and in the third one integrates \(1/(t\log^p t)\). Taking the square root gives the stated Dini modulus for \(p>3\). The Sobolev case supplies a Hölder exponent strictly between 0 and \(\min(1,s-1/2)\). In the change \(x=e^u\), the critical archimedean numerator is \(e^{-u/2}(F(u)+F(-u))-2e^{-2u}F(0)\). Either modulus plus \(O(u)\) is integrable against \(du/u\). The value bounds control the integrals and prime sum away from this endpoint.

For either strip weight, an even log-coordinate cutoff acts on each line profile by multiplication, hence by Fourier convolution with a uniformly bounded weighted \(L^1\) kernel. This is the suggested terminology adjustment to “bounded Fourier multipliers” in the Sobolev discussion. The stated operation and norm estimate are valid. Strong convergence follows first on Schwartz profiles and then by weighted density. At fixed cutoff, convolution of the central profile by a smooth even mollifier gives the linewise Fourier multiplier obtained by tilting that mollifier by \(e^{(\beta-1/2)u}\). It is uniformly bounded on the excess strip and converges to 1. Both approximations thus converge in the integrated strip norm, and their spectral sides converge absolutely by sampling. Near 1 the cutoff changes nothing once it equals one there. At fixed cutoff convolution with a nonnegative mollifier preserves a common central modulus, giving dominated convergence of the archimedean endpoint. Prime arguments lie in a fixed compact set during mollification, and under expanding cutoff they are dominated by the original value envelope. These steps justify passage from the classical smooth compact formula without invoking the false broad version. [Sobolev proof](analytic132_mellin_trace_repair.md) · [Critical proof](analytic135_critical_log_mellin_repair.md)

## Smooth strict inclusion and compact-cutoff witness

For the strict-inclusion example, the packets are disjoint and locally finite, and their amplitudes give \(f(x)=O(x^{-2})\) at infinity and zero near zero. On each line \(-1/4\le\beta\le5/4\), the weighted norm of the \(j\)-th packet is bounded by a constant times
\[
 a_j e^{(\beta-1/2)j}w_p(\Gamma_j)^{1/2}
 \ll j^{-2}e^{-5j/4}.
\]
This follows from moderation of \(w_p^{1/2}\) and uniform Schwartz bounds on the fixed translated profile. Its sum is finite uniformly in the strip. On a fixed sufficiently small window about \(\Gamma_j\), demodulation leaves the matching coefficient bounded below in modulus by \(c a_j e^{(\beta-1/2)j}\). The phase \(e^{i(t-\Gamma_j)j}\) has modulus one. The off-carrier total is \(O_M(\Gamma_j^{-M})\) uniformly in the strip, using offset separation and \(\sum_k a_k e^{3k/4}<\infty\); it is smaller than even the worst matching coefficient. On the fixed positive-measure substrip \(1/2\le\beta\le3/4\) the lower bound is thus \(c'a_j\). Integrating the Sobolev norm there and over the disjoint windows gives a lower bound by
\[
 \sum_j \Gamma_j^{2s-1}\log(e+\Gamma_j)^{-p}j^{-4}e^{-4j}.
\]
The terms diverge for each \(s>1/2\) because \(\log\Gamma_j=j^2\log2\). A Sobolev comparison on a central line alone was unnecessary. This proves strict inclusion even for smooth value-decaying tests. There is no claim at \(p=3\) or about an optimal test space.

Finally, in the rendered p. 8 equation (3.5) at \(n=1,\epsilon=2/3\), the two ordinary integrals give \(\log(3/2)+1/3\) and there is no prime term. The truncated archimedean integral is \(\int_1^{3/2}dx/[x(x+1)]=\log(6/5)\). The separate compensation integrand persists above \(1/\epsilon\); its missing contribution has the positive sign and exact size \(-\tfrac n2\log(1-\epsilon^2)\), giving \(\tfrac12\log(9/5)\) in the witness. The error vanishes in the limit. These fixed compact tests have the known \(1/\rho\) endpoint contributions and the absolutely summable remainder, so their valid midpoint formula does not depend on either continuous-test repair. The main theorem and the pinned local findings are properly distinguished. No change to author flags, corpus status or canonical records is made.
