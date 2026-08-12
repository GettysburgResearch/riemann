# T-91541 — A target-normalized typed branching reset closes the score consumer without restriction-loss comparisons

Claim ID: `T-91541`  
Status: **PROVED CONDITIONAL TYPED-PACKET CONSUMER**  
Created: 2026-08-13  
Depends on: `L-91540`; `L-91329`; the PR `#352` loss-to-RH consumer  
RH status: **unproved absent the typed reset producer**

## 1. Why the packet itself must be propagated

Let \(\mathcal C\) be a family of paired positive kernel types as in `L-91540`.
For a positive packet \((\tau,\nu)\), let

\[
 \ell_X(\tau,\nu)
\]

denote its target score minus the best score of a feasible physical packing.
Write the packet target score as \(J_X(\tau,\nu)\) and its feasible
packing cone as \(\mathcal F_X(\tau,\nu)\).  Linearity of the target and
positive capacity maps gives

\[
 \mathcal F_X(\tau,\alpha\nu)
 =\alpha\mathcal F_X(\tau,\nu)
 \qquad(\alpha\ge0),
\]

and

\[
 d_i\in\mathcal F_X(\tau_i,\nu_i)
 \Longrightarrow
 d_1+d_2\in
 \mathcal F_X\!\left((\tau_1,\nu_1)\oplus(\tau_2,\nu_2)\right).
\]

Consequently

\[
 \ell_X(\tau,\alpha\nu)=\alpha\ell_X(\tau,\nu)
 \tag{T-91541.0a}
\]

for the **same** packet, and

\[
 \ell_X\!\left((\tau_1,\nu_1)\oplus(\tau_2,\nu_2)\right)
 \le
 \ell_X(\tau_1,\nu_1)+\ell_X(\tau_2,\nu_2).
 \tag{T-91541.0b}
\]

The only structural properties used below are therefore:

1. positive homogeneity in the **same** packet;
2. subadditivity under positive direct sums;
3. positive, capacity-faithful assembly of child packings.

No comparison is made between the loss of a restriction and a scalar multiple
of the loss of an unrelated full packet.  In particular, this theorem does not
use the false implication

\[
 \nu'\le\nu
 \Longrightarrow
 \ell(\nu')\le
 \frac{\|\nu'\|}{\|\nu\|}\ell(\nu).
\]

The actual child packet is retained and normalized only by its own target mass.

## 2. Worst-case normalized typed loss

For endpoint \(X\), define

\[
 \boxed{
 \mathfrak L_X^{\mathcal C}
 =\sup\left\{
  \ell_X(\tau,\nu):
  \tau\in\mathcal C,\ 
  \nu\ge0,\ 
  \mathfrak T_{\tau,X}(\nu)=1
 \right\}.
 }
 \tag{T-91541.1}
\]

Assume a finite base on which this supremum is bounded.

## 3. Typed reset hypothesis

Suppose every normalized packet in \(\mathcal C\) admits a positive reset with:

- child endpoints \(Y_b\le cX+C_0\), \(0<c<1\);
- actual positive child packets \((\tau_b,\nu_b)\in\mathcal C\);
- child target masses
  \[
   \omega_b=\mathfrak T_{\tau_b,Y_b}(\nu_b),
   \qquad
   \sum_b\omega_b\le1;
  \tag{T-91541.2}
  \]
- a capacity-faithful lift of arbitrary feasible child packings;
- local debt
  \[
   E_X(\tau,\nu)
   \le C_1(1+\log\log(3X))^A.
  \tag{T-91541.3}
  \]

For \(\omega_b>0\), write
\(\widehat\nu_b=\nu_b/\omega_b\).  Positive homogeneity applied to the actual
child gives

\[
 \ell_{Y_b}(\tau_b,\nu_b)
 =\omega_b\ell_{Y_b}(\tau_b,\widehat\nu_b)
 \le\omega_b\mathfrak L_{Y_b}^{\mathcal C}.
 \tag{T-91541.4}
\]

Subadditivity and the positive assembly therefore yield

\[
 \boxed{
 \mathfrak L_X^{\mathcal C}
 \le C_1(1+\log\log(3X))^A
   +\sum_b\omega_b\mathfrak L_{Y_b}^{\mathcal C}.
 }
 \tag{T-91541.5}
\]

## 4. Tree expansion

At every depth the path target weights sum to at most one by
(T-91541.2).  All endpoints enter the finite base after

\[
 J(X)=O(\log X/|\log c|)
 \tag{T-91541.6}
\]

levels.  Expanding (T-91541.5) gives

\[
 \boxed{
 \mathfrak L_X^{\mathcal C}
 =O\!\left(
  \log X(1+\log\log X)^A
 \right)
 =o(\log^2X).
 }
 \tag{T-91541.7}
\]

This is the same branching estimate as `T-91302`, now formulated for actual
typed packets.

## 5. Entry from the native packet

Suppose the native factor-54 packet has one positive entry decomposition

\[
 \text{native target}
 =\sum_\alpha\text{typed target}_\alpha
  +\text{positive current-generation target},
 \tag{T-91541.8}
\]

whose represented score is at least the native score, whose exact finite rows
are nonnegative, and whose normalized typed target masses sum to at most one.
Then

\[
 \mathfrak L_X^{\rm native}
 \le E_X^{\rm entry}
   +\sum_\alpha\omega_\alpha
     \mathfrak L_{Y_\alpha}^{\mathcal C}.
 \tag{T-91541.9}
\]

If the entry debt is bounded by the same class as (T-91541.3), (T-91541.7)
applies to the native loss.  The PR `#352` conclusion then gives RH.

## 6. Application of `L-91540`

For the paired-kernel branching of `L-91540`, target normalization gives
(T-91541.2), every child endpoint is at most \(X/67<c_0X\), the finite-row lift
and one-use quantization are supplied by `L-91329`, and

\[
 E_X\le1
 \tag{T-91541.10}
\]

for a normalized packet by (L-91540.15).  Thus all recursive hypotheses of this
consumer are exact once the one-prime positive entry has been supplied.

```text
actual-packet positive homogeneity                  EXACT
loss subadditivity under positive sums              EXACT
restriction-loss proportionality                    NOT USED
typed target subprobability recurrence              EXACT
bounded debt per tree depth                         EXACT
typed loss = O(log X polyloglog X)                  EXACT
native positive typed entry                         PRODUCER HYPOTHESIS
typed entry + PR #352                               RH CONDITIONAL
Riemann Hypothesis                                  UNPROVEN
```
