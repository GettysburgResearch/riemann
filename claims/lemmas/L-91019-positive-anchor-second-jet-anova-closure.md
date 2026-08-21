# L-91019 — A positive anchor closes every second logarithmic jet into one returned state and exactly two orthogonal details

Claim ID: `L-91019`  
Status: **PROPOSED COMPLETE EXACT HILBERT-JET THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `L-91014`  
RH status: **unproved**

## 1. The dyadic anchor law

Fix `a>0`.  The second coherent factor in

\[
 V_{a,a}k_{2a,s}=k_{a,s}\otimes k_{a,s+a}
\]

has boundary norm

\[
 R_a=Q_a(1+2a).
\]

Define the unit anchor

\[
 \eta_a
 =\frac1{\sqrt{R_a}}
  \sum_{n\ge1}\sqrt{q_a(n)}n^{-1/2-a}e_n.
 \tag{L-91019.1}
\]

Let `T e_n=(log n)e_n`.  Then `eta_a` induces the positive probability law

\[
 \mathbb P_a(n)
 =\frac{q_a(n)n^{-1-2a}}{Q_a(1+2a)}.
 \tag{L-91019.2}
\]

All logarithmic moments are finite.

## 2. Centred moments and orthogonal anchor jets

Put

\[
 \mu_a=\langle T\eta_a,\eta_a\rangle,
 \qquad X_a=T-\mu_a I,
\]

and

\[
 \sigma_a^2=\langle X_a^2\eta_a,\eta_a\rangle.
 \tag{L-91019.3}
\]

Unless the anchor is a point mass, `sigma_a>0`; here the support contains
`1` and every prime, so `sigma_a>0`.

Let

\[
 m_{3,a}=\langle X_a^3\eta_a,\eta_a\rangle,
 \qquad
 m_{4,a}=\langle X_a^4\eta_a,\eta_a\rangle.
\]

Define

\[
 e_{0,a}=\eta_a,
 \qquad
 e_{1,a}=\frac{X_a\eta_a}{\sigma_a},
 \tag{L-91019.4}
\]

and

\[
 p_{2,a}(X)
 =X^2-\sigma_a^2-\frac{m_{3,a}}{\sigma_a^2}X.
 \tag{L-91019.5}
\]

Its squared norm is

\[
 \boxed{
 \tau_a^2
 =m_{4,a}-\sigma_a^4-rac{m_{3,a}^2}{\sigma_a^2}
 \ge0.
 }
 \tag{L-91019.6}
\]

The inequality is exactly the Schur-complement inequality for the positive
moment Gram of `1,X,X^2`.  If `tau_a>0`, put

\[
 e_{2,a}=p_{2,a}(X_a)\eta_a/\tau_a.
 \tag{L-91019.7}
\]

If `tau_a=0`, the second detail port is absent and every formula below remains
valid after deleting it.

Then `e_0,e_1,e_2` are orthonormal.

## 3. Exact first-jet closure

Let `H` be any Hilbert space carrying a self-adjoint logarithmic generator `L`.
On `H tensor H_a`, put

\[
 L_{\rm tot}=L\otimes I+I\otimes T.
\]

For every vector `f` in the domain of `L`,

\[
 \boxed{
 L_{\rm tot}(f\otimes e_0)
 =(L+\mu_a)f\otimes e_0
 +\sigma_a f\otimes e_1.
 }
 \tag{L-91019.8}
\]

Thus the first logarithmic jet has one returned, affinely centred coarse state
and one orthogonal positive detail.

## 4. Exact second-jet closure

For every `f` in the domain of `L^2`,

\[
 \boxed{
\begin{aligned}
 L_{\rm tot}^2(f\otimes e_0)
 ={}&\big[(L+\mu_a)^2+\sigma_a^2\big]f\otimes e_0\\
 &+\left[2\sigma_a(L+\mu_a)+\frac{m_{3,a}}{\sigma_a}\right]
   f\otimes e_1\\
 &+\tau_a f\otimes e_2.
\end{aligned}}
 \tag{L-91019.9}
\]

This follows by expanding `(L+mu+X)^2`, projecting `X eta` and `X^2 eta`
onto the orthonormal anchor jets, and using

\[
 X^2\eta
 =\sigma_a^2e_0+rac{m_{3,a}}{\sigma_a}e_1+	au_ae_2.
 \tag{L-91019.10}
\]

No remainder exists.

## 5. Positive three-state Gram identity

Taking norms in (L-91019.9) gives

\[
 \boxed{
\begin{aligned}
 \|L_{\rm tot}^2(f\otimes e_0)\|^2
 ={}&\|[(L+\mu_a)^2+\sigma_a^2]f\|^2\\
 &+\|[2\sigma_a(L+\mu_a)+m_{3,a}/\sigma_a]f\|^2\\
 &+\tau_a^2\|f\|^2.
\end{aligned}}
 \tag{L-91019.11}
\]

The polarization of this identity is positive semidefinite for arbitrary
independent carrier vectors before aggregation.  Thus the positive source
cocycle closes the complete degree-two logarithmic jet in exactly three states:

```text
one coefficient-one returned state
+ two orthogonal emitted detail states.
```

This is the same state count as the `SO(3)` Cauchy all-pass completion, obtained
here without guessing a matrix polarization.

## 6. Moment formulas from the Euler source

The anchor cumulants are explicit derivatives of the positive Euler function:

\[
 \mu_a=-\partial_s\log Q_a(s)|_{s=1+2a},
 \tag{L-91019.12}
\]

\[
 \sigma_a^2=\partial_s^2\log Q_a(s)|_{s=1+2a},
 \tag{L-91019.13}
\]

and higher centred moments are universal polynomials in the derivatives of
`log Q_a` at the same absolutely convergent point.  Equivalently they are sums
of independent local-prime cumulants under the product probability law
(L-91019.2).

Hence every coefficient in the three-state source jet is finite, explicit and
prime-side positive at every `a>0`.

## 7. Intertwining with the divisor isometry

Because `V_(a,a)L=(L_1+L_2)V_(a,a)`, equations (L-91019.8)--(L-91019.9)
apply directly to the dyadic factorisation of the generalized-Jordan coherent
state.  The returned component is the delayed coarse logarithmic jet, with the
explicit affine centering determined by the positive anchor.  The two emitted
components are genuine orthogonal source details.

Thus the inherited pole-subtracted term of `L-91015` cannot create an
unbounded state family at second-current order.  Any remaining obstruction must
be a mismatch between the two-dimensional source-detail metric here and the
two physical Cauchy-detail ports of `L-91013`, not a hidden fourth state or an
indefinite source Gram.

## 8. Boundary

Closed:

```text
positive anchor probability law;
exact centred first- and second-jet decomposition;
one returned state plus exactly two orthogonal details;
source-side independent-frequency PSD;
explicit Euler-moment coefficients;
no state proliferation through second-current order.
```

Open:

```text
unitary identification of the source-detail plane with the physical Cauchy ports;
completed gamma/pole contribution in that identification;
coefficient-one physical recurrence;
RH.
```
