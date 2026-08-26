# T-106210 — Harmonic small-discrepancy and finite-depth rough frontier

Claim ID: `T-106210`  
Programme aliases: `LFAM1.HARMONIC_BOOLEAN_DICHOTOMY`, `LFAM2.SMALL_MODULUS_OR_WITT_TRACE`, `STRESS.ROUGH_HALF_SOURCE_MATRIX`  
Status: **EXACT SOURCE PARTITION; TWO SHARPENED GATES OPEN**  
Created: 2026-08-26  
Depends on: `T-106150`, `L-106210--L-106212`, parent `T-102990`  
Programme issues: #743, #736, #737  
RH status: **unproved**

Freeze

\[
U=\lfloor Y^{1/6}\rfloor
\]

on one dyadic horizon. In the live coprime two-sided Wick/ordinary half-source
current, split each interaction after common-core extraction into:

```text
SMALL:
  the least reduced-core discrepancy prime is <=U;

ROUGH:
  every prime in both reduced cores is >U.
```

The split is coefficient-exact and commutes with the fixed differential
operator \(\mathcal D_{\rm out}\).

## 1. SMALL sector

`L-106211` gives one source-exact nonzero phase with the atomically optimal
harmonic selector. Define

```text
HSMALL106210:
  after the complete source recombination and before conductorwise absolute
  values, the negative mass of the SMALL half-source current is subpower;
  equivalently, its harmonic first-discrepancy martingale/dispersion form is
  subpower with every Boolean, owner, shell and marked-prime mask retained.
```

The phase moduli in this sector are at most \(U=Y^{1/6}\), and the harmonic
selector costs no more than the deterministic least-prime allocation.
`HSMALL106210` remains open.

## 2. ROUGH sector

By `L-106210`, each reduced core has at most three primes cofinally and its
half-source coefficient lies in one two-state parity transfer. By
`L-106212`, the character-twisted half-source is a Witt tower of the
\(L(u^m,\chi^m)\) family.

Define

```text
HROUGH106210:
  the negative mass of the ROUGH half-source current is subpower after its
  prime/semiprime/triple-prime parity fibres are evaluated through the
  normal-ordered Witt L-tower, with principal and quadratic resonances kept
  explicit.
```

`HROUGH106210` remains open.

## 3. Exact implication matrix

Since the two currents sum to the live half-source current,

\[
\boxed{
\mathrm{HSMALL}_{106210}
\wedge
\mathrm{HROUGH}_{106210}
\Longrightarrow
\mathrm{WKSFSC}_{106150}
\Longrightarrow
\mathrm{BCI}_{102990}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-106210.1}
\]

The two gates require genuinely different mechanisms:

```text
HSMALL:
  signed small-modulus dispersion / least-prime martingale;

HROUGH:
  finite-depth parity trace / Witt L-family moment.
```

Neither gate is proved.
