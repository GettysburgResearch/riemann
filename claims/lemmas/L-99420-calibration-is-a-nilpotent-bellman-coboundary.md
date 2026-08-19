# L-99420 — A primitive calibration potential is an exact nilpotent Bellman coboundary

Claim ID: `L-99420`
Status: **PROVED EXACT ALGEBRAIC COMPOSITION THEOREM**
Created: 2026-08-19
RH status: **not assumed**

## 1. Typed finite source DAG

Fix one root endpoint and one physical component row.  Let `V` be the finite
typed source DAG obtained from compact Hall and the random-key factor-67
partition.  Let `T` be its nonnegative child operator.  The endpoint decreases
along every edge, so

\[
T^{N+1}=0
\tag{L-99420.1}
\]

for some finite `N`.

At every state let

* \(E\) be the exact signed native equality frame;
* \(P\) be the positive endpoint frame retained for physical realization;
* \(A\) be the primitive signed calibration potential.

Assume the exact frame split

\[
\boxed{E=P+A.}
\tag{L-99420.2}
\]

Here \(A\) contains the retained-cell finite/continuum difference, every
activation-knot atom, and the two homogeneous Volterra boundary modes.  No sign
is imposed on \(A\).

The endpoint-nested common-parent construction is the exact positive identity

\[
\boxed{P=J+PT, \qquad J\ge0.}
\tag{L-99420.3}
\]

The same typed operator \(T\) occurs in every term.  Hall row bonuses are in
\(J\) and never enter \(T\).

## 2. Exact local identity

Substituting (L-99420.2)--(L-99420.3),

\[
\begin{aligned}
J+ET+(A-AT)
 &= (P-PT)+(P+A)T+A-AT\\
 &=P+A\\
 &=E.
\end{aligned}
\]

Therefore

\[
\boxed{
E=J+ET+\Delta_TA,
\qquad
\Delta_TA:=A-AT.
}
\tag{L-99420.4}
\]

The signed local calibration consumed by the recursive equation is not \(A\)
itself.  It is its exact Bellman coboundary \(\Delta_TA\).

## 3. Exact resolution

Since \(T\) is nilpotent,

\[
(I-T)^{-1}=I+T+\cdots+T^N
\tag{L-99420.5}
\]

is a finite nonnegative polynomial.  From (L-99420.3),

\[
P=J(I-T)^{-1}\ge0.
\tag{L-99420.6}
\]

From (L-99420.4),

\[
\begin{aligned}
E
 &=J(I-T)^{-1}
   +(A-AT)(I-T)^{-1}\\
 &=J(I-T)^{-1}+A,
\end{aligned}
\]

because

\[
(A-AT)(I-T)^{-1}=A(I-T)(I-T)^{-1}=A.
\]

Thus

\[
\boxed{
E=D+A,
\qquad
D:=J(I-T)^{-1}=P\ge0.
}
\tag{L-99420.7}
\]

Every descendant calibration contribution cancels exactly.  There is no
factor \(1/(1-\kappa)\), no leaf-count loss, and no generationwise calibration
sum.

## 4. Source and parity interfaces

Equation (L-99420.7) is source-faithful because:

1. \(T\) is the one random-key restriction of the same unnormalised residual
   source;
2. the parent-minus-child current is the complement of those restrictions and
   is nonnegative by endpoint nesting;
3. no oriented child is observed as a separate positive row;
4. no terminal Target–Lorenz orientation is selected after accumulated rough
   parity;
5. the same child operator appears in \(P\), \(E\), and \(A\).

Hence the odd-history obstruction of PR #561 and the negative ordinary
`q=2` child obstruction of PRs #512/#514 are outside the operation list.

## 5. Fail-closed boundary

The cancellation fails if different coordinatewise child operators are used,
if a Hall bonus is recursively copied, or if a local defect is inserted without
its child subtraction.  Those are statement-to-use failures, not harmless
normalisations.
