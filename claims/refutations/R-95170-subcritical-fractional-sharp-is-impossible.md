# R-95170 — Every subcritical fractional-SHARP route is impossible

Claim ID: `R-95170`  
Status: **PROPOSED COMPLETE UNCONDITIONAL NO-GO THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-17  
Depends on: `L-32408` at `f8030b7fab808956f6e7968d3699685d7fb2cf6c`; `L-32701` at `36b3bebea80e18f965f304638e2123c4d2363a09`; Hardy's theorem that zeta has a nonreal zero on the critical line  
Scope: the average-carry triangular inverse of endpoint-vanishing power hinges; no assertion of square-root SHARP or RH

## 1. Fractional hinges and fixed inverse rows

For `0<alpha<=1/2` and real `X>=3`, put

\[
h_{X,\alpha}(q)=q^{-\alpha}-X^{-\alpha},
\qquad 2\le q\le X.
\]

For each fixed row `j>=2`, let `c_{X,alpha}(j)` be the same average-carry inverse used by SHARP. The finite adjoint formula gives an endpoint-independent coefficient sequence `K_j(q)` such that

\[
 c_{X,\alpha}(j)
 =\sum_{2\le q\le X}K_j(q)
   \bigl(q^{-\alpha}-X^{-\alpha}\bigr).
\tag{R-95170.1}
\]

For rows two and three,

\[
\sum_{q\ge2}{K_2(q)\over q^s}
={E_2(s)\over2\zeta(s)}+1,
\qquad
E_2(s)=-2+4\,2^{-s}-2\,3^{-s},
\tag{R-95170.2}
\]

and

\[
\sum_{q\ge2}{K_3(q)\over q^s}
={E_3(s)\over6\zeta(s)}+{1\over3},
\qquad
E_3(s)=-2-2\,2^{-s}+10\,3^{-s}-6\,4^{-s}.
\tag{R-95170.3}
\]

The elementary constants are the exact correction for the omitted carry column `q=1`.

## 2. Exact Mellin transform

For `Re z` initially large,

\[
\int_q^\infty
\bigl(q^{-\alpha}-X^{-\alpha}\bigr)X^{-z-1}\,dX
={\alpha\,q^{-z-\alpha}\over z(z+\alpha)}.
\]

Finite-sum interchange therefore gives

\[
\boxed{
\int_1^\infty c_{X,\alpha}(j)X^{-z-1}\,dX
={\alpha\over z(z+\alpha)}
\left[
 {E_j(z+\alpha)\over j(j-1)\zeta(z+\alpha)}
 +{2\over j(j-1)}
\right].
}
\tag{R-95170.4}
\]

No interpolation error is hidden here. On every interval `[N,N+1)`, the active carry columns are fixed and (R-95170.1) is affine in `X^{-alpha}`. The left and right endpoint values are precisely the integer inverse rows because the newly activated `q=N+1` hinge vanishes at activation. Hence eventual one-sign on integer endpoints implies eventual one-sign of the continuous endpoint function.

## 3. The two row numerators cannot cancel one zero together

Write

\[
x=2^{-s},\qquad y=3^{-s}.
\]

If `E_2(s)=0`, then `y=2x-1`. Substitution into `E_3` gives

\[
E_3=-6(x-1)(x-2).
\]

For `Re s>0`, one has `|x|<1`, so neither root is possible. Thus

\[
\boxed{E_2(s),E_3(s)\text{ have no common zero in }\Re s>0.}
\tag{R-95170.5}
\]

## 4. Critical-line zeros kill every strict subcritical exponent

Let

\[
\rho={1\over2}+i\gamma
\]

be any nonreal critical-line zero. Fix `0<alpha<1/2`. Then

\[
z_\rho=\rho-\alpha
\]

lies in `Re z>0`. By (R-95170.5), at least one of the transforms in (R-95170.4) has a genuine nonreal pole at `z=z_rho`.

For positive real `z`, the reciprocal-zeta term in (R-95170.4) has no pole: the pole of zeta at `z+alpha=1` becomes a zero, and the elementary factors have singularities only at nonpositive real points. Therefore the transform has no positive-real singularity.

If the corresponding row were eventually nonnegative or eventually nonpositive, Landau's one-sign theorem would force a singularity at the positive real abscissa of convergence. The nonreal pole with positive real part makes that abscissa positive, while the explicit transform has no positive-real singularity. Contradiction.

Hence, for every strict subcritical exponent,

\[
\boxed{
0<\alpha<{1\over2}
\Longrightarrow
\text{at least one of rows }2,3\text{ changes sign infinitely often.}
}
\tag{R-95170.6}
\]

In particular, nonnegative inverse coefficients for all rows and all endpoints are impossible:

\[
\boxed{
0<\alpha<{1\over2}
\Longrightarrow
\text{fractional SHARP is false.}
}
\tag{R-95170.7}
\]

## 5. Critical-exponent rigidity

At `alpha=1/2`, every critical-line pole moves to `Re z=0`, exactly the boundary of the one-sign argument. Only a hypothetical zero with `Re rho>1/2` moves into `Re z>0`. Thus the square-root exponent is the unique exponent in the positive hinge family `0<alpha<=1/2` not unconditionally ruled out by known critical-line zeros.

This does not prove square-root SHARP. It proves that changing to `alpha=1/3`, `1/4`, or any other strict subcritical exponent cannot be a shortcut.

## 6. Boundary

```text
fixed-row Mellin transforms                 EXACT
integer-to-continuous sign interpolation    EXACT
no-common-zero numerator theorem            EXACT
subcritical fractional SHARP                FALSE
alpha=1/2 uniquely viable in this family    PROVED
square-root SHARP                           OPEN / RH-BEARING
Riemann Hypothesis                          UNPROVED
```
