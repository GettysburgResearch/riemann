# L-91410 — A first-entrance rough-prime reset needs no multiprime tensorization

Claim ID: `L-91410`  
Status: **PROPOSED COMPLETE ABSTRACT COMPOSITION THEOREM; ARITHMETIC PORT IDENTIFICATION REQUIRES HOSTILE REVIEW**  
Created: 2026-08-12  
Authoring agent: `gpt56-pro`  
Depends on: PR #399 at `616fc8f33c618332b30f06ff25b199d1e19beaa0`, especially `L-91114/L-91115`, `L-91317`–`L-91325`, and `T-91101`  
RH status: **unproved**

## 1. The support fact that changes the recursion

Let

\[
0.01844367547103<c_0<0.01844367547105.
\]

Every rough prime remaining after the finite block through `61` satisfies

\[
p\ge 67,
\qquad
\frac1p\le\frac1{67}<c_0.
\tag{L-91410.1}
\]

Hence, at parent scale `X`, stripping the unique least rough prime sends the
branch immediately below the next reset endpoint:

\[
\boxed{
Y_p:=X/p<c_0X.
}
\tag{L-91410.2}
\]

If an integer contains several rough prime factors, only its least rough prime
is processed in the current generation. Every remaining rough factor belongs to
the child state at scale `Y_p` and is processed in a later generation.

Consequently **there is at most one new rough-prime transition on each source
atom during one factor-54 reset**. Same-generation scalar tensorization over
distinct rough primes is unnecessary.

This does not invalidate the common Hilbert and four-state semigroups on PR
#399; it shows that the conclusion-producing reset may be proved with the
strictly simpler first-entrance ledger.

## 2. Positive source and target disintegration

Let `(E_X,mu_X)` be the positive endpoint-source measure at scale `X`, and let

\[
\mathcal T_X:E_X\longrightarrow\mathcal M_+(H_X)
\]

be the positive source-to-target Markov kernel of the factor-four endpoint
block. Thus, for every positive source measure `lambda`,

\[
\nu=\mathcal T_X\lambda
\]

is its assigned physical target measure.

Suppose the arithmetic source has the exact first-entrance decomposition

\[
\boxed{
\lambda_X
=\lambda_{X,0}+
 \sum_{p\ge67}\lambda_{X,p},
\qquad
\lambda_{X,p}\ge0,
}
\tag{L-91410.3}
\]

where every source atom occurs in exactly one summand, labelled by its least
rough prime. Define

\[
\nu_{X,b}=\mathcal T_X\lambda_{X,b}.
\]

Positivity and monotone convergence give the exact target partition

\[
\boxed{
\nu_X=\nu_{X,0}+
 \sum_{p\ge67}\nu_{X,p}.
}
\tag{L-91410.4}
\]

No branch is compared with a fresh copy of the complete target. One physical
target unit is spent exactly once.

The same statement is valid for a positive-semidefinite matrix-valued source
measure. If

\[
\mathbf K_X=\mathbf K_{X,0}+
 \sum_p\mathbf K_{X,p},
\qquad
\mathbf K_{X,b}\succeq0,
\]

then entrywise application of the scalar Markov kernel gives

\[
\boxed{
\mathcal T_X\mathbf K_X
=\mathcal T_X\mathbf K_{X,0}+
 \sum_p\mathcal T_X\mathbf K_{X,p},
\qquad
\mathcal T_X\mathbf K_{X,b}\succeq0.
}
\tag{L-91410.5}
\]

This is the correct way to transport the strict endpoint Schur port. A scalar
trace replacement is not required and is not generally valid.

## 3. One-prime branch data

For one `p>=67`, assume the resident branch construction supplies:

1. a positive completed state map `N_p`;
2. exact preservation of the native block-mass functional
   \[
   w_\Psi=(1,2),
   \qquad
   w_\Psi N_p=w_\Psi M_p;
   \tag{L-91410.6}
   \]
3. nondecrease of the endpoint score;
4. a positive child source at `Y_p=X/p`;
5. exact affine Pascal covariance on every real column;
6. a positive matrix-port split paying the projective correction before the
   child is passed to the next generation.

Items 1–5 are the exact roles of `L-91319`, `L-91318`, and `L-91324`. Item 6 is
the load-bearing interpretation of `L-91316/L-91320`; it must be checked as a
matrix-valued source partition, not merely as a lower eigenvalue estimate.

Let `d_{Y_p}` be a continuously feasible nonnegative child packing. Its affine
lift satisfies, at every physical column `Q`,

\[
\operatorname{Resp}_X(\mathcal A_pd_{Y_p};Q)
=p^{-1/2}
 \operatorname{Resp}_{Y_p}(d_{Y_p};Q/p).
\tag{L-91410.7}
\]

The assigned target share obeys the same covariance. Hence the lifted branch is
feasible against `nu_(X,p)` at all columns, including columns not divisible by
`p`.

## 4. Assembly at one reset generation

Define the parent packing

\[
\boxed{
 d_X=d_{X,0}+
 \sum_{p\ge67}\mathcal A_p d_{Y_p},
}
\tag{L-91410.8
}

where `d_(X,0)` is the already-paid outer/finite packet.

For each physical column, branch feasibility and (L-91410.4) give

\[
\begin{aligned}
\operatorname{Resp}_X(d_X;Q)
&\le \nu_{X,0}(Q)+\sum_p\nu_{X,p}(Q)\\
&=\nu_X(Q).
\end{aligned}
\tag{L-91410.9}
\]

The equality is source disintegration, not an operator-norm estimate. The
finite/continuum mismatch, B-spline collar, and terminal omission are operations
on the **summed** positive measure and are therefore charged once.

The radix-four detail constraint must be inherited from a positive detail
transport or checked through the exact real-column detail kernel. It may not be
obtained by subtracting two ordinary-column inequalities. This is the mandatory
firewall from `L-91324`.

## 5. Collapse to one contracted child state

By (L-91410.2), every child endpoint satisfies

\[
Y_p\le K_X:=\lfloor c_0X\rfloor+C.
\]

Assume the normalized component rows admit the positive scale embedding

\[
\mathcal J_{Y_p\to K_X}:
\text{positive child states at }Y_p
\longrightarrow
\text{positive states at }K_X,
\tag{L-91410.10}
\]

and that this embedding preserves feasibility and does not reduce score. The
finite factor-54 version is exactly the normalized row monotonicity proved in
`L-91322`.

Linearity gives one combined child state

\[
\lambda_{K_X}^{\rm child}
=\sum_p\mathcal J_{Y_p\to K_X}\lambda_{Y_p}.
\tag{L-91410.11}
\]

Least-prime labels make the source coefficient one: an atom is not present in
two terms of the sum.

Therefore the score loss satisfies

\[
\boxed{
\mathfrak L_X
\le
\mathfrak L_{K_X}+E_X,
\qquad
E_X=O((1+\log\log X)^A),
}
\tag{L-91410.12}
\]

provided the finite collars and the matrix-port split in Section 3 are paid at
their resident bounds.

## 6. Iteration

Since `K_X<=c_0X+C` and `c_0^-1>54`, iteration uses `O(log X)` generations.
Equation (L-91410.12) gives

\[
\mathfrak L_X
=O\bigl(\log X(1+\log\log X)^A\bigr)
=o(\log^2X).
\]

The consumer `T-91101` then yields RH.

Thus the first-entrance theorem removes the need for any same-generation
multiprime tensorization. The complete conclusion reduces to one exact local
question:

> Does the completed one-prime state plus its strict endpoint Schur port form
> the positive matrix-valued source partition required in Section 3, before
> target transport and before radix-four projection?

## 7. Proof boundary

```text
one rough prime per source atom per reset generation      EXACT
positive scalar/matrix target disintegration              EXACT
one-use target ledger                                      EXACT
coefficient-one least-prime recursion                      EXACT
formal score recurrence under branch hypotheses           EXACT
finite collars and terminal annulus                        IMPORTED
one-prime positive state map / affine covariance           IMPORTED
matrix-valued Schur-port source partition                  OPEN AUDIT JOINT
positive detail-kernel compatibility                       OPEN AUDIT JOINT
factor-54 recurrence and RH                                CONDITIONAL
Riemann Hypothesis                                         UNPROVED
```
