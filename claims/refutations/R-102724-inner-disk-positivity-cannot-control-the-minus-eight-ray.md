# R-102724 — Inner filtered-disk positivity cannot control the outer ray at \(w=-8\)

Claim ID: `R-102724`  
Status: **PROVED SHARP SOURCE-BLIND COUNTERMODEL**  
Created: 2026-08-22  
Depends on: `L-102738--L-102739`  
RH status: **unproved**

Consider the real Hermitian quadratic

\[
P_*(w)=1-4|w|^2.
\]

On the complete filtered disk

\[
|w|\le\frac12,
\]

one has

\[
P_*(w)\ge0.
\]

Its coefficients are

\[
A=-4,
\qquad
B=0,
\qquad
C=1.
\]

The conclusion-facing Lorentz coordinate is

\[
4A-B=-16.
\]

Equivalently,

\[
P_*(-8)=-255,
\qquad
P_*(0)=1,
\]

and

\[
\frac{P_*(-8)-P_*(0)}{16}=-16.
\]

The S-lemma completion is exact with

\[
\lambda=4,
\qquad
\eta=0,
\]

because

\[
\begin{pmatrix}
A+\lambda&B\\
B&C-\lambda/4
\end{pmatrix}
=
0.
\]

Its radial cost is

\[
\frac{255}{64}\cdot4+rac1{16}=16,
\]

which is exactly the negative Lorentz magnitude.

Thus all of the following statements are sharp:

```text
full filtered SHARP-disk positivity;
existence of one post-filter S-lemma slack;
the constants 255/64 and 1/16 in the radial gauge;
the outer evaluation point w=-8.
```

But none of them, without arithmetic source information, implies the desired
outer-ray orientation.

This countermodel is not an arithmetic refutation of `OER102780`.  It is a
binding firewall against any proof which uses only abstract positivity on the
inner disk or only the post-filter PSD matrix.