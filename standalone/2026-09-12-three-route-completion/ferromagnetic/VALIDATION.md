# Validation and source boundary

Date: 2026-09-12. Platform: Windows, Python3.12. The exact arithmetic uses only
the Python standard library. It proves finite rational interval assertions;
it is not a formal proof of the paper's general statements.

## New arithmetic

`certify_graft.py` uses closed dyadic intervals with denominator2^256.
Conversion from rational numbers, multiplication, division and integer square
roots round outwards. Sums retain both endpoints. Every intermediate division
requires exclusion of zero. Floating conversions occur only in printed
human-readable endpoints, after every strict acceptance comparison.

The input root box is fixed by the SHA256 of its canonical mathematical fields:

    bf6895caf995e334bfe7b039a74a6f87ecc9961f7861f0c28edda7cd16f66d4f

Those fields were compared exactly with PR #863's parameters.json at commit
`0640c9c59be0bf20c18258460a7517fb09728e82`, Git blob
`e338c68ec803acd7991d52a83f7d5b5b97896ee3`. The root's full-theta existence and
degree14 matching are named predecessor premises; no new native-source replay
is claimed. No displayed theta moment or predecessor result receipt is read
by the new accepting program.

Every run reconstructs the unit-sign and dimer cumulants, the component
polynomial, its nonzero functional denominator, all annihilator coefficients,
all six edge-score polynomials and all compensated slope intervals. These are
evaluated on the WHOLE seven-dimensional predecessor box. The result is
compared with the complete stored JSON, and simple rational strict brackets
are checked. Acceptance uses exceptions, not assert statements.

The normal and optimized accepting modes both pass and reconstruct the same
artifact. These are two execution modes of one implementation, not independent
backends or independent review.

## Independent bounded controls

`test_graft.py` runs three groups of tests:

1. Three rational dimer/sign parameter panels. Complete eight-configuration
   sums verify the merger identity at three coupling ratios, all moments
   through16, and eight derivative coefficients. A directly differentiated
   moment-to-cumulant recursion checks the formal sinh/tanh quotient.
2. Six orders of the general annihilator, with distinct rational weights and
   positive multiplicities. Full exact Gaussian elimination and all Jacobian
   columns are compared with the polynomial formula.
3. Rational signed-arithmetic and square-root enclosures; full actual-box
   reconstruction; rejection of a changed predecessor coupling ratio and a
   changed claimed derivative sign.

These finite tests exercise different algebraic representations. They do not
replace the general proof, establish all-order graph realization, or replay
the predecessor's theta integration. Both normal and optimized test commands
pass. No remote CI, Lean proof or full repository build is claimed.

## Exploratory calculations

The mpmath scouts are outside the certificate. They read exact-SHA predecessor
data through `git show` and use midpoint moment targets. The bounded owner0
continuation reaches tau0.99 with the excess still positive, about0.200593;
the owner2 trace reaches0.1 and turns upward after its small initial decrease.
An earlier slower owner2 attempt at0.2 was interrupted and is not counted as
a completed path. The retained bounded replay finishes normally and records
its actual values in `continuation-scout.json`.

After #867 appeared, `star_scout.py --solve` failed to find an eight-equation
root with any of four individually released controls. The fixed-bias-rule
all-ten-weight minimum-norm run completed60 steps, with a nonzero residual
and no certified root. `star-minnorm-scout.json` retains its trace. Nothing
in these failures is an infeasibility theorem, and no optimizer output is
used to prove the strict signs of the accepting calculation.
