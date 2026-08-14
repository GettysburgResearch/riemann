# L-91685 — Target-Lorenz is the exact common-source vector primal and has an explicit support-function dual

Claim ID: `L-91685`  
Status: **PROVED EXACT ORDERED-MEASURE / FINITE-DUAL THEOREM**  
Created: 2026-08-14  
Depends on: `L-91682`, `L-91684`; elementary fractional-knapsack duality and finite-dimensional separation  
Replay: `X-91685-target-lorenz-vector-primal-dual`  
RH status: **unproved**

## 1. Typed even source and odd demand

Let

\[
 e_1<e_2<\cdots<e_N
\]

be the available even source atoms. Atom `e` has one positive target mass
`T_e`, one nonnegative score mass `S_e`, and nonnegative physical row masses

\[
 R_e^\alpha,
 \qquad \alpha\in\mathcal A.
\]

Let the odd demand totals be

\[
 O_T,
 \qquad O_S,
 \qquad O_R^\alpha.
\]

A common-source removal is a coefficient vector

\[
 0\le u_e\le1.
\]

It is feasible when

\[
 \sum_eu_eT_e=O_T,
 \tag{L-91685.1}
\]

\[
 \sum_eu_eS_e\le O_S,
 \tag{L-91685.2}
\]

and

\[
 \sum_eu_eR_e^\alpha\ge O_R^\alpha
 \qquad(\alpha\in\mathcal A).
 \tag{L-91685.3}
\]

Then the unused source `nu_e=1-u_e` has exactly the signed target, at least the
signed score, and no more than the signed arithmetic row in every coordinate.
The same coefficients are used in every ledger.

## 2. Common monotone order

Assume

\[
 \sigma_e:=\frac{S_e}{T_e}
 \quad\hbox{is nondecreasing in }e,
 \tag{L-91685.4}
\]

and, for every physical row,

\[
 \rho_e^\alpha:=\frac{R_e^\alpha}{T_e}
 \quad\hbox{is nonincreasing in }e.
 \tag{L-91685.5}
\]

Let `U` be the leftmost target submeasure of total mass `O_T`: it fills every
target atom from the left, with at most one fractional cutoff atom.

The one-dimensional bathtub principle gives simultaneously

\[
 \boxed{
 S(U)\le S(V)
 }
 \tag{L-91685.6}
\]

and

\[
 \boxed{
 R^\alpha(U)\ge R^\alpha(V)
 \qquad(\alpha\in\mathcal A)
 }
 \tag{L-91685.7}
\]

for every target-matched submeasure `V` satisfying (L-91685.1).

The point is simultaneous: all row profiles use the same source order, so the
same leftmost `U` maximizes every row while minimizing score.

## 3. Exact vector-primal equivalence

There exists a common-source coefficient vector satisfying
(L-91685.1)--(L-91685.3) if and only if the Target-Lorenz vector itself obeys

\[
 \boxed{S(U)\le O_S}
 \tag{L-91685.8}
\]

and

\[
 \boxed{R^\alpha(U)\ge O_R^\alpha
 \quad\hbox{for every }\alpha.}
 \tag{L-91685.9}
\]

The forward implication follows from (L-91685.6)--(L-91685.7); the reverse
implication takes `u=U`.

Therefore the Target-Lorenz object is not merely one convenient ansatz. Inside
the literal even-source box it is the universal common-source primal:

```text
Target-Lorenz succeeds  <=>  some common-source vector succeeds.
```

No more general redistribution among the same source atoms can repair a failed
Target-Lorenz row.

## 4. Exact support-function dual

For

\[
 \tau\in\mathbb R,
 \qquad \beta\ge0,
 \qquad \lambda_\alpha\ge0,
\]

put

\[
 A_e(\tau,\beta,\lambda)
 =\tau T_e-\beta S_e+
   \sum_\alpha\lambda_\alpha R_e^\alpha.
 \tag{L-91685.10}
\]

The common-source system is feasible if and only if, for every such multiplier,

\[
 \boxed{
 \sum_e[A_e(\tau,\beta,\lambda)]_+
 \ge
 \tau O_T-\beta O_S+
 \sum_\alpha\lambda_\alpha O_R^\alpha.
 }
 \tag{L-91685.11}
\]

Necessity follows by evaluating a feasible `u` and using `0<=u_e<=1`.
Sufficiency is finite-dimensional separation: the support function of the box
image is exactly the left side of (L-91685.11).

Thus every finite stopped leaf is fail-closed:

```text
primal: one literal common-source coefficient vector;
dual:   one explicit support-function separator.
```

The theorem extends to finite positive endpoint fibers by direct integration;
for the current arithmetic application the source set is already finite.

## 5. A failed row supplies its own exact separator

Fix one row `alpha`, and let `c` be the fractional Target-Lorenz cutoff. Choose

\[
 \beta=0,
 \qquad
 \lambda_\alpha=1,
 \qquad
 \lambda_\gamma=0\ (\gamma\ne\alpha),
 \qquad
 \tau=-\rho_c^\alpha.
 \tag{L-91685.12}
\]

Since the row-per-target profile is nonincreasing,

\[
 [R_e^\alpha-\rho_c^\alpha T_e]_+
 =
 \begin{cases}
 R_e^\alpha-\rho_c^\alpha T_e,&e<c,\\
 0,&e\ge c
 \end{cases}
\]

up to harmless zero-profile ties. The dual inequality becomes exactly

\[
 \boxed{
 R^\alpha(U)-O_R^\alpha\ge0.
 }
 \tag{L-91685.13}
\]

If this margin is negative, (L-91685.12) is an explicit strict separator. The
single-row gate and the finite Farkas alternative are therefore the same
object, not two unrelated proof strategies.

## 6. One full determinant is sufficient

Let

\[
 E_T=\sum_eT_e,
 \qquad
 E_R^\alpha=\sum_eR_e^\alpha.
\]

The proportional target submeasure

\[
 V=\frac{O_T}{E_T}E
\]

is target matched. Hence, by (L-91685.7),

\[
 R^\alpha(U)\ge\frac{O_T}{E_T}E_R^\alpha.
\]

Consequently the single full determinant

\[
 \boxed{
 O_TE_R^\alpha-E_TO_R^\alpha\ge0
 }
 \tag{L-91685.14}
\]

implies the Target-Lorenz row gate for coordinate `alpha`.

For all rows simultaneously, the family (L-91685.14) is a sufficient
cutoff-free producer theorem. It is stronger than necessary but has only one
full-packet determinant per row.

## 7. `P_61` causal specialization

For the stopped `P_61` leaf, set

\[
 T_e=K_T(e),
 \qquad
 S_e=K_S(e),
 \qquad
 R_e^j=K_R^{(j)}(e),
 \qquad 2\le j\le66.
\]

`L-91682` proves the common row order (L-91685.5). The target-to-score order in
`L-91684` proves (L-91685.4), and `L-91684` already proves the score gate
(L-91685.8). Therefore the entire literal common-source problem is equivalent
to the 65 Target-Lorenz margins

\[
 \boxed{
 \mathfrak L_j(p,y)=R_j(U)-O_R^{(j)}\ge0.
 }
 \tag{L-91685.15}
\]

Ordinary and radix-four capacities are positive linear images of the
nonnegative component-row bonus. They do not require independent source
coefficients. The fixed shared boundary/port packet remains a separate one-use
coordinate in the native-root composition.

## 8. Exact boundary

```text
same source coefficients in target/score/all rows       EXACT
Target-Lorenz simultaneous bathtub optimality            EXACT
common-source primal equivalence                          EXACT
support-function/Farkas dual                              EXACT
failed row -> explicit cutoff separator                   EXACT
full target-normalized determinant sufficient             EXACT
actual P61 row margins beyond proved quotient region      OPEN / ARITHMETIC
native root/port composition                              SEPARATE
Riemann Hypothesis                                        UNPROVEN
```
