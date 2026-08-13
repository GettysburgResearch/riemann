# L-91403 — Leafwise Hall projections sum exactly; no nonlinear commutation theorem is needed

Claim ID: `L-91403`  
Status: **PROVED EXACT POSITIVE-ASSEMBLY THEOREM**  
Created: 2026-08-13  
Depends on: paired source partition `L-91402`; no-upward Hall transports; interval-seed and component-row identities  
RH status: **unproved**

## 1. Disjoint terminal packets

Let a positive paired parity source be decomposed into source-disjoint terminal packets

\[
(E,O)=\sum_{\lambda\in\mathcal S}(E_\lambda,O_\lambda)
\]

by a least-prime stopping line. The equality is coefficientwise as positive measures.

Assume each packet lies in a finite reset window and admits a no-upward transport

\[
\pi_\lambda:O_\lambda\to E_\lambda,
\qquad e\le o.
\]

Let `E_\lambda^{\rm res}` be the unused even measure and let `I_\lambda>=0` be the interval seed associated with the matched edges. Then, exactly,

\[
\boxed{
E_\lambda-O_\lambda
=E_\lambda^{\rm res}-\Delta I_\lambda.
}
\tag{L-91403.1}
\]

## 2. Sum after projection

Summing (L-91403.1) over the stopping line gives

\[
\boxed{
E-O
=E^{\rm res}-\Delta I,
\qquad
E^{\rm res}=\sum_\lambda E_\lambda^{\rm res}\ge0,
\quad
I=\sum_\lambda I_\lambda\ge0.
}
\tag{L-91403.2}
\]

Thus the Hall selector need not commute with the source recursion. One may choose an arbitrary feasible Hall transport independently on every disjoint leaf and add the resulting positive packets.

No source or even capacity is used twice because the leaf measures are disjoint before transport.

## 3. Exact row assembly

Let `\mathcal R_X` denote any linear component-row map for which every no-upward edge satisfies the normalized monotonicity inequality used in the factor-54 row theorem. Applying the exact edge factorization leaf by leaf gives

\[
\mathcal R_X(E_\lambda-O_\lambda)\ge0
\]

coefficientwise. Therefore

\[
\boxed{
\mathcal R_X(E-O)
=\sum_\lambda\mathcal R_X(E_\lambda-O_\lambda)\ge0.
}
\tag{L-91403.3}
\]

The same identity holds before ordinary or radix-four carry evaluation. Since those evaluations are linear, the physical leaf outputs may be summed in the parent coordinate and quantized once.

## 4. Score

For one edge `e<=o`, the interval score is

\[
\log(o/e)\ge0.
\]

Hence every leaf correction is score-favorable and

\[
\boxed{
\operatorname{Score}(I)
=\sum_\lambda\operatorname{Score}(I_\lambda)\ge0.
}
\tag{L-91403.4}
\]

Any uniform finite collar or endpoint-port charge applied after summing leaves is paid once, not once per branch.

## 5. Two labelled SHARP channels

Apply the theorem separately to the balanced and reserve source labels. Their atomwise source measures are disjoint and sum exactly to the SHARP source. Therefore their terminal residual rows, interval packets, target shares and scores add exactly.

The heterogeneous-parameter counterexample does not apply because one Hall transport is never asked to mix demands from one parameter with capacities from the other.

## 6. Consequence

The open identity historically written as

\[
\mathcal P_a\left[\sum_\lambda P_\lambda\right]
=\sum_\lambda\mathcal P_a[P_\lambda]
\]

is unnecessary. Hall projection is nonlinear, but the **outputs of separately chosen leaf projections** satisfy the required linear identities by (L-91403.1)--(L-91403.4).

The remaining obligations are:

1. every stopped packet must fall in a certified no-upward Hall window;
2. the packet-level current/frontier and boundary charges must have one uniform mass bound;
3. the packet-envelope reset inequality must be verified.

## 7. Proof boundary

```text
source-disjoint leaf Hall projection             EXACT
sum of positive residual/interval packets         EXACT
component-row assembly                            EXACT GIVEN LOCAL MONOTONICITY
score-favorable global assembly                    EXACT
nonlinear Hall/tree commutation                    NOT NEEDED
uniform reset-window producer                      SEPARATE
packet-envelope recurrence                         AVAILABLE
Riemann Hypothesis                                 UNPROVED
```
