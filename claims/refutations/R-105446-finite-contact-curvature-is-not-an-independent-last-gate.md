# R-105446 — Finite contact curvature is not an independent last gate

Claim ID: `R-105446`  
Status: **BINDING FRONTIER CORRECTION**  
Created: 2026-08-24  
Depends on: `L-105442--L-105446`  
RH status: **unproved**

## 1. The former candidate

`L-105443` introduced the exact identity

\[
\partial_b\mathcal Q_{r,b}
={2\over3}
\left[2\Re\mathcal R_r(z_1)-\Re\mathcal R_r(z_2)-1\right]
\]

and proposed `ACCR105443`, a strict adjacent-ratio inequality at every finite
first zero contact.

The identity remains correct and useful. The proposed contact theorem is not a
separate conclusion-facing obligation.

## 2. Why no finite smooth first contact exists

The infinitesimal field

\[
\mathcal C_{r,b}
={1\over2}[h\partial_h\Im m_r-\Im m_r]
\]

satisfies the uniformly elliptic equation

\[
\partial_a^2\mathcal C
+
\partial_h^2\mathcal C
-{2\over h}\partial_h\mathcal C=0.
\]

By `L-105446`, `mathcal C<=0` cannot attain zero at a finite interior point
while the ratio is holomorphic: the strong maximum principle would make the
field identically zero, contradicting the strict Xi anchor

\[
\mathcal C_{r,b}(0,h)<0.
\]

The same conclusion is visible after dividing by `h^3`, when the field becomes
an ordinary axisymmetric harmonic function in six dimensions.

Thus an argument designed only to orient a finite smooth zero contact solves a
mechanism which cannot be the first global failure.

## 3. Correct obstruction list

The zero-height variational formula and `beta_(r+1)<=beta_r` leave only:

```text
zero-height injection at a parent zero or positive critical charge;
a co-terminal denominator pole;
spatial escape |a|->infinity when the supremal height is not attained.
```

The coarse scale is already strictly negative. A pole cannot arrive at a base
strictly above the parent-zero height. Consequently the normative analytic
obstruction is a zero-height event, possibly escaping to infinity.

## 4. Disposition of ACCR105443

```text
adjacent-ratio differential identity      RETAINED / EXACT
finite-contact inequality ACCR105443      OPTIONAL LOCAL DIAGNOSTIC
finite smooth contact as first failure    EXCLUDED
zero-height/spatial escape                OPEN / RH-BEARING
```

Future work may still use the adjacent-rung ratio to quantify a boundary
contact or an escaping sequence. It must not advertise exclusion of finite
interior contact as the missing RH implication.