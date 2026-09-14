# L-106413 — Finite two-boundary endpoint-bank adapter

Claim ID: `L-106413`  
Status: **PROVED EXACT AT TRUNCATED FOURIER / REGULAR-WINDOW SCOPE**  
Created: 2026-08-24  
Depends on: `L-105260`, `L-105500`, `L-106400--L-106412`  
RH status: **not assumed**

Let

\[
F_L(t)=\int_0^L\Phi(u)e^{itu}\,du,
\qquad
F_L^\#(t)=\int_0^L\Phi(u)e^{-itu}\,du,
\]

and put

\[
\Xi_L=F_L+F_L^\#.
\]

Fix \(\lambda L=1/200\).  Form the endpoint numerator and denominator

\[
N_L=(\Xi_L-i\lambda\Xi_L')
    (\Xi_L''+i\lambda\Xi_L'''),
\]

\[
D_L=(\Xi_L+i\lambda\Xi_L')
    (\Xi_L''-i\lambda\Xi_L''').
\]

## 1. Exact four-channel decomposition

Expanding by the signs of the two Fourier frequencies gives exactly four
source-owned channels:

```text
(+,+) and (-,-): same-sign Hankel channels;
(+,-) and (-,+): reflected Toeplitz channels.
```

The one-sided Paley--Wiener identities of `L-105260` realize these four terms
on one direct-sum source space.  No formal replacement of a Hermitian product
by an analytic square is used.

For one same-sign orientation, the positive denominator density and the
endpoint-Turán density are exactly those of `L-106410`.  For one reflected
orientation they are exactly those of `L-106411`.  Summing the four channels
therefore reconstructs, coefficient-for-coefficient,

\[
\boxed{
N_L-D_L
=2i\lambda
 \bigl(\Xi_L\Xi_L'''-\Xi_L'\Xi_L''\bigr).
}
\tag{L-106413.1}

The complete positive denominator bank is the direct sum of the four positive
source densities used in `L-106410--L-106411`.  Its total normalized endpoint
leakage obeys

\[
\boxed{
\mathfrak r_L
\le\frac{2547232}{1568239201}<\frac1{600}.
}
\tag{L-106413.2}

Thus item 1 of `ENDPOINTBANK106410`—the finite source-for-source two-boundary
adapter—is closed exactly.

## 2. Source dimension and feature changes

The four-channel representation is a fixed finite direct-sum feature map.  A
constant unitary recombination of the channel coordinates preserves:

```text
source dimension;
Hilbert--Schmidt energy;
all-pass determinant winding;
positive denominator Gram.
```

The channel map is fixed before the Xi zero signs are observed.  No
source-dependent selection or post hoc deletion is present.

## 3. Common factors and confluent events

At a common zero of an endpoint function and its derivative, reduce the common
local factor before forming the meromorphic companion, exactly as in
`L-105500` and `L-105550`.  The common real multiplicity transfers directly to
the parent count; a nonreal conjugate confluent block has zero signature.
The complete finite-window endpoint correction belongs to `{-1,0,1}`.

Consequently the finite adapter incurs no positive-density common-zero,
multiplicity or confluent penalty.  These events are represented in the exact
Cauchy-index ledger rather than placed in an analytic error term.

## 4. Remaining scope

The theorem does **not** prove that a cofinal source frame covers all but
\(o(N)\) of the endpoint companion model space, nor that the actual normalized
denominator Gram has \(o(d)\) one-sided deficit.  Those are now the sole
noncompact source/geometry rows.  The Fourier-tail passage from \(\Xi_L\) to
\(\Xi\) is treated separately in `L-106414`.
