# Arithmetic criterion slack: independently reconstructed elementary consequences

Source: PAPER-R001, Lemmas3.1–3.2 and Propositions3.1–3.2, arXiv math/0008177v2, §3 pp6–8. Status: direct corollaries/reconstructions, novelty not claimed; original Robin oscillation theorem remains an external dependency.

## Sharper asymptotic of the comparison slack

Put t=log n and r_n=H_n−log n−γ. The displayed integral in Lagarias (3.5) gives0<r_n<1/n. Thus

exp(H_n)=e^γ n(1+O(1/n)),
log H_n=log t+γ/t+O(t^−2).

Subtracting e^γ n log t and adding H_n=O(t) gives

Δ(n):=H_n+exp(H_n)log H_n−e^γ n log log n
= e^γ γ n/log n+O(n/log²n).

The terms O(log n+log log n) are absorbed since log³n/n→0. The coefficient e^γγ is about1.028, substantially below the convenient7 of Lemma3.2. This changes numerical slack, not the equivalence mechanism. Next useful task: obtain a rigorous explicit bound |Δ−e^γγ n/logn|≤C n/log²n above a specified effective n0, with an interval-certified constant for γ.

## A family of equivalent comparison criteria

Fix C≥0 and integer n0≥5041. Let R(n)=e^γ n log log n. Then RH is equivalent to

σ(n)≤R(n)+C n log log n/sqrt(log n) for every integer n≥n0.

Forward: Robin under RH gives σ≤R for these n. Reverse: if ¬RH, Proposition3.2 gives excess ≥c n log log n/(logn)^β infinitely often for some β<1/2. The ratio to the allowed C-scale tends to infinity as (logn)^(1/2−β), so the criterion fails (C=0 is immediate). More generally any nonnegative slack bounded above by this scale has the same implication. This is a direct use of Robin's oscillation strength, not a new RH approach.

Failure of an overgeneralization: replacing the exponent1/2 by a fixed α<1/2 cannot be justified by this argument, because β may satisfy α<β<1/2. That does not refute such an equivalence; it locates the missing quantitative input.

## Finite certificate

See experiments/results/lagarias_finite_summary.json and exact integer certificate. The certificate covers1..5040, thereby reconstructing the finite step in the inspected paper. It says nothing by itself about the infinite tail.
