# The first ordered dual menu fails exactly

This is a negative theorem about one proposed support certificate, not
about the ordered candidate itself. The physical input is frozen at
`a454106bd685d618f61231549e6fd99bf5b5a1ad`; its L96 Gram capture has Git
blob `78a5a8ae10b065bb32bfe114b9ac3063bf0ed0f1`. The variational dependency
and normalization are those recorded in `variational_REPLAY.md`.

The five-dimensional ordered-face equations have a unique root in the
directed radius-`10^-8` box about

\[
(-0.08233305700654603,1.1226168381295267,
 -0.5082335933099136,0.5775184399712018,
 0.9383761444256082).
\]

Its Krawczyk contraction is below `3.872e-6`; the lower-clipping and
switch inequalities are strict. The path has directed physical energy
near `179.358344`, but no global-optimality assertion follows from that
number.

For the potential

\[
 \Phi_K=\theta_{10}u^2v+wR-Kuw(1-v),
\]

the necessary support inequality in the early branch is
`A_K(u,v,w)>=q_v(u,f(u))`. The following rational points lie strictly
before the true switch and violate it:

| K | `(u,v,w)` | certified gap interval, approximately |
|---|---|---|
| 1 | `(15/16,31/32,1/32)` | `[-7.9950e-4,-7.9942e-4]` |
| 2 | `(15/16,501/512,21/1024)` | `[-9.0780e-4,-9.0770e-4]` |
| 3 | `(15/16,503/512,5/256)` | `[-5.0750e-4,-5.0738e-4]` |

Every upper endpoint is strictly negative in exact Arb-directed rational
arithmetic. Thus all three registered linear potentials fail the global
inequality. The initial 33-cube grid missed the narrow wells for K=2 and
K=3; this is precisely why `variational_ORDERED_DUAL_THEOREM.md` requires
analytic minimization in `w` and a continuum polynomial certificate.

The certificate authenticates the physical Gram and the already reviewed
variational base before import, independently encloses the five-variable
root, and preserves every rational witness. Its final `--write`, `--check`
and optimized `--check` runs all pass. It does not establish a legal
descent from the ordered path, rule out a nonlinear potential, or identify
the global three-coordinate optimizer.
