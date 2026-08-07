# Integration handoff — full-problem global attack

Frozen live heads used for reconciliation:

- PR #165: `de31a1df1f6011f306eb3f00ff6ba212a1421d09`;
- PR #216: `b76eef1b769584aa9d66d082bfc6634126f986a2`;
- PR #217: `a1e3e7b3838a9d5ab837abc44cc133c17da10ffa`.

`T-15411`, `T-15412`, `L-15439`, the experiment, and the continuation report
are additive follow-ups for PR #165. `L-21702` is logically a follow-up to PR
#217 and should preferably be published there, or clearly marked as a
cross-branch proposed dependency if retained on #165.

Proposed new claims:

- `T-15411`: square interval Weil compression;
- `T-15412`: dyadic Chebyshev square-function exponent;
- `L-15439`: critical-load deposition transport and one-sided queue energy;
- `L-21702`: uniform parabolic Hausdorff saddle positivity.

Exact synthetic regression:

- `experiments/X-15414-global-rank-one-attack/`.

Primary review order:

1. audit the centered Weil polarization and inherited square-sampling normalization in `T-15411`;
2. audit the one-sided exponential Hardy `H2` transfer and the delay inverse in `T-15412`;
3. audit the curvature calculation, queue scaling, and Jensen allocation in `L-15439`;
4. audit the uniform Riemann–von Mangoldt and displaced-tail estimates in `L-21702`;
5. rerun the exact synthetic checker;
6. compare the new global coordinates with PRs #216 and #217 before assigning registry status.

Status boundary:

- all new claims are PROPOSED pending independent review;
- the checker proves synthetic finite algebra only;
- no RH resolution is claimed.

Parallel-work compatibility:

- do not overwrite the live `L-15433`--`L-15438` files or the existing
  `2026-08-07-full-problem-global-attack.md` report;
- the continuation report is
  `reports/gpt56-05-l/2026-08-07-rank-one-dyadic-critical-load-hausdorff-attack.md`;
- the new prime-side coordinates complement the endpoint-collapse and
  completed-xi total-positivity coordinates already at the frozen PR #165 head.
