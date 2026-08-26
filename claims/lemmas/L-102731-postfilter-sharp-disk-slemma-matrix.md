# L-102731 — The full filtered SHARP disk has one exact post-filter S-lemma matrix

Claim ID: `L-102731`  
Status: **PROVED EXACT MATRIX CONSEQUENCE**  
Created: 2026-08-23  
Depends on: `L-102729`; `L-102728`  
RH status: **not assumed**

Fix a completion time `tau` and physical scale `X`.  For

\[
 z=-1+w,
 \qquad |w|\le\frac12,
\]

put

\[
 \mathcal P_\tau(w;X)
 =JP_2Q_{\tau,-1+w}(X).
\]

By `L-102729`,

\[
 \mathcal P_\tau(w;X)\ge0
 \qquad(|w|\le1/2).
\]

Let

\[
 A=P_2a_\tau(X),
 \qquad
 G=G_\tau(X),
 \qquad
 P_0=JP_2Q_{\tau,-1}(X).
\]

Expanding the shifted quadratic around `z=-1` gives

\[
 \boxed{
 \mathcal P_\tau(w;X)
 =P_0+2\Re(w)B+A|w|^2,
 \qquad
 B=G-A.
 }
 \tag{L-102731.1}
\]

The three rays of `L-102728` are simply the values of this polynomial at
`w=-1/2,0,1/2`.

## 1. Exact S-lemma matrix

For a real Hermitian quadratic nonnegative on the disk `|w|<=1/2`, the exact
S-lemma gives one number `lambda>=0` such that

\[
 \boxed{
 \begin{pmatrix}
  A+\lambda & B\\
  B & P_0-\lambda/4
 \end{pmatrix}
 \succeq0.
 }
 \tag{L-102731.2}
\]

Equivalently,

\[
 A+\lambda\ge0,
 \qquad
 P_0-\frac\lambda4\ge0,
\]

and

\[
 \boxed{
 (A+\lambda)
 \left(P_0-\frac\lambda4\right)
 \ge B^2.
 }
 \tag{L-102731.3}
\]

The slack `lambda` belongs to one source occurrence at one `(tau,X)`.  It is
not a separate reserve for the activation and wavelet rows.

## 2. Exact relation to the Lorentz coordinate

The conclusion-facing current is

\[
 5A-G=4A-B.
 \tag{L-102731.4}
\]

Thus the filtered Lorentz problem is now a fixed support functional of the
single matrix (L-102731.2), not an unknown cone-preservation problem.

A useful deterministic lower estimate follows from

\[
 |B|\le
 \sqrt{(A+\lambda)(P_0-\lambda/4)}
 \le
 4(A+\lambda)+\frac1{16}(P_0-\lambda/4),
\]

which gives

\[
 \boxed{
 4A-B
 \ge
 -\frac{255}{64}\lambda
 -\frac1{16}P_0.
 }
 \tag{L-102731.5}
\]

This estimate is intentionally not advertised as a closure: `P_0` contains the
common affine carrier.  That carrier cancels only in the complete barycentric
combination of `T-102750`.

## 3. Centered matrix

Let `C_tau(X)` be the exact common affine carrier from `T-102750` and put

\[
 P_0^\circ=P_0-C_\tau.
\]

The coefficients `A` and `B` are already carrier-free because they are
obtained from differences of the same shifted quadratic family.  Hence all
conclusion-bearing carrier transport has been reduced to the lower-right entry
of one matrix.

Define the centered radial correction

\[
 \eta_\tau(X)
 =
 \inf\left\{
 \eta\ge0:
 \exists\lambda\ge0,
 \begin{pmatrix}
  A+\lambda & B\\
  B & P_0^\circ+\eta-\lambda/4
 \end{pmatrix}\succeq0
 \right\}.
 \tag{L-102731.6}
\]

This is a source-owned scalar measure of the exact amount of filtered disk
positivity lost when the common affine carrier is removed once.  It is the
matrix form of the centered three-ray fluctuation.

No bound for `eta_tau` is proved here.