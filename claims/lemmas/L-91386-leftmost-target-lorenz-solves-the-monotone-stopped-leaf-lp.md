# L-91386 — The leftmost target fill simultaneously solves the monotone stopped-leaf LP

Claim ID: `L-91386`  
Status: **PROVED EXACT FINITE-DIMENSIONAL OPTIMIZER THEOREM**  
Created: 2026-08-14  
Primary input: the score/target and row/target divisor orders of `L-91682`  
RH status: **unproved**

## 1. Abstract source LP

Let

\[
e_1<e_2<\cdots<e_N
\]

be the ordered even source nodes. Give node \(e_i\) available source mass
\(a_i\ge0\) and positive target density \(T_i>0\). Let \(M\) be the complete odd
target demand, with

\[
0\le M\le\sum_i a_iT_i.
\]

Consider positive submeasures \(u=(u_i)\) satisfying

\[
0\le u_i\le a_i,
\qquad
\sum_i u_iT_i=M.
\tag{L-91386.1}
\]

Let \(\sigma_i=S_i/T_i\) be nondecreasing in \(i\), and let every
row-per-target profile \(\rho_i^{(j)}=R_i^{(j)}/T_i\) be nonincreasing in \(i\).

## 2. Leftmost target fill

Define \(u^*\) by filling source capacity from the smallest node until target
mass \(M\) is reached:

```text
u_i^*=a_i for i<c;
0<=u_c^*<=a_c;
u_i^*=0 for i>c.
```

The cutoff \(c\) and the possible fractional last coefficient are uniquely
determined up to zero-target degeneracies.

## 3. Exchange proof

Suppose \(i<j\), \(u_i<a_i\) and \(u_j>0\). Move target mass
\(\varepsilon>0\) from \(j\) to \(i\):

\[
u_i\mapsto u_i+\frac{\varepsilon}{T_i},
\qquad
u_j\mapsto u_j-\frac{\varepsilon}{T_j}.
\]

The target equality is unchanged. For every row,

\[
\Delta R^{(j)}
=
\varepsilon\bigl(\rho_i^{(j)}-\rho_j^{(j)}\bigr)\ge0,
\]

while

\[
\Delta S
=
\varepsilon(\sigma_i-\sigma_j)\le0.
\]

Iterating exchanges terminates at \(u^*\). Therefore

\[
\boxed{
S(u^*)=\min\{S(u):(L\text{-}91386.1)\},
}
\tag{L-91386.2}
\]

and, simultaneously for every row coordinate,

\[
\boxed{
R^{(j)}(u^*)=\max\{R^{(j)}(u):(L\text{-}91386.1)\}.
}
\tag{L-91386.3}
\]

No row-dependent basis selection is required.

## 4. Exact live stopped-leaf consequence

For the actual \(P_{61}\) stopped-leaf packet, `L-91682` proves on the complete
arithmetic source set that

\[
d_1<d_2
\Longrightarrow
\frac{K_R^{(j)}(d_1)}{K_T(d_1)}
\ge
\frac{K_R^{(j)}(d_2)}{K_T(d_2)}
\]

for every \(2\le j\le66\), and that \(K_S/K_T\) increases in divisor order.
Thus the live LP

\[
0\le u_e\le a_e,
\]

\[
T(U)=T(O),
\qquad
S(U)\le S(O),
\qquad
R_j(U)\ge R_j(O)\quad(2\le j\le66)
\tag{L-91386.4}
\]

has the following fail-closed reduction.

* If the leftmost target fill \(U^*\) satisfies every row inequality, it is a
  simultaneous feasible solution. Its score is no larger than the score of any
  target-exact even submeasure; the existing score-feasible source comparison
  therefore gives \(S(U^*)\le S(O)\).

* If \(R_j(U^*)<R_j(O)\) for one row, then no feasible \(U\) exists. The failed
  row functional is an exact separating certificate because `L-91386.3` says
  \(U^*\) is the maximum possible value of that row under the target equation.

Hence an unrestricted LP cannot outperform the leftmost target-Lorenz basis on
the declared monotone generator cone. A failed row is a genuine Farkas
separator, not evidence that another basis should be searched.

## 5. Scope

The theorem proves the optimizer structure. It does not prove the remaining
arithmetic signs

\[
R_j(U^*)-R_j(O)\ge0.
\]

Those signs form the finite-cell campaign of `L-91387`.

```text
leftmost target fill                      EXACT OPTIMIZER
simultaneous score and all-row optimality EXACT
live LP basis search                      REMOVED
leftmost row inequalities                 OPEN / FINITE-CELL
Riemann Hypothesis                        UNPROVED
```
