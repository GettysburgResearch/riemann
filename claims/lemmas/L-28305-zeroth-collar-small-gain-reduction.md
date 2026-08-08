# L-28305 — Zeroth-collar small-gain reduction

Claim ID: `L-28305`  
Title: Once the noncollar boundary states are contractive, the complete Pascal renewal is equivalent to one explicit collar Schur-return inequality  
Status: **PROPOSED COMPLETE ABSTRACT LEMMA / APPLICATION REDUCTION PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-x`  
Created: 2026-08-08  
Dependencies: `L-28304`  
Scope: finite-state small-gain theorem; arithmetic constants remain to be produced

## 1. Two-block state

Let `X_0` be the zeroth-collar state and let `Y` contain every other current-scale
boundary state after the acyclic weighting of `L-28304`.  Write the complete
one-generation operator as

\[
 \mathcal T=
 \begin{pmatrix}
 C&B\\
 D&A
 \end{pmatrix}
 :X_0\oplus Y\longrightarrow X_0\oplus Y.
 \tag{L-28305.1}
\]

Assume the source-bound norm estimates

\[
 \|C\|\le c,
 \qquad
 \|B\|\le b,
 \qquad
 \|D\|\le d,
 \qquad
 \|A\|\le\theta<1.
 \tag{L-28305.2}
\]

Here:

```text
C  collar -> collar;
D  collar -> noncollar jet/Pascal states;
B  noncollar states -> collar;
A  complete noncollar transition.
```

## 2. Exact small-gain theorem

Suppose

\[
 \boxed{
 bd<(1-c)(1-\theta).
 }
 \tag{L-28305.3]
\]

Equivalently,

\[
 \boxed{
 c+{bd\over1-\theta}<1.
 }
 \tag{L-28305.4}
\]

Choose a positive number `r` satisfying

\[
 {b\over1-\theta}<r<{1-c\over d},
 \tag{L-28305.5}
\]

with the evident one-sided interpretation when `b=0` or `d=0`.  On
`X_0 direct_sum Y`, define

\[
 \|(x,y)\|_r=\|x\|_{X_0}+r\|y\|_Y.
 \tag{L-28305.6}
\]

Then

\[
\begin{aligned}
 \|\mathcal T(x,y)\|_r
 &\le(c+rd)\|x\|+(b+r\theta)\|y\|\\
 &\le\Theta_r\,[\|x\|+r\|y\|],
\end{aligned}
\tag{L-28305.7}
\]

where

\[
 \boxed{
 \Theta_r
 =\max\left(c+rd,\,\theta+{b\over r}\right)<1.
 }
 \tag{L-28305.8}
\]

Thus

\[
 \boxed{
 \|\mathcal T\|_r<1.
 }
 \tag{L-28305.9}
\]

This is the elementary two-block small-gain theorem.  No selfadjointness,
normality, compactness, or finite-dimensional spectral computation is used.

## 3. Schur-return interpretation

The quantity

\[
 \boxed{
 \kappa_0
 :=c+{bd\over1-\theta}
 }
 \tag{L-28305.10]
\]

is the norm majorant for one direct collar return plus every excursion through
the noncollar state:

\[
 C+B(I-A)^{-1}D.
 \tag{L-28305.11}
\]

Therefore `kappa_0<1` is the exact scalar reserve to be certified.  It is
stronger than a favorable diagonal entry and weaker than bounding the full
unweighted boundary matrix by one.

## 4. Boundary-jet application

The current exact inputs are:

1. shifted analytic bulk reserve `6/7` from PR #286;
2. eta-comb finite-jet reserve `theta_*<1` from `L-28301`;
3. local capacity-feasible eta/Pascal map from `L-28302`;
4. positive Peano sign for every order `m>=1` from `L-28303`;
5. geometric Euler top remainder `2^(-M)` from PR #286;
6. strict weighted contraction of every acyclic noncollar graph from
   `L-28304`.

Consequently the complete noncollar block `A` can be given one rational bound
`theta<1` after the exact transition manifest is topologically ordered.  The
only remaining production constants are

\[
 \boxed{c_0,b_0,d_0}
 \tag{L-28305.12}
\]

for the zeroth collar and the verification

\[
 \boxed{
 c_0+{b_0d_0\over1-\theta}<1.
 }
 \tag{L-28305.13}
\]

Call (L-28305.13), with source-bound rational enclosures for the exact finite
state, the **Zeroth-Collar Small-Gain theorem** (`ZCSG`).

## 5. Production object

A fail-closed ZCSG certificate consists of:

```text
finite state and transition manifest;
proof that the noncollar graph is acyclic after diagonal loops are removed;
rational diagonal reserves for every noncollar state;
rational weights from L-28304;
rational bounds theta,c0,b0,d0;
strict rational verification
    c0+b0*d0/(1-theta)<1;
all lower-scale and finite-collar destinations;
source and first-cell mutations.
```

No floating eigenvalue or undeclared operator norm is accepted.

## 6. Consequence

`ZCSG` gives the complete BJPR recurrence with a strict homogeneous factor.
Iteration over `O(log X)` support halvings gives a polylogarithmic boundary debt.
The exact Cycle-Debt/entropy and square-screw/Landau consumers then yield RH as
stated in `T-28301`.

## 7. Proof boundary

Closed exactly:

- two-block small-gain theorem;
- explicit weighted contraction norm;
- Schur-return interpretation;
- reduction of BJPR to four rational constants after noncollar typing.

Open:

- the exact zeroth-collar transition ledger;
- rational production bounds `c0,b0,d0,theta` satisfying ZCSG;
- RH.
