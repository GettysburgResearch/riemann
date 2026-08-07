# M-23201 — Review protocol for the Möbius-resolvent terminal proposal

Methodology ID: `M-23201`  
Title: Review the full proposal by one finite terminal-certificate family, not by re-auditing every historical route  
Status: **PROPOSED REVIEW PROTOCOL**  
Authoring agent: `gpt56-pro-21`  
Created: 2026-08-07  
Issue: #232

## Review order

1. `L-23201` — exact finite Möbius resolvent.
2. `L-23202` — high-order geometric Mertens equivalence.
3. `L-23203` — well-founded elimination to terminal rows.
4. `L-23204` — finite positive Selberg–Hankel terminal adapter.
5. `T-23201` — composition to RH.
6. `X-23201` — exact synthetic regression.
7. proposal report and integration handoff.

## Frozen external inputs

```text
PR #158 head c5a57f33ae5c33fe16ded944ab2d3c50edc7fe07
  L-15151, L-15155, L-15156, T-15122

PR #229 head 1daf03443265ce36cfb6efbd8de1ca9c702de793
  L-23001, L-23003, T-23002

PR #216 head b76eef1b769584aa9d66d082bfc6634126f986a2
  centered Selberg/prime-energy normalization

PR #231
  R-22802 generic Farey-cluster operator refutation
```

No result from these branches is silently promoted beyond its stated status.

## Load-bearing questions

### Finite algebra

- Is `r_V` exactly zero through the declared cutoff?
- Is the finite geometric resolvent coefficient identity correct?
- Does the geometric-difference inversion retain floor conventions?
- Does every tuple have exactly one packet destination?

### Packet graph

- Does every same-scale reduced edge strictly lower complexity?
- Are all cycles impossible?
- Are all cutoff and transition sources retained?
- Is every terminal type declared?

### Terminal certificate

- Are all exponential weights nonnegative?
- Does the claimed Hankel kernel have a literal Gram representation?
- Is the Loewner domination checked on the actual source span?
- Are the centered Selberg signs and `1/2` shift correct?
- Is the real-axis linear reserve subtracted with the correct orientation?
- Does every residual route to a lower scale or a declared source term?

### Asymptotic composition

- Is `eta_K/delta_K -> 0` proved, rather than observed at finitely many orders?
- In a tensor recurrence, is the weighted scale sum strictly below one?
- Does the first-cell Mertens mutation pass?

## Automatic rejection conditions

Reject the proposal if any proof:

```text
uses a generic critical-cluster operator norm
takes total variation before signed packet recombination
removes an uncertified null companion
drops a transition or endpoint residual
replaces factor-ratio normal geometry by product dilation
leaves an undeclared terminal row
uses a same-scale cycle
infers an all-order rate from finitely many K
fails to imply the first-cell Mertens bound
```

## Status semantics

Passing `L-23201`--`L-23204` verifies the architecture and certificate adapter.
It does not verify `STC(K)`.

Only a source-bound unbounded family satisfying the rate theorem completes the
proposal. Until then:

```text
FULL PROPOSAL
ONE ARITHMETIC HINGE OPEN
RH UNPROVED
```
