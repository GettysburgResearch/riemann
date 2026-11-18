# A single infinitesimal membership criterion for RH

17 November 2026. Fix any integer \(k\ge2\). Let \(S\) be the unit-interval step subspace of \(L^2([1,\infty),dx/x^2)\), and put
\[
 f_j(x)=B h_j(x)=j\lfloor x/j\rfloor-\lfloor x\rfloor,\qquad
 W=\overline{\operatorname{span}}^{\,S}\{f_j:j\ge2\}.
\]
Let \(G\) be the strong infinitesimal generator of the Manzur–Noor jump group \(J_\tau\) on \(S\). Then
\[
 \mathrm{RH}\quad\Longleftrightarrow\quad Gf_k\in W .
\]
The reverse implication uses zero multiplicity and continuous Mellin derivatives. The forward implication uses the classical integer-span criterion recorded in Manzur–Noor (A). The spectral statements about the generator are separate from this membership proof. [Manzur–Noor, pinned arXiv v1](https://arxiv.org/pdf/2610.03568v1) · [Step model](director_manzur_noor_round8.md) · [Closed generator](jump_generator63_skeptic.md)

## Domain and signs

Write \(n=\lfloor x\rfloor\), \(b_n=f_k|_{[n,n+1)}\), and \(b_0=0\). Then \(b_n=-(n\bmod k)\) is bounded. The jump transport and summation by parts give
\[
 (J_\tau b)_n=e^{i\tau\log n}b_n
   -i\tau\sum_{r<n}b_r\int_{\log r}^{\log(r+1)}e^{i\tau u}\,du.
\]
Consequently \(|((J_\tau-I)b)_n/\tau|\le2\|b\|_\infty\log n\) for \(\tau\ne0\). Its dominating sequence is square summable against \(w_n=1/[n(n+1)]\). Coordinatewise convergence and dominated convergence give \(f_k\in\mathcal D(G)\) and
\[
 (Gf_k)|_{[n,n+1)}
   =i\left[(\log n)b_n-\sum_{r<n}\log((r+1)/r)b_r\right]
   =i\sum_{r\le n}(\log r)\big(k1_{k\mid r}-1\big).
\]
Equivalently, for \(q=\lfloor n/k\rfloor\), this cell value is \(i[k\log(q!)+kq\log k-\log(n!)]\), with \(0!=1\).

For \(\mathcal M f(s)=\int_1^\infty f(x)x^{-s-1}\,dx\), integrating the jumps over \(\Re s>1\) gives
\[
 s\mathcal M f_j(s)=\zeta(s)(j^{1-s}-1)=:F_j(s).
\]
Indeed \(\lfloor x/j\rfloor=\sum_{r\ge1}1_{x\ge jr}\), and \(s\mathcal M(1_{x\ge n})(s)=n^{-s}\). The factor \(j^{1-s}-1\) cancels the pole of \(\zeta\) at 1 and gives \(F_j(1)=-\log j\). Holomorphy extends the identity to \(\Re s>1/2\). This identifies the zeta span in the criterion explicitly. The nonprincipal-character anchored span from the prior audit has a different evaluation at 1.

The group identity is \(s\mathcal M(J_\tau f)(s)=(s-i\tau)\mathcal M f(s-i\tau)\). Since \(f_k\) lies in the strong generator domain and \(\mathcal M(\,\cdot\,)(s)\) is bounded on \(S\), differentiation gives
\[
 \mathcal M(Gf_k)(s)=-\frac{i}{s}F_k'(s)
 =-\frac{i}{s}\frac{d}{ds}\big[\zeta(s)(k^{1-s}-1)\big].
\]
As a sign check, the jump expression gives \(s\mathcal M(Gf_k)(s)=i\sum_{n\ge1}(\log n)(k1_{k\mid n}-1)n^{-s}\) on \(\Re s>1\), which is also \(-iF_k'(s)\).

## Multiplicity and the continuous witness

For \(z\) with \(\beta=\Re z>1/2\), differentiation under the integral gives the continuous linear functional
\[
 L_{z,a}(u)=(\mathcal M u)^{(a)}(z)
 =\int_1^\infty u(x)(-\log x)^a x^{-z-1}\,dx,\qquad
 \|L_{z,a}\|\le\frac{\sqrt{(2a)!}}{(2\beta-1)^{a+1/2}} .
\]
Cauchy–Schwarz reduces the square of the constant to \(\int_1^\infty x^{-2\beta}(\log x)^{2a}\,dx\). The same estimate on compact subsets of the half-plane supplies local domination for differentiation. It applies to every \(u\in S\), including limits in the norm defining \(W\).

If RH fails, the symmetry of nontrivial zeros gives a zero \(\rho\) in \(1/2<\Re\rho<1\). Let \(m\ge1\) be its exact order. Since \(\rho\ne0\), every \(\mathcal M f_j\) vanishes to order at least \(m\) at \(\rho\). Hence \(L_{\rho,a}\) vanishes on \(W\) for \(0\le a<m\). The modulus \(k^{1-\Re\rho}>1\) guarantees \(k^{1-\rho}-1\ne0\), regardless of the ordinate. Thus \(F_k\) has exact order \(m\) there. Write \(F_k(s)=(s-\rho)^m E(s)\). In \(-iF_k'(s)/s\), the coefficient of \((s-\rho)^{m-1}\) is \(-imE(\rho)/\rho\), yielding
\[
 L_{\rho,m-1}(Gf_k)
   =-\frac{i}{\rho}\,\zeta^{(m)}(\rho)(k^{1-\rho}-1)\ne0 .
\]
This covers a simple zero with \(m=1\), zeros of higher order and either ordinate sign. The logic is conditional on the existence of a zero in the open right half of the critical strip and has no nonzero-ordinate assumption. A left-half zero reflects into that open right half by the functional equation. Hence \(Gf_k\in W\) rules out every off-line nontrivial zero. Conversely RH makes \(W=S\) by the integer-span criterion and unitarity of \(B\), so \(Gf_k\in W\).

For a specified off-line \(\rho\), the argument gives the explicit lower bound
\[
 \operatorname{dist}_S(Gf_k,W)
 \ \ge\
 \frac{(2\Re\rho-1)^{m-1/2}}{\sqrt{(2m-2)!}}\,
 \frac{|\zeta^{(m)}(\rho)|\,|k^{1-\rho}-1|}{|\rho|}.
\]
Since \(f_k\in W\) and \(J_\tau f_k=f_k+\tau Gf_k+o_S(|\tau|)\), orthogonal projection onto \(W^\perp\) gives
\[
 \operatorname{dist}_S(J_\tau f_k,W)
 =|\tau|\operatorname{dist}_S(Gf_k,W)+o(|\tau|).
\]
An off-line zero therefore excludes membership for every sufficiently small nonzero real \(\tau\), and supplies a positive first-order coefficient. The interval of times can depend on \(k\) and the zero.

## Relation to the preceding power argument

The earlier power argument tested only \(\mathcal M(\,\cdot\,)(\rho)\), which still vanishes on \(Gf_k\) if \(m>1\). Its first detectable iterate is \(G^m f_k\), using \(s\mathcal M(G^m f_k)=(-i)^m F_k^{(m)}\). It therefore uses invariance on the graph domain to reach that iterate. The higher evaluation \(L_{\rho,m-1}\) uses only \(Gf_k\) and one fixed \(k\). This proof uses the established integer-span equivalence in the RH direction and no zero-density estimate in the converse. Manzur–Noor's Theorem 5.1 gives a separate statement at every individually fixed nonzero transport time. [Earlier power argument](jump_generator63_proponent.md) · [Manzur–Noor, Theorem 5.1](https://arxiv.org/pdf/2610.03568v1)

The membership remains a closure condition. A direct length obstruction follows from the jumps: a finite floor combination \(\sum_{d\le N}c_d\lfloor x/d\rfloor\) would have jump \(\sum_{d\mid n,\ d\le N}c_d\) at \(n\). Matching \(Gf_k\) at \(n=1\) gives \(c_1=0\). At a prime \(p>\max(k,N)\) the finite floor jump would be zero, while the required jump is \(-i\log p\). This leaves open quantitative approximation by increasing finite spans.
