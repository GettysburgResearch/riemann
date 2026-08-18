# Hostile review specification

Review in this order:

1. `L-97500`, especially the sign in `g=b+(T-R)f`.
2. `R-97500` on the two-node chain.
3. `L-97501`, checking that `(r-t)+t=r` occurs in the paired source before observation.
4. `L-97502`, checking that current and recursive exposure sum to raw exposure.
5. `T-97500`, checking the orientation of `c>=Tc` and the finite M-matrix identity.
6. The exact replay and mutation suite.

Reject the packet at the first erased swap, omitted leftover coefficient,
replacement of raw exposure by contracted exposure, or promotion of `NCBI67`
to a proved theorem.
