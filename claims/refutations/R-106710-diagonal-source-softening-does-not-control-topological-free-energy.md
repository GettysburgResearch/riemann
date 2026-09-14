# R-106710 — Diagonal source softening does not control the topological free-energy factor

Claim ID: `R-106710`  
Status: **PROVED EXACT SCOPE FIREWALL**  
Created: 2026-08-27  
Depends on: `L-106674`, `L-106710`, `T-106700`  
RH status: **unproved**

`L-106710` proves that, at the frequency-adapted scale `lambda_xi=2/xi`, the
fifth antiphase density is asymptotic to one tenth of the physical source
scale. This does not prove the full endpoint free-energy estimate.

## 1. The operation is nonlocal

The physical quotient is

\[
U_{5,\lambda}(t)
=\frac{A_{5,\lambda}(t)+i\lambda\mathcal L_5(t)}
       {A_{5,\lambda}(t)-i\lambda\mathcal L_5(t)}
\]

up to the fixed sign convention. Its boundary unimodularity and winding use a
single positive scalar `lambda` (or a positive analytic real-boundary scale)
in physical space. The assignment

\[
\lambda\mapsto\frac2\xi
\]

inside the Fourier convolution is a pseudodifferential multiplier. It is not a
physical companion homotopy, does not define the same inner quotient, and does
not carry the reverse--Rolle index.

## 2. The free energy has a forced unit spectrum

For every reduced physical endpoint quotient, `L-106674` gives

\[
\det(I-\tau Q)
=(1-\tau)^d\det(I-\tau Q_{\rm bal}),
\qquad
 d=(m_--m_+)_+.
\]

Hence

\[
\mathfrak F_\tau
=c(\tau)d+\mathfrak F_{\tau,\rm bal},
\qquad
c(\tau)=\frac{-\log(1-\tau)}\tau.
\]

No estimate of a diagonal Fourier density can delete the `d` unit eigenvalues.
Globally this index is the reverse--Rolle loss `R_5-R_0` up to the declared
ledger. Bounding it below `97/1000 N` is already the new ninety-percent
zero-count theorem.

## 3. Exact countermodel boundary

The family `F_n=c+cos(nt)` in `R-106700` has a positive even source, positive
fifth-Wronskian source, real simple fifth-derivative zeros, carrier-matched
scale and vanishing finite pole height, while its endpoint charge equals two
per period. It fails the Xi conditional-difference concentration used in
(L-106710.14): its decisive source interaction couples the zero mode directly
to the carrier.

Thus Xi conditional concentration is genuinely new information, but a valid
proof must still transfer it through the physical outer factor and retain the
unit topological spectrum. A coefficient-level or diagonal-density argument
alone cannot establish the source-Pick determinant lower bound.
