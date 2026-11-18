# Mellin carriers on the two arithmetic combs

**Proposed unconditional estimate.** At every large real carrier \(T=2\pi q\) there is a space of \(\asymp\sqrt q\) narrow packets with the genuine linear Mellin phase and a positive Weil gap of order \(\log q\). The time locations are \(\log n\) and \(\log(q/m)\), the two locations in a balanced approximate functional equation. The proof uses the actual prime powers in the entire physical support. It handles the interactions between the two sets of locations, including close products \(dnm\ne q\). These differ from the [packets with an additive carrier](nov18b-weil-packets.md).

Fix \(0<\kappa<1\) and \(c>0\) with \(\kappa+2c<1\) and \(2c\kappa<1\). Choose two fixed smooth functions in \(C_c^\infty(-c/2,c/2)\), of unit \(L^2\) norm. Put \(r=\sqrt q\) and \(N=\lfloor\kappa r\rfloor\). Use translates of
\[
 r^{1/2}\phi(ru)e^{-iTu},\qquad r^{1/2}\psi(ru)e^{-iTu}
\]
at the locations \(\log n\), \(\log(q/m)\), respectively, for \(2\le n,m\le N\). The support lies in \((0,\log q)\) for all large \(q\). Consecutive locations in the same family differ by at least \(\log(1+1/N)>c/r\), and the two families have a gap tending to \(2\log(1/\kappa)>0\). The packets form an orthonormal system. Every linear combination satisfies
\[
 W(g)\ \ge\ \big((1-\kappa-2c)/2-o(1)\big)\log q\,\|g\|_2^2 .
 \tag{1}
\]
In particular \(\kappa=1/2, c=1/8\) gives a lower bound \((1/8-o(1))\log q\).

## The full cross term

A dilation \(d\ge2\) can match two low locations only if \(dn=m\): its overlap requires \(|dn-m|\le(1+o(1))c m/r<1\). The same argument holds in the other orientation for the high locations. Within a family the normalized prime adjacency has edge weight \(\Lambda(d)/\sqrt d\) from \(n\) to \(dn\); any carrier gauge has modulus one. The Schur weights \(v_n=n^{-1/2}\) give row sum at most
\[
 \sum_{d\mid n}\Lambda(d)+\sum_{d\le N/n}\Lambda(d)/d
 =\log N+O(1).
\]
This uses the ordinary first Mertens estimate for prime powers and includes composite prime powers. The estimate also bounds the absolute value of the Hermitian form on the coefficients.

Between the families, only the orientation from the left family to the right one is possible. The \((n,m)\) matrix entry for this orientation is
\[
 C_{nm}=\sum_d\frac{\Lambda(d)}{\sqrt d}\,
    e^{-iT\log(dnm/q)}K(r\log(dnm/q)),\qquad
 K(v)=\int\psi(s+v)\overline{\phi(s)}ds.
 \tag{2}
\]
Thus \(|K|\le1\), and \(K=0\) outside \([-c,c]\). In the row test multiply by \(v_m/v_n=\sqrt{n/m}\). On the overlap the resulting factor apart from \(\Lambda\) is \((1+O(1/r))n/r\). Put \(y=r/n\), and let \(I\) be the interval of integers \(l\) satisfying \(|r\log(nl/q)|\le c\). Its length in integers is \(B\le 1+(2c+o(1))y\). For \(l\in I\), the exact inner arithmetic sum obeys
\[
 \sum_{md=l,\ m\le N}\Lambda(d)
 \le \log l-\sum_{d\mid l,\ d\le y/(2\kappa)}\Lambda(d).
\]
Indeed all the displayed small divisors have \(l/d>N\) for large \(q\). Counting their multiples in the consecutive integers of \(I\) gives at least \(B/d-1\) for each \(d\). By the same Mertens bound and Chebyshev's estimate, the sum over all \(l\in I\) is at most
\[
 B(\log(q/n)-\log y+O_\kappa(1))+O_\kappa(y)
 =B(\log r+O_\kappa(1))+O_\kappa(y).
\]
This also applies when the displayed small-divisor sum is empty, since then \(y\) is bounded. Dividing by \(y\) and using \(1/y\le\kappa\) gives \( (\kappa+2c+o(1))\log r\) as an upper bound for the weighted row. The same calculation holds for columns since the absolute majorant is symmetric. Schur therefore bounds the cross-block norm by this quantity. Combining it with the two diagonal blocks costs at most \((1+\kappa+2c+o(1))\log r\) on the unit sphere.

All packets have Fourier magnitude \(r^{-1/2}|\widehat\phi((t-T)/r)|\) or its counterpart for \(\psi\). Off \([T/2,2T]\) the resulting mass, even weighted by \(\log(2+|t|)\), is \(O_A(q^{-A})\) per squared coefficient norm after summing the \(O(\sqrt q)\) packets. Stirling gives the gamma contribution \((\log q+O(1))\|g\|_2^2\). At either pole integration by parts after scaling the individual packet yields arbitrary powers of \(r/T\), absorbing the factor \(O(\sqrt q)\) from translating the exponential weight. The explicit formula proves (1).

## The sharp edge within a single family

For the real symmetric matrix \(A_N\) on *all* \(1\le n\le N\), with entries \(\Lambda(d)/\sqrt d\) on the edges from \(n\) to \(dn\), one in fact has
\[
 \lambda_{\max}(A_N)=\log N-\gamma_E+o(1).
 \tag{3}
\]
Here the index 1 is included in both the upper and the lower comparison. For \(a_n=b_n/\sqrt n\) put \(U=\log N\) and
\[
 \mathcal E=\sum_{dn\le N}\frac{\Lambda(d)}{dn}|b_{dn}-b_n|^2,\qquad
 R(t)=\log t-\sum_{d\le t}\frac{\Lambda(d)}d .
\]
Completing the squares gives \(\langle(U-A_N)a,a\rangle=\mathcal E+\sum_{n\le N}R(N/n)|a_n|^2\). The classical prime number theorem with its de la Vallée Poussin remainder and partial summation give \(R(t)\to\gamma_E\) (the constant follows by expanding \(-\zeta'/\zeta(1+s)=1/s-\gamma_E+O(s)\) at zero). In particular \(R\) is bounded. The vector \(b_n=1\) has zero difference energy and places \(o(1)\) of its normalized mass at \(n>N/Y\) if \(Y=\exp(\sqrt U)\); it supplies the required upper comparison for the infimum of the residual.

Conversely any normalized vector minimizing the residual has \(\mathcal E=O(1)\) by this comparison and the bounded potential. For \(n>N/Y\) use \(\log n=\sum_{d\mid n}\Lambda(d)\) and bound \(|b_n|^2\le2|b_n-b_{n/d}|^2+2|b_{n/d}|^2\). On summing with weights \(\Lambda(d)/n\), the latter term costs \(O(1+\log Y)\|a\|^2\): for each lower endpoint \(j=n/d\), the remaining sum is \(\sum_{N/(Yj)<d\le N/j}\Lambda(d)/d\). Thus the mass on \(n>N/Y\) is \(O((1+\log Y)/\log(N/Y))=o(1)\). Everywhere else \(R(N/n)=\gamma_E+o(1)\) uniformly. This proves (3). Establishing a positive Weil gap on the narrow combs still requires (2); the two separate graph bounds cannot supply it.
