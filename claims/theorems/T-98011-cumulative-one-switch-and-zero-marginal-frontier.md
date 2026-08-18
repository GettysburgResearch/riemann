# T-98011 — Corrected cumulative one-switch and zero-marginal frontier

Claim ID: `T-98011`  
Status: **CONTROLLING CORRECTION TO `T-98010`**  
Created: 2026-08-18  
Depends on: `L-98010`–`L-98012`, `R-98010`, PRs #594 and #596  
RH status: **unproved**

`R-98010` makes the pointwise theorem `OSTP67` false. Wherever `T-98010` lists `OSTP67` as an open closure option, this file controls and withdraws that option.

## 1. Exact surviving cumulative object

For a finite prime state `P`, define

\[
\mathcal C_P(X,\lambda)
=(\mathcal E_PH_\lambda)(X)
=\int_\lambda^6\mathcal T_P(X;Y_u)\,du,
\qquad 0\le\lambda\le6.
\tag{T-98011.1}
\]

This is the **Cumulative One-Switch Profile**. It satisfies

\[
\mathcal C_P(X,6)=0,
\qquad
-\partial_\lambda\mathcal C_P(X,\lambda)
=\mathcal T_P(X;Y_\lambda)
\]

away from finitely many source breakpoints.

The pointwise derivative may be negative. The exact required sign is the area inequality

\[
\boxed{
\mathcal C_P(X,\lambda)\ge0,
}
\tag{T-98011.2}
\]

not `mathcal T_P>=0`.

Call the complete source-faithful assertion (T-98011.2) `COSP67`.

## 2. Minimal state after the counterexample

The instantaneous two-moment state

\[
(U_P(K),V_P(K))
\]

still determines the derivative exactly, but it cannot support a pointwise positive cone. A legitimate Bellman state must retain at least

\[
\boxed{
\left(
\mathcal C_P(X,\lambda),
U_P(K_\lambda),
V_P(K_\lambda)
\right),
}
\tag{T-98011.3}
\]

or an equivalent accumulated-area coordinate. Any proposed two-coordinate proof must first explain how it recovers the missing signed area; otherwise `R-98010` is a separator.

## 3. Corrected closure alternatives

The live exact alternatives are now:

### Root route

\[
\boxed{
\mathrm{GPC67}/\mathrm{RBLPTE67}
\Longrightarrow\mathrm{RH}.
}
\tag{T-98011.4}
\]

This is the minimal conclusion-producing theorem and remains open.

### Zero-marginal Lorenz route

\[
\boxed{
\mathrm{ZMTS67}+\mathrm{GPC67}
\Longrightarrow\mathrm{CPSL67}
\Longrightarrow\mathrm{RH}.
}
\tag{T-98011.5}
\]

Here `ZMTS67` is target-only; it shows that every nonzero hinge is no worse than the root.

### Cumulative one-switch route

A source-faithful proof of `COSP67`, together with the exact inactive-odd cushion and statement-to-use map, gives the corresponding Lorenz-Bellman profile. At `lambda=0`, it contains the native root scalar.

## 4. Allowed next mechanisms

Because a derivative may be negative, a successful proof may use:

```text
one-crossing of the target-prefix derivative;
a positive terminal area plus a bound on total negative excursion;
an area-plus-slope Bellman invariant;
a future-prime martingale storing accumulated signed area;
an exact Type-II estimate for only the negative derivative sectors.
```

The following are now forbidden:

```text
pointwise positivity of every target prefix;
a fixed cone in only (U,V) with no area coordinate;
a fixed positive mass aperture;
source-blind absolute values of the negative derivative sector.
```

## 5. Exact boundary

```text
ordered marginal ratios                         PROVED
one-switch derivative profile                   PROVED
pointwise OSTP67                                REFUTED
cumulative one-switch profile                   EXACT
COSP67 cumulative positivity                    OPEN
ZMTS67 target sandwich                          OPEN
GPC67 / RBLPTE67 root scalar                    OPEN / RH-BEARING
Riemann Hypothesis                              UNPROVEN
```
