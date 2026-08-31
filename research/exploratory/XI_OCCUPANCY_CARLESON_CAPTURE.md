# Local crowding, weighted Hardy sampling, and actual-Xi capture

Status: PREREGISTERED THEOREM/EXACT-CONTROL TARGET, before evaluation.
Base: `a7479e85fdc2a464cdc753021435cfef7a1f3910` (LB).
Scope: the literal boundary-dx Hardy metric; fixed lambda>0; bounded-height
surviving denominator nodes. RH, innerness, and cofinal alignment are not proved.

The proposed bridge replaces LB3's unpaid uniform unweighted Bessel hypothesis
by an explicit per-unit-cell Carleson crowding cost. This is a weighting of
test vectors, NOT a change of physical Hilbert norm or source observation.

Preregistered exact controls:

1. For every N=1,...,16, test two declared rational cell families:
   dispersed x_j=1/4+j/[2(N+1)], y_j=1/(64N^2), and
   crowded x_j=1/4+j/[64N^2(N+1)], y_j=1/4, j=1,...,N.
   Predictions: exact cell Carleson costs respectively1 andN.
2. Compare the polynomial-size endpoint/height enumeration with an independent
   complete nonempty-subset formula on all declared families N<=8 and a fixed
   mixed-height four-node control. No random or additional fitted families.
3. Exhaust rational test intervals with left endpoint j/8, -8<=j<=16,
   and length m/8, 1<=m<=24, on a fixed three-cell union of the declared
   families. Verify the universal normalized box bound3|I|, retaining all rows.
4. Verify exact crowded-kernel Rayleigh bounds and dyadic sparse-survey
   summability controls. All numeric output is rational strings or integers.

The all-height Jensen bound and the infinite Carleson/capture implication are
written analytic arguments. The finite controls do not machine-certify them.
No actual-Xi zero is newly evaluated in this packet.
