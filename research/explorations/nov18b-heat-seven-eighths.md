# Heat propagation from the seven-eighths bound

The half-plane hypothesis in this note is that every nontrivial Riemann zero has real part at most \(7/8\). The new OpenAI formalization includes this statement in its \(q=1\) specialization. The implications below use the zeta specialization only. [Formalized result](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Nonvanishing.lean) · [Hakimoglu-Brown's conditional finite-time calculation](https://arxiv.org/abs/2610.12803)

**Proposed asymptotic consequences.** Write \(F_u(1/2+iz)=8H_{4u}(2z)\), \(L=\log(T/(2\pi))\) and \(c=uL\). For fixed \(c>0\), the largest possible high-ordinate positive defect of an \(F_u\)-zero, for times with \(uL\to c\), is at most
\[
       \left(\frac38-\frac{54855}{92791}c\right)_+ .                       \tag{1}
\]
For \(c>92791/146280=0.63433825\ldots\), all high zeros are real and simple in the Xi coordinate. In Polymath time the resulting high-ray threshold is any constant strictly greater than \(4(92791/146280)=2.5373530\ldots\) for \(t\log x\). The threshold height is unevaluated. An explicit symmetric positive spectral model below saturates (1) as long as its right side is positive.

There is a further consequence with different hypotheses. Let
\[
 A=\limsup_{\xi(1/2+\delta+iT)=0,\ T\to\infty}|\delta| .
\]
Under the Lindelöf hypothesis, the upper envelope of possible high-ordinate heat defects at \(uL\to c\) equals \((A-c)_+\) for every fixed \(c>0\). Here an envelope is the supremum of zero and all subsequential limit defects. For \(c>A\) every sufficiently high zero on these rays is real and simple. This second statement does not require the seven-eighths input. The use of subsequences allows for the bounded ordinate displacement of zeros in the reverse estimate.

## A growth majorant and its time evolution

Suppose more generally that physical zero defects have limsup at most \(a\le1/2\). For any fixed positive distance inside \(\sigma>1/2+a\), with a bounded upper bound on \(\sigma\), one has
\[
 |\log\zeta(\sigma+iT)|+|(\log\zeta)'(\sigma+iT)|+
 |(\log\zeta)''(\sigma+iT)|=o(\log T).                         \tag{2}
\]
The branch continues horizontally from \(\sigma=4\). For the proof use the rectangle and Borel–Carathéodory argument in the [reverse estimate](nov18b-heat-drift.md) at time zero, where its normalized function is \(\zeta\). If only the limsup hypothesis is available, take the left edge an arbitrarily small fixed distance to the right of \(1/2+a\) and then let the height tend to infinity. This gives \(\mu(1/2+a)=0\) by continuity of the convex zeta growth exponent, also when \(a=0\).

Let \(m(r)\ge\mu(1/2+r)\) be a continuous piecewise affine majorant on \(0\le r\le a\), with \(m(a)=0\); take \(m=0\) to its right. Suppose \(y\ge0\) and
\[
             y> a-c,\qquad
             y>\sup_{0\le r\le a}\{r-c+2\sqrt{c\,m(r)}\}.          \tag{3}
\]
Then for sufficiently large heights there are no \(F_u\)-zeros with defect near \(y\) if \(y>0\). If (3) holds at zero, the zeros on the central line are real and simple in a surrounding strip. The assertions are uniform on compact parameter sets with the strict inequalities.

Here are details of the saddle argument where the Dirichlet series at the saddle may no longer converge absolutely. For fixed positive distance from the boundary in (3), the point \(s+c\), \(s=1/2+y+iT\), lies in the interior of (2). Stirling gives \((\log\xi)'=L/2+o(L)\) and \((\log\xi)''=o(L)\) on a fixed neighborhood there. The analytic saddle \(s_*=s+2u(\log\xi)'(s_*)\) exists by contraction, has \(s_*=s+c+o(1)\), and depends holomorphically on \(s\) for fixed \(u\). Moving a fixed small saddle segment onto the parallel line through \(s_*\), Taylor expansion gives the relative integral \(1+o(1)\) after division by \(e^{-(s_*-s)^2/(4u)}\xi(s_*)\). Its logarithmic modulus equals the gamma scale at \(1/2+iT\) plus \((y/2+c/4)L+o(L)\), by (2). Endpoint connectors are exponentially small in \(L\).

For displacement \(r\ge0\) in the remaining horizontal integral, the logarithmic exponent relative to that stationary scale, divided by \(L\), is at most
\[
                   m(r)-(y+c-r)^2/(4c)+o(1).
\]
This follows first with an arbitrary positive growth allowance in place of \(o(1)\); there are finitely many linear pieces. Inequalities (3) and compactness give a fixed negative margin up to \(r=a\). Beyond \(a\), the exponent is uniformly negative outside a fixed neighborhood of the saddle. The negative reflection \(-r\) costs an additional \(ry/c\) relative to the displayed bound. For \(y>0\) this also supplies strict loss in the reflected saddle neighborhood. The unbounded tails are controlled by the gamma and Gaussian bound as in the [unconditional forward calculation](nov18b-heat-forward.md). This proves nonvanishing for positive \(y\). If (3) holds at zero, apply the calculation to the positive half wave for \(|y|\) sufficiently small, using continuity of the strict margin and the functional equation for the short part of its integration range lying left of the central line. Its derivative has real logarithmic part \(L/2+o(L)\), by differentiating the stationary factor and applying Cauchy to the relative error on a fixed neighborhood. Reflection gives unequal opposing wave moduli for \(y>0\) near zero and a strictly increasing phase on the line. In fact consecutive local real zeros then have spacing \((2\pi/L)(1+o(1))\) in the \(T\) coordinate. For unbounded \(c=uL\), with \(0\le u\le1/8\), the previously published high-ray result applies. [Polymath15, Theorem 1.5](https://arxiv.org/abs/1904.12438)

## Exact constants for seven-eighths

Take \(a=3/8\). Convex interpolation through the three points with abscissae \(1/2\), \(88225/153852\), and \(7/8\), taking the Trudgian–Yang bounds at the first two points and zero at the third, gives
\[
 m(r)=\max\left\{\frac37(13/36-r),\
                        \frac{37936}{92791}(3/8-r)\right\},
           \qquad 0\le r\le3/8 .
\]
For a line \(k(b-r)\), allowing all \(r\le b\), the supremum in (3) is \(b-(1-k)c\), by completing a square in \(\sqrt{b-r}\). The second line dominates both bounds for \(0<c\le92791/146280\): the two affine bounds have that ordering at both endpoints. For \(c\) greater than this number the two upper bounds are strictly negative. This proves (1) and the simplicity assertion. [Trudgian–Yang, Theorem 2.4](https://arxiv.org/abs/2306.05599)

Under Lindelöf take \(a=A\) and \(m=0\) throughout. Formula (3) gives the upper bound \((A-c)_+\). If \(c<A\), choose any sequence of physical zeros approaching defect \(A\) on the positive side by reflection and apply the [reverse transport inequality](nov18b-heat-drift.md) with \(u=c/L\). It gives nearby heat zeros with defects at least \(A-c-o(1)\), and their bounded ordinate shifts preserve the limit of \(uL\). This proves the asserted equality.

## An obstruction to time-zero feedback from the strip

Fix \(a=3/8\), \(k=37936/92791\), \(0<K<1/2\). The explicit family
\[
 P_L(z)=2\cosh(Lz/2)+2K e^{kaL}\cosh((1/2-k)Lz)
\]
has a positive symmetric four-atom spectral measure, complex conjugation and reflection symmetry, and satisfies the identical Gaussian heat equation in the displacement coordinate. For \(\Re z=r\ge a\), the leading exponential \(e^{Lz/2}\) strictly dominates the three others for sufficiently large \(L\); reflection gives a strip of width \(a\). For \(r\ge0\), after extracting \(e^{Lr/2}\), the magnitude costs at most exponent \(\max(0,k(a-r))L+O(1)\), within the majorant used above. Its heat transform at \(u=c/L\) has its two groups multiplied by \(e^{cL/4}\) and \(e^{c(1/2-k)^2 L}\). Where \(b=a-(1-k)c>0\), the positive exponentials of the two groups cancel exactly at
\[
             z=b+(\log K+i\pi)/(kL).
\]
The two negative exponentials are smaller by \(e^{-\kappa L}\) for some \(\kappa>0\) in a neighborhood. Rouché on a circle of radius \(e^{-\kappa L/2}/L\) therefore gives a zero there, and elementary dominance excludes zeros right of \(b+O(1/L)\). Thus the strip, the growth majorant, the symmetric positive spectral measure and the heat flow at this scale permit exactly the edge (1), including the time-zero edge \(a\). This is a local model family. A strict improvement of seven-eighths for zeta would need more information than these estimates supply.
