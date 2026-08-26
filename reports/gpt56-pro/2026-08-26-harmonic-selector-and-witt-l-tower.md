# Harmonic discrepancy selector and the Boolean Witt \(L\)-tower

Date: 2026-08-26  
Execution PR: #751  
Programmes: #743, #736, #737  
Status: **new exact reductions; RH unproved**

This continuation is based on the connected Kummer/Wick-half-source head
`98af0db6ec7f77d6333a77a3dac53c4698852f43`.

Two new source structures emerge.

First, reciprocal phase-cardinality weights

\[
w_p\propto\frac1{p-1}
\]

give the unique atomically optimal one-phase discrepancy selector after
repeated labelled copies of each numerical prime are combined. An
exponential race realizes the same weights through one global random prime
ordering. This avoids the bilateral product phase cardinality while retaining
every interaction coefficient exactly.

Second, the fully \(U\)-rough Boolean half-source is a two-state transfer with
eigenvalues \(\pm1/2\), and cofinally its reduced cores have at most three
prime factors. Its twisted Euler product is not one isolated \(L\)-function:
it is the exact Witt tower

\[
\prod_{m\ge1}L(u^m,\chi^m)^{-\gamma_m}.
\]

The tower classifies the principal and quadratic-root resonances intrinsically.

Over \(\mathbf F_q[T]\), every complete nonprincipal half-source shell has
normalized square-root size. This closes deep-core family shells under the
explicit conductor/degree inequality in `T-106213`.

For the number field, the live implication matrix is

```text
HSMALL106210
AND HROUGH106210
  -> WKSFSC106150
  -> BCI102990
  -> RH.
```

Both first gates remain open.
