# R-91654 — The proposed root ledger conflates native allowances with realized packet responses

Claim ID: `R-91654`  
Status: **EXACT TYPE/SCOPE CORRECTION — ROOT COMPOSITION UNPROVED AS WRITTEN**  
Created: 2026-08-13  
Depends on: `L-91653`, `L-91658`, `L-91659`, `L-91660`, `L-91340`, `L-91341`, `L-91661`  
RH status: **unproved**

## 1. Two different kinds of coordinates

A native packing problem has **allowance coordinates**

\[
w_X(q)=q^{-1/2}\log(X/q),
\qquad
\Omega_X=D_4w_X,
\]

and a candidate row has **realized response coordinates**

\[
\Gamma_d(q)=\sum_nd(n)\beta_{nq},
\qquad
\Xi_d=D_4\Gamma_d.
\]

Feasibility is the pair of inequalities

\[
\boxed{
\Gamma_d\le w_X,
\qquad
\Xi_d\le\Omega_X.
}
\tag{R-91654.1}
\]

The allowance and response vectors are not interchangeable fields.

## 2. Incompatible datum signatures

`L-91658` declares a recursively transportable datum of the form

\[
(\ell,J,T,S,E,q,\Gamma,\Xi,b),
\tag{R-91654.2}
\]

where `T,S` are scalar SHARP target/declared-score coordinates and
`Gamma,Xi` are exact responses of `q`.

`L-91659` then declares the native root datum as

\[
(\ell,J,w,\Omega,q,\Gamma,\Xi,b),
\tag{R-91654.3}
\]

and writes

\[
w(\mathcal C_X)=w_X-w(\mathcal R_X),
\qquad
\Omega(\mathcal C_X)=\Omega_X-\Omega(\mathcal R_X).
\tag{R-91654.4}
\]

But the recursive datum in (R-91654.2) has no native allowance fields `w` or
`Omega`. Replacing its scalar `T,S` fields by the native vector allowances is
not a type-preserving operation.

## 3. Scalar target subordination is not vector capacity subordination

`L-91340` proves the scalar inequality

\[
T_{\rm residual}\le T_{\rm signed}
\]

for the SHARP target kernel `W_Psi`. `L-91341` proves that the same Hall
transport gives a nonnegative component row and hence nonnegative ordinary and
detail **responses**.

Neither statement proves

\[
\Gamma_{\rm residual}\le w_X
\quad\text{or}\quad
\Xi_{\rm residual}\le\Omega_X
\tag{R-91654.5}
\]

in every physical column. A scalar target inequality cannot be relabelled as a
coordinatewise allowance inequality.

The distinction is substantive, not cosmetic: `L-91661` gives an exact row
whose scalar/source properties are favorable and whose response is positive,
yet whose ordinary and detail responses strictly exceed the native allowances.

## 4. Correct complete datum

A complete recursive datum must retain both classes of coordinates, for example

\[
\boxed{
P=(\ell,J,T,S,E;\ w,\Omega;\ q,\Gamma,\Xi;\ b).
}
\tag{R-91654.6}
\]

Here:

```text
T,S,E          scalar benchmark/target/score data;
w,Omega        physical allowance vectors;
q,Gamma,Xi     candidate row and its exact responses;
b              child-owned boundary allowances.
```

Admissibility requires

\[
q\ge0,
\qquad
\Gamma\le w,
\qquad
\Xi\le\Omega,
\qquad
b_{\rm used}\le b.
\tag{R-91654.7}
\]

The multiplicative placement functor must scale **all** allowance and response
coordinates separately. An exact root identity must then be proved in each
field:

\[
\boxed{
\begin{aligned}
J_N&=J_C+\sum_bJ_b,\\
w_N&=w_C+\sum_bw_b,\\
\Omega_N&=\Omega_C+\sum_b\Omega_b,\\
q_N&=q_C+\sum_bq_b,\\
\Gamma_N&=\Gamma_C+\sum_b\Gamma_b,\\
\Xi_N&=\Xi_C+\sum_b\Xi_b,
\end{aligned}}
\tag{R-91654.8}
\]

with nonnegative current and child allowances. Only after (R-91654.8) and
(R-91654.7) are proved does subadditivity of the deficit apply.

## 5. Consequence for the live proposal

The algebraic coefficient identity and the subcritical child-mass estimate of
the provenance-causal route survive. The exact score bridge in `L-91660` also
survives for genuinely native-feasible rows.

What does not survive is the assertion that `L-91659` already supplies the
native root decomposition. Its displayed complement is not a proved identity
of the complete datum (R-91654.6), and its coordinate table cites scalar target
subordination where vector allowance subordination is required.

```text
coefficient/hazard budget                         RETAINED EXACT
same-index response scaling                       RETAINED EXACT
native deficit -> complete gap                    RETAINED EXACT
allowance/response distinction                    MANDATORY
L-91659 complete root datum identity              NOT WELL-TYPED AS WRITTEN
coordinatewise native allowance decomposition     OPEN / LOAD-BEARING
T-91651 unconditional composition                 UNPROVED
Riemann Hypothesis                                 UNPROVED
```
