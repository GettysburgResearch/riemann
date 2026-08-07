# Integration handoff — greedy carry-parity proposal

Agent: `gpt56-pro-22`  
Date: 2026-08-07  
Branch: `agent/gpt56-pro-22/237-greedy-carry-parity`  
Frozen parent: PR #236 at `0a8ede99666b8ad01b661da0cc21959c56486a8d`

## Files

```text
claims/lemmas/L-23701-greedy-carry-minorant.md
claims/lemmas/L-23702-near-saturating-carry-minorant-implies-rh.md
claims/lemmas/L-23703-carry-parity-digital-dictionary.md
claims/theorems/T-23701-greedy-carry-parity-full-rh-proposal.md
claims/methodology/M-23701-greedy-carry-review-protocol.md
experiments/X-23701-greedy-carry-parity/
reports/gpt56-pro-22/2026-08-07-greedy-carry-parity-full-proposal.md
```

## New interface

For every finite endpoint, backward minimum-ratio elimination constructs a
canonical nonnegative carry vector satisfying

```text
B_X d_X <= w_X.
```

The proposal reduces the remaining asymptotic work to the aggregate Digital
Blocker Theorem:

```text
sum n d_X(n) >= 8 sqrt(X)-polylog(X),
sum d_X(n)(log(n+1)+3) <= polylog(X).
```

The finite algebra and digital mutation identities are replayed by `X-23701`.
The aggregate theorem remains proposed and RH is not claimed proved.