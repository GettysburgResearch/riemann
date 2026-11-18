# Independent check of Suzuki’s compensated drift

18 November 2026. Suzuki's arXiv v2 §5.1 p. 6 has an overall sign discrepancy in the compensated drift when the coefficient, exterior sign, jump locations and truncation are all read as displayed. Either flipping the sign of the displayed coefficient or replacing the exterior \(+iC_Ft\) by \(-iC_Ft\) restores (1.1). An explicit member of the extended Selberg class has a nonzero drift and distinguishes the two signs.

## Signs from the source conventions

Write \(E(z)=\xi_F(1/2-iz)\). Equation (2.5) gives the logarithmic derivative
\[
\frac{E'(z)}{E(z)}
 =B_F+\frac{m_0}{z}
    +\sum_{\gamma\ne0}m_\gamma\left(\frac{1}{z-\gamma}+\frac1\gamma\right).
\]
Thus \(B_F\) is the exponential coefficient of the Hadamard product in the \(z\)-plane. The conversion is \(E'/E=-i(\xi_F'/\xi_F)(1/2-iz)\). Under GRH, let \(A=\sum_{\gamma\ne0}m_\gamma/(\gamma(1+\gamma^2))\). The coefficient sum is absolutely convergent by the order-one zero summability and discreteness of zeros near zero. Equation (1.1) has linear part \(-iB_Ft\) plus the uncompensated zero sum. The compensated integral displayed in §5.1 is
\[
I(t)=-\frac{m_0t^2}{2}
 +\sum_{\gamma\ne0}m_\gamma
    \frac{e^{-i\gamma t}-1}{\gamma^2}
 +itA .
\]
Indeed, at the atom \(\lambda=-\gamma\) the subtraction of \(i\lambda t/(1+\lambda^2)\) adds \(i\gamma t/(1+\gamma^2)\), and the integral's integrand extends to \(-t^2/2\) at the origin. Therefore \(g_F(t)=I(t)-i(B_F+A)t\). The printed exterior \(+iC_Ft\) agrees only if \(C_F=-(B_F+A)\). Interpreting the displayed integral as a characteristic exponent with a different Fourier sign would also change its oscillatory term or the sign of the jump locations. Such a change is absent from the rendered display. [Equation (1.1), (2.5)–(2.6) and §5.1](https://arxiv.org/pdf/2209.12832v2#page=6)

## Test inside the extended class

Set \(F(s)=1+2i4^{-s}\), \(m_F=0\), \(r=0\), \(Q=2\). The finite Dirichlet series is absolutely convergent, and \(F\) is entire of order one. With \(\xi_F(s)=2^s+2i2^{-s}\) one has
\[
i\,\overline{\xi_F(1-\bar s)}
=i(2^{1-s}-2i2^{s-1})=\xi_F(s).
\]
These are the three printed axioms for \(S^\sharp\). Taking moduli at a zero gives \(4^{-\Re s}=1/2\), so all zeros lie on \(\Re s=1/2\). At the center \(F(1/2)=1+i\), and there is no real zero anywhere. The log-derivative also has an absolutely convergent expansion for \(\Re s>1\) by the geometric series in \(2i4^{-s}\). Only the extended-class axioms are needed for this check.

For \(u=\log 2\), \(E(z)=\sqrt2(e^{-iuz}+ie^{iuz})\). One has \(E'(0)/E(0)=-u=B_F\) and
\[
\Re \frac{E'(i)}{E(i)}
=\Re\left(iu\frac{-2+i/2}{2+i/2}\right)=-\frac{8u}{17}.
\]
On the other hand, the real part of each Hadamard correction at \(i\) is \(-\gamma/(1+\gamma^2)+1/\gamma\), and the term \(m_0/i\) contributes no real part. Hence \(B_F+A=-8u/17\), \(A=9u/17\), and the printed right side differs from \(g_F(t)\) by \(-16iut/17\). All values follow from the finite Dirichlet polynomial and the absolutely convergent logarithmic derivative. The linear imaginary discrepancy cancels in the screw kernel and in real-part tests. Its effect on the compensated probability representation is the deterministic translation.

## Version and scope

I read the class axioms and Hadamard convention, and visually checked the atom \(\delta_{-\gamma}\), compensation, exterior sign and coefficient on rendered v2 p. 6. The v2 PDF in the shared cache hashes to c706479044babf3618fff6910ce28238faf1bb321c7ffee9f73f1ee765f34232. The arXiv history lists v1 on 14 September 2022 and v2 on 25 March 2025. Earlier v1 p. 5 also has the positive exterior drift and positive displayed coefficient, with no multiplicities in the displayed coefficient sum. The witness has only simple zeros, so that omission does not affect it. The v1 PDF hash is 7cf9c85f305d4001827e2d9c00c83cbf00f64845f509787025ec82df922e0b59. The publisher route for the 2025 journal manifestation returned HTTP 403. The verified conclusion concerns the arXiv wording. The independent uniform review reaches the same result. [ArXiv history](https://arxiv.org/abs/2209.12832) · [ArXiv v1](https://arxiv.org/pdf/2209.12832v1#page=5) · [Publisher DOI](https://doi.org/10.1142/S1793042125500885) · [Uniform review](uniform66_suzuki_compensated_drift.md)
