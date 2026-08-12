# Eta-paired dyadic sector-change attack — 2026-08-12

## Verdict

This is the most radical constructive route.

The global Jordan zero that cancels Suzuki's unstable free gamma pole can be
reorganized exactly as

```text
absolutely convergent odd/even paired eta channel
x one explicit dyadic zero
x one explicit free gamma pole.
```

At the pole node, the zero coefficient is exactly `zeta(1-2 omega)`, matching
the coefficient in the existing pole-bridge theorem.

## Exact advance

- `L-91430`: eta/dyadic factorization and exact pole coefficient;
- `L-91431`: positive paired eta Hilbert vectors and an explicit Householder
  safe-to-hard one-vector sector change;
- `R-91408`: the same Householder cannot intertwine the full carrier family;
- `T-91405`: a one-node eta/dyadic/gamma optical bridge for a sequence
  `omega_j -> 0` would prove RH.

## Why it is promising

The safe positive Euler Fock sector becomes disjoint at the critical boundary.
The eta representation changes the order of operations before Hilbert
completion:

1. pair odd and even integers, making the hard-strip series absolutely
   convergent;
2. isolate the pole-canceling zero in one dyadic factor;
3. perform a positive one-vector sector change;
4. combine with the explicit free gamma pole before taking norms.

This directly attacks the global pole-zero cancellation that finite Euler
products miss.

## Immediate next calculation

1. Mellin-convolve the paired eta vector with the pole-subtracted free Suzuki
   Green vector;
2. insert the dyadic zero as a two-port Julia node;
3. compute the exact critical and stable one-node model outputs;
4. show the Householder-transformed source norm equals those two outputs;
5. retain the carrier-Gram mismatch of `R-91408` as a strict scope boundary.

## Boundary

```text
eta/dyadic pole bridge                   EXACT
positive one-vector sector change        EXACT
full carrier unitary                      REFUTED
completed one-node eta/gamma optical map  OPEN / RH-BEARING
RH                                        UNPROVED
```