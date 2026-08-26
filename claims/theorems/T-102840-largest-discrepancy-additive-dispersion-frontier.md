# T-102840 — The final pair restriction is a nonzero-phase largest-discrepancy dispersion problem

Claim ID: `T-102840`  
Status: **MAJOR UNCONDITIONAL DISPERSION REDUCTION; RH UNPROVED**  
Created: 2026-08-24  
Base: PR #719  
RH status: **unproved**

`T-102830` places the hard current in unique semiprime squareclasses
`pq a^2`. `L-102835--L-102836` now put every cross-squareclass term into an
exact nonzero additive-phase packet.

## 1. Zero phase is absent

For the largest discrepancy prime `ell`, orient the products so that

\[
ell\mid N,
\qquad
\ell\nmid M.
\]

Then

\[
1=-\sum_{h=1}^{\ell-1}e_\ell(h(N-M)).
\]

Thus the complete `ell` sector is a sum over nonzero additive frequencies. The
source-blind zero frequency and its deterministic carrier do not enter the
dispersion identity.

## 2. Fixed-squareclass phase energy

For a non-`ell` squareclass `Q` and a square-core octave of length `B`,

\[
\sum_{h=1}^{\ell-1}\|F_{h,Q}\|_2^2
\ll
{1\over Q}\left(1+{\ell\over B}\right).
\]

Hence:

```text
long core B>=ell:
  phase energy <<1/Q;

short core B<ell:
  phase energy <<ell/(B Q).
```

The estimate is obtained by exact additive orthogonality and the congruence
`b'=+-b mod ell`; it uses no unproved Möbius cancellation.

## 3. Closed versus open terms

The following are now closed before the final dispersion estimate:

```text
root and first chaos;
repeated physical-prime pair diagonal;
equal-pair owner multiplicity;
complete cofactor squaring;
semiprime-squareclass injectivity;
same-squareclass core overlap;
free quadratic-Walsh energy;
zero additive phase;
fixed-squareclass long/short phase energy.
```

The sole unresolved operation is coherent summation over **different**
non-`ell` semiprime squareclasses and discrepancy primes.

Define

```text
QDSP102840:
  after the exact carrier quotient and source/gauge recombination, the bilinear
  sum of the nonzero additive-phase packets over all largest discrepancy primes
  and all different semiprime squareclasses has subpower logarithmic negative
  mass in the fixed ratio-eight outer observation.
```

Then

\[
\boxed{
\mathrm{QDSP}_{102840}
\Longrightarrow
\mathrm{LDPC}_{102834}
\Longrightarrow
\mathrm{DPWNC}_{102749}
\Longrightarrow
\mathrm{OER}_{102780}
\Longrightarrow
\mathrm{RH}.
}
\]

## Recommended analytic split

```text
long core:
  multiplicative/additive large sieve in (ell,h), retaining the owner weights;

short core:
  direct residue sparsity and the injective p q a^2 parameterization;

shared owner:
  factor the common prime before the phase estimate;

disjoint owners:
  use the four-label squareclass parity and quadratic-character dispersion.
```

The principal/zero phase must not be reintroduced by Cauchy. No finite grid or
source-blind Fock norm proves `QDSP102840`.

```text
nonzero additive-phase identity              PROVED EXACT
fixed-squareclass phase energy                PROVED
coherent cross-squareclass dispersion         OPEN / RH-BEARING
Riemann Hypothesis                            UNPROVED
```