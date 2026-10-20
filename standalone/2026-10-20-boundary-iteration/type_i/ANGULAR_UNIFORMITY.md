# Polynomial angular uniformity of the resummed cubic mean

20 October 2026. **Status: proposed source-dependent theorem.**
This is an additional proof over the frozen fixed-angular mean.
It does not alter that theorem's file or presume a uniform angular
version of a spherical theorem in the literature.

Dependencies:

* ../average/ANGULAR_SELF_ABSORPTION.md, SHA256
  0c195c93ef2548a81197e21d0eca58f1632f25e9339d0f078fa185f8605d59e8;
* FINITE_PROFILE_CLOSURE.md, SHA256
  a4a1798f304fd9a551c35b2a161ef2f7b82644d62d9f0eae986df2afb7100dad;
* DUAL_RESUMMATION.md, SHA256
  d8dae0a17a85b466ba9d9d5b762ee532ce92b0a45de7236ffe5b3bb8256dbef2;
* the exact Dunn--Radziwill source identities already pinned and
  independently audited in those notes.

The optional quadratic extension also uses
../mixed/QUADRATIC_PAIR_ABSORPTION.md and, at angular order zero,
../global/GUARDED_SPHERICAL_MEAN.md. The numerical zero-free
boundary is not an input to the unconditional assertions here.

## 1. Uniform theorem

Let \(\ell\) be any nonzero integer, and let
\(\mathbf Q_r^{[\ell]}\) denote the eight-component vector formed
from the four ramified profiles at both angular signs \(\ell,-\ell\).
Set
\[
                       L=1+|\ell|+|t|.
\]
For every fixed \(0<\delta<1/4\) and \(\epsilon>0\),
\[
 \sum_{Nr\le R}^{*}
   \|\mathbf Q_r^{[\ell]}(1/2+\delta+it)\|^2
 \ll_{\delta,\epsilon}
          R^{1+\epsilon}L^{\,2-4\delta+\epsilon}.
\tag{U1}
\]
The implied constant is independent of \(R,\ell,t\).
The field, the four specified profiles, and the finite excluded
prime \(3\) are fixed. The asterisk retains primary squarefree
rows and every original common-prime zero.

For \(1/4<p<1/2\), the same exact reflection gives
\[
 \sum_{Nr\le R}^{*}\|\mathbf Q_r^{[\ell]}(p+it)\|^2
 \ll_{p,\epsilon}
          R^{2-2p+\epsilon}L^{\,4-4p+\epsilon}.
\tag{U2}
\]
These are polynomial angular bounds. No subpower or Lindelof
bound in the angular parameter is asserted.

For the Type-I form in the fixed-angular theorem, uniformly in
every \(|b_v|\le1\),
\[
 |T_\ell(A,B)|
 \ll_{\epsilon,W_A,W_B}
 (AB)^\epsilon(1+|\ell|)^{1+\epsilon}A^{1/2}B.
\tag{U3}
\]
All constants in this statement involve finitely many seminorms
of the fixed smooth radial profiles. No derivative of order
depending on \(\ell\) is required.

## 2. The exact finite family is uniformly bounded in angular order

In the four-to-27 cusp conversion and its left inverse, every
angular phase is a product of \(i^\ell\), a sixth-root unit to
the power \(\ell\), and a power of \(\omega^\ell\).
Thus these phases run through a finite set as \(\ell\) varies.
The three-cusp inverse remains \(M^*/3\), with \(MM^*=3I\).
Its fixed factors \(3^{5/2+3s}\), \(9\,3^{4s}\), and their
inverses have bounded magnitude on each fixed vertical line,
independently of height and angular order.

The only infinite ramified sum has ratio
\[
                  i^{3\ell}3^{1/2-3w}.
\]
On \(\Re w\ge1/2+\delta\), its denominator has magnitude at
least \(1-3^{-1-3\delta}\). Thus the full finite-family
conversion, not just the displayed minor, is uniform in \(\ell\).
The moving-row cusp action is a finite collection of monomial
matrices indexed by \(r\bmod9\), also independent of \(|\ell|\).

The scalar extraction from cusp Mellins has no geometric
denominator: it is the exact exceptional-cusp minor and the
trivial-channel projection. It can therefore be continued to a
left line below \(1/6\) without using a divergent coefficient
expansion there. When that left-line extraction is reflected,
the 27-to-four expansion is used at \(1-s\), whose real part is
greater than one. This observation is needed in Section 4.

Nonzero angular order still gives entire continuation for every
integer \(\ell\). That qualitative assertion is used separately
for each member; the estimates below do not take the implicit
constants of an \(\ell\)-fold differentiation argument as uniform.

## 3. Uniform gamma and resummed reflection estimates

Apart from fixed ramified powers and unit phases, the exact gamma
quotient is
\[
 G_\ell(s)=(2\pi)^{4s-2}
 \frac{\Gamma(5/6+|\ell|/2-s)\Gamma(7/6+|\ell|/2-s)}
      {\Gamma(s+|\ell|/2-1/6)\Gamma(s+|\ell|/2+1/6)}.
\tag{U4}
\]
For any fixed \(0<\eta<1/6\), uniformly on the two lines
\(\Re s=-\eta,1/2-\delta\) in use,
\[
                    |G_\ell(\sigma+it)|
              \ll_{\sigma}(1+|\ell|+|t|)^{2-4\sigma}.
\tag{U5}
\]
Indeed \(|\Gamma(x-it)|=|\Gamma(x+it)|\) for real \(x\).
Pair the first numerator with the second denominator and the
second numerator with the first denominator. The real shifts
in each pair are fixed; their sum is \(2-4\sigma\).
The uniform gamma-ratio bound on a right half-plane gives (U5),
including the bounded region of its arguments. All arguments on
these lines have real part bounded away from zero when
\(|\ell|\ge1\). There is no exponential angular factor.

Combining (U5) with the exact local divisor identity gives,
uniformly in \(\ell\),
\[
 \|\mathbf Q_r^{[\ell]}(1/2-\delta+it)\|
 \ll_{\delta,\eta}
 L^{4\delta}(Nr)^{-1/2+2\delta+\eta}
       \sum_{k\mid r}(Nk)^{1/2-\delta}
               \|\mathbf Q_k^{[\ell]}(1/2+\delta-it)\|.
\tag{U6}
\]
All ray phases and all common-prime zeros are still those of the
frozen theorem. Summing the square over \(r\le R\) yields
\[
 \mathcal A_{-}(R,\ell,t)
 \ll L^{8\delta}R^{4\delta+\eta}
       \sum_{Nk\le R}(Nk)^{-2\delta}
               \|\mathbf Q_k^{[\ell]}(1/2+\delta-it)\|^2.
\tag{U7}
\]

## 4. A uniform initial growth bound before absorption

On \(\Re s=1+\eta\), the complete Dirichlet series is absolutely
bounded by
\(\zeta_E(1+\eta)\zeta_E(5/2+3\eta)\), independently of
\(\ell,r,t\), since every coefficient phase has magnitude at
most one.

On \(\Re s=-\eta\), use the exact cusp extraction and reflect.
At \(w=1+\eta\), the divisor identity has coefficient
\((Nk)^{-\eta}\), and its complementary local factors have
bounded product \(O((Nr)^{\eta'})\). The absolutely convergent
right-line series and (U5) give
\[
 \|\mathbf Q_r^{[\ell]}(-\eta+it)\|
 \ll_{\eta,\eta'}(Nr)^{1/2+2\eta+\eta'}
                    (1+|\ell|+|t|)^{2+4\eta}.
\tag{U8}
\]
This bound uses the full dual series, not a truncated tail.

Three-lines interpolation now gives, at
\(\sigma=1/2+\delta\),
\[
 \|\mathbf Q_r^{[\ell]}(\sigma+it)\|
 \ll_{\eta,\eta'}(Nr)^{C_{\eta,\eta'}}
              (1+|\ell|+|t|)^{\,1-2\delta+2\eta}.
\tag{U9}
\]
Only a fixed polynomial in \(r\) is needed at this stage.
For clarity, uniformity of the height parameter can be checked by
fixing \(t_0,\ell\), writing \(L_0=1+|\ell|+|t_0|\), and applying
three-lines to each scalar component multiplied by \(e^{s^2}\)
after translating height by \(t_0\). On a boundary line,
\(1+|\ell|+|t_0+v|\le L_0(1+|v|)\), and \(e^{-v^2}\) absorbs
the latter fixed power. Divide by the affine interpolation of
the two powers of \(L_0\). The resulting boundary constants are
uniform. The source split Mellin integrals and gamma factors have
sub-Gaussian strip growth for each member, so the Gaussian
three-lines argument is legitimate without uniform derivative
constants in the original angular construction.

For any proposed final angular loss \(\epsilon_0>0\), choose
\(4\eta<\epsilon_0/2\). Equation (U9), squared, shows that
the supremum normalized by
\[
                R^{1+\epsilon_0}
                   L^{\,2-4\delta+\epsilon_0}
\tag{U10}
\]
is finite for every finite row cutoff and finite angular cutoff,
even though its preliminary bound may depend on those cutoffs.
The normalization has enough height power before absorption.
This avoids assuming the desired uniform estimate to define its
own supremum.

## 5. Simultaneous row and angular absorption

Let \(M\) be the supremum just described, over
\(R\le R_{\max}\), \(1\le|\ell|\le L_{\max}\), and all real
heights. Include both signs of each angular order in the vector.
The original free-split integral, at \(Y\ge1\), obeys
\[
 \mathcal I(R,\ell,t;Y)
 \ll (RY)^\eta
       \{R+Y^{1-2\delta}+R^{2/3}Y^{2/3-2\delta}\}.
\tag{U11}
\]
Its constant is independent of \(\ell,t\): the squarefree
column phases \(\alpha(c)^\ell(Nc)^{-it}\) and cube phases
have magnitude one. The same three convergent cube sums and
the same fixed Gaussian cutoff are used as in the frozen mean.

Use (U7), partial summation, and Minkowski in the shifted Gaussian
integral. Relative to (U10), the shifted contribution is bounded
by
\[
             C_{\delta,\epsilon_0}M
                        Y^{-4\delta}R^{2\delta+\eta}L^{8\delta}.
\tag{U12}
\]
The height convolution is uniform because
\(1+|\ell|+|t+v|\le L(1+|v|)\); its remaining factor is
integrated against \(e^{-v^2}\). Reflection changes \(\ell\)
only to \(-\ell\), and \(k\mid r\), so both finite cutoffs close.

Choose
\[
                  Y=C_0 R^{1/2+\delta/4}L^2.
\tag{U13}
\]
Then the coefficient of \(M\) is
\[
 C_{\delta,\epsilon_0}C_0^{-4\delta}
                         R^{-\delta^2+\eta}.
\]
Choose \(\eta<\delta^2/2\), then choose the fixed \(C_0\)
sufficiently large to make this at most one half for every
\(R\ge1\). This \(C_0\) is independent of both finite cutoffs,
the angular order, and height.

For (U11), the nonconstant row powers before the small sieve loss
are
\[
 (1/2+\delta/4)(1-2\delta)<1,\qquad
 2/3+(1/2+\delta/4)(2/3-2\delta)<1.
\]
Their angular powers are \(2-4\delta\) and
\(4/3-4\delta\), respectively. Choose all sieve and divisor
losses sufficiently small relative to \(\epsilon_0,\delta\);
then (U11) is at most a fixed constant times (U10).
The finite supremum therefore satisfies \(M\le C+M/2\).
Let both cutoffs tend to infinity. Renaming \(\epsilon_0\)
proves (U1). Equation (U7) then proves (U2).

## 6. Type I and smooth angular localization

Mellin inversion in the unrestricted \(u\)-variable and Cauchy
in \(v\) give, at each fixed \(0<\delta<1/4\),
\[
 |T_\ell(A,B)|
 \ll_{\delta,\epsilon,W}
       A^{1/2+\delta}B^{1+\epsilon}
                  (1+|\ell|)^{1-2\delta+\epsilon}.
\tag{U14}
\]
The inverse cube factor is uniformly bounded by absolute Euler
convergence on this line, even when \(\ell\) grows.
The Mellin integration in \(t\) uses a fixed number of radial
derivatives exceeding its displayed polynomial height degree.
Choose \(\delta\) inside the final loss to obtain (U3).

Let \(f\) be a smooth function on \(\mathbb R/\mathbb Z\) with
mean zero, and define \(T_f\) by inserting
\(f(\arg\alpha(uv)/(2\pi))\) in the same bilinear form.
Absolute Fourier summation gives
\[
 |T_f(A,B)|\ll_{\epsilon,W}(AB)^\epsilon A^{1/2}B
            \sum_{k\ne0}(1+|k|)^{1+\epsilon}|\widehat f(k)|.
\tag{U15}
\]
This is a genuine growing-angular-family consequence. The
coefficient \(b_v\) is the same in every Fourier mode.

For a fixed compact smooth bump \(\phi\), an angular center
\(\theta_0\), and \(0<\Delta\le1\), periodize
\(\phi((\theta-\theta_0)/\Delta)\). Its nonzero Fourier
coefficients have weighted sum \(O_{\phi,\epsilon}(\Delta^{-1-\epsilon})\).
Consequently
\[
 \left|T_{\phi_{\Delta,\theta_0}}(A,B)
       -\Delta\!\left(\int_{\mathbb R}\phi\right)T_0(A,B)\right|
 \ll_{\epsilon,W,\phi}
       (AB)^\epsilon A^{1/2}B\Delta^{-1-\epsilon}.
\tag{U16}
\]
The zero-mode term is retained; no claim is made that the
untwisted spherical residue vanishes. At \(A=B=X^{1/2}\),
(U16) is smaller by a power than the natural absolute scale
\(X\Delta\) whenever \(\Delta\ge X^{-1/8+\eta}\) for fixed
\(\eta>0\), after choosing the error allowances sufficiently small.
This is a smooth weighted angular statement, not an asymptotic
for prime counts or a sharp interval with arbitrary coefficients.

## 7. Optional quadratic-pair extension

The same proof applies to the closed pair with conductor \(S\)
of norm \(H\), with the unchanged exact j-exchange and all cube
zeros. For \(0<\delta<1/6\), put
\[
 F_\delta(R,H)=R+R^{1/2-\delta}H^{1-2\delta}
                         +R^{1-\delta}H^{2/3-2\delta}.
\]
Its uniform version is
\[
 \sum_{Nr\le R,(r,S)=1}^{*}
    \|\mathbf Q_{r,S}^{[\ell]}(1/2+\delta+it)\|^2
 \ll_{\delta,\epsilon}
       (RH)^\epsilon F_\delta(R,H)
                 (1+|\ell|+|t|)^{2-4\delta+\epsilon}.
\tag{U17}
\]
For \(\ell\ne0\), constants vanish by angular differentiation.
For \(\ell=0\), require the nonunit primitive quadratic guard
and use GUARDED_SPHERICAL_MEAN.md; the duplicate sign in the
vector is then omitted.

The finite-cutoff supremum may also include \(NS\le H_{\max}\).
The preliminary left-line bound acquires only a fixed polynomial
in \(H\), and the reflected term gains \(H^{4\delta}\).
Use
\[
                Y=C_0R^{1/2+\theta}H(1+|\ell|+|t|)^2,
                 \qquad 4\delta\theta>\eta.
\]
This cancels that factor and gives the same contraction for all
three finite cutoffs. Choosing \(\theta,\eta\) inside the final
loss gives the three powers in \(F_\delta\).
At \(\ell=0\), the finitely many bounded gamma arguments on
the preliminary left line are handled separately; choose
\(0<\eta<1/6\). They introduce no pole or changing height degree.

In particular, uniformly in \(\ell\), the unconditional pair
Type-I bound is
\[
 |T_{\ell,\xi_S}(A,B)|
 \ll_{\epsilon,W}(ABH)^\epsilon(1+|\ell|)^{1+\epsilon}A^{1/2}
          \{B+B^{3/4}H^{1/2}+BH^{1/3}\}.
\tag{U18}
\]
For fixed nontrivial \(S\), this also covers the zero angular
mode and yields (U15) without a mean-zero condition, with the
corresponding fixed-conductor constant.
The displayed moving-conductor costs remain. No joint
quadratic-row saving or stricter mixed-terminal boundary is
inferred from polynomial angular uniformity.
