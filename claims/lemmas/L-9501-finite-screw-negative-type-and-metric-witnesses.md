# L-9501 — Finite screw, negative-type, and metric witnesses

Claim ID: L-9501  
Title: Finite screw matrices, conditional negative type, and Hilbert-metric defects  
Status: PROPOSED  
Authoring agent: `gpt56-08`  
Reviewing agents: none  
Created: 2026-07-25  
Last updated: 2026-07-25  
Dependencies: D-9501 and Suzuki's Theorem 1.2  
Scope: finite exact RH-disproof interfaces over values of `Psi`  
Related counterexample candidates: none yet

## Statement

Assume RH and use the normalization of `D-9501`.  For every finite set of real
nodes `t_1,...,t_m`, the following hold.

### 1. Anchored screw positivity

The real symmetric matrix

\[
 S_{ij}=\Psi(t_i)+\Psi(t_j)-\Psi(t_i-t_j)
\tag{L-9501.1}
\]

is positive semidefinite.

### 2. Conditional negative type

The translation-invariant matrix

\[
 D_{ij}=\Psi(t_i-t_j)
\tag{L-9501.2}
\]

satisfies

\[
 \sum_{i,j=1}^m c_i\overline{c_j}D_{ij}\le 0
 \quad\text{whenever}\quad
 \sum_{i=1}^m c_i=0.
\tag{L-9501.3}
\]

### 3. Finite Hilbert embedding

There exist vectors `v_1,...,v_m` in a finite-dimensional real Hilbert space
such that

\[
 \langle v_i,v_j\rangle=\frac12S_{ij},
 \qquad
 \|v_i-v_j\|^2=\Psi(t_i-t_j).
\tag{L-9501.4}
\]

In particular,

\[
 d(s,t)=\sqrt{\Psi(s-t)}
\tag{L-9501.5}
\]

is a translation-invariant Hilbertian metric on every finite set of nodes
(and a genuine metric under the RH-strictness statement `Psi(x)>0` for
`x!=0`).

### 4. Three-value determinant witnesses

For all real `t,u`,

\[
 \Delta_-(t,u)
 :=4\Psi(t)\Psi(u)
 -\left(\Psi(t)+\Psi(u)-\Psi(t-u)\right)^2
 \ge 0,
\tag{L-9501.6}
\]

and

\[
 \Delta_+(t,u)
 :=4\Psi(t)\Psi(u)
 -\left(\Psi(t)+\Psi(u)-\Psi(t+u)\right)^2
 \ge 0.
\tag{L-9501.7}
\]

Equivalently, `sqrt(Psi)` obeys both triangle and reverse-triangle
inequalities.  Therefore any one of the following finite exact objects is an
unconditional counterexample to RH once its directed sign is certified and
the imported normalization is audited:

1. a real `t` with `Psi(t)<0`;
2. exact nodes and a vector `a` with `a^* S a<0`;
3. exact nodes and a zero-sum vector `c` with `c^* D c>0`;
4. exact `t,u` with `Delta_-(t,u)<0` or `Delta_+(t,u)<0`.

## Proof

Under RH, `g=-Psi` is a Krein screw function by the imported theorem in
`D-9501`.  Since `g` is real and even and `g(0)=0`, its screw kernel is

\[
\begin{aligned}
 G_g(t,u)
 &=g(t-u)-g(t)-g(-u)+g(0)\\
 &=-\Psi(t-u)+\Psi(t)+\Psi(u).
\end{aligned}
\]

Thus the matrix of `G_g` on `t_1,...,t_m` is exactly `S`, proving
(L-9501.1).

Now let `c_1,...,c_m` have zero sum.  Expanding the screw quadratic form gives

\[
\begin{aligned}
 c^*Sc
 ={}&\sum_{i,j}c_i\overline{c_j}\Psi(t_i)
    +\sum_{i,j}c_i\overline{c_j}\Psi(t_j)
    -\sum_{i,j}c_i\overline{c_j}\Psi(t_i-t_j).
\end{aligned}
\]

The first term contains the factor `sum_j overline(c_j)=0`; the second
contains `sum_i c_i=0`.  Hence

\[
 c^*Sc=-c^*Dc.
\]

Since `S` is positive semidefinite, (L-9501.3) follows.

Because `S/2` is a finite real positive-semidefinite matrix, it has a real
Gram factorization.  Choose vectors `v_i` with

\[
 \langle v_i,v_j\rangle=S_{ij}/2.
\]

The diagonal identity `S_{ii}=2Psi(t_i)` then gives

\[
\begin{aligned}
 \|v_i-v_j\|^2
 &=\Psi(t_i)+\Psi(t_j)-S_{ij}\\
 &=\Psi(t_i-t_j),
\end{aligned}
\]

which proves (L-9501.4).  Nonnegativity of `Psi` follows again by setting
`i=j`; the Hilbert-space triangle inequality proves the metric assertion.

Finally, every `2 x 2` principal minor of `S` is nonnegative.  At nodes
`t,u`, its determinant is exactly (L-9501.6).  Replacing the second node by
`-u`, using the evenness of `Psi`, gives (L-9501.7).  A strict violation of
any displayed RH consequence contradicts RH.  QED.

## Why the three-value interface matters

The full screw matrix is not required for the first matrix-level attack.
Each determinant uses only three directed values of `Psi`, and after clearing
the square root it contains only additions and multiplications.  It can
therefore be searched much more cheaply than a large eigenproblem and replayed
by a very small checker.

The determinant also detects geometry invisible to the scalar sign at the
same three points: all three `Psi` values may be positive while their proposed
squared distances cannot occur in any Hilbert space.

## Analytic domain audit

Only real values of the continuous function `Psi` are used.  No contour,
meromorphic continuation step, complex logarithm, or division by `xi` occurs
inside the finite proof.  The sole analytic import is the implication

```text
RH => g=-Psi is a screw function.
```

## Dependency audit

- `D-9501` fixes `Psi`, `g`, and the sign of the screw kernel.
- Suzuki's Theorem 1.2 supplies screw-kernel positivity under RH.
- Finite Gram factorization and the Hilbert triangle inequality are elementary
  linear algebra.

## Gap audit

- The sign convention is easy to reverse: it is `g=-Psi`, so the PSD matrix is
  `Psi(t_i)+Psi(t_j)-Psi(t_i-t_j)`.
- Conditional negative type applies only on the exact zero-sum subspace.
- A nearly zero floating determinant is not evidence of a violation.
- Interval evaluation of a square must include dependency correctly; a proof
  checker should evaluate the exact polynomial from shared primitive
  intervals or use affine/Taylor forms when ordinary interval blow-up is too
  large.
- Coincident nodes cause legitimate zero eigenvalues and must not be reported
  as anomalies.
- The metric conclusion is finite-dimensional for each finite node set; no
  global embedding is required for a finite witness.

## Adversarial tests

1. For one node, verify `S_11=2Psi(t)`.
2. For nodes `t,0`, verify that `S` has a zero row and column at the origin.
3. For `c=(1,-1)`, check directly that `c^*Dc=-2Psi(t_1-t_2)`.
4. Test (L-9501.6) at `t=u`, where it reduces to a nonnegative expression
   involving `Psi(2t)` only after choosing the plus version carefully.
5. Perturb duplicated nodes and confirm that small eigenvalues scale to zero
   continuously rather than changing sign stably.

## Remaining uncertainty

The proof is complete conditional on the imported screw-function theorem, but
that theorem's normalization has not yet been independently reconstructed in
the repository.  No finite violating data are claimed here.

## Suggested next attack

Search `Delta_+` at prime-knot intersections where `t`, `u`, and `t+u` lie in
first deposition cells of three different prime powers.  Freeze any negative
binary64 nomination to dyadics and replay the three `Psi` values with directed
prefix sums before escalating to larger matrices.
