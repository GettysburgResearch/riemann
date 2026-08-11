# R-90705 — Truncated geometric atoms do not have positive average-carry inverses

Claim ID: `R-90705`  
Status: **EXACT RATIONAL COUNTEREXAMPLE**  
Created: 2026-08-11  
Depends on: the exact average-carry matrix; `L-90705`  
Scope: refutes a second source-blind mixture shortcut; it does not refute square-root CHS

## 1. The tempting Hausdorff-mixture route

The square-root hinge has the positive integral representation

\[
q^{-1/2}-T^{-1/2}
=\frac1{\sqrt\pi}
\int_0^1
\bigl(x^{q-1}-x^{T-1}\bigr)
(-\log x)^{-1/2}\,dx.
\tag{R-90705.1}
\]

A natural proposed proof is therefore:

1. prove the finite average-carry inverse of every truncated geometric atom
   \[
   G_{T,x}(q)=x^q-x^T
   \qquad(0<x<1,\ 2\le q\le T)
   \]
   is coefficientwise nonnegative;
2. integrate those positive inverses against the measure in (R-90705.1).

Step 1 is false.

## 2. Exact witness

Take

\[
T=126,
\qquad
x=\frac{99}{100},
\qquad
G(q)=x^q-x^{126}.
\tag{R-90705.2}
\]

Let \(g(n)\) be the exact average-carry inverse:

\[
G(q)=\sum_{n=q}^{126}g(n)\beta_{nq}.
\tag{R-90705.3}
\]

Exact rational backward substitution gives

\[
\boxed{
-\frac{666}{10^6}<g(9)<-\frac{665}{10^6}<0.
}
\tag{R-90705.4}
\]

Numerically,

\[
g(9)=-0.0006658453476192181385\ldots.
\tag{R-90705.5}
\]

The retained verifier checks the complete rational reconstruction (R-90705.3), hashes the 250-digit numerator and 253-digit denominator of \(g(9)\), and verifies (R-90705.4) exactly.

## 3. Consequence

The following second shortcut is closed:

```text
square-root is a positive Hausdorff mixture of geometric atoms
+ every truncated geometric atom has positive inverse
-> CHS.
```

The geometric response itself becomes signed near the boundary scale \(x\uparrow1\). Hence CHS must use cancellation across the full square-root mixing measure, just as `R-90704` shows that it must use cancellation across the signed linear-hinge response kernel.

The two viable exact representations are complementary:

```text
linear-hinge coordinate:
    positive discrete second-difference weights
    against signed endpoint responses a_K(n);

geometric coordinate:
    positive Hausdorff measure
    against signed truncated-geometric responses g_(T,x)(n).
```

A proof must show that one of these specific positive averages pays its signed response—not that each atom is positive.

## 4. Exact boundary

```text
individual truncated-geometric inverse positivity    false
exact witness                                         T=126, x=99/100, n=9
square-root integral cancellation                     open / RH-bearing
CHS and RH                                             unproved
```
