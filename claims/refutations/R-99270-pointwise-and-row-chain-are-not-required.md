# R-99270 — Pointwise SHARP Harnack positivity and the row/Hall composition are not logically necessary for the scalar consumer

Claim ID: `R-99270`  
Status: **PROVED LOGICAL FIREWALL**  
Created: 2026-08-20  
RH status: **unproved**

Two overstatements are rejected.

## 1. Pointwise positivity is not the minimal producer

The T-99250 implication

\[
h(x)\ge0\text{ eventually}\Longrightarrow RH
\]

is correct, but pointwise nonnegativity is not consumed by Mellin–Landau.
`L-99270` proves that either of the following is sufficient:

\[
\int_{X/A}^{X}h(t)\frac{dt}{t}\ge0\quad\text{eventually}
\]

for one fixed `A>1`, or

\[
\int_1^Xh_-(t)\frac{dt}{t}=X^{o(1)}.
\]

Thus a future negative value of `h` would refute the pointwise route, not the
scalar Mellin programme.

## 2. The row/Hall tree is not an antecedent of the scalar theorem

The identity

\[
\int_1^\infty h(x)x^{-s-1}dx
=\frac{(1-67^{-(s+1/2)})(s+3/2)}
{s(s-1/2)\zeta(s+1/2)}
\]

follows directly from `beta`, `T`, and finite/absolute Fubini.  It does not use

```text
Q_Y(j)=T*kappa_j;
compact SHARP Hall;
normalized row-profile monotonicity;
Radon-Nikodym child thinning;
random-key ownership;
calibration coboundaries;
fixed-row noncancellation.
```

Those statements remain valuable independent mathematics and cross-checks.
Failure of one of them cannot invalidate the scalar implication of
`L-99270/L-99272`.

## 3. Required status correction

The normative T-99270 dependency graph must therefore distinguish:

```text
conclusion-facing scalar core     primitive / self-contained;
row/common-parent reconstruction  parallel cross-check only;
pointwise Harnack tail             one sufficient producer, not the unique one.
```

No claim is made that any of the weaker producers has been proved globally.
RH remains unproved.
