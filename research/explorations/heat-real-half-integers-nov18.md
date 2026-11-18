# Real heat zeros at half-integer values of the Polymath15 coordinate

**Proposed theorem.** In the normalization of the [interior-ray theorem](heat-first-real-ray-nov18.md), put
\[
 \beta=x/b-\pi/4,\qquad N=\sqrt{(x-\pi b/4)/(4\pi)},\qquad A=\pi/16.
\]
On every fixed \(0<\beta_0\le\beta\le\beta_1<\infty\), as \(b\to\infty\), the positive real zeros of \(H_{-b}(x)\) consist of one simple zero at \(N=k+1/2+o(1)\) for each half integer in range, with the usual endpoint ambiguity of at most one at either end. The error is uniform. The number of zeros in this physical interval is
\[
 \frac{\sqrt{\beta_1}-\sqrt{\beta_0}}{2\sqrt\pi}\sqrt b+O_{\beta_0,\beta_1}(1).
\]
In particular there are \(\gg_\epsilon \sqrt b\) sign changes by \((\pi/4+\epsilon)b\). This is the fixed-supercritical-ray case of the half-integer pattern observed by Polymath15. The [Airy edge for fixed index](heat-real-airy-edge-nov18.md) lies on the opposite side of \(\pi b/4\). [Polymath15, numerical observations and later heuristic refinements](https://terrytao.wordpress.com/2018/12/28/polymath-15-eleventh-thread-writing-up-the-results-and-exploring-negative-t/)

## A real theta profile

Let \(c=\pi/8\), \(A_k=A(2k+1)^2\), and \(e_k=(-1)^{k(k+1)/2}\). Set
\[
 W_b(N)=-\frac{16 e^{cx-bc^2}}{\sqrt\pi(\beta b)^{3/2}} H_{-b}(x),
 \qquad T(\beta,N)=\sum_{k\ge0}e_k e^{-A_k/\beta}\cos((2k+1)\pi N).
\]
We prove uniformly on the indicated compact \(\beta\)-range that
\[
 W_b(N)=T(\beta,N)+o(1),\qquad
 W_b'(N)=\partial_N T(\beta,N)+o(1). \tag{1}
\]
In the partial derivative on the right \(\beta\) is held fixed. Along the physical curve \(d\beta/dN=O(b^{-1/2})\), so the total derivative of the profile has the same approximation.

First consider the zero structure of \(T\). Write
\[
 h(s)=\sum_{k\ge0}e^{-A_k/\beta}\cos((2k+1)\pi s)
 =\tfrac12\vartheta_2(\pi s,e^{-4A/\beta}).
\]
Since \(e_k=\sqrt2\cos((2k+1)\pi/4)\), one has \(T=(h(N+1/4)+h(N-1/4))/\sqrt2\). The Jacobi product writes \(h(s)\) as a positive constant times \(\cos(\pi s)\prod_{m\ge1}(1+2q^{2m}\cos(2\pi s)+q^{4m})\), \(q=e^{-4A/\beta}\). It is positive and strictly decreasing with strictly negative derivative on \((0,1/2)\). It is even and changes sign under translation by one. Thus \(T>0\) for \(0\le N<1/2\). On the part \(1/4<N<1/2\) this follows because \(N-1/4<3/4-N\), with both distances in \([0,1/2]\). At \(N=1/2\) its derivative is \(\sqrt2 h'(1/4)<0\). Symmetry, antiperiodicity and continuity in \(\beta\) give uniform simple crossings and uniform sign margins away from small neighborhoods of the half integers on every compact \(\beta\)-range. Formula (1) gives the claim, applying it on a slightly larger compact interval to deal with the endpoints.

## Uniform stationary phase for the cusp modes

Let \(L=\sqrt b\). Shift the full Fourier integral to \(u=i(c-1/b)+v/L\), \(v\in\mathbb R\). The constant from the Gaussian and Fourier phase is \(e^{bc^2-cx} e^{\beta+1/b}\). Their remaining factor is \(e^{-v^2+iL\beta v+2iv/L}\). The cusp parameter is \(z=L^{-2}+iv/L\). In the modular expansion from the [kernel proof](heat-first-real-ray-nov18.md),
\[
 Y=\tfrac12\cot(2z),\quad D=1+4Y^2,\quad P_k=4A_k,\qquad
 F(c-z)=-\frac{\sqrt2}{16}D^{5/4}\sum_{k\ge0} e_k e^{-P_kY}
      \big[3-12P_kY+P_k^2D\big].
\]
The leading prefactor of a single mode is \(-A_k^2 z^{-9/2}/16\). Powers are continued from positive real \(z\). After removing the constant and scaling by the Jacobian and \(L^{9/2}\), the integral over positive \(v\) consequently reduces to a sum of oscillatory integrals
\[
 e_k A_k^2 e^{-9\pi i/4}
 \int_0^\infty v^{-9/2}e^{-v^2-A_k/v^2}
                  e^{iL(\beta v+A_k/v)}\,dv , \tag{2}
\]
up to the common factor \(-1/16\) and an absolute error \(o(L^{-1/2})\). Negative \(v\) supplies the conjugate; the factor \(1/2\) of the full Fourier representation converts their sum into the real part.

For details of the error, choose \(\delta=1/40\). On \(L^{-\delta}\le v\le L^\delta\) and \(k+1\le 2L^\delta\), expand \(Y=1/(4z)+O(z)\),
\[
 -A_k/z=iL A_k/v-A_k/v^2+O(L^{-1+5\delta}),\qquad
 z^{-9/2}=L^{9/2}(iv)^{-9/2}(1+O(L^{-1+\delta})).
\]
The remaining polynomial terms produce relative error \(O(|z|/P_k+|z|^2/P_k^2+|z|^2)\), and the small exponent errors produce relative error \(O(L^{-1+5\delta})\). The sum of the integrals of the absolute limiting amplitudes in (2) is bounded, even after multiplication by \(1+v\), since \(v^2+A_k/v^2\ge c_1 k+v^2/2+A_k/(2v^2)\) for an absolute \(c_1>0\).

For \(0\le v\le L^\delta\), one has \(\Re Y\asymp 1/(L^{-2}+v^2)\), uniformly. For example the identity \(\Re\cot(2z)=\sin(4/L^2)/(\cosh(4v/L)-\cos(4/L^2))\) proves this directly. It bounds the original small-\(v\) contribution for \(v<L^{-\delta}\) by a polynomial times \(e^{-c_2 L^{2\delta}}\), and the omitted high modes in the middle range by a polynomial times \(e^{-c_3 L^\delta}\) after using part of \(e^{-v^2}\). For \(v>L^\delta\) the global strip bound in the [cusp note](heat-real-cusp-nov18.md) is only polynomial in \(L\), so the Gaussian suffices. The limiting integrals have the same tail controls. These estimates justify the claimed \(o(L^{-1/2})\) absolute error. They also hold with an extra factor of \(v\) in the integrand.

For fixed \(k\), \(\beta v+A_k/v\) has its unique stationary point at \(v_k=\sqrt{A_k/\beta}\), with second derivative \(2A_k/v_k^3>0\). The stationary-phase factor \(e^{i\pi/4}\) cancels \(e^{-9\pi i/4}\). The leading term of (2) is therefore
\[
 e_k\sqrt{\pi/L}\,\beta^{3/2} e^{-A_k/\beta-\beta}
           e^{2iL\sqrt{A_k\beta}} .
\]
The remainder is \(o_k(L^{-1/2})\) uniformly for \(\beta\) in a compact positive interval. To justify summing this asymptotic, use the second-derivative van der Corput bound separately on consecutive unit intervals in \(v\). On \([m,m+1]\) it bounds the modulus multiplied by \(\sqrt L\) by \(O((m+1)^{3/2}/\sqrt{A_k})\) times the supremum plus the integrated absolute first derivative of the amplitude. For \(m=0\) take the limit from a positive endpoint. After summing over \(m\) these bounds are \(O((1+k)^{C} e^{-c_4 k})\): each arising power of \(v,1/v,A_k\) is absorbed using parts of \(e^{-v^2-A_k/v^2}\), and the remaining exponential gives decay in both \(m\) and \(k\). This also holds with the extra amplitude factor \(v\). Thus the integrated series has the sum of the stated main terms with uniform \(o(L^{-1/2})\) remainder.

Finally \(2L\sqrt{A_k\beta}=(2k+1)\pi N\). Restoring the factors, including \(L^{9/2-1}\) from the cusp and the Jacobian, gives the first equation of (1). For the second, differentiate the normalized integral with \(b\) fixed. The phase supplies \(4i\sqrt{\pi\beta}\,v\), and derivatives of the smooth exterior factors cost \(O(1/L)\) on the compact range. At the stationary point this multiplier equals \(i(2k+1)\pi\). The preceding weighted error bounds therefore give the differentiated equation. This establishes the sign and count statements for the physical heat function.
