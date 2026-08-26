# T-102780 — Outer-ray extrapolation is the exact remaining filtered arithmetic frontier

Claim ID: `T-102780`  
Status: **MAJOR UNCONDITIONAL NORMAL-FORM ADVANCE; RH UNPROVED**  
Created: 2026-08-22  
Base: PR #719  
RH status: **unproved**

The completion-defect programme has already established:

```text
one native source and one fixed common mother;
Euler/half-divisor gauge equivalence;
owner/transfer first-chaos cancellation;
polylogarithmic squared and higher-prime-power costs;
subpower source diagonals and same-product multiplicity;
full filtered SHARP-disk positivity;
one post-filter S-lemma slack;
exact common-carrier cancellation;
one-octave localization and strict channel contraction.
```

`L-102738--L-102739` now solve the remaining radial matrix algebra exactly.

## 1. Exact primal and dual

The centered radial cost is one real minimization

\[
\mathfrak R(A,B,C)
=
\inf_{x\ge\max\{A,0\}}
\left[
4(x-A)+\frac1{16}
\max\left(
\frac{B^2}{x},
C+\frac{A-x}{4},
0
\right)
\right].
\]

It is also the supremum of a fixed compact family of linear source
functionals.  No latent matrix variable remains.

## 2. The conclusion scalar is one fixed outer ray

For

\[
P(w)=C+2Bw+Aw^2,
\]

the filtered Lorentz current is

\[
\boxed{
5P_2a_\tau-G_\tau
=4A-B
=\frac{P(-8)-P(0)}{16}.
}
\]

Quadratic interpolation gives

\[
P(-8)=136P(-1/2)+120P(1/2)-255P(0).
\]

Thus `TRF102750`, the Lorentz part of `OERSC102770`, and the outer-ray
increment are exactly the same scalar.

## 3. Sharpness

The rank-one dual point

\[
\begin{pmatrix}4&-1/2\\-1/2&1/16\end{pmatrix}
\]

is feasible and evaluates the ray `w=-8`.  Hence

\[
(4A-B)_-\le\mathfrak R(A,B,C).
\]

`R-102724` proves sharpness with

\[
P_*(w)=1-4|w|^2.
\]

It is nonnegative on the complete inner disk, while

\[
[P_*(-8)-P_*(0)]/16=-16.
\]

Therefore no source-blind argument using only inner-disk positivity or the
local S-lemma matrix can orient the final scalar.

## 4. Exact remaining theorem

Define

```text
OER102780:
  after exact deterministic-carrier subtraction, source-region recombination,
  owner/gauge recombination and one-octave localization, the fixed outer-ray
  increment [P(-8)-P(0)]/16 has subpower logarithmic negative mass.
```

Then

\[
\mathrm{OER}_{102780}
\Longleftrightarrow
\mathrm{TRF}_{102750}
\Longrightarrow
\mathrm{FLC}_{102730}
\Longrightarrow
\mathrm{AR\!-\!DEFECT}_{102600}
\Longrightarrow
\mathrm{RH}.
\]

The equivalence is an exact coordinate identity; the conclusion arrows use the
already-proved source and Mellin interfaces.

```text
radial primal reduction                  PROVED EXACT
compact SDP dual                         PROVED EXACT
outer-ray identity                       PROVED EXACT
three-ray extrapolation coefficients     PROVED EXACT
sharp source-blind countermodel          PROVED EXACT
OER102780                                OPEN / RH-BEARING
Riemann Hypothesis                       UNPROVED
```