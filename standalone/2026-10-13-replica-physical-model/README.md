# Principal replicas: a quantitative physical/model comparison and the coherent mode

**Status: proposed research, not independently reviewed; no new zero-free exponent.**

This is an additive continuation of PR #932, base
`c63b5aaa5d53dd183abb20299cea4628f0ab57b7`. It also compares the probability
model with the invariant-free construction in PR #931. These source files were
read live from GitHub. No historical proof or integrated status is changed.

## What this pass establishes in written proofs

1. **A uniform r-linear comparison for the actual principal replicas.** The
   empirical measure on rough Eisenstein-ideal bases of norm about Y is compared
   with independent prime-divisibility indicators of means 1/Np. The error is
   O(Y^(-1/2)) above the critical exponent and O(Y^(-1/2) log(D)^r) at the
   critical exponent, times the explicitly retained finite source norms.

2. **Growing-order control.** With Y=D^rho and roughness P=(log D)^2, the
   normalized comparison error is D^(-eta+o(1)) uniformly for total order
   r <= (rho/2-eta) log D/log log D. This is not merely a collection of fixed-k
   bounds with unspecified k-dependent constants. It compares models relative
   to an UNKNOWN past critical source envelope; it does not bound that envelope.

3. **An exact coherent-mode/innovation decomposition.** Apply the explicit
   causal inverse of #932's mean operator. The resulting independent model has
   mean exactly F(D), the ordinary Möbius source. Its second moment is exactly
   |F(D)|^2 plus a positive, summable prime-innovation energy. The local operators
   and every split-prime multiplicity are explicit.

4. **A precise limitation of a tempting combination.** #931's invariant-free
   random-phase moment theorem cannot be transported to this divisibility model
   by treating the mean as zero. For the normalized replica model, even one
   fixed all-scale moment bound at an exponent is equivalent to the corresponding
   bound for F. The comparison theorem controls one error term; it does not
   remove the arithmetic content of the target.

The ordinary-zeta source is

    F(D)=sum_n mu(n) W(n/D).

After a fixed rescaling to make it vanish below 1, define

    M(D)=sup_{1<=x<=D}|F(x)|/sqrt(x).

The growing-order result for r=2k is

    |E_physical |B_w(D)|^(2k) - E_divisibility |B_X(D)|^(2k)|
        <= D^(-eta+o(1)) M(D)^(2k) D^k.

**M(D) is not proved to be bounded or subpower.** Replacing it by a constant
would be an invalid strengthening and would conceal the very RH-level term
identified by the second manuscript.

## Why this is relevant to the current attack

The previous packet's signed-quantile criterion and the adjacent independent-
prime hierarchy suggested combining a narrow ordinary-zeta detector with a
probabilistic moment bound. This pass follows that idea far enough to separate
two questions that must not be conflated:

- How accurately does an independent divisibility model represent the physical
  principal replicas? The comparison above answers this quantitatively.
- Is the random model itself small? Its exact coherent component is the original
  F, so this question still requires genuine Möbius cancellation.

The original full-family physical/phase-model discrepancy in #931 is a different
object and remains unproved. Nor do these results handle the original long
coprime signed singleton covariance of the sextic moment expansion.

## Reading order

- [PHYSICAL_MODEL_COMPARISON.md](PHYSICAL_MODEL_COMPARISON.md): definitions,
  uniform ideal counting, all fixed orders, critical endpoint, explicit growing
  roughness and growing-order estimates.
- [COHERENT_MODE_AND_PRIME_INNOVATIONS.md](COHERENT_MODE_AND_PRIME_INNOVATIONS.md):
  exact local normalization, orthogonal energy identity, physical error,
  equivalence of model bounds and source bounds, and moving-roughness coherence.
- [VALIDATION.md](VALIDATION.md): checks performed, self-audit, scope and limits.
- [SOURCE_LOCK.json](SOURCE_LOCK.json): exact remotely read source identities.

## Reproduction

From this directory:

```sh
python checks/check_replica_model.py --output /tmp/replica-check.json
python -O checks/check_replica_model.py --output /tmp/replica-check-O.json
cmp /tmp/replica-check.json results/exact_checks.json
cmp /tmp/replica-check.json /tmp/replica-check-O.json
python checks/verify_manifest.py
```

The diagnostic is standard-library Python and uses exact rational arithmetic.
It tests finite identities, not limiting estimates, zeta zero locations or the
existence of an asymptotic signed-quantile bound.

## Publication and mathematical boundaries

The active GitHub connector exposed reads but no commit/branch/PR mutation tool.
Plugin discovery found the installed GitHub connector but no additional usable
write capability. A direct local GitHub request failed at DNS resolution; no
GitHub push or PR was created in this pass. This packet and the additive patch
are local deliverables. Their hashes attest only to file integrity.

The proposed target branch is
`research/replica-physical-model-20261013`, based on #932. This branch name is a
suggestion for applying the patch, NOT a remotely created branch.

No claim of independent AI review, human review, Lean verification or new
zero-free region is made. The generalized native moment and the signed
principal-witness arithmetic estimates remain open.
