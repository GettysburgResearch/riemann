# L-91611 — Log determinant is resolvent-integrated Julia production

Claim ID: `L-91611`  
Status: **PROVED EXACT FINITE-DIMENSIONAL ENTROPY IDENTITY**  
Created: 2026-08-12  
Depends on: `L-91610`  
RH status: **unproved**

## 1. Positive contraction and Julia defect

Let `T` be an invertible contraction on a finite-dimensional Hilbert space and
put

\[
 A=T^*T,
 \qquad
 D=(I-A)^{1/2}.
\]

Thus

\[
 0<A\le I,
 \qquad
 D^2=I-A.
\]

For `0<=t<=1`, define the interpolating positive operator

\[
 A_t=A+tD^2=(1-t)A+tI.
\]

Every `A_t` is positive and invertible.

## 2. Exact resolvent formula

Differentiating the finite-dimensional determinant gives

\[
 \frac d{dt}\log\det A_t
 =\operatorname{tr}(A_t^{-1}D^2).
\]

Since `A_0=A` and `A_1=I`, integration yields

\[
 \boxed{
 -\log\det(T^*T)
 =\int_0^1
  \operatorname{tr}
  \left[(A+tD^2)^{-1}D^2\right]dt.
 }
\]

Equivalently,

\[
 \boxed{
 -\log\det(T^*T)
 =\int_0^1
  \left\|D(A+tD^2)^{-1/2}\right\|_{\rm HS}^2dt.
 }
\]

The integrand is an explicit positive Julia-production norm at every
resolvent level.

If `T` is singular, both sides are `+infinity` in the monotone regularized
sense obtained from `A+epsilon I`.

## 3. Scalar recovery

For a scalar Schur factor `m`,

\[
 A=|m|^2,
 \qquad
 D^2=|d|^2=1-|m|^2.
\]

The identity reduces exactly to

\[
 -\log|m|^2
 =\int_0^1
  \frac{|d|^2}{|m|^2+t|d|^2}dt,
\]

the Clark-entropy formula of `L-91610`.

## 4. Cascades

For square invertible contractions `T_1,T_2`, determinant multiplicativity
gives

\[
 \boxed{
 -\log\det[(T_1T_2)^*(T_1T_2)]
 =-\log\det(T_1^*T_1)
  -\log\det(T_2^*T_2).
 }
\]

No commutativity is required.  Hence a finite Redheffer/Julia cascade admits
an additive entropy ledger even when its matrix factors do not commute.

Applied to finite coefficient compressions of the explicit safe prime cascade,
this gives a source-defined entropy environment assembled solely from the
returned Euler contractions and their declared Julia defects.

## 5. What the identity does and does not provide

The theorem converts multiplicative contraction loss into an integral of
positive defect norms.  It does **not** imply Loewner domination from a scalar
or determinant inequality.  In particular, equal log determinants do not
identify two operator Grams.

Its correct role is to provide the additive source quantity needed by a
logarithmic Clark/Green completion, while the completed connection must still
preserve the full packet polarization.

## 6. Exact boundary

```text
finite contraction entropy identity             EXACT
resolvent-level positive production ports        EXACT
scalar Julia entropy                             RECOVERED
cascade log-determinant additivity                EXACT
operator Loewner domination from determinant      NOT IMPLIED
completed source-to-model entropy identification  OPEN / RH-BEARING
Riemann Hypothesis                                UNPROVED
```
