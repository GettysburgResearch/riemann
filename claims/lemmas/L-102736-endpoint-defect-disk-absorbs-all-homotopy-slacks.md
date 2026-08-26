# L-102736 — The endpoint completion-defect disk absorbs all homotopy slacks

Claim ID: `L-102736`  
Status: **PROVED EXACT HOMOTOPY-COMPRESSION THEOREM**  
Created: 2026-08-23  
Depends on: `L-102729--L-102733`  
RH status: **not assumed**

For the filtered tangent disk write

\[
 \mathcal P_\tau(w;X)
 =P_{0,\tau}+2B_\tau\Re w+A_\tau|w|^2
 \ge0
 \qquad(|w|\le1/2).
\]

Integrate the complete homotopy **before** choosing an S-lemma slack:

\[
 \overline{\mathcal P}(w;X)
 =
 \int_0^1\mathcal P_\tau(w;X)\,d\tau.
 \tag{L-102736.1}
\]

By linearity and `L-102722`, this is exactly the filtered endpoint defect
between the squared completion and the native source.  It remains nonnegative
throughout the full disk.

Put

\[
 \bar A=\int_0^1A_\tau d\tau,
 \qquad
 \bar B=\int_0^1B_\tau d\tau,
 \qquad
 \bar P_0=\int_0^1P_{0,\tau}d\tau.
\]

Then

\[
 \overline{\mathcal P}(w)
 =\bar P_0+2\bar B\Re w+\bar A|w|^2.
\]

## 1. One endpoint S-lemma slack

There exists a single `bar lambda>=0` such that

\[
 \boxed{
 \begin{pmatrix}
 \bar A+\bar\lambda&\bar B\\
 \bar B&\bar P_0-\bar\lambda/4
 \end{pmatrix}\succeq0.
 }
 \tag{L-102736.2}
\]

No measurable selection of pointwise homotopy slacks is required.

The integrated Lorentz current is exactly

\[
 \int_0^1(4A_\tau-B_\tau)d\tau
 =4\bar A-\bar B.
 \tag{L-102736.3}
\]

## 2. Endpoint centered radial cost

Let `bar C(X)` be the exact endpoint affine carrier obtained by integrating
`L-102732.2`, and put

\[
 \bar P_0^\circ=\bar P_0-\bar C.
\]

Define `bar mathfrak R(X)` from the same centered PSD optimization as
`T-102760`, but with the endpoint coefficients
`(bar A,bar B,bar P_0^circ)`.

Then

\[
 \boxed{
 (4\bar A-\bar B)_-
 \le
 \bar{\mathfrak R}(X).
 }
 \tag{L-102736.4}
\]

Moreover, convexity and subadditivity give

\[
 \boxed{
 \bar{\mathfrak R}(X)
 \le
 \int_0^1\mathfrak R_\tau(X)\,d\tau.
 }
 \tag{L-102736.5}
\]

Thus the endpoint formulation is never more expensive than the time-resolved
radial ledger.

## 3. Sharpened frontier

Define

```text
ERSC102736:
  after exact carrier, source-region, owner and gauge recombination,

  integral_1^Y bar(mathfrak R)(X) dX/X = Y^o(1).
```

Then

\[
 \boxed{
 \mathrm{ERSC}_{102736}
 \Longrightarrow
 \mathrm{TRF}_{102750}
 \Longrightarrow
 \mathrm{RH}.
 }
 \tag{L-102736.6}
\]

By `L-102733--L-102735`, the endpoint cost remains sublinear under exact source
partition and reduces to four one-octave source packets on each dyadic physical
horizon.

The final arithmetic object can therefore be taken to be one fixed endpoint
completion defect, with no homotopy parameter in the conclusion-facing
estimate.