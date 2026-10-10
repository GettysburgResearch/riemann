# Polynomial approach to the critical SHARP power

Status: new proved combination theorem, conditional where an external zero-free line is supplied. It does not improve a zero-free line. The theorem concerns the literal native arithmetic source, not a surrogate kernel.

Exact source: [PR 911 at d93e2b2c5a5cb5fc5ad940119dff86ba96503180](https://github.com/GettysburgResearch/riemann/blob/d93e2b2c5a5cb5fc5ad940119dff86ba96503180/research/exploratory/2026-10-10-four-hour-wave/arithmetic/README.md), specifically NEGATIVE_MASS.md (A-NM1/A-NM2), ZERO_FREE_MERTENS.md (A-ZM1), and POWER_THRESHOLD.md (A-SP2). Local exact copies and blob/content hashes are in adjacent-sources/MANIFEST.json. The sextic moment-to-zero adapter is PR 912's MELLIN_AND_SPIKES.md, Corollary 3.2, at 6afd64e042ce7b59d550c3d76e9e2cca8b2c7379. No finite numerical check proves these analytic assertions.

## 1. Uniform expansion near power one

Retain the source exactly:
\[
\beta(n)=\mu(n)-\mathbf1_{67\mid n}\mu(n/67),\qquad
T(y)=(4\sqrt y-3)\mathbf1_{y\ge1},
\]
\[
H_m(x)=\sum_{n\le x}\frac{\beta(n)}{\sqrt n}T(x/n)^m,
\qquad B(a)=\frac{1-67^{-a}}{\zeta(a)}.
\]
At \(a=1\), interpret \(B(1)=0\) by its removable continuation.

**Theorem 1.** Suppose \(M(x)=O(x^b)\) for a fixed \(1/2<b<1\). Fix \(0<\delta_0<2b-1\). Uniformly for \(x\ge1\) and \(0\le\delta\le\delta_0\),
\[
\boxed{
H_{1+\delta}(x)
=4^{1+\delta}B(1+\delta/2)x^{(1+\delta)/2}
+O_{b,\delta_0,M}\bigl(x^{b-1/2}\bigr).}
\tag{1.1}
\]
The implied constant depends on the stated Mertens constant, not on \(\delta,x\).

**Proof.** The coefficient prefix \(A(t)=\sum_{n\le t}\beta(n)=M(t)-M(t/67)\) obeys \(|A(t)|\le C t^b\). Set \(m=1+\delta\), \(a=(m+1)/2\), and \(q=3/4\). Since \(a\ge1>b\), partial summation gives
\[
\sum_{n>x}\beta(n)n^{-a}=O(x^{b-a})
\tag{1.2}
\]
uniformly in the compact \(a\)-range. The boundary term is bounded by \(Cx^{b-a}\), and the tail integral by \(Ca x^{b-a}/(a-b)\); its denominator is at least \(1-b>0\). The conditionally convergent series at \(a=1\) has value \(B(1)=0\) by Abel continuation, as in A-NM2.

For \(1\le t\le x\), put
\[
f(t)=t^{-a}\left[(1-q\sqrt{t/x})^m-1\right].
\]
The bracket is \(O(\sqrt{t/x})\), and its derivative in \(t\) is \(O(x^{-1/2}t^{-1/2})\), uniformly for the stated \(m\). Therefore
\[
|f(x)|\ll x^{-a},\qquad
|f'(t)|\ll x^{-1/2}t^{-a-1/2}.
\]
Partial summation now bounds its coefficient sum by
\[
\left|\sum_{n\le x}\beta(n)f(n)\right|
\ll x^{b-a}
+x^{-1/2}\int_1^x t^{b-a-1/2}\,dt
\ll x^{b-a}.
\tag{1.3}
\]
The last constant is uniform because
\(b-a+1/2=b-m/2\ge b-(1+\delta_0)/2>0\).

Finally,
\[
H_m(x)=4^m x^{m/2}
\sum_{n\le x}\beta(n)n^{-a}(1-q\sqrt{n/x})^m.
\]
Subtract the full series \(4^m B(a)x^{m/2}\), and use (1.2)–(1.3). Since \(m/2+b-a=b-1/2\), this proves (1.1). \(\square\)

**Corollary 1.1.** Under the same hypothesis there exists a fixed \(C>0\) such that
\[
\boxed{
H_{1+\delta}(x)>0
\quad\text{for }0<\delta\le\delta_0,\quad
x\ge C\delta^{-1/(1-b)}.}
\tag{1.4}
\]
To prove this, use
\[
B(1+\delta/2)\ge
\frac{66}{67}\frac{\delta}{2+\delta}\gg_{\delta_0}\delta,
\]
which follows from \(\zeta(a)\le a/(a-1)\). In (1.1) the ratio of the positive main term to the error is bounded below by a fixed constant times
\(\delta x^{1-b+\delta/2}\ge\delta x^{1-b}\).
Taking \(C\) sufficiently large makes that ratio greater than two.

This is a uniform polynomial horizon. PR 911's unconditional elementary A-SP2 horizon has logarithm \((4/\delta)\log(1/\delta)+O(1/\delta)\). The polynomial improvement here uses the explicit additional cancellation hypothesis \(M(x)=O(x^b)\); it is not an unconditional improvement toward RH, and its constant is not certified numerically.

## 2. Conversely, a polynomial horizon pays the native critical rate

**Theorem 2.** Suppose \(A\ge2\) and there are fixed \(C,\delta_0>0\) such that
\[
H_{1+\delta}(x)\ge0
\quad(0<\delta\le\delta_0,\ x\ge C\delta^{-A}).
\tag{2.1}
\]
Then the critical detector \(F(x)=H_1(x)\) has
\[
F_-(x)\ll x^{1/2-1/A}\log^2(2x),
\qquad
N(Y):=\int_1^Y F_-(x)\frac{dx}{x}
\ll_\epsilon Y^{1/2-1/A+\epsilon}.
\tag{2.2}
\]
Consequently \(\zeta(s)\) has no zero in \(\Re s>1-1/A\).

**Proof.** For \(1\le m\le1+\delta\) and \(0<\delta\le1/\log(2x)\), finite differentiation in \(m\), \(|\beta(n)|\le2\), and \(1\le T(x/n)\le4\sqrt{x/n}\) give
\[
|\partial_mH_m(x)|
\le\sum_{n\le x}\frac{2}{\sqrt n}T(x/n)^{1+\delta}\log T(x/n)
\ll\sqrt x\log^2(2x).
\tag{2.3}
\]
Here \(T(x/n)^\delta\) is uniformly bounded, and the remaining harmonic sum is \(O(\log(2x))\). This is valid for every real \(x\), including activation points, since differentiation is in \(m\).

For sufficiently large \(x\), take \(\delta=(C/x)^{1/A}\). It meets both smallness restrictions and \(x=C\delta^{-A}\). Since \(H_{1+\delta}(x)\ge0\), the mean-value bound (2.3) gives the first inequality in (2.2). Integrating proves the second. At \(A=2\), the integral costs at most \(\log^3(2Y)\), absorbed in \(Y^\epsilon\). PR 911's exact nonnegative-transform theorem A-NM1 then excludes zeros with real part greater than \(1/2+(1/2-1/A)\). \(\square\)

## 3. Exact horizon index, and its moment consequence

Let \(\Theta_\zeta\) be the supremum of real parts of nontrivial zeta zeros. Define
\[
\mathcal A_*=\inf\{A\ge2:\ \text{there exist }C,\delta_0>0
\text{ for which }H_{1+\delta}(x)>0
\text{ whenever }0<\delta\le\delta_0,\ x\ge C\delta^{-A}\},
\]
with the infimum of the empty set equal to infinity. Then
\[
\boxed{\mathcal A_*=\frac1{1-\Theta_\zeta}.}
\tag{3.1}
\]
For the lower bound, apply Theorem 2 to each admissible \(A\). For the upper bound when \(\Theta_\zeta<1\), take any \(A>1/(1-\Theta_\zeta)\), choose \(\Theta_\zeta<b<1-1/A\) with \(b>1/2\), and use A-ZM1 with a smaller positive buffer to obtain \(M(x)=O(x^b)\). Corollary 1.1 gives an admissible exponent \(1/(1-b)<A\), hence also \(A\). If \(\Theta_\zeta=1\), Theorem 2 excludes every finite \(A\). This proves (3.1).

The infimum is restricted to \(A\ge2\) deliberately. No necessity of that lower cutoff for arbitrary positivity horizons is claimed under RH. Nor is the infimum asserted to be attained: every conversion from a zero-free line retains its positive buffer.

For the sextic moment program, a moment bound
\[
M_{2k}(D,D^h;W_*)\ll_\epsilon D^{k+h+e_k+\epsilon}
\]
for PR 912's universal test gives the zeta boundary
\[
\sigma_*=\frac12+\frac{5h}{12k}+\frac{e_k}{2k}.
\]
If \(\sigma_*<1\), it therefore gives every polynomial SHARP horizon exponent
\[
\boxed{A>\frac1{1-\sigma_*}.}
\tag{3.2}
\]
This uses only the principal \(K\)-member \(\zeta_K=\zeta L(\,\cdot\,,\chi_{-3})\); a bound for the ordinary native detector alone does not control all sextic twists.

Conditional on the inherited boundary \(139999/160000\), every \(A>160000/20001\) is admissible. The proposed fourth-moment limit \(17/24\), if proved, would give every \(A>24/7\). A cofinal moment hierarchy with boundary tending to \(1/2\) would give \(\mathcal A_*=2\). These are exact consequences and equivalent rate criteria, not new moment estimates or new zero-free regions.
