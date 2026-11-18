# Independent check of the Bombieri–Lagarias raw-height counterexample

The printed test hypotheses in the pinned Bombieri–Lagarias author manuscript allow a real \(C^\infty\) function with a finite arithmetic side and a divergent symmetric height-ordered zero sum. The construction is unconditional. It uses only the average density of actual zeta zeros, not a local count at a prescribed height. The compact truncations used in Theorem 2 avoid this failure. This check is confined to the pinned manuscript and enters no canonical finding.

## Controlling statement and conventions

I visually checked pp. 5–10 of the 12-page author manuscript at `sources/uniform121_bombieri_lagarias/bombieri_lagarias_author.pdf`, SHA-256 **cd13c8560f961c68e21256e5ba107bdd08fa7f34ce1e2cffbd4b63a16e8d48e0**. On p. 5, (A) requires continuity and continuous differentiability on the open positive half-line except at finitely many first-kind discontinuities, with the function assigned its midpoint value there. It imposes no derivative bound or total-variation condition at either infinite endpoint in log coordinates. Condition (B) bounds \(f\) itself by \(O(x^\delta)\) near zero and \(O(x^{-1-\delta})\) near infinity for some \(\delta>0\). On p. 6 the source defines \(\widetilde f(x)=x^{-1}f(1/x)\), \(\widehat f(s)=\int_0^\infty f(x)x^{s-1}dx\), and explicitly takes the limit over \(|\Im\rho|\le T\). This is an ordinary height cutoff, without a smoothing factor or a specified restricted height sequence. The endpoint convention for jumps in \(f\) is separate from that for zero ordinates. [Author manuscript](../../sources/uniform121_bombieri_lagarias/bombieri_lagarias_author.pdf)

## Constructing the smooth test

Fix \(\delta>0\), \(0<r<1/5\), and choose \(0\le\psi\in C_c^\infty((-r,r))\) with \(\int\psi>0\). For positive carriers \(\Gamma_j\) to be specified, define
\[
 F(t)=\sum_{j\ge1} a_j\psi(t-j)\cos(\Gamma_j t),\qquad
 a_j=e^{-(1/2+\delta)j},\qquad f(x)=x^{-1/2}F(\log x).
\]
The supports are disjoint and locally finite, so \(f\) is smooth on the full open half-line and is zero in a neighborhood of \((0,1]\). On a packet \(t=j+u\), \(|u|<r\), its absolute value is \(O(e^{-(1+\delta)j})=O(e^{-(1+\delta)t})\). Thus both printed conditions hold, independently of carrier growth. In particular the construction does not substitute a piecewise-defined function with accumulating finite discontinuities.

For \(\rho=\beta+i\gamma\), write
\[
 J_\beta(v)=\int\psi(u)e^{(\beta-1/2)u} e^{ivu}du.
\]
The fixed packet profile gives \(J_\beta(v)=O_M((1+|v|)^{-M})\) for each fixed \(M\), uniformly on \(0\le\beta\le1\), by integration by parts. The dependence of differentiation on the carrier has been removed by putting its two frequencies into \(v\). Changing variables \(x=e^t\) and expanding the cosine gives
\[
 \widehat f(\beta+i\gamma)
 =\frac12\sum_{k\ge1}a_k e^{(\beta-1/2)k}
          \sum_{\pm}e^{i(\gamma\pm\Gamma_k)k}
                  J_\beta(\gamma\pm\Gamma_k).
\]
The interchange is absolutely justified by \(a_k e^{(\beta-1/2)k}\le e^{-\delta k}\) and the uniform \(L^1\) bound on the packet. The transform is also holomorphic in the open strip supplied by (B).

Choose fixed \(c>0\) so small that \(c(1+r)<\pi/3\). When \(|\gamma-\Gamma_j|\le c/j\), the term with \(k=j\) and minus sign has real part at least
\[
 \frac14 e^{-r/2}\left(\int\psi\right)e^{-(1+\delta)j}.
\]
Indeed during integration the phase \((\gamma-\Gamma_j)(j+u)\) stays in the cosine-positive interval uniformly, and the uniform lower envelope for the amplitude uses \(\beta=0\). Impose \(\Gamma_{j+1}\ge4\Gamma_j\) and take all carriers large. Every other oscillatory term, including the plus sign with \(k=j\), has offset at least \(\Gamma_j/2\) in absolute value throughout this same window. For the future carriers this uses their separation, rather than any attempt to bound their total geometric weight by the smaller matching amplitude. Summing the rapid decay against \(e^{-\delta k}\) gives \(O_M(\Gamma_j^{-M})\), with a single uniform constant. Hence we can arrange
\[
 \Re\widehat f(\beta+i\gamma)\ge c_1 e^{-(1+\delta)j}
 \quad\text{for }0\le\beta\le1,\quad
 |\gamma-\Gamma_j|\le c/j
]
by requiring the lower edge of each carrier search range to be sufficiently large. The estimate is uniform over **all** subsequent carrier selections subject to lacunarity.

## Locating the windows and failing the Cauchy test

For each \(j\) choose \(R_j\) sufficiently large, increasing it if needed to satisfy \(R_j>8R_{j-1}\), the off-frequency estimate, and \(\log R_j\ge j^2e^{(1+\delta)j}\). The Riemann–von Mangoldt formula gives \(N(2R_j)-N(R_j)\gg R_j\log R_j\) with multiplicity, uniformly for large \(R_j\). Partition the range into \(O(jR_j)\) cells of width at most \(c/(4j)\). Some cell contains \(\gg\log R_j/j\) zeros. Define \(\Gamma_j\) as its midpoint. Then \(R_j\le\Gamma_j\le2R_j\) and the imposed separation holds independently of which cell wins. This avoids assuming a comparable count in any preassigned short window or asserting that the carrier itself is an ordinate. Enlarge the winning cell to an interval \([T_j^-,T_j^+]\) centered at \(\Gamma_j\) with radius in \([c/(2j),c/j]\) and endpoints avoiding all zero ordinates. Local finiteness suffices. Any additional zeros in the enlarged interval have the same positive real-part estimate. [Classical zero count, Titchmarsh §9.4](../../sources/selberg_round2/titchmarsh_zeta.pdf)

Let \(S_f(T)=\sum_{|\Im\rho|\le T}\widehat f(\rho)\). Reality of \(f\) and zero conjugation pair positive and negative ordinates with equal multiplicities, making their contribution twice the real part. Thus
\[
 S_f(T_j^+)-S_f(T_j^-)
 \gg e^{-(1+\delta)j}\frac{\log R_j}{j}\gg j.
\]
Both endpoint sequences tend to infinity, so the printed height sum fails the Cauchy test. This uses neither RH nor a restriction to simple zeros. The chosen endpoints avoid any ambiguity about a half contribution from a zero on the cutoff itself.

Both ordinary integrals on p. 6 exist absolutely. In fact \(\widetilde f\) is zero on \([1,\infty)\), vanishes near 1, and is \(O(x^\delta)\) near zero. The prime sum is absolute by \(\Lambda(n)\le\log n\) and \(f(n)=O(n^{-1-\delta})\). The \(f(1)\) terms are zero, and the remaining archimedean integral is finite because both functions vanish near 1 and the weight at infinity is \(O(dx/x)\). The divergence concerns the specified zero sum, rather than a cancellation of two undefined arithmetic quantities.

The witness also survives an extra involution symmetry if imposed. For every fixed cutoff, \(\widehat{\widetilde f}(\rho)=\widehat f(1-\rho)\), and \(\rho\mapsto1-\rho\) preserves the multiset and its absolute height. Consequently \(f+\widetilde f\) has precisely twice the displayed increments, still meets (A)–(B), and is invariant under the involution. Global variation or derivative-tail control would change the test class. For example, smooth log-coordinate tests with two derivatives integrable against the appropriate exponential weights have a uniform \(O((1+|t|)^{-2})\) Mellin decay on \(0\le\Re s\le1\), enough for absolute convergence of the zero sum. Local smoothness alone provides no such estimate. An alternative interpreted or averaged spectral limit is outside the asserted raw-height formula.

## Why the compact use in Theorem 2 survives

Manuscript pp. 7–8 define \(g_n(x)=P_n(\log x)\) on \(0<x<1\), with the midpoint at 1 and zero above 1. The proof explicitly notes that \(g_n\) is outside (B), then uses \(g_{n,\epsilon}\) supported on \([\epsilon,1]\) with both endpoint midpoint values. For each fixed \(\epsilon>0\), this is smooth on the interior and has only finitely many endpoint jumps with bounded one-sided derivatives. Integration by parts twice in the compact Mellin integral gives
\[
 \widehat g_{n,\epsilon}(s)
  =\frac{P_n(0)-P_n(\log\epsilon)\epsilon^s}{s}
      +O_{n,\epsilon}((1+|\Im s|)^{-2})
\]
on \(0\le\Re s\le1\) for large \(|\Im s|\). The remainder sums absolutely over zeros. The symmetric \(\sum 1/\rho\) converges by conjugate pairing and the zero count. The symmetric \(\sum\epsilon^\rho/\rho\) reduces to the classical von Mangoldt explicit formula at \(1/\epsilon>1\) by \(\rho\mapsto1-\rho\) and \(1/(1-\rho)=-1/\rho+O(|\rho|^{-2})\). This proves the raw limit for these fixed compact tests, including the classical midpoint convention.

For a direct bridge to the arithmetic identity, mollify the compact log-coordinate profile \(G(t)=e^{t/2}g_{n,\epsilon}(e^t)\) by a real even smooth compact approximate identity of width \(\tau\). Smooth compact profiles satisfy the standard explicit formula. Their zero sums tend to the just-established raw limit: the Mellin multiplier is \(\int\phi(v)e^{\tau(\beta-1/2+i\gamma)v}dv\). Replacing it by the common Fourier multiplier \(\int\phi(v)e^{i\tau\gamma v}dv\) changes the zero sum by \(o(1)\), since the difference is \(O_M(\tau(1+\tau|\gamma|)^{-M})\) uniformly in \(\beta\), and \(|\widehat g_{n,\epsilon}(\rho)|\ll_{n,\epsilon}(1+|\gamma|)^{-1}\). The common multiplier tends to 1 pointwise and has uniformly bounded total variation as a function of positive height, so summation by parts preserves the limit of the convergent paired series. On the arithmetic side only finitely many prime terms can arise on that compact support, and even mollification gives all midpoint values. For the archimedean endpoint at 1, the even part \(G(t)+G(-t)\) is continuous and Lipschitz near zero, with its even mollifications having a common Lipschitz bound; subtracting the value required in the formula gives uniform integrable control there. Ordinary dominated convergence applies to the remaining compact and decaying terms. This justifies the stronger fixed compact-test interface needed for Theorem 2. The subsequent limit \(\epsilon\downarrow0\) in (3.8)–(3.9) is its separate classical zero-free-region and PNT argument. The packet witness does not alter that argument or the multiset criterion.

The independently reconstructed obstruction agrees with the two other checks. It is an actual failure of the displayed combination of (A)–(B) and the specified height limit in the controlling author manuscript. I do not assign it to the separate publisher manifestation or to Weil's original formulation. [Independent packet construction](geometry130_explicit_formula_countermodel.md) · [Independent lacunarity check](weighted130_explicit_formula_countermodel_review.md)
