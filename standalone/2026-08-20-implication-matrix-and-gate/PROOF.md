# A two-ended implication matrix for the factor-67 critical envelope

## Status

This document proves the source algebra, the two-ended convex decomposition,
the exhaustive two-witness classification, and the implication to RH.  It does
not prove the two long-collar arithmetic witness estimates.  RH remains
unproved.

## 1. Opposite owner decompositions

Let `U_i` be commuting scale shifts, `0<r_i<1`, and

\[
E_{1:k}=\prod_{i=1}^k(I-r_iU_i).
\]

Write

\[
L_i=\prod_{h<i}(1-r_h),\qquad
R_i=\prod_{h>i}(1-r_h),\qquad
s_k=\prod_h(1-r_h).
\]

Direct coefficient comparison gives

\[
\begin{aligned}
E_{1:k}={}&s_kI
+\sum_i r_iL_iR_i(I-U_i)\\
&+\sum_{i<j}r_ir_jL_iR_j
(I-U_i)(I-U_j)E_{i+1:j-1}.
\end{aligned}
\tag{1}

The coefficients are the probabilities of zero successes, one success, or
least and greatest successes `(i,j)` in independent Bernoulli trials of
parameters `r_i`; hence they are nonnegative and sum to one.

For the centered cubic carrier

\[
\Psi(y)=64\begin{cases}
3y-y^{3/2},&y\le1,\\
3\sqrt y-1,&y\ge1,
\end{cases}
\]

`Psi` and every one-prime difference are nonnegative.  Thus only the interval
terms in (1) can contribute to the negative part.

## 2. Stable joint collar measure

Put

\[
\pi_{ij}=r_ir_jL_iR_j,
\qquad
H_{ij}=(I-U_i)(I-U_j)E_{i+1:j-1}\Psi.
\]

Then

\[
(E_{1:k}\Psi)_-
\le\sum_{i<j}\pi_{ij}(H_{ij})_-.
\tag{2}

The two outside survivals must remain together.  Deleting the entire right
survival from a row energy gives a divergent sum at `X=1`; this is proved in
`R-100616`.

If one constructs source-owned certificates `A_ij,B_ij>=0` with

\[
(H_{ij})_-^2\le A_{ij}B_{ij},
\]

then

\[
(E_{1:k}\Psi)_-
\le
\sqrt{
\left(\sum_{i<j}\pi_{ij}A_{ij}\right)
\left(\sum_{i<j}\pi_{ij}B_{ij}\right)
}.
\tag{3}

Equation (3) is the exact least-owner/greatest-owner AND port.

## 3. Quadratic-envelope cell calculus

For a finite labelled prime multiset `B`, define

\[
S_\sigma(x)=\sum_{P_A\le x}(-1)^{|A|}P_A^{-\sigma},
\qquad
\bar S_{3/2}=\prod_{q\in B}(1-q^{-3/2})-S_{3/2}.
\]

The quadratic envelope is

\[
\mathcal E_B(x)=
16\bar S_{3/2}+24x^{-1/2}S_1-9x^{-1}S_{1/2}.
\tag{4}

Between activations,

\[
\mathcal E_B'(x)
=-3x^{-2}(4\sqrt xS_1-3S_{1/2}).
\tag{5}

At an activation product `d`, the jump is

\[
\mathcal E_B(d)-\mathcal E_B(d^-)
=-b_B(d)d^{-3/2},
\tag{6}

where `b_B(d)` is the signed multiplicity of that product.

Every minimum is therefore exactly one of:

1. a downward activation with `b_B(d)>0`;
2. an interior point in a cell with `S_1<0` and `S_(1/2)<0`.

The latter point is

\[
x_*=(3S_{1/2}/4S_1)^2,
\]

and its sign is equivalent to

\[
S_1^2+\bar S_{3/2}S_{1/2}\le0.
\tag{7}

Hence the two statements

```text
AEP: all downward activation endpoints are nonnegative;
DNT: every actual interior witness satisfies (7)
```

are jointly equivalent to `E_B(x)>=0` for all `x`.

## 4. Conclusion

Absolute convergence at exponent `3/2` passes the finite statement to the
complete prime source.  The Mellin transform of the resulting envelope is
regular at every positive real point and retains every pole arising from a
zeta zero with real part greater than one half.  Therefore Landau's theorem
and the functional equation give

\[
\boxed{AEP\ \wedge\ DNT\Longrightarrow RH.}
\]

The repository already proves AEP/DNT in the root, singleton, empty-interior,
ratio-eight, fixed power-width, fully-active, and finite-completion corridor
regions.  Long mixed actual-prime collars remain open.  No further detector or
transport theorem is missing after those two witness classes.