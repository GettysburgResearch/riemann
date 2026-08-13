# L-91662 — A coordinatewise allowance decomposition with subcritical children gives a bounded native deficit

Claim ID: `L-91662`  
Status: **PROVED EXACT ABSTRACT CONSUMER**  
Created: 2026-08-13  
Depends on: `L-91658`, `L-91660`, `R-91654`  
RH status: **conditional on one explicit allowance-aware producer theorem**

## 1. Complete allowance-aware datum

Let a physical endpoint datum be

\[
P=(\ell,J,T,S,E;\ w,\Omega;\ q,\Gamma,\Xi;\ b),
\tag{L-91662.1}
\]

with all coordinates additive and positively homogeneous. The vectors
`w,Omega,b` are physical allowances. The vectors `q,Gamma,Xi` are a candidate
row and its exact responses.

Let `F(P)` be the cone of nonnegative rows `d` satisfying every ordinary,
radix-four and boundary inequality owned by `P`, and define

\[
\Delta(P)=J(P)-\sup_{d\in F(P)}\operatorname{Score}(d).
\tag{L-91662.2}
\]

No sign is imposed on `J`; only the physical allowance and row coordinates are
required to be admissible.

## 2. Exact datum decomposition

Suppose

\[
\boxed{
P_X=C_X+\sum_{i=1}^kc_iU_iP_{Y_i}
}
\tag{L-91662.3}
\]

is an identity in **every coordinate** of (L-91662.1), with

\[
c_i\ge0,
\qquad
Y_i\le cX+C_0,
\qquad
0<c<1.
\tag{L-91662.4}
\]

In particular,

\[
\begin{aligned}
w_X&=w_C+\sum_ic_iU_iw_{Y_i},\\
\Omega_X&=\Omega_C+\sum_ic_iU_i\Omega_{Y_i},\\
b_X&=b_C+\sum_ic_iU_ib_{Y_i}.
\end{aligned}
\tag{L-91662.5}
\]

Assume every allowance on the right of (L-91662.5) is nonnegative. Let the
placement functor carry arbitrary child-feasible rows to parent rows while
scaling their responses and score by the same coefficient, as in `L-91658`.

Assume also that there is one current feasible row

\[
d_C\in F(C_X)
\]

with

\[
\boxed{
J(C_X)-\operatorname{Score}(d_C)\le A.
}
\tag{L-91662.6}
\]

## 3. Deficit inequality

Choose arbitrary child rows `d_i in F(P_(Y_i))`. By (L-91662.5) and exact
placement covariance,

\[
d_C+\sum_ic_iU_id_i\in F(P_X).
\tag{L-91662.7}
\]

Additivity of the benchmark and score gives

\[
\begin{aligned}
J(P_X)-\operatorname{Score}
\left(d_C+\sum_ic_iU_id_i\right)
={}&J(C_X)-\operatorname{Score}(d_C)\\
&+\sum_ic_i
 [J(P_{Y_i})-\operatorname{Score}(d_i)].
\end{aligned}
\]

Taking child suprema yields

\[
\boxed{
\Delta(P_X)
\le A+\sum_ic_i\Delta(P_{Y_i}).
}
\tag{L-91662.8}
\]

This is the packet-envelope inequality with the missing allowance hypotheses
made explicit.

## 4. Subcritical envelope

Let

\[
\Lambda(X)=\sup\Delta_+(P_Y)
\]

over the declared mass-one packet family and all `Y<=X`. If

\[
\sum_ic_i\le\rho<1,
\tag{L-91662.9}
\]

then (L-91662.8) gives

\[
\boxed{
\Lambda(X)
\le A+\rho\Lambda(cX+C_0).
}
\tag{L-91662.10}
\]

Iteration terminates at a fixed compact base and gives

\[
\boxed{
\Lambda(X)\le\frac{A}{1-\rho}+O(1)=O(1).
}
\tag{L-91662.11}
\]

For the live causal coefficient budget,

\[
\rho<1/8,
\]

so

\[
\Lambda(X)<\frac87A+O(1).
\tag{L-91662.12}
\]

## 5. Root certificate of bounded mass

Suppose the native root has one current datum of debt at most `A_root` plus a
positive certificate of coefficient mass at most `M`, and every mass-one
certificate obeys the subcritical reset above. Homogeneity gives

\[
\boxed{
\Delta(\mathcal N_X)
\le A_{\rm root}+
M\left(\frac{A}{1-\rho}+O(1)\right)
=O(1).
}
\tag{L-91662.13}
\]

The proposed factor-54 ledger has `M<=54` and `rho<1/8`; those constants are
more than sufficient. No logarithmic accumulation is needed.

## 6. Endpoint consequence

For a genuinely native-feasible datum, `L-91660` gives

\[
F_\Lambda(X)\le\Delta(\mathcal N_X).
\]

Therefore (L-91662.13) implies

\[
F_\Lambda(X)=O(1)=o(\log^2X),
\]

and the frozen endpoint consumer implies RH.

The only conclusion-producing producer obligation is now the complete
coordinatewise identity (L-91662.3)--(L-91662.6). Scalar target
subordination or response positivity alone is not enough.

```text
allowance-aware subadditivity                 EXACT
subcritical envelope                          EXACT
rho<1/8 gives O(1) deficit                    EXACT
bounded root certificate mass                 SUFFICIENT
native O(1) deficit -> RH                     FROZEN CONSUMER
coordinatewise native producer                OPEN / SOLE GATE
Riemann Hypothesis                             CONDITIONAL / UNPROVED
```
