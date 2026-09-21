## BCP26: executed continuation of the Sylvester-inspired boundary route

**Proposed component proofs; RH and GRH remain open.** The new reading
entry is `standalone/2026-09-19-sylvester-boundary-execution/README.md`.

The earlier #903 sketch left its kernel unspecified and focused on the
square residual, which is zero in the reconstructed stage. This packet
studies the energy-bearing single-residual correction. Exact inversion
collapses a least-prime residual channel to a finite cutoff-pivot Euler
polynomial. Each output squarefree coefficient has one unique pivot;
every nonsquarefree channel coefficient cancels. The actual annular Gram,
signed mean and both completed A/F states are explicitly identified.

The natural raw pivot partition is not a benign positive decomposition.
A native semiprime rectangle proves a diagonal lower bound of order
Y/log^3 Y and positive ordered cross mass of order Y^2/log^4 Y, even
using coprime output integers. Thus this partition cannot support the
old positive-excess estimate. Mean-centering does not fix its diagonal.
This does not refute a coarser signed grouping or the native RH target.

Finite execution covers six full stages through 65,535, with 70,986
coefficient checks including overlaps and 1,964 Gram entries. Independent
trial factorization and 160-bit Stieltjes bounds check the producer's
80-bit enclosures by containment. At Y=255 the raw diagonal 14.49227 and
cross covariance -14.31242 yield the unchanged annular energy 0.179852.
This raw diagonal is worse than NSR26's bank regrouping; no numerical
norm improvement is claimed. RCB26's separate subpower theorem is preserved.

For #738, LFAMILY.md imports Burungale--Tian's exact central-rank-one
result for the CM cubic-twist family (not the original quadratic family),
derives the rank correction K_deflated=K_raw-r vv*, and checks a synthetic
masking control: raw 4/3 becomes -8/3 after correct deflation. The packet
also checks 14 auxiliary-prime examples, 12 cubic projectors and two
Fermat lifts exactly; eta_67 remains undetermined. No elliptic L-values,
CM integrals, heights or new zero computations are certified.

The authoring receipt is in VALIDATION.md. Publication must be accompanied
by the actual remote SHA and the publisher's own replay receipt; the
original authoring session did not have a working GitHub write path.
