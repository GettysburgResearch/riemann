# L-91720 — Target-Lorenz is the exact common-source vector primal/dual

Claim ID: `L-91720`  
Status: **PROVED EXACT ORDERED-CONE OPTIMIZATION AND SEPARATION THEOREM**  
Created: 2026-08-14  
Depends on: elementary fractional-knapsack duality; for the `P_61` specialization, `L-91682/L-91684`  
Replay: `X-91720-target-lorenz-vector-primal-dual`  
RH status: **unproved**

## 1. Ordered typed source problem

Let

\[
 d_1<d_2<\cdots<d_n
\]

be the even source atoms. Atom `i` has strictly positive target capacity
`t_i`, declared score `s_i`, and a physical vector

\[
 r_i\in K,
\]

where `K` is a closed convex cone. In the finite physical application one may
take

\[
 K=\mathbb R_+^{65}
\]

for component rows `2<=j<=66`, or a larger product cone after adjoining any
other coordinate whose target-normalized profile has the same order.

Fix an odd target demand `M` with

\[
 0\le M\le\sum_i t_i.
\]

An exact-target common-source removal is a vector

\[
 0\le u_i\le1,
 \qquad
 \sum_i u_i t_i=M.
\tag{L-91720.1}
\]

It uses the same source coefficient `u_i` in target, score and every physical
coordinate. Put

\[
 T(u)=\sum_i u_it_i,
 \quad
 S(u)=\sum_i u_is_i,
 \quad
 R(u)=\sum_i u_ir_i.
\tag{L-91720.2}
\]

## 2. Opposite monotone profiles

Assume the vector row-per-target profile is nonincreasing in cone order:

\[
 \boxed{
 i<k
 \Longrightarrow
 \frac{r_i}{t_i}-\frac{r_k}{t_k}\in K.
 }
\tag{L-91720.3}
\]

Assume the score-per-target profile is nondecreasing:

\[
 \boxed{
 i<k
 \Longrightarrow
 \frac{s_i}{t_i}\le\frac{s_k}{t_k}.
 }
\tag{L-91720.4}
\]

Thus moving target mass left is simultaneously favorable for every physical
coordinate and favorable in the opposite direction for score cost.

## 3. Greedy Target-Lorenz removal

Let `c` be the unique cutoff index satisfying

\[
 \sum_{i<c}t_i<M\le\sum_{i\le c}t_i,
\]

with the evident endpoint conventions. Define `u^*` by

\[
 u_i^*=1\quad(i<c),
 \qquad
 u_c^*=\frac{M-\sum_{i<c}t_i}{t_c},
 \qquad
 u_i^*=0\quad(i>c).
\tag{L-91720.5}
\]

This is the leftmost Target-Lorenz submeasure.

## 4. Simultaneous vector extremality

For every exact-target removal `u` satisfying (L-91720.1),

\[
 \boxed{
 R(u^*)-R(u)\in K,
 }
\tag{L-91720.6}
\]

and

\[
 \boxed{
 S(u^*)\le S(u).
 }
\tag{L-91720.7}
\]

### Proof

Every feasible `u` can be converted into `u^*` by finitely many exchanges of
target mass from a later atom `k` to an earlier atom `i`. An exchange of target
mass `delta>=0` changes the physical vector by

\[
 \delta\left(\frac{r_i}{t_i}-\frac{r_k}{t_k}\right)\in K
\]

and changes score by

\[
 \delta\left(\frac{s_i}{t_i}-\frac{s_k}{t_k}\right)\le0.
\]

Iteration proves both assertions. Equivalently, apply every functional in the
dual cone `K^*` and use scalar fractional-knapsack duality; closedness of `K`
then recovers (L-91720.6).

The important point is simultaneity: no coordinate chooses its own source
submeasure.

## 5. Exact scalar dual certificates

Let `ell in K^*` and put

\[
 q_i=\frac{\ell(r_i)}{t_i}.
\]

By (L-91720.3), `q_i` is nonincreasing. With

\[
 \lambda_\ell=q_c,
\]

every exact-target removal obeys

\[
\boxed{
 \ell(R(u))
 \le
 \lambda_\ell M
 +\sum_{i<c}\bigl(\ell(r_i)-\lambda_\ell t_i\bigr)
 =\ell(R(u^*)).
}
\tag{L-91720.8}
\]

Indeed, after subtracting `lambda_ell M`, the coefficients are nonnegative to
the left of the cutoff and nonpositive to the right; use `u_i<=1` on the left
and `u_i>=0` on the right.

Similarly, with

\[
 h_i=\frac{s_i}{t_i},
 \qquad
 \lambda_S=h_c,
\]

every exact-target removal obeys

\[
\boxed{
 S(u)
 \ge
 \lambda_SM
 +\sum_{i<c}(s_i-\lambda_St_i)
 =S(u^*).
}
\tag{L-91720.9}
\]

Equations (L-91720.8)--(L-91720.9) are explicit dual certificates, not only an
existence theorem.

## 6. Complete primal-or-dual alternative

Let the odd source have physical demand `R_O` and score demand `S_O`, with
target `M=O_T`. Exactly one of the following outcomes is returned by the
greedy object.

### Primal certificate

If

\[
 \boxed{R(u^*)-R_O\in K}
\tag{L-91720.10}
\]

and

\[
 \boxed{S(u^*)\le S_O,}
\tag{L-91720.11}
\]

then `u^*` is one common-source certificate satisfying target, score and every
physical coordinate simultaneously.

For even source `E`, define the residual source

\[
 \nu=E-U^*.
\]

Then

\[
 T(\nu)=E_T-O_T,
\]

\[
 S(\nu)=E_S-S(U^*)\ge E_S-O_S,
\]

and

\[
 R(\nu)=E_R-R(U^*)\preceq_K E_R-O_R.
\tag{L-91720.12}
\]

The nonnegative physical bonus is exactly

\[
 B=R(U^*)-R_O\in K.
\tag{L-91720.13}
\]

### Dual separator

If (L-91720.10) fails, finite-dimensional cone separation gives an
`ell in K^*` with

\[
 \ell(R(u^*))<\ell(R_O).
\]

Then (L-91720.8) proves

\[
 \boxed{
 \ell(R(u))<\ell(R_O)
 \quad\text{for every exact-target common-source removal }u.
 }
\tag{L-91720.14}
\]

Thus the failed coordinate is an obstruction to the entire common-source
submeasure cone, not merely to the greedy ansatz. For a product cone, one may
take `ell` to be the failed coordinate projection.

If (L-91720.11) fails, (L-91720.9) proves

\[
 \boxed{
 S(u)>S_O
 \quad\text{for every exact-target common-source removal }u.
 }
\tag{L-91720.15}
\]

The score failure is likewise a complete separator.

## 7. `P_61` causal specialization

For a stopped `P_61` one-prime leaf, take the ordered even divisors and put

\[
 t_d=K_T(d),
\]

\[
 r_d=
 \bigl(K_R^{(2)}(d),\ldots,K_R^{(66)}(d)\bigr),
\]

\[
 s_d=K_S(d).
\]

`L-91682` proves, on the actual arithmetic source set for every real `p>=67`
and `1<=y<67`, that

\[
 d_1<d_2
 \Longrightarrow
 \frac{K_R^{(j)}(d_1)}{K_T(d_1)}
 \ge
 \frac{K_R^{(j)}(d_2)}{K_T(d_2)}
\]

for all `2<=j<=66`. `L-91684` proves that `K_S/K_T` is nondecreasing. Hence
the hypotheses of this theorem hold simultaneously in the complete 65-row
cone.

Consequently the Target-Lorenz object of `L-91684` is not merely one plausible
producer. It is the exact optimizer for the complete common-source problem:

\[
 \boxed{
 \mathfrak L_j(p,y)=R_j(U^*)-O_R^{(j)}\ge0
 \quad(2\le j\le66)
 }
\tag{L-91720.16}
\]

is necessary and sufficient for the existence of an exact-target even-source
submeasure satisfying every row inequality, while the already proved score
comparison is simultaneously optimal.

A negative value of `mathfrak L_j` automatically emits the exact dual bound
(L-91720.8) with

\[
 \lambda_j=\frac{K_R^{(j)}(c)}{K_T(c)}.
\tag{L-91720.17}
\]

No high-dimensional linear program is needed to decide this source cone.

## 8. Positive response consequence

When (L-91720.16) holds, the row bonus `B>=0` is one literal nonnegative row.
Every ordinary and radix-four response obtained from the resident positive row
maps is therefore subordinate in the same source coefficients. This conclusion
does not create or copy a boundary collar, mismatch packet, omission or common
port; those coordinates remain in the one-use root ledger.

## 9. Scope

This theorem completely solves the **optimization and duality** of the
common-source submeasure problem. It does not prove the arithmetic signs in
(L-91720.16), export the live collar/port allocation, or prove RH.

```text
common exact-target source cone                 EXACT
one simultaneous vector optimizer               EXACT
score minimum and all-row maximum               EXACT
explicit coordinate dual separators             EXACT
P_61 reduction to 65 Lorenz margins             EXACT FROM L-91682/L-91684
arithmetic nonnegativity of all margins          OPEN / RH-BEARING ROUTE
one-use root correction ledger                  SEPARATE LIVE EXPORT
Riemann Hypothesis                              UNPROVEN
```
