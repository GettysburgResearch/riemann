# Corrections to the first #903 pass

Historical head: 67132424e3cbe35a94752581a5b5271ab8bfc56f.
Its five notes remain in Git history. This revision is explicit rather than
a silent promotion of those notes into tested mathematics.

1. **Executed scope.** The first pass supplied notes but no executable
   covariance calculation, local-field reproduction, or test report. This
   pass adds them; their outputs must not be attributed retrospectively.
2. **Mathematical rendering.** Backslashes were lost or interpreted as string
   escapes during the earlier upload. The formulas in all five notes and the
   PR description are repaired. New files are byte/hash checked.
3. **Wrong driver for the annulus.** The identity mu-N(g)=mu*e*e is valid,
   but e*e vanishes identically below (Y+1)^2. Describing those error collisions
   as the object generating the energy to be bounded in that same annulus
   was misleading. The relevant operator is g*e; it is now explicit.
4. **Incomplete source adapter.** Uncompleted g and capped completion c do
   not have interchangeable full harmonic energies. Equations (14)-(15)
   give the actual adapter to PCR26/RCB26's Q, with all source moments and
   above-endpoint products accounted for.
5. **Untested partition.** The prime/antichain partition was a proposal, not
   an established gain. Its naive coalesced large-prime diagonal is now
   proved to have a Y/log^2Y-scale obstruction on the native source itself.
   This is a revision of our strategy, not a defect in the Sylvester paper.
6. **Family scope.** CM cubic twists are an extension to, not an example of,
   #738's originally specified quadratic-twist family. Exact local fixtures,
   good-prime Euler algebra, global rank theorems, and numerical CM recognition
   are separately classified.

No failure is concealed by moving it into a renamed equivalent criterion.
The missing unbounded signed gain remains missing after these corrections.
