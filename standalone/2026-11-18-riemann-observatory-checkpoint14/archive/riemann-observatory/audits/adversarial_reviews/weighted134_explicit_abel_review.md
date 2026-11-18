# Independent check of the explicit Abel substitution

The real-shift coefficient 31 and the proposed complex-shift estimate hold, including the \(m=0\) boundary term. The result quantifies the prime-to-integral replacement in Gonek's Lemma 8. It does not allocate constants to the rest of the derivative-moment proof. [Prime126 calculation](prime126_explicit_abel_constant.md) · [Gonek primary PDF](../../sources/classical63_lfunctions/gonek1984.pdf)

## Primary explicit bound

I inspected rendered PDF pp. 4, 44 and 45 of Andrew Fiori and Mikko Jaskari, *Explicit bounds for the prime number theorem*, arXiv:2609.23222v2. The pinned preprint has 50 pages and SHA-256 \(\texttt{77d12f382218e5d63e1c3b6de0f96a7bb9dfe23538f1ecf0221d28d1f840c8db}\). Theorem 1.1, p. 4, takes \(x\ge x_0\ge e^3\) and lists \(L(e^3)=0.2390\) and
\[
 D=\frac52(5/3)^{1/5}(2000/161967)^{3/5}>0.198.
\]
The final inequality in its proof in §5.1, p. 45, has \(|\psi(x)-x|/x\) on the left; Theorem 5.2 on p. 44 also uses the absolute error. Thus it is legitimate to use the absolute bound at the Table value \(x_0=e^3\), independently of the quasi-RH hypothesis in Theorem 5.3. The check is of these source passages, rather than a complete audit of the 50-page preprint. The lower bound on \(D\) follows directly by taking fifth powers and comparing rationals. [Pinned Fiori–Jaskari PDF](../../sources/prime122_frontier_pending/2609.23222.pdf)

Write \(E(u)=\psi(u)-u\) and \(r(u)=|E(u)|/u\). Put \(v=\log u\). For \(v\ge3\), the correction \((\log\log v)/(15\log v)\) in Theorem 1.1 is nonnegative, and \(\log v\le\sqrt v\), as seen by minimizing \(\sqrt v-\log v\) at \(v=4\). Hence
\[
 r(e^v)\le 0.239 e^{-0.198\sqrt v}\qquad(v\ge3).
\]
For \(0\le v\le3\), \(\psi(e^v)\le e^v v\) gives \(r(e^v)\le1+v\). In particular \(r(u)\le4\) for all \(u\ge1\). Extending the nonnegative exponential integral down to zero gives the exact rational majorant
\[
 \int_1^\infty r(u)\frac{du}{u}
 \le \frac{15}{2}+\frac{0.478}{0.198^2}
 =\frac{386015}{19602}<20.
\]

## Complex Abel estimate

Let \(x>1\), \(L=\log x\), \(m\ge0\) an integer, and \(\delta\in\mathbb C\). The powers for positive arguments use the real log. Define
\[
 A_m=\sum_{n\le x}\Lambda(n)n^{i\delta-1}(\log(x/n))^m
         -\int_1^x u^{i\delta-1}(\log(x/u))^m\,du .
\]
The zeroth log power equals one, including at \(u=x\). With \(f_x(u)=u^{i\delta-1}(\log(x/u))^m\) and \(K=|\Im\delta|\log x\), the right-continuous Stieltjes integration over \((1,x]\) gives
\[
 A_m=E(x)f_x(x)-E(1)f_x(1)-\int_1^x E(u)f_x'(u)\,du .
\]
It includes a possible prime-power jump exactly at \(x\). There is no contribution from \(\Lambda(1)\). The lower term is \(L^m\) since \(E(1)=-1\). The upper term vanishes for \(m>0\) and is bounded by \(4e^K\) for \(m=0\).

On the finite interval \(1\le u\le x\), \(|u^{i\delta}|=u^{-\Im\delta}\le e^K\) and
\[
 |f_x'(u)|\le e^K u^{-2}
  \left(|i\delta-1|(\log(x/u))^m+
               m(\log(x/u))^{m-1}\right),
\]
where the second term is absent at \(m=0\). Replace the nonnegative log powers by \(L^m,L^{m-1}\), respectively. Only after bounding \(u^{-\Im\delta}\) on the finite interval may the integral of \(r(u)/u\) be extended to infinity. This gives
\[
 |A_m|\le L^m+4e^K{\bf 1}_{m=0}
       +20e^K|i\delta-1|L^m+20me^K L^{m-1},
\]
with the last term omitted at \(m=0\). The asserted common bound
\[
 |A_m|\le [1+e^K(4+20|i\delta-1|)]L^m
                 +20me^K L^{m-1}
\]
follows, and \(K\) can even be taken as \(\max(0,-\Im\delta)\log x\). The finite-\(x\) order of these estimates matters. Extending an integrand containing \(u^{-\Im\delta}\) to infinity would not yield this conclusion for a negative imaginary shift. The formula becomes uniform on any fixed microscopic disk \(|\delta|\log x\le C\) as \(x\to\infty\), since \(K\le C\) and \(|i\delta-1|\le1+|\delta|\).

For \(m\ge1\), the exponent \(m-1\) is nonnegative, so there is no singularity as \(x\downarrow1\). In fact \(A_m\) is the negative of the integral for \(1<x<2\), and that integral is \(O(e^K L^{m+1})\) directly. At \(x=1\) both original terms vanish under the stated log conventions. The estimate does not assign any meaning to \(0\cdot L^{-1}\) at \(m=0\), since that term has been dropped.

For real \(|\delta|\le1/2\), \(K=0\) and \(|i\delta-1|\le\sqrt5/2\). The common coefficient \(1+4+20\sqrt5/2=5+10\sqrt5<31\), giving the claimed \(31L^m+20m L^{m-1}\) with the same zeroth-order convention. In Gonek's application the prime integral has \(m=\mu+\kappa+1\), so the optional \(m=0\) endpoint is only a generalization of the Abel estimate. No numerical full derivative-tail bound, new bound on its normalized constant, or canonical change follows from this check.
