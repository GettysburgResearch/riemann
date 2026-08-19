# Discounted literal-score debt on the actual factor-67 branching tree

## Research question

PR #620 proposes a complete score-free Hall/direct-integral proof candidate.
Its most fragile recursive interface is the claim that literal-score debt does
not accumulate over the full branching rough-prime tree. The published prose
uses a distinguished sequence `X/(d67^j)`, although the actual source children
use varying primes and branch.

## New idea

Treat score shortfall as a Bellman debt normalized by **actual target mass**.
At every typed node, exact physical-row and target identities split the packet
into current-owned mass plus normalized alpha-child mass. Charge the current
mass the full terminal unit debt, even though nonterminal current packets have
no shortfall. Descendant debt is carried only by the alpha-children.

If `m_v` is parent target mass and `a_(vw)` are normalized child coefficients,
then

\[
D_v\le D_0\left(m_v-\sum_wa_{vw}m_w\right)+\sum_wa_{vw}D_w.
\]

The envelope `D_0 m_v` is therefore invariant exactly. Backward induction on
the finite scale DAG yields `D_v<=D_0m_v` independently of branch count and
depth.

## Fixed source ledger

With

\[
D_0=2(4\sqrt{67}-3),
\qquad
W_{61}=\prod_{p\le61}(1+p^{-1/2}),
\]

the replay gives the directed upper bound

```text
W61 < 59.423461968782085
D0 W61 < 3534.675221310727920 < 3600.
```

## Firewall

The survival and lambda-current coefficients are not recursive. Counting them
as children gives total coefficient

\[
1+\sum_i\alpha_i>1,
\]

which destroys every contraction argument. Only alpha-children cross to later
states.

## Status

This closes the all-depth score-debt composition of PR #620 if its local typed
identities and terminal unit-debt theorem survive review. It deliberately does
not promote the full candidate: compact Hall, endpoint-frame normalization,
all-column feasibility and the endpoint Mellin–Landau consumer remain separate
review obligations. RH remains unproved.
