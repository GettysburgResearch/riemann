# R-30405 — The scalar parity coefficient is not a physical norm contraction

Claim ID: `R-30405`  
Title: The coefficient `1-eta(1/2)<1` governs only the zero-frequency Möbius–Riesz coordinate; every zeta-zero mode has parity multiplier exactly one  
Status: **EXACT SCOPE REFUTATION / REQUIRED PHYSICAL PIVOT**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Dependencies: `L-30407`; elementary Dirichlet eta algebra  
Scope: translation-invariant physical contractions derived solely from the parity renewal; source-specific reflected or boundary-coupled estimates are not refuted

## 1. Full complex-parameter recurrence

`L-30407` proves for every `Re(s)>0`

\[
\boxed{
\sigma_{N,s}(m)
={1\over m^s}
\left[
-M_s(N/m)
+[1-\eta(s)]M_s(Q/m)
+1-2^{1-s}
\right],}
\tag{R-30405.1}
\]

where

\[
M_s(y)=\sum_{d\le y}{\mu(d)\over d^s},
\qquad
Q=\left\lfloor{N+1\over2}\right\rfloor.
\]

At the real critical exponent this gives the strict scalar coefficient

\[
\rho_2=1-\eta(1/2)\in(0,1).
\tag{R-30405.2}
\]

## 2. Physical oscillations change the coefficient

A logarithmic frequency `t` replaces the critical source weight `m^(-1/2)` by

\[
m^{-1/2-it}.
\]

Thus the child coefficient seen by that physical mode is not `rho_2`, but

\[
\boxed{
\mathfrak r(t)
=1-\eta(1/2+it).}
\tag{R-30405.3}
\]

More generally an exponential mode with horizontal displacement `delta` sees

\[
\boxed{
\mathfrak r_\delta(t)
=1-\eta(1/2+\delta+it).}
\tag{R-30405.4}
\]

Equation (R-30405.4) follows directly from (R-30405.1); no asymptotic passage is
used.

## 3. Every zeta zero saturates the renewal

The eta function satisfies

\[
\eta(s)=(1-2^{1-s})\zeta(s).
\tag{R-30405.5}
\]

The finite factor has no pole in the critical strip. Therefore, at every
nontrivial zeta zero `rho`,

\[
\boxed{
\eta(\rho)=0,
\qquad
1-\eta(\rho)=1.}
\tag{R-30405.6}
\]

Consequently:

- a critical-line zero `rho=1/2+i gamma` gives
  \[
  \mathfrak r(\gamma)=1;
  \tag{R-30405.7}
  \]
- a hypothetical off-line zero
  `rho=1/2+delta+i gamma` gives
  \[
  \mathfrak r_\delta(\gamma)=1.
  \tag{R-30405.8}
  \]

The parity renewal is exactly noncontracting on every zero mode, irrespective of
its horizontal location.

## 4. Refutation of a direct norm upgrade

Let `H` be any translation-invariant Hilbert or Banach norm on logarithmic
signals for which exponential modes are tested by their Fourier/Laplace
multipliers. Suppose one attempts to deduce from (R-30405.2) an estimate

\[
\|\mathcal T f\|_H
\le\theta\|f\|_H+\text{tempered defect},
\qquad\theta<1,
\tag{R-30405.9}
\]

where `T` is the parity child operator and the defect has smaller exponential
growth than a tested zero mode.

Insert a mode corresponding to a zeta zero. By (R-30405.6), its leading
coefficient is unchanged. The two sides of (R-30405.9) have the same leading
mode on the left and only `theta<1` times that mode on the right; the tempered
defect cannot supply the missing fixed proportion. This is a contradiction.

Thus the implication

```text
rho_2=1-eta(1/2)<1
-> uniform physical parity contraction
```

is false.

This obstruction already applies to known critical-line zeros. It is not a
conditional argument assuming RH is false.

## 5. Relation to the pole-canceling carry-window obstruction

The same factorization explains `R-26902`. The parity/carry analysis function
contains a factor of `zeta(s)`, while the inverse-zeta source contains
`1/zeta(s)`. Their product is regular at a zero, and the resulting renewal
multiplier equals one.

The coefficient recurrence remains valuable in source coordinates, but its
physical norm upgrade must retain data outside the pure eta/carry channel.

## 6. Corrected production theorem

A valid continuation must use a pole-preserving physical source frame before the
eta factor is introduced. At minimum it must contain:

1. the complete independent-frequency physical block;
2. a boundary or commutator channel whose transform does not contain the common
   zeta factor;
3. the all-order positive Selberg hierarchy of `L-30409`;
4. every parity-shell cross term;
5. a Schur reserve compatible with critical-line modes;
6. a lower-scale recurrence whose tempered channel explicitly contains the
   line spectrum.

The source coefficient `rho_2` may appear inside that calculation, but it cannot
be used as the physical contraction constant by itself.

## 7. Proof boundary

Proved exactly here:

- the full oscillatory parity multiplier;
- saturation at every zeta zero;
- failure of a direct strict translation-invariant norm contraction;
- the necessity of a pole-preserving boundary/physical channel.

Not refuted:

- a reflected source-specific Schur inequality retaining the physical boundary;
- a critical-order observability theorem with an explicit tempered line channel;
- RH.
