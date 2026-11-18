# Uniform high zeros on a specified vanishing heat-time scale

**Proposed theorem.** In the normalization of Polymath15 there is an absolute \(X_0\) such that for every \(x\ge X_0\), every \(0<t\le1/2\) with \(t\log x\ge2.541\), all zeros of \(H_t\) with real part \(x\) are real and simple. For \(t\log x\) in any fixed compact interval above this threshold, the consecutive real zeros near \(x\), with \(t\) held fixed, have spacing \((4\pi/\log x)(1+O(1/\log x))\). No hypothesis on zeta zeros enters. The threshold height is unevaluated.

Only the bounded transition variable is new to this argument. Polymath15's Theorem 1.5 gives the conclusion for \(t\log x\) greater than a sufficiently large absolute constant. The present estimate retains the entire Euler wave near its Gaussian saddle and uses the unconditional subconvex bounds for zeta on the intervening strip. [Polymath15](https://arxiv.org/abs/1904.12438) · [Trudgian–Yang, Theorem 2.4](https://arxiv.org/abs/2306.05599)

## A strict exponent comparison

Use \(T=x/2,\ u=t/4,\ L=\log(T/(2\pi)),\ c=uL\) and the notation \(G,\alpha,F_u\) of the [Gaussian identities](nov18b-heat-persistence.md). Then \(c\ge c_0=397/625\) for all sufficiently large \(x\) in the claimed region. By the preceding large-parameter theorem we may assume \(c\le C_0\) with \(C_0\) fixed. Write \(\mu(\sigma)\) for the infimal growth exponent of \(|\zeta(\sigma+iT)|\). Trudgian–Yang's piecewise linear majorant \(m(\sigma)\) on \([1/2,9/10]\), continued linearly to \(m(1)=0\), has
\[
   \min_{0\le r\le1/2}
     \left(\frac{(c-r)^2}{4c}-m(1/2+r)\right)>1/30000 .
                                                               \tag{1}
\]
For \(c\ge c_0>1/2\), the quadratic is increasing in \(c\) at each such \(r\). At \(c_0\), the minimum on an affine piece is at the critical point clipped to the two endpoints. The [rational checker](nov18b-heat-growth.py) reads all eleven rational pieces and checks the strict bound. The last interpolation uses the convexity of \(\mu\). For each fixed \(\epsilon>0\) the standard vertical-line bounds and the three-lines principle between each pair of endpoints give \(|\zeta(\sigma+iT)|\ll_\epsilon T^{m(\sigma)+\epsilon}\), uniformly in this strip. There is no differentiation of an asymptotic zeta bound.

## Separating the two waves

Put \(s=1/2+y+iT\) and
\[
 W_u(s)=\int_0^\infty g_u(v)\xi(s+v)\,dv,\qquad
 F_u(s)=W_u(s)+W_u(1-s).
\]
These functions are holomorphic, and \(W_u(\overline s)=\overline{W_u(s)}\). For some fixed \(h>0\), uniformly in \(|y|\le2h\),
\[
 \frac{W_u(s)}{G(s)e^{u\alpha(s)^2}}
       =\zeta(s+2u\alpha(s))+O(\sqrt u).                    \tag{2}
\]
To prove this, after taking out the gamma factor the tilted absolute Gaussian mass is \(e^{u(\Im\alpha)^2}=1+O(u)\) and its center is \(c+O(u/T)\). In a fixed small interval about \(c\) the zeta argument has real part at least \(1+(c_0-1/2)/2\). Its value and first derivative are uniformly bounded by absolute Dirichlet series. Taylor's estimate inside the Gaussian gives the error \(O(\sqrt u)\) upon replacing zeta by the indicated value, since the complex and real saddles differ by \(O(u)\). Stirling gives \(G(s+v)=G(s)e^{\alpha(s)v}(1+O_B(T^{-1}))\) for \(|v|\le B\) fixed. Outside a sufficiently large fixed cutoff \(B=B(C_0)\), the Gaussian absorbs the full growth bound for \(\xi\) in the companion calculation, even after division by this gamma normalization.

For the remaining bounded positive \(v\), first take \(y=0\). Where \(0\le v\le1/2\), (1) beats the absolute zeta exponent by a fixed positive margin. Where \(v>1/2\) outside the saddle interval, the Gaussian costs a fixed power of \(T\), whereas zeta costs at most \(T^\epsilon\). The bounds are uniform for \(c\in[c_0,C_0]\). The functional equation continues the growth majorant to the left of \(1/2\) by \(m(\sigma)=1/2-\sigma+m(1-\sigma)\); on the right of one take exponent zero. This continuous piecewise linear upper envelope remains sufficient on replacing \(y=0\) by \(|y|\le2h\), if \(h\) and \(\epsilon\) are fixed smaller than the preceding strict margins. Polynomial Gaussian normalization factors in \(\log T\) are harmless. This proves (2).

For \(h\le y\le1/2\) the same main wave gives
\[
 F_u(s)/(G(s)e^{u\alpha(s)^2})=\zeta(s+2u\alpha(s))+o(1).
                                                               \tag{3}
\]
Here it is convenient to take the full Gaussian in \(v\) and write \(r=y+v\). After extracting the common gamma scale at real part \(1/2\), the absolute exponent in powers of \(T\) is bounded by
\[
  -\frac{(r-y)^2}{4c}+|r|/2+m(1/2+|r|)+\epsilon .
\]
This uses the functional equation for \(r<0\) and Stirling for bounded \(r\), and again \(m=0\) to the right of one. The positive saddle has exponent \(y/2+c/4\). At \(0\le r\le1/2\) the difference from it is at most \(m(1/2+r)-(c+y-r)^2/(4c)+\epsilon\), strictly negative by (1). At negative \(r\) the exponent is at most that for \(|r|\). On the remaining negative tail \(r\le-1/2\) its upper bound is \(-y/2+c/4+\epsilon\) by completing the square, a loss of at least \(h-\epsilon\). The only surviving positive contribution is again a fixed neighborhood of the positive saddle; the rest has a uniform Gaussian saving. These arguments give (3). The right-hand zeta values in (2) and (3) have modulus bounded below by a fixed positive constant by the absolutely convergent reciprocal Euler series.

## The sign of the phase derivative

Apply Cauchy's derivative estimate to the bounded, nonvanishing quotient in (2), on a circle of fixed sufficiently small radius in the enlarged strip. The same estimates hold at all imaginary coordinates \(T+O(1)\), since \(u\log((T+O(1))/(2\pi))=c+o(1)\); the strict margin in (1) persists under this perturbation. It follows that for \(|y|\le h\),
\[
       \Re W'_u(s)/W_u(s)=L/2+O(1).
\]
Here the real part applies to the full logarithmic derivative, and the derivative of the gamma normalization is \(\alpha+2u\alpha\alpha'\). Thus \(|W_u(1/2+y+iT)|>|W_u(1/2-y+iT)|\) for \(0<y\le h\). The symmetry of the second wave excludes a zero of \(F_u\) there. Equation (3) excludes the rest of \(0<y\le1/2\); the original de Bruijn strip and reflection cover the complement.

At \(y=0\), \(F_u=2\Re W_u\) and \(d\arg W_u(1/2+iT)/dT=L/2+O(1)\). This proves simplicity and the spacing assertion by integration. To use a unit neighborhood around an endpoint exactly satisfying the stated inequality, keep the fixed slack between \(2.541/4\) and \(c_0\). Returning from \(T\) to \(x=2T\) gives the stated constants.

Together with the [reverse estimate](nov18b-heat-drift.md), the result confines the heat time needed to erase any fixed positive defect to a logarithmic scale at high ordinates. The forward estimate still leaves the interval of times below \(2.541/\log x\).
