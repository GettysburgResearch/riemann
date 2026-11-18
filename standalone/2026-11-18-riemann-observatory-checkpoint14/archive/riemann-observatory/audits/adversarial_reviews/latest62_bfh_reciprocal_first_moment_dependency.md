# Technical dependency audit of the BFH reciprocal first moment

17 November 2026. Scoped reconstruction of Bui–Florea–Heycock arXiv:2610.27591v1, Theorem 1.2 (1.4), the omitted proof of Lemma 7.2, and the use on the ordinary Möbius contour. This audit checks the original source formulas and supplies the prime-power and Dirichlet polynomial uniformity arguments. It does not certify the Gaussian recursion or the full paper at Level 2. [BFH v1](https://arxiv.org/pdf/2610.27591v1) · [Bui–Florea accepted manuscript](https://pure.manchester.ac.uk/ws/portalfiles/portal/280630528/BuiFlorea_negative_moments.pdf)

## 1. The exact estimate and contour shift

Write \(U=\log T\), \(h=\log U\), \(a=\alpha U\), and \(W_\alpha(t)=-\log|\zeta(1/2+\alpha+it)|\) for uniform \(t\in[T,2T]\). For fixed \(0<\varepsilon,c<1\), the audited branch gives under RH
\[
T^{-1}\int_T^{2T}|\zeta(1/2+\alpha+it)|^{-1}\,dt
\ll \exp(U^\varepsilon),
\qquad
 C_\varepsilon/h\le a\ll(\log h)^{-c}.
\]
The moment parameter is \(k=1/2\) in \(I_{-k}\), and the reciprocal power is \(2k=1\). The contour applies the result at dyadic height \(Y\) and shift \(b(Y)=B_0/(\log Y\log\log Y)\), with fixed \(\varepsilon=1/3\) and \(B_0\ge C_{1/3}\). It follows that \(b(Y)\log Y=B_0/\log\log Y\), strictly below the scale of a fixed nonzero multiple of \(1/\log Y\) for the shift \(b(Y)\). A shift comparable to \(1/\log Y\) would generally fall outside (1.4). The supplied choice remains in the range as \(Y\to\infty\), with \((B_0/\log\log Y)(\log\log\log Y)^c\to0\). The original theorem covers full dyadic windows. Its positive integrand also majorizes the integral over any retained portion of such a window, with the full-window normalization unchanged.

## 2. Exact primary inequality and the cutoff

The accepted Bui–Florea manuscript, internal pp. 8–9, Lemma 2.2 (2.8), gives the leading reciprocal exponent \((\log t)/(2\log\log t)\log[1/(1-(\log t)^{-2\alpha})]\), an \(O(\log t/\log\log t)\) error, and an \(O((\log t)/(\log\log t)^2)\) error times the same logarithm. Its hypothesis is \(\alpha=o(1/\log\log t)\). In the stated (1.4) shift range \(\alpha\log\log t=o(1)\) uniformly, and \(\log(1/\alpha)=h+O(\log h)\). Thus (2.8) bounds \(W_\alpha(t)\le C_* U\) uniformly for \(t\in[T,2T]\). A fixed \(C_*\) is possible for all \(C_\varepsilon\ge1\), since increasing the lower shift only lowers the largest possible \(\log(1/\alpha)\). This provides the needed version of BFH (7.3).

Let \(U^\varepsilon\le V\le C_*U\), let \(J=\lfloor\log V\rfloor\), and put \(x=T^{J/V}\), so \(\log x=UJ/V\). In this regime \(J\asymp_\varepsilon h\), \(J/V=o(1)\), and \(\log x\gg_\varepsilon h\). Write \(z=\alpha\log x=aJ/V\). Then \(z=o(1)\) and \(aJ\ge C_\varepsilon\varepsilon/2\) for sufficiently large \(T\). By enlarging \(C_\varepsilon\) one can require \(aJ\ge1\), so \(0<\log(1/z)\le\log V\).

Here is a direct recovery of (7.4) from BFH Lemmas 2.1–2.2 on pp. 10–12, with the earlier source Bui–Florea Lemma 2.1 and (2.4)–(2.7) on internal pp. 6–8. In the explicit formula the two displayed errors involving \((\log x)^2\sqrt{x}/(1+t\log x)\) and \((\log x)\log(1+\sqrt t\log x)/\sqrt t\) are \(o(1)\), since \(x=T^{o(1)}\). Replacing \(\log(t/(2\pi))\) by \(U\) in the main penalty costs \(O(1)\), because \(\log(1/z)=O(J)\) and \(\log x\gg J\). For \(p^r\le x\), BFH Lemma 2.2 applied to the explicit coefficients gives
\[
|b_\alpha(p^r;x)|\ll \frac1r+
 \frac{(1+\log(1/z))\log p}{\log x}.
\]
Prime squares contribute \(O(1+\log\log x+\log(1/z))=O(h)\) by \(\sum_{p\le y}1/p\ll1+\log\log y\) and \(\sum_{p\le y}(\log p)/p\ll\log y\). For \(r\ge3\), the corresponding series converges absolutely with bound \(O(1)\), since \(\log(1/z)/\log x=O(1)\). This leaves exactly the prime polynomial \(Q_x(t)\) and the uniform inequality
\[
W_\alpha(t)\le\Re Q_x(t)+\frac{V}{J}\log\frac1{1-e^{-aJ/V}}+O(h).
\]
The calculation retains the full negative additive logarithm that governs the cutoff choice. The bound from the earlier Lemma 2.1 stated directly with its prime-power remainder gives the same result. [BFH explicit formula and coefficients](https://arxiv.org/pdf/2610.27591v1#page=10)

For \(z\) small, \(1-e^{-z}\ge z/2\). Therefore
\[
V-\frac VJ\log\frac1{1-e^{-z}}
\ge\frac VJ\{\log(aJ)-1-\log2\}.
\]
For any fixed large \(D\), choose \(C_\varepsilon\) large enough that this exceeds \(2DV/J\). The \(O(h)\) remainder is \(o(V/J)\) uniformly as \(V\ge U^\varepsilon\). Consequently \(W_\alpha>V\) implies \(|Q_x|>DV/J\). The constants in the coefficient and moment bounds below can be fixed before choosing \(D\) and raising \(C_\varepsilon\): they use only \(\log(1/z)\le\log V\), \(V\le C_*U\) and the fixed shift upper implied constant.

## 3. Prime blocks and the extra factor after \(e^{-V}\)

For \(j=0,\ldots,J-1\), split at \(T^{j/V}<p\le T^{(j+1)/V}\), and call the block \(Q_j\). The full coefficient from BFH Lemma 2.2 satisfies
\[
|b_\alpha(p;x)|\ll 1+Jr(1-r),\qquad r=\log p/\log x.
\]
It is bounded in \(Q_0\) and is \(O(J-j)\) on \(Q_j\), \(j\ge1\). For the block variances one needs the \(O(1/\log y)\) remainder in Mertens' prime reciprocal sum, not just an \(O(1)\) approximation. Its difference over the \(j\)-th block for \(j\ge1\) is
\[
\log((j+1)/j)+O(V/(jU))\ll 1/(j+1).
\]
For the finitely small values whose lower endpoint is below 2, \(jU/V<\log 2\) forces \(j\) bounded, and the elementary estimate gives the same order after enlarging the constant. Hence the coefficient square sums are \(O(h)\) for \(Q_0\) and \(O((J-j)^2/(j+1))\) for \(j\ge1\). These are the elementary block variances in (7.7).

Take \(q_j=\lfloor V/(j+1)\rfloor\). The length of \(Q_j^{q_j}\) is at most \(T\) even at equality, which suffices for the upper-bound form of Montgomery–Vaughan. Unique factorization and the multinomial coefficients give the coefficient square sum of that power at most \(q_j!\) times the unpowered square sum to power \(q_j\). Markov at thresholds \(w/4\) and \(w/(4(J-j)^2)\), respectively, with \(w=DV/J\), then gives
\[
O\!\left((C h J^2/(D^2V))^{\lfloor V\rfloor}\right)
\quad\text{and}\quad
O\!\left((C(J-j)^8/(D^2V))^{q_j}\right).
\]
For the second simplification use \((j+1)(J-j)\ge J\). The thresholds sum to less than \(w\).

Since \(r-8\log r\) has a finite lower bound for \(r\ge1\), a fixed \(D\) can ensure \(\log(D^2 V/[C(J-j)^8])\ge j+5\) simultaneously. The rounding inequality \(q_j(j+5)\ge V+4V/J-(J+4)\ge V+3V/J\) holds uniformly. The first block is \(O(e^{-2V})\) since \(V\ge U^\varepsilon\). Summing at most \(J\) blocks yields \(O(e^{-V-2V/\log V})\), as printed in Lemma 7.2. This factor beyond \(e^{-V}\) is essential to the first reciprocal moment. Below \(U^\varepsilon\) the layer-cake integral is at most \(e^{U^\varepsilon}\). Above it, the remaining integrand is \(O(e^{-2V/\log V})\), and its total integral up to \(C_*U\) is \(o(1)\). This reconstructs Theorem 1.2 (1.4) with uniform constants in the required shift range. [BFH Lemma 7.2](https://arxiv.org/pdf/2610.27591v1#page=36) · [Layer cake, p. 39](https://arxiv.org/pdf/2610.27591v1#page=39)

## 4. Dependency isolation and downstream conclusion

The corrected variance term in the Gaussian recursion, \(O(1+z_\ell^2)\) rather than the uniform \(O(1)\) printed in (6.4), has no path into the estimate audited here. Equations (7.7) and the factorial moments are derived directly for the prime blocks from the coefficients and Mertens' theorem. They never invoke the Gaussian checkpoint variance, Gaussian barrier estimates, or the \(k<1/2\) moment theorem. The two parameters that appear as \(z\) here and \(z_\ell=\log(1/\beta_\ell)\) in the recursion have distinct meanings. [Earlier variance audit](../bui_florea_heycock_latest62_fullsource_round5.md)

In §8.1, the ordinary Möbius contour uses (1.4) at \(\varepsilon=1/3\). At an ordinate comparable to \(Y\), the original kernel \(1/s\) costs \(O(Y^{-1})\). In the twisted contour, an ordinary retained segment away from \(v\approx t\) also has \(|s-it|^{-1}=O(Y^{-1})\). Neither usage requires a moving short-interval estimate, a second reciprocal moment, or a near-ordinate pointwise bound inferred from an average. The \(q=1\) contour handles its local panel with the separate pointwise (2.8). I found no omitted condition in the first-moment input that excludes those applications. This conclusion concerns the first-moment dependency. It leaves the rest of the twisted-contour argument to its separate audits. [Ordinary Möbius contour](https://arxiv.org/pdf/2610.27591v1#page=40) · [Classical-norm transfer](../../proposals/independent_campaigns/mertens_shifted_q1_latest62_round5.md)

Primary copies used were BFH v1, SHA-256 `471eef2f839d4e67f9018c58d8a7fd529dc7bd10271c4b008bfba541d046d555`, and Bui–Florea's institutional accepted manuscript, SHA-256 `0fa36e9efeeb3e96448191f814ec1ae42cbd4c355dad2863b7ba552b32127921`. The latter contains the exact (2.8) error used here and the related arXiv v1 displays the same bound. The external Carneiro–Chandee explicit formula and Montgomery–Vaughan mean-value theorem are treated as established inputs.
