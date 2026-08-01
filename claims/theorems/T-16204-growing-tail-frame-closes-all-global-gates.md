# T-16204 — One growing exact-radical tail frame closes all global gates

Claim ID: `T-16204`  
Status: **PROVED CONDITIONAL TRANSFER THEOREM; GROWING FRAME HYPOTHESIS OPEN**  
Authoring agent: `gpt56-pro-12`  
Created: 2026-07-31  
Depends on: `L-16206`, `L-16210`, `L-16211`, `T-16203`

## 1. Purpose

The four-gate program separated:

1. a fixed low tail-profile theorem;
2. a global target floor;
3. a background complement gap;
4. a source/background coupling estimate.

This separation is artificial. If the finite CCM space is represented by one
complete exact-radical source frame and its zero-side Weil matrix scalarizes in
the corresponding omitted-tail metric, then the floor, gap, and cross control
all follow from the same Loewner estimate.

The only substantive remaining theorem is therefore a **growing source-frame
profile and conditioning theorem**.

## 2. Finite exact-radical frame

For each `lambda`, let `V_lambda` be the finite CCM Fourier space used in the
positive diagonal criterion. Assume the support length is chosen away from the
finite zeta-cycle obstruction of `L-16211`, so that

```text
P_N Sigma_mu E(S_0^ev)=V_lambda.                         (T-16204.1)
```

Choose exact-radical sources

```text
f_(1,lambda),...,f_(m_lambda,lambda)                     (T-16204.2)
```

whose projected arithmetic images form a basis of `V_lambda`. Let

```text
D_lambda                                                   (T-16204.3)
```

be their ordinary omitted-tail Gram, and let

```text
A_lambda                                                   (T-16204.4)
```

be the localized Weil matrix. By `L-16206`, `A_lambda` is exactly the omitted
tail zero-side matrix.

Let `G_lambda>0` be the production Hardy or ordinary coefficient Gram.

## 3. Tail hierarchy

Let

```text
0<delta_1<=delta_2<=...<=delta_(m_lambda)                (T-16204.5)
```

be the generalized eigenvalues of `(D_lambda,G_lambda)` after the two exact
source constraints. Assume the repaired target `p_lambda` is `G`-normalized and
satisfies

```text
<p,Dp>_G=O(d_4(lambda)),                                  (T-16204.6)
```

and the complete target complement satisfies

```text
boxed:
D_lambda-mu_D G_lambda
 >=c_D d_8(lambda)G_lambda
 on p_lambda^perp.                                       (T-16204.7)
```

Equivalently, the first target scale is `O(d_4)` and the next complete frame
scale is bounded below by `c_Dd_8`.

For a prolate-adapted growing frame, the stronger expected statement is

```text
delta_1=Theta(d_4),
delta_2=Theta(d_8),
delta_j>=c d_8 for j>=2.                                 (T-16204.8)
```

## 4. Complete relative scalarization

Assume there are `a_lambda>0` and `epsilon_lambda->0` such that

```text
boxed:
||D_lambda^(-1/2)
  (A_lambda-a_lambda D_lambda)
  D_lambda^(-1/2)||_op
 <=epsilon_lambda a_lambda.                              (T-16204.9)
```

Equivalently,

```text
(1-epsilon_lambda)a_lambda D_lambda
 <=A_lambda
 <=(1+epsilon_lambda)a_lambda D_lambda.                  (T-16204.10)
```

This is the growing-packet analogue of the fixed-profile local Weyl theorem.

## 5. Global floor and gate 2

Equation (T-16204.10) gives

```text
boxed:
A_lambda>=0.                                              (T-16204.11)
```

Thus one may take the global floor

```text
L_lambda=0.                                               (T-16204.12)
```

The actual target Rayleigh value satisfies

```text
mu_lambda
 <=(1+epsilon_lambda)a_lambda mu_D
 =O(a_lambda d_4).                                       (T-16204.13)
```

Therefore

```text
boxed:
mu_lambda-L_lambda=O(a_lambda d_4).                      (T-16204.14)
```

Gate 2 is automatic.

An affine scalar term `sigma_lambda G_lambda` may be included throughout; then
take `L_lambda=sigma_lambda` and apply the theorem to
`A_lambda-sigma_lambda G_lambda`.

## 6. Complete complement gap and gate 3

For `x perp_G p_lambda`, (T-16204.7)--(T-16204.10) imply

```text
<x,(A-mu G)x>
 >=[(1-epsilon)a(mu_D+c_Dd_8)-mu] <x,Gx>.                (T-16204.15)
```

Using `mu=O(ad_4)` and `d_4/d_8->0`,

```text
boxed:
g_complete,lambda
 >=(c_D/2)a_lambda d_8(lambda)                           (T-16204.16)
```

for every sufficiently large `lambda`.

This is stronger than a separately postulated background gap: it covers the
entire finite target complement. Gate 3 is automatic.

## 7. Cross block and gate 4

Let `S_lambda` be any `D_lambda`-invariant low source sector containing the
target and first repaired complement, and let `B_lambda` be its
`G`-orthogonal high-frame complement. Generalized `D/G` eigenvectors make the
leading scalar form `aD` block diagonal.

Write

```text
A=aD+R.                                                   (T-16204.17)
```

From (T-16204.9),

```text
|<x,Ry>|
 <=epsilon a
   sqrt(<x,Dx>)sqrt(<y,Dy>).                             (T-16204.18)
```

The diagonal blocks satisfy

```text
A_SS>=(1-epsilon)aD_SS,
A_BB>=(1-epsilon)aD_BB.                                  (T-16204.19)
```

Hence the source/background energy angle of `T-16203` obeys

```text
boxed:
kappa_lambda<=epsilon_lambda/(1-epsilon_lambda)->0.       (T-16204.20)
```

Thus the cross block is harmless in the invariant relative-energy geometry.
The former absolute requirement

```text
eta_lambda^2=o(g_source g_background)                    (T-16204.21)
```

is unnecessary and can fail on high-energy vectors even when the Schur angle
tends to zero. Gate 4 is replaced by the stronger-in-use and weaker-in-assumption
statement (T-16204.20).

If an absolute `G`-norm gate is nevertheless desired on a spectrally truncated
background satisfying `D_B<=C_B d_max G_B`, then

```text
eta^2
 <=epsilon^2 a^2
   ||D_S||_G ||D_B||_G,                                  (T-16204.22)
```

which gives (T-16204.21) whenever the declared spectral-width ratio is controlled.
It is not needed for the RH transfer.

## 8. Ground-line convergence

Combining (T-16204.14) and (T-16204.16),

```text
boxed:
(mu_lambda-L_lambda)/g_complete,lambda
 =O(d_4/d_8)=O(lambda^-8).                               (T-16204.23)
```

The Rayleigh-floor identity `L-15107` gives the finite ground-line correction.
With the source-specific Hardy Gram of `L-16208` and the target projection tail,
the positive diagonal criterion `T-15103` follows.

## 9. How to obtain complete scalarization

For a fixed packet, `L-16210` proves (T-16204.9) from a fold-admissible profile.
For a growing frame one needs constants uniform in `m_lambda`. A sufficient
package is:

```text
A. a normalized profile representation at scale R_lambda->infinity;
B. a uniform frame Gram cI<=D_profile<=CI;
C. logarithmic moment bounds uniform in frame dimension;
D. matrix variation and horizontal-shift budgets
   V_lambda+U_lambda=o(R_lambda/log m_lambda);            (T-16204.24)
E. a matrix Riemann--von Mangoldt error whose operator norm is o(log R_lambda).
```

The precise dimension factor depends on whether one uses trace, row-sum, or
operator-valued variation estimates. It must be retained explicitly.

## 10. Generic support is not quantitative conditioning

`L-16211` proves algebraic finite surjectivity away from zeta cycles. It does not
prove a uniformly conditioned source basis. The smallest singular value of the
projected arithmetic source map can collapse near an exceptional length.
Therefore the complete remaining theorem is:

```text
boxed:
Choose a cofinal support/cutoff schedule and construct a uniformly conditioned
growing exact-radical source frame satisfying (T-16204.7), (T-16204.9), and the
source Hardy approximation gates.                       (T-16204.25)
```

## 11. Strategic consequence

After the fixed repaired profile theorem, gates 2--4 should not be attacked as
independent estimates. They are all consequences of (T-16204.25).

The four original gates have been reduced to two nested profile problems:

```text
fixed two-profile theorem
 -> proves the mode-4/mode-8 source mechanism;

growing complete-frame theorem
 -> proves the global floor, complete gap, and cross stability.             (T-16204.26)
```

## 12. Proof boundary

The transfer theorem is exact. The growing-frame profile, conditioning, and
complete tail hierarchy are not proved. Those statements contain the remaining
global difficulty and may be equivalent in strength to positivity of the
cofinal localized Weil operators. No RH proof is claimed.
