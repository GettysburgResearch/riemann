# L-105472 — The endpoint jump ledger is subpower on the canonical F1 source

Claim ID: `L-105472`

Status: **PROVED FROM THE FROZEN SOURCE-DIAGONAL AND EQUAL-PRODUCT ENERGY**

Let \(a_n=\sigma_U(n)/\sqrt n\) be the recombined physical coefficients of the
canonical equal-pair Boolean source after the fixed common-mother reduction.
On every dyadic horizon the frozen source ledger gives

\[
\boxed{
\sum_{M/8<n\le2M}|a_n|^2=M^{o(1)}.
}
\tag{L-105472.1}
\]

For the half-divisor coordinates this is `L-102702.3`; for the stopped balanced
coordinates it is the free-energy plus equal-product-collapse theorem
`L-102883.1--L-102883.3`.  `T-102990`, `L-106133`, and `L-106134` transport the
same literal diagonal ledger to the canonical equal-pair source.  No estimate
between distinct physical products is imported.

## 1. Weighted coefficient jumps

Let \(E(m)\) and \(J_M(a)\) be as in `L-105471`.  Since
\(w_m\le1/(2m)\), each of the four dyadic terms in \(E(m+1)\) is bounded after
the change of variable \(m+1=2^jn\) by a constant multiple of

\[
\sum_{n\asymp M/2^j}{|a_n|\over n}.
\]

Cauchy--Schwarz and (L-105472.1) give, uniformly for \(0\le j\le3\),

\[
\sum_{n\asymp M/2^j}{|a_n|\over n}
\le
\left(\sum|a_n|^2\right)^{1/2}
\left(\sum_{n\asymp M/2^j}{1\over n^2}\right)^{1/2}
=M^{-1/2+o(1)}.
\tag{L-105472.2}
\]

Therefore

\[
\boxed{J_M(a)=M^{-1/2+o(1)}.}
\tag{L-105472.3}
\]

This is stronger than the required subpower bound.

## 2. What is and is not closed

The discontinuities of \(H\) at integers do not create atoms in the original
logarithmic `L1` observation: `K_L` is the bounded density representative
fixed in `L-102880`.  The jump filter is used only to convert a cell's left
endpoint into the right-continuous Hardy sample.

Equation (L-105472.3) closes exactly:

```text
source diagonal energy;
equal-product representation collapse;
right/left endpoint bookkeeping;
finite dyadic jump transfers.
```

It does **not** estimate

\[
\sum_{M\le m\le2M}{|\Delta_2W(m)|\over m}.
\]

That sequence contains the correlations between different physical products
which the frozen energy theorems explicitly leave open.

## 3. Consequence

Combining (L-105472.3) with `L-105471.12--L-105471.13`,

\[
\boxed{
V_M(H)=M^{o(1)}
\quad\Longleftrightarrow\quad
\sum_{m=M}^{2M}{|\Delta_2W(m)|\over m}=M^{o(1)}.
}
\tag{L-105472.4}
\]

The equivalence is at the same frozen dyadic source and boundary convention.
