# T-99100 — Discounted score-debt supermartingale closes the all-depth interface of the direct-integral candidate

Claim ID: `T-99100`  
Status: **UNCONDITIONAL COMPOSITION THEOREM ON THE STATED TYPED INPUTS; RH UNPROVEN**  
Created: 2026-08-19  
Frozen base: PR #620 at `493e12fcba3f9b98dda7c3595bff73b256e00ca4`  
Depends on: `L-99100`, `R-99100`  
RH status: **unproved**

Assume the local inputs of PR #620 at their literal scopes:

```text
compact Hall output is split into residual-source and current-only row sorts;
residual causal splitting is an exact physical-row identity;
only normalized alpha-children recurse;
actual target mass is conserved between current and children;
recursive child target mass is < parent/8;
nonterminal current score has no shortfall;
terminal score shortfall is <= 2(4sqrt(67)-3) per unit target mass.
```

Then the complete branching factor-67 tree has total literal-score debt

\[
\boxed{
D_{\rm tree}
\le2(4\sqrt{67}-3)
\prod_{p\le61}(1+p^{-1/2})
<3600.
}
\tag{T-99100.1}
\]

The estimate is independent of branch count, varying rough primes and depth.
It replaces the distinguished-chain argument in `L-99024` and proves the
backup per-packet envelope at its exact typed scope.

If the equality-frame score, single root thinning and root-owned omission
bounds in `L-99022/L-99023` are independently verified, then the same
composition yields

\[
\mathcal H(d_X)
\ge4\sqrt X-
\left(3600+96\sqrt{67}+C_{\rm top}\right).
\tag{T-99100.2}
\]

This is precisely the score input required by the endpoint consumer of PR
#620. The theorem does not verify those other inputs and therefore does not by
itself prove the endpoint theorem or RH.

```text
all-depth branching score debt       CLOSED ON TYPED LOCAL INPUTS
fixed 67^j source-path assumption     REMOVED
geometric generation debt             REMOVED
compact Hall / endpoint measure       OPEN TO INDEPENDENT REVIEW
all-column / endpoint consumer        OPEN TO INDEPENDENT REVIEW
Riemann Hypothesis                    UNPROVEN
```
