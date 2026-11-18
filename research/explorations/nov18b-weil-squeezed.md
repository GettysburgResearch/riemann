# A positive arithmetic space with only an additive triple-log margin

**Proposed unconditional theorem.** For all sufficiently large real \(q\), write \(T=2\pi q\) and \(L=\log q\). There is an explicit space \(V_q\) of dimension \(\asymp \sqrt q\,L^{1/3}/\sqrt{\log L}\), consisting of compactly supported smooth tests whose logarithmic support has length \(\log q+o(1)\). Its smallest normalized Weil value lies between
\[
 \tfrac12\log\log L-O(1)
 \quad\hbox{and}\quad
 \log\log L+O(1).
 \tag{1}
\]
The bounds hold at every such carrier. Each test has gamma energy \((\log q+o(1))\|g\|^2\) and negligible pole term. Thus this space includes actual prime terms equal to the whole gamma main term up to an additive \(O(\log\log\log q)\); the lower bound controls every coefficient vector to the same order. This is a subspace theorem. In particular it does not bound the Weil form on arbitrary Mellin waves at this carrier.

## Matched profiles and unequal cutoffs

Put \(e=L^{-1/3}\), \(A=C\sqrt{\log L}\) for a sufficiently large fixed \(C\), and \(r=\sqrt q\). Use the two families of centered, \(L^2\)-normalized, Mellin-modulated packets from [the two-comb estimate](nov18b-weil-combs.md). In the physical coordinate scaled by \(r\), the low profile begins as the unit Gaussian proportional to \(\exp(-\pi u^2/e^2)\). Choose the unit high profile to attain equality in the [Fresnel coupling](nov18b-weil-fresnel.md), i.e. its additive Fourier transform equals that of the low profile times a quadratic phase of modulus one chosen so the absolute coupling is one. With the conventions there the phase can be taken to be \(e^{i\pi\xi^2}\); any constant unit phase is immaterial. For these Gaussians the absolute cross correlation at displacement \(w\) is exactly
\[
 B(w)=\frac{\sqrt 2 e}{(1+4e^4)^{1/4}}
       \exp\left(-\frac{2\pi e^2 w^2}{1+4e^4}\right),
 \qquad M:=\int B=(1+4e^4)^{1/4}=1+O(e^4).
 \tag{2}
\]
Indeed the Fourier transform of the correlation is \(e^{i\pi\xi^2}|\widehat\phi(\xi)|^2\), where \(|\widehat\phi(\xi)|^2=\sqrt2 e\exp(-2\pi e^2\xi^2)\). Equation (2) follows by a complex Gaussian integral. In particular the absolute correlation mass exceeds one by \(o(1/L)\).

Smoothly truncate the low and high profiles to \(|u|<2Ae\) and \(|u|<2A/e\), with cutoff equal to one to half these radii, and renormalize. Their removed \(L^2\) norms are \(O(\exp(-cA^2))\), with absolute \(c>0\); this holds for the high Gaussian since its physical variance has order \(1/e^2\). The cross correlation \(K\) changes pointwise by at most \(O(\exp(-cA^2))\). Its support is contained in \([-4A/e,4A/e]\). Its Fresnel coupling differs from one in absolute value by \(O(\exp(-cA^2))\) by unitarity. Choose \(C\) large enough that these errors are at most \(L^{-20}\).

Fix \(c_0=20\). In the low and high sums use the indices \(1\le n\le N_1\) and \(1\le m\le N_2\) respectively, with
\[
 N_1=\left\lfloor\frac r{c_0 A e}\right\rfloor,
 \qquad N_2=\left\lfloor\frac{r e}{c_0 A}\right\rfloor.
\]
These unequal cutoffs keep the physical packets disjoint within each family, ensure that within-family prime overlaps require exact integer divisibility, and leave a central gap \(b=\log(q/(N_1N_2))=2\log(c_0 A)+o(1)\). For example, two matched low centers under a possible shift would require \(|dn-m|\le(1+o(1))4AeN_1/r<1\), and likewise on the high side with \(e\) inverted. The entire centered log support has length \(\log q+O(A/(er))\). The systems are orthonormal, including orthogonality between the low and high spaces.

## A one-sided row estimate for every coefficient vector

The diagonal within-family weighted rows are at most \(\log N_i+O(1)\) with the weights \(n^{-1/2}\) on both sets, as in the comb note. In a low-to-high cross row, fix \(n\) and put \(y=r/n\), \(x=q/n\). Each possible overlap at \(l=dm\) has \(w=(l-x)/y=O(A/e)\). Replacing \(|K(r\log(nl/q))|\) by the upper bound \(B(w)+O(L^{-20}+q^{-1/2}L^{O(1)})\) follows from (2), Gaussian truncation, and Taylor's theorem. The ratio of the Schur factor \(\sqrt{n/(md)}\) to \(1/y\) is \(1+O(A/(er))\). In either row orientation these errors cost \(o(1)\) after summation: the number of possible \(l\), divided by \(y\), is \(O(A/e+1/y)\), and \(\sum_{d\mid l}\Lambda(d)\le\log l=O(L)\).

Here is the useful counting estimate. On the relevant interval,
\[
 \sum_{m d=l,\,m\le N_2}\Lambda(d)
   \le\log l-\sum_{d\mid l,\,d\le D}\Lambda(d),
 \qquad D=\min\{y/e,\,x/(2N_2)\}.
\]
All displayed subtracted divisors have \(l/d>N_2\). The Gaussian sum over all integers satisfies
\[
 \frac1y\sum_l B((l-x)/y)=M(1+O(\exp(-c(y/e)^2))).
\]
For the subtracted multiples of \(d\le D\), their analogous sum is \(M/d\) up to an absolute error \(O(d^{-1}\exp(-c(y/(ed))^2))\). Both statements follow from Poisson summation and the Gaussian Fourier transform; in the latter \(y/(ed)\ge1\). The sum of the latter errors with weights \(\Lambda(d)\) is \(O(1)\), by dyadically grouping \(d\) below \(y/e\) and using \(\sum_{d\asymp H}\Lambda(d)/d\ll1\). The subtracted sums may be restricted to \(|w|\le 5A/e\) with loss \(O(d^{-1}e^{-c'A^2})\) each, by the same Gaussian decay and lattice spacing at most one Gaussian scale. To justify using this larger interval, bound the original nonnegative cross row by the full majorant \(B(w)\) times the restricted-divisor sum on \(|w|\le5A/e\), after paying the preceding profile error. Throughout this interval \(\log l=\log x+o(1)\). Also \(y/e\gg A\) for both row orientations. Increasing the fixed \(C\) as needed makes the other exponential errors negligible even after multiplication by \(O(L)\). Thus
\[
 \text{weighted cross row}\ \le\ M(\log x-\log D)+O(1).
 \tag{3}
\]
All multipliers and errors in (3) are uniform over the stated ranges. The same argument applies starting at a high index with \(x=q/m\), \(y=r/m\), and the opposite cutoff \(N_1\), since the absolute cross majorant is symmetric.

In a low row, \(D=y/e\), giving \(\log x-\log D=\log(re)\). In a high row, \(D=x/(2N_1)\), giving \(\log x-\log D=\log(2N_1)\). As \(M-1=o(1/L)\), (3) bounds the combined diagonal and cross rows by, respectively,
\[
 \log N_1+\log(re)+O(1)\le L-\log(c_0A)+O(1),
 \qquad \log N_2+\log N_1+O(1)\le L-2\log(c_0A)+O(1).
\]
The Schur test bounds the prime form for all coefficient vectors. Derivatives of each rescaled profile of any fixed order have at most polynomial growth in \(L\). Hence the Fourier tails beyond \(|t-T|\le q^{3/4}\) and both pole evaluations are negligible by the same integrations by parts as for fixed profiles. On this band the gamma multiplier is \(L+O(q^{-1/4})\). This proves the lower bound in (1).

## A vector attaining the additive order

Take the coefficients \(n^{-1/2}\), \(m^{-1/2}\) in both families and choose their relative phase to maximize the signed prime term. The squared norm is \(H_{N_1}+H_{N_2}\), while the scalar cross term, after removing a constant unit phase, is
\[
 I\left[H_{N_1}\log q-J_{N_1}-J_Q+
       \sum_{d\le Q/N_1}\frac{\Lambda(d)}d
             (H_{\lfloor Q/d\rfloor}-H_{N_1})\right]+o(1),\qquad Q=q/N_2 .
 \tag{4}
\]
This is the [integer-sum calculation](nov18b-weil-fresnel.md) with separate cutoffs. For clarity, its error estimates continue to hold here. The profile support and all its fixed derivative and Fourier seminorms grow by at most fixed powers of \(L\). The range of the outer divisor \(h\) is \(O(r L^{O(1)})\); the exceptional divisors in the threshold replacement lie in an interval of length at most a fixed power of \(L\) around \(Q\) and each has at most \(L^{O(1)}\) relevant multiples. Likewise the step sizes \(d\le Q/N_1=O(A^2)\) are polylogarithmic. In the Poisson and second-derivative estimates, split at \(|j|\le L^B r^{-1}H\) with any sufficiently large fixed \(B\), or sum their Schwartz weight directly. On dyads bigger than \(r\) their upper ratio \(H/r\) is only polynomial in \(L\). The same inequalities then lose only \(L^{O(1)}\) on the previous \(q^{-1/4}\) error. Equivalently, the total is \(O_\delta(q^{-1/4+\delta})\) for any fixed \(\delta>0\), in addition to the smaller Taylor and threshold errors. This verifies the asserted \(o(1)\) for these specified profiles.

With \(x_i=\log N_i\), \(b=L-x_1-x_2\), the bracket in (4) is \(H_{N_1}H_{N_2}+D(b)+o(1)\) by the same expansion. Here \(D(b)=O(1+b^2)\) already suffices, by the first Mertens bound. The absolute coupling is \(1+O(L^{-20})\). Consequently the signed prime term, including the two exact diagonal contributions \(2J_{N_1}+2J_{N_2}\), is
\[
 (x_1+x_2)(H_{N_1}+H_{N_2})+O(1+b^2).
\]
Dividing and adding the gamma and pole comparisons gives \(W/\|g\|^2=b+o(1)=\log\log L+O(1)\) on this explicit direction. This proves the other half of (1). The square-root-scale prime sum and the Fresnel match are essential to this upper comparison; positivity of the diagonal blocks would not give it.
