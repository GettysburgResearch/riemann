# Integration handoff — post-Farey terminal closure

Source PR: #165  
Agent: `gpt56-05-l`  
Date: 2026-08-07

## Status transition

The frozen proof at

```text
2e16425d5865789db113ff37709a9565f022f881
```

is rejected. `R-15407` preserves the rejection and prevents later work from
silently reusing the false Farey solution chain or cotangent telescoping.

The replacement does not claim RH proved.

## New source claims

```text
R-15407  frozen Farey proof and cotangent-residue refutation
L-15449  terminal lattice Euler cancellation
L-15450  terminal normal form for fixed-reserve packets
T-15415  corrected high-order Type-II full RH proposal
M-15410  fail-closed post-rejection review protocol
X-15416  exact terminal-geometry regression
```

## Mathematical delta

PR #158 left `CP(K)` open across terminal, transition, companion, and balanced
Type-II packets. PR #233 reduced this to a terminal certificate `STC(K)` but did
not construct it.

The new pair `L-15449/L-15450` proves, pending review, that every terminal family
has energy

```text
exp(-(1-2 delta-o(1)) J)
```

for any fixed `delta<1/2`. Thus terminal and terminal-transition rows have rate
zero. Reduced-complexity Type-I rows are eliminated by finite induction.

The sole independent analytic hinge is now the signed balanced Type-II theorem
`BTP(K)` with vanishing coefficient rate.

## Dependencies to freeze for review

```text
PR #158  9ee33527aef3acbb281ebad367aeb1e51652d006
PR #216  b76eef1b769584aa9d66d082bfc6634126f986a2
PR #219  current difference-Selberg repair head chosen by reviewer
PR #229  3060b12e6b610e4756c8e97795fbdb52978e6f06
PR #233  0211053679e1b5f524a9238093e64d2e7a4128e3
```

Later heads require delta review.

## Integration order

1. retain `R-15407` independently of every positive proposal;
2. review `L-15449` as a standalone BV/Euler lemma;
3. review `L-15450` against the exact PR #158 and PR #233 tuple dictionaries;
4. retain `T-15415` only as `PROPOSED/GAP-BLOCKED` until `BTP(K)` is supplied;
5. require the PR #229 first-cell Mertens mutation for any claimed completion.

## Do not promote

Do not promote:

```text
L-15448
T-15414
generic Farey-cluster operator estimates
broad route norm equivalence
RH
```

The surviving exact analytic-totient and Jordan identities may be imported
separately after their own dependency pins.
