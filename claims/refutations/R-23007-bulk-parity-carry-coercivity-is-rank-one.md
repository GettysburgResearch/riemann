# R-23007 — Bulk parity/carry coercivity is rank one

Claim ID: `R-23007`  
Title: Neither the positive parity comb alone nor the parity/carry bulk pair can furnish the missing source coercivity  
Status: **EXACT SCOPE REFUTATION**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-08  
Frozen parent: PR #236 at `1c9a749a1648c4772509eb3b056598c7044f4393`  
Dependencies: `L-23013`, `L-23014`  
Scope: generic bulk-frame arguments only; source-specific boundary/Green transport remains open

## 1. One positive comb has a compact actual output

For the aligned source

\[
\beta_2
=
\sum_n\frac{b_2(n)}{\sqrt n}\delta_{\log n},
\]

`L-23013` proves

\[
\operatorname{supp}(P_2*\beta_2)
\subset[0,2\log2].
\]

The source itself persists at arbitrarily large logarithmic scales and has the
full fixed-ratio Mertens/rightmost-zero exponent. Therefore no translated-tail
coercivity estimate of the form

\[
\|\beta_2\|_{\text{tail}}
\le C\|P_2*\beta_2\|_{\text{comparable tail}}
\]

can hold without an additional boundary or source term.

## 2. The two positive bulk kernels have one common zeta factor

The symbols are

\[
\widehat P_2(z)
=
\zeta(z+1/2)N_P(z),
\qquad
\widehat k(z)
=
\zeta(z+1/2)N_K(z),
\]

with explicit zero-free rational/delay factors `N_P,N_K` in the open strip.
Thus their pointwise two-channel Gram is

\[
|\zeta(z+1/2)|^2
\begin{pmatrix}
|N_P|^2&N_P\overline{N_K}\\
\overline{N_P}N_K&|N_K|^2
\end{pmatrix},
\]

whose determinant is identically zero.

Hence

\[
\boxed{
\text{the parity and carry bulk channels have no strict pointwise Schur reserve.}
}
\tag{R-23007.1}

Every hypothetical off-line zeta zero is a common null frequency. Adding the
second bulk kernel does not remove the RH mode.

## 3. What the finite-horizon inequality does and does not prove

`L-23014` proves that the two output channels are polynomially equivalent on a
finite dyadic horizon. This is useful for transporting a valid boundary reserve
between coordinates. It does not estimate the input source.

Therefore a successful continuation must obtain strictness from one of:

1. the finite boundary commutator;
2. the endpoint-projected Green correction;
3. positivity-preserving signed constraint transport;
4. a source-specific two-frequency reflected Schur complement.

A bulk multiplier or generic frame argument is excluded.

## 4. Proof boundary

Refuted:

- one-kernel translated-tail coercivity for the actual aligned source;
- a strict bulk `2x2` parity/carry Schur reserve;
- treating `L-23014.12` as source inversion.

Not refuted:

- a finite-boundary parity/Green reserve;
- signed carry dipole transport;
- a source-specific reflected inequality;
- RH.
