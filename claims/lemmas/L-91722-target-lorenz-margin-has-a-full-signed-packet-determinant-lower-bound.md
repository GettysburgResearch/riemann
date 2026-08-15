# L-91722 — The Target-Lorenz margin has a full signed-packet determinant lower bound

Claim ID: `L-91722`  
Status: **PROVED EXACT SUFFICIENT REDUCTION**  
Created: 2026-08-14  
Depends on: `L-91682`, `L-91684`  
RH status: **unproved**

## 1. Signed packet and Lorenz residual

For one causal leaf, write the complete signed target and row as

\[
 \mathscr T=E_T-O_T>0,
\tag{L-91722.1}
\]

\[
 \mathscr R_j=E_R^{(j)}-O_R^{(j)}.
\tag{L-91722.2}
\]

Let `U` be the leftmost even target submeasure with

\[
 T(U)=O_T,
\]

let `c` be its cutoff, and put

\[
 \nu=E-U.
\]

Then

\[
 T(\nu)=\mathscr T.
\tag{L-91722.3}
\]

The Target-Lorenz row margin is

\[
\begin{aligned}
 \mathfrak L_j
 &=R_j(U)-O_R^{(j)}\\
 &=\mathscr R_j-R_j(\nu).
\end{aligned}
\tag{L-91722.4}
\]

## 2. Right-tail bound

The residual `nu` is supported on the cutoff atom and even atoms to its right.
By the proved target-normalized causal profile order,

\[
 \rho_j(d)=\frac{K_R^{(j)}(d)}{K_T(d)}
\]

is nonincreasing in divisor order. Therefore

\[
 \rho_j(d)\le\rho_j(c)
 \qquad(d\in\operatorname{supp}\nu).
\]

Integrating in target currency gives

\[
\boxed{
 R_j(\nu)
 \le\rho_j(c)T(\nu)
 =\rho_j(c)\mathscr T.
}
\tag{L-91722.5}
\]

Substitution into (L-91722.4) proves

\[
\boxed{
 \mathfrak L_j(p,y)
 \ge
 \mathscr R_j(p,y)
 -\rho_j(c;p,y)\mathscr T(p,y).
}
\tag{L-91722.6}
\]

## 3. Full signed determinant gate

Since `K_T(c)>0`, the sufficient sign condition is

\[
\boxed{
 \mathscr D_{j,c}(p,y)
 :=\mathscr R_j(p,y)K_T(c;p,y)
  -\mathscr T(p,y)K_R^{(j)}(c;p,y)
 \ge0.
}
\tag{L-91722.7}
\]

Indeed, (L-91722.7) is precisely

\[
 \mathscr R_j-\rho_j(c)\mathscr T\ge0.
\]

This is a **full signed-packet determinant**, not the signed prefix determinant
of `L-91684.5`. It uses the complete causal finite-Euler row and target plus one
cutoff atom.

The condition is sufficient, not asserted necessary: the actual right-tail
average can be strictly smaller than its cutoff maximum.

## 4. Relation to the support reduction

If

\[
 c\ge py/j,
\]

then `K_R^(j)(c)=0` by `L-91721`. Equation (L-91722.7) reduces to

\[
 \mathscr R_jK_T(c)\ge0,
\]

and (L-91722.6) becomes the exact equality

\[
 \mathfrak L_j=\mathscr R_j.
\]

Thus `L-91721` is the zero-cutoff-row sector of the present determinant route.

## 5. Correct cell form

Using

\[
 A=\sqrt{py},
 \qquad u=\sqrt y,
\]

the target factors are quadratic-algebraic after multiplication by `A`, as in
`R-91720`. On a fixed parent/child row activation cell,

\[
 Q_Y(j)=C_{j,N}\log Y-D_{j,N}
\]

makes both `mathscr R_j` and `K_R^(j)(c)` explicit
algebraic-logarithmic functions. Hence (L-91722.7) defines a smaller
fail-closed cell campaign than the original prefix determinant:

```text
complete signed causal row;
complete signed causal target;
one of 185 cutoff atoms;
one of 65 component rows.
```

## 6. Boundary

```text
right-tail target identity                           EXACT
right-tail row <= cutoff ratio times target          EXACT
full signed determinant -> Lorenz row margin         EXACT
support-easy theorem recovered                       EXACT
all full signed determinant signs                    OPEN / FINITE-ANALYTIC
necessity of the determinant                         NOT CLAIMED
Riemann Hypothesis                                   UNPROVEN
```
