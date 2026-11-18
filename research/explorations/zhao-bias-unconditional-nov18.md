# Unconditional sign changes for a positive proportion of quadratic discriminants

Write \(P_D(x)=\sum_{p\le x}\chi_D(p)\), \(H_D(x)=\int_2^xP_D(t)\,dt\), and \(I_D(x)=x^{-3/2}\log x\,H_D(x)\). The following consequences concerning [Zhao's question 2 in §8](https://doi.org/10.1007/s40993-025-00640-y) require no GRH.

* For every fixed \(A>0\), the lower relative density of discriminants with \(\limsup I_D>A\) and \(\liminf I_D<-A\) is at least \(1/5\) among \(D=-8d\) with \(d\) positive odd squarefree. Among all negative fundamental discriminants the lower relative density is at least \(1/30\).
* For each of \(D=2221,2237,2269,-2207,-2239,-2287\), \(H_D\) has both signs arbitrarily far out.

## The off-critical case

For real primitive nonprincipal \(\chi=\chi_D\), let \(R\) be the greater of \(1/2\) and the supremum of its real nontrivial zeros, using \(R=1/2\) if there are none. If there is a nonreal zero with \(\Re\rho>R\), then for each \(\max(R,1/2)<c<\Re\rho\),
\[
 \limsup_{x\to\infty}x^{-1-c}H_D(x)=+\infty,\qquad
 \liminf_{x\to\infty}x^{-1-c}H_D(x)=-\infty .
\]
To prove this, for \(\Re z>1\) integrate each summand \((x-p)_+\) to obtain
\[
 \int_2^\infty H_D(x)x^{-z-2}\,dx=
 \frac1{z(z+1)}\sum_p \frac{\chi(p)}{p^z}.
\]
The prime Dirichlet series is \(\log L(z,\chi)\) plus a holomorphic term on \(\Re z>1/2\), by absolute convergence of the second and higher prime powers there. In particular it has regular continuation along the real interval \((R,\infty)\). A putative eventual upper or lower bound by \(C x^{1+c}\) would give an eventually nonnegative function \(C x^{1+c}\mp H_D(x)\). The abscissa of convergence of its similarly weighted Mellin integral must be at least \(\Re\rho\): a smaller abscissa would continue the prime Dirichlet series holomorphically across that half-plane, impossible because its derivative has a pole of positive residue at \(\rho\). The abscissa is at most one. Landau's singularity theorem now requires a singularity on the real axis there. Both terms are regular on the real interval \((\max(R,c),\infty)\), giving the contradiction. A bounded initial signed segment affects the transform by an entire function. In particular any failure of GRH for a real character having no real zero in \((1/2,1)\) gives unbounded excursions of both signs for \(I_D\). Here functional-equation symmetry supplies a right-half zero.

## Family counting with individual hypotheses

For each fixed \(A>0\), the number of fundamental discriminants of either sign with \(|D|\le Q\) that **satisfy GRH for their own character but fail either strict excursion condition** is \(o_A(Q)\), unconditionally. To check the quantifiers, take the proof of the [finite-dimensional family theorem](zhao-bias-density-nov18.md). For an arbitrarily small \(\eta>0\), take its finite tuple of positive and negative model witnesses with margin two and probability \(>1-\eta\). Truncate at a sufficiently large fixed \(K\); the finite character polynomials then have both witnesses with margin one on a proportion at least \(1-O(\eta)\) of **all** discriminants, by finite-coordinate equidistribution and a union bound. The model truncation error is small in probability by the square-sum tail. In the family the error between \(K\) and \(L=(\log Q)^6\) is small in probability using the unconditional mean-square estimate on all discriminants, increasing \(K\) if necessary. The uniform GRH bound beyond \(L\) is used only on characters satisfying their individual GRH. For each such character outside these unconditional exceptional sets, the two strict prime-tail witnesses and almost periodicity give the required limiting excursions. Taking \(\eta\downarrow0\) yields the claimed count in dyadic intervals and then cumulatively. This deduction does not assume any particular density for the characters satisfying GRH.

By [Conrey–Soundararajan, Theorem 1](https://arxiv.org/abs/math/0111013), the number of odd positive squarefree \(d\le X\) for which \(L(\sigma,\chi_{-8d})>0\) throughout \([0,1]\) exceeds \((1/5)(4X/\pi^2)\) for all sufficiently large \(X\). Among these discriminants, the off-critical case already proves the excursion conditions for every character violating GRH. The preceding counting statement excludes at most \(o(X)\) of the others. This proves the first assertion, since the number of negative fundamental discriminants up to absolute size \(Q\) is asymptotic to \(3Q/\pi^2\) and the specified progression has \(Q/(2\pi^2)+o(Q)\) elements. Conrey and Soundararajan remark that their methods apply in other progressions. Their stated theorem concerns the negative progression just used. For the sign-change conclusion itself one can dispense with family moment estimates: on this real-zero-free progression subset every GRH failure gives the Landau excursions, and every individually GRH-true character with sufficiently large conductor and nonvanishing center gives both signs by the [single-low-zero argument](zhao-bias-central-nov18.md). The family argument supplies arbitrary fixed amplitudes instead.

## Six individual discriminants

The [prime-tail calculation and its rational-error bounds](zhao-bias-kernel-nov18.md) give \(K_{\chi_D}(0)<-1\) for the six characters listed above if they satisfy their individual GRH. Consequently \(\limsup I_D\ge -2/3-K_{\chi_D}(0)>1/3\) by almost-periodic recurrence. Also the Bohr mean of \(K_{\chi_D}\) is \(4m/3\ge0\), where \(m\) is the central multiplicity. Its supremum is at least its mean, so \(\liminf I_D\le-2/3\). If the individual GRH fails, a positive real zero is already excluded at each of these six conductors. For the positive discriminants use [Chua, Math. Comp. 74 (2005), even characters of conductor up to 200,000](https://doi.org/10.1090/S0025-5718-04-01701-6). For the negative discriminants use [Watkins, Math. Comp. 73 (2004), odd characters of conductor up to 300,000,000](https://doi.org/10.1090/S0025-5718-03-01537-0). The off-critical result applies in that case, establishing the same sign statements unconditionally.

## A finite census and correction to the proposed containment

The first stage of the [integer-interval census](../../experiments/X-nov18-quadratic-bias/README.md) gives unconditional sign changes for 5,941 of the 6,086 nonprincipal fundamental discriminants with \(1<|D|\le10,000\), by the same individual dichotomy. The 5,941 split into 2,939 negative and 3,002 positive discriminants. Of these, 4,977 lie strictly outside \([-1151,2161]\), the span reported for the 381 candidates in Zhao's concluding remark. There are substantive discrepancies inside that span.

In particular the [printed Table 3](https://link.springer.com/article/10.1007/s40993-025-00640-y/tables/3) lists \(D=-59\). Its integrated prime count nevertheless has positive values arbitrarily late. At \(X=1\) the simpler [independent Decimal checker](../../scripts/check_zhao_bias_witness_nov18.py) gives \(-0.804<K_{\chi_{-59}}(0)<-0.688\) on GRH. This formula can also be derived directly from the completed Hadamard product: \(K(0)=\Lambda'/\Lambda(-1)-\Lambda'/\Lambda(0)=\Lambda'/\Lambda(1)-\Lambda'/\Lambda(2)\), using the functional equation. Its digamma contribution is \(\log 2-1\) for this odd character. Invoke the real-zero certification for the complementary case. The asserted containment of the Tables 2 and 3 set in the eventual-negative set in §8(2) thus fails already at \(-59\). The comparison \(|\rho(\rho+1)|>|\rho(\rho-1)|\) there decreases the oscillatory majorant, but the constant in the normalized integrated prime-count mean is \(2/3\) where the normalized quantity in Theorem 3 has constant 2. This comparison concerns the two different observables. The theorem about the Mertens integrals in Theorem 3 has a separate statement and proof.

The small example can be replayed from the repository root with
```sh
python -c 'from scripts.check_zhao_bias_witness_nov18 import witness; witness(-59)'
```

The [completed finite classification](zhao-bias-classification-nov18.md) strengthens this to 6,067 unconditional exclusions through conductor 10,000. All remaining nineteen have eventual negative sign precisely if their respective GRH holds. Of the 1,009 nonprincipal fundamental discriminants in Zhao’s reported span from −1151 through 2161, exactly 990 have unconditional sign changes.
