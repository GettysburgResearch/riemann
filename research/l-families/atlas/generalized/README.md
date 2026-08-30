# Generalized L-object Gate-0 packets

Status: **proposed exact local mathematics; external novelty unreviewed**.

This directory contains bounded theorem and obstruction packets for issue
[#764](https://github.com/gfreund123/riemann/issues/764). It reuses the atlas
normalization and provenance conventions but does not extend the atlas into a
catalogue of generalized zeta functions.

The first packet is
[`NONINTEGRAL_LOCAL_POWER_RATIONALITY.md`](NONINTEGRAL_LOCAL_POWER_RATIONALITY.md).
It classifies rationality of one positive-chamber, determinant-one local
coefficient-power series. Here \(x>2\) is the hyperbolic, non-tempered
chamber, not the normalized tempered \(\mathrm{GL}_2\) trace chamber
\([-2,2]\). The result is local: it constructs no global Euler product,
completion, automorphic lift, or zero theorem, and it is not an automorphic
nonintegral-symmetric-power no-go theorem. Its inherited inputs are recorded
in the colocated
[sources manifest](nonintegral_local_power_rationality.sources.json).

The second packet is
[IRRATIONAL_ROTATION_ABSOLUTE_POWER_RATIONALITY.md](IRRATIONAL_ROTATION_ABSOLUTE_POWER_RATIONALITY.md).
For a determinant-one tempered recurrence with
\(\theta/\pi\notin\mathbb Q\), it proves that
\(\sum_r |u_r|^\lambda T^r\) is rational exactly for even nonnegative
integers \(\lambda=2m\), with minimal local order \(2m+1\). It treats
absolute powers rather than complex powers, excludes rational rotations,
and makes no global or novelty claim. Its inherited inputs and nearby
almost-periodic-series prior art are recorded in the colocated
[sources manifest](irrational_rotation_absolute_power_rationality.sources.json).
