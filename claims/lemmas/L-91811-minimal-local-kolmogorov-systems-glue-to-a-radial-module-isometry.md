# L-91811 — Minimal local Kolmogorov systems glue to a radial module isometry

Claim ID: `L-91811`  
Status: **PROVED ABSTRACT LOCAL-TO-GLOBAL MODULE GLUING THEOREM**  
Created: 2026-08-13  
Depends on: `L-91740`, `L-91803`, `L-91810`  
RH status: **unproved**

## 1. Setup

Let `R>0`. For every half-open rational interval `I subset (0,R)`, let `A_I` and `C_I` be positive kernels on the same index set `X`, and suppose

\[
 A_I-C_I=:D_I\succeq0.
\]

Assume finite additivity on disjoint rational intervals:

\[
 A_{I\dot\cup J}=A_I+A_J,
\qquad
 C_{I\dot\cup J}=C_I+C_J,
\qquad
 D_{I\dot\cup J}=D_I+D_J.
\tag{L-91811.1}
\]

Let

\[
 A_I(x,y)=\langle a_{I,x},a_{I,y}\rangle,
\quad
 C_I(x,y)=\langle c_{I,x},c_{I,y}\rangle,
\quad
 D_I(x,y)=\langle d_{I,x},d_{I,y}\rangle
\]

be minimal Kolmogorov decompositions.

## 2. Orthogonal interval realization

Finite additivity implies that the global kernel

\[
 A_{(0,R)}=\sum_j A_{I_j}
\]

for any finite rational partition has the orthogonal Kolmogorov realization

\[
 a_x=\bigoplus_j a_{I_j,x}.
\]

Minimality makes any two such realizations canonically unitarily equivalent. Refinement therefore gives a directed system of isometric embeddings. Its inductive limit is a Hilbert space `H_A` with projections `P_I^A` satisfying

\[
 P_I^A a_x=a_{I,x},
\qquad
 P_I^A P_J^A=P_{I\cap J}^A.
\tag{L-91811.2}
\]

The same construction gives `H_C,H_D` and projection-valued interval algebras `P_I^C,P_I^D`.

## 3. Local lurking isometries

For each interval, positivity of `D_I=A_I-C_I` gives the canonical local lurking isometry

\[
 W_I:a_{I,x}\longmapsto c_{I,x}\oplus d_{I,x}.
\tag{L-91811.3}
\]

Indeed the two sides have identical Gram kernels `A_I`. Minimality makes `W_I` unique on the closed span of the kernel vectors.

For disjoint intervals `I,J`, the direct sum `W_I\oplus W_J` and `W_{I\dot\cup J}` agree on every generator because both send

\[
 a_{I,x}\oplus a_{J,x}
\]

to

\[
 (c_{I,x}\oplus c_{J,x})\oplus(d_{I,x}\oplus d_{J,x}).
\]

Hence the local maps are automatically refinement compatible.

## 4. Global module isometry

The directed union therefore defines an isometry

\[
\boxed{
 W:H_A\longrightarrow H_C\oplus H_D
}
\tag{L-91811.4}
\]

such that for every rational interval

\[
\boxed{
 W P_I^A=(P_I^C\oplus P_I^D)W.
}
\tag{L-91811.5}
\]

Monotone-class closure extends the relation from half-open rational intervals to the generated Borel projection algebra whenever the interval measures are countably additive in the strong operator topology.

Thus **local positive kernel defects plus additive compatibility automatically construct the interval-natural source-to-output map**. No additional choice of intertwiner is required.

## 5. Zeta reduction

Combining this theorem with `L-91803`, the RLSL burden can be reduced further. It is enough to construct, on every rational radial interval `I`, positive full-carrier kernels satisfying

\[
\boxed{
 A_I^{\rm arith}
 =C_I^{\rm crit}+S_I^{\rm st}+H_I^{\rm hyp}+E_I^{\rm aux}
}
\tag{L-91811.6}
\]

with all terms finitely/countably additive under interval refinement.

Equivalently, define

\[
 C_I=C_I^{\rm crit}+S_I^{\rm st}+H_I^{\rm hyp},
\qquad
 D_I=E_I^{\rm aux},
\]

and verify positivity interval by interval. The module map then follows from minimality rather than being a separate theorem.

If the arithmetic source is diffuse and `H^hyp` is pure point, `L-91802/L-91803` force `H^hyp=0`.

## 6. Stronger useful formulation

Exact equality is stronger than needed. If

\[
 A_I-C_I=D_I\succeq0
\]

for every rational interval and the three kernel measures are countably additive, the same construction applies. Therefore the final target may be written simply as the **radial kernel-measure domination**

\[
\boxed{
 C^{\rm model}(I)\preceq A^{\rm arith}(I)
 \quad\text{for every rational interval }I.
}
\tag{L-91811.7}
\]

This is strictly more structured than the global kernel lock of `L-91740` but removes the separate CAJE/RLSL map-construction problem.

## 7. Firewall

Global domination

\[
 C((0,R))\preceq A((0,R))
\]

does not imply (L-91811.7). Nor does positivity on one fixed dyadic grid. Intervalwise domination on a generating algebra, with refinement compatibility, is load bearing.

## 8. Exact boundary

```text
local kernel defect -> local lurking isometry        EXACT
additive minimal systems -> refinement compatibility EXACT
rational-interval maps glue to module isometry       EXACT
Borel extension under countable additivity           EXACT
RLSL map construction as separate burden             REMOVED
radial kernel-measure domination                      OPEN / RH-BEARING
Riemann Hypothesis                                    UNPROVED
```
