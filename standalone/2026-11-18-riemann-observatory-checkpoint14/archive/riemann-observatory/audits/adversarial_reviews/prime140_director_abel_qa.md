# Independent check of the Round 15 explicit Abel review

18 November 2026. The source scope, exact numerical fraction, and uniform Abel bounds in the director note check out. The argument supplies the prime-to-integral constant in Gonek's Lemma 8. Its other numerical constants are separate. [Director review](director_explicit_abel_round15.md) · [Original real-shift proof](prime126_explicit_abel_constant.md) · [Independent complex-shift proof](weighted134_explicit_abel_review.md)

## Primary source and numerical majorant

I rechecked the pinned version of Fiori–Jaskari, arXiv:2609.23222v2, pp. 4, 44–45, SHA-256 77d12f382218e5d63e1c3b6de0f96a7bb9dfe23538f1ecf0221d28d1f840c8db. Theorem 1.1, p. 4, takes \(x\ge x_0\ge e^3\); its table supplies \(L(e^3)=0.2390\). The displayed \(E_\psi\) in the introduction is signed. Theorem 5.2 on p. 44 and the last display of the proof in §5.1 on p. 45 explicitly bound the absolute error. Theorem 5.2 by itself is only a large-\(x\) component; the proof of Theorem 1.1 joins it to estimates for lower \(x\). The conditional half-plane transfer in Theorems 1.4 and 5.3 is not used. I checked those source passages and did not replay the preprint's interval optimization. [Pinned Fiori–Jaskari PDF](../../sources/prime122_frontier_pending/2609.23222.pdf)

If \(r(u)=|\psi(u)-u|/u\), write \(v=\log u\). The exponent constant \(D=\tfrac52(5/3)^{1/5}(2000/161967)^{3/5}\) satisfies
\[
 D^5=\frac{3906250000000}{12746791119654189}>(198/1000)^5.
\]
The correction \(1+\log\log v/(15\log v)\) is at least 1 for \(v\ge3\). The minimum of \(\sqrt v-\log v\) is positive at \(v=4\), so \((\log v)^{-1/5}\ge v^{-1/10}\) there. The PNT upper bound is then \(r(e^v)\le0.239e^{-0.198\sqrt v}\). For \(0\le v\le3\), the elementary bound \(r(e^v)\le1+v\) follows from \(\psi(u)\le u\log u\). Hence \(r\le4\) throughout and, on extending the positive tail majorant to \(v=0\),
\[
 \int_1^\infty r(u)\frac{du}{u}
 \le \frac{15}{2}+\frac{0.478}{(0.198)^2}
 =\frac{386015}{19602}<20 .
\]
Both rational comparisons were independently evaluated in exact fractions.

## Complex shifts and all endpoints

Let \(x>1\), \(L=\log x\), \(m\) a nonnegative integer and \(f_x(u)=u^{i\delta-1}\log^m(x/u)\). With \(E(u)=\psi(u)-u\), the right-continuous Stieltjes convention on \((1,x]\) gives the exact identity for the substitution error
\[
 A_m=E(x)f_x(x)-E(1)f_x(1)-\int_1^x E(u)f_x'(u)\,du .
\]
This includes a prime-power jump at the upper endpoint. The lower term costs \(L^m\) since \(E(1)=-1\). The upper term is zero for \(m>0\), or bounded by \(4e^K\) for \(m=0\), where \(K=|\Im\delta|L\). The sharper \(K=\max(0,-\Im\delta)L\) also works.

The derivative bound uses \(|u^{i\delta}|=u^{-\Im\delta}\le e^K\) first, on the finite interval. After replacing the log powers by \(L^m,L^{m-1}\), the remaining nonnegative integral is at most the \(r(u)/u\) integral less than 20. This order avoids an invalid extension of a factor \(u^{-\Im\delta}\) through infinity. It gives
\[
 |A_m|
 \le L^m+4e^K\mathbf1_{m=0}
    +20e^K|i\delta-1|L^m+20me^K L^{m-1},
\]
where the last term is omitted for \(m=0\). For real \(|\delta|\le1/2\) the common coefficient is bounded by \(5+10\sqrt5<31\). For \(1<x<2\) the discrete sum is zero and the absolute integral is at most \(e^K L^{m+1}/(m+1)\), giving the direct \(x\downarrow1\) check, even on a fixed microscopic disk where \(K\) is bounded. At \(x=1\) both original terms are zero under the zeroth-power convention. There is no negative power to interpret for \(m=0\). The result matches the real shift range in Gonek and extends the isolated substitution to complex shifts; it does not extend Gonek's other steps to complex shifts by itself.

## Next constant in Gonek's Lemma 8

The next explicit allocation is the coefficient in Gonek's Lemma 7, equation (40), journal pp. 133–134 (PDF pp. 11–12), for \((\mu,\kappa)=(1,1)\). This is the divisor-convolution error multiplying \(x\sum_{d\le x}\Lambda(d)d^{-1}\log^2(x/d)\) when Lemma 8 inserts Lemma 7 before equation (36), journal pp. 134–135 (PDF pp. 12–13). Set
\[
 A_{11}(z)=\sum_{d r\le z}\log d\,\log r,\qquad
 C_{11}=\sup_{z>1}\frac{|A_{11}(z)-z(\log z)^3/6|}{z(\log z)^2}.
\]
The source gives finiteness without a value. A direct calculation plan is to estimate the inner \(\sum_{r\le z/d}\log r\) by its integral scale with a uniform floor error, then compare the remaining log kernel to its integral by total variation, keeping the right-continuous endpoint. The companion note completes this allocation and gives \(C_{11}\le5/2\), with the exact endpoint treatment. It controls the specified pair of indices and does not allocate the contour or final tail constants. [Gonek journal PDF](../../sources/classical63_lfunctions/gonek1984.pdf) · [Explicit convolution calculation](prime142_gonek_convolution_constant.md)
