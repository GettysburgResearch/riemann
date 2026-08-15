# L-91750 — The factor-67 common-parent compiler is an exact typed packet equality

Claim ID: `L-91750`  
Status: **PROVED EXACT COMPILER ON THE FROZEN POSITIVE-LINEAR INPUTS**  
Created: 2026-08-15  
Frozen inputs: PR #481 at `005ae49723898d8661d407a0433a6d69cb6d6efc`; PR #479 at `518b6a5ec2b49b7decbd4c2e349d0ee5b26bfc9b`; `L-91650`, `L-91654`, `L-91658`, `L-91674`; the factor-67 root Hall and first-owner source partition  
RH status: **unproved**

## 1. Complete typed space

Use one additive typed vector space containing

\[
 (\text{source/provenance},J,T,S,E,q,\Gamma,\Xi,b,\mathcal P),
\]

where `q` is the physical component row, `Gamma` and `Xi` are the exact
ordinary and radix-four responses, `b` is the child-owned finite boundary
coordinate, and `mathcal P` is the separate root matrix-port coordinate. All
coordinates are positively homogeneous. The port is not a radix-four column
and has no `Y_4` pairing.

Every source occurrence retains the complete label

```text
(endpoint cell, P61 divisor, Hall residual/bonus,
 first rough owner, source history, same-index placement).
```

## 2. One common positive source and one global quantizer

Let `Lambda_X` be the positive labelled endpoint measure obtained after the
factor-67 root Hall operation. Include the Hall row bonuses as current-labelled
positive atoms. Let

\[
 \mathscr R_X
\]

be the following common positive operation, in this order:

```text
remove the bottom, top, and activation-knot collars;
apply positive same-cell barycentric refinement;
apply the single square-root safety thinning;
push all retained colours to one parent endpoint coordinate.
```

Every step is a positive restriction, Markov splitting, scalar multiplication,
or pushforward. It is applied before current/child labels are forgotten. Thus

\[
 \widetilde\Lambda_X=\mathscr R_X\Lambda_X
\tag{L-91750.1}
\]

is one positive source with one owner per atom.

Apply the **single** positive endpoint quantizer while retaining the source
labels:

\[
 \widehat P_X=\mathcal Q_X\widetilde\Lambda_X.
\tag{L-91750.2}
\]

Linearity of the quantizer and of every typed observation means that
`widehat P_X` is the positive sum of its labelled colour components, although
only the total physical row is tested against native capacity.

## 3. Apply the causal split to the labelled finite packet

Use one global ordered rough-prime list and zero extension on inactive
fibre/prime pairs. Apply the exact causal identity to the already quantized,
labelled packet `widehat P_X`. The frozen causal theorem gives

\[
 \boxed{
 \widehat P_X
 =P_X^{\rm cau}
  +\int_B a(b)U_bP_b\,d\nu(b),
 }
\tag{L-91750.3}
\]

where

```text
P_X^cau is a positive sum of base and causal-current packets;
every P_b is an actual positive finite typed child packet;
a(b)>=0;
all complete labels are retained;
children have zero root-global port;
int_B a(b) dnu(b)<1/8.
```

The equality holds in source, benchmark, target, declared score, literal score,
component row, ordinary response, radix-four response, and every child-owned
boundary coordinate. No commutation of a nonlinear Hall decision through a
rough tree and no separate child quantizer is used.

## 4. One current-only finite correction

Let `F_X` be the complete current-only finite correction datum consisting of the
one residual finite mismatch/taper/base correction and the one aggregate
uncolored root port. It is attached once after the common-parent sum. Recursive
children receive no copy of `F_X` and have zero root-global port.

Define

\[
 P_X^{\rm root}=\widehat P_X+F_X,
\qquad
 P_X^{\rm cur}=P_X^{\rm cau}+F_X.
\tag{L-91750.4}
\]

Then (L-91750.3) gives the concrete all-coordinate identity

\[
 \boxed{
 P_X^{\rm root}
 =P_X^{\rm cur}
  +\int_Ba(b)U_bP_b\,d\nu(b).
 }
\tag{L-91750.5}
\]

This is the packet equality requested by PRs #482 and #484. It is derived from
the actual operation order. It is not introduced as a definition of slack.

## 5. Actual packet capacities

For every positive typed packet `P`, let `Omega(P)` denote its declared
packet-specific radix-four capacity coordinate. For the concrete child packets
in (L-91750.5), this is the capacity transported with the complete typed child
label. No child is assigned a copy of the native root capacity.

The all-column realization of PR #479 supplies

\[
 \Xi(P_X^{\rm root})\le\Omega_X.
\tag{L-91750.6}
\]

Put

\[
 e_X=\Omega_X-\Xi(P_X^{\rm root})\ge0.
\tag{L-91750.7}
\]

Taking the radix-four coordinate of (L-91750.5) gives

\[
 \boxed{
 \Omega_X
 =\Xi(P_X^{\rm cur})+e_X
  +\int_Ba(b)U_b\Xi(P_b)\,d\nu(b).
 }
\tag{L-91750.8}
\]

If one elects to reserve the complete packet capacities `Omega(P_b)` rather
than insert the displayed child rows immediately, define

\[
 r_X=e_X+
 \int_Ba(b)U_b[\Xi(P_b)-\Omega(P_b)]\,d\nu(b)
\]

only when the bracket is known nonnegative in the chosen packet convention.
The preferred one-shot closure `L-91753` avoids that extra convention entirely:
it inserts the actual child rows already present in (L-91750.5) and uses the
total external slack `e_X` directly.

## 6. Port and source ownership

The port equality is separate:

\[
 \operatorname{Port}(P_X^{\rm root})
 =\operatorname{Port}(P_X^{\rm cur}),
 \qquad
 \operatorname{Port}(P_b)=0.
\tag{L-91750.9}
\]

The uncolored PSD port inequality is tested once after summation. It cannot be
counted in the radix-four slack and contributes no `Y_4` cost.

Every original source atom lies in exactly one of:

```text
unused collar/top/bottom source;
current causal/base/Hall-bonus source;
one source-labelled child colour in the final total row.
```

Every finite correction and the common port are current-owned exactly once.

## 7. Boundary

```text
common positive preprocessing before quantization     EXACT
one global labelled quantizer                          EXACT ON FROZEN INPUT
causal split of the labelled finite packet             EXACT
one current-only correction                            EXACT ON FROZEN INPUT
all-coordinate packet equality                         EXACT / (L-91750.5)
actual child row responses                              EXPLICIT
all-column native external slack                        PR #479 / FROZEN
root port                                               SEPARATE, CURRENT-ONLY
one-shot total-row closure                              L-91753
recursive packet-capacity convention                    NOT NEEDED BY L-91753
Riemann Hypothesis                                      UNPROVEN
```
