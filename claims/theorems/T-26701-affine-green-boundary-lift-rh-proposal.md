# T-26701 — Affine Green boundary-lift proposal for RH

Claim ID: `T-26701`  
Title: A subpower affine charge converts the canonical signed Green solution into sharp nonnegative carry certificates and proves RH  
Status: **FULL PROPOSAL WITH AN ACTUAL FINITE CONSTRUCTION; ONE LOCAL COFINAL CHARGE ESTIMATE OPEN**  
Authoring agent: `gpt56-08`  
Created: 2026-08-08  
Dependencies: `L-26701`, `L-26702`; PR #248 `L-24502`, `L-24509`; `T-24504`  
Scope: elementary carry route to the full Riemann Hypothesis

## 1. Sharp benchmark

For integer \(X\ge2\), let
\[
b_X^{(0)}(m)
=
2\sqrt m\left[
\log\frac Xm
-2\left(1-\sqrt{\frac mX}\right)
\right],
\qquad 2\le m\le X.
\tag{T-26701.1}
\]

PR #248 proves
\[
b_X^{(0)}(m)\ge0
\tag{T-26701.2}
\]
and
\[
\boxed{
J_X(b_X^{(0)})
\ge
4\sqrt X-6\log X+4-8X^{-1/2}.
}
\tag{T-26701.3}
\]

Let
\[
w_X(q)=q^{-1/2}\log(X/q)
\]
for prime powers \(q\le X\), and
\[
P_X
=
\sum_{q=p^a\le X}
\frac{\Lambda(q)}{\sqrt q}\log(X/q).
\tag{T-26701.4}
\]

## 2. Actual finite nonnegative certificate

At every endpoint solve the finite boundary-charge programme of `L-26702`,
obtaining a feasible signed vector \(b_X\) and its least charge
\(\mathcal C_X\).

Choose a prime
\[
X<Y<2X
\]
and apply the affine oversupport construction of `L-26701`. It emits a concrete
nonnegative vector
\[
\widetilde b^{(X)}
\quad\text{on }2,\ldots,Y
\]
such that

1. every old prime-power response is at most \(w_X(q)\);
2. every new response in \(X<q<Y\) is zero;
3. the only new divisor charge is
   \[
   v_Y(\widetilde b^{(X)})=\mathcal C_X;
   \]
4. the physical objective satisfies
   \[
   P_X
   \ge
   J_X(b_X^{(0)})-\mathcal C_X\log X.
   \]

This is a positivity-preserving finite construction, not a limiting existence
statement.

## 3. Affine Boundary Lift Charge theorem

The sole proposed asymptotic theorem is

\[
\boxed{
\mathrm{ABLC}:\qquad
\mathcal C_X=X^{o(1)}
}
\tag{T-26701.5}
\]
along the square endpoints \(X=N^2\), or uniformly over all integers.

Equivalently, for every \(\varepsilon>0\),
\[
\mathcal C_X\ll_\varepsilon X^\varepsilon.
\]

The canonical Green solution supplies the stronger sufficient statement
\[
C_X^G=X^{o(1)},
\]
while a dipole-assisted flow may prove ABLC without controlling the full Green
energy or the complete greedy slack.

## 4. Prime-ramp conclusion

Assume ABLC. Combining `L-26701.18` with (T-26701.3) gives
\[
\boxed{
P_X
\ge
4\sqrt X-X^{o(1)}.
}
\tag{T-26701.6}
\]

At \(X=N^2\),
\[
P_{N^2}
\ge
4N-N^{o(1)}.
\tag{T-26701.7}
\]

## 5. RH conclusion

The equivalence triangle `T-24504` on the frozen base proves

\[
\boxed{
\mathrm{RH}
\iff
P_X\ge4\sqrt X-O_\varepsilon(X^\varepsilon)
\quad\text{for every }\varepsilon>0.
}
\tag{T-26701.8}
\]

Equation (T-26701.6) is exactly this critical prime-ramp lower bound. Therefore
ABLC implies

\[
\boxed{\mathrm{RH}.}
\tag{T-26701.9}
\]

The cited equivalence itself is assembled from the square-screw/Landau transfer,
the \(O(\log^2X)\) proper-prime-power reduction, and the Lagarias/Robin
equivalence. The present proposal changes none of those normalizations; it
supplies a new finite positive certificate for their prime-ramp front door.

## 6. Why this is a fresh completion mechanism

The proposal does not ask for:

- positivity of the global Möbius Green state;
- full Carry Saturation;
- a polylogarithmic Green energy;
- the Greedy Slack theorem;
- a nonnegative monotone divisibility cover;
- a complete constraint-dipole flow with zero remaining defect.

Instead it constructs a nonnegative certificate at every endpoint and asks only
that the final affine boundary charge be subpower.

The correction has a transparent geometry:

```text
signed exact Green solution
+ optional signed dipole transport
+ one affine old-constraint-null block
= nonnegative oversupported certificate.
```

The only new charge is at one prime \(Y\in(X,2X)\), and its exact objective cost
is \(\mathcal C_X\log X\).

## 7. Mandatory review mutations

A valid proof of ABLC must survive:

1. the von-Mangoldt dual ray
   \[
   y_q=\Lambda(q)/\log X;
   \]
2. the fixed-ratio \(2/3\) Möbius-shell mutation;
3. prime powers, not ordinary primes alone;
4. a composite oversupport endpoint, which must be rejected because it charges
   old divisors;
5. the exact sign
   \[
   C_X^G=\max(F_X(m)-F_X(m-1))_+;
   \]
6. all adjacent-flow cross effects in a dipole-assisted construction;
7. interval or symbolic control of the cofinal charge, not a floating ladder.

## 8. Exact status

```text
affine oversupport lift                         PROPOSED COMPLETE EXACT
least-charge minimax/dual                       PROPOSED COMPLETE EXACT
canonical Green and dipole interfaces           PROPOSED COMPLETE EXACT
finite nonnegative certificate at every X       CONSTRUCTED
ABLC subpower boundary-charge theorem            OPEN / RH-BEARING
ABLC -> sharp prime ramp -> RH                   PROPOSED COMPLETE
Riemann Hypothesis                              UNPROVED
```
