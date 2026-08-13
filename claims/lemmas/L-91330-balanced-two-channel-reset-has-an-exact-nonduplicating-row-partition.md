# L-91330 — The balanced two-channel reset has an exact nonduplicating source split and direct finite-row lift

Claim ID: `L-91330`  
Status: **PROPOSED COMPLETE EXACT ONE-RESET SOURCE/ROW PROJECTION — ALL-GENERATION ROUGH RECURSION OPEN**  
Created: 2026-08-12  
Depends on exact paths:

- `claims/lemmas/L-91315-balanced-rough-ray-is-uniquely-mass-and-score-neutral.md`;
- `claims/lemmas/L-91320-balanced-ray-has-no-upward-parity-and-an-interval-seed-lift.md`;
- `claims/lemmas/L-91322-normalized-component-row-monotonicity-lifts-the-parity-shadow-exactly.md`.

RH status: **unproved**

## 1. Canonical balanced parameter

Put

\[
 z_0=\zeta(1/2),
 \qquad
 \kappa_*=-\frac{2(1+z_0)}{2+z_0},
 \qquad
 a_*=-\frac2{z_0}.
\]

Then

\[
 H_*=L+\kappa_*R
 =(1+\kappa_*)U_{a_*},
\]

where

\[
 U_a(x)=a\sqrt x\,B(x)-A(x).
\]

The elementary eta bounds on the branch give

\[
 1<a_*<2,
 \qquad
 0<\kappa_*<2.
\]

## 2. Atomwise nonduplicating SHARP split

For one squarefree atom `n<=x`, write

\[
 w_a(x,n)=\frac{a\sqrt x}{n}-\frac1{\sqrt n}.
\]

The RH-sensitive SHARP atom is

\[
 w_\Psi(x,n)=\frac{4\sqrt x}{n}-\frac3{\sqrt n}.
\]

Direct algebra gives the pointwise identity

\[
 \boxed{
 w_\Psi
 =(1+\kappa_*)w_{a_*}
 +(2-\kappa_*)w_1.
 }
\]

Both summands are nonnegative on the complete reset window. Thus the native
SHARP source measure splits **atom by atom** into two separately labelled
positive measures:

```text
balanced channel: (1+kappa_*) w_(a_*);
reserve channel:  (2-kappa_*) w_1.
```

No even capacity, odd demand, Schur slack or target atom is copied. Summing the
signed parity masses gives exactly

\[
 \boxed{
 \Psi=H_*+(2-\kappa_*)R.
 }
\]

This establishes the native source-mass interpretation at one reset boundary
without using the false completed-cascade tensorization.

## 3. Two disjoint no-upward Hall transports

On

\[
 1\le x\le c_0^{-1},
\]

the reserve channel has the certified prefix Hall margin

\[
 \mathcal H_{1,t}(x)>39/100
\]

with support `e<=o`.

The balanced channel has the certified margin

\[
 \mathcal H_{*,t}(x)>21/100
\]

with the same support `e<=o`.

Apply the two Hall transports to their separately labelled atomwise source
shares. Since the shares sum exactly to `w_Psi`, the transports are disjoint in
the source ledger. Their unused even masses are respectively

\[
 H_*(x)
 \quad\text{and}\quad
 (2-\kappa_*)R(x),
\]

and therefore sum exactly to `Psi(x)`.

Every matched edge produces a nonnegative interval seed and has nonnegative
score

\[
 \log(o/e)\ge0.
\]

## 4. Universal normalized component-row monotonicity

Retain the positive component row

\[
 Q_Y(n)=C_{n,N}\log Y-D_{n,N}
 \qquad(N\le Y<N+1).
\]

For any real `a>=1`, define

\[
 \mathcal Q_{n,a}(Y)
 =\frac{Q_Y(n)}{a\sqrt Y-1}.
\]

The coefficient `C_(n,N)` is strictly positive. Indeed it is the derivative of
`Q_Y(n)` with respect to `log Y`, and differentiating the positive component-row
formula replaces every active logarithmic atom by its positive coefficient.

A direct calculation gives

\[
 \boxed{
 2Y(a\sqrt Y-1)^2
 \mathcal Q_{n,a}'(Y)
 =M_a(Y),
 }
\]

where

\[
 M_a(Y)=a\sqrt Y\,[2C_{n,N}-Q_Y(n)]-2C_{n,N}.
\]

Moreover

\[
 \boxed{
 M_a'(Y)=-\frac{aQ_Y(n)}{2\sqrt Y}\le0.
 }
\]

The directed theorem in `L-91322` proves at every right cell endpoint that

\[
 M_1(Y)>1/20.
\]

Since `C_(n,N)>0`, this inequality implies

\[
 2C_{n,N}-Q_Y(n)>0.
\]

Consequently, for every `a>=1`,

\[
 \boxed{
 M_a(Y)
 =M_1(Y)+(a-1)\sqrt Y[2C_{n,N}-Q_Y(n)]
 >M_1(Y)>1/20.
 }
\]

Thus

\[
 \boxed{
 \mathcal Q_{n,a}(Y)
 \text{ is strictly increasing on the complete reset window}
 }
\]

simultaneously for every `a>=1`, including `a=1` and `a=a_*`.

## 5. Exact finite-row lift for both channels

For either channel parameter `a in {1,a_*}`,

\[
 k^{-1/2}Q_{x/k}(n)
 =w_a(x,k)\mathcal Q_{n,a}(x/k).
\]

If a Hall edge satisfies `e<=o`, then

\[
 x/e\ge x/o
\]

and universal monotonicity gives

\[
 \mathcal Q_{n,a}(x/e)
 -\mathcal Q_{n,a}(x/o)
 \ge0.
\]

Therefore each of the two disjoint Hall transports lifts directly to every
exact finite component row. The unmatched even residuals are also nonnegative.
After multiplying by the positive channel coefficients, their row sum is the
exact SHARP row.

Hence one reset boundary has a source-faithful positive decomposition into:

```text
balanced Hall row packets;
reserve Hall row packets;
nonnegative balanced residual rows;
nonnegative reserve residual rows;
```

with every source coefficient used exactly once.

## 6. What this repairs and what remains

This theorem repairs part of interface 1 in the PR #405 review. The statement
that `L+2R` had no proved native endpoint-block realization was too broad:
there is now an exact atomwise and rowwise realization on every factor-54 reset
window, and it does not use the false two-state completed cascade.

It does not prove the recursive rough-tree composition. Between reset boundaries
one must still use the exact four-state arithmetic semigroup and show that the
child source measures presented to the next local projection form the required
nonduplicating recursive ledger with coefficient-one score transfer.

```text
atomwise SHARP split into balanced+reserve channels  EXACT
no duplicate source mass at one reset               EXACT
both no-upward Hall transports                       DIRECTED EXACT
universal a>=1 row-profile monotonicity              PROPOSED COMPLETE
exact balanced and reserve row lift                  PROPOSED COMPLETE
one-reset native source/row partition                PROPOSED COMPLETE
all-generation four-state child ledger               OPEN / RH-BEARING
Riemann Hypothesis                                   UNPROVEN
```
