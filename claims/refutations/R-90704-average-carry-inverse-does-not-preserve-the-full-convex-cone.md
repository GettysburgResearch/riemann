# R-90704 — Average-carry inversion does not preserve the full decreasing-convex cone

Claim ID: `R-90704`  
Status: **EXACT RATIONAL COUNTEREXAMPLE**  
Created: 2026-08-11  
Depends on: the exact average-carry matrix  
Scope: refutes a generic cone theorem; it does not refute square-root CHS

## 1. The target

At endpoint \(E=60\), take the linear hinge

\[
h(q)=(61-q)_+
\qquad(2\le q\le60).
\tag{R-90704.1}
\]

This target is nonnegative, strictly decreasing on its support, and discretely convex:

\[
h(q)-2h(q+1)+h(q+2)\ge0.
\tag{R-90704.2}
\]

Let \(c(n)\) be its unique average-carry inverse,

\[
h(q)=\sum_{n=q}^{60}c(n)\beta_{nq}.
\tag{R-90704.3}
\]

## 2. Exact negative coefficient

Backward triangular substitution over \(\mathbb Q\) gives

\[
\boxed{c(11)=-\frac2{55}<0.}
\tag{R-90704.4}
\]

For calibration, neighbouring exact values include

\[
c(10)=\frac{53}{45},
\qquad
c(12)=\frac{131}{33},
\tag{R-90704.5}
\]

so the negative value is not a numerical conditioning artefact or a broad sign convention error.

The retained standard-library checker verifies every row identity in (R-90704.3) exactly with `Fraction` arithmetic.

## 3. Consequence

The following proposed shortcut is false:

```text
h is nonnegative, decreasing and discretely convex
-> every average-carry inverse coefficient is nonnegative.
```

Since the square-root hinge belongs to this cone, CHS cannot be proved by a source-blind total-positivity or cone-preservation theorem at this level of generality.

By `L-90705`, the square-root coefficient is instead a positive weighted sum of these signed linear-hinge responses. Its positivity must exploit the specific square-root weights and cancellation across endpoints.

## 4. Exact boundary

```text
generic decreasing-convex inverse positivity     false
first retained exact witness                      E=60, n=11
square-root weighted response sum                 open
CHS and RH                                        unproved
```
