# L-91375 — Positive typed causal generators have debt at most twice their exact target mass

Claim ID: `L-91375`  
Status: **PROVED EXACT PHYSICAL GENERATOR THEOREM**  
Created: 2026-08-14  
Depends on: positive component rows and their exact ordinary/detail responses  
RH status: **unproved**

## 1. Positive typed atom

For a quotient `Y>=1`, define

\[
 T(Y)=4\sqrt Y-3,
 \qquad
 S(Y)=5\sqrt Y-3,
\tag{L-91375.1}
\]

and retain the positive component row `Q_Y(j)`, its literal entropy

\[
 E(Y)=\sum_jQ_Y(j)G_j,
\]

its ordinary response `C_Y(q)`, and its radix-four response `Theta_Y(q)`.

All five coordinates are nonnegative.  Moreover they are nondecreasing in `Y`:

- `T,S` are elementary;
- `Q_Y(j)` is nondecreasing from its positive three-sector formula;
- `C_Y(q)=q^-1/2 H(Y/q)` is nondecreasing;
- `Theta_Y(q)=q^-1/2[H(Y/q)-H(Y/(4q))]` is nondecreasing;
- `E(Y)` is a positive logarithmic ramp sum.

## 2. One causal contraction

Let `p>=2`, put `r=p^-1/2`, and use causal zero extension below quotient one.  For `Y>=p`, define the current residual atom

\[
 G_{p,Y}=P_Y-rP_{Y/p}
\tag{L-91375.2}
\]

in every typed coordinate.

Monotonicity and `0<r<1` give coefficientwise

\[
\boxed{
 Q_Y-rQ_{Y/p}\ge0,
 \quad
 C_Y-rC_{Y/p}\ge0,
 \quad
 \Theta_Y-r\Theta_{Y/p}\ge0,
 \quad
 E(Y)-rE(Y/p)\ge0.
}
\tag{L-91375.3}
\]

Thus the causal generator is a complete nonnegative physical row packet and consumes exactly its residual ordinary/detail capacities.

## 3. Exact target mass and score debt

The residual target and declared score are

\[
 T_p(Y)
 =T(Y)-rT(Y/p)
 =(1-r)[4\sqrt Y(1+r)-3],
\tag{L-91375.4}
\]

\[
 S_p(Y)
 =S(Y)-rS(Y/p)
 =(1-r)[5\sqrt Y(1+r)-3].
\tag{L-91375.5}
\]

Both are positive.  Direct subtraction gives

\[
\boxed{
 2T_p(Y)-S_p(Y)
 =3(1-r)[\sqrt Y(1+r)-1]
 \ge0.
}
\tag{L-91375.6}
\]

The displayed causal row has realized loss

\[
 \ell_p(Y)
 =S_p(Y)-[E(Y)-rE(Y/p)].
\]

The optimal packet deficit is no larger than the loss of this admissible row. Since the bracketed literal entropy is nonnegative,

\[
\boxed{
 \Delta_p(Y)\le\ell_p(Y)
 \le S_p(Y)
 \le2T_p(Y).
}
\tag{L-91375.7}
\]

This is a proportional estimate in the exact physical target coordinate, not an absolute-per-generator estimate and not a source-coefficient heuristic.

## 4. Positive source measures

Let `nu` be any finite positive source measure over quotient nodes.  Integrating the atomwise identities gives a complete causal packet `G_p(nu)` satisfying

\[
 G_p(nu)_{\rm row}\ge0,
\]

exact residual ordinary/detail capacities, and

\[
\boxed{
 \Delta[G_p(\nu)]
 \le2\,m[G_p(\nu)],
 \qquad
 m[P]:=T(P).
}
\tag{L-91375.8}
\]

The same target mass is additive and positively homogeneous.

For a child restriction at quotient `Y/p`, including any inherited scalar
coefficient `0<=alpha<=1`, monotonicity and homogeneity of `T` give

\[
\boxed{
 m(\alpha A_pP)
 =\alpha T(Y/p)
 \le T(Y)
 =m(P).
}
\tag{L-91375.9}
\]

## 5. Scope

This theorem closes the physical-generator and proportional-mass joint in Route B **after entry into a positive typed source cone**.

It does not prove that the native signed arithmetic packet admits the exact nonduplicating positive-source entry required before (L-91375.2) may be applied.  That hereditary entry is the remaining producer theorem.

```text
positive typed causal row               EXACT
ordinary/detail residual capacities     EXACT
literal residual entropy nonnegative    EXACT
mass = physical target                  EXPLICIT
local debt <= 2 target mass             EXACT
child target mass nonexpansive          EXACT
native signed-to-positive typed entry    OPEN / RH-BEARING
Riemann Hypothesis                       UNPROVEN
```
