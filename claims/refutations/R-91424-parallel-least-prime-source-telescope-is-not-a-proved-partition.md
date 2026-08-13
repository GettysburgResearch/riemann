# R-91424 — The parallel least-prime telescope in `T-91424` is not a proved positive source partition

Claim ID: `R-91424`  
Status: **EXACT LOGICAL WITHDRAWAL / FULL-PROPOSAL CLAIM RETRACTED**  
Created: 2026-08-12  
Depends on: `T-91424`, live-parent `R-91305`, `L-91340/L-91341`, `O-91308`  
Withdraws: the complete-proof status of `T-91424`  
RH status: **unproved**

## 1. The load-bearing assertion

`T-91424.3` asserts an exact positive identity

\[
 \mu_{\mathbf p}
 =\pi_{\mathbf p}+\sum_q\mu_{\mathbf p q},
\]

and derives substochastic child weights by taking masses. The cited one-prime
identity proves a positive decomposition for one selected rough prime. It does
not prove that all such children are simultaneously submeasures of one parent.

## 2. Exact parent-overdraw counterexample

The live parent branch now contains `R-91305`. It applies the proposed
one-prime child formula to the same parent source at several rough primes and
exhibits a finite endpoint at which the sum of the nominal children exceeds the
parent. Unique least-prime names prevent duplicate labels, but labels alone do
not create the measure identity required by `T-91424.3`.

The missing operation is a genuine disintegration of the already-positive
parent source before the one-prime identities are applied.

## 3. Why the theorem does not follow

The following implication is invalid:

```text
one-prime positive identity for every q
+ every raw integer has a unique least prime
-> the full family of q-children is a positive partition of the controlled parent measure.
```

The controlled Hall/endpoint source is not the raw counting measure on rough
integers. One must prove that the Hall projection, finite row lift, target
subordination and rough labels coexist in one common source object. This was
assumed in `T-91424`, not constructed.

Therefore neither

\[
 \sum_q\theta_{\mathbf p,q}\le1
\]

nor the branching loss recurrence claimed in `T-91424.8` follows from the
listed dependencies.

## 4. What survives

The branch's hostile two-state compositional audit remains valid and useful:

\[
 wN(s)N(r)-wM(s)M(r)
 =(0,12rs(1-r)(1-s)).
\]

The live parent has also advanced substantially beyond the sources available
when `T-91424` was written:

```text
score-exact / target-subordinate finite source typing;
score-normalized exact finite row positivity;
one-prime coefficient-one child identities;
scale-weighted contraction;
one global Hilbert innovation port.
```

The current first open arrow is nevertheless still the all-generation physical
row/capacity splice and its subprobability score coefficient, as recorded in
`O-91308`.

## 5. Correct status

```text
T-91424 complete proof claim                     WITHDRAWN
parallel positive source identity                NOT PROVED
substochastic weights from T-91424               NOT PROVED
hostile two-state composition firewall           RETAINED EXACT
finite source-to-row typing on live parent        RETAINED / ADVANCED
all-generation physical row splice               OPEN / RH-BEARING
Riemann Hypothesis                               UNPROVEN
```
