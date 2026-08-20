# L-100162 — Log-interval coarea reduces critical activation debt to three endpoint Euler weights

Status: **PROVED EXACT KERNEL IDENTITY; SCOPE OF ENDPOINT TERMS REPAIRED**  
Created: 2026-08-20  
RH status: **unproved**

For the partial-activation correction in `L-100161`, write

\[
d(z)={(\sqrt z-1)^2\over z^{3/2}},\qquad z>1.
\]

Its logarithmic antiderivative is

\[
\boxed{
\int d(z){dz\over z}
={2\over z}-{2\over\sqrt z}-{2\over3z^{3/2}}+C.
}
\tag{L-100162.1}
\]

Equivalently, for one source integer `n` and endpoint variable `x<n`, putting `z=n/x` gives boundary primitives

\[
\boxed{
2{x\over n}-2{\sqrt x\over\sqrt n}
-{2\over3}{x^{3/2}\over n^{3/2}}.
}
\tag{L-100162.2}
\]

Thus the logarithmic integral of the entire signed upper-ideal correction over any activation interval is an exact linear combination of endpoint parity sums at Dirichlet exponents

```text
1, 1/2, 3/2.
```

## Correct analytic classification

The `3/2` term is absolutely convergent.  The exponent-`1` term is **not** absolutely convergent; for the duplicate-67 source it is controlled by the classical prime number theorem through

\[
\sum_{n\le X}{\beta(n)\over n}\longrightarrow0,
\qquad
\sum_n{\beta(n)\over n^s}={1-67^{-s}\over\zeta(s)}.
\]

It carries no open-strip RH obstruction, but it may not be discarded as an absolutely convergent error.  The exponent-`1/2` endpoint is the unique RH-critical member of the three-term coarea identity.

Therefore interval integration localizes the conclusion-producing obstruction to the half-order endpoint while leaving:

- one PNT-controlled exponent-`1` boundary term;
- one absolutely convergent exponent-`3/2` boundary term.

No estimate for only the latter two can remove the half-order residue.
