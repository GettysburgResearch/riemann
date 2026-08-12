# T-91404 — One-node annular innovation exhaustion would prove RH

Claim ID: `T-91404`  
Status: **FULL CONDITIONAL RH PROPOSAL / DYADIC ONE-NODE EXHAUSTION OPEN**  
Created: 2026-08-12  
Depends on: `L-91420`, `L-91421`, `R-91407`; `L-91313`--`L-91319` on PR #403  
RH status: **unproved**

## 1. Fixed node and dyadic scales

Fix

\[
 \eta=1,
 \qquad
 a_j=2^{-j-1}
 \quad(j\ge0).
 \tag{T-91404.1}

At `a_0=1/2`, the crossed half-plane is `Re s>1`, so the hyperbolic port is
zero.  At every later scale, the same Cauchy node detects every newly crossed
zero in the annulus

\[
 \frac12+a_j<\Re s\le\frac12+a_{j-1}.
 \tag{T-91404.2}

## 2. Declared arithmetic innovations

For each `j>=1`, let

\[
 \mathcal S_j^{\rm arith}
\]

be the explicit positive source innovation built from:

```text
the dyadic generalized-Jordan prime first chaos;
the completed gamma/pole channel;
the one-Green vector at q_j=1/2-a_j;
the coefficient-one scale cocycle;
the fixed deterministic terminal channel.
```

The prime part has norm

\[
 F(a_j)-F(a_{j-1})
 \]

with the orientation written according to the positive innovation convention
of `L-91319`; all completed amplitude factors are safe real-axis xi values.

## 3. One-Node Annular Innovation Exhaustion (`ONAIE_j`)

Construct explicitly a source-ordered isometry

\[
 \mathfrak U_j:
 \mathcal S_j^{\rm arith}
 \longrightarrow
 \mathcal K_j^{\rm crit}
 \oplus
 \mathcal K_j^{\rm st}
 \oplus
 \mathcal K_j^{\rm hyp}
 \oplus
 \mathcal E_j
 \tag{T-91404.3}

at the one Cauchy vector `r_1`, compatible with the dyadic cocycle, and prove

\[
 \boxed{
 \|\mathcal S_j^{\rm arith}\|^2
 =\|\mathcal K_j^{\rm crit}\|^2
  +\|\mathcal K_j^{\rm st}\|^2.
 }
 \tag{T-91404.4}

No same-annulus auxiliary norm may remain.  In particular

\[
 \mathcal K_j^{\rm hyp}=0,
 \qquad
 \mathcal E_j=0.
 \tag{T-91404.5}

The model hyperbolic norm is exactly

\[
 |B_{a_{j-1}}(1)|^{-2}
 H_{a_j,a_{j-1}}^{\rm ann}(1).
 \tag{T-91404.6}

## 4. Completion to RH

If `ONAIE_j` holds for every `j`, every term in the telescope

\[
 H_{a_J}(1)
 =\sum_{j=1}^{J}
 |B_{a_{j-1}}(1)|^{-2}
 H_{a_j,a_{j-1}}^{\rm ann}(1)
 \tag{T-91404.7}

vanishes.  Hence there are no zeros with

\[
 \Re s>\frac12+a_J
\]

for any `J`.  Letting `J -> infinity` and reflecting across the critical line
proves RH.

## 5. Why this is genuinely weaker than CPPD

`ONAIE` asks for one scalar source map per dyadic annulus at one fixed interior
node.  It does not ask for:

```text
all carriers;
all delays;
both Hardy orientations as independent variables;
the full bridge Gram;
a full operator ordering on the CPPD packet.
```

The Cauchy node diagonalizes every translation port and automatically closes
the adverse long parity port.  The remaining load-bearing component is the
prime/connection allocation at one scalar node.

## 6. Review firewall

`R-91407` shows that positive source innovations and positive annular
innovations do not imply exhaustion.  A claimed proof must construct the
source-to-model map before declaring the hyperbolic output absent.

## 7. Exact boundary

```text
one fixed node detects all crossed annuli              EXACT
dyadic hyperbolic telescope                            EXACT
one-node source vectors and safe scalars               EXPLICIT
translation and compensation ports scalarized          EXACT
positive innovation alone                              INSUFFICIENT
ONAIE coefficient-one source exhaustion                OPEN / RH-EQUIVALENT
Riemann Hypothesis                                     UNPROVED
```