# L-101003 — Conjunctive source-cover principle

Claim ID: `L-101003`  
Status: **PROVED ABSTRACT COMPOSITION THEOREM**  
Created: 2026-08-20  
RH status: **not assumed**

Let a conclusion-facing scalar admit an exact decomposition

\[
F=F_{\rm closed}+F_{\rm open}.
\]

Assume

\[
\int_2^\infty |F_{\rm closed}(X)|\frac{dX}{X}<\infty
\tag{L-101003.1}
\]

and

\[
\int_2^Y(F_{\rm open}(X))_-\frac{dX}{X}=Y^{o(1)}.
\tag{L-101003.2}
\]

Then

\[
\boxed{
\int_2^Y(F(X))_-\frac{dX}{X}=Y^{o(1)}.
}
\tag{L-101003.3}
\]

This follows from

\[
(F_{\rm closed}+F_{\rm open})_-
\le
|F_{\rm closed}|+(F_{\rm open})_-.
\]

The theorem is elementary, but it is the correct logical type for the live
programme: conclusion-producing estimates are often **hyperedges**, not single
arrows.

Exact instantiations include:

```text
smooth wavelet sector + rough largest-prime sector;
zero-moment Type-I sector + balanced Vaughan sector;
finite squared small-prime core + oriented large-prime collar;
positive current source + signed one-use calibration.
```

A claimed composition is valid only after the two pieces are shown to be an
exact source partition on the same normalization.  Source mass, target mass,
or a diagnostic decomposition cannot replace equality of the conclusion-facing
scalar.
