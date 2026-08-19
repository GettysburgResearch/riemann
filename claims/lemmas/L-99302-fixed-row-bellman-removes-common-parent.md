# L-99302 — Fixed-row Bellman projection removes the common-parent requirement

Claim ID: `L-99302`  
Status: **PROVED ABSTRACT FINITE-DAG THEOREM / APPLICATION REQUIRES THE LOCAL SCALAR LEDGER**  
Created: 2026-08-20  
RH status: not assumed

## 1. Setting

Fix one physical component row `j`. For a finite scale DAG, let `v` denote a
typed quotient state and let `c_v(j)` be its canonical signed row value.
Assume the exact local cumulative-Hall and causal algebra has the scalar form

\[
\boxed{
 c_v(j)=J_v(j)+\sum_{w\succ v}a_{vw}c_w(j)+C_v(j),
}
\tag{L-99302.1}
\]

where

\[
J_v(j)\ge0,
\qquad a_{vw}\ge0,
\qquad \sum_{w\succ v}a_{vw}\le\kappa<1.
\tag{L-99302.2}
\]

For the factor-67 packet one may take

\[
\kappa<67^{-1/2}<1/8.
\tag{L-99302.3}
\]

Here `J_v` contains the cumulative compact-Hall residual row, the nonnegative
Hall edge bonus and every current-owned causal difference. Only the positive
`alpha` child coefficients occur among the `a_vw`. The signed term `C_v` is
the finite/continuum, knot, anchor or realization calibration left outside the
positive row.

No common source measure is assumed in this theorem.

## 2. Positive scalar Bellman witness

Define recursively from the terminal states upward

\[
\boxed{
 D_v(j)=J_v(j)+\sum_{w\succ v}a_{vw}D_w(j).
}
\tag{L-99302.4}

Because the DAG is finite and every coefficient is nonnegative,

\[
\boxed{D_v(j)\ge0\quad\text{for every state }v.}
\tag{L-99302.5}

Let

\[
E_v(j)=c_v(j)-D_v(j).
\]

Subtracting (L-99302.4) from (L-99302.1) gives the exact defect recursion

\[
\boxed{
 E_v(j)=C_v(j)+\sum_{w\succ v}a_{vw}E_w(j).
}
\tag{L-99302.6}

Thus the positive surrogate and its signed calibration are separated before
any source-ownership or cross-coordinate question arises.

## 3. Uniform defect estimate

If

\[
|C_v(j)|\le B_j
\tag{L-99302.7}
\]

uniformly in the state and root endpoint, backward induction gives

\[
\boxed{
 |E_v(j)|\le \frac{B_j}{1-\kappa}.
}
\tag{L-99302.8}

Indeed, truncating at depth `N` gives

\[
|E_v(j)|
\le B_j\sum_{r=0}^{N}\kappa^r,
\]

and the finite depth permits passage to the geometric bound. For factor 67,

\[
|E_v(j)|<\frac87B_j.
\tag{L-99302.9}
\]

This bound uses neither a global root-source mass nor a literal disintegration
of one parent packet.

## 4. Why physical common-parent ownership is unnecessary here

The original all-coordinate construction required one physical source to carry
simultaneously target, score, every ordinary/detail capacity and all child
labels. The fixed-row Mellin consumer asks only for one nonnegative scalar
function of `X`.

Accordingly:

* the cumulative Hall flow may be chosen independently at each finite state;
* no monotone selection in the endpoint parameter is required;
* no random-key partition is required;
* no first-owner source disintegration is required;
* no common coupling across different physical coordinates is required.

A canonical measurable choice is available: on the finite Ferrers Hall graph,
process odd vertices in increasing order and fill eligible even capacities in
increasing order. This greedy flow is a finite composition of `min`, addition
and subtraction, hence is Borel measurable in the cumulative capacities.

The Hall and causal identities remain exact after applying the single linear
row observation. Therefore independent cumulative choices define the scalar
`J_v(j)` needed in (L-99302.1), even though they need not be restrictions of one
endpoint-nested source.

## 5. Exact application boundary

This theorem proves that the following interfaces are not needed by the
fixed-row route:

```text
pointwise endpoint-density Hall
endpoint-nested Hall residual measure
literal common-parent random-key partition
all-coordinate cone-valued ownership
```

The repository-specific obligation is reduced to one local scalar identity:
verify (L-99302.1) in the actual component row, including the same-index child
observation and the explicit signed calibration `C_v(j)`. Once that identity
and a fixed-row bound for `C_v` are established, the positive Bellman witness
is automatic.
