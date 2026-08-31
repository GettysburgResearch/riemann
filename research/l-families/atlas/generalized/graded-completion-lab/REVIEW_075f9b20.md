# Independent review of the arithmetic after-source radius dichotomy

Reviewed freeze: `075f9b203aefefb4a29f3279b6de1c4127093af6`.
Reviewer: `/root/recent_landscape`, separate from the proof and producer authors.
Conclusion: **no mathematical or acceptance blocker found within the declared scope**.

## Exact identity and what was reviewed

I independently read the full radius proof, complete arithmetic producer and
all 28 tests before freeze, then verified that the reviewed scientific paths
were unchanged at this exact commit. I inspected the artifact's schema,
counts, source/binding metadata and stated analytic scope; I did not re-enumerate
the 3044 rows or rerun any computation. Exact Git blobs are:

| file | blob |
|---|---|
| `ARITHMETIC_RADIUS_DICHOTOMY.md` | `cf8d794a35c2dc88eb86c1a6f62f6a06cbe3d03f` |
| `arithmetic_radius_replay.py` | `f33245de6552337df00f65b0bf78621fa6d6d028` |
| `arithmetic_radius.verification.json` | `88360519800f8ba2f8f4de6d8e62b0a0190ea9e3` |
| `tests/test_graded_completion_arithmetic_radius.py` | `c420b1daf8a768d4905c57f1b3febc17083b06e7` |

The artifact uses schema `actual-after-arithmetic-radius-v1`, records 3044
parameter rows, and records radius counts 1798 at `1/2` and 1246 at
`1/sqrt(2)`. These are a finite parameter atlas, not isomorphism-class counts
or the proof of the general theorem.

## Load-bearing analytic and arithmetic checks

The actual source identity `tZ=aD+2aE` and the rational-fibre count imply
`tZ` is divisible by six. The proof uses the actual even Koszul multiplicities
and the transposition/cycle characters, not fitted dimensions. Their restricted
divisor remainders justify the three-log expansion and its continuation beyond
the second critical circle. The secondary transposition term is retained.

The first-point exponent is the sum of the analytic multiplier exponent
`alpha=tZ/12` and the **actual finite-source zero order** at the opposite signed
split fibre. Therefore an integer test on `alpha` alone would be incorrect.
Both signed orders must be nonnegative integers for the first circle to be
removable. The second-circle real and imaginary exponent analysis, including
the quarter lattice and elliptic-trace parity restriction, ensures that the
larger radius is exactly `1/sqrt(2)`, not just a lower bound.

The finite-factor subtraction/cancellation argument precedes the claimed
holomorphy disk. The proof does not count denominator zeros of an isolated
multiplier as new poles of the full source. The mathematical statement is an
all-field source theorem; the bounded atlas checks its arithmetic inputs and
counterfeits without replacing the remainder proof.

## Implementation and acceptance

The producer reconstructs the discovery rows from literal quadratic pairs and
cubic preimage fibres; it does not accept the discovery JSON as authoritative
arithmetic. Selected proper closure counts provide an additional source check.
The PBW/divisor remainder controls, finite product versus Newton checks, and
finite-source order falsifiers are substantively different checks.
Authentication precedes executable imports. The strict JSON-tree and canonical
serialization comparison rejects numeric type counterfeits and nonfinite values.

Root reports Ruff, ordinary write/check, optimized check, and **28 ordinary
plus 28 optimized tests passed**. I did not execute them. The frozen replay
contract still contains prospective execution wording; this report supplies
the later coordinator-reported status without changing bound scientific files.

This packet proves the after-source classification. It does not independently
compute the before-extension classification, enlarge the ordinary trace-class
domain, or establish a number-field/archimedean bridge. The smallest scientific
invalidator would be a wrong finite-source zero order or omitted secondary
character term; atlas agreement alone would not cure that defect.
