# L-91736 — Actual-mass children obey an exact native-slack cocycle, and the distinguished root closes against the positive causal envelope

Claim ID: `L-91736`
Status: **PROVED EXACT ALGEBRAIC ROOT-TO-CAUSAL COMPOSITION / FROZEN ROOT INPUT REQUIRED**
Created: 2026-08-15
Depends on: `L-91378`, `L-91658`, `L-91732`, `L-91735`, `L-91737`, the positive causal packet envelope `T-91312/T-91305`
Refines: `L-19882` by separating the one-time native root cost from the hereditary positive causal consumer
RH status: **unproved**

## 1. Exact one-use native root identity

Let `P_X` be the distinguished native root packet at endpoint `X`, with native
detail capacity vector `Omega_X(P_X)`.  After the audited factor-67 root
realization, suppose the complete current row, full child capacities and unused
root detail satisfy

\[
 \boxed{
 \Omega_X(P_X)
 =\Xi_X(d_X^{\rm cur})+r_X+
  \sum_b\beta_bU_b
  \Omega_{Y_b}(\widetilde P_b),
 \qquad
 r_X\ge0.
 }
\tag{L-91736.1}
\]

Here the children may be presented either in the aggregate global-list form of
`L-91732.5--.8` or in the optional actual-mass normalized form

\[
 m(\widetilde P_b)=M_X:=m(P_X),
 \qquad
 \sum_b\beta_b<\frac18,
 \qquad
 Y_b\le X/67+C_0.
\tag{L-91736.2}
\]

Equation (L-91736.1) is the exact algebraic form of one-use native packing.  It
must be reconstructed from the frozen source/current/full-child realization;
it is not implied merely by a scalar score estimate.

## 2. Insert arbitrary feasible child rows

Let `d_b` be any feasible row for `\widetilde P_b`, and put

\[
 s_b=
 \Omega_{Y_b}(\widetilde P_b)-
 \Xi_{Y_b}(d_b)\ge0.
\]

Define

\[
 d_X=d_X^{\rm cur}+
 \sum_b\beta_bU_bd_b.
\tag{L-91736.3}
\]

Linearity and (L-91736.1) give

\[
 \boxed{
 s_X(P_X;d_X)
 =r_X+
  \sum_b\beta_bU_bs_b\ge0.
 }
\tag{L-91736.4}
\]

Thus native feasibility is hereditary once the full child capacities have been
reserved exactly once.

## 3. Exact scalar native cocycle

Normalized same-index placement changes endpoint and provenance labels but not
the numerical detail coordinates.  Therefore

\[
 \langle Y_4,U_bs\rangle
 =\langle Y_4,s\rangle.
\tag{L-91736.5}
\]

Put

\[
 \delta_{\rm root}(X)=
 \langle Y_4,r_X\rangle.
\]

Pairing (L-91736.4) with `Y_4` gives

\[
 \boxed{
 \Delta_X(P_X;d_X)
 =\delta_{\rm root}(X)+
  \sum_b\beta_b
  \Delta_{Y_b}(\widetilde P_b;d_b),
 }
\tag{L-91736.6}
\]

where, by `L-91378`,

\[
 \Delta_X(P_X;d_X)
 =J_\Lambda(X)-\mathcal H(d_X).
\tag{L-91736.7}
\]

No continuum benchmark occurs in the cocycle.

## 4. The children use the positive causal envelope, not a second root realization

After the native signed packet has entered the positive typed cone, the
hereditary operation is the exact causal reset of `L-91650`, with current debt
bounded by `L-91375`.  Let

\[
 \Lambda_+(Y)
 =\sup_{Z\le Y}
  \sup_{m(P)=1}
  \Delta_Z(P)
\]

on this positive causal packet class.  The frozen consumer `T-91312` (or its
measure-valued form `T-91305`) gives one absolute bound

\[
 \boxed{\Lambda_+(Y)\le C_+}
\tag{L-91736.8}
\]

once the positive causal identity and source ownership are reconstructed.  The
coarse theorem value may be taken from the `2m` current debt and the strict
one-eighth child contraction; its optimization is irrelevant here.

This is load-bearing: the endpoint-frame mismatch, knot refinement and root
port are not re-applied independently to every normalized child.  Those are
one-time native-root operations.

## 5. Bound the complete child contribution

Using the actual-mass normalization in (L-91736.2),

\[
\begin{aligned}
 \sum_b\beta_b
  \Delta_{Y_b}(\widetilde P_b)
 &\le C_+M_X\sum_b\beta_b\\
 &<\frac18C_+M_X.
\end{aligned}
\tag{L-91736.9}
\]

Equivalently, in the measure-valued form,

\[
 \sum_b\Delta(R_b)
 \le C_+\sum_bm(R_b)
 \le C_+\rho M_X.
\]

`L-91737` proves the physical target-mass bound

\[
 M_X<3020.
\tag{L-91736.10}
\]

This bound is derived from the actual factor-67 endpoint measure and target
coordinate; it does not confuse the historical certificate-count bound `54`
with physical target mass.  Hence the entire child term in (L-91736.6) is
`O(1)`.

## 6. Distinguished-root native bound

`L-91735` gives

\[
 \delta_{\rm root}(X)
 \le4\log X+C_{\rm root}.
\tag{L-91736.11}
\]

Combining (L-91736.6), (L-91736.9), (L-91736.10) and the root mass bound yields

\[
 \boxed{
 \Delta_X(P_X;d_X)
 \le4\log X+C_{\rm root}+
      \frac{3020}{8}C_+
 =O(\log X)
 =o(\log^2X).
 }
\tag{L-91736.12}
\]

There is no recurrence which repeatedly charges the root endpoint-frame cost to
arbitrary mass-one children.  The only recursive envelope is the already
subcritical positive causal packet envelope.

## 7. Endpoint consumer

Equation (L-91736.12) has the exact sign and normalization consumed by
`T-91313`.  If the frozen root Hall/profile theorem, endpoint-frame source
realization, retained-cell correction, terminal packet, narrow port,
full-child identity (L-91736.1), positive causal envelope and one-sided endpoint
consumer are independently reconstructed at their locked blobs, the resident
consumer gives the proposed implication to RH.

```text
actual aggregate/normalized children                 L-91732
full-child/current/root-slack identity               frozen root producer input
native slack vector cocycle                          exact
Y4 scalar cocycle                                    exact
positive child deficit envelope                      O(1) per target mass
one-time distinguished root cost                     <=4 log(X)+C
retained physical target mass                        <3020 / L-91737
complete distinguished native deficit                O(log X)
4sqrt(X)-H(d_X)=O(1)                                 not used / false as written
Riemann Hypothesis                                   unproved
```
