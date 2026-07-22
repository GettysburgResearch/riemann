# X-2501 certificate schema

Schema: `riemann.robin.canonical-tree.v1`.

The certificate stores one deterministic depth-first token stream for each support size. Tokens are `P` for a rigorously pruned prefix, `S` for a rigorously satisfied leaf, `B` for a leaf at or below 5040, `U` for an unresolved leaf, and `V` for a rigorously violating leaf.

The verifier regenerates the prime list, primorial support limit, child ranges, exact integers, exact divisor-sum ratios, finite-budget exponent caps, dyadic right-hand-side intervals, and every classification. Missing, extra, duplicated, or reordered tokens are rejected.

For each strict leaf or prune, the verifier also reconstructs an exact rational upper bound for the normalized Robin quotient and checks the stored global maximum. Search and replay use separate traversal implementations but share `certmath.py`; this is an independent traversal replay, not a second numerical backend.

The production manifest binds the full certificate digest, terminal-stream digest, exact finite region, counts, quantitative bounds, and source snapshots. A hash is an integrity check only; mathematical acceptance comes from replay.
