# Actual graded completion and its analytic loss

This continuation of PR769 defines the degreewise limit of the existing actual
constructible pole-clearing sources. It proves that the limit over F7 has Taylor
radius 1/sqrt(2), and over F49 radius 1/2, even though the finite-stage guaranteed
disks approach one. In the F49 case every finite stage is holomorphic on the unit
disk. An explicit fractional singularity, not a finite numerical trend, proves
the loss. The same actual cohomological operator retains trace-class radius1/2.

Read [the proof](MATHEMATICS.md), [preregistered targets](PREREGISTERED_TARGETS.md),
and [replay contract](REPLAY.md). The all-grade source identity, finite coefficient
stabilization and exact base-change substitution are kept separate from ordinary
Fredholm convergence. No RH or number-field transfer is claimed.

On 2026-08-31 the source-bound producer and all20 tests passed in ordinary and
optimized Python. Ruff passed. The execution records are retained in the root
six-hour audit directory. The measured Python working-set peak was below23MiB.
An independent draft proof read found no blocker; an exact-commit review follows
the scientific freeze. This frontdoor is not part of the bound proof packet.
