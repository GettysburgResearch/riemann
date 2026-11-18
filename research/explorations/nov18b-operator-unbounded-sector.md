# An infinite-dimensional positive sector of the xi resolvent

**Proposed unconditional theorem.** Let \(z_j=a_j+ib_j\), \(a_j>0\), with repetitions allowed, and form
\[
 L=\sup_{t\in\mathbb R}\sum_j\frac{2a_j}{a_j^2+(t-b_j)^2}.
\]
If \(L\le10^{-3}\), then the actual xi resolvent form is strictly positive on every nonzero proper rational test whose poles belong to this packet with the specified multiplicities. There is no restriction on the number or heights of the nodes. All finite subpackets of a given infinite set obey the same lower bound when its full displayed sum has the stated bound. This theorem uses the critical strip and an unconditional zero-count estimate, without a verified critical-line prefix.

More precisely put \(r(t)=R(it)\), \(w(t)=\log(2+|t|/(2\pi))\), and \(\|r\|_w^2=\int_{\mathbb R} w(t)|r(t)|^2dt\). With \(\lambda=\rho-1/2\), the [exact resolvent identity](nov18b-operator-pick.md) gives the full quadratic form
\[
 \mathcal Q(R)=\sum_\lambda R(\lambda)\overline{R(-\bar\lambda)}.
\]
It satisfies
\[
 .038\|r\|_w^2<\mathcal Q(R)<.29\|r\|_w^2. \tag{1}
\]
In particular its polarized form extends continuously and positively to the closure of the rational subspace in this norm. The theorem accounts for all off-line displacements allowed by the strip.

## 1. A derivative bound from the pole locations

The poles of \(r\) are \(u_j=b_j-ia_j\) in the lower half-plane. Write \(B(t)=\prod_j(t-\bar u_j)/(t-u_j)\) for the finite product. Its boundary phase derivative is the positive sum defining \(L\). Direct contour integration gives
\[
 r'(x)=\frac{1}{2\pi i}\int_{\mathbb R}r(t)
    \left(\frac{1-B(x)/B(t)}{t-x}\right)^2dt,\qquad x\in\mathbb R. \tag{2}
\]
First replace \(x\) by a point in the upper half-plane and expand the square. Cauchy's formula gives the derivative from the first term. The terms involving \(r/B\) and \(r/B^2\) integrate to zero by closing in the lower half-plane, where they are holomorphic and vanish at infinity. Boundary passage follows by removable cancellation of the difference quotient and the rational decay. Thus \(|r'|\) is bounded by the convolution of \(|r|\) with \((2\pi)^{-1}\min(L^2,4/|t|^2)\).

Since \(w(x)/w(t)\le1+\log(1+|x-t|)/\log2\), weighted Young's inequality now gives
\[
 \|r'\|_w\le A_L\|r\|_w,\qquad
 A_L=4L\sqrt{1+\log(1+1/L)/\log2}.
\]
Indeed substitute \(u=Lt\) in the kernel integral and use \(1+|u|/L\le(1+1/L)(1+|u|)\). The remaining constant is at most
\[
 \frac1\pi\int_0^\infty \min(1,4/u^2)
       \left(1+\frac{\log(1+u)}{\log2}\right)du<4 .
\]
Splitting at 2 gives the integral before division by \(\pi\) as \(4+(5\log3-2+4\log(3/2))/\log2\).

The derivative \(r^{(j)}\) has a denominator dividing that of the product \(B^{j+1}\), in the sense that its pole multiplicities are at most the corresponding multiplicities of that denominator. Using (2) for that product costs at most \((j+1)A_L\) at the next derivative. Therefore
\[
 \|r^{(j)}\|_w\le A_L^j j!\|r\|_w. \tag{3}
\]
The function \(A_L\) is increasing, as follows by differentiating its square. Hence \(A_L<.014\) in the stated range.

## 2. Sampling the projected ordinates

Let \(\nu=\sum_\rho\delta_{\Im\rho}\) count all signed ordinates with multiplicity. On \(t\ge0\) its cumulative count differs from \((2\pi)^{-1}\int_0^t w(v)dv\) by at most \(4w(t)\). To check this for \(t\ge2\pi e\), put \(u=t/(2\pi)\). The smooth cumulative count exceeds \(u\log(u/e)\) by
\[
 u\log(1+2/u)+2\log(1+u/2)\le 2+2\bigl(w(t)-\log2\bigr).
\]
Insert \(N(t)=u\log(u/e)+7/8+E(t)\), \(|E(t)|\le.28\log t\). The stated bound follows since \(w(t)\ge\log(2+e)\) here. For smaller \(t\), monotonicity and the error bound at \(2\pi e\) give \(N(t)\le1\), and the smooth cumulative count is at most \(e\,w(t)\). Take one-sided limits at zeros and use symmetry on the negative axis. [Zero-count estimate, footnote 1](https://arxiv.org/abs/2009.13791)

Integration by parts on the line for any proper rational \(v\) without real poles gives
\[
 \left|\sum_\gamma |v(\gamma)|^2-\frac1{2\pi}\|v\|_w^2\right|
 \le8\|v\|_w\|v'\|_w. \tag{4}
\]
The boundary term vanishes at both infinities. Thus the baseline vector \((r(\gamma))\) has squared norm between \((1/(2\pi)-8A_L)\|r\|_w^2\) and \((1/(2\pi)+8A_L)\|r\|_w^2\).

## 3. Restoring the actual zeros

For any independent displacements \(|\delta_\gamma|\le1/2\), the Taylor series for \(r(\gamma+i\delta_\gamma)\) converges: every pole has depth \(a_j\ge2/L\). By (3), (4) and the triangle inequality on the complete sequence of ordinates, the norm of its difference from the baseline is at most
\[
 \|r\|_w\sum_{j\ge1}\left(\frac{A_L}{2}\right)^j
  \sqrt{1/(2\pi)+8(j+1)A_L}
 < .008\|r\|_w. \tag{5}
\]
For the last inequality majorize the square root by \(.53(j+1)\) and use \(A_L/2<.007\). Absolute convergence of these norm bounds justifies the Taylor summation. Taking the opposite displacements and bounding the real cross terms by Cauchy–Schwarz yields (1), since
\[
 1/(2\pi)-.112-2(.008)\sqrt{1/(2\pi)+.112}-.008^2>.038 .
\]
Reflection makes the total form real.

For example the entire two-sided sequence \(z_j=10^4+10^5 i j\), \(j\in\mathbb Z\), obeys the hypothesis. With common real part \(a\) and spacing \(D\), the nearest term is at most \(2/a\) and the rest sum to at most \(2\pi^2 a/D^2\). The resolvent form is therefore bounded below on the infinite-dimensional span at arbitrarily large carriers. Clustering high-real-part nodes is also permitted if the total phase derivative stays small.

The hypothesis gives a finite Blaschke sum, by evaluating the phase derivative at zero. An infinite set with this bound cannot be a half-plane uniqueness set by divergent Blaschke mass alone. Establishing a comparable source-specific estimate for packets with arbitrarily large mass is the remaining issue for an RH argument through real-axis interpolation.
