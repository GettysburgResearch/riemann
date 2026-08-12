# L-91549 — The affine child lift is score-loss nonexpansive for typed packets

Claim ID: `L-91549`  
Status: **PROVED EXACT FIXED-AFFINE LOSS THEOREM**  
Created: 2026-08-13  
Depends on: `L-91318`, `L-91329`, `L-91540/L-91547`  
RH status: **unproved pending native-loss integration audit**

## 1. Child packing and loss

Let a positive typed child packet at endpoint `Y=X/m`, `m>=1`, have declared
source score

\[
 J_Y\ge0.
 \tag{L-91549.1}
\]

Let `d(n)>=0` be any feasible finite child row packing with entropy score

\[
 \mathcal S_Y(d)=\sum_nd(n)G_n.
 \tag{L-91549.2}
\]

Its packet loss is

\[
 \boxed{
 \ell_Y(d)=J_Y-\mathcal S_Y(d).
 }
 \tag{L-91549.3}
\]

No positivity of `ell_Y` is required for the algebra below.

## 2. Exact affine lift

Use the affine map

\[
 \Phi_m(n)=m(n+1)-1
 \tag{L-91549.4}
\]

and define

\[
 \boxed{
 D(\Phi_m(n))=m^{-1/2}d(n),
 }
 \tag{L-91549.5}
\]

with zero coefficients off the affine image.

`L-91318` proves simultaneously:

1. exact matched-fiber carry covariance;
2. nonnegative leakage on every other physical column;
3. entropy amplification
   \[
   \boxed{
   \mathcal S_X(D)
   \ge\sqrt m\,\mathcal S_Y(d)
   \ge\mathcal S_Y(d).
   }
   \tag{L-91549.6}
   \]

The target covariance is exactly the critical factor `m^-1/2` already present
in (L-91549.5), so no second branch coefficient is introduced.

## 3. Parent branch score has coefficient one

The positive typed source decomposition of `L-91540/L-91547` assigns to this
child the coefficient-one declared score

\[
 J_Y.
 \tag{L-91549.7}
\]

All endpoint change appears in the positive parent residual; it does not
multiply the inherited child score.  Therefore the parent score deficit carried
by the lifted child is

\[
\begin{aligned}
 J_Y-\mathcal S_X(D)
 &\le J_Y-\mathcal S_Y(d)\\
 &=\ell_Y(d).
\end{aligned}
\]

Hence

\[
 \boxed{
 \ell_X^{\rm inherited}(D)
 \le\ell_Y(d).
 }
 \tag{L-91549.8}
\]

The affine lift is loss nonexpansive.  In fact it has the favorable reserve

\[
 \mathcal S_X(D)-\mathcal S_Y(d)
 \ge(\sqrt m-1)\mathcal S_Y(d).
 \tag{L-91549.9}
\]

## 4. Target-mass scaling

If the actual child packet has target mass `omega>=0`, positive homogeneity gives

\[
 J_Y\mapsto\omega J_Y,
 \qquad
 d\mapsto\omega d,
 \qquad
 \ell_Y\mapsto\omega\ell_Y.
 \tag{L-91549.10}
\]

Applying (L-91549.8) to the scaled packet yields

\[
 \boxed{
 \ell_X^{\rm inherited}
 \le\omega\ell_Y(\widehat d),
 }
 \tag{L-91549.11}
\]

where `widehat d` is target-normalized.  Thus the inherited loss coefficient is
at most the child target mass.  There is no factor `sqrt(m)`, `m`, or
`m^-1/2` multiplying the loss.

For the normative reset of `L-91547`, `m=67` for both child types.

## 5. Several children and one physical quantization

Apply (L-91549.5) to every positive child endpoint measure, push all images into
the parent continuum coordinate, and sum.  `L-91329` quantizes this total measure
once.  Positivity and linearity preserve (L-91549.11) under the sum:

\[
 \boxed{
 \ell_X^{\rm inherited}
 \le\sum_b\omega_b
  \ell_{Y_b}(\widehat d_b).
 }
 \tag{L-91549.12}
\]

The one global safety factor, top omission and collar add only their resident
bounded current-generation debt.

## 6. Scope firewall

This theorem concerns the score deficit of an already identified positive typed
child packet.  It does not prove that the signed arithmetic source produces the
child, nor that the typed packet loss is the same object as the native loss
consumed by PR `#352`; that final identification is a separate audit.

```text
matched-fiber capacity covariance                    EXACT
nonmatched physical leakage                          POSITIVE
entropy score amplification                          EXACT
coefficient-one typed child score                    EXACT ON L-91540/47
inherited affine score loss <= child loss             EXACT
loss coefficient <= target mass                      EXACT
fixed-67 affine normalization joint                  CLOSED
native PR352 loss identification                      AUDIT REQUIRED
Riemann Hypothesis                                   UNPROVEN
```
