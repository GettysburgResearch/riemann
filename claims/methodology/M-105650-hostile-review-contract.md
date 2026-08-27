# M-105650 — Hostile review contract for adaptive Jensen index and balanced Jessen flow

Claim ID: `M-105650`  
Created: 2026-08-25  
Applies to: `L-105647--L-105651`, `R-105647`, `T-105650`, `T-105652`  
RH status: **unproved**

An independent reviewer should attack the packet in the following order.

## A. One-factor logarithmic integral

1. Recompute

   ```text
   |B_(beta+i delta)(x+i y)|^2
    = ((x-beta)^2+(y-delta)^2)
      /((x-beta)^2+(y+delta)^2).
   ```

2. Verify with the absolute value at `y=delta` that

   ```text
   integral log((x^2+a^2)/(x^2+c^2)) dx = 2 pi (a-c),
   ```

   and hence the normalized defect is `min(1,delta/y)`.
3. Confirm the sign convention:

   ```text
   U=A/B,
   lim_(y->0) J_y(U)=deg B-deg A=-wind U.
   ```
4. Check that an exponential inner factor would make the unrenormalized real-
   line integral diverge.  It must be removed before consumption.

## B. Coarea and random-scale mixture

1. Differentiate `y min(1,delta/y)=min(y,delta)` distributionally.
2. Verify

   ```text
   -d^2[y J_y]/dy^2
    = denominator depth atoms - numerator depth atoms.
   ```
3. Reintegrate the probability density

   ```text
   2s/(1+s)^3
   ```

   and verify

   ```text
   x/(1+x)=integral min(1,x/s) 2s/(1+s)^3 ds.
   ```
4. Check the change of variables to

   ```text
   8 H y/(H+2y)^3 dy.
   ```
5. Ensure that the additive soft-depth sum is not silently identified with a
   nonorthogonal product-model-space trace.

## C. Monotone-current layer cake

1. Check Stieltjes conventions in

   ```text
   r(xi)=integral_[xi,infinity) d nu_r(L).
   ```
2. Apply Tonelli and recover

   ```text
   q_r(delta)=integral (1-exp(-2 delta L)) d nu_r(L).
   ```
3. Verify that the complement is exactly

   ```text
   r(0)-q_r(delta)=integral exp(-2 delta L) d nu_r(L).
   ```
4. Confirm that the Xi application uses the monotone profile `R_H`, not a
   fixed-band surrogate.

## D. Degree-zero firewall

For

```text
U=B_(ia)/B_(ib),
```

recompute

```text
wind U=0,
J_y(U)=0 for y<min(a,b),
||H_U||_HS^2=(a-b)^2/(a+b)^2.
```

Any inference from signed index to oriented phase energy is invalidated by this
fixture.

## E. Directional majorization

1. Reconstruct the compression `C` of the diagonal root matrix to `e^perp`
   and verify `det(wI-C)=p'(w)/n`.
2. Pinch the Hermitian directional part to `Ce plus e^perp` and apply Hermitian
   eigenvalue majorization.
3. In a Schur basis of `C`, verify that the diagonal entries of the directional
   Hermitian part are the projected critical points.
4. Check transitivity and equal sums before applying Karamata.
5. Verify the centroid term.  It may be dropped at upper height only for a real
   polynomial and `H>=0`.
6. Recompute the absolute-distance/Jessen carrier identity and the rung
   telescope.

## F. Entire-function and status firewalls

The finite formulas do not by themselves justify:

```text
an unregularized infinite Xi log integral;
removal of the Cartwright exponential carrier;
vanishing horizontal endpoint terms;
pointwise Turan positivity;
control of the degree-zero reverse Hankel energy;
real-rootedness of a parent from a real-rooted derivative;
RH.
```

The following must remain false in every result object and summary:

```text
D0PHASE105650 proved;
POINTID105630 proved;
cofinal Xi endpoint ledger proved;
fixed-width moving-saddle theorem authenticated;
Riemann Hypothesis established.
```
