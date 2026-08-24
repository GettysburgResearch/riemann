# T-105610 — Moving-carrier and actual-Turán source collapse the physical-transfer ledger

Claim ID: `T-105610`  
Status: **MAJOR EXACT SOURCE REDUCTION; PHYSICAL RESTRICTION OPEN**  
Created: 2026-08-24  
Depends on: `T-105600`, `L-105610--L-105613`, `R-105610`; sibling PR #731  
RH status: **unproved**

## 1. Two former approximation layers are gone

The previous differential-microscope transfer was organized schematically as

```text
freeze completed-zeta carrier
 -> construct positive reciprocal coefficients
 -> transfer a frozen numerator
 -> pay carrier drift
 -> restrict to the physical one-sided frame.
```

`L-105610--L-105613` prove that the first four items can be reorganized
exactly.

### Denominator / reciprocal source

For

\[
q={1\over L_\xi-A_\zeta},
\]

the actual moving carrier has the exact resolution

\[
q-hq'
=\int_0^\infty e^{-uL_\xi(s)}
\sum_nc_u(n)
(1+h\log n+h uL_\xi'(s))n^{-s}\,du,
\qquad c_u(n)\ge0.
\tag{T-105610.1}
\]

The complete carrier phase is common at each `u`, so the phase-uniform
one-sided Hardy theorem applies without freezing. The only adverse term is the
scalar drift

\[
{h|L_\xi'(s)|\over
 (\Re L_\xi(s)-A_\zeta(\sigma))^2}.
\tag{T-105610.2}
\]

A single prime-two coefficient beats this debt on every far right safe line.

### Numerator / actual Xi source

For

\[
m={\Xi\over\Xi'},
\qquad
\mathcal T_\Xi=\Xi'^2-\Xi\Xi'',
\qquad
J_\Xi=\Im(\Xi\overline{\Xi'}),
\]
the hyperbolic derivative is exactly

\[
\boxed{
{h m'(z)\over\Im m(z)}
={h\mathcal T_\Xi(z)\over J_\Xi(z)}
 {\overline{\Xi'(z)}\over\Xi'(z)}.
}
\tag{T-105610.3}
\]

Moreover

\[
\widehat{\mathcal T_\Xi}(\xi)
={1\over4\pi}
\int(2u-\xi)^2\Phi(u)\Phi(\xi-u)\,du
\ge0.
\tag{T-105610.4}
\]

Thus the numerator is already the actual positive theta exterior-square source
used independently by PR #731. There is no frozen-to-actual numerator theorem
to prove.

## 2. The reduced physical gate

The pointwise and averaged programmes now share the literal actual pair

```text
positive numerator:          T_Xi;
denominator/current:         J_Xi and conjugate(Xi')/Xi'.
```

Define the reduced gate:

```text
MCTPHYS105610 — moving-carrier Turan physical restriction

Realize the exact Laplace-resolved reciprocal source and the actual Xi
exterior-square source in one source-owned smooth one-sided frame, and prove
that

  pole/seam transport,
  horizontal endpoints,
  taper conditioning,
  reciprocal-tail truncation,
  denominator whitening,
  and physical two-trace identification

consume less than the integrated phase-uniform reserve.
```

Carrier freezing, carrier-phase approximation, reciprocal-coefficient
reconstruction, an operator-valued archimedean drift and frozen-numerator
transfer are **not** members of this gate.

If `MCTPHYS105610` supplies the pointwise physical trace, then

\[
\mathcal C_{0,b}(a,h)\le0
\qquad
(0\le b\le1/2,\ a\in\mathbb R,\ h>0),
\]

and `T-105444` gives RH.

If it supplies only the averaged denominator/Turán frame bounds, it feeds the
robust proportion theorem on sibling PR #731. The two outputs differ in norm,
not in source.

## 3. Exact actual scalar target

In every region with `J_Xi>0`, the strongest pointwise normal form is

\[
\boxed{
h|\mathcal T_\Xi(z)|\le J_\Xi(z).
}
\tag{T-105610.5}
\]

The directional microscope needs only

\[
\boxed{
h\Re\left(
\mathcal T_\Xi(z)
 {\overline{\Xi'(z)}\over\Xi'(z)}
\right)
\le J_\Xi(z).
}
\tag{T-105610.6}
\]

The robust-frame programme is an averaged denominator-whitened version of the
same inequality.

## 4. Firewall

`R-105610` proves that positivity of either source by itself is insufficient.
The finite positive Fourier model

\[
1+{1\over2}\cos z
\]

has a positive exterior-square source but a positive differential microscope
at `z=pi+i log 2`. The denominator all-pass orientation and the physical
restriction are indispensable.

## 5. Updated implication matrix

```text
positive moving-carrier Laplace family                 PROVED EXACT
phase-uniform integrated Hardy reserve                  PROVED EXACT
far-safe-line drift absorption                          PROVED UNCONDITIONALLY
actual Xi Turan exterior-square source                  PROVED UNCONDITIONALLY
Turan source = hyperbolic phase numerator               PROVED EXACT
frozen carrier/numerator transfer layers                REMOVED
MCTPHYS105610 physical restriction/conditioning         OPEN / RH-BEARING
DMPXFER105603                                           STRICTLY REDUCED
ROBUSTFRAME106310                                       SAME ACTUAL SOURCE / OPEN
Riemann Hypothesis                                      UNPROVEN
```

## 6. Scope

This theorem does not prove the physical restriction estimate, the shell
energy below two, the moving-saddle terminal theorem, or RH. Its advance is to
replace two moving approximation interfaces by exact positive-source
resolutions and to identify the pointwise and averaged programmes as two norms
of the same actual Xi object.