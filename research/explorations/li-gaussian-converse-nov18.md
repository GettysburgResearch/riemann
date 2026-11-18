# An extremal zero forces both signs of Li's coefficients on a logarithmic scale

**Proposed theorem.** Suppose RH is false. Set \(z_\rho=1-1/\rho\), \(a=\max_\rho\log|z_\rho|>0\), and \(L=\log(2/a)\). For every integer \(N\ge1\), each sign occurs strictly among the classical Li coefficients with indices in
\[
 [N,\ N+C (L/a)\{1+\log(2+aN/L)\}].
 \tag{1}
\]
In particular the first negative index is at most \(C a^{-1}\log(2/a)\). Conversely, nonnegativity of the first \(M\) coefficients implies for every nontrivial zero
\[
 |\Re\rho-1/2|\ \ll\ (1+|\Im\rho|^2)\frac{\log(2M)}M .
 \tag{2}
\]
Constants are absolute and unevaluated. This improves the logarithm in [the earlier angular-filter converse](li-angular-converse-nov18.md). The proof imports the classical local zero count and the Kolesnik–Straus consecutive-power inequality. Its finite predicate concerns all initial indices. See the earlier note for comparisons with results of Brown and Palojärvi.

## Angular isolation with a discrete Gaussian

Write \(u_\rho=a-\log|z_\rho|\in[0,2a]\), \(\theta_\rho=\arg z_\rho\). Choose an extremal zero with positive ordinate and angle \(\theta_*\). By the squared-modulus identities and the arctangent estimate in the earlier note, for \(\gamma>0\)
\[
 |\log|z_\rho||\le(2\gamma^2)^{-1},\qquad
 \theta_\rho=1/\gamma+O(\gamma^{-3}),\qquad
 1/\theta_\rho=\gamma+O(1/\gamma).
\]
Reflection ensures that \(a\) is attained. Since \(|\gamma|\ge14\), we always have \(a<1/300\). At the target \(\theta_*\gg\sqrt a\) and, more precisely, \(\theta_*\ge 0.99\sqrt{2a}\) by \(x-x^3/3\le\arctan x\le x\). The zeros within angular distance \(a\) of \(\theta_*\) therefore have positive ordinates in an interval of bounded length and ordinates \(\ll a^{-1/2}\). Indeed taking reciprocals spreads their angles by at most \(2a/(\theta_*-a)^2=O(1)\). By the unit-interval zero count their number \(m\), counting multiplicity, satisfies \(1\le m\le C_1 L\). All angles here have absolute value less than \(1/10\), so there is no ambiguity at the principal cut.

Put \(S=L\{1+\log(2+aN/L)\}\), \(W=A S/a\), where \(A\) is a sufficiently large fixed constant specified by successive inequalities below. Let \(t_0=N+2W\). For \(t\in[t_0,t_0+2W]\) use variance
\[
 v=\eta Wt/(a t_0),\qquad \eta=1/100.
\]
Thus \(\eta W/a\le v\le 2\eta W/a\) and \(v/t\le \eta/a\). The discrete weights are \(g_t(n)=(2\pi v)^{-1/2}\exp(-(n-t)^2/(2v))\). Poisson summation gives exactly
\[
 \sum_{n\in\mathbb Z} g_t(n)e^{-un+i\vartheta n}
 =\sum_{j\in\mathbb Z}\exp\{t b_j+v b_j^2/2\},
 \qquad b_j=-u+i(\vartheta-2\pi j).
 \tag{3}
\]
For \(0\le u\le2a\), the modulus of a summand is at most
\(\exp(-(1-\eta)tu-v(\vartheta-2\pi j)^2/2)\).
All nonprincipal aliases for our angles have total modulus \(O(e^{-v})\).

For each of the \(m\) angular neighbors put \(b=-u_\rho+i(\theta_\rho-\theta_*)\). Let \(h=W/m\), \(M_0=\lceil t_0/h\rceil\), and apply Kolesnik–Straus to the numbers
\[
 \zeta_j=\exp\{h(b+\eta W b^2/(2at_0))\}.
\]
They have modulus at most one and one value is exactly one. For some \(M_0<k\le M_0+m\) and \(t=kh\in[t_0,t_0+2W]\) we get
\[
 \left|\sum_{\rm neighbors}e^{tb+vb^2/2}\right|
 \ge 1.007\left(\frac{m}{4e(M_0+m)}\right)^m
 \ge e^{-B S}.
 \tag{4}
\]
Here \(B\) is absolute and independent of \(A\ge1\), since \((M_0+m)/m\le 5+N/W\) and \(m\ll L\). Repeated zeros and coincident phases are allowed. [Thorner–Zaman, Theorem 5.2](https://arxiv.org/pdf/1604.01750)

## Truncation and comparison of the two means

Fix \(P\) sufficiently large compared with \(B\) and set \(Y=e^{P S}\). We can take \(Y\) to exceed all target neighbors. For every integer \(n\) use the real finite sum \(l_n=\sum_{|\gamma|\le Y}(1-z_\rho^n)\), real by conjugation. There are \(\ll Y\log Y\) terms. For the \(t\) selected in (4) consider the modulated sum \(\sum g_t(n)e^{-an-in\theta_*} l_n\) over all integers. Its modulus is at least
\[
 e^{-BS}-O\!\left(Y\log Y\,[e^{-(1-\eta)at}+e^{-v a^2/2}+e^{-v}]\right).
 \tag{5}
\]
Indeed the constant subtraction uses \(u=a\) in (3). The principal terms for the \(m\) neighbors give (4), and every other angle is at distance at least \(a\) from the target. In the **unmodulated** sum the absolute value is at most
\[
 O\!\left(Y\log Y\,[e^{-(1-\eta)at/2}+e^{-v a^2/2}+e^{-v}]\right).
 \tag{6}
\]
If \(|\gamma|>a^{-1/2}\) then \(u_\rho\ge a/2\). At the remaining ordinates \(|\theta_\rho|\ge0.99\sqrt a>a\). This accounts for all principal terms. Taking \(A\) large in terms of \(P,B\) makes both error budgets less than \(e^{-BS}/20\).

Restrict both means to \(I=[N,N+6W]\). Outside \(I\) the distance to the Gaussian center is at least \(2W\). For \(n\ge0\), \(e^{-an}|l_n|\ll Y\log Y\). For \(n<0\) use \(e^{-an}|l_n|\ll Y\log Y\,e^{-2an}\): completing the square translates the center to \(t-2av\ge t-4\eta W\) and multiplies the Gaussian by \(e^{-2at+2a^2v}\le1\). The discrete Gaussian tail, bounded by its endpoint term and Gaussian integral, therefore costs \(O(Y\log Y\,e^{-cW^2/v})\) in either mean. Increasing \(A\) again makes it less than \(e^{-BS}/20\).

Finally, for \(n\in I\) the omitted Li tail obeys
\[
 |\lambda_n-l_n|\ll(n+n^2)e^{n/(2Y^2)}\log(2Y)/Y.
\]
Pair conjugate zeros, apply \(|1-r^n|\le n|\log r|e^{n|\log r|}\), \(1-\cos(n\theta)\le n^2\theta^2/2\), and sum \(\sum_{|\gamma|>Y}\gamma^{-2}\ll\log(2Y)/Y\). For clarity about constants, take \(P\) large first, then \(A\) a sufficiently large fixed multiple of \(P+B+1\); each exponential suppression in (5), (6) and the Gaussian tail is at least \(cAS\). We have \(\log(N+6W)\le C S+\log(1+A)\) with an absolute \(C\), by the definition of \(S\). Thus \(P\) can be chosen so this last approximation costs less than \(e^{-BS}/20\) in either mean for all allowed \(a,N\): the extra \(O(\log(1+A))=O(\log(2+P+B))\) is absorbed by \(PS\). The normalized Gaussian masses are bounded by 2, as follows also from (3) at \(u=\vartheta=0\).

The modulated mean of \(e^{-an}\lambda_n\) on \(I\) consequently has modulus larger than the absolute value of its unmodulated mean. A real one-signed sequence with nonnegative weights cannot satisfy that strict inequality. Both signs occur, giving (1). At \(N=1\) this implies \(M\ll a^{-1}\log(2/a)\) if the first \(M\) coefficients are nonnegative. For \(a\le1/M\) the estimate (2) is immediate, and otherwise \(\log(2/a)\le\log(2M)\). The squared-modulus identity also gives \(|\beta-1/2|\le (1+\gamma^2)a\) by reflection and \(\log(1+x)\ge x/(1+x)\). This proves (2).

## Matching lower bound for the first negative index

Let \(n_-\) be the first index with \(\lambda_{n_-}<0\). If RH fails then
\[
  n_-\asymp a^{-1}\log(2/a).
\]
More precisely, for sufficiently small \(a\), all positive indices through
\[
 M=a^{-1}\{L/2+\log L-C_2\}
\]
have strictly positive coefficients, with an absolute \(C_2\). This implication needs only the maximal radial displacement \(a\).

Indeed set \(H=(2a)^{-1/2}\). Reflection pairs the opposite logarithmic radii at each positive ordinate with the same angle. The difference between \(\lambda_n\) and the nonnegative phase sum \(P_n=2\sum_{\gamma>0}(1-\cos(n\theta_\rho))\) therefore has magnitude at most
\[
 2\sum_{\gamma>0}\big[\cosh(n\min(a,(2\gamma^2)^{-1}))-1\big]
 \ll H\log(2H)\,(\cosh(na)-1).
\]
Up to \(H\) use the zero count. Above \(H\) use \(\cosh(bx)-1\le x^2(\cosh b-1)\) for \(0\le x\le1\), with \(x=H^2/\gamma^2\), and sum the fourth-power tail dyadically. On the other hand \(P_n\gg n\log(2n)\) for all \(n\ge1\): for \(\gamma>2n+100\) the individual terms are \(\gg n^2/\gamma^2\), and the classical counting asymptotic gives \(\sum_{\gamma>x}\gamma^{-2}\gg\log x/x\) for \(x\ge100\).

For \(n\le H\), the loss divided by \(n\log(2n)\) is \(O(H^2 L a^2)=o(1)\). For \(H<n\le M\), use \(\log(2n)\gg L\) and monotonicity of \((\cosh(na)-1)/n\) to bound the ratio by \(O(H e^{aM}/M)=O(e^{-C_2})\), uniformly as \(a\downarrow0\). Choose \(C_2\) large enough for strict positivity. Absolute comparability of \(n_-\) on the remaining bounded range of \(a^{-1}\) follows from \(n_-\ge1\) and (1).
