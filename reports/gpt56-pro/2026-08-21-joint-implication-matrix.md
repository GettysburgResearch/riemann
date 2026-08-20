# Joint implication-matrix review

## Review scope

This pass reconciles the recent quadratic-envelope, activation-coarea,
adaptive-squaring, minimal-wavelet, largest-prime, Vaughan, and phase-Hasse
branches.  It treats the no-go results as typing constraints rather than as
reasons to discard RH-equivalent nodes.

## Main conclusion

The strongest composition is not a chain but a two-input gate.  The exact
identity

\[
3G_\beta=C_2JP_2\delta_0-JP_2\mathcal A_\beta-JP_2(D-1)E_2
\]

shows that the minimal wavelet receives one continuous input from the
quadratic envelope and one atomic input from activation ownership.  The
quadratic route has the strongest small-prime/squared control; the wavelet
route has the strongest large-prime/zero-moment control.  Their unresolved
terms should therefore be estimated *against each other* before either is
sent to an absolute-value norm.

## New closure mechanism

Positive-completion absorption gives a vector inequality

\[
n\le r+e+Mn.
\]

Perron contraction, rather than rowwise closure, is sufficient.  In two
channels the exact gate is

\[
bc<(1-a)(1-d).
\]

This allows one lane to pay part of the other and vice versa.  It is strictly
more flexible than demanding either QACG100400, CATD100300, LPMW100410, or
BVD100310 in isolation.

## Numbering repair

The repository contains multiple historical `T-100200` labels.  This packet
uses the collision-free family

```text
L-101100  positive-completion absorption
L-101101  quadratic--wavelet bridge
L-101102  horizon-safe auxiliary matrices
R-101100  matrix firewalls
T-101100  joint closure matrix
```

No earlier theorem is silently renumbered.

## Remaining work

Prove two source-faithful cross estimates whose nonnegative coupling matrix
has spectral radius below one.  Candidate inputs are the `<3/4` adaptive
squaring budget and the zero-moment largest-prime/Vaughan boundary.  The
crucial audit is that both rows act on the exact bridge channels, retain
activation atoms, and use the same logarithmic measure.

RH remains unproved.
