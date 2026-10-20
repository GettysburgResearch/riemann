# A hybrid row and angular mean with sharper smooth sectors

20 October 2026. **Proposed source-dependent unconditional theorem.**
This retains all three original-side terms in the proved angular
absorption mechanism. It strengthens the coarse angular dependence
of ANGULAR_UNIFORMITY.md without changing that frozen proof.
It gives no numerical zero-free improvement and no prime-sector
asymptotic.
The strongest balanced smooth-sector consequence below has width
exponent \((\sqrt{73}-1)/48\), proved in Section 4.

Inputs:

* ANGULAR_UNIFORMITY.md, SHA256
  9735a9cf2a7c75495a86da9c80ff9ddb7e2efb1e19bb6acad226aaec00b99385,
  especially its uniform gamma quotient, initial growth argument,
  and exact original-side inequality (U11);
* ../average/ANGULAR_SELF_ABSORPTION.md, SHA256
  0c195c93ef2548a81197e21d0eca58f1632f25e9339d0f078fa185f8605d59e8,
  and its audited eight-component finite Mellin family.

## 1. The sharper mean

Use that exact completed cubic family with both angular signs,
primary squarefree rows, and all natural common-prime zeros.
Let \(\ell\ne0\), \(L=1+|\ell|+|t|\), and fix
\(0<\delta<1/6\). Define
\[
 F_\delta(R,L)=
 R+R^{1/2-\delta}L^{2-4\delta}
                 +R^{1-\delta}L^{4/3-4\delta}.
\tag{H1}
\]
Then, for every \(\epsilon>0\),
\[
 \boxed{\displaystyle
 \sum_{Nr\le R}^{*}
  \|\mathbf Q_r^{[\ell]}(1/2+\delta+it)\|^2
 \ll_{\delta,\epsilon}
                  (RL)^\epsilon F_\delta(R,L).}
\tag{H2}
\]
The constant is independent of \(R,\ell,t\).
The field and finite profiles are fixed.
This is stronger than replacing the right side by
\(R^{1+\epsilon}L^{2-4\delta+\epsilon}\).

For completeness, the absorption needs a different normalization,
so it is checked explicitly. Fix finite row and angular cutoffs.
Normalize the mean by \((RL)^{\epsilon_0}F_\delta(R,L)\) and
take the supremum over those cutoffs and all heights.
It is finite before absorption: the preliminary uniform bound
(U9), squared, has height degree \(2-4\delta+4\eta\).
For each fixed finite row range the second term in (H1) controls
that height degree when \(4\eta<\epsilon_0\).
The preliminary conductor factor is merely a finite constant
at this stage. No uniform desired conclusion is assumed.

All three \(R\)-powers in (H1) exceed \(2\delta\):
\[
          1>2\delta,\quad 1/2-\delta>2\delta,\quad
                                      1-\delta>2\delta.
\]
The middle inequality is the reason for the stated range.
Partial summation in the exact reflected inequality (U7) gives
\[
 \sum_{Nk\le R}(Nk)^{-2\delta}
       \|\mathbf Q_k^{[\ell]}(1/2+\delta-it)\|^2
 \ll M(RL)^{\epsilon_0}R^{-2\delta}F_\delta(R,L),
\tag{H3}
\]
where \(M\) denotes the finite supremum.
After the Gaussian contour shift, the coefficient of this same
supremum, relative to the normalization, is at most
\[
          C\,Y^{-4\delta}R^{2\delta+\eta}L^{8\delta}.
\tag{H4}
\]
The height convolution is uniform: each positive \(L\)-power
in (H1) changes by at most a fixed power of \(1+|v|\) under
\(t\mapsto t+v\), and the Gaussian integrates that power.

Choose
\[
                  Y=C_0R^{1/2+\theta}L^2,
                 \qquad \theta>0.
\tag{H5}
\]
Take the divisor/sieve losses below \(4\delta\theta\).
Then (H4) is \(C C_0^{-4\delta}R^{-4\delta\theta+\eta}\).
A fixed large \(C_0\) makes it contract for every \(R\ge1\).
The original-side estimate (U11) becomes, before small losses,
\[
 R+
 R^{1/2-\delta+\theta(1-2\delta)}L^{2-4\delta}
 +R^{1-\delta+\theta(2/3-2\delta)}L^{4/3-4\delta}.
\tag{H6}
\]
Choose \(\theta\) inside the final row loss, then all sieve
losses inside the remaining row and angular allowances.
Thus (H6) is bounded by a constant times the chosen normalization.
The finite supremum satisfies \(M\le C+M/2\).
Reflection only decreases the row and reverses an included
angular sign, so both cutoffs close.
Letting them increase proves (H2).

## 2. Free-column and smooth-sector consumers

Use exactly the Type-I form \(T_\ell(A,B)\) from (S6) of
CONDITIONAL_ANGULAR_SECTORS.md: fixed smooth radial weights,
arbitrary \(|b_v|\le1\), and an unrestricted smooth inner
variable \(u\). There is no moving quadratic conductor.
The inverse ordinary Hecke factor in the cube completion is
absolutely bounded on \(\Re s=1/2+\delta\), uniformly in
angular order. Mellin inversion and Cauchy over \(v\) give
\[
 |T_\ell(A,B)|\ll (AB(1+|\ell|))^\epsilon A^{1/2+\delta}
 \left\{
 B+B^{3/4-\delta/2}(1+|\ell|)^{1-2\delta}
  +B^{1-\delta/2}(1+|\ell|)^{2/3-2\delta}
 \right\}.
\tag{H7}
\]
Only a fixed number of radial derivatives is required.
Choose \(\delta\) inside the final \(AB\)-loss, with constants
allowed to depend on that loss. It follows that
\[
 \boxed{\displaystyle
 |T_\ell(A,B)|\ll_\epsilon
  (AB(1+|\ell|))^\epsilon A^{1/2}
  \{B+B^{3/4}(1+|\ell|)
                      +B(1+|\ell|)^{2/3}\}.}
\tag{H8}
\]

Let \(\phi_{\Delta,\theta_0}\) be the same periodized fixed
smooth bump as in the sector note, with \(0<\Delta\le1\).
Keep the same \(b_v\) in every Fourier mode.
Its nonzero Fourier coefficients have weighted sums
\(O(\Delta^{-q-\epsilon})\) for weight \((1+|k|)^{q+\epsilon}\).
The exact zero coefficient is \(\Delta\int\phi\).
Consequently
\[
 \boxed{\displaystyle
 \left|T_{\phi_{\Delta,\theta_0}}
          -\Delta\!\left(\int\phi\right)T_0\right|
 \ll_{\epsilon,W,\phi}(AB)^\epsilon A^{1/2}
       \{B^{3/4}\Delta^{-1-\epsilon}
                   +B\Delta^{-2/3-\epsilon}\}.}
\tag{H9}
\]
The constant \(B\)-term from (H8) is absorbed by the second
displayed term for \(\Delta\le1\).
The zero-angular mode is retained exactly; no spherical residue
is assumed to vanish.

Write \(A=X^a\), \(B=X^{1-a}\), \(0\le a\le1\).
Comparing each term of (H9) with the natural absolute scale
\(X\Delta\) gives the width exponent
\[
 \boxed{\displaystyle
       \xi_{\rm hyb}(a)=
                \min\left\{\frac{1+a}{8},\frac{3a}{10}\right\}.}
\tag{H10}
\]
For fixed \(a>0\) and \(0<\eta<\xi_{\rm hyb}(a)\), take
all error allowances sufficiently small.
At every width \(\Delta\ge X^{-\xi_{\rm hyb}(a)+\eta}\),
(H9) is smaller than \(X\Delta\) by a fixed power of \(X\).
The two expressions in (H10) meet at \(a=5/7\).
At balance \(a=1/2\), this gives
\[
                     \xi_{\rm hyb}(1/2)=3/20,
\tag{H11}
\]
improving the earlier coarse \(1/8\).
It strictly improves the previous exponent \(a/4\) for
\(0<a<1\), agrees at \(a=1\), and gives no positive shrinking
width exponent at \(a=0\).

## 3. Comparison with the earlier conditional consumer

The separately proved conditional exponent
\[
 \xi_\beta(a)=
       \frac{(7-4\beta)a-2(1-\beta)}{4(4-\beta)}
\]
remains valid under its actual common-family premise.
Its earlier comparison with \(a/4\) should not be read as a
comparison with the new (H10).
For \(1/2\le\beta<1\), direct algebra shows that
\(\xi_\beta(a)<\xi_{\rm hyb}(a)\) throughout \(0<a\le5/7\).
For \(5/7\le a\le1\),
\[
 \xi_\beta(a)-\xi_{\rm hyb}(a)
   =\frac{(10-7\beta)a+5\beta-8}{8(4-\beta)}.
\tag{H12}
\]
Thus the older conditional expression improves (H10) only for
\[
                         a>\frac{8-5\beta}{10-7\beta}.
\tag{H13}
\]
Both proven bounds can be used by taking their better exponent.
A sharper conditional hybrid reflection is a separate possible
consumer and is not assumed in this note.

These are smooth weighted discrepancies for the exact free-column
Gauss form. They are not asymptotics for primes or sharp intervals,
do not remove the spherical zero mode, and do not replace the
quadratic/sextic marked detector by this cubic family.

## 4. Retain the contour displacement before optimizing the sector

The fixed-\(\delta\) bound (H7) gives more than its
\(\delta\to0\) consequence (H8).
At \(A=B=X^{1/2}\), Fourier summation in (H7) gives, up to
\(X^\epsilon\Delta^{-\epsilon}\), the three errors
\[
 X^{3/4+\delta/2},\qquad
 X^{5/8+\delta/4}\Delta^{-1+2\delta},\qquad
 X^{3/4+\delta/4}\Delta^{-2/3+2\delta}.
\tag{H14}
\]
For \(0<\delta<1/6\), their width constraints are
\[
 d<\min\left\{\frac14-\frac{\delta}{2},\
       \frac{3-2\delta}{16-16\delta},\
       \frac{3(1-\delta)}{20-24\delta}\right\}.
\tag{H15}
\]
Letting \(\delta\) approach \(1/6\) from below with a fixed
buffer for the requested saving gives the exponent \(5/32\).
No constant uniform as \(\delta\to1/6\) is used.

There is also a valid enlarged row normalization past that point.
For \(1/6\le\delta<1/4\), put
\[
 F_\delta^*(R,L)=
     R+R^{2\delta}L^{2-4\delta}
                    +R^{1-\delta}L^{4/3-4\delta}.
\tag{H16}
\]
Then the same family satisfies
\[
 \sum_{Nr\le R}^{*}
  \|\mathbf Q_r^{[\ell]}(1/2+\delta+it)\|^2
       \ll_{\delta,\epsilon}(RL)^\epsilon F_\delta^*(R,L).
\tag{H17}
\]
Here is the only changed absorption step.
Normalize the finite supremum by
\((RL)^{\epsilon_0}F_\delta^*(R,L)\), with \(\epsilon_0>0\).
The middle row power in this normalization is
\(2\delta+\epsilon_0\), strictly greater than \(2\delta\).
Its weighted partial sum costs \(O(1/\epsilon_0)\) times
\(R^{\epsilon_0}L^{2-4\delta+\epsilon_0}\), exactly the
required \(R^{-2\delta}\) multiple of that term.
The other row powers still exceed \(2\delta\) because
\(\delta<1/4<1/3\).
The fixed contraction constant \(C_0\) may depend on
\(\delta,\epsilon_0\), so this additional constant is harmless.
The original middle row power satisfies
\(1/2-\delta\le2\delta\) in this range; consequently (H6) is
dominated by the new normalization after choosing \(\theta\)
and all small losses as before.
The uniform initial height bound is again controlled by its
middle term. Every other step of the finite-cutoff proof is
unchanged. This proves (H17) without assuming an endpoint
mean or discarding the small positive normalization exponent.

Its fixed-\(\delta\) Type-I consequence is
\[
 |T_\ell(A,B)|\ll
 (AB(1+|\ell|))^\epsilon A^{1/2+\delta}
 \{B+B^{1/2+\delta}(1+|\ell|)^{1-2\delta}
                  +B^{1-\delta/2}(1+|\ell|)^{2/3-2\delta}\}.
\tag{H18}
\]
At balance, the first and third errors in (H14) are unchanged.
The middle error is now
\(X^{1/2+\delta}\Delta^{-1+2\delta}\).
Thus the three width thresholds are
\[
 d_1=\frac14-\frac{\delta}{2},\qquad
 d_2=\frac{1-2\delta}{4-4\delta},\qquad
 d_3=\frac{3(1-\delta)}{20-24\delta}.
\tag{H19}
\]
The middle never binds, since
\[
 d_2-d_1=\frac{\delta(1-2\delta)}{4(1-\delta)}>0.
\]
The first decreases, while
\(d_3'=12/(20-24\delta)^2>0\).
Their unique intersection in \((1/6,1/5)\) solves
\(12\delta^2-13\delta+2=0\), namely
\[
 \delta_*=\frac{13-\sqrt{73}}{24},\qquad
 \boxed{\displaystyle d_*=\frac{\sqrt{73}-1}{48}.}
\tag{H20}
\]
This is an interior value of the proved interval, not a limiting
endpoint. Choose \(\delta=\delta_*\), and let \(\eta>0\) be fixed.
For every
\[
                         \Delta\ge X^{-d_*+\eta},
\tag{H21}
\]
the exact zero-mode-subtracted balanced discrepancy is smaller
than \(X\Delta\) by a fixed power, after choosing all auxiliary
losses sufficiently small.
Numerically \(d_*\) is about \(0.15717\).
This improves both \(3/20\) and \(5/32\).
The optimization is exact algebra, not a numerical search.
It is the optimum within the three displayed fixed-displacement
constraints on this interval; no optimality among other methods
is asserted.

The comparison in Section 3 concerns the simple all-ratio
exponent (H10). The refined balanced result (H21) is stronger
and remains unconditional relative to the stated theta and
large-sieve inputs. It preserves exactly the same free-column,
smooth-weight, and retained-zero-mode scope.
