# FC26 — fixed-feedback obstruction and improved finite conditioning

**RH and the growing-horizon corrected-error estimate remain unproved.**
Status: proposed component theorems with complete proofs; independent review required.
This is a continuation of PR #812, not an independent acceptance of it.

## Results

1. The attempt to reuse one good correction as a fixed relative-feedback
   controller fails on the actual source. For every compact, finitely
   piecewise-absolutely-continuous input with finitely many jumps, integrable
   regular derivative, and initial value 1, the relative multiplier has
   unbounded long-interval critical-boundary mean square. Infinitely many
   prime frequencies survive every finite list of input jump times.
2. Accordingly, the Newton horizon-refinement sequence
   `F_m=H(1-(1-F/H)^m)` has superexponential norm cost as m grows, with infinite
   norm permitted when an iterate leaves L2. This is not a theorem about
   separately chosen controllers at different horizons.
3. For the predecessor's IDEAL degree-four correction, even the second
   iterate has a Dirac mass `-17689/100000000` at `2log2`. The actually
   compactified correction is distinct; result 1, rather than that atom,
   applies to it. The predecessor's finite error certificate is unchanged.
4. A source-specific argument gives the unconditional all-rank lower bound
   `lambda_min(G_K)>=exp(-C(1+log(K+2))^2)`. A conservative rational floor is
   `2^(-168k^2-2904k-12513)`, k=ceil(log2(K+1)). This improves the earlier
   root-exponential asymptotic envelope, not necessarily small-rank constants.
   The corresponding full source cutoff is `O(log^2(K+2))` in time, retaining
   all filtered tails. Neither result proves source cyclicity or an error rate.

Read PROOF.md, then REVIEW.md and SOURCES.md. The proof reconstructs the
conditional completion and the exact point where the tested mechanism fails.
Do NOT advertise this packet as a proposed full RH proof.

## Replay

From this directory, with the frozen predecessor's PROOF.md and
verification.json in the sibling directory specified by SOURCE_LOCK.json:

```sh
python -B check.py
python -B -O check.py
python -B check.py --rejections
python -B -O check.py --rejections
```

The checker authenticates those two predecessor files but executes no parent
Python and does not repeat its numerical certificate. It uses only the Python
standard library, integers, and Fraction. The scalar/collision/conditioning
checks are bounded algebraic controls, not machine proofs of the analytic
statements. VALIDATION.md records executions and omissions.
