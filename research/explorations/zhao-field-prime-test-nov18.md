# A finite prime-ideal certificate for the spectral field criterion

Suppose GRH for \(\zeta_K\). Write \(D=|\operatorname{disc}K|\), \((r_1,r_2)\) for the signature, and \(B_K=\sum_\gamma(1/4+\gamma^2)^{-1}\) with all ordinates and multiplicities. For any integer \(P\ge2\), set \(U=\log P\), \(g_0=(P-1)/(P+1)\) and \(\delta=2\sqrt P/(P+1)\). The following test approximates \(B_K\) to **relative error at most \(\delta\)** using only the signature, discriminant and prime ideal residue degrees through \(P\). The strict tests also apply when some residue degrees are missing by bounding those individual terms. [Arb checker](../../scripts/check_zhao_field_weight_nov18.py)

Put
\[
 \begin{split}
 E_K(P)={}&g_0\log D+2U g_0+(r_1+r_2)A_0+r_2 A_1\\
 &-\frac{2}{P+1}\sum_{N\mathfrak p^j\le P}\log N\mathfrak p\,(P/N\mathfrak p^j-1),\\
 A_a={}&g_0[\psi((1+a)/2)-\log\pi]+2I_a/(P+1)+2g_0J_a,\\
 I_0={}&\log((P+1)/2),\quad I_1=\log(2P/(P+1)),\\
 J_0={}&\operatorname{atanh}(1/P),\quad J_1=-\tfrac12\log(1-P^{-2}).
 \end{split}
\]
Then \((1-\delta)B_K\le E_K(P)\le(1+\delta)B_K\).

**Proof.** The even test
\[
 h(t)=\frac{1-\cos(Ut)/\cosh(U/2)}{1/4+t^2}
\]
has removable poles at \(\pm i/2\). Its inverse Fourier transform, with \(h(t)=\int g(y)e^{-ity}dy\), is \(g(y)=(P e^{-|y|/2}-e^{|y|/2})/(P+1)\) on \(|y|\le U\), zero elsewhere. This follows by translating the known transform pair for \(e^{-|y|/2}\). The test is real and nonnegative on the real line and stays within the stated relative error of the desired summand at every real ordinate. Its sum over zeros is exactly \(E_K(P)\) by the explicit formula. The two poles of the completed zeta function contribute \(2h(i/2)=2U g_0\). The conductor multiplies \(g(0)=g_0\). The prime side is \(-2\sum\log N\mathfrak p\,g(j\log N\mathfrak p)/(N\mathfrak p)^{j/2}\), which gives the finite sum above.

For the gamma side write a complex place as one even and one odd real gamma factor, up to a constant. In the digamma integral subtract the fixed value at \((1+a)/2\). Fourier inversion in the standard digamma integral gives the remaining correction
\[
 2\int_0^\infty\frac{e^{-(1/2+a)y}}{1-e^{-2y}}
       [g_0 e^{-y/2}-g(y)]dy .
\]
For \(y<U\) its integrand after removing the factor 2 is \(e^{-ay}/[(P+1)(1+e^{-y})]\), and above \(U\) it is \(g_0e^{-(1+a)y}/(1-e^{-2y})\). These integrals give exactly the indicated \(I_a,J_a\). All prime-side terms are nonnegative before the displayed minus sign. For an unknown rational prime the whole contribution lies between zero and its fully split value, since \(\sum_{\mathfrak p\mid p} f_{\mathfrak p}\le [K:\mathbb Q]\) and the weight decreases with the exponent. The checker encloses unresolved prime terms by these two extremes.

**Example of exhaustive bounds.** In degree three take \(P=4\), and bound every prime as fully split. For a field with \(B_K\le2\) the inequality \(E_K(4)\le2(1+\delta)\) then implies \(D<81,290\) for signature \((3,0)\) and \(D<42,758\) for signature \((1,1)\). The endpoints may be tightened further by specifying the ramification and splitting of 2 and 3. For the rational field the replay directly compares the finite formula at cutoffs 20, 100 and 1,000 with \(2+\gamma_E-\log(4\pi)\).
