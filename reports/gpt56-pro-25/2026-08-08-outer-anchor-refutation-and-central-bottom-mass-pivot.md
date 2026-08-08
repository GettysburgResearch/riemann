# Outer-anchor refutation and central bottom-mass pivot — 2026-08-08

Status: `MAJOR SCOPE CORRECTION / NEW EXACT SCALAR CONSTRUCTION / RH UNPROVED`  
Issue: #245  
PR: #248

## Executive result

The newest terminal adjacent-commutator completion was reconstructed against the
complete positive stopped-power resolution of the critical target.  Its exact
commutator algebra survives, but its proposed source norm does not.

For every stopped endpoint `Y` and every `q` with

```text
Y/3 < q <= (Y+1)/2,
```

the `k=1` even term is inside and the odd term at `3q` is outside.  Summing the
positive endpoint weights over `2q-1<=Y<=3q-1` leaves a coefficient at `3q` of
size at least

```text
log(3/2)/sqrt(3q).
```

The square-root atomic commutator norm therefore pays an absolute constant for
every `q<=X/3` and is `Omega(X)`.  The claimed polylogarithmic terminal debt
cannot be obtained by a termwise triangle inequality.

This correction is `R-24530`.

## What did not fail

The exact adjacent-tree identity

```text
E_(m-1)=T_m-T_(m-1),
load_q(E_(m-1))=1_(q|m)
```

is correct and valuable.  The failure is the ambient norm in which the complete
boundary source was inserted.

`L-24534` gives the correct global potential for the common tail:

```text
sum_m sigma_m E_(m-1)
 =sigma_N T_N+sum_(m<N)(sigma_m-sigma_(m+1))T_m.
```

Every decreasing nonnegative, hence every positive Hausdorff, source is already
a nonnegative combination of complete central trees and has zero debt.  Only
the signed first-difference parity/cutoff boundary remains.

Thus the terminal programme should not be described as wholly false.  Its
common Hausdorff tail is actually easier than proposed; its unmatched outer
anchor is harder.

## New exact source collapse

The central cascade admits two successive sparse reductions.

### Reciprocal eta

The coefficients of

```text
1/[(1-2^(1-s)) zeta(s)]
```

have a dyadic staircase divisor prefix.  Pairing them with one central carry row
gives `1` on every parent except `2P-1`, where the value is `1-P`.

Hence any exact central cascade is measured by only:

```text
bottom values at q=2;
one adjacent Mersenne jump per binary scale.
```

This is `L-24531`.

The raw eta scalar is not a valid RH consumer because `1-2^(1-s)` has artificial
zeros on `Re(s)=1`.

### Exact dyadic filter to Möbius

The coefficient identity

```text
mu=b-2 delta_2*b
```

removes those artificial zeros.  More strongly, Möbius pairing of every central
carry row is exactly `-1`:

```text
sum_q mu(q) chi_n^c(q)=-1.
```

Therefore, if `f_j` are the residual stages of the terminating central Neumann
cascade,

```text
R_mu(X)
 =sum_(n<=X)mu(n)n^(-1/2)log(X/n)
 =log X-sum_j f_j(2).
```

This is `L-24533`.

The entire RH-bearing source has therefore collapsed to one explicit scalar
bottom-mass ledger.  No positivity of the full coefficient vector and no
ambient Green norm is required.

## Sparse boundary estimates

`L-24532` proves that every power-log analytic channel and every fixed finite
Peano/Euler jet bank has polylogarithmic norm under the bottom-plus-Mersenne
functional.  The complete positive stopped-endpoint layer cake remains
polylogarithmic in this sparse norm, including its endpoint jumps.

This explains why the boundary can be simultaneously

```text
macroscopic in ambient square-root atomic norm,
polylogarithmic on every fixed analytic/jet channel,
and still RH-bearing after all generations are composed.
```

The unresolved issue is all-generation stability after the mandatory dyadic
recombination.

## Corrected full attack

The preferred construction is now:

```text
critical logarithmic target
-> exact nilpotent central Neumann cascade
-> common Hausdorff source tails
   -> positive central-tree layer cake, zero debt
-> finite power-log / Peano jets
   -> sparse Mersenne seminorm, polylog per bank
-> exact eta Mersenne pairing
-> dyadic filter mu=b-2 delta_2*b before absolute values
-> Mobius central-row collapse
-> one bottom-mass recurrence
-> subpower Mobius Riesz mean
-> Mellin/Landau
-> RH.
```

A valid final recurrence would have the form

```text
D(X)
 <= C log^A(2X)
    +sum_beta theta_beta D(Y_beta),
Y_beta<=X/2,
sum theta_beta<1,
```

for the complete signed bottom scalar

```text
D(X)=log X-sum_j f_(X,j)(2).
```

The recurrence must be emitted after complete eta/dyadic source recombination.
It may not use the refuted ambient terminal norm.

## Why this is narrower than WSTS but not weaker in arithmetic content

PR #276 identifies WSTS as the canonical weighted dyadic shell theorem and
proves `WSTS <=> RH`.  The bottom-mass coordinate above is another exact scalar
projection of the same Möbius source.  Its advantage is proof production:

```text
all stages are explicit;
termination is finite;
the final consumer is one coordinate;
the common monotone boundary is already positive;
every analytic jet has a proved sparse bound.
```

Its disadvantage is honest: a strict all-generation bottom recurrence is not
yet proved.  Producing another finite carry packing or another equivalence does
not address that recurrence.

## Immediate review order

1. `R-24530` outer-anchor family and atomic lower bound.
2. `L-24534` source integration by parts.
3. `L-24531` reciprocal-eta/Mersenne identity and artificial-pole firewall.
4. `L-24533` Möbius constant-row and bottom-mass identity.
5. `L-24532` sparse power-log jet estimates.
6. The next production bottom recurrence.
7. Existing Möbius-Riesz/Landau normalization.

## Exact boundary

```text
terminal commutator algebra                 retained exact
polylog ambient atomic boundary norm        refuted
monotone/Hausdorff common tail debt          zero, proved exact
eta/Mersenne central source collapse         proved exact
Mobius central bottom-mass collapse          proved exact
fixed finite sparse jet bounds               proved elementary
all-generation strict bottom recurrence      open / RH-bearing
Riemann Hypothesis                           unproved
```
