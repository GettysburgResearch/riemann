# L-91335 — The rough Euler semigroup has a diagonal positive contractive four-state lift

Claim ID: `L-91335`  
Status: **PROVED EXACT POSITIVE-DILATION / CONTRACTIVE-HIDDEN-STATE THEOREM**  
Created: 2026-08-12  
Depends on: `L-91311`, `R-91306`  
RH status: **unproved**

## 1. Diagonal physical modes

Retain

\[
 X=L-R,
 \qquad
 Y=L-2R.
\]

For one rough prime put

\[
 A_p=1-p^{-1},
 \qquad
 B_p=1-p^{-1/2}.
\]

The exact Euler action is diagonal:

\[
 X\mapsto A_pX,
 \qquad
 Y\mapsto B_pY.
\tag{L-91335.1}

## 2. Positive hidden coordinates

Introduce four nonnegative coordinates

\[
 z=(X^+,X^-,Y^+,Y^-)^T\in\mathbb R_{\ge0}^4
\]

and the observation

\[
\boxed{
 Jz=
 \binom{
  2X^+-2X^--Y^++Y^-}
  {X^+-X^--Y^++Y^-}.
}
\tag{L-91335.2
}

Thus

\[
 X=X^+-X^-,
 \qquad
 Y=Y^+-Y^-,
\]

and `Jz=(L,R)^T`.

Every positive physical state has the canonical positive lift

\[
\boxed{
 I\binom LR=egin{pmatrix}L\\R\\L\\2R\end{pmatrix}.
}
\tag{L-91335.3
}

Directly,

\[
\boxed{JI=I_2.}
\tag{L-91335.4
}

## 3. Diagonal positive Euler lift

Define

\[
\boxed{
 D_p=\operatorname{diag}(A_p,A_p,B_p,B_p).
}
\tag{L-91335.5
}

Then `D_p` is entrywise nonnegative and

\[
\boxed{
 JD_p=M_pJ,
}
\tag{L-91335.6
}

where `M_p` is the exact signed `(L,R)` matrix of `L-91319`.

Indeed, `D_p` multiplies `X^+-X^-` by `A_p` and `Y^+-Y^-` by `B_p`, and (L-91335.2) is exactly the inverse change from `(X,Y)` to `(L,R)`.

Consequently, for every finite ordered prime packet `Q`,

\[
\boxed{
 J\prod_{p\in Q}D_p
 =\left(\prod_{p\in Q}M_p\right)J.
}
\tag{L-91335.7
}

No lower-triangular auxiliary port is required for the semigroup identity.

## 4. True unweighted contraction

Since

\[
 0<B_p<A_p<1,
\]

one has

\[
\boxed{
 \|D_pz\|_1
 \le A_p\|z\|_1
 <\|z\|_1
 \qquad(z\ge0).
}
\tag{L-91335.8
}

Thus the rough semigroup does possess a positive unweighted contractive lift.
`R-91306` refutes only the different lower-triangular lift `L-91327`, whose
chosen coordinates fold a boundary port into the state and thereby increase
raw mass.

For a prime path,

\[
\boxed{
 \left\|\prod_{j=1}^kD_{p_j}z\right\|_1
 \le\left(\prod_{j=1}^kA_{p_j}\right)\|z\|_1.
}
\tag{L-91335.9
}

## 5. Score and SHARP observations

The two physical functionals become

\[
\boxed{
 \Psi=L+2R
 =4X^+-4X^--3Y^++3Y^-,
}
\tag{L-91335.10
}

and

\[
\boxed{
 2L+R
 =5X^+-5X^--3Y^++3Y^-.
}
\tag{L-91335.11
}

These observations are signed. Positivity and contraction of the hidden state
do not by themselves imply positivity of `Psi` or of every physical endpoint
coefficient.

The projective corrections and observation cost are exactly the bounded common
Hilbert/endpoint port handled by `L-91333/L-91334`.

## 6. Why this lift is useful

The hidden state separates two tasks cleanly:

```text
rough least-prime branching:
    diagonal positive contraction in four coordinates;

physical (L,R) observation:
    one bounded signed port, assembled globally before color erasure.
```

Therefore source-mass subprobability should be proved in the hidden coordinates,
where it is literal, while physical endpoint feasibility is recovered once per
reset through the common endpoint port.

## 7. Proof boundary

```text
positive four-state hidden lift                     EXACT
fixed observation J and canonical injection I       EXACT
arbitrary rough-semigroup intertwining               EXACT
unweighted hidden ell1 contraction                   EXACT
false lower-triangular ell1 claim                    REMAINS REFUTED
least-prime hazard partition                         NEXT / L-91336
bounded physical observation port                    AVAILABLE
full reset composition                               OPEN
Riemann Hypothesis                                   UNPROVEN
```
