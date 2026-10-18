# Joint mollifier / dual moments: the complete relative error

Status: PROPOSED mathematics; independent review required. NOT PUSHED.
No RH proof or new zero-free half-plane. The complete inverse-value theorem is capped.

For the exact sextic ideal family, at s=3/4+it with t in a fixed compact set, the proposed argument establishes

    sum_(Na<=U)^flat |L_a(s)M_(U^(3/5))(s,a)-1|^2
                              << U^(11/15+epsilon).

#984's stated predecessor at its longest allowed mollifier gives U^(7/8+epsilon). The improvement is 17/120 in the exponent of the complete relative error, not an improvement to an RH zero-free boundary.

The key complete norms are M6: U, dual R2: U^(7/10), and dual R4: U^(1/2). Three-factor Holder gives U^(11/15) for M*R without combining conjugate and original characters. The main polynomial has exact Mobius cancellation through A and the same bound on its full remaining support. Both functional-equation pieces and all tails remain.

For every fixed n>=6, choose a=2(n-3)/(3n-8); the corresponding error exponent is 2(n^2-2n-2)/(n(3n-8)). There is no growing-n or growing-moment uniformity.

For each fixed k>=1, with theta=4/15 for k<=3 and theta=1/k for k>=4,

    sum_(Na<=U)^flat min(|L_a(3/4+it)|^(-2k),U^theta)
                              << U^(1+epsilon).

At a zero the summand is the cap, not zero. Every row, including the principal member when present, stays in the prefix. The first three caps are much larger than #984's displayed U^(1/80). This is ONLY an upper estimate, not that earlier Euler asymptotic; at k>=80 its cap is not larger. A single fixed zero still fits inside every proved bound.

Read PROOF.md for the full argument and its exact remaining gap. SOURCES.md records the imported analytic contracts and targeted repository scope. VALIDATION.md distinguishes exact finite checks from analytic review.

Replay (Python standard library):

    python replay.py

The intended add-only repository path is
`standalone/2026-10-18-joint-mollifier-dual-moments/`, on #984 at
`b6a29037a2be358294401d71d7305b0f402c2eea`.

No remote branch or PR was created in this turn. GitHub read actions worked; write discovery exposed no write action and direct git networking failed DNS resolution. The separate supplied patch preserves every inherited file.
