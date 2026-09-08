# All-scale residual growth: the exact exponent, not its evaluation

Status: proposed complete component proofs; independent review required.
RH, native all-window positivity, and the signed failure-count saving remain open.
Parent: PR #803 at 6c86b5fbfe92c97ecccf17b81585744ccde33b10.

## What changed

The preceding pass certified four finite-support minima. This pass proves an
all-scale growth characterization of the SAME positive-residual problem.
Let Theta be the supremum of real parts of the nontrivial zeta zeros. For the
literal Mobius prefix below Y, p(1)=0 and p'(1)=1, let e_2(Y) be the minimum
with support through 2Y, and e_inf(Y) the infimum over all finite supports.
An explicit two-endpoint completion p_Y^sharp satisfies

```
lim log(1+e_inf(Y))/log Y
 = lim log(1+e_2(Y))/log Y
 = lim log(1+E(p_Y^sharp))/log Y
 = 2Theta-1.
```

These are limits over EVERY integer Y, not only selected subsequences. The
proof allows a nonattained zero supremum and the case Theta=1. Infinite
support is not used to manufacture an admissible polynomial.

The new upper side is proved with a uniform twisted Mobius-prefix estimate
on |t|<=Y^4, obtained by a zero-free-strip Littlewood/Perron argument. The
full remaining boundary norm has an unconditional O(Y^(-1/2)) tail bound.
The lower side is the complete delayed Hardy point-evaluation bound, with
the safe jet retained. Both halves are reconstructed in PROOF.md.

## What has NOT been shown

Theta has not been evaluated as 1/2. The estimate
E(p_Y^sharp)=O_epsilon(Y^(2Theta-1+epsilon)) is not an unconditional known
fixed power saving from O(Y): Theta=1 remains possible within this argument.
The constants are not numerically explicit and are not uniform as the
chosen contour approaches the unknown zero boundary.

The result shows that this simple candidate is optimal at the limiting
POWER scale, even compared with arbitrarily long finite corrections. It
does not make it a finite optimizer, bound its loss by a constant factor,
prove logarithmic asymptotics, or estimate the minimum as subpower without
RH. Numerical gains from the previous minima remain meaningful at their
finite scope. No new minimum or positive range is computed.

## Review and replay

Read PROOF.md, then REVIEW.md and SOURCES.json. Classical Nyman--Beurling,
Littlewood, Perron, and Hardy methods are credited without novelty claims.
The original closed-source and entropy programmes were consulted only as
context, not used as unexplained input theorems.

```
python -I -S -B verify.py --check result.json
python -I -S -B -O verify.py --check result.json
python -I -S -B test_rejections.py
python -I -S -B test_rejections.py --optimized
```

The sibling parent PROOF.md at the locked path is required. No parent Python
is executed. Bounded checks do not prove the infinite analytic statements.
