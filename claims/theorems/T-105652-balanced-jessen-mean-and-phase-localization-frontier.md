# T-105652 — The balanced Jessen mean has an unconditional sign

Claim ID: `T-105652`  
Status: **MAJOR EXACT FINITE-PACKET TURÁN-FLOW THEOREM; POINTWISE LOCALIZATION OPEN**  
Created: 2026-08-25  
Depends on: `L-105643`, `L-105646--L-105651`; `T-105645--T-105650`  
RH status: **unproved**

## 1. Parent and derivative penetration moments

Let `p` be a real monic polynomial of degree `n>=2`.  For `H>=0`, define

\[
\mathcal P_H(p)
=
\sum_{p(\rho)=0}
(\operatorname{Im}\rho-H)_+,
\]

with multiplicity.  `L-105651` proves the full directional majorization of the
critical points plus the root centroid by the parent roots.  Since the centroid
of a real polynomial is real,

\[
\boxed{
\mathcal P_H(p')\le\mathcal P_H(p)
\qquad(H\ge0).
}
\tag{T-105652.1}

Define the one-rung penetration loss

\[
\boxed{
\mathcal E_H(p)
=2\bigl(\mathcal P_H(p)-\mathcal P_H(p')\bigr)
\ge0.
}
\tag{T-105652.2}

This is an unconditional nonnegative physical quantity for every finite real
polynomial packet.

## 2. Exact Jessen carrier formula

Let

\[
\mathcal M_H(p)
=
\sum_{p(\rho)=0}|\operatorname{Im}\rho-H|.
\]

Because the total imaginary part of the roots of `p` and `p'` is zero,

\[
\mathcal M_H(p)
=nH+2\mathcal P_H(p),
\]

\[
\mathcal M_H(p')
=(n-1)H+2\mathcal P_H(p').
\]

Therefore

\[
\boxed{
\mathcal E_H(p)
=
\mathcal M_H(p)-\mathcal M_H(p')-H
\ge0.
}
\tag{T-105652.3}

The term `H` is the unavoidable one-degree Jessen carrier.  After it is
removed, the parent-minus-derivative horizontal logarithmic potential is
always nonnegative.

Equivalently, every regularized horizontal log-modulus mean of `p/p'` lies on
the favorable side of its degree-one carrier.  This is a genuine integrated
physical sign; it does not use real-rootedness.

## 3. Exact signed height-index integral

Let

\[
N_p(t)
=
\#\{\rho:p(\rho)=0,\ \operatorname{Im}\rho>t\}
\]

and define `N_(p')` similarly.  Layer cake gives

\[
\mathcal P_H(p)-\mathcal P_H(p')
=
\int_H^\infty
\bigl(N_p(t)-N_{p'}(t)\bigr)dt.
\]

The parent/derivative all-pass of `L-105643/T-105645` has degree

\[
\deg\mathcal R_{p,t}
=N_{p'}(t)-N_p(t).
\]

Hence

\[
\boxed{
\mathcal E_H(p)
=-2\int_H^\infty
\deg\mathcal R_{p,t}\,dt
\ge0.
}
\tag{T-105652.4}

The balanced signed all-pass flow therefore already has the correct sign after
horizontal/height integration.  No adverse-only Hankel norm and no absolute
model-space coverage appears.

## 4. Rung-by-rung decomposition of the complete off-line penetration

Let `p^(R)` be a real-rooted derivative of `p`.  Telescoping (T-105652.2)
gives

\[
\sum_{r=0}^{R-1}\mathcal E_H(p^{(r)})
=2\bigl(\mathcal P_H(p)-\mathcal P_H(p^{(R)})\bigr).
\]

Since `p^(R)` is real-rooted,

\[
\boxed{
2\mathcal P_H(p)
=
\sum_{r=0}^{R-1}
\mathcal E_H(p^{(r)}).
}
\tag{T-105652.5}

Thus the complete upper off-line penetration of the parent is exactly a sum of
nonnegative adjacent-rung Jessen--Turán excesses.

For a conjugation-symmetric zero set, the lower-half-plane copy is identical.
The complete distance of the zero divisor from the real axis is therefore
resolved into positive one-rung spectral-flow increments.

## 5. Xi consequence at finite-window scope

Apply (T-105652.5) to real canonical-product truncations of the Xi derivative
ladder on a regular rectangle.  If the proposed fixed-width terminal derivative
theorem is authenticated, the terminal packet is real-rooted in the inner
window.  Up to the explicit horizontal endpoint and common-zero ledger, the
base Xi penetration is then the sum of the nonnegative adjacent-rung
Jessen--Turán excesses.

This proves `BSTF105645` at the **horizontally averaged penetration level**.
The remaining difficulty is no longer the sign of the integrated balanced
flow.  It is localization:

```text
D0PHASE105650 / POINTID105630

Prevent a positive Jessen--Turan mean from concentrating into arbitrarily
shallow, spatially escaping, degree-zero phase slips while all source averages
remain favorable.
```

The exact logarithmic clipped-index and adaptive-band machinery of
`L-105647--L-105649` retains every integer during that localization.

## 6. Why the theorem does not already prove RH

A conjugate pair at heights `+epsilon` and `-epsilon` contributes only
`2epsilon` to penetration.  It remains a full off-real pair topologically.
Thus an arbitrarily small positive value of the right side of (T-105652.5)
does not imply zero off-line roots.

Moreover, an integrated horizontal sign does not imply the pointwise
microscope inequality; `R-105630` gives an exact finite-frequency separator.
The theorem closes the mean sign, not the phase localization.

## 7. Exact status

```text
full directional critical-point majorization         PROVED EXACT
all convex projected-root tests decrease              PROVED EXACT
balanced Jessen carrier excess nonnegative             PROVED EXACT
signed height-integrated allpass flow favorable        PROVED EXACT
rung sum = complete parent penetration                 PROVED EXACT
finite-window Xi endpoint/common-zero transfer         OPEN
D0PHASE105650 degree-zero phase localization            OPEN / RH-BEARING
POINTID105630 pointwise physical evaluation             OPEN / RH-BEARING
fixed-width terminal derivative theorem                PROPOSED / REVIEW
Riemann Hypothesis                                      UNPROVEN
```

## 8. Scope

All statements through (T-105652.5) are finite-polynomial theorems.  Entire Xi
passage requires the cofinal canonical-product and endpoint ledger.  The result
does not reverse differentiation, exclude shallow off-line pairs, prove the
pointwise Turan sign, or prove RH.
