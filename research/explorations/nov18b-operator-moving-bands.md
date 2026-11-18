# A linear-height bound for the full xi Pick hierarchy

**Proposed theorem for review.** Suppose every nontrivial zeta zero of ordinate \(|\gamma|\le H\) lies on the critical line, where \(H\ge10^{12}\). For every
\[
 k\le\lfloor H/40000\rfloor,\qquad \Re z_j>0,\quad |\Im z_j|\le H/2,
\]
the centered logarithmic-derivative Pick matrix of \(\xi\) at \(k\) distinct nodes is positive definite. The real parts may be arbitrarily large or close to zero. At the published Platt–Trudgian height this gives every order through **75,004,383**, including every configuration of that many positive real nodes. The proof admits all proper rational tests with allowed poles of total multiplicity at most \(k\). [Definition, resolvent identity and published inputs](nov18b-operator-pick.md)

The proof works for every zero configuration with the same strip, reflection, convergence, low-zero and zero-counting hypotheses. It bounds the actual contribution of all unknown zeros. The improvement over the sharp-edged dyadic argument comes from using a positive weight vanishing at the edges and integrating over the band center. The powers and constants below are sufficient values.

## 1. A moving interval and a weighted polynomial

Put \(\eta=1/16\), \(T_0=H/(1+\eta)\), and take any \(T\ge T_0\). Parameterize positive ordinates by \(t=T(1+\eta x)\), \(-1\le x\le1\). Write
\[
  A=\frac{\eta T}{2\pi}\log\frac{T}{2\pi},\qquad
  m=12k+500,\qquad n=3m.
\]
Then \((n+1)/T<0.001\). For a nonzero proper rational test \(R\) of denominator degree at most \(k\), set \(r(x)=R(iT(1+\eta x))\). The argument below applies unchanged to \(r(x)=R(-iT(1+\eta x))\) on the negative band. Every pole \(b\) has real part at most \((H/(2T)-1)/\eta\le -7.5\). Each unknown zero displacement amounts to evaluating \(r(x+i\tau)\) with \(|\tau|\le8/T\).

Let \(p\) be the degree-\(m\) Chebyshev truncation of \(r\) on \([-1,1]\), and put
\[
  q(x)=(1-x^2)^m p(x).
\]
All unlabelled norms below are on \([-1,1]\). We record three elementary bounds.
\[
 \max_{|\Re z|\le1,\ |\Im z|\le8/T}|r(z)-p(z)|<10^{-12}\|q\|_2, \qquad
 \|q'\|_2\le4(n+1)\|q\|_2. \tag{1}
\]
For \(.95\le|x|\le1\), \(|\tau|\le 8/T\), one also has
\[
 |q(x)|+(1-x^2)^m|p(x+i\tau)|<10^{-12}\|q\|_2. \tag{2}
\]

Here are the details for (1) and (2). On the Bernstein ellipse \(E_8\), which has semimajor axis \(65/16\), \(|r|\le24^k\|r\|_\infty\). The numerator costs \(8^k\) by the polynomial Bernstein–Walsh inequality. Each denominator factor costs at most \((|b|+1)/(|b|-65/16)<3\). The Chebyshev tail on \(E_{17/16}\) is bounded by
\[
 2\,24^k\frac{(17/128)^{m+1}}{1-17/128}\|r\|_\infty
 <4(0.175)^m\|r\|_\infty .
\]
The smaller ellipse contains the entire indicated strip rectangle. The real-interval approximation implies \(\|r\|_\infty\le2\|p\|_\infty\). Bernstein–Walsh from \([-1/2,1/2]\) to \([-1,1]\) and then the degree-\(n\) Legendre evaluation bound give
\[
 \|p\|_\infty\le [(2+\sqrt3)(4/3)]^m\|q\|_\infty
 \le 5^m(n+1)\|q\|_2.
\]
Thus the tail in (1) is at most \(8(0.875)^m(n+1)\|q\|_2<10^{-12}\|q\|_2\) for \(m\ge512\). The same estimates and \(|p(x+i\tau)|\le(17/16)^m\|p\|_\infty\) give (2), since \(1-x^2\le0.0975\) there. In particular \(q\ne0\).

For any polynomial \(v\) of degree \(n\), expanding in Legendre polynomials gives
\[
 \int_{-1}^1(1-x^2)^j|v^{(j)}(x)|^2dx\le \frac{(n+j)!}{(n-j)!}\|v\|_2^2
 \quad(0\le j\le n). \tag{3}
\]
Indeed the differentiated Legendre polynomials of degrees \(l\ge j\) are orthogonal with the indicated weight and squared-norm multiplier \((l+j)!/(l-j)!\), by Rodrigues' formula and integration by parts. With \(j=1\), (3) bounds the norm of \(q'\) on \(|x|\le.95\) by \(\sqrt{n(n+1)/.0975}\|q\|_2\). On the edges differentiate the factors of \(q\), using \(\|p'\|_\infty\le m^2\|p\|_\infty\) (the classical Markov inequality). The norm there is bounded by \(\sqrt2(n+1)(m^2+21m)(.488)^m\|q\|_2\), which supplies the second estimate in (1).

## 2. Sampling and complex displacement

The normalized zero-counting main density on this interval is between \(.997A\) and \(1.003A\). The uniform bound \(.28\log(2T)\) on its counting remainder is less than \(32 A/T\). These constants hold for all \(T\ge T_0\) by the explicit Riemann–von Mangoldt bound cited in the companion note. Write \(x_\gamma=(\gamma/T-1)/\eta\) on the positive band, counting multiplicity. Its total count is below \(3A\) using the one-sided endpoint limits. As \(q(\pm1)=0\), Stieltjes integration by parts and (1) yield
\[
 .73A\|q\|_2^2\le \sum_\gamma |q(x_\gamma)|^2\le1.27A\|q\|_2^2.
 \tag{4}
\]
The absolute quadrature error is at most \(64A\|q\|_2\|q'\|_2/T\).

For derivatives, insert a piecewise linear cutoff equal to one on \(|x|\le.95\), zero for \(|x|\ge.98\), with Lipschitz constant at most 34. On its support (3) bounds the \(L^2\) norm of \(q^{(j)}\) by \((11n)^j\|q\|_2\), since \(2/\sqrt{1-.98^2}<11\). Apply the same Stieltjes formula to the cutoff times \(|q^{(j)}|^2\). The main term is bounded by \(1.003A(11n)^{2j}\|q\|_2^2\), and the error by \((32A/T)(34+22n)(11n)^{2j}\|q\|_2^2\). This gives
\[
 \sum_{|x_\gamma|\le.95}|q^{(j)}(x_\gamma)|^2\le 2A(11n)^{2j}\|q\|_2^2
 \quad (0\le j\le n). \tag{5}
\]
The derivative of order \(n+1\) in the last integration by parts is zero.

Choose independently any \(|\tau_\gamma|\le8/T\). Taylor expansion and (5) bound the interior discrete norm of \(q(x_\gamma+i\tau_\gamma)-q(x_\gamma)\) by \(\sqrt{2A}(e^{88n/T}-1)\|q\|_2<0.131\sqrt A\|q\|_2\). To return to the original weight define
\[
 d(x,\tau)=\frac{1-x^2}{1-(x+i\tau)^2}.
\]
On the interior \(|d|\le1\), and
\[
 |d^m-1|\le m|d-1|\le \frac{m(2|x\tau|+\tau^2)}{1-x^2}<0.055
\]
by the bound on \((n+1)/T\). Multiply the shifted \(q\) by \(d^m\), and use (4) to pay the change in the unshifted vector. The interior error is at most \((.131+.055\sqrt{1.27})\sqrt A\|q\|_2\). The edges and the approximation of \(r\) cost less than \(4\cdot10^{-12}\sqrt A\|q\|_2\) by (1), (2) and the band count. Consequently
\[
 \left(\sum_\gamma\left|
 (1-x_\gamma^2)^m r(x_\gamma+i\tau_\gamma)-q(x_\gamma)\right|^2\right)^{1/2}
 <.20\sqrt A\|q\|_2. \tag{6}
\]
Taking the two opposite displacements and using (4), the real inner product of the resulting weighted vectors is at least
\[
 (.73-2\sqrt{1.27}\, .20-.20^2) A\|q\|_2^2>.23 A\|q\|_2^2.
\]
This strict lower bound uses all ordinates of the band, including any with off-critical real part.

## 3. Recovering the unweighted form

Integrate the positive band forms over \(T\ge T_0\) against \(dT/T\). Every ordinate \(t\ge H\) receives the same total weight
\[
 C=\int_{1-\eta}^{1+\eta}\left(1-\left(\frac{u-1}{\eta}\right)^2\right)^{2m}\frac{du}u>0.
\]
Every lower positive ordinate receives a weight between zero and \(C\). Negative ordinates use the reflected bands. Absolute convergence of the resolvent form and the uniform mass bound justify interchange. The unused weight multiplies \(|R(i\gamma)|^2\ge0\) throughout the verified interval. Dividing by \(C\) proves strict positivity of the full unweighted form for every nonzero rational test.

The source-independent part of this proof costs a factor comparable to \(k/T\) for a horizontal displacement in a high band, replacing the earlier \(k^2/T\). To use the result at unbounded order with a fixed zero census, one would need to control bands in which this factor is large or use further arithmetic information. The argument uses the published ordinate bound, without requiring simple zeros or numerical values for the interpolation nodes.
