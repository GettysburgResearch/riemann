# L-91323 — Every rough Euler action has a fixed positive three-state dilation and one minimal rank-one boundary port

Claim ID: `L-91323`  
Status: **PROPOSED COMPLETE EXACT POSITIVE-DILATION THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-12  
Depends on: `L-91316`, `L-91317`, `L-91318`  
RH status: **unproved**

## 1. The two diagonal multipliers

Let a finite rough Euler packet have diagonal mode multipliers

\[
 0<B\le A\le1.
\]

For a finite squarefree rough-prime cube `Q`, these are

\[
 A=A_Q=\prod_{p\in Q}(1-p^{-1}),
 \qquad
 B=B_Q=\prod_{p\in Q}(1-p^{-1/2}),
\tag{L-91323.1}
\]

and

\[
 d=A-B\ge0.
\tag{L-91323.2}
\]

The diagonal coordinates of `L-91311` are

\[
 X=L-R,
 \qquad
 Y=L-2R,
\]

and the Euler packet acts by

\[
 X\mapsto AX,
 \qquad
 Y\mapsto BY.
\tag{L-91323.3}
\]

Returning to `(L,R)` gives the exact physical matrix

\[
 \boxed{
 M(A,B)=
 \begin{pmatrix}
  2A-B&-2d\\
  d&2B-A
 \end{pmatrix}.
 }
\tag{L-91323.4}

The unique negative entry is the upper-right one.

## 2. Rank-one port normal form

Put

\[
 x=\binom21,
 \qquad
 e_2^*=\begin{pmatrix}0&1\end{pmatrix},
\]

and

\[
 P(A,B)=
 \begin{pmatrix}
  2A-B&0\\
  d&B
 \end{pmatrix}
 \succeq0.
\tag{L-91323.5}
\]

Then

\[
 \boxed{
 M(A,B)=P(A,B)-d\,x e_2^*.
 }
\tag{L-91323.6}

For every `L,R>=0`,

\[
\boxed{
 M(A,B)\binom LR+dR\binom21
 =
 \binom{(2A-B)L}{dL+BR}
 \in\mathbb R_{\ge0}^2.
}
\tag{L-91323.7}

The coefficient `d` is sharp among corrections constrained to the square-root
ray `x`.  Indeed, if

\[
 M(A,B)\binom LR+\tau R\binom21
 \ge0
\]

for every `L,R>=0`, then setting `L=0`, `R=1` in the first component gives

\[
 -2d+2\tau\ge0,
\]

and therefore

\[
 \boxed{\tau\ge d.}
\tag{L-91323.8}

Thus the projective cone defect is exactly one minimal scalar port.

## 3. Fixed positive three-state realization

Define the fixed observation

\[
 \boxed{
 J:\mathbb R^3\to\mathbb R^2,
 \qquad
 J(u,v,z)=\binom{u-2z}{v-z}.
 }
\tag{L-91323.9}

Define

\[
 \boxed{
 \widetilde M(A,B)=
 \begin{pmatrix}
  2A-B&0&0\\
  d&B&0\\
  0&d&A
 \end{pmatrix}.
 }
\tag{L-91323.10}

Every entry is nonnegative.  Direct multiplication gives the exact
intertwining identity

\[
 \boxed{
 J\widetilde M(A,B)=M(A,B)J.
 }
\tag{L-91323.11}

Hence the signed two-state action is the fixed observation of a positive
three-state action.

Starting from the zero-port lift `(L,R,0)`, one packet produces

\[
 \boxed{
 \widetilde M(A,B)
 \begin{pmatrix}L\\R\\0\end{pmatrix}
 =
 \begin{pmatrix}
  (2A-B)L\\
  dL+BR\\
  dR
 \end{pmatrix}
 \in\mathbb R_{\ge0}^3.
 }
\tag{L-91323.12}

The third coordinate is exactly the minimal boundary port of Section 2.

## 4. Arbitrary rough-prime composition

Let

\[
 (A_j,B_j),\qquad j=1,\ldots,k,
\]

be any finite sequence with `0<=B_j<=A_j`.  Repeated use of
(L-91323.11) gives

\[
 \boxed{
 J\widetilde M(A_k,B_k)\cdots\widetilde M(A_1,B_1)
 =M(A_k,B_k)\cdots M(A_1,B_1)J.
 }
\tag{L-91323.13}

The product on the left is entrywise nonnegative.  Thus **every finite rough
Euler cascade** admits one fixed three-dimensional positive realization.  No
stepwise projective cone conversion is required.

The positive port obeys the causal recursion

\[
 \boxed{
 z_{j+1}=(A_j-B_j)v_j+A_jz_j.
 }
\tag{L-91323.14}

Since `0<=A_j<=1`, the existing port is never amplified by a factor larger
than one at one Euler step.  New port mass is generated only from the positive
second reservoir coordinate `v_j`.

The canonical lift of a composite cube need not equal the product of the
single-factor lifts; this is irrelevant.  The fixed observation identity and
positivity survive arbitrary composition exactly.

## 5. Critical output and the remaining scalar port

The physical SHARP output is

\[
 \Psi=L+2R.
\]

In the positive three-state coordinates,

\[
 \boxed{
 \Psi=u+2v-4z.
 }
\tag{L-91323.15}

Thus the entire two-dimensional projective obstruction has become one scalar
subtraction:

\[
 \boxed{
 4z\le u+2v.
 }
\tag{L-91323.16}

Likewise the balanced state is

\[
 H_*=L+\kappa_*R
 =u+\kappa_*v-(2+\kappa_*)z.
\tag{L-91323.17}

The additive Euler boundary theorem `L-91316` supplies a strict positive
endpoint Schur port, while `L-91315` supplies the positive complementary
reserve `(2-kappa_*)R`.  The remaining rough allocation may therefore be
formulated as one scalar port-capacity comparison for `z`, rather than a
signed two-dimensional cone-conversion problem.

## 6. Compatibility with affine Pascal dilation

`L-91318` gives an exact positive affine lift of every rough child on its
colored Pascal fiber and proves entropy amplification.  Apply that affine lift
separately to each of the three positive coordinates `(u,v,z)`.

Because (L-91323.10) is entrywise nonnegative, the colored child construction
remains positive.  Because (L-91323.11) is linear, forgetting the auxiliary
state only after all colored routing recovers the exact physical `(L,R)` action.

The only unresolved operation is now:

```text
project the colored positive three-state fibers into the uncolored physical
column space while proving the scalar port inequality (L-91323.16), using the
strict endpoint Schur reserve and without spending one target column twice.
```

Support routing and score amplification are already exact in
`L-91317/L-91318`.

## 7. Verification

The companion exact `Fraction` replay checks:

```text
J Mtilde = M J for four generic rational pairs;
positivity on representative source vectors;
arbitrary two-factor composition;
rank-one port correction;
minimality of the port coefficient along (2,1).
```

Retained verdict:

```text
PASS_ROUGH_EULER_RANK_ONE_POSITIVE_DILATION
```

## 8. Proof boundary

```text
rough Euler action = positive block - rank-one port   EXACT
minimal square-root-ray port                           EXACT
fixed positive three-state dilation                    EXACT
arbitrary finite-factor composition                    EXACT
causal nonexpansive old-port recursion                  EXACT
reduction to one scalar port-capacity inequality       EXACT
colored affine carry/score lift                         AVAILABLE
uncolored column projection and port payment            OPEN / RH-BEARING
Riemann Hypothesis                                      UNPROVED
```
