# Match three complete tail moments with a Gaussian and two real pairs

Status: proposed conditional analytic mechanism, pending independent review.
Scope: an actual complete paired tail, a complete simple real finite product,
and explicitly source-bound parameters. The construction matches the native
logarithmic coefficients through degree six and retains the full residual.
No native slab or full-parameter-family certificate is claimed here.
Exact dependencies: the complete source in THEOREM.md, the protected companion
error predicate in FINITE_CENSUS_COMPLEMENT.md, and
[MOMENT_NORM_TRANSPORT.md](MOMENT_NORM_TRANSPORT.md).
What was actually run: a separate exploratory directed probe refined 111 low
root brackets to width `2^-80`, replayed their 222 actual Hardy-Z endpoint
signs, and evaluated the native degree-six Gamma/zeta logarithmic jet. Its
existing remaining census intervals retain their imported complete-count
scope. It found a feasible candidate `K=6905`; this is not a native slab
certificate or an independently reviewed primitive packet.
Smallest remaining gap: independently bind the refined prefix and all native
moment intervals, then cover the complete parameter family in a new protected
finite-domain certificate.

## 1. Source moments and the exact two-pair feasibility interval

Let `P_R(0)=1` be the normalized product of the complete simple real census,
let `p_R` be the complete
remaining paired product, and `Xi=Xi(0)*P_R*p_R`. Set

\[
a_1=t_1,\quad t_2=\sum_{\operatorname{Re}\rho>R}m_\rho\rho^{-4},
\quad t_3=\sum_{\operatorname{Re}\rho>R}m_\rho\rho^{-6}.
\tag{SA1}
\]

Assume `R>6A`; these are real positive moments by (MN2)--(MN4).
Choose a fixed positive integer `K` satisfying

\[
\frac{t_2^3}{2t_3^2}<K<\frac{t_2^3}{t_3^2},\qquad
 a_1>\sqrt{2Kt_2}.
\tag{SA2}
\]

These are source-bound hypotheses, not consequences of positivity alone.
There are unique unordered distinct positive numbers `u,v` such that

\[
K(u^2+v^2)=t_2,\qquad K(u^3+v^3)=t_3.
\tag{SA3}
\]

To prove this, put `s_2=t_2/K`, `s_3=t_3/K`, and `p=u+v`.
The required product is `(p^2-s_2)/2`, while the cubic sum is
`(3s_2p-p^3)/2`. On `sqrt(s_2)<p<sqrt(2s_2)`, this latter function is
strictly decreasing from `s_2^(3/2)` to `s_2^(3/2)/sqrt(2)`.
Condition (SA2) places `s_3` strictly between those endpoints. The unique
`p` therefore gives positive distinct roots of
`X^2-pX+(p^2-s_2)/2=0`, proving (SA3). Moreover

\[
p<\sqrt{2t_2/K},\quad \max(u,v)<\sqrt{t_2/K},\quad
K(u^4+v^4)\le t_2^2/K.
\tag{SA4}
\]

The last bound uses `u^4+v^4<=(u^2+v^2)^2`.

## 2. Source-faithful auxiliary base and exact cancellation

Define

\[
a=a_1-K(u+v)>0,\qquad
G(z)=\Xi(0)e^{-az^2}P_R(z)(1-uz^2)^K(1-vz^2)^K.
\tag{SA5}
\]

The Gaussian guard in (SA2) and (SA4) prove `a>0`. This is an auxiliary
Laguerre--Polya base with real zeros; no inverse-Fourier positivity assertion
is made. Its artificial real roots are `+/-u^(-1/2)` and `+/-v^(-1/2)`,
each of multiplicity `K`.

For a protected disk `|z|<=B` require

\[
B<R,\qquad B^2\max(u,v)<1.
\tag{SA6}
\]

Put `q=Xi/G`, choosing the analytic logarithm `h=log q` with `h(0)=0`.
The complete source gives

\[
\log p_R(z)=-a_1z^2-t_2z^4/2-t_3z^6/3-\cdots.
\tag{SA7}
\]

By (SA3)--(SA5), `a+K(u+v)=a_1`, `K(u^2+v^2)=t_2`, and
`K(u^3+v^3)=t_3`. Thus `h` starts at degree eight. This cancels exactly
three native complete moments; the tail after them is never omitted.

## 3. Complete residual bounds

Choose any complete bound `U_8>=sum_tail m/|rho|^8`. Two legitimate examples
are the coarse-count bound `S_2/R^6`, or the stronger native moment bound

\[
U_8=\frac{(t_3)_{\rm upper}}{c_3R^2}
\tag{SA8}
\]

from (MN5). Set `d=B^2/R^2`, `w=B^2 max(u,v)`, `V_4=K(u^4+v^4)`.
Exact differentiation of the full log residual gives

\[
h'(z)=-2z^7\sum_{\rm tail}
\frac{m_\rho}{\rho^6(\rho^2-z^2)}
+2Kz^7\left(\frac{u^4}{1-uz^2}+\frac{v^4}{1-vz^2}\right).
\tag{SA9}
\]

Consequently on the entire protected disk,

\[
\begin{aligned}
|h'|&\le J_1=2B^7\left(\frac{U_8}{1-d}+\frac{V_4}{1-w}\right),\\
|h''|&\le J_2=2B^6\left(
U_8\frac{7-5d}{(1-d)^2}
+V_4\frac{7-5w}{(1-w)^2}\right),\\
|q'/q|&\le J_1,\qquad |q''/q|\le J_1^2+J_2.
\end{aligned}
\tag{SA10}
\]

For the second bound differentiate each exact summand in (SA9) and use
`7/(1-x)+2x/(1-x)^2=(7-5x)/(1-x)^2`. This function is increasing for
`0<=x<1`, since its derivative is `(9-5x)/(1-x)^3>0`, permitting the
common `d,w` bounds. The complete unknown source and both artificial-pair
residuals are included. Whole interval upper endpoints can replace `t_3`,
`V_4` and `w`; by (SA4), `V_4<=t_2_upper^2/K`.

## 4. Protected companion transfer remains a full-family requirement

At order zero, `G` has no lower nonreal zeros. Its Gaussian polynomial
approximants and logarithmic derivative therefore give the strict lower
companion sector as in GAUSSIAN_TAIL_TRANSPORT.md. On the real protected
interval all original census roots are simple, and the artificial multiple
roots are excluded by (SA6). Thus the strict real Laguerre inequality also
holds there. In a joint compact source-bound parameter family satisfying all
strict guards, the base companion and its derivative have positive protected
margins by continuity and compactness.

Suppose a finite checker really covers that complete parameter family and
all target boxes, giving `Re W_G>=a_0>0`, `|W_G|<=M`, and `tau=a_0/M`.
The full multiplier predicate is still

\[
\alpha=\lambda J_1,\quad
\beta=M[2J_1+\lambda(J_1^2+J_2)],\quad
\beta<1,\quad\alpha+(1+\tau)\beta<\tau.
\tag{SA11}
\]

It then protects both actual companion denominators and gives the strict
actual sector using (C14)--(C17). A feasible `K`, a positive native jet or
a selected parameter point alone does not verify this predicate everywhere.
The new analytic mechanism remains separate from the accepted finite column
and from every earlier frozen Gaussian or quartic certificate.
