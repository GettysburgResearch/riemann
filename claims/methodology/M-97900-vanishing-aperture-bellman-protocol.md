# M-97900 — Protocol after the fixed-angle Bellman no-go

Methodology ID: `M-97900`  
Status: **SOURCE-FAITHFUL CLOSURE PROTOCOL**

A continuation must not attempt to iterate the repaired `P_61` interval with a
uniform positive scalar-to-mass angle. `R-97900` proves that mechanism
impossible.

The remaining legitimate attacks are:

1. **Euler-minus profile.** Prove `LBP67` directly:
   \[
   \prod_{p\in Q}(I-p^{-1/2}U_p)D_0^+(X,\lambda)\ge0.
   \]
2. **Root zero hinge.** Prove the root scalar `D^+(0)>=0` using the complete
   future-product quotient profile, without demanding a state-wise positive
   angle.
3. **Exact Lorenz separator search.** At each finite horizon test only `lambda=0`,
   target-capacity rays, and actual atom ratios. A negative value is an exact
   CPSL separator.
4. **Vanishing aperture.** If mass is retained, its aperture must depend on the
   installed prime set and tend to zero at least as fast as
   \[
   \prod_{p\in Q}(p-1)/(p+1).
   \]
   Such a profile is diagnostic until its exact finite error is controlled.

Required firewalls:

```text
no contracted child coefficient substituted for the raw coefficient;
no completed child replaced by a local current;
no fixed positive mass angle claimed invariant;
no finite quotient scan promoted to all-scale proof;
no NCBI/CPSL equivalence asserted;
no target cushion used at lambda=0.
```
