# L-96503 — The finite paired source tree is exactly the native two-row Möbius state

Claim ID: `L-96503`  
Status: **PROPOSED COMPLETE PRODUCER THEOREM**  
Created: 2026-08-17  
Depends on: `L-96501`, `L-96502`

For fixed `X`, take the finite stopping-line equality (L-96501.7). Realize each
canonical current leaf by the directed terminal Hall theorem and each outer
source with scale `x<67` by the frozen directed positive native-row certificate.
Let `D_X` be the finite direct sum of those nonnegative physical rows.

Every substitution was an exact paired-source equality before observation, and
every root occurrence has one owner. Therefore signed component-row
observation commutes with the finite sum and gives

\[
D_X(j)=c_X(j),\qquad j=2,3.
\tag{L-96503.1}
\]

Every summand of `D_X` is nonnegative in those coordinates. Consequently

\[
\boxed{c_X(2)\ge0,\qquad c_X(3)\ge0\quad(X\ge1).}
\tag{L-96503.2}
\]

The proof does not assert positivity of an oriented child, a Möbius seed, or a
rough-prefix block. Cancellation is completed inside the labelled paired
source tree before the row marginal is taken.

For audit, the exact rows also have the sparse Riesz form

\[
c_X(j)=\sum_{n\le X}{a_j(n)\over\sqrt n}\log{X\over n},
\]

with

\[
a_2(n)=\mathbf1_{n=1}-\mu(n)
 +2\mathbf1_{2\mid n}\mu(n/2)
 -\mathbf1_{3\mid n}\mu(n/3),
\]

and

\[
3a_3(n)=\mathbf1_{n=1}-\mu(n)
 -\mathbf1_{2\mid n}\mu(n/2)
 +5\mathbf1_{3\mid n}\mu(n/3)
 -3\mathbf1_{4\mid n}\mu(n/4).
\]

The finite tree and sparse Riesz formula are two exact descriptions of the same
rows; neither is an asymptotic approximation.
