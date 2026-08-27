# Curve-adapted finite differences select Frobenius channels exactly

Status: **exact all-curve inverse-design theorem, generic minimal-depth
firewall, and bounded symbolic replay; no incomplete-family, number-field,
RH, or GRH estimate**

Bounded replay:
[function_field_frobenius_channel_filter_calculus.py](function_field_frobenius_channel_filter_calculus.py).
Canonical summary:
[function_field_frobenius_channel_filter_calculus.json](function_field_frobenius_channel_filter_calculus.json).

This packet imports the all-curve factorization at frozen commit
18056756f6fdf36c5d7d88f3cc3d5f442878da80 through the four Git blob IDs
checked by the replay. It does not fit finite rows and enumerates no curve.

## 0. Outcome

Let \(C/\mathbf F_q\), \(\Sigma\), and

\[
 F_{C,\Sigma}(X,Y)=
 {\mathcal J_{C,\Sigma}(X,Y)\over
  Z_C(X/\sqrt q)Z_C(Y/\sqrt q)Z_C(XY/q)D_\Sigma(X,Y)}
\tag{0.1}
\]

be exactly as in the frozen predecessor. Write

\[
 Z_C(u)={P_C(u)\over(1-u)(1-qu)},
 \qquad \deg P_C=2g.
\tag{0.2}
\]

Choose a coefficient field \(K\) containing \(\sqrt q\) and the
coefficients of \(P_C\), and choose three factorizations over \(K\):

\[
 P_C=Q_xR_x=Q_yR_y=Q_mR_m.
\tag{0.3}
\]

For a \(K\)-valued filter, the chosen root submultisets must be stable under
\(\operatorname{Gal}(\overline K/K)\). If a filter is required over a
smaller field \(K_0\) not containing \(\sqrt q\), stability of \(Q(u)\)
alone is not enough: the scaled polynomial \(Q(X/\sqrt q)\) itself must
descend to \(K_0[X]\).

Define the finite coefficient operator by multiplying the generating
function by

\[
 \mathscr R_{Q_x,Q_y,Q_m}(X,Y)
 =R_x(X/\sqrt q)R_y(Y/\sqrt q)R_m(XY/q).
\tag{0.4}
\]

Then the selected generating function is exactly

\[
 \boxed{
 \mathscr R_{Q_x,Q_y,Q_m}F_{C,\Sigma}
 =
 {\mathcal J_{C,\Sigma}U_x(X)U_y(Y)U_m(XY)\over
  Q_x(X/\sqrt q)Q_y(Y/\sqrt q)Q_m(XY/q)D_\Sigma},}
\tag{0.5}
\]

where

\[
 U_x(X)=(1-X/\sqrt q)(1-\sqrt qX),
 \quad U_y(Y)=(1-Y/\sqrt q)(1-\sqrt qY),
\tag{0.6}
\]

and

\[
 U_m(XY)=(1-XY/q)(1-XY).
\tag{0.7}
\]

Thus every Galois-stable subset of the three Frobenius pole channels can be
selected or nulled by an explicit finite difference stencil. This is an
exact inverse-design calculus, not a histogram or a fitted recurrence.

Two specializations are important.

### Axis deflation

Set \(Q_x=Q_y=1\) and \(Q_m=P_C\). Then

\[
 \boxed{
 P_C(X/\sqrt q)P_C(Y/\sqrt q)F_{C,\Sigma}
 =
 {\mathcal J_{C,\Sigma}U_xU_yU_m\over
  P_C(XY/q)D_\Sigma}.}
\tag{0.8}
\]

The only remaining Frobenius denominator is mixed. It is analytic on a
bidisc larger than the residual Euler-product bidisc. Consequently, for
every fixed offsets \(a,b\) and every \(\epsilon>0\),

\[
 \boxed{
 [X^{h+a}Y^{h+b}]
 P_C(X/\sqrt q)P_C(Y/\sqrt q)F_{C,\Sigma}
 =O_{C,\Sigma,a,b,\epsilon}
 \left(q^{-(1/3-\epsilon)h}\right).}
\tag{0.9}
\]

So a curve-adapted finite stencil restores the affine exponential shell
scale on every fixed curve, even when repeated normalized Frobenius roots
made the unfiltered shell grow polynomially.

### Complete Frobenius deflation

Set all three \(Q\)'s equal to one. Then

\[
 \boxed{
 P_C(X/\sqrt q)P_C(Y/\sqrt q)P_C(XY/q)F_{C,\Sigma}
 = {\mathcal J_{C,\Sigma}U_xU_yU_m\over D_\Sigma}.}
\tag{0.10}
\]

This removes every Frobenius denominator. It does not improve the proven
bidisc beyond \(r^3<\sqrt q\), because the cubic residual Euler product is
then the limiting analytic object.

## 1. Proof of the selector identity

Equation (0.2) gives

\[
 {1\over Z_C(X/\sqrt q)}
 ={U_x(X)\over P_C(X/\sqrt q)},
 \qquad
 {1\over Z_C(XY/q)}
 ={U_m(XY)\over P_C(XY/q)}.
\tag{1.1}
\]

Substitute (1.1) and its \(Y\)-analogue into (0.1), then cancel the three
complementary factors \(R_x,R_y,R_m\). This proves (0.5) in the rational
function field \(K(X,Y)\). Coefficient multiplication is a finite
convolution, so the identity is also an exact finite-difference statement
for the coefficient array.

If \(Q\) is a proper \(\operatorname{Gal}(\overline K/K)\)-stable factor of
\(P_C\), (0.5) retains exactly the reciprocal roots of \(Q\) in that
channel. Over a splitting field an individual root can be selected. Over
\(K\), roots in one Galois orbit cannot be separated by a \(K\)-polynomial
stencil.

## 2. Exponential decay after axis deflation

The predecessor proves that \(\mathcal J_{C,\Sigma}\) is analytic on every
closed bidisc \(|X|,|Y|\le r\) satisfying \(r^3<\sqrt q\). On the same
bidisc:

- \(1/P_C(XY/q)\) is analytic whenever \(r^2<\sqrt q\), hence in
  particular throughout the smaller residual bidisc \(r<q^{1/6}\);
- deleted axis factors first vanish at modulus \(\sqrt q\);
- deleted mixed factors first vanish at \(|XY|=q\).

The mixed Frobenius denominator alone would allow \(r<q^{1/4}\), but the
residual Euler product is already limiting at \(r<q^{1/6}\). Hence the
right side of (0.8) is analytic on every residual bidisc. Cauchy gives

\[
 [X^iY^j](0.8)=O_r(r^{-i-j}).
\tag{2.1}
\]

For \(i=h+a,j=h+b\), take any \(r<q^{1/6}\) sufficiently close to
\(q^{1/6}\). Equation (2.1) becomes (0.9). No cancellation between
Frobenius phases is used.

This theorem is member-adapted: the filter contains \(P_C\). It does not
say that one fixed observable works uniformly as \(C\) varies.

## 3. Generic minimal-depth firewall

Treat the residual numerator as algebraically independent of the three
Frobenius denominators, so accidental cancellation is excluded. Suppose a
polynomial multiplier leaves precisely the denominators
\(Q_x(X/\sqrt q),Q_y(Y/\sqrt q),Q_m(XY/q)\). Unique factorization forces
that multiplier to be divisible by

\[
 R_x(X/\sqrt q)R_y(Y/\sqrt q)R_m(XY/q).
\tag{3.1}
\]

The primitive minimal multiplier is therefore (0.4), unique up to a scalar.
For a generic degree-\(2g\) numerator, nulling both axis channels requires
bidegree at least

\[
 (2g,2g).
\tag{3.2}
\]

Nulling all three channels has channel-depth sum \(6g\), from three
univariate factors of degree \(2g\). Thus no fixed-depth memberwise finite
difference filter can remove every generic Frobenius channel throughout a
growing-genus family. A family-uniform construction must instead exploit
average or cohomological cancellation, a representation-valued observable,
or deliberately target only a fixed common subchannel.

This is a degree lower bound, not a lower bound on the number of nonzero
stencil coefficients: special sparse numerators can have sparse filters.
For a particular curve, zeros of the residual numerator can also cancel a
pole accidentally; such curve-specific accidents are expressly excluded
from the formal minimality statement.

### One filter across a family

For a finite family of curve numerators \(P_1,\ldots,P_N\), the same
divisibility argument gives the unique primitive full-axis null filter

\[
 L_{\mathcal F}(u)=\operatorname {lcm}(P_1(u),\ldots,P_N(u)).
\tag{3.3}
\]

Indeed, a common multiplier must be divisible by every \(P_i\), and the
least common multiple is sufficient. If the numerators are pairwise
coprime and all have degree \(2g\), the required per-axis depth is \(2gN\).
Common functorial or isotypical factors reduce the depth by exactly their
overlap in the least common multiple.

Overlap does not make complete growing-genus deflation fixed-depth:
\(\deg L_{\mathcal F}\ge\max_i\deg P_i\). It can instead permit
fixed-depth deletion of one fixed common subchannel while the remaining
member-specific channels are retained.

Thus exact memberwise pole deletion becomes more expensive, not cheaper,
as a structurally diverse family grows. This sharpens the design lesson:
a useful family detector should null universal representation or
cohomological channels before specialization, rather than multiply together
every member's zeta numerator.

## 4. What this changes for detector design

The preceding all-curve packet showed that positive genus introduces
unit-circle axis residues. The present theorem gives the exact response:

1. if a fixed curve is the object, its numerator produces the unique
   primitive finite filter which deletes any prescribed stable channels;
2. if genus grows, complete filter depth must grow; shared structure can
   provide a fixed filter only for a fixed common subchannel;
3. after the two axis channels are removed, complete shells again have
   exponential decay at the cubic residual scale;
4. the remaining mixed channel can be retained for spectroscopy or removed
   exactly, but its removal does not improve the currently proved residual
   domain.

This is useful for inverse-design and calibration. It does **not** provide
the incomplete owner/Boolean family required by the RH-facing programme,
nor does it turn a curve-adapted observable into a number-field estimate.

## 5. Claim ledger

| statement | grade |
|---|---|
| three-channel selector identity (0.5) | **PROVED EXACT** |
| \(K\)-stable channel criterion | **PROVED BY FACTORIZATION OVER \(K\supseteq\mathbf Q(\sqrt q)\)** |
| axis-deflated formula (0.8) | **PROVED EXACT** |
| axis-deflated exponential shell bound (0.9) | **PROVED BY THE PINNED RESIDUAL DOMAIN AND CAUCHY** |
| complete deflation identity (0.10) | **PROVED EXACT** |
| generic primitive multiplier and degree lower bound | **PROVED IN THE FORMAL NO-ACCIDENT MODEL** |
| family-uniform least-common-multiple theorem | **PROVED IN THE FORMAL NO-ACCIDENT MODEL** |
| fixed-depth complete filter for growing genus | **REFUTED GENERICALLY** |
| fixed-depth filter for a fixed common subchannel | **POSSIBLE WHEN THAT COMMON FACTOR EXISTS** |
| incomplete owner/Boolean observable | **NOT CONSTRUCTED HERE** |
| number-field transfer, RH, or GRH | **NOT PROVED** |

## 6. Bounded replay

~~~text
python -B research/l-families/atlas/function_field/function_field_frobenius_channel_filter_calculus.py --check
python -B -O research/l-families/atlas/function_field/function_field_frobenius_channel_filter_calculus.py --check
python -B -m unittest tests.test_function_field_frobenius_channel_filter_calculus
python -B -O -m unittest tests.test_function_field_frobenius_channel_filter_calculus
~~~

The replay uses \(q=9\), the formal reciprocal degree-four numerator
\((1+9u^2)^2\), one stable quadratic factor, and bivariate series through
degree ten. It verifies exact partial selection, two-axis deflation, and
three-channel deflation. The example only authenticates the algebra; the
all-curve theorem is proved symbolically above. No field element, point,
closed point, curve, zero, conductor, or \(L\)-function is enumerated.
