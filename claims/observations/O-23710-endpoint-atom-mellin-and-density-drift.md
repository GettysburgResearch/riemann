# O-23710 — Endpoint-atom Mellin symbol and the parabolic density drift

Observation ID: `O-23710`  
Title: The continuum endpoint atom is the Mellin derivative of the parabolic shell defect and carries the same deterministic prime-density drift  
Status: **EXACT CONTINUUM IDENTIFICATION; NO PRIME-SAMPLING ESTIMATE**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Dependencies: `L-23719`; PRs #240/#274 parabolic shell notation  
Scope: cross-route identification only

## 1. Endpoint continuum kernel

Retain

\[
\phi(u)=2K-\frac{S_K+1}{\sqrt u},
\qquad
K=\left\lfloor\frac1u\right\rfloor,
\qquad
S_K=\sum_{k=1}^{K}k^{-1/2}.
\tag{O-23710.1}
\]

This is the scaling limit of the endpoint residual in `L-23719`.

For `Re(s)>1`, divisor switching gives

\[
\int_0^1\left\lfloor\frac1u\right\rfloor u^{s-1}du
=\frac{\zeta(s)}s,
\tag{O-23710.2}
\]

and

\[
\int_0^1u^{s-3/2}
 \sum_{k\le1/u}k^{-1/2}du
=\frac{\zeta(s)}{s-1/2}.
\tag{O-23710.3}
\]

Therefore

\[
\boxed{
 \Phi(s):=\int_0^1\phi(u)u^{s-1}du
 =\frac{(s-1)\zeta(s)-s}{s(s-1/2)}.
}
\tag{O-23710.4}
\]

## 2. Relation to the parabolic shell defect

The continuum parabolic defect used in the weighted-shell programme has Mellin
symbol

\[
\mathcal M_E(s)
=\frac1{(s-1/2)^2}
 \left[\frac{(s-1)\zeta(s)}s-1\right].
\tag{O-23710.5}
\]

Comparison with (O-23710.4) gives the exact identity

\[
\boxed{
 \Phi(s)=(s-1/2)\mathcal M_E(s).
}
\tag{O-23710.6}
\]

Thus the endpoint atom is the infinitesimal scale derivative of the same
continuum shell state underlying WSTS.  AWTO is a strictly atomized strengthening
of the weighted-shell theorem, not an independent continuum phenomenon.

## 3. Critical moments

At `s=1`, the pole of zeta is removable and

\[
\boxed{
 \Phi(1)=\int_0^1\phi(u)du=0.
}
\tag{O-23710.7}
\]

Using

\[
(s-1)\zeta(s)=1+\gamma(s-1)+O((s-1)^2),
\]

one obtains

\[
\boxed{
 \Phi'(1)=2(\gamma-1),
 \qquad
 \int_0^1\phi(u)\log(1/u)du=2(1-\gamma)>0.
}
\tag{O-23710.8}
\]

The endpoint continuum atom therefore has zero total mass but a nonzero
logarithmic drift.  Its positive lower-ratio mass and negative upper-ratio mass
are exactly balanced in total, in agreement with the strict upper-tail order of
`L-23719`.

## 4. Consequences for proof strategy

1. The deterministic density drift isolated on PR #274 and the endpoint-atom
   continuum state are the same object after one Mellin derivative.
2. A prime-only unweighted queue cannot be substituted for the logarithmically
   weighted atom tail; it retains the nonzero moment (O-23710.8).
3. Checking any fixed number of quotient layers cannot close AWTO: `L-23719`
   proves those layers eventually negative, while (O-23710.7) forces the
   compensating positive mass into quotient depth tending to infinity.
4. A successful completion must control the prime sampling of this zero-mass
   ordered state, or produce an exact lower-scale recurrence for its deep
   quotient ledger.

## 5. Boundary

Exact here:

- the Mellin transform (O-23710.4);
- the derivative relation (O-23710.6);
- the two critical moments.

Not proved:

- atomwise prime-tail order;
- WSTS;
- RH.
