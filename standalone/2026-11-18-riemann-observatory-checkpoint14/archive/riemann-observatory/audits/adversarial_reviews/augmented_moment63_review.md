# Independent review of the augmented lattice moment classification

The classification for feasible data is valid. The closure adds a ray in the highest moment for \(n\ge1\), and a point on that ray can have interior pure moments while its augmented data are infeasible. The support-plane argument can distinguish exact feasibility from such escape at each boundary point of the closure. This concerns positive lattice profiles representing finite prefix data. [Proposed classification](../latest62_inverse_adjacent_lattice.md#exact-classification-with-the-constant-term-included) · [Earlier finite-moment review](finite_moment63_review.md)

## Realizability and planting

Write \(\Lambda=\{m(m-1):m\ge2\}\) and \(g(x)=4/(\sqrt{1+4x}-1)^2\). For \(M_0>0\), normalize the multiple part by its mass. The coordinates are the moments of a probability measure on \(\Lambda\) through degree \(n\), omitting its initial coordinate 1, and \(c=C(0)/M_0\). The vertical slack is \(s=W_1/M_0=c-\int g\,d\nu/M_0\). If \(M_0=0\), positivity forces zero multiple mass and all its moments vanish, with \(W_1=C(0)\ge0\).

For the finite representation of the multiple part, let \(S\) consist of the points \(z(x)=(x,\ldots,x^n,g(x))\) at active lattice nodes. Every coordinate is integrable. Truncation of this countable distribution and replacement of the omitted mass by a fixed member of \(S\) puts its expectation in \(\overline{\operatorname{conv} S}\). If this expectation were in its relative boundary, a relative supporting affine functional, nonzero on the affine hull, could be oriented nonnegative on \(S\) with zero average. Every active weight is positive, so the functional would vanish on all of \(S\), a contradiction. Consequently the expectation is in the relative interior of the closed hull. To see that it lies in \(\operatorname{conv} S\), surround it by a simplex in that relative interior and approximate the simplex vertices by points of \(\operatorname{conv} S\). Small perturbations preserve the strict barycentric inequalities for the expectation. The zero-dimensional case is immediate. Carathéodory gives at most \(n+2\) active atoms. This is also the discrete instance of the cited positive cubature theorem. [Bayer–Teichmann, Corollary 2](https://arxiv.org/pdf/math/0502473v2)

It follows that the feasible normalized set is
\[
 A_n=\operatorname{conv}\{z(x):x\in\Lambda\}+\mathbb R_{\ge0}e_c,
\]
where \(e_c\) is the unit vector for the constant term. Its projection has full dimension by the Vandermonde determinant, and the independent vertical direction gives full dimension to \(A_n\). At an interior datum \(y\), for any prescribed lattice node, the point \((y-\epsilon z(x))/(1-\epsilon)\) remains in \(A_n\) for all sufficiently small \(\epsilon>0\). Represent that point with finite support and restore the removed atom. The same argument plants every lattice node simultaneously if one subtracts a small multiple of the whole augmented vector of a probability with positive weights at every node and finite moments, with slack zero. For example use weights proportional to \(e^{-x}\). The residual data have a finite representation and the restored competitor has all square-root exponential moments.

There is also an exact relation with the unaugmented moment hull. An augmented datum is interior if and only if its pure moments are interior in that hull and it has at least one representation with positive simple slack. For necessity, projection of an interior ball gives interior pure moments, while a small downward translation in the last coordinate is still feasible. Its representative acquires positive slack when returned upward. For sufficiency, suppose a feasible datum with positive slack and interior pure moments lay on the boundary. The supporting functional below would then have \(\beta=0\), giving a proper supporting functional for the interior pure moments, a contradiction. An individual representation of an interior datum may itself have zero slack.

## Boundary certificates and exact contact bound

A feasible boundary point of \(A_n\) is on the boundary of its closure. In fact the interior of the closure equals the interior of \(A_n\) by the simplex argument above. Orient a nonzero supporting affine functional nonnegative on the closure and write its value on generators as \(h(x)=p(x)+\beta g(x)\), where \(\deg p\le n\) and the vertical ray forces \(\beta\ge0\). Its value at a feasible datum is \(\int h\,d\nu/M_0+\beta s\). A zero value forces \(\beta s=0\) and every occupied lattice node to be a root of \(h\).

For \(\beta=0\), the nonzero polynomial has at most \(n\) distinct roots. For \(\beta>0\), rationalizing gives
\[
 g(x)=x^{-1}+\frac{1}{2x^2}
      +\frac{x^{-2}+4x^{-1}}{2\sqrt{1+4x}}.
\]
Each inverse power and the shifted inverse square root is completely monotone on \((0,\infty)\), and the product rule preserves alternating derivative signs. The first term makes each sign strict, so \((-1)^k g^{(k)}(x)>0\) for all \(k\ge0\). Thus \(h^{(n+1)}=\beta g^{(n+1)}\) is never zero. Rolle gives at most \(n+1\) distinct real roots in this interval. The first \(n+1\) moments determine their masses by Vandermonde, and the constant term determines simple slack. This proves the proposed uniqueness for feasible boundary data.

The bound for \(\beta>0\) can be sharpened by parity. If there are \(n+1\) distinct lattice contacts \(x_1<\cdots<x_{n+1}\), the polynomial must equal \(-\beta I_n[g]\), where \(I_n[g]\) interpolates \(g\) at the contacts. The interpolation remainder for every other \(x>0\) has sign
\[
 (-1)^{n+1}\operatorname{sgn}\prod_{i=1}^{n+1}(x-x_i).
\]
If \(n\) is even this is negative past the largest contact. Infinitely many such lattice points exist, so at most \(n\) contacts are possible. For odd \(n\), \(n+1\) contacts occur exactly when \((x_1,x_2),(x_3,x_4),\ldots,(x_n,x_{n+1})\) pair adjacent lattice nodes. Those are precisely the intervals where the even-degree product is negative. Conversely interpolation on such pairs gives a nonnegative certificate. For positive even \(n\), one can attain \(n\) contacts by interpolating on the first \(n\) lattice nodes with degree \(n-1\). The remainder has positive sign at every other lattice node. Choosing strictly positive probabilities on every contact in these constructions makes the support bound sharp on the feasible boundary.

## Escape and the exact boundary of the closure

For \(n\ge1\) the closure is
\[
 \overline{A_n}=A_n+\mathbb R_{\ge0}e_n,
\]
where \(e_n\) is the unit vector for the highest pure moment. To prove it, add an initial mass coordinate to the lattice generators and divide them by \(1+x^n+g(x)\). Include the vertical slack generator \(e_c\) and the only additional limit point, the unit vector \(e_n\) with initial mass coordinate zero. The resulting generator set is compact, and all its points lie on the slice where the sum of mass, highest moment and constant coordinates is 1. Its convex hull is compact, and its nonnegative cone is closed because this positive linear functional recovers the conic scale. The normalized lattice generators and the two rays therefore describe the closed original cone. Conversely the limit generator and its nonnegative multiples belong to the original cone closure. Intersect at mass coordinate 1. Equivalently a closed-cone approximation can be rescaled to mass coordinate 1 because those coordinates tend to 1. For \(n=0\), \(A_0=(0,\infty)\) and its missing closure boundary is \(c=0\), since \(g(x)>0\) decays to zero.

At a point of the closure boundary the supporting coefficient \(p_n=[x^n]p\) is nonnegative, by the escape ray. In a closed representation let \(a\ge0\) be the escape coefficient. Complementarity gives
\[
 \int h\,d\nu/M_0+\beta s+a p_n=0.
\]
If \(p_n>0\), every closed representation has \(a=0\) and the datum is feasible. If \(p_n=0\), then \(\deg p\le n-1\). There are at most \(n-1\) lattice roots when \(\beta=0\) and at most \(n\) when \(\beta>0\), applying the same derivative argument with order \(n\). The moments through degree \(n-1\) then uniquely determine the lattice weights on the contact set. The constant term determines simple slack and the highest moment determines \(a\). Thus a normalized closure-boundary datum has a unique representation by lattice mass, slack and escape. It is feasible exactly when its recovered escape coefficient vanishes. This applies even when the convex hull is nonclosed and uses a supporting certificate, not a conclusion inferred from approximate nonnegative polynomial tests.

For \(n=1\) the escape ray is already absorbed by the feasible set. From any feasible datum, mix a representing probability with an atom at a sufficiently high node. Its \(g\)-value is below the original mean cost while its location exceeds the desired new mean. An appropriate mixture increases the first moment to that value without increasing the cost. Hence \(A_1\) is closed. For every \(n\ge2\), \(z(2)+e_n\) is in the closure and infeasible. Its first moment 2 forces unit mass at 2, which fails to give its highest moment. Thus the closure inclusion is strict for every \(n\ge2\).

For \(n=2\) consider exact normalized data
\[
 (M_0,M_1,M_2,C(0))=(1,6,37,1/4).
\]
For any lattice node \(x>6\), put mass \(1/[(x-6)(x-2)]\) at \(x\), mass \(1/[4(x-2)]\) at 2, and the remainder at 6. The mean is 6 and the variance is 1. At \(x=12\) all three weights are positive and the pure moments are interior by the nondegenerate three-node simplex. As \(x\to\infty\), these probabilities' \(g\)-costs converge to \(g(6)=1/4\). Each value is strictly greater than \(1/4\) by strict Jensen since the variance is positive. No measure representing the exact pure data can have \(g\)-cost at most \(1/4\), because equality in Jensen would force a point mass at 6. Thus the augmented point is an infeasible closure boundary point even with interior pure data. The tangent certificate \(g(x)-g(6)-g'(6)(x-6)\) has sole contact 6 and degree-one polynomial part. Its recovered escape is exactly 1. Every approximant is finitely supported with all exponential moments. It is a common quantitative bound on higher moments or tails that can exclude such escape in a limiting computation. [Earlier nonaugmented escape test and moment-cap bounds](finite_moment63_review.md#the-lattice-moment-problem-and-certified-optimization)
