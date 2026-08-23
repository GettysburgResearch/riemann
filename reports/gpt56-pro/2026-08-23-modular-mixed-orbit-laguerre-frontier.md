# Modular mixed-orbit attack on the fixed Xi''' -> Xi'' bridge

## Outcome

The T104540 publication retry succeeded.  The direct fixed-order bridge of T104550 is now refined to one fully typed modular matrix.

The desired new implication is

\[
\alpha_2\ge\alpha_3>0.9873.
\]

It follows if

\[
\Xi'''(t)^2-\Xi''(t)\Xi''''(t)\ge0
\]

for every real `t`, or asymptotically at all but a zero-density subset of the real zeros of `Xi'''`.

## Exact source reduction

The Jacobi mother

\[
\mathcal A(u)=e^{u/2}\vartheta(e^{2u})
\]

is even and satisfies

\[
\Phi={1\over4}(D^2-1/4)\mathcal A.
\]

The positive orbit expansion

\[
u^2\Phi(u)=\sum_{n\ge1}g_n(u)
\]

converges with every polynomial weight.  For `F_n=widehat(g_n)`, the complete Laguerre profile is

\[
\sum_{m,n}
\left[
F_m'F_n'-{1\over2}(F_mF_n''+F_nF_m'')
\right].
\]

This is one common all-frequency matrix.  No product or cross term is omitted.

## Exact no-go

The two-frequency fixture

\[
F_1=\cos t,
\qquad
F_2={1\over2}\cos2t
\]

has positive diagonal Laguerre expressions but a negative complete Laguerre expression at `t=pi`.  Therefore the following shortcuts are invalid:

```text
prove every individual theta orbit is good;
sum diagonal energies;
use scalar trace positivity;
control cross terms only after absolute values.
```

The remaining theorem must preserve the complete mixed source.

## What is now finite

The theta orbit moments satisfy

\[
M_{n,j}\ll_J n^{J+4}e^{-\pi n^2}.
\]

Hence the mixed matrix tail is exponentially small uniformly in `t`.  Every fixed compact height can therefore be certified by a finite directed matrix plus an explicit tail.

The asymptotic theorem still requires a cofinal margin or a direct modular Gram.  A fixed cutoff is not enough because the finite-block margin may approach zero as the height grows.

## Two next attacks

### Modular integration-before-splitting

Use

\[
\Phi={1\over4}(D^2-1/4)\mathcal A
\]

inside the complete associated kernel and integrate by parts before any theta-orbit decomposition.  The target is a coefficient-one Gram or one Schur complement for the full modular source.

### Cofinal directed margin

Produce `T_j -> infinity` and cutoffs `N_j` such that

\[
\min_{|t|\le T_j}\mathbf1^T\mathbf T_{N_j}(t)\mathbf1
>
C N_j^C e^{-\pi N_j^2}.
\]

The intervals must cover every sufficiently large real zero of `Xi'''`; isolated verified boxes do not imply a proportion theorem.

## Status

```text
T104540 exact historical packet             pushed
T104550 fixed-order orientation bridge      proved
L104531 modular source/exhaustion            proved
L104532 complete mixed matrix                proved
L104533 compact certification                proved
R104516 diagonal shortcut                    refuted
MTSG104560                                   open
alpha_2 >= alpha_3 from alpha_3              not yet established
RH                                           unproved
```
