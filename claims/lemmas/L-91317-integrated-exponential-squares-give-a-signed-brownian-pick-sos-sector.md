# L-91317 — Integrated exponential squares give an unconditional signed Brownian/Xi Pick SOS sector

Claim ID: `L-91317`  
Status: **PROVED EXACT SIGNED SUM-OF-SQUARES SECTOR; COMPLETE COEFFICIENT SPACE OPEN**  
Created: 2026-08-12  
Depends on: `L-91314`  
RH status: **unproved**

## 1. Exponential-square primitive

Fix

\[
 0<a<\frac12,
 \qquad
 r_0>0,
 \qquad
 d>0,
\]

and let

\[
 P(y)=\sum_{j=0}^{m}a_jy^j
\]

be an arbitrary complex polynomial.  Assume

\[
 a+r_0+2md<\frac12.
\tag{L-91317.1}
\]

Define

\[
 \boxed{
 F_P(x)
 =\int_{-\infty}^{x}
  e^{r_0t}|P(e^{dt})|^2dt.
 }
\tag{L-91317.2}
\]

Then

\[
 \boxed{
 F_P(x)\ge0,
 \qquad
 F_P'(x)=e^{r_0x}|P(e^{dx})|^2\ge0.
 }
\tag{L-91317.3}
\]

Thus `F_P` belongs to the monotone test cone of `L-91314` for every choice of
the internal coefficient phases.

## 2. Explicit signed exponential coefficients

Put

\[
 \boxed{
 b_n=\sum_{j+k=n}\overline{a_j}a_k
 \in\mathbb R,
 \qquad
 0\le n\le2m.
 }
\tag{L-91317.4}
\]

Since

\[
 |P(y)|^2=\sum_{n=0}^{2m}b_ny^n
 \qquad(y>0),
\]

integration gives

\[
 \boxed{
 F_P(x)
 =\sum_{n=0}^{2m}
  \frac{b_n}{r_0+nd}
  e^{(r_0+nd)x}.
 }
\tag{L-91317.5}
\]

The coefficients `b_n` need not be nonnegative.  Their signs and magnitudes
contain genuine interference between the phases of the `a_j`.

Nevertheless the derivative is a pointwise square, so all such signed vectors
belong to the unconditional Brownian-positive sector.

## 3. Brownian reflection/Pick positivity

Let `mathcal R_a` be the Brownian reflection quadratic of `L-91106/L-91310`.
By `L-91314`,

\[
 \boxed{
 \mathcal R_a(F_P)\ge0.
 }
\tag{L-91317.6}
\]

If

\[
 \widetilde K_a(r,s)
 =\frac{
  M(r+a)M(s+a)-M(r-a)M(s-a)
 }{r+s}
\tag{L-91317.7}
\]

is the cross-multiplied Xi Pick kernel, then (L-91317.5) gives the exact finite
matrix inequality

\[
\boxed{
 \sum_{n,\ell=0}^{2m}
 \frac{b_nb_\ell}
 {(r_0+nd)(r_0+\ell d)}
 \widetilde K_a(r_0+nd,r_0+\ell d)
 \ge0.
}
\tag{L-91317.8}
\]

This is an unconditional signed quadratic sector of the target Pick matrix.

## 4. Quartic Gram form in the polynomial coefficients

Substituting (L-91317.4), equation (L-91317.8) becomes

\[
\boxed{
 \sum_{j,k,p,q=0}^{m}
 \overline{a_j}a_k\overline{a_p}a_q
 \frac{
  \widetilde K_a(
   r_0+(j+k)d,
   r_0+(p+q)d)
 }
 {[r_0+(j+k)d][r_0+(p+q)d]}
 \ge0.
}
\tag{L-91317.9}
\]

Thus one explicit fourth-order tensor built from the Xi Pick kernel is positive
on every rank-one Hermitian polynomial square.

Finite sums of squares

\[
 \sum_{\nu}|P_\nu(e^{dx})|^2
\]

give the corresponding convex cone of positive semidefinite polynomial Gram
matrices.

## 5. The first signed three-carrier family

Take

\[
 P(y)=\alpha+\beta y.
\]

Then

\[
 |P(y)|^2
 =|\alpha|^2
 +2\operatorname{Re}(\overline\alpha\beta)y
 +|\beta|^2y^2.
\]

Hence

\[
\boxed{
 F_P(x)
 =\frac{|\alpha|^2}{r_0}e^{r_0x}
 +\frac{2\operatorname{Re}(\overline\alpha\beta)}{r_0+d}
  e^{(r_0+d)x}
 +\frac{|\beta|^2}{r_0+2d}e^{(r_0+2d)x}.
}
\tag{L-91317.10}

The middle coefficient ranges over both signs.  Therefore (L-91317.6) proves a
nontrivial three-carrier interference family which is not contained in the
common-phase positive coefficient cone of `L-91313`.

For fixed endpoint magnitudes, the most adverse middle coefficient is attained
when `alpha` and `beta` have opposite phases; it is still covered by the square
identity.

## 6. Higher-degree sign complexity

For larger `m`, the autocorrelation coefficients `b_n` may have multiple sign
changes.  For example choosing alternating polynomial coefficients produces an
alternating interior profile while the derivative remains the nonnegative
square

\[
 e^{r_0x}|P(e^{dx})|^2.
\]

Thus Brownian positivity is already known on signed packets of arbitrarily
large support and sign complexity.  The obstruction is not merely the presence
of a negative coefficient.

## 7. Exact remaining gap

The full finite coefficient space is larger than the integrated-square cone.
An arbitrary exponential polynomial `F` need not satisfy

\[
 F\ge0,
 \qquad
 F'\ge0,
\]

and its coefficient vector need not be an antiderivative of a nonnegative
exponential polynomial.

The missing theorem is therefore a completion from the signed SOS cone to all
Hermitian coefficient directions.  Equivalently one must control the cross
reflection form between independent square primitives, not only each positive
square separately.

## 8. Proof boundary

```text
arbitrary complex polynomial square derivative       EXACT POSITIVE
signed autocorrelation coefficient vector             EXACT
Brownian reflection positivity                        EXACT ON SOS CONE
signed three-carrier interference family               EXACT
arbitrarily long signed SOS packets                    EXACT
cross terms between independent square primitives      OPEN
full complex Pick coefficient space                    OPEN / RH-BEARING
Riemann Hypothesis                                     UNPROVED
```
