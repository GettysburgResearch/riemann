# L-91319 — Every rough Euler state map has a sharp positive completion preserving SHARP and improving endpoint score

Claim ID: `L-91319`  
Status: **PROVED EXACT POSITIVE MATRIX COMPLETION — UNCOLORED PHYSICAL-COLUMN PROJECTION OPEN**  
Created: 2026-08-12  
Depends on: `L-91108`, `L-91311/L-91315`, `L-91317/L-91318`  
RH status: **unproved**

## 1. Signed rough-factor matrix

Use the diagonal states

\[
 X=L-R,
 \qquad
 Y=L-2R.
\]

For a prime `p`, put

\[
 r=p^{-1/2},
 \qquad
 a=1-p^{-1}=1-r^2,
 \qquad
 b=1-p^{-1/2}=1-r.
\]

One Euler factor acts diagonally by

\[
 X\mapsto aX,
 \qquad
 Y\mapsto bY.
\]

Returning to `(L,R)` gives

\[
 \boxed{
 M_p=
 \begin{pmatrix}
  2a-b&2(b-a)\\
  a-b&2b-a
 \end{pmatrix}
 =(1-r)
 \begin{pmatrix}
  1+2r&-2r\\
  r&1-r
 \end{pmatrix}.
 }
\tag{L-91319.1}

The upper-right entry is negative; every other entry is positive for `p>1`.
This is the projective cone obstruction isolated in `L-91317`.

## 2. Positive completion

Define

\[
 \boxed{
 N_p
 =M_p+r(1-r)
 \begin{pmatrix}
  0&2\\
  0&-1
 \end{pmatrix}.
 }
\tag{L-91319.2}

Then

\[
 \boxed{
 N_p=(1-r)
 \begin{pmatrix}
  1+2r&0\\
  r&1-2r
 \end{pmatrix}.
 }
\tag{L-91319.3}

For every `p>=5`, and hence for every rough prime `p>=59`, all entries are
nonnegative. In fact the diagonal entries are strictly positive.

Thus

\[
 \boxed{
 (L,R)\in\mathbb R_{\ge0}^2
 \Longrightarrow
 N_p(L,R)^T\in\mathbb R_{\ge0}^2.
 }
\tag{L-91319.4}

No boundary constant or asymptotic estimate enters this state-level completion.

## 3. Exact preservation of the RH-sensitive output

The all-depth SHARP output is

\[
 \Psi=L+2R.
\]

Let

\[
 w_\Psi=(1,2).
\]

The correction in (L-91319.2) lies in the kernel of this functional:

\[
 (1,2)
 \begin{pmatrix}
  0&2\\
  0&-1
 \end{pmatrix}
 =(0,0).
\]

Therefore

\[
 \boxed{
 w_\Psi N_p=w_\Psi M_p.
 }
\tag{L-91319.5}

The positive completion reproduces the exact arithmetic SHARP scalar of one
rough Euler factor. It changes only how that scalar is allocated between the
equality and reserve channels.

## 4. Endpoint entropy score strictly improves

The endpoint entropy score of a density `c_L L+c_R R` is, up to the common
factor two,

\[
 \mathfrak s(c_L,c_R)=2c_L+c_R,
\]

because

\[
 \widehat L(1/2)=2,
 \qquad
 \widehat R(1/2)=1.
\]

Let

\[
 w_S=(2,1).
\]

Then

\[
 \boxed{
 w_SN_p-w_SM_p
 =(0,3r(1-r)).
 }
\tag{L-91319.6}

Consequently, for every positive input state,

\[
 \boxed{
 w_SN_p(L,R)^T
 \ge w_SM_p(L,R)^T,
 }
\tag{L-91319.7}
\]

with strict inequality whenever `R>0`.

Thus the exact transfer which removes the negative state coefficient is not paid
by entropy debt. It creates favorable score curvature.

## 5. Minimality and uniqueness

Consider corrections supported only in the `R`-input column:

\[
 \Delta=
 \begin{pmatrix}
  0&u\\
  0&v
 \end{pmatrix}.
\]

Requiring

\[
 w_\Psi\Delta=0
\]

forces

\[
 u+2v=0.
\]

To make the negative upper-right entry of `M_p` nonnegative one needs

\[
 u\ge2r(1-r).
\]

The smallest possible choice is therefore

\[
 u=2r(1-r),
 \qquad
 v=-r(1-r),
\]

which is exactly (L-91319.2). For `p>=5`, the reduced lower-right entry remains
nonnegative:

\[
 (1-r)^2-r(1-r)
 =(1-r)(1-2r)\ge0.
\]

Hence `N_p` is the unique minimal correction in this natural one-column class
which is positive and preserves `Psi` exactly.

## 6. Colored capacity lift

All four entries of `N_p` are nonnegative. Therefore each rough child channel
may be split positively into equality and reserve outputs according to this
matrix.

`L-91318` supplies the exact affine Pascal lift on the rough color `p`:

\[
 n\mapsto p(n+1)-1,
 \qquad
 q\mapsto pq,
\]

which preserves every matched carry and radix-four detail coefficient and
amplifies the entropy score. Combining the two results gives an exact positive,
SHARP-preserving, score-favorable lift on the **colored** rough-fiber carry cone.

`L-91317` further proves that the support of every nontrivial rough branch lies
either in the already paid outer factor-54 block or below the contracted scale.

## 7. Remaining physical projection

The matrix obstruction has disappeared. The only remaining operation is the
forgetful projection from colored columns `(p,q)` and their least-prime
descendants to the single ordinary physical column `Q`.

The affine lift has nonnegative leakage into columns not carrying the selected
rough color. Several colored children cannot be superposed until this leakage is
recombined without spending one physical target column more than once.

Thus the exact frontier is now:

```text
rough support contraction                         EXACT
balanced additive endpoint port                   POSITIVE / BOUNDED
signed (L,R) Euler matrix                         POSITIVELY COMPLETED
SHARP scalar under completion                     PRESERVED EXACTLY
endpoint entropy score                            IMPROVED
colored affine Pascal capacity lift               EXACT / POSITIVE
colored-to-uncolored physical-column projection   OPEN
Riemann Hypothesis                                UNPROVED
```
