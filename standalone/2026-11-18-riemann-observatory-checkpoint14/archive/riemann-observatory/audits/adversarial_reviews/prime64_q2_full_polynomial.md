# The full degree-four polynomial for the fixed \(Q_2\) derivative moment

Put \(Q_2(s)=2\,2^{-s}-1\), \(q=\log2\), and write
\[
 \zeta(1+z)=z^{-1}+c_0+c_1z+c_2z^2+c_3z^3+\cdots,
 \qquad c_j=(-1)^j\gamma_j/j!,
\]
where \(\gamma_j\) are the Stieltjes constants. Use the variable \(L=\log(t/(2\pi))\). Define
\[
\begin{aligned}
 D_1(L)={}&\frac{L^4}{12}+\frac{2c_0}{3}L^3
 +(c_0^2+2c_1)L^2+(-2c_0^3+10c_0c_1-2c_2)L\\
 &+2c_0^4-12c_0^2c_1+16c_0c_2+14c_1^2-20c_3,\\
 D_2(L)-D_1(L)={}&\frac{2q}{3}L^3+(4c_0q+q^2)L^2\\
 &+\left(4c_0^2q+4c_0q^2+8c_1q-\frac{16}3 q^3\right)L\\
 &-4c_0^3q+2c_0^2q^2+20c_0c_1q-\frac{32}3c_0q^3
       +4c_1q^2-4c_2q+\frac{49}6q^4.
\end{aligned}
\]
For \(i=1,2\), set \(P_{i,\pm}(L)=\sum_{j=0}^4(\pm1)^j D_i^{(j)}(L)\). Let
\[
 A_2(T)=\sum_{0<\gamma\le T}\zeta'(\rho)\zeta'(1-\rho)Q_2(\rho)Q_2(1-\rho).
\]
The fixed-support specialization of the shifted Heap–Li–Zhao theorem gives
\[
 A_2(T)=\frac{T}{2\pi}P_{2,-}\!\left(\log\frac{T}{2\pi}\right)
                 +O_A(T(\log T)^{-A})\qquad(A>0).
\]
Under RH, \(A_2\) is the nonnegative derivative-weighted moment. The argument below also gives the conditional error \(O_\varepsilon(T^{7/8+\varepsilon})\) for every \(\varepsilon>0\). For the strict two-sign tail under RH this yields
\[
 \boxed{\sum_{|\gamma|>Y}
           \frac{|\zeta'(\rho)|^2|Q_2(\rho)|^2}{|\rho|^2}
 =\frac{1}{\pi Y}P_{2,+}\!\left(\log\frac{Y}{2\pi}\right)
       +O_\varepsilon(Y^{-9/8+\varepsilon}).}
\]
The proof does not assign numerical constants to these error estimates. The leading term agrees with the fixed-\(k\) coefficient already recorded. [HLZ journal Theorem 5](https://doi.org/10.2140/ant.2022.16.1589) · [Prior leading coefficient](prime_array63_hlz_derivative_tail.md)

## The local computation and removal of all nonprincipal terms

The HLZ proof uses a polynomial supported up to \(y=T^\theta\). Here use \(y=T^{1/8}\) with zeros beyond index 2. The coefficients \((-1,2)\) at \((1,2)\) meet the submultiplicative premise directly. In §4.4, each term of \(E\) has a factor \(a(kq')\), with \(q'\ge2\) and a primitive character modulo \(q'\). Thus \(kq'\) could only be 2. Modulo 2 has only the principal character, induced from modulus 1, so this primitive sum is empty. In fact in the additive-character expansion of §4.2 the original modulus divides 2 and has no nonprincipal character at all. This identity removes \(E\) before any small-modulus or large-sieve estimate. In particular Proposition 10 and its Siegel step are absent. [HLZ §§4.2 and 4.4, equations (29) and (30)](https://doi.org/10.2140/ant.2022.16.1589)

Write \(a,b\) for the two shifts and \(g\) for the auxiliary differentiation shift. In the HLZ sum over relatively prime \((h,k)\) after taking out a common divisor, the total weight at \((1,1)\) is \(1+2=3\), and the weight at each of \((2,1)\), \((1,2)\) is \(-1\). The \(J\) integrand before division by \(2\pi\) is
\[
 L\big[\zeta(1+a+b)(3-2^{-a}-2^{-b})
       +e^{-(a+b)L}\zeta(1-a-b)(3-2^a-2^b)\big].
\]
For the \(Z\)-ratio in (24), put \(U=2^{-u}\), \(V=2^{-v}\), \(W=2^{-w}\) temporarily. The local series for \(f_{u,w}(2^m)\) is \((1-z)/[(1-Uz)(1-Wz)]\). Consequently the shifted numerator series for \(k=2\), divided by the unshifted one, at \(z=V/2\) is \((U+W-1-UWV/2)/(1-V/2)\). Including the weight at \(h=2\) gives
\[
 \mathcal W(u,v,w)=3-V-\frac{U+W-1-UWV/2}{1-V/2}.
\]
It is symmetric in \(u,w\), with \(\mathcal W(0,0,0)=1\). The corresponding summed \(Z\)-ratio in (24) is
\[
 \frac{\zeta(1+u+v)\zeta(1+v+w)}{\zeta(1+v)}
       \mathcal W(u,v,w).
\]
The third-shift derivative of the local factor is
\(\partial_w\mathcal W=qW(1-UV/2)/(1-V/2)\).

For a direct parity check before taking residues, set \(x=T/(2\pi)\) and
\[
 C(s)=\frac{\zeta(s)\zeta(s+a+b)\zeta(s+b+g)}{\zeta(s+b)},\qquad
 C_{\rm loc}(s)=\frac{1-2^{-s-b}}{(1-2^{-s})(1-2^{-s-a-b})(1-2^{-s-b-g})}.
\]
The four pairs in the main term \(M\) of HLZ §4.3 give the Perron kernel \(x^sC(s)G(s)/s\), where
\[
 G(s)=3-2^{1-s-b}-2^{s+b}\bigl(1-2/C_{\rm loc}(s)\bigr).
\]
For \((h,k)=(2,1)\) the endpoint is \(x/2\), and for \((1,2)\) it is \(2x\) with parity sign \(+1\) on even \(n\), \(-1\) on odd \(n\). The odd terms have Dirichlet series \(C(s)/C_{\rm loc}(s)\). This proves the kernel formula. At each of \(s=1,\,1-a-b,\,1-b-g\), one of the three denominator factors in \(C_{\rm loc}\) is \(1/2\). The remaining factors in \(G\) then give respectively
\(\mathcal W(a,b,g),\,\mathcal W(-b,-a,g),\,\mathcal W(a,-g,-b)\). This provides a second derivation of the local factor used in the residues.

## Differentiation and removal of apparent poles

Put
\[
 D(u,v)=\zeta(1+u+v)
    \left[
       \frac{\zeta'}{\zeta}(1+v)\mathcal W(u,v,0)
                   +\partial_w\mathcal W(u,v,0)
    \right].
\]
Differentiating the three terms of (24) in \(g\) at zero gives the \(I(a,b)\) integrand
\[
 D(a,b)+e^{-(a+b)L}D(-b,-a)
       -e^{-bL}\zeta(1+a)\zeta(1-b)\mathcal W(a,0,-b).
\]
The last minus sign follows from \(1/\zeta(1-g)=-g+O(g^2)\). Add the transposed \(I\) term. The source conjugates that term with the two complex shifts conjugated. Since the coefficients and Taylor constants here are real, its analytic expression is exactly the transpose with shifts \(b,a\).

The sum of the \(J\) integrand and both \(I\) integrands is holomorphic in \(a,b\) near zero. At \(a+b=0\) the \(J\) weights agree on the polar locus. For each \(I\), the first two terms have opposite residues there. At \(b=0\), the pole of \(D(a,b)\) cancels the third term with the same \(\mathcal W(a,0,0)\). The other possible pole on \(b=0\) cancels between the second and third terms of the transposed expression using symmetry in the first and third local shifts. The argument at \(a=0\) is the transpose. All denominators locally divide a unit times \(ab(a+b)\), so cancellation on each of these hyperplanes also removes the intersection's apparent singularity.

To calculate the \(ab\) coefficient, take \(a=A z,b=B z\). The degree-two terms are a symmetric quadratic \(U(A^2+B^2)+VAB\), so \(V=2[z^2]_{(1,2)}-[z^2]_{(1,3)}\). The script uses exact Laurent arithmetic and verifies the additional ray \((2,3)\). Taylor terms through degree four in the exponentials are needed because the shifted \(I\) pieces can start at degree \(-2\). For the logarithmic derivative the power series used is
\[
 \frac{\zeta'}{\zeta}(1+z)=-\frac1z+
 \frac{c_0+2c_1z+3c_2z^2+4c_3z^3+O(z^4)}
      {1+c_0z+c_1z^2+c_2z^3+c_3z^4+O(z^5)} .
\]
This gives \(D_2(L)\) above. The integrated density is \(P_{2,-}\) since \(\int_0^T D_2(\log(t/(2\pi)))dt=T P_{2,-}(\log(T/(2\pi)))\). In applying HLZ's error bound, Cauchy differentiation on \(|a|=c/\log T\), \(|b|=2c/\log T\) loses two logarithms, absorbed by choosing the source's \(A\) larger.

## Independent check with the untwisted polynomial

Set \(\mathcal W=1\), with the \(J\) weights also set to 1, to obtain \(D_1\). Its integrated \(P_{1,-}\) matches all five coefficients of Milinovich's proved polynomial as printed in equation (1.4) of Durkan–Hughes–Pearce-Crump, which their Corollary 2 independently recovers. The script verifies the equality under \(c_j=(-1)^j\gamma_j/j!\). Their preceding transcription of the Conrey–Snaith *integrand* is algebraically inconsistent with (1.4), so that transcription is not the check. Gonek's 1984 result provides the leading \(1/12\) check but does not determine the other four coefficients. [Durkan–Hughes–Pearce-Crump, equation (1.4) and Corollary 2](https://arxiv.org/pdf/2601.06292v1) · [Gonek](https://doi.org/10.1007/BF01403094) · [Exact symbolic checks](../../scripts/prime64_q2_full_polynomial.py)

## A conditional power-saving contour and the open numerical constant

The finite parity kernel gives a direct substitute for the principal part of HLZ §4.3 under RH. Use \(\kappa=1+1/\log T\), Perron height \(U=T^{1/4}\), and the Liu–Ye truncation parameter \(H=\sqrt U\). Apply the truncated Perron formula separately at the three endpoints \(x,x/2,2x\); one sum carries the bounded parity factor. The coefficient majorant from (30) at these endpoints is \(O(\tau_4(n))\) for the small shifts. The near-endpoint window has length \(O(T/H+1)\), and the absolute Dirichlet series of the majorant at \(\kappa\) is a fixed power of \(\log T\), using absolute convergence of four shifted zeta series. Thus the Perron error is \(O_\varepsilon(T^{7/8+\varepsilon})\). This bound is uniform on auxiliary circles of radius \(O(1/\log T)\), so differentiating in \(g\) gives at most an extra logarithm, absorbed in \(\varepsilon\). This choice of \(H\) deliberately implements the \(\sqrt U\)-width band displayed in the source, irrespective of the nearby prose's \(H=U\). [HLZ Lemma 9 and §4.3.1](https://doi.org/10.2140/ant.2022.16.1589)

Differentiate before moving to the line \(\Re s=3/4\). The differentiated principal integrand there is a product \(\zeta(s)\zeta(s+a+b)\) times
\[
 \left[\frac{\zeta'}{\zeta}(s+b)G(s)\big|_{g=0}
                     +\partial_g G(s)\big|_{g=0}\right]\frac{x^s}{s}.
\]
The finite local factors and their derivatives are bounded on the rectangle. On RH, the critical zeros stay a fixed positive distance in real part from all points \(s+b\) on the left line and horizontal edges for sufficiently large \(T\). The horizontal edges also have distance at least \(U-O(1)\) from the pole at \(1\); the left edge is separated in real part from that pole. Comparing the Hadamard log derivative at \(s+b\) with \(2+i\Im(s+b)\) gives a bound \(O(\log(|\Im s|+2))\) there. The local zero count contributes \(O(\log(|\Im s|+2))\) because of the real-part separation, and the paired far differences are summable by the inverse-square kernel. Ordinary Euler summation truncated at \(\lceil|\Im s|+2\rceil\) gives \(O((|\Im s|+2)^{\max(0,1-\Re s)}\log(|\Im s|+2))\) for each zeta factor on those edges, with the shift changing the power by \(O(1/\log T)\). Hence the left and horizontal contour pieces are, up to log powers, bounded by \(T^{3/4}U^{1/2}\) and \(TU^{-1/2}\), respectively. Both are \(T^{7/8}\). Only the near-one principal residue cluster is crossed. Differentiation of its total residue is valid on a single enclosing circle, so it is the same differentiated main term as in (24).

Fix \(y=T^{1/8}\) in the initial HLZ rectangular contour and the stationary-phase replacement in Lemma 7. Their error powers \(y^{1+\varepsilon}T^{1/2+\varepsilon}\) and \(yT^{1/2+\varepsilon}\) are smaller. For the continuous term, the direct fixed-product AFE proof in the companion note gives \(O(T^{3/4}(1+\log T)^4)\) on the actual sharp cutoff, and independently bounds the functional-equation \(O(1/t)\) correction by \(O(T^{7/8})\). It does not import a sharp version of the smoothed Pratt–Robles theorem. Logarithmic losses are harmless after Cauchy differentiation. [Direct sharp-cutoff proof](prime64_q2_sharp_j.md) Moving from an admissible contour height to the desired \(T\) takes a bounded height displacement. On RH the unit-window zero count and the explicit critical-line \(O(T^{7/16})\) derivative bound bound this adjustment by \(O(T^{7/8}\log T)\). This proves the claimed \(O_\varepsilon(T^{7/8+\varepsilon})\) conditional profile. [HLZ pp. 1607–1613](https://doi.org/10.2140/ant.2022.16.1589) · [Explicit derivative and zero-count bounds](prime_array63_effective_bound_skeptic.md)

For the strict tail, integrate against \((t^2+1/4)^{-1}\) by Stieltjes partial summation on \((Y,\infty)\), using the inclusive \(A_2(Y)\) in the subtracted boundary term. Reflection doubles the integral. For the smooth main term, \(d[tP_{2,-}(\log(t/(2\pi)))]/dt=D_2(\log(t/(2\pi)))\). Replacing \((t^2+1/4)^{-1}\) by \(t^{-2}\) there costs \(O((\log Y)^4/Y^3)\), and \(\int_Y^\infty D_2(\log(t/(2\pi)))t^{-2}dt=P_{2,+}(\log(Y/(2\pi)))/Y\). The cumulative moment error contributes \(O_\varepsilon(Y^{-9/8+\varepsilon})\) by its boundary and integrated terms.

For scale only, the uncorrected main term at height 100 is approximately \(0.399680\), and at 400 it is approximately \(0.223983\). These are not tail certificates. Turning them into a rigorous practical enclosure requires a numerical error budget on the fixed shifted continuous-moment and stationary-phase inputs, their uniform disk radii, and the explicit Perron and endpoint constants. Merely removing the nonprincipal character terms does not supply those numbers. [Source and constant ledger](prime64_q2_full_polynomial_sources.md)
