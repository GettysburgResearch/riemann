# L-93784 — The explicit typed leaves compile to one native-feasible common parent

Claim ID: `L-93784`  
Status: **PROPOSED COMPLETE COMMON-PARENT AND ALL-COLUMN COMPILER ON FROZEN FRAME ESTIMATES — REVIEW REQUIRED**  
Created: 2026-08-15  
Depends on: `L-91107`, `L-91110`, `L-91362`, `L-91650`, `L-91733`, `L-93602`, `L-93783`  
Replay: `X-93781-target-lorenz-typed-ledger`  
RH status: **unproved**

For integer `X>=10^12`, put

\[
K=\lfloor X/67\rfloor+1,
\qquad I_X=[K+2,X-10002],
\]

and retain the frozen positive endpoint-frame measure

\[
d\mu_X(s)=\frac{2L(X/s)}s\,ds.
\tag{L-93784.1}
\]

## 1. Concrete common parent

Let `L_(X,s)` be the exact finite stopped-leaf set, including the labels in
`L-93783.1`, and let `omega_(s,l)>=0` be the product of the literal stopping and
causal path coefficients. Define the typed common parent

\[
\boxed{
\mathcal P_X^{TL}
=
\int_{I_X}
\sum_{\ell\in\mathscr L_{X,s}}
\omega_{s,\ell}
(\nu_{s,\ell};B_{s,\ell};\sigma_{s,\ell})
\,d\mu_X(s).
}
\tag{L-93784.2}
\]

Every term in (L-93784.2) is explicit:

```text
leaf source nu             E minus the literal cutoff coefficients;
leaf row bonus B           R(U)-R(O), current-only and nonnegative;
score surplus sigma        S(O)-S(U);
path weight omega          product of frozen nonnegative causal coefficients;
owner                      the complete label (n,h,i,d,epsilon,c).
```

By (L-93783.9)--(L-93783.11), substitution into the frozen stopped-tree
identity gives, before finite endpoint observation, the exact signed native
marginals in target, declared score and every physical row. This derives the
actual row marginal; it does not merely name a coupling with the desired
marginals.

All actual rough-child rows are already labelled leaves inside
`P_X^TL`. They remain internal colours of the one final row. The exported
recursive family is empty.

## 2. Positive operations performed once

Perform, in this order:

1. omit the literal bottom and top strips as unused positive source;
2. multiply the complete common parent by
   \[
   \tau_K=\frac{\sqrt K}{\sqrt K+130};
   \]
3. push every retained label to the parent endpoint coordinate;
4. apply one label-blind positive martingale B-spline quantizer;
5. sum every labelled physical row.

The resulting finite row `d_X` is coefficientwise nonnegative. No leaf or
child receives a second Hall map, quantizer, collar, omission, comparison,
base correction or port.

## 3. Separate signed observation ledger

Let `e_X(q)` be the complete retained-cell, intrinsic-collar and finite
observation excess in the radix-four coordinate. It is a signed numerical
vector, not an element of the positive source ledger. The frozen all-column
theorem gives, for every nonterminal `q>=2`, including `2<=q<K`,

\[
\frac{|e_X(q)|}{\Omega_X(q)}<\frac{129}{\sqrt K}.
\tag{L-93784.3}
\]

Therefore

\[
\Xi_{d_X}(q)
<\tau_K\left(1+\frac{129}{\sqrt K}\right)\Omega_X(q)
=
\frac{\sqrt K+129}{\sqrt K+130}\Omega_X(q)
<\Omega_X(q).
\tag{L-93784.4}
\]

The frozen terminal comparison is paid by the one positive top omission and
leaves

\[
(5033-4452)X^{-3/2}=581X^{-3/2}>0.
\tag{L-93784.5}
\]

Above the retained support the response vanishes. Hence

\[
\boxed{\Xi_{d_X}(q)\le\Omega_X(q)\quad(q\ge2).}
\tag{L-93784.6}
\]

Positive radix-four inversion gives simultaneously

\[
\boxed{C_{d_X}(q)\le w_X(q).}
\tag{L-93784.7}
\]

Only after (L-93784.6) is proved define the native numerical complement

\[
r_X=\Omega_X-\Xi_{d_X}\ge0.
\tag{L-93784.8}
\]

`r_X` is not claimed to be a positive arithmetic source packet.

## 4. Port and ownership disposition

The declared operation list contains no coloured state completion or Schur
realization. Consequently

\[
D_X^{port}=P_X^{port}=0.
\]

Every source occurrence has one leaf owner, every current-only bonus has one
leaf owner, signed observations have no source owner because they are not
source, and no full child capacity is reserved or exported.
