# L-91686 — The target-Lorenz cutoff is the exact simultaneous box-LP optimum

Claim ID: `L-91686`  
Status: **PROVED EXACT FINITE-LP REDUCTION**  
Created: 2026-08-14  
Frozen arithmetic inputs: PR `#467` at `d5e03a3a63bd05b43abf4b5e37905f86e9ec59d6`  
Depends on: the monotone score/target and row/target profiles in `L-91682`  
Replay: `X-91686-native-root-compiler-separator`  
RH status: **unproved**

## 1. Ordered box LP

Let ordered source atoms be indexed by

\[
1<2<\cdots<n.
\]

For each atom let

\[
a_i\ge0,
\qquad t_i>0,
\qquad s_i,
\qquad r_{j,i}
\]

be its available coefficient, target, score, and row-`j` response. Consider

\[
0\le u_i\le a_i,
\qquad
\sum_i t_i u_i=M.
\tag{L-91686.1}
\]

Assume

\[
\sigma_i:=\frac{s_i}{t_i}
\quad\text{is nondecreasing in }i,
\tag{L-91686.2}
\]

and, for every retained row `j`,

\[
\rho_{j,i}:=\frac{r_{j,i}}{t_i}
\quad\text{is nonincreasing in }i.
\tag{L-91686.3}
\]

Let `u*` be the left-greedy target fill: saturate atoms from the left until the target mass `M` is reached, with at most one fractional cutoff atom.

## 2. Exact score minimum

Let `k` be the cutoff and put `lambda_S=sigma_k`. For any feasible `u`,

\[
S(u)-\lambda_S M
=
\sum_i t_i(\sigma_i-\lambda_S)u_i.
\]

For `i<k` the coefficient is nonpositive and `u_i<=a_i`; for `i>k` it is nonnegative and `u_i>=0`. Therefore

\[
\begin{aligned}
S(u)-\lambda_S M
&\ge
\sum_{i<k}t_i(\sigma_i-\lambda_S)a_i\\
&=S(u^*)-\lambda_S M.
\end{aligned}
\]

Hence

\[
\boxed{S(u)\ge S(u^*).}
\tag{L-91686.4}
\]

The leftmost target fill is the exact score-minimizing basis of the full box LP.

## 3. Exact simultaneous row maximum

For a fixed row `j`, let `lambda_j=rho_{j,k}`. Then

\[
R_j(u)-\lambda_jM
=
\sum_i t_i(\rho_{j,i}-\lambda_j)u_i.
\]

For `i<k` the coefficient is nonnegative and `u_i<=a_i`; for `i>k` it is nonpositive and `u_i>=0`. Thus

\[
\begin{aligned}
R_j(u)-\lambda_jM
&\le
\sum_{i<k}t_i(\rho_{j,i}-\lambda_j)a_i\\
&=R_j(u^*)-\lambda_jM.
\end{aligned}
\]

Therefore, simultaneously for every retained row,

\[
\boxed{R_j(u)\le R_j(u^*).}
\tag{L-91686.5}
\]

## 4. Exact feasibility equivalence and Farkas separators

Consider the stopped-leaf program

\[
T(U)=T(O),
\qquad
S(U)\le S(O),
\qquad
R_j(U)\ge R_j(O)
\quad\text{for all }j.
\tag{L-91686.6}
\]

Under (L-91686.2)--(L-91686.3), this program is feasible if and only if the leftmost target fill `U*` satisfies all displayed inequalities.

Indeed:

- if `S(U*)>S(O)`, then (L-91686.4) rules out every feasible `U`;
- if `R_j(U*)<R_j(O)` for one row, then (L-91686.5) rules out every feasible `U`;
- if all inequalities hold at `U*`, then `U*` itself is feasible.

The threshold inequalities are exact dual certificates. For example, if

\[
R_j(O)>R_j(U^*),
\]

then every box-feasible `U` obeys

\[
R_j(U)-\lambda_jT(U)
\le
\sum_{i<k}t_i(\rho_{j,i}-\lambda_j)a_i,
\tag{L-91686.7}
\]

while `O` lies strictly above the right side after using `T(U)=T(O)`. This is an explicit Farkas separator. The score failure has the analogous reversed inequality.

## 5. Application to the live `P_61` stopped-leaf LP

On PR `#467`, order the even `P_61` divisor atoms by increasing divisor. `L-91682` proves:

\[
\frac{K_S(d)}{K_T(d)}
\quad\text{increases with }d,
\]

and, for every row `2<=j<=66`,

\[
\frac{K_R^{(j)}(d)}{K_T(d)}
\quad\text{decreases with }d.
\]

Therefore the target-Lorenz producer of `L-91684` is not a heuristic restriction. It is the exact common optimal basis for the complete finite box LP requested by the reviewer.

No non-leftmost basis can repair a negative margin

\[
\mathfrak L_j(p,y)=R_j(U^*)-O_R^{(j)}.
\]

A negative directed interval for one such margin is already an exact separator for the full LP.

## 6. Hostile-leaf directed probe

The companion replay reconstructs the historically hostile point

\[
p=67,
\qquad y=13,
\qquad j=66.
\]

The exact target cutoff is the even divisor `123`, with directed fractional fill

\[
0.283843792756777528\ldots
\]

and every row-66-active divisor is at most `13`, hence fully before the cutoff. The directed optimal row margin is

\[
\boxed{
\mathfrak L_{66}(67,13)
>
0.0083815482754633380.
}
\tag{L-91686.8}
\]

This closes that one hostile cell. It does not certify all remaining activation cells.

## 7. Exact boundary

The theorem removes arbitrary basis discovery from the stopped-leaf campaign. The remaining arithmetic work is now deterministic:

```text
enumerate the 185 possible target cutoffs below 2000;
partition the (p,y)-plane by activation and cutoff cells;
certify the leftmost-basis row margins by directed intervals;
return the threshold dual immediately on any negative cell.
```

Ordinary/detail subordination follows only after a nonnegative row bonus is assembled through the frozen response map. Shared boundary-port ownership and the global native-root realization remain separate obligations.

```text
leftmost target cutoff as score optimum       EXACT
leftmost target cutoff as all-row optimum     EXACT
full stopped-leaf box LP equivalence          EXACT
hostile p=67,y=13,row=66 cell                 DIRECTED POSITIVE
all remaining activation cells               OPEN / FINITE-DIRECTED
ports and global root provenance              OPEN
Riemann Hypothesis                            UNPROVEN
```
