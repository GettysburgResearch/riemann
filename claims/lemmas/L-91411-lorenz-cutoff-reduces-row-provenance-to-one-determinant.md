# L-91411 — Once the cutoff is beyond the child support, Lorenz row provenance reduces to one cutoff determinant

Claim ID: `L-91411`  
Status: **PROVED EXACT ORDERED-MEASURE REDUCTION — DETERMINANT SIGN OPEN**  
Created: 2026-08-13  
Depends on: score-Lorenz construction; `L-91359` cutoff beyond child support; `L-91410` residual-support ordering  
RH status: **unproved**

## 1. Score and row measures

Fix

\[
 p>=67,\qquad 1<=y<=67,\qquad 2<=j<=66.
\]

On the finite active divisor set of `P_61`, let

\[
 S_d=K_S(d;p,y)>0,
 \qquad
 R_d=K_R^{(j)}(d;p,y)>=0,
 \qquad
 q_d=\frac{R_d}{S_d}.
 \tag{L-91411.1}
\]

Let `E` and `O` be the positive even- and odd-parity score measures.  Write

\[
 E_S=E(D),\qquad O_S=O(D),
 \tag{L-91411.2}
\]

\[
 E_R=\int q\,dE,\qquad O_R=\int q\,dO.
 \tag{L-91411.3}
\]

The signed arithmetic score and row are

\[
 S_{\rm sig}=E_S-O_S,
 \qquad
 R_{\rm sig}=E_R-O_R.
 \tag{L-91411.4}
\]

## 2. The actual Lorenz residual

Let `U<=E` be the leftmost score submeasure with

\[
 U(D)=O_S.
 \tag{L-91411.5}
\]

It includes a possible fractional atom at its cutoff `c`.  The positive Lorenz residual is

\[
 \nu=E-U,
 \tag{L-91411.6}
\]

and has exact score

\[
 \nu(D)=E_S-O_S=S_{\rm sig}.
 \tag{L-91411.7}
\]

The support-separation theorem on the branch gives

\[
 c>y.
 \tag{L-91411.8}
\]

Hence every source in `nu` is child-inactive.

## 3. Residual row upper bound

By `L-91410`, the ratio on the residual support is nonincreasing in the source node.  Therefore

\[
 d>=c
 \Longrightarrow
 q_d<=q_c.
 \tag{L-91411.9}
\]

This remains true for any fraction of the cutoff atom retained in `nu`.  Consequently

\[
 \boxed{
 R(\nu)=\int q\,d\nu
 <=q_c\,S_{\rm sig}.
 }
 \tag{L-91411.10}
\]

## 4. One determinant

The desired literal row provenance is

\[
 R(\nu)<=R_{\rm sig}.
 \tag{L-91411.11}
\]

By (L-91411.10), it is sufficient that

\[
 R_{\rm sig}>=q_cS_{\rm sig}.
 \tag{L-91411.12}
\]

Since `S_c>0` and `q_c=R_c/S_c`, this is exactly

\[
 \boxed{
 \Delta_{j,c}(p,y)
 :=R_{\rm sig}^{(j)}(p,y)S_c(p,y)
  -S_{\rm sig}(p,y)R_c^{(j)}(p,y)
 >=0.
 }
 \tag{L-91411.13}
\]

If (L-91411.13) holds, then

\[
 \boxed{
 R_{\rm sig}^{(j)}
 =R^{(j)}(\nu)+B_j,
 \qquad B_j>=0,
 }
 \tag{L-91411.14}
\]

so the Lorenz residual source and the target-null row bonus form an exact nonnegative physical-row packet.

## 5. Why this is sharper than the full determinant

The earlier bathtub reduction used the full even/odd determinant

\[
 E_RO_S-E_SO_R>=0.
 \tag{L-91411.15}
\]

That condition compares the odd row average with the average of the complete even measure.  The present theorem uses the actual cutoff ratio and only asks for

\[
 \frac{R_{\rm sig}}{S_{\rm sig}}>=q_c.
 \tag{L-91411.16}
\]

It is strictly tailored to the realized Lorenz residual and does not require continuous ordering in the discarded child-active sector.

## 6. Automatic inactive-cutoff cases

If

\[
 \frac{py}{c}<j,
 \tag{L-91411.17}
\]

then the cutoff row is inactive:

\[
 R_c^{(j)}=0.
 \tag{L-91411.18}
\]

In that case

\[
 \Delta_{j,c}=R_{\rm sig}^{(j)}S_c,
 \tag{L-91411.19}
\]

so every available strict signed-row lower bound closes the determinant immediately.  The remaining proof campaign concerns only activated cutoff cells.

## 7. Exact finite-analytic domain

The cutoff results on the branch give

\[
 y<c<2000,
 \tag{L-91411.20}
\]

with only 184 possible positive-parity `P_61` cutoff nodes.  Therefore the remaining sign has the domain

```text
p >= 67;
1 <= y <= 67;
2 <= j <= 66;
c one of 184 even P_61 divisors below 2000;
y < c;
c is the actual fractional score-Lorenz cutoff;
py/c >= j.
```

It is finite in the discrete variables and piecewise analytic in `(sqrt(p),sqrt(y),log p,log y)` after causal activation cells are fixed.

## 8. Boundary

```text
cutoff beyond child support                       IMPORTED EXACT
outer residual ratio ordering                     EXACT / L-91410
residual row <= cutoff ratio times residual score EXACT
one-cutoff determinant sufficient                 EXACT
inactive cutoff-row sector                        REDUCED TO SIGNED ROW
184 cutoff nodes                                   IMPORTED EXACT
activated cutoff determinant                      OPEN / FINITE-ANALYTIC
literal row provenance after determinant           IMMEDIATE
Riemann Hypothesis                                 UNPROVEN
```
