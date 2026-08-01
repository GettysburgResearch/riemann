# L-16201 — Exact affine-prolate falsifiers and a sufficient constrained-sector theorem

Claim ID: `L-16201`  
Status: **PROVED FINITE-DIMENSIONAL OPERATOR LEMMA; PRODUCTION ASYMPTOTICS OPEN**  
Authoring agent: `gpt56-pro-12`  
Created: 2026-07-31  
Depends on: `L-15107`, `L-15109`, `T-15102`, `T-15103`

## 1. Purpose

The desired bridge has been stated in the strong full-space form

```text
A_lambda = sigma_lambda G_lambda
           + a_lambda D_lambda + R_lambda,
D_lambda = I-K_lambda,

lambda^(2tau_lambda) ||R_lambda||_(G_lambda)
/(a_lambda d_8(lambda)) -> 0.                            (L-16201.1)
```

Here

```text
||R||_G := ||G^(-1/2) R G^(-1/2)||_op.                  (L-16201.2)
```

This lemma does two things.

1. It gives exact finite falsifiers that every full-space affine decomposition
   must pass before an asymptotic proof is attempted.
2. It proves that the full-space statement is stronger than the positive RH
   route requires. A sandwich on the constrained low prolate sector, together
   with an independently certified global floor and a Schur-controlled
   background, is sufficient.

No assertion is made here that the production CCM matrices satisfy either the
full or sector comparison.

## 2. Whitening

Let `G` be positive definite and put

```text
Ahat = G^(-1/2) A G^(-1/2),
Dhat = G^(-1/2) D G^(-1/2),
Rhat = G^(-1/2) R G^(-1/2).                              (L-16201.3)
```

Then

```text
A = sigma G+aD+R
```

is equivalent to

```text
Ahat = sigma I+a Dhat+Rhat,                              (L-16201.4)
```

and `||R||_G=||Rhat||_op`. Thus every statement may be proved in the whitened
metric and transported back by congruence.

Define the best unrestricted affine residual

```text
epsilon_*(A;G,D)
 := inf_(sigma,a in R) ||A-sigma G-aD||_G.               (L-16201.5)
```

Allowing arbitrary real `a` only weakens lower bounds. Therefore every lower
bound below also applies when the proof requires `a>0`.

## 3. Exact full-space falsifiers

### A. Commutator obstruction

For every affine decomposition with `||R||_G<=epsilon`,

```text
[Ahat,Dhat]=[Rhat,Dhat].                                 (L-16201.6)
```

Consequently

```text
||[Ahat,Dhat]||_op
 <= 2 epsilon inf_(c in R)||Dhat-cI||_op.                (L-16201.7)
```

For self-adjoint `Dhat`, twice the infimum is its spectral diameter. Hence, if
`Dhat` is not scalar,

```text
boxed:
epsilon_*(A;G,D)
 >= ||[Ahat,Dhat]||_op
    /diam(spec(Dhat)).                                   (L-16201.8)
```

Thus (L-16201.1) forces the normalized commutator to be
`o(a_lambda d_8/lambda^(2tau_lambda))`.

### B. Off-diagonal obstruction

Let `u_i` be an orthonormal eigenbasis of `Dhat`, with

```text
Dhat u_i=delta_i u_i.
```

For `i!=j`, the affine part `sigma I+aDhat` is diagonal, so

```text
boxed:
|<u_i,Ahat u_j>| <= epsilon.                             (L-16201.9)
```

In particular,

```text
epsilon_*(A;G,D)
 >= max_(i!=j)|<u_i,Ahat u_j>|.                          (L-16201.10)
```

The requested full operator theorem therefore demands superexponentially small
mixing between **every** pair of prolate modes, not only between the target and
its first constrained complement.

### C. Three-mode affine-curvature obstruction

Put

```text
alpha_i=<u_i,Ahat u_i>.
```

For three distinct model eigenvalues `delta_i,delta_j,delta_k`, define

```text
C_ijk
 =(delta_j-delta_k)alpha_i
 +(delta_k-delta_i)alpha_j
 +(delta_i-delta_j)alpha_k.                              (L-16201.11)
```

Both the scalar and linear parts cancel exactly. Therefore

```text
boxed:
|C_ijk|
 <= epsilon(
   |delta_j-delta_k|
  +|delta_k-delta_i|
  +|delta_i-delta_j|).                                   (L-16201.12)
```

Equivalently,

```text
epsilon_*(A;G,D)
 >= |C_ijk|/
   (|delta_j-delta_k|+|delta_k-delta_i|+|delta_i-delta_j|).
                                                                    (L-16201.13)
```

This is a scale- and shift-invariant finite test that the generalized diagonal
of `A` is approximately affine in the prolate defects.

## 4. Proof of the falsifiers

Equation (L-16201.6) follows because `I` and `Dhat` commute with `Dhat`. For any
real `c`,

```text
||[Rhat,Dhat]||
 =||[Rhat,Dhat-cI]||
 <=2||Rhat|| ||Dhat-cI||,
```

which proves (L-16201.7)--(L-16201.8).

Taking matrix entries of (L-16201.4) in a `Dhat` eigenbasis proves
(L-16201.9)--(L-16201.10). For the diagonal entries,

```text
alpha_r=sigma+a delta_r+r_r,
|r_r|<=epsilon.
```

Substitution into (L-16201.11) cancels `sigma` and `a`; the triangle inequality
proves (L-16201.12)--(L-16201.13). QED.

## 5. The sufficient constrained-sector theorem

The positive RH criterion does not require the full operator to be affine in
the prolate defect.

Work in the `G` metric. Let `S` be a `D`-invariant finite source sector
containing the target `p`, and let

```text
E_S = S intersect p^(perp_G)
```

with all additional source constraints imposed. Let `B` be a `G`-orthogonal
background sector such that the complete target complement is

```text
E = E_S direct_sum_G B.                                  (L-16201.14)
```

Assume the **projected** affine sandwich

```text
A_SS = sigma G_SS+aD_SS+R_S,
a>0,
||R_S||_(G_SS)<=epsilon_S.                               (L-16201.15)
```

Let

```text
mu_D = <Dp,p>_coordinates/<Gp,p>_coordinates
```

and assume the model source complement satisfies

```text
x^T(D-mu_D G)x >= g_D x^TGx,
x in E_S.                                                (L-16201.16)
```

Let `mu_A` be the actual target Rayleigh value. Then

```text
boxed:
x^T(A-mu_A G)x
 >= g_S x^TGx,

g_S:=a g_D-2epsilon_S,
x in E_S.                                                 (L-16201.17)
```

Now suppose the actual background and cross block satisfy

```text
y^T(A-mu_A G)y >= g_B y^TGy,
y in B,                                                   (L-16201.18)

|x^T(A-mu_A G)y|
 <= eta sqrt(x^TGx) sqrt(y^TGy).                         (L-16201.19)
```

Then the complete target-complement gap obeys

```text
boxed:
g_full >=
 [g_S+g_B-sqrt((g_B-g_S)^2+4eta^2)]/2.                  (L-16201.20)
```

In particular, if

```text
eta^2 <= theta g_S g_B,
0<=theta<1,                                               (L-16201.21)
```

then

```text
boxed:
g_full >=(1-sqrt(theta)) min(g_S,g_B).                  (L-16201.22)
```

## 6. Independent floor and the RH-closing condition

Assume an independent rigorous global floor

```text
lambda_min(A,G)>=L_A                                     (L-16201.23)
```

and let

```text
Delta_A:=mu_A-L_A.                                       (L-16201.24)
```

The Rayleigh-floor identity `L-15107` and the ordinary-to-Hardy support bound
give

```text
||ground-line correction||_(Hardy)^2
 <=2 lambda^(2tau) Delta_A/g_full.                       (L-16201.25)
```

Therefore the diagonal positive route closes if the target projection tail
tends to zero and

```text
boxed:
lambda^(2tau_lambda) Delta_A/g_full ->0.                 (L-16201.26)
```

A sufficient asymptotic package is

```text
Delta_A <= C a d_4+epsilon_F,                            (L-16201.27)

epsilon_S/(a d_8)->0,                                   (L-16201.28)

g_B >= c_B a d_8,                                       (L-16201.29)

eta^2/(g_S g_B)->0,                                      (L-16201.30)

lambda^(2tau) epsilon_F/(a d_8)->0.                      (L-16201.31)
```

Indeed `T-15102` gives `g_D=(176/211+o(1))d_8`, while
`d_4/d_8=Theta(lambda^-8)`. Hence (L-16201.26) follows even for
'tau_lambda->1/2`.

This sector theorem is strictly weaker than (L-16201.1): it controls only the
source block that carries the target and first constrained mode, one independent
floor scalar, the background gap, and one cross-block norm.

## 7. Proof of the sector theorem

From (L-16201.15),

```text
mu_A=sigma+a mu_D+r_p,
|r_p|<=epsilon_S.                                        (L-16201.32)
```

For `x in E_S`,

```text
x^T(A-mu_A G)x
 =a x^T(D-mu_DG)x+x^T R_Sx-r_p x^TGx
 >=(a g_D-2epsilon_S)x^TGx,
```

which proves (L-16201.17).

For `z=x+y` with `x in E_S`, `y in B`, put

```text
X=sqrt(x^TGx),
Y=sqrt(y^TGy).
```

Equations (L-16201.17)--(L-16201.19) imply

```text
z^T(A-mu_AG)z
 >=g_S X^2-2eta XY+g_B Y^2.
```

The smallest eigenvalue of the displayed `2 x 2` scalar matrix is exactly the
right side of (L-16201.20). The weaker bound (L-16201.22) follows from
`eta<=sqrt(theta g_Sg_B)` and

```text
2sqrt(g_Sg_B)XY <=g_SX^2+g_BY^2.
```

Finally apply `L-15107` with the independent floor (L-16201.23), then the Hardy
support bound. Conditions (L-16201.27)--(L-16201.31) and `T-15102` prove
(L-16201.26). QED.

## 8. Literature boundary

Connes--Consani's archimedean trace-form theorem gives an exact identity of the
shape

```text
N_I = constant * (I-K_I)
```

for a particular archimedean correction operator on a fixed small interval.
That theorem is genuine evidence for an affine-defect architecture. It does not
identify `K_I` with the standard prolate concentration operator used to define
`d_4,d_8`, and it does not give (L-16201.1) for the complete semilocal CCM Weil
matrix. In fact the same paper reports a leading eigenvalue of its `K_I` above
one, whereas a concentration operator is a positive contraction.

The later CCM paper explicitly retains the rigorous moving-prolate-to-Weil-ground
comparison as the main remaining obstacle. Thus neither the full-space
remainder estimate nor the sector conditions (L-16201.27)--(L-16201.31) are
currently imported from the literature.

## 9. Production decision rule

Before trying to prove the full statement, compute at several exact supports:

```text
commutator lower bound          (L-16201.8)
maximum prolate off-diagonal    (L-16201.10)
three-mode affine curvature     (L-16201.13)
```

and normalize each by `a d_8/lambda^(2tau)`. If any fails to decrease, the full
operator hypothesis is refuted as a proof strategy, while the constrained
sector theorem remains available.
