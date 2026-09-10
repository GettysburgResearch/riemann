# Independent-review handoff: HC26

**Review requested for the component capture theorem, NOT for a completed RH
proof.** The exact remaining original premise is HC.OPEN, in Section 7.
An external reviewer should not be asked to invent or silently assume it.

## Claim separation

| Record | Scope and disposition proposed by the author |
|---|---|
| HC26.1 | Complete source small-value distribution and integrated logarithmic deficit; unconditional paper proof. |
| HC26.2 | Clipped outer inverse admits finite polynomials at a stretched-logarithmic rate; unconditional paper proof. |
| HC26.3 | Actual source and its full inner factor have the needed fractional regularity; no RH or simplicity hypothesis. |
| HC26.4 | Target-dependent finite correction rate to the intrinsic floor, uniform on the stated Sobolev/bounded target class. |
| HC26.5 | Exact-horizon compact inverse seeds satisfy that class with C(1+T)exp(T/2); rank exp(O(T^2)) pays removable error. |
| HC26.OPEN | Subexponential intrinsic minimum on unbounded horizons: UNPROVED, equivalent here to the missing RH conclusion. |

These are local packet labels, not allocations in the repository's canonical
claim-ID registry. No inherited verdict or main file is changed.

## Six decisive review checks

1. Section 2: verify the Euler--Maclaurin normalization, local disk count with
   multiplicity, the conversion of ordinate intervals to normalized circle
   measure, and the distribution-to-integrated-logarithm bound. In particular,
   a finite-Gram floor alone is NOT a substitute for the measure estimate.
2. Section 3: verify clipped logarithm regularity at boundary zeros and the
   Hilbert-transform step; the exponential Lipschitz bound is applied only in
   Re z>=-v. Holder uses O in H^3 and the inverse error in L6. No Sobolev algebra
   theorem at exponent below 1/2 is presumed.
3. Section 4: verify the absence of a singular inner factor, the fractional
   energy estimate for Blaschke products, the summability of every zero with
   multiplicity, and the regularity of P_+(conjugate(B)q). P_+ is NOT asserted
   bounded on L-infinity, and g is NOT asserted bounded.
4. Section 5: check both finite polynomial degrees, the two separate error
   terms, and Pythagoras. This is approximation to B g, not to g without B.
   The rate concerns squared excess above the closed-domain minimum.
5. Section 6: check the actual seed's compact BV boundary terms, its Cayley
   regularity bound with explicit dependence on T, and cancellation of the
   delay without assuming arbitrary backward-shift invariance. Verify the
   norm perturbation used to replace finite closed-domain vectors by compact
   L2 inputs. No uniform input bound is claimed.
6. Section 7: check the synthetic counterexample and the hypothetical-zero
   lower bound. Neither the measured small-value sets nor the rate to the
   floor proves that B is constant. That final missing assertion is not a
   review formality.

## Proof and implementation boundaries

The rate constants C,c are absolute for this fixed source; the proof shows
finiteness and constructs the dependence. C is not numerically evaluated.
Thus no executable numerical rank guarantee has been certified in this pass.
The asymptotic growth class is not a claim of efficient computation.

The analytic proof uses inner/outer factors to demonstrate existence of a
polynomial competitor. The implementation is the best finite ORIGINAL Gram
projection and needs no zeros or inner factor. There is no new high-rank
implementation or actual-source energy certificate in this packet.

The finite checker protects the supplied artifact inventory and reconstructs
its bounded examples. Its manifest is not a cryptographic trust root against
an adversary replacing both code and all hashes. Review must pin the final
publication commit and inspect code, proof and source normalization.
