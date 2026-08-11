# L-91017 — Exact source–scattering tensor assembly and coefficient-one main-state closure

Claim ID: `L-91017`  
Status: **PROPOSED COMPLETE EXACT ASSEMBLY THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `L-91013`, `L-91014`, `L-91016`  
RH status: **unproved**

## 1. Two independent lossless structures

The positive generalized-Jordan source supplies the divisor isometry

\[
 V_{a,a}:H_{2a}\longrightarrow H_a\otimes H_a
\]

with

\[
 V_{a,a}k_{2a,s}=k_{a,s}\otimes k_{a,s+a}.
 \tag{L-91017.1}
\]

The dyadic Cauchy bank supplies the fixed-axis transfer

\[
 \mathcal R_a(u)=\mathcal R(u/a):\mathbb C^3\to\mathbb C^3,
 \tag{L-91017.2}
\]

which is unitary for real `u` and satisfies

\[
 h_{2a}(u)\mathcal R_a(u)e_1
 =\begin{pmatrix}h_a(u)\\g_{1,a}(u)\\g_{2,a}(u)\end{pmatrix}.
 \tag{L-91017.3}
\]

The source map and scattering map act on different tensor factors. Therefore

\[
 \boxed{
 (V_{a,a}\otimes I_3)(I\otimes\mathcal R_a(u))
 =(I\otimes\mathcal R_a(u))(V_{a,a}\otimes I_3).
 }
 \tag{L-91017.4}
\]

No compatibility estimate is required: the two constructions commute exactly.

## 2. Exact coherent-state assembly

For `Re(s)>1/2` and real `u`, apply the combined map to the coarse input:

\[
 k_{2a,s}\otimes h_{2a}(u)e_1.
\]

Equations (L-91017.1) and (L-91017.3) give

\[
 \boxed{
 \begin{aligned}
 &(V_{a,a}\otimes\mathcal R_a(u))
  [k_{2a,s}\otimes h_{2a}(u)e_1]\\
 &\qquad=
 k_{a,s}\otimes k_{a,s+a}\otimes
 \begin{pmatrix}h_a(u)\\g_{1,a}(u)\\g_{2,a}(u)\end{pmatrix}.
 \end{aligned}
 }
 \tag{L-91017.5}
\]

Taking norms yields

\[
\begin{aligned}
 Q_{2a}(2\sigma)h_{2a}(u)^2
 ={}&Q_a(2\sigma)Q_a(2\sigma+2a)\\
 &\cdot
 [h_a(u)^2+g_{1,a}(u)^2+g_{2,a}(u)^2],
\end{aligned}
 \tag{L-91017.6}
\]

where `sigma=Re(s)`.  Both factors in this identity are exact: the first by the
sieve cocycle, the second by the paraunitary Cauchy square.

## 3. Critical-pole limit

Let `sigma=1/2+epsilon`.  Since

\[
 Q_c(1+2\varepsilon)
 =\frac{\kappa_c}{2\varepsilon}+O_c(1)
\]

and

\[
 \kappa_aQ_a(1+2a)=\kappa_{2a},
\]

multiplying (L-91017.6) by `2 epsilon/kappa_(2a)` and letting
`epsilon downarrow 0` gives

\[
 \boxed{
 h_{2a}(u)^2
 =h_a(u)^2+g_{1,a}(u)^2+g_{2,a}(u)^2.
 }
 \tag{L-91017.7}
\]

The interpretation is stronger than the scalar identity alone:

```text
the universal Hardy/pole source returns at the delayed scale
with coefficient exactly one;

the two Cauchy details are emitted into orthogonal positive ports;

no reserve is spent twice and no extra source state is hidden.
```

Thus the main-term/pole part of the desired coefficient-one recurrence is
closed at the complete Hilbert-state level.

## 4. Off-line signature is purely scattering-side

For a complex centred coordinate `z=d+ir`, replace `u` by `-iz`.  The divisor
map `V_(a,a)` remains an isometry and has no negative direction.  By
`L-91016`, all Hermitian indefiniteness is confined to the three-dimensional
factor

\[
 \mathcal R(-iz/a)^*\mathcal R(-iz/a)-I,
\]

which has signature `(1,1,0)` for `d>0` and vanishes for `d=0`.

Therefore:

\[
 \boxed{
 \text{positive source flow creates no hidden negative state;
 every off-line defect is one explicit hyperbolic scattering block.}
 }
 \tag{L-91017.8}
\]

This is the exact source/state separation required by an inertia or
Pontryagin-space consumer.

## 5. All-generation composition

The divisor maps are coassociative and the scattering matrices commute across
scales.  Hence a dyadic ladder

\[
 a,2a,4a,\ldots,2^Ja
\]

has an unambiguous all-generation tensor assembly.  The internal source state
and internal scattering state remain coefficient-one; each generation emits
exactly two new detail ports.  On the critical line,

\[
 \boxed{
 h_{2^Ja}(u)^2
 =h_a(u)^2+
  \sum_{j=0}^{J-1}
  \bigl[g_{1,2^ja}(u)^2+g_{2,2^ja}(u)^2\bigr].
 }
 \tag{L-91017.9}
\]

The state dimension does not proliferate.  Only the physically observable
detail outputs accumulate.

## 6. What remains after the exact assembly

The pole/main state is closed, the positive source cocycle is closed, the
three-state scattering is closed, and their tensor compatibility is closed.
The sole missing interface is the pole-subtracted arithmetic fluctuation
`H_a` of `L-91015` after the actual explicit-formula/window recombination.

A complete theorem must show that its windowed Hermitian coisometry has no
negative defect beyond the positive one-shot tail channel in (L-91015.7).
Equivalently, it must prove that the emitted physical detail ports pay the
pole-subtracted fluctuation without returning a same-scale signed state.

## 7. Boundary

Closed:

```text
positive source isometry;
three-state all-pass isometry;
exact commutation of source and scattering;
coefficient-one critical-pole return;
orthogonal two-port detail emission;
all-generation state composition;
localisation of every negative signature to the scattering block.
```

Open:

```text
pole-subtracted windowed coisometry;
complete prime-side detail payment;
dyadic soft-count monotonicity;
RH.
```
