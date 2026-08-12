# L-91025 — The three-state Cauchy all-pass is the symmetric square of one two-state rotation

Claim ID: `L-91025`  
Status: **EXACT REPRESENTATION-THEORETIC SIMPLIFICATION**  
Created: 2026-08-12  
Depends on: `L-91013`  
RH status: **unproved**

## 1. The elementary two-state rotation

For `a>0` and real `u`, define

\[
 \boxed{
 R_a(u)=\frac1{\sqrt{a^2+u^2}}
 \begin{pmatrix}
 a&u\\
 -u&a
 \end{pmatrix}.
 }
 \tag{L-91025.1}
\]

Then `R_a(u)` is an orthogonal rotation. In the orthonormal symmetric-square basis

\[
 e_1^2,\qquad \sqrt2e_1e_2,\qquad e_2^2,
\]

its symmetric-square representation is

\[
 \boxed{
 S_a(u)=\frac1{a^2+u^2}
 \begin{pmatrix}
 a^2&\sqrt2au&u^2\\
 -\sqrt2au&a^2-u^2&\sqrt2au\\
 u^2&-\sqrt2au&a^2
 \end{pmatrix}.
 }
 \tag{L-91025.2}
\]

It satisfies

\[
 S_a(u)S_a(u)^T=I_3,
 \qquad
 \det S_a(u)=1.
\]

## 2. Fixed conjugacy to the Cauchy matrix

Put

\[
 c=\frac{\sqrt5+\sqrt3}{4},
 \qquad
 s=\frac{\sqrt5-\sqrt3}{4},
\]

so that `c^2+s^2=1`, and define the fixed orthogonal matrix

\[
 \boxed{
 O=\begin{pmatrix}
 c&0&s\\
 0&1&0\\
 -s&0&c
 \end{pmatrix}.
 }
 \tag{L-91025.3}
\]

Let `U_a(u)` be the three-state all-pass matrix of `L-91013`. Direct multiplication gives

\[
 \boxed{
 U_a(u)=O\,S_a(u)\,O^T
 \qquad(a>0,u\in\mathbb R).
 }
 \tag{L-91025.4}
\]

The conjugating matrix is independent of both scale and frequency.

## 3. Minimal spectral content

The eigenvalues of `R_a(u)` are

\[
 \frac{a+iu}{\sqrt{a^2+u^2}},
 \qquad
 \frac{a-iu}{\sqrt{a^2+u^2}}.
\]

The symmetric-square eigenvalues are therefore

\[
 \boxed{
 1,
 \qquad
 \frac{a+iu}{a-iu},
 \qquad
 \frac{a-iu}{a+iu},
 }
 \tag{L-91025.5}
\]

which are exactly the eigenvalues of `U_a(u)`.

Thus the apparent three-state system has only one genuine scalar phase. The neutral coordinate is the mixed tensor of the two conjugate one-dimensional phases.

## 4. Consequence for CJHI

Any completed source-side colligation for the Cauchy gate may be constructed at the two-state level and lifted functorially by the symmetric-square representation:

```text
one two-state completed contraction
 -> symmetric square
 -> one neutral returned state
    plus the reflected conjugate innovation pair.
```

There is no need to solve an arbitrary three-by-three matrix interpolation problem. Conversely, a failure of contractivity in the two-state factor cannot be repaired by the symmetric-square lift.

The remaining source-to-boundary theorem is therefore equivalent to constructing one scalar/2-state completed Cauchy colligation compatible with the generalized-Jordan divisor isometry.

## 5. Boundary

```text
two-state rotation                              EXACT
symmetric-square matrix                         EXACT
fixed orthogonal conjugacy to U_a               EXACT
minimal one-phase spectral content              EXACT
completed two-state source colligation          OPEN / RH-EQUIVALENT
Riemann Hypothesis                              UNPROVED
```