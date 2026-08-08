# L-23702 — A near-saturating nonnegative carry minorant implies RH

Claim ID: `L-23702`  
Title: Sharp first moment and logarithmic control of any feasible nonnegative carry vector supply the complete `4 sqrt(X)` prime-ramp cancellation and imply RH  
Status: **PROPOSED EXACT CONDITIONAL LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Dependencies: `L-23701`; the square-screw/Landau transfer on PRs #202/#218  
Scope: deduction from a finite carry certificate; no claim that the certificate estimates are already proved

## 1. Average binomial entropy

Retain

\[
G_n=rac1{n+1}\sum_{j=0}^n\log {n\choose j}.
\]

For `0<j<n`, put `x=j/n`. The `j`-th mass of a `Binomial(n,x)` law is
maximal, hence is at least `1/(n+1)`. Therefore

\[
{n\choose j}x^j(1-x)^{n-j}\ge\frac1{n+1}
\]

and

\[
\log {n\choose j}
\ge nH(x)-\log(n+1),
\tag{L-23702.1}
\]

where

\[
H(x)=-x\log x-(1-x)\log(1-x).
\]

The concavity of `H`, its endpoint values, and one trapezoid comparison give

\[
\frac1{n+1}\sum_{j=0}^n H(j/n)
\ge\frac12-rac3n.
\tag{L-23702.2}
\]

Consequently

\[
\boxed{
G_n\ge\frac n2-\log(n+1)-3.}
\tag{L-23702.3}
\]

The constant `3` is deliberately nonoptimal. Any absolute constant is
sufficient for the argument.

## 2. Two carry masses

Let `d_X(n)>=0` be any finite vector satisfying

\[
\sum_{n=q}^X d_X(n)\beta_{nq}\le w_X(q)
\qquad(2\le q\le X).
\tag{L-23702.4}
\]

Define

\[
\boxed{
\mathfrak M_X=\sum_{n=2}^X n\,d_X(n),}
\tag{L-23702.5}
\]

and

\[
\boxed{
\mathfrak L_X=\sum_{n=2}^X
 d_X(n)\bigl(\log(n+1)+3\bigr).}
\tag{L-23702.6}
\]

By `L-23701.14` and (L-23702.3),

\[
\boxed{
\mathcal P(X)
\ge
\frac12\mathfrak M_X-\mathfrak L_X.}
\tag{L-23702.7}
\]

This is an exact finite implication.

## 3. Near-saturation hypothesis

Assume the following two estimates for the chosen feasible vectors:

\[
\boxed{
\mathfrak M_X
\ge8\sqrt X-O(\log^A X),}
\tag{L-23702.8}
\]

and

\[
\boxed{
\mathfrak L_X=O(\log^A X)}
\tag{L-23702.9}
\]

for one fixed exponent `A`.

Then

\[
\boxed{
\mathcal P(X)
\ge4\sqrt X-O(\log^A X).}
\tag{L-23702.10}
\]

Only a lower bound is needed. The vector need not saturate every carry row, and
no sign assertion about the exact triangular inverse is used.

## 4. Square-screw transfer

The exact all-integer square-screw formula on PR #202 has the form

\[
\Psi(\log X)
=
4\sqrt X-
\sum_{q=p^k\le X}
\frac{\Lambda(q)}{\sqrt q}\log\frac Xq
+O(\log^C X),
\tag{L-23702.11}
\]

with the complete pole, gamma, and endpoint terms included in the displayed
polylogarithmic remainder. Inserting (L-23702.10) yields

\[
\boxed{
\Psi(\log X)\le O(\log^{\max(A,C)}X).}
\tag{L-23702.12}
\]

The square-sampling/Landau theorem on PRs #202/#218 then gives

\[
\Theta_\zeta=0,
\]

and functional-equation symmetry yields

\[
\boxed{\mathrm{RH}.}
\tag{L-23702.13}
\]

The exact special-function normalization remains an imported review dependency;
the carry and entropy steps above do not modify it.

## 5. Minimal sufficient asymptotic form

The polylogarithmic hypotheses may be weakened to

\[
\mathfrak M_X\ge8\sqrt X-o(\sqrt X),
\qquad
\mathfrak L_X=o(\sqrt X),
\tag{L-23702.14}
\]

provided the chosen square-screw transfer is used in its subexponential
negative-part form. The polylogarithmic version is preferred because it matches
the natural finite carry numerics and gives the cleanest one-sided screw bound.

## 6. Exact role of the greedy construction

The vector of `L-23701` is canonical, nonnegative, and feasible at every finite
endpoint. Thus the full arithmetic theorem may be stated without an existential
linear program:

\[
\boxed{
\mathfrak M_X(d^{\rm greedy})
\ge8\sqrt X-O(\log^A X),
\qquad
\mathfrak L_X(d^{\rm greedy})=O(\log^A X).}
\tag{L-23702.15}
\]

A proof of (L-23702.15) is already a complete proof of RH through the exact
chain above.

## 7. Proof boundary

Closed exactly:

- the elementary entropy lower bound;
- the prime-ramp lower bound from any feasible nonnegative carry vector;
- the reduction of RH to two aggregate carry estimates.

Open:

- the sharp aggregate estimates for the greedy vector;
- RH.