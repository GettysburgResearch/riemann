# L-91315 — The balanced rough-prime ray is the unique simultaneous constant-mode and endpoint-score neutral state

Claim ID: `L-91315`  
Status: **PROVED EXACT TWO-LEDGER THEOREM; FULL COLUMN CAPACITY ALLOCATION OPEN**  
Created: 2026-08-12  
Depends on: `L-26204`, `L-91108`, `L-91311`  
RH status: **unproved**

## 1. A two-parameter centered state

For real `lambda` and `c`, put

\[
 \boxed{
 E_{\lambda,c}(x)
 =L(x)+\lambda R(x)-c.
 }
\tag{L-91315.1}
\]

Use the Mellin convention

\[
 \widehat f(s)=\int_1^\infty f(x)x^{-s-1}dx.
\]

`L-91108` gives

\[
 \widehat L(s)
 =\frac{s+\frac12}
 {s(s-\frac12)\zeta(s+\frac12)},
\tag{L-91315.2}
\]

\[
 \widehat R(s)
 =\frac1{2s(s-\frac12)\zeta(s+\frac12)}.
\tag{L-91315.3}
\]

Hence

\[
 \boxed{
 \widehat E_{\lambda,c}(s)
 =\frac{s+\frac{1+\lambda}{2}}
 {s(s-\frac12)\zeta(s+\frac12)}
 -\frac cs.
 }
\tag{L-91315.4}
\]

## 2. Endpoint entropy-score neutrality

`L-26204` identifies the endpoint entropy score of a causal endpoint density
`f` as

\[
 \boxed{
 \mathfrak S(f)=2\widehat f(1/2),
 }
\tag{L-91315.5}
\]

whenever the removable value exists.

Since

\[
 \lim_{s\to1/2}
 (s-\tfrac12)\zeta(s+\tfrac12)=1,
\]

one has

\[
 \widehat L(1/2)=2,
 \qquad
 \widehat R(1/2)=1.
\tag{L-91315.6}
\]

Therefore

\[
 \boxed{
 \mathfrak S(E_{\lambda,c})
 =2(2+\lambda-2c).
 }
\tag{L-91315.7}
\]

Thus

\[
 \boxed{
 \mathfrak S(E_{\lambda,c})=0
 \iff
 c=1+\frac\lambda2.
 }
\tag{L-91315.8}
\]

This is exactly the center required to remove the leading square-root mass of
the rough monoid.

## 3. Constant-mode neutrality

Put

\[
 z_0=\zeta(1/2)<0.
\]

The residue at `s=0` is

\[
 \operatorname*{Res}_{s=0}\widehat L(s)
 =-\frac1{z_0},
 \qquad
 \operatorname*{Res}_{s=0}\widehat R(s)
 =-\frac1{z_0}.
\tag{L-91315.9}
\]

Consequently

\[
 \boxed{
 \operatorname*{Res}_{s=0}
 \widehat E_{\lambda,c}(s)
 =-\frac{1+\lambda}{z_0}-c.
 }
\tag{L-91315.10}
\]

Define the constant-mode ledger

\[
 \mathfrak M(f)=\operatorname*{Res}_{s=0}\widehat f(s).
\tag{L-91315.11}
\]

Then

\[
 \boxed{
 \mathfrak M(E_{\lambda,c})=0
 \iff
 c=-\frac{1+\lambda}{z_0}.
 }
\tag{L-91315.12}
\]

This is the center required to remove the constant boundary forcing after the
small-prime Boolean block.

## 4. Unique simultaneous neutrality

The two neutral centers agree if and only if

\[
 1+\frac\lambda2
 =-\frac{1+\lambda}{z_0}.
\]

Solving gives

\[
 \boxed{
 \lambda=\kappa_*
 =-\frac{2(1+z_0)}{2+z_0},
 \qquad
 c=c_*=\frac1{2+z_0}.
 }
\tag{L-91315.13}
\]

These are exactly the constants of `L-91311`.  Therefore

\[
 \boxed{
 E_*=L+\kappa_*R-c_*
 }
\tag{L-91315.14}
\]

is the unique centered affine combination of `L` and `R` satisfying

\[
 \boxed{
 \mathfrak S(E_*)=0,
 \qquad
 \mathfrak M(E_*)=0.
 }
\tag{L-91315.15}
\]

The elementary alternating-eta bounds give `-3/2<z_0<-1`; hence

\[
 0<\kappa_*<2.
\tag{L-91315.16}
\]

In particular the RH-bearing SHARP output decomposes with positive coefficients:

\[
 \boxed{
 \Psi=L+2R
 =H_*+(2-\kappa_*)R,
 \qquad
 H_*=L+\kappa_*R.
 }
\tag{L-91315.17}
\]

Thus the balanced bulk ray lies strictly inside the available positive
`(L,R)` output wedge and leaves a positive reserve coefficient.

## 5. Rough renewal has no neutral multiplicative debt

Let

\[
 \mathcal R_{59}(s)
 =\zeta(s+\tfrac12)P_{53}(s)
\]

be the rough-monoid multiplier.  `L-91311` proves

\[
 \mathcal R_{59}E_*
 =-c_*\mathcal B_{53}
\tag{L-91315.18}
\]

in physical coordinates, where

\[
 \mathcal B_{53}(x)=O_{P_{53}}(x^{-1/2}).
\]

In Mellin coordinates, both the `s=0` residue and the potential `s=1/2`
rough pole are removable.  Equivalently,

\[
 \boxed{
 \mathcal R_{59}(s)\widehat E_*(s)
 \text{ is holomorphic at }s=0,\frac12.
 }
\tag{L-91315.19}
\]

Therefore the balanced rough transfer can create neither:

```text
multiplicative constant-mode debt;
multiplicative endpoint-score debt.
```

Its complete scalar discrepancy is the decaying finite boundary port
`-c_* B_53`.

## 6. Bounded accumulation over factor-54 generations

Let the reset scales satisfy

\[
 X_{j+1}\le c_1X_j+C_0,
 \qquad
 c_1<1.
\]

Above the finite base, enlarge constants so that

\[
 X_{j+1}\le c_2X_j
\]

for one fixed `c_2<1`.  A boundary port of size `O(X_j^-1/2)` accumulates as

\[
 \sum_{j<J}O(X_j^{-1/2}).
\]

Since the scales decrease geometrically, the sum is dominated by its final
terms and is bounded independently of the initial endpoint:

\[
 \boxed{
 \sum_{j<J}X_j^{-1/2}=O_{X_{\rm base},c_2}(1).
 }
\tag{L-91315.20}
\]

Thus the balanced-ray boundary port is compatible with bounded **total** scalar
ledger debt, stronger than the bounded-per-generation allowance in `T-91101`.

## 7. What is not proved

The two ledgers above are conclusion-relevant scalar functionals.  They are not
the complete family of ordinary and radix-four column inequalities.

It remains to construct a nonnegative endpoint/carry allocation which:

```text
propagates the balanced H_* child packets with coefficient one;
uses the positive residual coefficient (2-kappa_*)R;
pays the finite boundary port in actual columns;
preserves every endpoint weight and detail capacity.
```

The vanishing scalar ledgers do not imply that capacity theorem by themselves.

## 8. Proof boundary

```text
endpoint score as 2 fhat(1/2)                    IMPORTED EXACT
score-neutral center for L+lambda R                EXACT
constant-mode-neutral center                       EXACT
unique simultaneous balanced ray                   EXACT
0<kappa_*<2 and positive SHARP decomposition       EXACT
no rough multiplicative score/mass debt            EXACT
bounded total scalar boundary accumulation          EXACT
full column-capacity balanced allocation            OPEN / RH-BEARING
Riemann Hypothesis                                 UNPROVED
```
