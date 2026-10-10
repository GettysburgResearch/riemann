# Validation and scope

## Executed

The standard-library checker was executed in this session in ordinary Python and in optimized Python, with isolated mode, site imports disabled, and bytecode output disabled:

    python -I -S -B checks/check_all_order.py --output results/exact_checks.json
    python -O -I -S -B checks/check_all_order.py --check results/exact_checks.json

Both returned exit status 0. Their complete JSON stdout was byte-for-byte identical under `cmp`.

Each mode executed **50,357 successful exact predicates** and rejected **four deliberate algebraic mutations**. The replay includes 24,309 multi-index comparisons against an independent numerator/geometric-series expansion, positivity checks, 791 forward/inverse formal convolutions, local coefficient coverage through order k=8 and total degree 8, the squarefree-support derangement boundary through k=16, scalar pair-pole removal, and exact extraction fractions.

It also executed **42 forward and 42 inverse finite row reconstructions**, with 21 cases containing zero phases, plus **42 moving-exclusion identities**. The finite arithmetic uses a free monoid on two prime ideals of norms 7 and 13 and exact Q(zeta_6) arithmetic. Phase assignments are structural fixtures, not a sample of the genuine full Hecke/sextic row family. Its rational compact weights are finite algebra fixtures, not the smooth tests of the analytic theorem. The fixture primes need not satisfy the large-prime cutoff, since formal identities do not require it; the analytic norm theorem does.

The four deliberately rejected mistakes were: removing the positive pair coefficient; replacing support size by total degree in the inverse kernel; treating a zero character value as one after a sixth power; and taking the wrong root in the defect-aware exponent.

An additional external tampering test changed the retained successful-predicate count. The optimized full reconstruction rejected that modified JSON with exit status 1 and the message `Retained JSON differs from full reconstruction`. The original result was unchanged.

## What is not established by these tests

Finite exact checks do not prove the all-order theorem, the infinite Euler-product estimates, or the asymptotic kernel mass. Those rely on the written proofs. There has been no independent mathematical reviewer, Lean build, upstream formalization rebuild, whole-repository validation, or scientific acceptance in this session.

No genuine new arithmetic fourth or sixth moment was established. No new numerical zero-free boundary or RH proof was established. The positive phase countermodel is explicitly synthetic, not a refutation of the actual sextic moment conjecture.

## Load-bearing statements requiring review

1. PROOF.md Theorem 3.1: the source-faithful multivariate convolution, including zero masks and scale shifts.
2. PROOF.md Theorem 4.1: the absolute convergence of the pair-pole-removed series and the sharp logarithmic asymptotic.
3. PROOF.md Theorem 5.2: the full-row, all-shorter-scale envelope quantifiers in the reversible transfer.
4. MOMENT_FRONTIER.md Theorem 1.1: exact prime extraction with a defect and every fixed h>0.

The smallest remaining analytic gap is NOT one of the executable identities. It is the fixed-mask rectangular collision-free row mean square stated in MOMENT_FRONTIER.md (5.1).

## Publication scope

This session could read the pinned repository through the GitHub connector. The available GitHub tool catalog had no write action. The terminal attempt to fetch the frozen parent failed with `Could not resolve host: github.com`. No remote push, commit, or pull request was created. The enclosing delivery contains an add-only patch and a publication helper; neither is a remote receipt.
