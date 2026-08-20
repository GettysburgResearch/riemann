# Hostile proof attempt on DCE100100 and QPET100101

## Executive verdict

The requested attempt did not prove RH.

It produced one binding refutation and one binding identification:

```text
QPET100101 is false as stated;
DCE100100 is exactly predecessor-state positivity at every edge.
```

## QPET consistency failure

For every fixed completion order `k`, the already-proved corridor says that for
each `A<A_k^*`,

\[
N_{Z,k}>Z^A
\]

for every sufficiently large `Z`. Taking `A` upward to `A_k^*` proves

\[
\liminf_{Z\to\infty}\frac{\log N_{Z,k}}{\log Z}\ge A_k^*.
\]

QPET was defined by the strict opposite inequality. It is therefore not an
open theorem waiting for a sharper Perron estimate; it is incompatible with
the theorem immediately before it.

The residue-amplification mechanism was also stress-tested. Inside the positive
corridor, the complete finite scalar has a uniform Euler-level bound, while an
individual selected residue may be superpolynomial on an amplified cutoff
subsequence. Any correct explicit formula must therefore contain an equally
large compensating spectral/contour term. One-pole dominance inside the
corridor is impossible.

## DCE algebraic collapse

The exact future-prime recurrence is

\[
C_p(Y)=C_{p^+}(Y)-p^{-1/2}C_{p^+}(Y/p).
\]

Consequently

\[
C_{p^+}(Y/p)\le\sqrt p\,C_{p^+}(Y)
\iff C_p(Y)\ge0.
\]

DCE does not sit before the state sign; it is that sign. The terminal corridor
proves the terminal state, but the proposed low-prime maximum principle merely
relabels each unproved predecessor.

A separate Mellin audit shows why the distinction matters. Removing finitely
many Euler labels multiplies the duplicate-67 source by a finite factor which
is zero-free in `Re z>0`. Every fixed tail therefore retains all hypothetical
off-line reciprocal-zeta poles. Eventual nonnegativity of any one fixed tail is
already conclusion-bearing through the frozen centered-cubic Landau consumer.

## Corrected route graph

```text
future-prime terminal corridor             proved
DCE edge = predecessor positivity          proved
DCE100100                                  open / conclusion-bearing

finite-completion corridor                 proved
finite multiplier zero-free                proved
residue amplification                      proved
QPET100101                                 refuted
inside-corridor one-pole dominance         refuted

Riemann Hypothesis                         unproved
```

The finite-completion packet remains valuable as an unconditional corridor and
spectral cancellation diagnostic, but it is not a second closure route through
QPET. The honest remaining arithmetic content is direct critical-source
cancellation: an actual-prime activation theorem, a cross-core estimate, or a
noncircular averaged negative-mass theorem.

## Replay

```text
PASS_T100103_DCE_QPET_HOSTILE_DISPOSITION
3c618fef8ef4f3012dfdb636be22dbe9c37736a0b5765e44b4f21a1a15070e86
```

The replay records

```text
dce100100_proved   = false
qpet100101_refuted = true
rh_established     = false
```
