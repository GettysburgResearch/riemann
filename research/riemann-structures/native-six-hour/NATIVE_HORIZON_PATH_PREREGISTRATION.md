# Fixed higher-horizon source-path campaign

This campaign uses the explicit20-moment decoder in
ALL_HORIZON_THREE_PRIME_SOURCE_MOMENTS.md and the eight exact
quadratic cone tests in EIGHT_QUADRATIC_LAST_ACTIVATION_CONE.md.
It retains only the originally declared prime support2,3,5, but
retains EVERY prime power and ordered factor pair with nm<=H.

Calibration is H=25. After freezing that executable and its output,
the same executable runs the heldout H=30 and60 panels. No other
horizons, source masks, coefficient choices or starting points are
added in response to results. The index cap is60, record cap200,
physical-ratio cap100 and source-artifact cap8MiB per phase.

Each local coefficient is extracted from the authenticated primitive
(1-t)sqrt(1-z^2)+t sqrt(1-z). The twenty-moment decoder is applied
before physical-ratio collection. Fixed path controls are all six
axis orders, the diagonal, and the polygon through
(1/3,1/4,1/5),(2/3,3/4,2/5). Every control retains every ordered record.
H25 additionally reproduces the frozen complete source and original
three-coordinate planar Gram; a source mismatch stops the campaign.

The original Gamma ratio-pair matrix, including1/sqrt(abcd), is
constructed once per horizon. The physical source has a fixed
twenty-moment readout, while the last-activation restriction has
coordinates(A,B,C/2). Compute its3x3 Gram and the20x4 couplings of
all source directions to its reference and three variation fields.
No replacement norm, diagonal norm or omitted physical cross term
is used. The matrix digest and complete rational source columns
remain auditable without serializing every duplicate kernel entry.

The same sixteen starts,32 floating Newton steps and16 step halvings
as the frozen H25 experiment propose centers only. The proposed path
is v=clip(lambda+mu*u), followed by w. Its original-metric equations
are independently certified by outward2^-512 rational arithmetic,
a fixed radius2^-30 box, an invertible rational preconditioner and
strict contraction/Krawczyk inclusion. The box must lie inside one
strict clipping regime. Pure interval/geometry utilities may be
imported from authenticated frozen code; no source or cap is patched.

At each certified root the FULL twenty-coordinate gradient is used
in the eight quadratic cone polynomials. Nonnegative exact minima
of their coefficientwise lower envelopes certify PASS. A negative
minimum of an upper envelope gives a rational witness for failure
of that sufficient cone. All other cases remain UNKNOWN. A failed
cone does not disprove a path optimum. A root with positive planar
quadratic coefficient still certifies its last-activation subclass
minimum; only PASS certifies a complete all-path minimum.

All sixteen starts and all refusals are retained. Every distinct
exact rational center with a root certificate is independently
integrated through all source records and its physical energy.
Repeated centers may share one stored witness; their attempt indices
are not deleted. There is no floating acceptance decision, numerical
quadrature, nonlinear fit of source coefficients, or new prime scout.
The intended worker memory is below128MiB, with coordinator execution
subject to the existing reserve guard.

Any result is about the complete stated primitive source at its
declared horizon. No full retained-gamma identification or automatic
persistence to every physical horizon is claimed.
