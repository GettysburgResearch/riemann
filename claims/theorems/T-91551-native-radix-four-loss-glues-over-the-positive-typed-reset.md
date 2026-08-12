# T-91551 — The native radix-four score loss glues over the positive typed reset

Claim ID: `T-91551`  
Status: **PROVED ALGEBRAIC NATIVE-LOSS GLUING; FACTOR-54 APPLICATION IS A CANDIDATE COMPLETE PROOF PACKET AWAITING INDEPENDENT RECONSTRUCTION**  
Created: 2026-08-13  
Depends on: `L-90029`, `T-91101`, `T-91302`, `L-91329`, `L-91541`, `L-91545`, `L-91547`--`L-91550`  
RH status: **unproved pending independent end-to-end verification**

## 1. The conclusion-producing native loss

For a nonnegative ordinarily feasible parent row `d`, the native radix-four
score loss is

\[
 \boxed{
 \mathfrak L_X(d)
 =J_\Lambda(X)-\mathcal S_X(d),
 \qquad
 \mathcal S_X(d)=\sum_nd(n)G_n.
 }
 \tag{T-91551.1}
\]

Equivalently, for endpoint weights `lambda_T`,

\[
 \mathfrak L_X(d)
 =\sum_{T=3}^X(1-\lambda_T)H_T.
 \tag{T-91551.2}
\]

`L-90029` proves that detail feasibility implies ordinary feasibility and that

\[
 \boxed{
 \mathfrak L_X(d)=o(\log^2X)
 \Longrightarrow \mathrm{RH}.
 }
 \tag{T-91551.3}
\]

Thus the reset must control the literal entropy-score deficit (T-91551.1).

## 2. Packet loss

Let a positive source packet `P=(tau,nu,Y)` have declared entropy-score ledger

\[
 J(P)\ge0
 \tag{T-91551.4}
\]

and positive feasible row cone `F(P)`.  For `d in F(P)` define

\[
 \boxed{
 \ell(P;d)=J(P)-\mathcal S_Y(d).
 }
 \tag{T-91551.5}
\]

The score and every capacity map are linear.  Hence, for `a>=0`,

\[
 \ell(aP;ad)=a\ell(P;d),
 \tag{T-91551.6}
\]

and positive direct sums are subadditive after feasible packings are added.
No sign condition on `ell` is needed; weights above one and favorable negative
loss remain allowed.

## 3. Score-superordinate gluing lemma

Suppose a parent packet with declared score `J_X` is decomposed into:

- a current-generation positive packet with a feasible row `d_0`;
- positive child packets `P_b` with arbitrary feasible rows `d_b`;
- current debt `E_X>=0`;
- a positive capacity-faithful parent assembly
  \[
  d_X=\mathcal A_X(d_0,(d_b)_b).
  \tag{T-91551.7}
  \]

Assume the score ledger and lift satisfy

\[
 \boxed{
 J_X
 \le E_X+\mathcal S_X(d_0)+\sum_bJ(P_b),
 }
 \tag{T-91551.8}
\]

\[
 \boxed{
 \mathcal S_X(d_X)
 \ge\mathcal S_X(d_0)+\sum_b\mathcal S_{Y_b}(d_b).
 }
 \tag{T-91551.9}
\]

Subtracting (T-91551.9) from (T-91551.8) gives the exact loss inequality

\[
 \boxed{
 J_X-\mathcal S_X(d_X)
 \le E_X+\sum_b\ell(P_b;d_b).
 }
 \tag{T-91551.10}
\]

This is pure algebra.  It does not compare the loss of a restriction with a
mass fraction of the loss of a different packet.

## 4. Target normalization

Let the child target masses be `omega_b>=0`, and write

\[
 P_b=\omega_b\widehat P_b,
 \qquad
 d_b=\omega_b\widehat d_b.
 \tag{T-91551.11}
\]

Positive homogeneity yields

\[
 \ell(P_b;d_b)
 =\omega_b\ell(\widehat P_b;\widehat d_b).
 \tag{T-91551.12}
\]

If

\[
 \sum_b\omega_b\le1,
 \tag{T-91551.13}
\]

then (T-91551.10) is exactly a substochastic branching recurrence.

## 5. Verification of the hypotheses for the live typed reset

The current factor-54 packet satisfies the gluing hypotheses as follows.

### 5.1 One-prime positive entry

`L-91452/L-91454`, with the merged directed replay `L-91550`, give two positive
branch Hall outputs whose targets sum exactly to the parent rough target and
whose scores sum to at least the parent rough score.

`L-91545` separates each Hall output into:

```text
a positive hereditary residual source c_tau;
a target-null coefficientwise positive row bonus B_tau.
```

Therefore the total declared score of the two residual sources plus the
current row bonuses is at least the signed one-prime score.

### 5.2 Fixed contraction and target weights

`L-91547` applies the same deterministic `67` split to both residual sources.
The child packets live at `X/67`, and

\[
 \boxed{
 \omega_s+\omega_h\le1.
 }
 \tag{T-91551.14}
\]

Every unused source and endpoint difference is a positive current-generation
packet.

### 5.3 Child score lift

`L-91549` proves that the fixed affine child lift is score-loss nonexpansive:

\[
 \mathcal S_X(D_b)
 \ge\mathcal S_{X/67}(d_b).
 \tag{T-91551.15}
\]

Thus each child enters (T-91551.9) with coefficient one.  The affine scaling
`67^{-1/2}` is already contained in the row pushforward and does not multiply
the inherited loss.

### 5.4 One-use physical assembly

`L-91329` pushes both child measures into the parent continuum coordinate,
sums all positive current and child packets, and quantizes once.  The global
safety factor, top omission and collar are charged once and contribute bounded
current debt.

`L-91548` proves that the binary target-null state correction uses one slice of
the common Hilbert innovation and that Hall row bonuses require no projective
port.  The complete endpoint-port cost is bounded by `147` per generation.

The previously resident finite mismatch, terminal annulus and outer block also
have bounded generationwise cost.  Hence

\[
 \boxed{
 E_X\le C
 }
 \tag{T-91551.16}
\]

for an absolute, deliberately unoptimized constant `C`.

Together these statements give (T-91551.8)--(T-91551.9) for the literal native
score (T-91551.1).

## 6. Native recurrence

For arbitrary target-normalized feasible child packings,

\[
 \boxed{
 \mathfrak L_X(d_X)
 \le C
 +\omega_s\ell_{X/67}(\widehat P_s;\widehat d_s)
 +\omega_h\ell_{X/67}(\widehat P_h;\widehat d_h),
 \qquad
 \omega_s+\omega_h\le1.
 }
 \tag{T-91551.17}
\]

The children are paired positive kernel types.  The actual-packet consumer
`T-91541` and finite target-normalized base give

\[
 \sup_{\widehat P}\inf_{d\in F(\widehat P)}\ell_X(\widehat P;d)
 =O(\log X).
 \tag{T-91551.18}
\]

Applying (T-91551.17) to the native entry therefore gives a nonnegative
ordinary/detail-feasible parent packing with

\[
 \boxed{
 \mathfrak L_X(d_X)=O(\log X)=o(\log^2X).
 }
 \tag{T-91551.19}
\]

## 7. Candidate RH conclusion

Combining (T-91551.19) with the exact consumer (T-91551.3) gives a complete
**candidate** factor-54 proof chain.

This document does not promote the Riemann Hypothesis to established status.
The chain must be independently reconstructed from the definitions of
`J_Lambda`, the endpoint rows, the Hall transports, the affine pushforward and
the one-use finite collar.  A mismatch at any one of those interfaces retracts
Section 6 while leaving the abstract gluing lemma intact.

## 8. Hostile review checklist

A reviewer should verify, without relying on this theorem's summary:

1. the score represented by each target-Hall residual source is the same
   entropy ledger appearing in `J_Lambda`;
2. every current row bonus is physically feasible before its score is counted;
3. the fixed-67 child score is not counted both before and after affine lift;
4. the one global safety factor/collar changes the score by only the resident
   bounded amount;
5. the final `d_X` is detail feasible, hence ordinarily feasible, in exactly the
   sense of `L-90029`;
6. the finite target-normalized base is uniform over both paired types.

```text
native loss = declared score - packing score          EXACT
positive packet loss homogeneity                      EXACT
score-superordinate gluing inequality                 EXACT
child loss coefficient = target mass                  EXACT
merged producer Hall/row margins                      CERTIFIED
fixed affine inherited loss nonexpansion              EXACT
one-use common port and collar                        EXACT ON CITED INPUTS
native O(log X) loss composition                      CANDIDATE COMPLETE
Riemann Hypothesis                                    UNPROVEN
```
