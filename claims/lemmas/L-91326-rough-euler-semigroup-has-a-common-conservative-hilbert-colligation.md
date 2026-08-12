# L-91326 — The complete rough Euler semigroup has one common conservative Hilbert colligation

Claim ID: `L-91326`  
Status: **PROPOSED COMPLETE EXACT MULTIPRIME ENERGY-COLLIGATION THEOREM — LINEAR POSITIVE ALLOCATION OPEN**  
Created: 2026-08-12  
Depends on: `L-91311`, `L-91317`, `L-91323`, `R-91303`  
RH status: **unproved**

## 1. Exact diagonalization

Retain the physical state

\[
 s=\binom LR
\]

and the diagonal Möbius modes

\[
 z=\binom XY,
 \qquad
 X=L-R,
 \qquad
 Y=L-2R.
\]

Thus

\[
 z=T^{-1}s,
 \qquad
 T^{-1}=
 \begin{pmatrix}
  1&-1\\
  1&-2
 \end{pmatrix},
 \qquad
 T=
 \begin{pmatrix}
  2&-1\\
  1&-1
 \end{pmatrix}.
\tag{L-91326.1}

A finite rough Euler packet has diagonal multipliers

\[
 0\le B\le A\le1
\]

and acts by

\[
 z\longmapsto
 D(A,B)z,
 \qquad
 D(A,B)=\operatorname{diag}(A,B).
\tag{L-91326.2}

In physical coordinates,

\[
 M(A,B)=TD(A,B)T^{-1}
 =
 \begin{pmatrix}
  2A-B&-2(A-B)\\
  A-B&2B-A
 \end{pmatrix}.
\tag{L-91326.3}

This contains the signed projective entry isolated in `L-91317`.

## 2. One common positive metric

Define

\[
 \boxed{
 H=(T^{-1})^{\!T}T^{-1}
 =
 \begin{pmatrix}
  2&-3\\
  -3&5
 \end{pmatrix}.
 }
\tag{L-91326.4}

The matrix is positive definite:

\[
 \det H=1,
 \qquad
 \operatorname{tr}H=7.
\]

Its energy is exactly the Euclidean energy of the diagonal modes:

\[
 \boxed{
 s^THs=X^2+Y^2.
 }
\tag{L-91326.5}

Since `0<=A,B<=1`,

\[
 \boxed{
 M(A,B)^THM(A,B)\preceq H.
 }
\tag{L-91326.6}

More precisely, put

\[
 u=1-A^2,
 \qquad
 v=1-B^2.
\]

Then

\[
\boxed{
 H-M^THM
 =(T^{-1})^T
  \begin{pmatrix}u&0\\0&v\end{pmatrix}
  T^{-1}
 =
 \begin{pmatrix}
  u+v&-u-2v\\
  -u-2v&u+4v
 \end{pmatrix}
 \succeq0.
}
\tag{L-91326.7}

The determinant of the defect is exactly

\[
 \boxed{uv\ge0.}
\tag{L-91326.8}

Thus every rough Euler packet is a contraction in the same fixed Hilbert metric;
no prime-dependent cone or norm is required.

## 3. Arbitrary distinct-prime composition

Let

\[
 M_j=M(A_j,B_j),
 \qquad
 P_j=M_jM_{j-1}\cdots M_1,
 \qquad
 P_0=I.
\]

Repeated insertion gives the exact telescoping defect identity

\[
\boxed{
 H-P_k^THP_k
 =\sum_{j=1}^{k}
  P_{j-1}^T
  (H-M_j^THM_j)
  P_{j-1}
 \succeq0.
}
\tag{L-91326.9
}

Every summand is positive semidefinite.  The complete multiprime defect is one
conservative sum; it never spends the parent metric twice.

Because the diagonal Euler factors commute, the final physical map is also

\[
 P_k=M\!\left(\prod_jA_j,\prod_jB_j\right).
\tag{L-91326.10}

Equation (L-91326.9), however, retains the causal branchwise allocation needed
for the reset.

This is the correct multiprime replacement for the false scalar tensorization
fenced by `R-91303`.

## 4. Explicit orthogonal dilation

For `0<=a<=1`, put

\[
 U_a=
 \begin{pmatrix}
  a&\sqrt{1-a^2}\\
  \sqrt{1-a^2}&-a
 \end{pmatrix}.
\tag{L-91326.11}

Then `U_a` is orthogonal.  The direct sum

\[
 U_{A,B}=U_A\oplus U_B
\tag{L-91326.12}

is an orthogonal dilation of `D(A,B)`.  Conjugating the observed two coordinates
by `T` supplies a conservative four-channel colligation for `M(A,B)`.

The two defect channels have squared amplitudes

\[
 (1-A^2)X^2,
 \qquad
 (1-B^2)Y^2.
\tag{L-91326.13}

Under composition, the orthogonal defect spaces concatenate exactly as in
(L-91326.9).  Distinct rough primes therefore require no independent scalar
copies of the endpoint port; they use orthogonal components of one Hilbert
defect ledger.

## 5. Bounds for the two conclusion-relevant functionals

The inverse metric is

\[
 \boxed{
 H^{-1}=
 \begin{pmatrix}
  5&3\\
  3&2
 \end{pmatrix}.
 }
\tag{L-91326.14}

For the SHARP functional

\[
 w_\Psi=(1,2),
\]

one has

\[
 w_\Psi H^{-1}w_\Psi^T=25.
\]

Hence

\[
 \boxed{
 |L+2R|^2\le25\,(X^2+Y^2).
 }
\tag{L-91326.15}

For the endpoint-score functional `w_S=(2,1)`,

\[
 w_SH^{-1}w_S^T=34,
\]

so

\[
 \boxed{
 |2L+R|^2\le34\,(X^2+Y^2).
 }
\tag{L-91326.16}

These are fixed constants independent of the number and size of the rough
primes.

## 6. Compatibility with endpoint Schur ports and color erasure

`L-91316/L-91320` provide positive-semidefinite endpoint matrix ports, and
`L-91324` proves that ordinary physical evaluation after affine Pascal lift is a
positive linear functor.  Apply that functor to every matrix in
(L-91326.9).  Positive-semidefinite order and the conservative telescoping
identity survive at every ordinary physical column.

Therefore:

```text
single-prime scalar endpoint detail            positive but non-tensorizing;
complete multiprime Hilbert defect              positive and telescoping;
ordinary physical color erasure                 preserves the matrix ledger;
source duplication                              absent in the defect sum.
```

The branchwise Hilbert defects may be embedded into the strict endpoint Schur
ports without duplicating a scalar parent port.

## 7. What this does not prove

The metric energy is quadratic.  The endpoint packing constraints and endpoint
weights are linear and coefficientwise.  A Hilbert contraction does not by
itself imply that the observed physical state remains in the positive `(L,R)`
wedge or that one row vector is coefficientwise dominated by another.

The remaining theorem is a **linearization of the conservative defect ledger**:
construct positive endpoint-row packets realizing the PSD summands in
(L-91326.9), with their ordinary/radix-four capacities and score charged to the
existing Schur-port packets.

This is narrower than the former multiprime color/duplication problem: the
complete nonlinear accumulation is already controlled by one exact identity.

## 8. Verification

The companion exact replay checks:

```text
M=T diag(A,B) T^-1;
H=(T^-1)^T T^-1;
H-M^T H M exact defect formula;
determinant uv;
three-factor telescoping;
H inverse and the constants 25,34.
```

Retained verdict:

```text
PASS_COMMON_ROUGH_HILBERT_COLLIGATION
```

## 9. Proof boundary

```text
common positive Hilbert metric                    EXACT
single-packet contraction                          EXACT
arbitrary multiprime defect telescope              EXACT
orthogonal conservative dilation                   EXACT
fixed SHARP/score energy bounds                    EXACT
ordinary physical PSD projection                   AVAILABLE
linear positive endpoint realization of defects   OPEN
coefficient-one score/capacity ledger              OPEN / RH-BEARING
Riemann Hypothesis                                 UNPROVEN
```
