# L-91780 — The proportional determinant lower-bounds every Target-Lorenz row gain

Claim ID: `L-91780`  
Status: **PROVED EXACT REDUCTION**  
Created: 2026-08-15  
Depends on: `L-91720`, `L-91682`, `L-91684`  
RH status: **unproved**

For one stopped causal leaf write the even and odd target totals as `E_T,O_T`
and the corresponding component-row totals as `E_R^(j),O_R^(j)`. Let `U` be
the leftmost even target submeasure with `T(U)=O_T`. Put

\[
 \mathfrak L_j=R_j(U)-O_R^{(j)}
\]

and define the target-proportional determinant

\[
 \boxed{
 \Theta_j=O_T E_R^{(j)}-E_T O_R^{(j)}.
 }
\tag{L-91780.1}
\]

The proportional even submeasure

\[
 V=\frac{O_T}{E_T}E
\]

is feasible in the exact-target box. `L-91720` says that the leftmost removal
maximizes every target-normalized component row. Hence

\[
 R_j(U)\ge R_j(V)=\frac{O_T}{E_T}E_R^{(j)}.
\]

Subtracting the odd row gives

\[
 \boxed{
 \mathfrak L_j
 \ge
 \frac{O_T E_R^{(j)}-E_T O_R^{(j)}}{E_T}
 =\frac{\Theta_j}{E_T}.
 }
\tag{L-91780.2}
\]

Since `E_T>0`, the sign condition `Theta_j>=0` closes the Target-Lorenz row
margin. The same source coefficients then lift through the resident positive
ordinary response maps; radix-four responses are formed only after the common
ordinary sum at `q` and `4q`.

This determinant is sufficient, not asserted necessary. It is distinct from
the cutoff determinant of `L-91722` and has no cutoff variable.
