# Parity-domain-wall attack on CPPD — 2026-08-12

## Verdict

This is the strongest **direct all-packet** route after PR #411.

The full completed Green ledger admits an exact Hadamard rotation.  Every
prime, long-jump, reflected, delayed, and bridge endpoint pair collapses to one
even and one odd port.  The singular short compensation pair `(C,J)` collapses
in the same way.  The source identity becomes

\[
 \mathbb K_a^{\rm del}
 =\mathcal C_a^\lambda
  +\mathcal P_a^{\rm par}
  -\mathcal N_a^{\rm par}.
\]

At the plastic-aligned scale the continuous source is a literal parity domain
wall: odd production is favourable on the short side and even endpoint energy
is favourable on the long side.

## Exact advance

- `L-91414`: full-packet Hadamard reduction;
- `L-91415`: parity ports are the graph of the Cayley transform of the
  translation semigroup;
- `R-91406`: no channelwise parity domination can work;
- `T-91403`: one joint connection-aware parity contraction implies CPPD and
  RH.

## Why it is promising

The original CPPD ledger compared many ports whose dependencies were hidden.
The parity basis is canonical and minimal.  It also identifies the exact
operator that the completed connection must regularize:

\[
 A_T=(I-T)(I+T)^{-1}.
\]

The low-frequency and anti-phase singularities explain both the bridge and the
need for the completed finite-jet connection.

## Immediate next calculation

1. rewrite the gamma-ladder/pole connection of `L-91411` in the parity basis;
2. compute the Redheffer/Schur complement of the `(C+J)` short even port;
3. retain the prime even port and the six-safe-jet connection in one block;
4. solve the resulting operator Riccati equation on the exact source range;
5. test against the phase resonances of `R-91406` and the Fejer packets of
   `R-91405`.

## Boundary

```text
parity source identity                 EXACT
Cayley graph                           EXACT
channelwise parity shortcut            REFUTED
joint parity-domain-wall contraction   OPEN / RH-EQUIVALENT
RH                                     UNPROVED
```