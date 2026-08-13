# L-91356 — Positive target-exact, score-superordinate maps fix the equality ray

Claim ID: `L-91356`  
Status: **PROVED EXACT CONE-RIGIDITY THEOREM**  
Created: 2026-08-13  
Depends on: the two physical functionals `t=(1,2)` and `s=(2,1)`  
RH status: **unproved**

## 1. Setup

Let

\[
 M=\begin{pmatrix}a&b\\c&d\end{pmatrix}
 \in\mathbb R_{\ge0}^{2\times2}.
\]

The SHARP target and endpoint-score functionals are

\[
 t=(1,2),
 \qquad
 s=(2,1).
\]

Assume

\[
 \boxed{tM=t}
\tag{L-91356.1}
\]

and

\[
 \boxed{sM\ge s}
\tag{L-91356.2}
\]

componentwise.

## 2. Equality-column rigidity

The first-column target equation is

\[
 a+2c=1.
\tag{L-91356.3}
\]

The first-column score inequality is

\[
 2a+c\ge2.
\tag{L-91356.4}
\]

Eliminating `a=1-2c` gives

\[
 2-3c\ge2.
\]

Since `c>=0`, one must have

\[
 \boxed{c=0,\qquad a=1.}
\tag{L-91356.5}
\]

Thus every positive target-exact, score-superordinate map fixes the pure equality
ray pointwise:

\[
 \boxed{Me_1=e_1.}
\tag{L-91356.6}
\]

This is not a property of one proposed matrix; it is forced by the extremal
score-to-target ratio of the equality ray.

## 3. Complete classification

The second-column target equation is

\[
 b+2d=2,
\]

so

\[
 d=1-\frac b2.
\]

Positivity gives

\[
 0\le b\le2.
\]

The second-column score is then

\[
 2b+d=1+\frac32b\ge1,
\]

so no further restriction occurs. Consequently

\[
\boxed{
 M=\begin{pmatrix}
 1&b\\
 0&1-b/2
 \end{pmatrix},
 \qquad0\le b\le2.
}
\tag{L-91356.7}

Conversely every matrix in (L-91356.7) is nonnegative, target exact and
score-superordinate.

## 4. Exact-score corollary

If score is also conserved exactly,

\[
 sM=s,
\]

then the second-column score equation gives

\[
 1+\frac32b=1,
\]

and hence

\[
 \boxed{b=0,\qquad M=I_2.}
\tag{L-91356.8}

Therefore:

\[
\boxed{
 \text{the identity is the unique positive map conserving both target and score.}
}
\tag{L-91356.9}

## 5. Consequences for rough-prime return architectures

Any nontrivial positive state return which moves the equality input into the
reserve coordinate has `c>0` and is therefore incompatible with simultaneous
target exactness and score superordination.

In particular, the target overdraw of `R-91310` is not repaired by searching for
a nearby positive two-state matrix with the same qualitative mixing.  A valid
rough reset must instead use at least one of:

```text
measure-valued source splitting before physical observation;
an additive current packet with explicitly charged score debt;
a higher-dimensional packet cone whose observation is not a positive 2x2 map;
a signed local correction controlled by an independent positive port.
```

The theorem explains why the live measure-valued causal-packet route is the
correct scope after the binary-return refutation.

## 6. Proof boundary

```text
positive target-exact score-superordinate cone      CLASSIFIED EXACTLY
equality ray fixed                                  EXACT
exact target and score imply identity               EXACT
nontrivial positive two-ledger state return         IMPOSSIBLE IN 2D
measure-valued causal packet typing                 OPEN / LRPT
Riemann Hypothesis                                  UNPROVEN
```
