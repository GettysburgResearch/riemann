# Xi source and derivative transport investigation

Status: exploratory mathematics; independently review before integration.
Scope: exact synthetic source obstructions and a quantitative companion-sector
certificate. RH remains unproved.
Baseline: `f99d9e3908dde4865377c75d9ca051c1f545bf4f`.
Exact inherited sources: `FORMAL_STATUS.md`,
`research/integrated/CURRENT_RESULTS.md#xi`,
`reviews/A/FINAL_AUDIT.md#f01`–`#f03`, and
`reviews/A/supplement/REPORT.md#S06`.

The derivative results use the real-zero coordinate
`Xi(z)=xi(1/2+iz)`, not the horizontal coordinate `xi(1/2+z)` used by the
safe-axis Pick programme.

* [An exact adjacent-order obstruction](DERIVATIVE_COUNTEREXAMPLE.md): an even
  entire positive-frequency transform has a complete arbitrarily thin zero
  strip and globally real-rooted derivatives of every positive order, while
  its original function has nonreal zeros. Every frozen positive companion
  parameter still produces a lower-ray zero at order zero. The precise wrong
  extremum residue and ray-zero bounds are computed.
* [A quantitative source-to-companion certificate](COMPANION_SECTOR.md): a
  nonasymptotic error bound for `i E_(r,lambda_r)/E'_(r,lambda_r)` retains both
  reflected terms. It states exactly which moment and tilted-variance inputs
  certify an entire ray. Its adjacent-parameter drift law distinguishes a
  high-order band from descent to a fixed order.
* [A smooth theta-tail obstruction](THETA_TAIL_OBSTRUCTION.md): the high-order
  entry mechanism is stable under compact positive source perturbations, even
  when they create a nonreal zero. The perturbed density is smooth, strictly
  positive, and agrees exactly with a scalar multiple of the actual theta
  density above a finite cutoff. It is not the actual arithmetic theta source.
* [A positive theta-derived quartet](POSITIVE_THETA_QUARTET.md): an explicit
  differential operator gives a strictly positive complete source whose
  transform is actual Xi times one off-real quartet factor. It preserves the
  known zero strip, any finite zero census below the chosen quartet height,
  and the full zero-count asymptotic. The source positivity has a complete
  rational Bernstein certificate in `theta_quartet_certificate.json`.
* [Modular binding and local forward transport](MODULAR_BINDING_AND_TRANSPORT.md):
  the quartet modification can preserve the exact normalized Jacobi reflection
  and xi endpoint values as well. Its literal lattice Gaussian/Mellin–Euler
  identity fails. Explicit compact-domain and companion-error bounds state
  what a protected local source comparison can prove and which denominator
  estimates remain necessary.

The finite checks in `verify_derivative_controls.py` use exact rational
arithmetic and symbolic identities; they do not claim to certify actual xi
zeros or the smooth-source saddle theorem. `verification.json` records the
executed finite checks and their limits.

The source-obstruction subtree is an independent investigation of higher
Pick-packet inertia and contains its own source and validation boundaries.

Smallest remaining RH-facing gap: control the signed low-order transport for
the exact theta source, including all wrong extrema, pole/winding terms and
endpoints. Positive source mass, an unchanged theta tail, narrow zero strips,
and high-order entry alone do not supply that estimate.
