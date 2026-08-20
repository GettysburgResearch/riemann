# L-101103 — Bad-set sparsity and derivative energy form a genuine conjunctive gate

Claim ID: `L-101103`  
Status: **PROVED DETERMINISTIC COAREA/POINCARÉ THEOREM**  
Created: 2026-08-20  
RH status: **not assumed**

Let \(F:[1,\infty)\to\mathbb R\) be continuous and locally absolutely
continuous in logarithmic coordinate.  Put
\[
 f(u)=F(e^u).
\]
Let \(\mathcal C(Y)\) be the connected components \(I=(a_I,b_I)\) of
\[
 \{u\in[0,\log Y]: f(u)<0\}
\]
whose two endpoints lie in \([0,\log Y]\), and put
\[
 \ell_I=b_I-a_I.
\]
Define
\[
 \mathfrak L_F(Y)=\sum_{I\in\mathcal C(Y)}\ell_I,    \tag{L-101103.1}
\]
\[
 \mathfrak V_F(Y)=
 \sum_{I\in\mathcal C(Y)}
 \int_I|f'(u)|^2du,                                 \tag{L-101103.2}
\]
and let \(\mathfrak B_F(Y)\) be the negative mass in a possible terminal
component meeting \(u=\log Y\).

On every compact negative component, \(f\) vanishes at both endpoints.
The one-dimensional Poincaré inequality and Cauchy--Schwarz give
\[
 \int_I(-f(u))\,du
 \le
 {\ell_I^{3/2}\over\pi}
 \left(\int_I|f'(u)|^2du\right)^{1/2}.              \tag{L-101103.3}
\]
Summing and using \(\sum_I\ell_I^3\le(\sum_I\ell_I)^3\) yields
\[
 \boxed{
 \int_1^Y(F(X))_-{dX\over X}
 \le
 {1\over\pi}
 \mathfrak L_F(Y)^{3/2}
 \mathfrak V_F(Y)^{1/2}
 +\mathfrak B_F(Y).
 }                                                   \tag{L-101103.4}
\]

Consequently the two statements
\[
 \mathfrak L_F(Y)=Y^{o(1)},                         \tag{L-101103.5}
\]
\[
 \mathfrak V_F(Y)+\mathfrak B_F(Y)=Y^{o(1)}         \tag{L-101103.6}
\]
imply subpower logarithmic negative mass.  Neither statement alone implies
that conclusion for a general function.

For the activation-zero envelope of PR #687,
\[
 \mathcal E_-(X)=4X\int_X^\infty L_-(t){dt\over t^2},
\]
and therefore
\[
 {d\over du}\mathcal E_-(e^u)
 =
 \mathcal E_-(e^u)-4L_-(e^u).                       \tag{L-101103.7}
\]
Thus the derivative-energy premise is a literal source-faithful critical
scalar estimate.  The activation/cell machinery naturally supplies
\(\mathfrak L\); the phase, wavelet, largest-prime, and Vaughan machinery
naturally attacks \(\mathfrak V\).  Equation (L-101103.4) is the exact
cross-class AND-gate between them.
