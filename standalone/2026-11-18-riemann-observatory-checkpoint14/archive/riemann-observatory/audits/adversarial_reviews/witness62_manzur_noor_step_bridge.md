# Manzur–Noor step bridge and the nonprincipal anchor

I checked Manzur–Noor, arXiv:2610.03568v1, especially (B)–(D), (11)–(14), (20) and (21). The inspected PDF SHA-256 is ba5c1ab46edf1dbef9741dd1e999ec492c0be59bc65d82cc7ac7dfab8520c076. The step-map and anchor calculations below are independent reconstructions. [Primary source](https://arxiv.org/pdf/2610.03568v1)

## Exact unitary map

Let \(S\) be the closed subspace of \(\mathcal H=L^2([1,\infty),dx/x^2)\) consisting of unit-interval step functions, with cell values \(b_n\) on \([n,n+1)\). Its squared norm is \(\sum_{n\ge1}|b_n|^2/[n(n+1)]\). On disk Hardy coefficients \(a_j\), \(j\ge0\), define
\[
 (Ba)_n=\sum_{j<n}a_j-na_n,\qquad n\ge1.
\]
For \(j\ge1\), \(Be_j\) vanishes on cells \(n<j\), equals \(-j\) at \(n=j\), and equals 1 at \(n>j\). Also \(Be_0=1\). Their squared norms are 1 exactly. Pairing any two different such vectors gives zero by \(\sum_{n>j}1/[n(n+1)]=1/(j+1)\). To see completeness, if \(b\) is perpendicular to every one, put \(T_j=\sum_{n>j}b_n/[n(n+1)]\). Cauchy–Schwarz gives convergence. Then \(T_0=0\), \(b_j/(j+1)=T_j\) for \(j\ge1\), and \(T_{j-1}=(1+1/j)T_j\), forcing all values to vanish. Thus \(B\) extends as a unitary onto \(S\), with
\[
 (B^{-1}b)_0=T_0,\qquad (B^{-1}b)_j=T_j-b_j/(j+1),\quad j\ge1.
\]
For general \(\ell^2\) coefficients the cell formulas follow from finite coordinate continuity. The jumps with \(b_0=0\) are \(b_n-b_{n-1}=n(a_{n-1}-a_n)\). The series of the analytic logarithms defining \(h_k\) gives \(n(a_{n-1}-a_n)=k\mathbf1_{k\mid n}-1\). Hence \(Bh_k=k(\lfloor x/k\rfloor-\lfloor x\rfloor/k)\), including the sign.

Let \(Mf(s)=\int_1^\infty f(x)x^{-s-1}\,dx\). This is the Laplace transform under \(x=e^u\) of \(e^{-u/2}f(e^u)\), with parameter \(s-1/2\), and is an isometry into the right half-plane \(H^2\) with boundary measure \(dt/(2\pi)\). On finite Hardy coefficient sequences, summing the jump formula, or integrating each basis vector, gives the exact relation \(\Lambda^{(s)}(a)=-M(Ba)(s)\) for the source functional (B). Both sides extend as continuous evaluations for \(\Re s>1/2\). In particular the factor \(1/s\) in (B) has not been absorbed into the isometry.

## Jump phase and vertical operator norm

By Manzur–Noor (13), \(J_\tau=BT_\tau B^{-1}\) multiplies physical jumps by \(n^{i\tau}\), for all \(S\) by continuity of the cell functionals. A finite Hardy coefficient sequence yields finitely many jumps, for which \(sMf(s)=\sum_n(b_n-b_{n-1})n^{-s}\) exactly. Density and bounded evaluation therefore give
\[
 M(J_\tau f)(s)=\frac{s-i\tau}{s}Mf(s-i\tau),\qquad \Re s>1/2 .
\]
The multiplier factor is essential. For \(f=1\) both sides above are \(1/s\), while a pure vertical translation would give \(1/(s-i\tau)\).

The right-hand side defines a bounded operator \(\widetilde J_\tau\) on the full physical space \(\mathcal H\), by the Mellin–Hardy identification. Vertical translation is unitary, and the analytic multiplier norm is the supremum of the boundary modulus. It equals \(\sqrt{1+\tau^2}+|\tau|\), obtained by maximizing \(\sqrt{(\tfrac14+(t-\tau)^2)/(\tfrac14+t^2)}\) over real \(t\). The multiplier norm equality in Hardy space follows from point evaluation kernels, and the maximum can be approached through interior points.

This bound is sharp even on \(S\). To see this, take smooth compactly supported ambient test \(f\) on \((1,\infty)\) arbitrarily close in norm ratio to the ambient operator norm, available by density. The integer dilation \(U_m f(x)=\sqrt m f(x/m)\), using zero extension, is an isometry, and \(\widetilde J_\tau U_m=m^{i\tau}U_m\widetilde J_\tau\) follows from the Mellin formula. The step function \(\sqrt m f(\lfloor x\rfloor/m)\) approximates \(U_mf\) in norm by \(O_f(1/m)\), as is seen after the change of variables \(y=x/m\). Taking \(m\to\infty\) preserves the ambient norm ratio in \(S\). Thus \(\|J_\tau\|_S=\sqrt{1+\tau^2}+|\tau|\), and \(J_\tau^{-1}=J_{-\tau}\). The exact bound is not needed for the distance argument.

## Anchor evaluation and distance

For nonprincipal \(\chi\) let \(L=L(\cdot,\chi)\) and \(S_\chi(x)=\sum_{n\le x}\chi(n)\), with value zero for \(x<1\). Bounded periodic partial sums imply \(S_\chi\in S\) and \(M S_\chi(s)=L(s)/s\) for \(\Re s>1/2\) by ordinary partial summation and continuation through \(\Re s>0\). For \(k\ge2\) the anchored generator
\[
 g_{\chi,k}(x)=S_\chi(x/k)-k^{-1}S_\chi(x)
\]
has Mellin transform \(L(s)(k^{-s}-k^{-1})/s\) and \(Mg_{\chi,k}(1)=0\). In \(\mathcal H\), the evaluation \(Mf(1)=\langle f,1\rangle\) has norm 1, and its representer 1 already lies in \(S\). If \(W_\chi\) is the closed span of the anchored generators in \(S\), the shifted generator therefore obeys the unconditional lower bound
\[
 \operatorname{dist}_S(J_\tau g_{\chi,k},W_\chi)
 \ge |M(J_\tau g_{\chi,k})(1)|
 =\frac{|L(1-i\tau,\chi)|}{k}\,|k^{i\tau}-1|.
\]
The factor \(1-i\tau\) in the jump shift cancels the denominator \(1-i\tau\) from \(Mg_{\chi,k}\). The classical nonvanishing on \(\Re s=1\) makes this positive for \(\tau\log k\notin2\pi\mathbb Z\). For each \(\tau\ne0\), at least one of \(k=2,3\) works because \(\log2/\log3\) is irrational. When \(k^{i\tau}=1\), the unconditional formula only gives a zero lower bound. This is a failure of invariance for the anchored nonprincipal space, independent of GRH. It is separate from the source zeta comparison (21), where the annihilator is at a zeta zero with possibly different evaluation norm.

The lower bound becomes an equality if the unanchored ordinary approximation to the step target 1 holds, as supplied by the fixed-character GRH upper theorem for primitive characters and the finite Euler factor transfer for imprimitive ones. Here is the necessary closure argument. The unrestricted span of \(S_\chi(x/n)\) contains 1 in its closure under that hypothesis, by Mellin isometry. Integer dilations preserve this closed span, so it contains every \(1_{[n,\infty)}\), whose consecutive differences span a dense set in \(S\). The unanchored span is consequently dense in \(S\). For \(f\in S\) with \(Mf(1)=0\), choose unrestricted approximating vectors \(f_j\), and set
\[
 f_j^0=f_j-\frac{Mf_j(1)}{L(1,\chi)}S_\chi .
\]
The nonzero denominator follows from the nonprincipal value at 1. Each \(f_j^0\) is a finite anchored combination and converges to \(f\) by continuity of evaluation. Thus \(W_\chi=\ker(M(\cdot)(1))\) **inside \(S\)** under the stated density hypothesis, and the exact orthogonal distance is the right-hand side above. No closure in the full half-plane Hardy space is asserted, since unit-step functions already form a proper closed subspace of the full physical space. The underlying zeta/principal pole is different, as the evaluation of an anchored zeta or principal product can be nonzero. [Anchor comparison](witness62_anchor_nonprincipal.md)

## Resonant converse and the fixed-strip density input

Fix \(k\ge2\) and \(\tau\ne0\) with \(k^{i\tau}=1\). Under GRH for the primitive inducing character, the unrestricted approximation and the closure argument above imply \(J_\tau g_{\chi,k}\in W_\chi\), since resonance makes its evaluation at 1 vanish. For the converse, assume this membership. At any zero \(\rho\) of \(L(\cdot,\chi)\) with \(\beta=\Re\rho>1/2\), the bounded evaluation \(M(\cdot)(\rho)\) annihilates every anchored generator, hence annihilates \(W_\chi\). The exact shift formula gives
\[
 0=\frac{L(\rho-i\tau,\chi)}{\rho}
       \left(k^{-\rho+i\tau}-k^{-1}\right).
\]
Classical nonvanishing on \(\Re s\ge1\) forces \(\beta<1\), so the parenthesized factor has terms of unequal moduli \(k^{-\beta}>k^{-1}\). It is nonzero for all iterates on the vertical line of \(\rho\), even if an ordinate becomes zero. Thus \(\rho-in\tau\) is a zero for every integer \(n\ge0\). With \(\tau\ne0\) these are distinct and at least a constant times \(T\) lie in \(|\Im s|\le T\) for sufficiently large \(T\).

I inspected the scanned PDF of Matti Jutila, *On a density theorem of H. L. Montgomery for L-functions*, Annales Academiae Scientiarum Fennicae A I Math. no. 520 (1972), DOI 10.5186/aasfm.1972.520, SHA-256 12e6598993164ef011de1f623629e77ac4f65aafc26ce69cfc7d6867eb732971. Section 1.1, PDF p. 3, defines \(N(\alpha,T,D)\) for the whole product over characters modulo \(D\) in the closed rectangle \(\alpha\le\Re s\le1,\ |\Im s|\le T\). Its displayed Montgomery estimate (1.1) has exponent \(\min(3/(2-\alpha),2/\alpha)(1-\alpha)\) and log factor \((\log DT)^{14}\), uniformly for \(1/2\le\alpha<1,\ T\ge2,\ D\ge1\). At a fixed \(D=q\) and any fixed \(1/2<\alpha<\beta\), this is \(o(T)\) since \(3(1-\alpha)/(2-\alpha)<1\). The product counts the progression because every factor is holomorphic at each progression point (\(\beta<1\)), including the principal factor whose only pole is at 1. The density bound already includes both signs of the ordinate and needs no identification of a complex character with its conjugate.

This contradicts the progression and excludes every right-half critical-strip zero. The imprimitive finite Euler factors have zeros only on \(\Re s=0\), so \(L(\cdot,\chi)\) and its inducing primitive function have the same critical-strip zeros. The primitive functional equation reflects left-half strip zeros to the right for that same character by the conjugate reflection \(s\mapsto1-\bar s\). Hence GRH follows. This proves the resonant equivalence for each specified pair and fixed character. The converse alone needs no resonance, but the forward inclusion needs it because of the anchor at 1. The case \(\tau=0\) gives automatic generator membership and cannot test GRH. [Jutila’s primary scan](https://www.acadsci.fi/mathematica/1972/no520pp01-13.pdf)
