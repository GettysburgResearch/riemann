# L-91311 — The rough-prime renewal diagonalizes into square-root and constant modes and has a unique positive double-neutral ray

Claim ID: `L-91311`  
Status: **PROVED EXACT RENEWAL NORMAL FORM; CAPACITY-FAITHFUL USE OF THE BALANCED RAY OPEN**  
Created: 2026-08-12  
Depends on: `L-91108`, `L-91113`, `L-91307`  
RH status: **unproved**

## 1. The two critical states have a simpler diagonal basis

Retain

\[
 A(x)=\sum_{n\le x}\frac{\mu(n)}{\sqrt n},
 \qquad
 B(x)=\sum_{n\le x}\frac{\mu(n)}n,
\]

and

\[
 L(x)=2\sqrt x\,B(x)-A(x),
 \qquad
 R(x)=\sqrt x\,B(x)-A(x).
\]

Define

\[
 \boxed{
 X(x)=L(x)-R(x)=\sqrt x\,B(x),
 }
\tag{L-91311.1}
\]

and

\[
 \boxed{
 Y(x)=L(x)-2R(x)=A(x).
 }
\tag{L-91311.2}
\]

The inverse change of variables is

\[
 \boxed{
 R=X-Y,
 \qquad
 L=2X-Y.
 }
\tag{L-91311.3}
\]

Thus the endpoint equality/reserve pair is a positive-cone presentation of the
classical half-weight Möbius prefixes `sqrt(x) B(x)` and `A(x)`.

## 2. Exact diagonal rough-prime renewals

Let

\[
 P_{53}=\prod_{p\le53}p,
 \qquad
 \mathcal M_{59}=\{m\ge1:(m,P_{53})=1\},
\]

and

\[
 \delta_{53}=\prod_{p\le53}\left(1-\frac1p\right),
 \qquad
 \beta_{53}=\prod_{p\le53}\left(1-\frac1{\sqrt p}\right).
\]

`L-91113` gives, for `a=1,2`,

\[
 F_a^{(53)}(x)
 =\sum_{\substack{m\in\mathcal M_{59}\\m\le x}}
 m^{-1/2}U_a(x/m),
 \qquad
 U_1=R,
 \quad U_2=L.
\tag{L-91311.4}
\]

For every `x>=P_53`,

\[
 F_a^{(53)}(x)=a\delta_{53}\sqrt x-\beta_{53}.
\]

Taking the combinations `F_2-F_1` and `F_2-2F_1` yields the exact diagonal
normal form

\[
 \boxed{
 \sum_{\substack{m\in\mathcal M_{59}\\m\le x}}
 m^{-1/2}X(x/m)
 =\delta_{53}\sqrt x,
 }
\tag{L-91311.5}
\]

\[
 \boxed{
 \sum_{\substack{m\in\mathcal M_{59}\\m\le x}}
 m^{-1/2}Y(x/m)
 =\beta_{53}.
 }
\tag{L-91311.6}
\]

Hence the two-state renewal is exactly the direct sum of its square-root neutral
mode and its constant neutral mode.  The difficulty is not coupling in the
renewal operator; it is the wedge of inequalities in (L-91311.3).

## 3. Mellin diagonalization

Use the Mellin convention

\[
 \widehat f(s)=\int_1^\infty f(x)x^{-s-1}dx.
\]

From `L-91108`,

\[
 \boxed{
 \widehat X(s)
 =\frac1{(s-\frac12)\zeta(s+\frac12)},
 \qquad
 \widehat Y(s)
 =\frac1{s\zeta(s+\frac12)}.
 }
\tag{L-91311.7}
\]

The rough-monoid multiplier is

\[
 \boxed{
 \mathcal R_{59}(s)
 =\sum_{m\in\mathcal M_{59}}m^{-s-1/2}
 =\zeta(s+\tfrac12)P_{53}(s),
 }
\tag{L-91311.8}
\]

where

\[
 P_{53}(s)=\prod_{p\le53}(1-p^{-s-1/2}).
\]

Therefore

\[
 \mathcal R_{59}(s)\widehat X(s)
 =\frac{P_{53}(s)}{s-1/2},
 \qquad
 \mathcal R_{59}(s)\widehat Y(s)
 =\frac{P_{53}(s)}s.
\tag{L-91311.9}
\]

The two neutral poles are now literally diagonal.

## 4. The unique positive ray cancelling both neutral modes

Put

\[
 z_0=\zeta(1/2).
\]

The elementary alternating-eta bounds give

\[
 -2<z_0<-1.
\tag{L-91311.10}
\]

Define

\[
 \boxed{
 \kappa_*
 =-\frac{2(1+z_0)}{2+z_0}>0,
 \qquad
 c_*=1+\frac{\kappa_*}{2}
 =\frac1{2+z_0}>0.
 }
\tag{L-91311.11}
\]

Numerically,

\[
 \kappa_*=1.705\ldots,
 \qquad
 c_*=1.852\ldots .
\]

Let

\[
 \boxed{
 H_*(x)=L(x)+\kappa_*R(x),
 \qquad
 E_*(x)=H_*(x)-c_*.
 }
\tag{L-91311.12}
\]

For a general `lambda`, the natural center of `L+lambda R` is
`1+lambda/2`; this always cancels the leading square-root mass of the rough
reservoir.  The remaining constant forcing vanishes if and only if

\[
 (1+\lambda)+(1+\lambda/2)z_0=0.
\]

Thus `lambda=kappa_*` is the **unique** centered ray cancelling both neutral
modes.  Because `kappa_*>0`, this ray lies in the interior of the original
positive `(L,R)` output cone.

## 5. Exact finite boundary-port identity

Put

\[
 S_{59}(x)
 =\sum_{\substack{m\in\mathcal M_{59}\\m\le x}}m^{-1/2}
\]

and define the rough lattice remainder

\[
 \boxed{
 \mathcal B_{53}(x)
 =S_{59}(x)
  -2\delta_{53}\sqrt x
  -z_0\beta_{53}.
 }
\tag{L-91311.13}
\]

For `x>=P_53`, equations (L-91311.4) and (L-91311.11) give exactly

\[
 \boxed{
 \sum_{\substack{m\in\mathcal M_{59}\\m\le x}}
 m^{-1/2}E_*(x/m)
 =-c_*\mathcal B_{53}(x).
 }
\tag{L-91311.14}
\]

The entire critical square-root and constant mass has disappeared.  The right
side is a finite small-prime boundary port.  Indeed, with

\[
 \rho(y)=\sum_{n\le y}n^{-1/2}-2\sqrt y-z_0,
\]

inclusion--exclusion gives

\[
 \boxed{
 \mathcal B_{53}(x)
 =\sum_{d\mid P_{53}}
  \frac{\mu(d)}{\sqrt d}\rho(x/d).
 }
\tag{L-91311.15}
\]

The classical Euler remainder yields

\[
 \mathcal B_{53}(x)=O_{P_{53}}(x^{-1/2}).
\tag{L-91311.16}
\]

Thus the distinguished mixed channel transfers the complete rough bulk with
coefficient one and leaves only a decaying finite boundary port.  This does not
assert positivity of the centered child states.

## 6. Double-pole cancellation in Mellin space

The transform of `H_*` is

\[
 \widehat H_*(s)
 =\frac{s-\dfrac{z_0}{2(2+z_0)}}
 {s(s-\frac12)\zeta(s+\frac12)}.
\tag{L-91311.17}
\]

Multiplying the centered state by the rough renewal gives

\[
\boxed{
 \widehat{\mathcal R_{59}*E_*}(s)
 =\frac{P_{53}(s)}{(2+z_0)s(s-\frac12)}
 \left[
  (2+z_0)s-\frac{z_0}{2}
  -(s-\tfrac12)\zeta(s+\tfrac12)
 \right].
}
\tag{L-91311.18}
\]

The bracket vanishes at both

\[
 s=0
 \quad\text{and}\quad
 s=\frac12,
\]

where the second value uses

\[
 \lim_{s\to1/2}(s-1/2)\zeta(s+1/2)=1.
\]

Hence both displayed neutral poles are removable.

## 7. Secant-defect interpretation

Set

\[
 w=s+\frac12,
 \qquad
 f(w)=(w-1)\zeta(w).
\]

The bracket in (L-91311.18) is exactly

\[
 \boxed{
 \operatorname{Chord}_{[1/2,1]}f(w)-f(w),
 }
\tag{L-91311.19}
\]

where the chord joins

\[
 f(1/2)=-z_0/2,
 \qquad
 f(1)=1.
\]

Thus, after the arithmetic and renewal diagonalizations, the residual transform
is governed by one classical one-variable secant defect of the regularized zeta
function.  No sign of that defect is asserted here; the identity is a new
one-dimensional analytic target and a diagnostic for any proposed mixed-port
construction.

## 8. Consequence for the reset design

The rough-prime interface now has the exact normal form

```text
square-root mode X = sqrt(x) B(x)     pure forcing delta_53 sqrt(x);
constant mode    Y = A(x)             pure forcing beta_53;
unique positive mixed ray H_*         both modes cancelled after centering;
remaining forcing                     finite O(x^-1/2) boundary port.
```

Therefore the mixed boundary port required by `L-91307` is not arbitrary.  One
canonical interior ray removes every macroscopic renewal mode.  A closing reset
may propagate `H_*` as the balanced bulk coordinate and retain one complementary
signed coordinate, equivalently `Y=A`, only in the finite boundary/capacity
ledger.

What remains is to lift this normal form through the positive endpoint rows and
radix-four capacities without inferring positivity from the alternating inverse.

## 9. Proof boundary

```text
(L,R) -> (sqrt(x)B,A) diagonalization              EXACT
pure square-root and constant rough renewals         EXACT
two neutral Mellin poles                             EXACT
unique positive double-neutral ray                   EXACT
finite decaying boundary-port identity               EXACT
double-pole cancellation                             EXACT
regularized-zeta secant-defect formula               EXACT
capacity-faithful balanced-ray reset                 OPEN
complementary signed-state control                    OPEN / RH-BEARING
Riemann Hypothesis                                   UNPROVED
```
