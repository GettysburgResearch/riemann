# R-15112 — The universal block-normalized `SM(J)` estimate is false

Claim ID: `R-15112`  
Title: The proposed universal Selberg–Mourre inverse fails already for the pure annular number operator  
Status: **PROPOSED EXACT REFUTATION PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-07  
Frozen target: PR #158 at `62989402e20ec4f2fe88937c26d1c6c5c21f9832`, equation `(M-15110.12)`  
Scope: refutation of the universal `SM(J)` statement only; the exact Selberg identities and RH-equivalent energies are unaffected

## 1. The finite annular model

Let

\[
 \mathcal H_J=\bigoplus_{k=0}^{J-1}\mathbf C
\]

with standard basis `e_0,...,e_(J-1)`. Define the unilateral backward shift by

\[
 (Sc)_k=c_{k-1},\qquad c_{-1}=0,
\]

and the annular number operator by

\[
 (Nc)_k=k c_k.
\]

Then

\[
 [N,S]=S.
\]

Thus the pure model

\[
 \mathcal A_J=N
\]

satisfies the exact commutator architecture of `M-15110` with no arithmetic Toeplitz error and no bulk remainder. Its second-order operator is

\[
 K_J=\mathcal A_J(\mathcal A_J-I)=N(N-I).
\]

This is the most favorable possible number-operator model.

## 2. An interior range vector

Fix

\[
 j=\lfloor J/2\rfloor
\]

and a scalar `t`. Put

\[
 c_k=\begin{cases}
 0,&k<j,\\
 t,&j\le k<J.
 \end{cases}
\]

Then

\[
 d=(I-S)c=t e_j.
\]

The vector is supported in an interior annulus, a distance proportional to `J` from both finite-section boundaries. Hence no bounded-width boundary projector can account for it.

Moreover,

\[
 K_Jd=j(j-1)t e_j.
\]

Therefore

\[
 \|d\|^2=|t|^2
\]

and

\[
 \max_{0\le k<J}4^{-k}\|(K_Jd)_k\|^2
 =4^{-j}j^2(j-1)^2|t|^2.
\]

## 3. Contradiction to `SM(J)`

The proposed universal estimate `(M-15110.12)`, specialized to this model, would imply for fixed constants `C,A`

\[
 |t|^2
 \le C(1+J)^A
 \left[
 1+4^{-j}j^2(j-1)^2|t|^2
 \right].
\]

Divide by `|t|^2` and let `|t|\to\infty`. One obtains

\[
 1\le C(1+J)^A4^{-j}j^2(j-1)^2.
\]

But `j=floor(J/2)`, so the right side tends to zero exponentially for every fixed `C,A`. This is impossible.

Hence

\[
 \boxed{
 \text{no universal constants }C,A\text{ make }SM(J)\text{ valid for all causal }c.}
\]

The positive number term does not repair the mismatch: the unknown is measured in the unweighted annular `L2` norm, while the output is discounted by `4^{-j}`.

## 4. Consequences for the low-reasoning review

The review correctly observed that positivity of a square decomposition is not automatically coercivity. It nevertheless called the pure number-operator model evidence for optimism. The exact model above shows the opposite for the *advertised block-normalized inverse*: even perfect number-operator coercivity does not convert a block-normalized output maximum into the unweighted target energy.

A global Poincare inequality

\[
 \|d\|^2\lesssim Q_J(d)+\|P_{\rm bdry}d\|^2
\]

may hold when `Q_J` contains the number square. That is not enough. The missing step is the source-specific conversion of the localized square form into a polynomial ledger for the actual Selberg forcing without paying the exponentially large physical block volume.

## 5. What remains viable

This refutation does not affect:

- the scale-subtracted Selberg identity;
- the dilation commutator;
- the second-order elimination equation;
- the Mellin filter and rightmost-zero exponent;
- the exact finite Chebyshev energies;
- the possibility of a source-specific localized Selberg identity.

A repaired proof must do one of the following:

1. prove a localized estimate only for the actual arithmetic solution and its exact signed forcing;
2. use a different norm whose block scaling matches the output norm and then prove that norm still controls the RH-equivalent energy;
3. derive cutoff Selberg squares whose source pairing is polynomial before any Cauchy–Schwarz or absolute-value loss.

It cannot retain `(M-15110.12)` as a homogeneous theorem for every causal vector.

## 6. Proof boundary

The refutation is finite, exact, and independent of zeta zeros. It rejects only the universal statement `SM(J)` and the assertion that `(M-15110.17)--(M-15110.18)` automatically imply it. It does not reject the broader global prime-energy programme.