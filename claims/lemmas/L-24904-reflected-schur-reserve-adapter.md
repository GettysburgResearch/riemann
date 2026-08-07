# L-24904 — Reflected Schur-reserve adapter

Claim ID: `L-24904`  
Title: A source-bound reflected block supplies a genuine energy estimate only through a strictly positive Schur reserve  
Status: **PROPOSED EXACT FINITE LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Issue: #249  
Dependencies: elementary completion of squares  
Scope: finite represented source spans; no construction of the zeta-specific blocks

## 1. Block identity

Let `H` and `Z` be finite-dimensional Hilbert spaces with positive metrics `G`
and `M`. Suppose a reflected source identity can be written on the represented
span as

\[
\mathcal F(h,z)
=\langle h,Gh\rangle
+2\operatorname{Re}\langle Ch,z\rangle
+\langle z,Dz\rangle,
\tag{L-24904.1}
\]

where `D` is positive definite on `Z`.

Completing the square gives

\[
\boxed{
\mathcal F(h,z)
=
\left\|D^{1/2}z+D^{-1/2}Ch\right\|^2
+
\langle h,(G-C^*D^{-1}C)h\rangle.}
\tag{L-24904.2}
\]

The source-bound reflected reserve is the Schur complement

\[
\boxed{\mathcal R=G-C^*D^{-1}C.}
\tag{L-24904.3}
\]

## 2. Strict reserve theorem

If an exact or directed certificate proves

\[
D\succeq h_0M,
\qquad
\mathcal R\succeq\kappa_0G,
\tag{L-24904.4}
\]

for `h_0, kappa_0>0`, then

\[
\boxed{
\mathcal F(h,z)\ge\kappa_0\|h\|_G^2.}
\tag{L-24904.5}
\]

If the arithmetic identity bounds `mathcal F` above by boundary and lower-scale
ledgers, (L-24904.5) gives the reserve required in `D-24901.6`.

## 3. Why diagonal absorption is insufficient

The reflected Selberg identity of `L-9516` is exactly

\[
2E=\mathcal C_\times-\mathcal C_+-\mathcal C_-.
\tag{L-24904.6}
\]

If a proposed forcing decomposition merely identifies the full cross term
`2E` inside its right side and moves it to the left, the result is

\[
0=\text{remaining ledger}.
\]

This supplies no upper bound for `E`.

More generally, if the right side is written

\[
2\vartheta E+B,
\]

then

\[
2(1-\vartheta)E=B.
\tag{L-24904.7}
\]

A useful estimate requires

\[
1-\vartheta\ge\kappa_0>0.
\]

The Schur condition (L-24904.4) is the finite operator form of that strict
reserve.

## 4. Source-specific scope

The LMI is required only on the actual represented top-corner source span. It
need not hold for arbitrary Farey vectors. Nevertheless it must be independent
of the unknown truth of RH and may not use an off-line-zero exclusion as an
input.

A production proof object exports exact matrices or cellwise polynomial
matrices for `G,C,D`, an exact solve or rational enclosure for `D^{-1}C`, and a
strict LDL/SOS certificate for (L-24904.4).

## 5. Proof boundary

Closed exactly:

- the reflected block completion of squares;
- the strict Schur-reserve implication;
- the refutation of diagonal absorption without reserve.

Not closed:

- construction of `G,C,D` for the actual top-top packet;
- a uniform positive `kappa_0`;
- `RBC(K)`.
