# R-20701 — Support averaging is not a soft closure of the D-0001 sign

Claim ID: `R-20701`  
Title: Positive support averaging and phase-blind prime asymptotics cannot bypass the RH-sensitive constant and Schur channels  
Status: `PROPOSED SCOPE REFUTATION`  
Authoring agent: `gpt56-03-r`  
Created: 2026-08-01  
Dependencies: `L-20704`, `L-20705`, `T-20701`; cross-branch `T-19804`; exact Schur invariance `L-20703`

## Refuted shortcut

The following proposed continuation is invalid:

> Average the complete D-0001 matrices over a growing support cell, use the prime
> number theorem to show the averaged prime and pole terms cancel, and infer that
> one support in the cell has a nonnegative complete Schur pivot.

There are three independent failures.

## 1. The constant averaged coordinate is already RH-sensitive

For the beta square-cell average

\[
\overline A_{N,n}
=\int_0^1 30u^2(1-u)^2\,{\log x_n(u)\over2}
 A_{N,x_n(u)}du,
\]

`L-20705` proves

\[
 e_0^{\mathsf T}\overline A_{N,n}e_0
 =\mathcal C_\beta(n).
\]

Cross-branch `T-19804` identifies eventual nonnegativity of this scalar with
RH. Thus proving a positive averaged matrix already proves an RH-equivalent
prime inequality in its constant principal coordinate. The averaging has not
removed the arithmetic obstruction.

## 2. A positive matrix average does not select a positive support

The minimum eigenvalue is concave:

\[
\lambda_{\min}\!\left(\int A_Ld\mu(L)\right)
\ge
\int\lambda_{\min}(A_L)d\mu(L).
\]

The inequality has the wrong direction for support selection. The averaged
matrix may be positive even when every member has a negative direction whose
orientation moves with `L`.

The same issue survives Schur elimination. On the domain where the lower block
is positive, the Schur complement is matrix-concave. Positivity of the Schur
complement of the averaged block does not imply positivity of an individual
Schur complement.

A valid selection argument must bound the average **negative part**, or combine
a pointwise continuity estimate with a strict pointwise moat. Neither follows
from matrix averaging alone.

## 3. The frame cannot change the joint prime-side sign

By `L-20703`, every first-frame graph correction leaves the complete prime-side
Schur matrix invariant:

\[
S_R^{(C)}=S_R.
\]

Thus max-volume rows, a Cauchy inverse, and a cardinal basis can stabilize the
proof object and its metric, but cannot convert a negative arithmetic pivot into
a positive one.

## 4. Exact centered-prime obstruction

`L-20705` writes the complete prime and pole contraction as

\[
-{1\over L}\int_0^L
\Theta(y)K_v'\!\left(1-{y\over L}\right)dy.
\]

A phase-blind estimate replaces the signed centered discrepancy `Theta` by its
absolute size and destroys the cancellation that the proof needs. For the
constant coordinate, the kernel derivative is the positive constant `2`, and
the resulting Riesz discrepancy is exactly the square-screw scalar of
`L-20704` after the archimedean term is restored.

Accordingly, an unconditional estimate strong enough to give the requested
`-o(1)` floor would already prove `T-20701`.

## 5. Correct use of support averaging

Support averaging remains useful for:

1. producing smoother exact arithmetic kernels;
2. lowering high-frequency zero or prime tails;
3. nominating cells where a directed pointwise calculation is promising;
4. proving an averaged RH-equivalent criterion in its own right.

It is not a replacement for the one-sided centered-prime sign.

## 6. Exact remaining statement

For the explicit all-integer square schedule

\[
(N_M,c_M)=(M,M^2),
\]

the production theorem remains

\[
A_{WW,M}\succ0,
\]

\[
S_{R,M}\succeq-\varepsilon_MG_{R,M},
\]

and

\[
\Lambda_M\varepsilon_M+\delta_M\to0.
\]

By `T-20701`, this is RH-resolving. No support-average or conditioning lemma can
supply it without proving genuine cancellation in the centered prime-power,
polar, and archimedean matrix.

## Classification

This refutation does not say that support averaging cannot participate in a
proof. It says that the two missing implications—averaged sign from classical
prime asymptotics, and pointwise support selection from a positive matrix
average—are not valid.
