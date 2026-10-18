# Exploration record for the degree-18 continuation

Status: exploratory history. Only the separate directed certificate and
its proof establish the finite theorem.

The preceding PR #974 tree matched theta through degree 16. Its next raw
moment discrepancy was about +0.03483367, and a separately proved local
compensated-edge derivative was negative. Neither result gave a path to
the degree-18 target.

## Attempts made in this pass

1. **Replace the largest old sign by an unequal dimer.** The conditional
   law was computed exactly with alignment probability p and two unequal
   positive observable weights. Several compensated directions reduced
   the next discrepancy. Fixed lower-eight continuations with different
   weight ratios stalled with positive discrepancy, approximately 0.012
   to 0.019 for the most useful profiles. These failures are solver and
   continuation diagnostics, not separating inequalities.
2. **Join the entire large-component sector into a flexible chain.** The
   model had 14 unequal core weights, thirteen independently variable
   ferromagnetic correlations, and the two repeated small-leaf groups.
   Direct least squares with a fixed whitening of all nine constraints
   produced poor residuals. An independent 75-digit raw-moment recurrence
   checked the long-double analytic Jacobian; its largest absolute
   discrepancy was approximately 2.55·10^-18. The failure was not treated
   as evidence that the moment target was impossible.
3. **Prioritize the lower-eight moment fiber.** A constrained SLSQP scout
   enforced the lower-eight equations separately and minimized a
   compensated ninth functional. One ordering reached a negative next
   raw-moment discrepancy, approximately −6.9427·10^-5, with lower-eight
   coordinate residual below 3·10^-13. That number was a floating scout,
   not an accepted moment equality or existence proof.
4. **Refine and certify the actual nine-equation root.** Independent
   95-digit Decimal Newton iteration solved all nine equations near that
   scout. The twelve small core correlations were then replaced by the
   exact common rational 10^-8 and the active weights refined again.
   Those terminating rational coordinates became input to the full-source
   directed checker. The checker, not the optimization, proves existence.

The successful root has one substantial edge between unequal core
weights, together with the twelve positive weak core edges and all hub
edges. Its weighted adjacent-spin covariance is greater than 1/60.
The construction therefore changes the correlated observable law; it is
not obtained by merely attaching an unobserved independent graph.

The original floating searches remain in the local research workspace and
are not dependencies of this compact proof packet. No failure above rules
out an entire architecture. No approximate next-moment improvement is
promoted to a theorem. The accepted new result is exactly the connected
degree-18 realization, with the nonzero degree-20 discrepancy recorded.
