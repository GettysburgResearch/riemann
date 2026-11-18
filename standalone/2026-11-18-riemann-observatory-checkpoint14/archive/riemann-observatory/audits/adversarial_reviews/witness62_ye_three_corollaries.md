# Independent check of three short-height consequences of Ye v2

I checked the pinned arXiv 2610.15989v2 PDF, SHA-256 `315819f42df41c3980ada66a171d7c2d257679c3f7100670ed298cb0bb2634f1`. The source passages used are §1, Theorems 1.1–1.3 and (1.7)–(1.11), §2 (2.17), §3 Proposition 3.3 and (3.14), and §4 (4.2). The same-height reflection \(1-\bar\rho\) in the proof of Proposition 3.3 is visible in the rendered p. 16. The checks derive consequences of the source results, using the fourth moment as cited in (2.17). The oscillatory consequence retains the external boundary \(\Re\rho\le7/8\), cited by Ye to his reference [17]. Its validity is unverified in this review. [Pinned primary source](https://arxiv.org/pdf/2610.15989v2)

## Short fourth moment and zero density

Theorem 1.1 includes zeta and requires (1.1) for every loss \(\eta>0\), uniformly for all sufficiently large real starts \(U\). The moment (2.17) holds for \(2/3\le a\le1\) in Ye's cited form. For a fixed \(0<a<2/3\), the length-\(U^a\) interval is contained in the length-\(U^{2/3}\) interval with the identical real start \(U\), so the nonnegative integral obeys (1.1) with \(\ell=2,\theta=2/3\). There is no shift to a grid or to an averaged start. The condition \(\theta\ge a\) is satisfied, and for \(a\ge 2/3\) the direct choice \(\theta=a\) works. The Type II denominator becomes \(2(2\sigma-1)+4(1-\sigma)=2\). Therefore
\[
 N_\zeta(\sigma;T,T+T^a)\ll_{a,\varepsilon}
 T^{(1-\sigma)\max\{15a/(3+5\sigma),2\max(a,2/3)\}+\varepsilon}.
\]
The count is defined with \(\Re\rho>\sigma\), multiplicities, and inclusive imaginary endpoints. The source range remains \(3/5\le\sigma<1\), and a bounded initial range of \(T\) can be absorbed uniformly in \(\sigma\) using the total zero count there. At \(a=3/5,\sigma=3/4\) the two slopes tie at \(4/3\), giving \(1/3\). The middle branch of Theorem 1.2 at \(a=2/3,\sigma=3/4\) gives \( (2/3)(1/4)(20/9)=10/27\). These are comparisons to direct use of the same paper, independent of the \(7/8\) boundary.

## Single-window weighted estimate

Take \(I=[U,U+U^{3/5}]\), \(U\in[cT,CT]\), and \(0<d<2/5\). Since \(e^{2y}/(1+y^2)\le T^{2\Re\rho-1}\), the zeros in \(I\) with real part between \(1/2\) and \(3/5\), inclusive, give \(O(T^{4/5+\varepsilon})\) by the unit-interval count. For \(s\in[3/5,1)\), Theorem 1.1 with \(a=3/5,\theta=2/3\) has slope at most \(3/2\). The resulting bound \(N_\zeta(s;I)\ll T^{(3/2)(1-s)+\varepsilon}\) is uniform in \(U\in[cT,CT]\), since \(U\) is comparable to \(T\) and \(s\) varies on a bounded range. On the upper slice, directly apply
\[
 \sum_{3/5<\sigma_\rho\le1-d} T^{2\sigma_\rho-1}
 \le T^{1/5}N_\zeta(3/5;I)
   +2\log T\int_{3/5}^{1-d}T^{2s-1}N_\zeta(s;I)\,ds .
\]
The tail count in the right side may include additional zeros above \(1-d\), which only enlarges the bound. This representation handles strict lower and inclusive upper real parts without grid adjustments. The integrand exponent is \(2s-1+(3/2)(1-s)=1-(1-s)/2\), at most \(1-d/2\). The lower-boundary term has exponent \(4/5\). Absorbing logarithms gives the claimed \(O(T^{1-d/2+\varepsilon})\), and choosing \(\varepsilon<d/2\) gives \(o(T)\). Summing this estimate over enough such windows to cover a full dyadic block costs \(O(T^{2/5})\) windows. This gives no global weighted tightness. No external real-part boundary is used here.

## Oscillatory prime-power sum

Ye (1.7) sets \(e(x)=e^{2\pi ix}\) and \(a_\zeta(n)=1\) at prime powers, so the exact sum is
\[
 \sum_{n\ge1}\Lambda(n)e^{2\pi i\alpha n^{3/5}}
      \phi\!\left(\frac{n-K}{K^{7/10}}\right).
\]
Here the fixed \(\alpha\ne0\), fixed \(\phi\in C_c^\infty((-1,1))\), and integer \(m=1\) satisfy (1.8)–(1.9) for all sufficiently large real \(K\). Parameters are \(b=3/5\), \(v=w_0=a_0=q=3/10\), with \(\delta=1-\beta/2\) exactly. Proposition 3.3 (3.14) applies. Its shorter-window (3.15) requires a strict inequality and is not used. Choose once and for all the allowed \(\eta=1/200\). The enlarged window \(J\) has length \(O(K^{61/200})\) and lies at absolute height \(\asymp K^{3/5}\). Reflection by zeta's conjugate symmetry makes it positive if needed. A single interval at its lower endpoint \(T\) with exponent \(a=13/25\) eventually covers it, since \(T\asymp K^{3/5}\) and \(T^a\asymp K^{39/125}\), with \(39/125>61/200\). The Type I slope is at most \((5/2)a=13/10<4/3\). The short fourth moment yields uniformly for \(3/5\le s<1\) the local upper count
\[
 N_\zeta(s;J)\ll_\varepsilon K^{(4/5)(1-s)+\varepsilon}.
\]
The fixed margin in the covering avoids any need for uniformity as \(a\) varies.

The zeros with \(1/2\le\sigma_\rho\le3/5\) contribute \(O(K^{181/200+\varepsilon})\) to \(\sum K^{\sigma_\rho}\) by the unit-interval count. Under the separate \(\Re\rho\le7/8\) assumption, the remaining weighted sum is exactly
\[
 K^{3/5}N_\zeta(3/5;J)
 +(\log K)\int_{3/5}^{7/8}K^sN_\zeta(s;J)\,ds .
\]
A zero at \(7/8\) contributes its full weight even though the count uses strict real-part thresholds. The exponent of the first term is \(23/25\), and the affine integrand exponent \(s+(4/5)(1-s)\) increases to \(39/40\). Inserting this estimate into (3.14) and multiplying by \(K^{-3/10}\) gives \(O(K^{27/40+\varepsilon})\) uniformly for large real \(K\), with constants for the fixed phase and cutoff function. That is a pointwise oscillatory estimate under the external boundary hypothesis.

At these parameters Theorem 1.3 uses \(\nu_m=2/5\) and the second branch of \(Q\), since \(91/230<2/5<169/300\). Its exponent is \(7/10+(9/13)(2/5)-3/10=44/65\). Subtracting \(27/40\) gives \(1/520\). Both exponents are compared at the same external boundary. I found no parameter failure in the three proposed corollaries. This does not verify a proof of the external cutoff, the original detector or the cited moment theorem from first principles.
