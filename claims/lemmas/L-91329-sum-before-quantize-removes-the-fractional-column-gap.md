# L-91329 — Sum before quantization removes the fractional-column gap

Claim ID: `L-91329`  
Status: **PROVED ABSTRACT POSITIVE-ASSEMBLY THEOREM; ROUGH SOURCE-PARTITION AUDIT REMAINS**  
Created: 2026-08-12  
Depends on: `L-90028`, `L-91110`, `L-91114`, `L-91115`, `L-91318`, `L-91324`, `R-91304`  
RH status: **unproved**

## 1. The incorrect order of operations

The blocked step in `L-91325` first quantizes every rough child, then evaluates
that finite packing at the generally noninteger column `Q/m`. Integer-column
feasibility does not justify the resulting inequality.

The correct order is

```text
positive continuum source partition;
positive target disintegration;
affine pushforward of every colored continuum measure;
sum all colors in the parent endpoint coordinate;
one positive quantization of the total measure;
one finite mismatch/collar repair at physical integer columns.
```

No finite child is ever tested at a fractional column.

## 2. Parent-coordinate source assembly

Let `lambda_0` be a finite positive endpoint measure in the parent coordinate.
For every branch `b`, let

\[
 m_b\in\mathbb Z_{\ge1}
\]

be its rough color and let `lambda_b` be a finite positive child endpoint
measure. Use the affine endpoint map

\[
 \boxed{
 \Phi_m(s)=m(s+1)-1.
 }
\tag{L-91329.1}

Define the parent pushforward

\[
 \boxed{
 \Lambda_b=m_b^{-1/2}(\Phi_{m_b})_\#\lambda_b
 }
\tag{L-91329.2}

and assume

\[
 \boxed{
 \Lambda=\lambda_0+\sum_b\Lambda_b
 }
\tag{L-91329.3}

is finite. All terms are positive, so the countable sum is unambiguous by
monotone convergence.

The factor `m_b^-1/2` is exactly the critical affine scaling of
`L-91318`.

## 3. Disintegrate the continuum target before discretizing

Let

\[
 K(y,dh)
\]

be the positive scale-free Markov kernel of `L-90028`, transporting the endpoint
block law to the capped-Gamma detail target. Attach the block source to every
endpoint measure and let

\[
 \mu=\mu_0+\sum_b\mu_b
\tag{L-91329.4}

be the corresponding positive source decomposition in the **parent**
coordinate. Define

\[
 \nu_b(B)=\int K(y,B)d\mu_b(y),
 \qquad
 \nu_0(B)=\int K(y,B)d\mu_0(y).
\]

Then

\[
 \boxed{
 \nu=\nu_0+\sum_b\nu_b
 }
\tag{L-91329.5}

exactly. Thus the physical continuum target is spent once, before any integer
row has been created.

Affine scale covariance is used only in constructing the parent measures
`Lambda_b`; it is not used to infer finite feasibility at `Q/m`.

## 4. One global martingale quantization

Let `mathcal Q` be the nearest-neighbor positive martingale B-spline
quantization of `L-91110`. It is a positive linear map on endpoint measures.
Therefore

\[
 \boxed{
 \mathcal Q\Lambda
 =\mathcal Q\lambda_0+
  \sum_b\mathcal Q\Lambda_b.
 }
\tag{L-91329.6}

Every endpoint coefficient on both sides is nonnegative. For every finite row,
physical integer column, radix-four detail column and entropy score, evaluation
of (L-91329.6) commutes with the sum.

The right side may still be *interpreted* as a colored decomposition, but the
actual packing is the single uncolored vector `mathcal Q Lambda`.

## 5. The finite correction is charged once

The discrepancy between the total continuum producer and `mathcal Q Lambda`
depends only on the total measure `Lambda`, not on a chosen decomposition.
Consequently the global safety scaling and fixed top omission of
`L-91114/L-91115` are applied once:

\[
 \boxed{
 d_X^{\rm fin}
 =\sigma_K\,\mathcal Q\Lambda
 \quad\text{with one fixed top omission}.
 }
\tag{L-91329.7}

If `Lambda` lies in the same bounded positive density corridor as the native
factor-54 producer, those theorems give

\[
 \sum_n d_X^{\rm fin}(n)\Xi_n(q)\le\Omega_X(q)
 \qquad(q\ge K)
\tag{L-91329.8}

at the physical integer columns. There is no branchwise safety factor and no
branchwise collar.

This is the exact sense in which target capacity is used once.

## 6. Score orientation

Linearity gives

\[
 \mathfrak S_{\rm cont}(\Lambda)
 =\mathfrak S_{\rm cont}(\lambda_0)
  +\sum_b\mathfrak S_{\rm cont}(\Lambda_b).
\tag{L-91329.9}

`L-91110` proves

\[
 \boxed{
 \mathfrak S(\mathcal Q\Lambda)
 \ge\mathfrak S_{\rm cont}(\Lambda).
 }
\tag{L-91329.10}

For a rough branch, `L-91318` proves that the affine finite row lift amplifies
entropy at least by the inverse of the critical coefficient. Hence the natural
`m_b^-1/2` branch scaling introduces no coefficient larger than one in the
score-loss recurrence.

The single global safety factor and top omission cost only the already certified
bounded amount.

## 7. Finite-tree and countable-tree versions

For a finite rough tree, (L-91329.3)--(L-91329.10) are finite linear identities.
For a countable least-prime tree, truncate after finitely many branches. All
source, target and endpoint measures increase monotonically, so monotone
convergence supplies the countable result whenever the total native measure is
finite.

No tensor product of scalar one-prime ports is used. The negative mixed-detail
counterexample `R-91303` is therefore irrelevant to this assembly.

## 8. Application boundary

The theorem repairs the fractional-column error of `L-91325`. To obtain a full
reset one must still verify, in the actual four-state/parity construction, the
load-bearing source identity

\[
 \boxed{
 \Lambda^{\rm native}
 =\lambda_0+\sum_b
   m_b^{-1/2}(\Phi_{m_b})_\#\lambda_b
 }
\tag{L-91329.11}

with no duplicated branch port and with the native bounded-density corridor.

`L-91317`, `L-91320`, `L-91322`, `L-91324`, `L-91327` and `L-91328` provide
positive local maps, unique least-prime labels, linear mass ledgers and local
parity projections. Writing their exact global endpoint-measure identity is now
the sole assembly task.

```text
abstract continuum target disintegration            EXACT
parent-coordinate affine pushforward                 EXACT
sum-before-quantize identity                          EXACT
one-use finite mismatch/collar correction             EXACT
fractional finite child feasibility                   NOT NEEDED
source-faithful global rough endpoint partition       OPEN / EXPLICIT
coefficient-one all-generation reset                  OPEN / RH-BEARING
Riemann Hypothesis                                    UNPROVEN
```
