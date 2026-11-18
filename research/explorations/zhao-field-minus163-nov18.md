# Unconditional prime-ideal oscillations for the field of discriminant −163

Let \(K=\mathbb Q(\sqrt{-163})\). For the [integrated prime-ideal harmonic error](zhao-field-sign-equivalence-nov18.md) put \(A_K(X)=(\log X)J_K(X)/\sqrt X\). Then
\[
 \liminf_{X\to\infty} A_K(X)<-4.81561,\qquad
 \limsup_{X\to\infty} A_K(X)>8.81561 .
\]
These bounds are unconditional. Only one low zero and finitely many of its harmonics enter the computation. [Interval replay](../../scripts/check_zhao_minus163_nov18.py)

Write \(\chi=(\frac{-163}{\cdot})\), so \(\zeta_K=\zeta L(\cdot,\chi)\). On the real segment \([1/2,1]\) the character partial sums \(S(x)=\sum_{n\le x}\chi(n)\) have absolute value at most 9, as one full period verifies. Differentiation of \(L(s,\chi)=s\int_1^\infty S(x)x^{-s-1}dx\) bounds \(|L'(s,\chi)|\le 18/s\le36\) there. Arb encloses \(L(j/512,\chi)>0.067\) at all integers \(256\le j\le512\). The maximum distance to this grid is \(1/1024\), giving strict positivity on the entire segment. The alternating eta series gives \(\zeta(s)<0\) on \([1/2,1)\). Thus a failure of the individual GRH forces both normalized signed limiting superiors to be infinite by the [Mellin and Landau argument](zhao-field-sign-equivalence-nov18.md).

Suppose the individual GRH holds. Then \(A_K(e^u)=P(u)+o(1)\), with absolutely convergent almost periodic profile
\[
 P(u)=2+\sum_{\rho=1/2+i\lambda}
             \frac{e^{i\lambda u}}{1/4+\lambda^2}.
\]
There is no central zero by the preceding real-segment check. Hardy values for \(\chi\) have opposite signs at \(1/5\) and \(21/100\). Bisection encloses a zero ordinate \(\gamma\) in \(0.202901337498798612982773\pm1.71\cdot10^{-25}\). The checker verifies by complex ball evaluation that both \(\zeta(1/2+ik\gamma)\) and \(L(1/2+ik\gamma,\chi)\) are nonzero for every integer \(2\le k\le128\).

For \(N=128\), write \(F_N(v)=(N+1)^{-1}|\sum_{j=0}^N e^{ijv}|^2\), the Fejér kernel with mean one. The time averages of \(P(u)F_N(\gamma u)\) and \(P(u)F_N(\gamma u+\pi)\) are respectively
\[
 2+\frac{2N}{N+1}\frac{m_\gamma}{1/4+\gamma^2},
 \qquad
 2-\frac{2N}{N+1}\frac{m_\gamma}{1/4+\gamma^2}.
\]
Indeed the finite Fourier expansion of the multiplier pairs only equal frequencies with opposite signs. Its higher harmonics have just been excluded. Each multiplier is nonnegative with time average one, so the first mean is at most the limiting superior of \(P\) and the second at least its limiting inferior. Substituting \(m_\gamma\ge1\) gives a shift exceeding \(6.81561720515\). This finite calculation needs no assumption on rational relations among other ordinates.

## Abelian fields containing the quadratic field

Every abelian number field \(E\) containing \(\mathbb Q(\sqrt{-163})\) and having conductor at most 400,000 satisfies
\[
 \liminf A_E<-1.43443,\qquad \limsup A_E>5.43443 .
\]
Indeed the primitive character factorization of \(\zeta_E\) retains \(L(s,\chi)\) as a factor. All nonprincipal factors are entire, and the zeta factor has only its pole at one. Theorems 7.1 and 7.2 of Platt exclude real zeros throughout \([1/2,1)\) for every constituent. Failure of individual GRH gives the same unbounded signed excursions as above. On individual GRH use the nonnegative multipliers \(1\pm\cos(\gamma u)\). Their weighted means are \(2\pm m_\gamma/(1/4+\gamma^2)\), which requires no harmonic exclusions for the additional factors. In particular, the bound applies to 1,840 distinct full cyclotomic fields: take \(E=\mathbb Q(\zeta_{163k})\) for \(1\le k\le2453\), omitting the 613 integers \(k\equiv2\pmod4\) that give redundant conductors. [Platt's verified rectangles and central values](https://doi.org/10.1090/mcom/3077)

## A majority of cyclotomic fields through conductor 400,000

For at least **188,960 of the 300,000 distinct full cyclotomic fields** of conductor at most 400,000, the normalized integrated error has strictly negative limiting inferior and strictly positive limiting superior, unconditionally. The coverage is a lower bound.

The [interval checker](../../scripts/check_zhao_cyclotomic_oscillation_nov18.py) searches conductor candidates \(3\le d\le1000\) in increasing order. It skips \(d\equiv2\pmod4\) and multiples of a previously certified conductor. At each remaining candidate, it checks primitive characters in increasing Conrey-label order. The first character whose real Hardy values at ordinates 0 and \(1/2\) have provably opposite signs supplies a witness \(0<\gamma<1/2\). This also works for a nonreal character since its phase-adjusted Hardy function is real on the critical line. The 192 certified conductor-label pairs have SHA-256 digest `412677a312fedb7ee3420a0956de739b7ee84eeeeb8bfb9360cdf90d59312470` when each is written as two decimal integers separated by a space and followed by a newline.

For every canonical cyclotomic conductor \(q\le400000\) divisible by such a \(d\), that primitive \(L\)-function occurs in \(\zeta_{\mathbb Q(\zeta_q)}\). Platt's theorems exclude real zeros throughout \([1/2,1)\). Under the individual GRH the same \(1-\cos(\gamma u)\) average is strictly negative, because \(1/(1/4+\gamma^2)>2\). The unweighted mean is 2. On failure of individual GRH, Landau's argument supplies excursions of both signs. Counting the union of the multiples with \(q\not\equiv2\pmod4\) gives the stated 188,960 fields.

These oscillation statements also hold for the normalized integrated Euler product \((\log X)T_E(X)/(C_E\sqrt X)\). On the individual RH the quadratic correction to the normalized harmonic error tends to zero. On failure of that RH the signed product excursions exceed the square-root scale by the fixed-field oscillation argument, including when the abscissa of the zeros is one. Thus the same 188,960 cyclotomic fields have sign changes for both statistics. [Prime-ideal product transfer](zhao-field-product-nov18.md)
