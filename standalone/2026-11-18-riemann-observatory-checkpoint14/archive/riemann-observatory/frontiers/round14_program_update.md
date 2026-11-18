# Round 14 frontier update

18 November 2026. This guide records adjudicated results and open problems in the archive. The arithmetic estimates below concern selected parts of a signed remainder. No full fourth-moment extension or publication-priority conclusion follows. [Round 14 synthesis](../final_synthesis/round14_report.md)

## Arithmetic missing estimate

Let \(D(s)=\sum_{Y^a<p\le Y^b}p^{-s}\), let \(c_k\) be the coefficients of \(D^4\), and put \(C_*=d_2*(\Lambda\log^2)\). For fixed \(0<a<b\), \(1/8<b<1/6\), and \(T\asymp Y\), the sufficient estimate for the remaining pure fourth arm is
\[
\Re\sum_{k\le Y^{4b}}\frac{c_k}{k}
  \sum_{m\ge1} C_*(m) w_T(2\pi m/k)
  \left[e(-m/k)-\frac{\mu(q)}{\varphi(q)}\right]
  =o(T\log^4T),
\qquad q=\frac{k}{(k,m)},\qquad e(x)=e^{2\pi ix}.
\]
Here \(w_T\) is the compact comparable-height cutoff with two smooth transitions of width \(H=T^\kappa\), for fixed \(\kappa<1\) sufficiently close to one for the chosen exponent margins. The mixed arms, smooth saddle replacement, and divisor terms are controlled. The arithmetic stratum estimates are unconditional. The transfer from the displayed estimate to the strict derivative-weighted fourth moment uses RH. [Reduction](../audits/adversarial_reviews/director_pure_fourth_round13.md) · [Stratum estimates](../audits/adversarial_reviews/director_arithmetic_strata_round14.md)

Opening \(C_*\) by its Mangoldt factor \(\nu=p^j\) removes shared prime factors, every \(j\ge3\), and short factors satisfying \(\nu/(k,\nu)^2\le H^2T^{-\delta_0}/(kT)\) with fixed \(\delta_0>0\). All square factors also save a power for \(1/2<\theta=4b<9/17\). For coprime genuine primes on blocks \(K\asymp T^\theta\), \(P\asymp T^\xi\), \(1/2<\theta<2/3\), the proved open regions are

| Input | Exponent conditions |
|---|---|
| Baker | \(\theta/2<\xi<\theta\), \((11/10)\theta+(4/5)\xi<1\), and \(\theta+(11/12)\xi<1\) |
| Fouvry–Shparlinski | \(0<\xi<(3/2)\theta\), \((13/10)\theta+(3/5)\xi<1\), and \((13/12)\theta+(5/6)\xi<1\) |

These use common prime endpoints, a uniform smooth dual-kernel envelope, and reduction of nonunit dual indices to their actual moduli. A separate pointwise Korolev argument covers a neighborhood of \(P=T^{1-\theta}\) on the top blocks when \(1/2<\theta<10/17\). The main target is cancellation on the remaining prime scales, which can reach \(P\asymp KT\). When \(\theta\ge9/17\), the full square stratum also remains outside the stated power-saving result. [Exact domains and dependencies](../audits/adversarial_reviews/director_arithmetic_strata_round14.md)

## Obstructions and intrinsic matrix work

- **Full-sequence contour shifts.** The character twist of \(C_*\) is \(L(s,\chi)^2(-L'/L)''(s,\chi)\). It has residue \(-2L'(\rho,\chi)^2\) at each simple character zero \(\rho\), with the potential singularities at multiple zeros removable. Freezing the prime factor before divisor Voronoi leaves a valid route. [Character-twist check](../audits/adversarial_reviews/director_arithmetic_strata_round14.md)
- **The first moment discrepancy can occur much earlier than Hankel failure.** The intrinsic CUE coefficient window is \(rb\le1\), and the RH-conditional arithmetic window is \(rb<1/2\). The formal CUE cosine series admits an explicit finite negative-square witness at every fixed rank. At rank one the least Hankel order \(L\) is the first for which the largest zero of \(\operatorname{He}_{L+1}\) exceeds \(\sigma/d\), where \(\sigma^2=\log(b/a)/2\) and \(d=b-a\). For \(a=b/2\) this order is asymptotic to \((\log 2)/(2b^2)\), while the first raw-moment crossing occurs at \(\lfloor1/b\rfloor+1\). Least witness orders for higher ranks remain a separate problem. [Window and first crossing](../audits/adversarial_reviews/director_cue_windows_round13.md) · [Quantitative witnesses](../audits/adversarial_reviews/director_quantitative_rmt_round14.md)
- **The exact factors have a positive finite representation.** On the real Laplace axis, Petrov’s tilted-to-ambient Fredholm ratio is a positive \(J\)-dimensional Schur determinant computable from finite matrices. It lies in \([\exp(-H_Nz^2/4),1]\). The continuum Gram uses the actual integration interval from \(\max(p,q)\) to one and vanishes when either shift exceeds one. Truncating the Hankel operator after a prescribed number of bandwidth blocks gives a factorial error uniform in matrix size on compact real parameter intervals. These tools support certified evaluation and the study of later intrinsic frequency chambers. [Exact positive factors and approximation](../audits/adversarial_reviews/director_quantitative_rmt_round14.md)

The [ranked research problems](../final_synthesis/top_25_research_opportunities.md) connect these questions with the rest of the archive.
